"""Ingest stage: list and download the papers of one conference venue.

Sources
  - proceedings.iclr.cc / proceedings.neurips.cc (listing pages, per track)
  - proceedings.mlr.press (PMLR volumes, for ICML and similar; see also
    ``aiconstructlexis.ingest.pmlr`` when the volume number is known)
  - the OpenReview API (used when no formal proceedings site exists)

This module also holds the helpers shared by every ingest module
(``anthology``, ``pmlr``): the no-overwrite guard, seeded sampling, PDF
download and paper-list writing.

Inputs
  conference and year; for proceedings.cc venues an optional track selection;
  for PMLR an optional volume number.

Outputs
  A paper-list JSON (``out_json``) and the PDFs under ``pdf_dir``. The list
  holds one dict per paper:

  name      title
  url       PDF url
  path      local PDF path. Set for every entry selected for download: all
            entries normally, only the sampled ones when a sample size is
            given. An entry whose download failed carries ``download_error``
            instead of ``path``, so a missing PDF is never read downstream as
            an empty paper.
  track     proceedings.cc track (Conference, Datasets_and_Benchmarks_Track, ...)
  sampled   only when sampling: true for the entries in the seeded sample

Rules
  - Lists are never overwritten: an existing list (or sample list) stops the
    run before anything is fetched, unless ``force`` is set.
  - With a sample size N and a seed S the full list is written to ``out_json``
    and the sampled entries (the ones with a PDF) also go to
    ``<out_json stem>.sample.json``, which can be screened on its own.
  - Sampling is seeded over the sorted paper URLs, so the sample does not
    depend on the order of the listing page.
  - Two papers never share one PDF file: repeated title slugs get a numeric
    suffix.

Command line
  python -m aiconstructlexis.ingest.proceedings --conference iclr --year 2026 --out work/iclr26/papers.json
  python -m aiconstructlexis.ingest.proceedings --conference neurips --year 2025 --out ... --tracks main,db
  python -m aiconstructlexis.ingest.proceedings --conference neurips --year 2025 --out ... --sample 50 --seed 0
  python -m aiconstructlexis.ingest.proceedings --conference icml --year 2026 --out ... --source pmlr --pmlr-volume 306
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Callable, Iterable, List, Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from tqdm.auto import tqdm

from aiconstructlexis.util.logging import setup_logging

log = logging.getLogger(__name__)

SLEEP = 0.25
HEADERS = {"User-Agent": "Mozilla/5.0 (paper-list downloader)"}
MIN_PDF_BYTES = 1000


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.ASCII)
    return re.sub(r"[-\s]+", "_", text.strip())[:120]


def clean_text(text: str) -> str:
    """Collapse whitespace without gluing words that sit in separate tags."""
    return " ".join((text or "").split())


def http_get(url: str, timeout: int = 60, retries: int = 3) -> requests.Response:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            r = requests.get(url, timeout=timeout, headers=HEADERS)
            r.raise_for_status()
            return r
        except Exception as e:  # network hiccup or 5xx
            last = e
            time.sleep(1.0 * (attempt + 1))
    raise RuntimeError(f"GET {url} failed: {last}")


def fetch_html(url: str) -> str:
    return http_get(url).text


# --- shared: overwrite guard, sampling, download, writing ---

def sample_list_path(out_path: Path) -> Path:
    return Path(out_path).with_name(Path(out_path).stem + ".sample.json")


def default_pdf_dir(out_json: Path) -> Path:
    """PDF directory used when none is given: the list path without its suffix
    (``work/iclr26/papers.json`` -> ``work/iclr26/papers/``)."""
    out_json = Path(out_json)
    return out_json.with_suffix("") if out_json.suffix else out_json.with_name(out_json.name + "_pdfs")


def guard_lists(paths: Iterable[Path], force: bool) -> None:
    """Raise FileExistsError before any network work if a list would be overwritten."""
    existing = [Path(p) for p in paths if Path(p).exists()]
    if existing and not force:
        names = ", ".join(str(p) for p in existing)
        raise FileExistsError(
            f"Refusing to overwrite existing list(s): {names}. "
            f"Pass force=True (--force) to replace them, or write to another path."
        )


def write_list(path: Path, entries: list, force: bool) -> None:
    """Write a paper list. Without force the file must not exist (exclusive create)."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(entries, indent=2, ensure_ascii=False)
    if not force:
        with open(path, "x", encoding="utf-8") as f:
            f.write(text)
        return
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def select_sample(entries: list, n: int, seed: int, key: str = "url") -> set:
    """Seeded sample of entry keys. Keys are sorted first, so the sample does
    not depend on the order the listing page happens to use."""
    keys = sorted({e[key] for e in entries})
    if n >= len(keys):
        return set(keys)
    return set(random.Random(seed).sample(keys, n))


def assign_paths(entries: list, pdf_dir: Path,
                 stem: Callable[[dict], str] = lambda e: slugify(e["name"])) -> None:
    """Set e['path'] to pdf_dir/<stem>.pdf; repeated stems get a numeric suffix so
    two papers never share one PDF file."""
    used: dict[str, int] = {}
    for e in entries:
        s = stem(e) or "paper"
        n = used.get(s.lower(), 0)
        used[s.lower()] = n + 1
        name = s if n == 0 else f"{s}__{n + 1}"
        e["path"] = str(Path(pdf_dir) / f"{name}.pdf")


def _is_pdf(path: Path) -> bool:
    try:
        with open(path, "rb") as f:
            return f.read(5) == b"%PDF-"
    except OSError:
        return False


def pdf_ok(path: Path) -> bool:
    path = Path(path)
    return path.is_file() and path.stat().st_size > MIN_PDF_BYTES and _is_pdf(path)


def download_one(url: str, path: Path, retries: int = 3, sleep: float = 0.0,
                 session: requests.Session | None = None) -> Optional[str]:
    """Download url to path. Returns None on success, else an error message."""
    path = Path(path)
    if pdf_ok(path):
        return None
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_name(path.name + ".part")
    getter = session or requests
    last = ""
    for attempt in range(retries):
        try:
            with getter.get(url, stream=True, timeout=60, headers=HEADERS) as r:
                r.raise_for_status()
                with open(part, "wb") as f:
                    for chunk in r.iter_content(8192):
                        if chunk:
                            f.write(chunk)
            if not (part.stat().st_size > MIN_PDF_BYTES and _is_pdf(part)):
                raise ValueError("response is not a PDF")
            os.replace(part, path)
            if sleep:
                time.sleep(sleep)
            return None
        except Exception as e:
            last = str(e)[:200]
            time.sleep(0.5 * (attempt + 1))
    part.unlink(missing_ok=True)
    return last or "download failed"


def download_pdfs(entries: list, workers: int = 1, sleep: float = 0.0,
                  fetch: Callable[[str, Path], Optional[str]] | None = None) -> dict:
    """Download every entry's PDF to its path. Returns {url: error or None}."""
    results: dict = {}
    if not entries:
        return results
    with requests.Session() as session:
        def one(e):
            if fetch is not None:
                return fetch(e["url"], Path(e["path"]))
            return download_one(e["url"], Path(e["path"]), sleep=sleep, session=session)

        with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
            futures = {pool.submit(one, e): e for e in entries}
            for fut in tqdm(as_completed(futures), total=len(futures),
                            unit="paper", desc="Downloading"):
                e = futures[fut]
                try:
                    err = fut.result()
                except Exception as ex:  # defensive: never lose the whole run
                    err = str(ex)[:200]
                results[e["url"]] = err
                if err:
                    log.warning("download failed: %s: %s", e["name"][:60], err)
    return results


def finish(entries: list, out_path: Path, *, metadata_only: bool,
           sample: Optional[int], seed: int, force: bool, workers: int = 1,
           sleep: float = 0.0,
           fetch: Callable[[str, Path], Optional[str]] | None = None) -> dict:
    """Sample, download and write the list(s). Entries must already carry a
    planned `path`. Returns a small summary dict."""
    out_path = Path(out_path)
    if sample is not None:
        chosen = select_sample(entries, sample, seed)
        for e in entries:
            e["sampled"] = e["url"] in chosen
        selected = [e for e in entries if e["sampled"]]
    else:
        selected = list(entries)
    selected_urls = {e["url"] for e in selected}
    for e in entries:
        if e["url"] not in selected_urls:
            e.pop("path", None)

    errors: dict = {}
    if not metadata_only:
        errors = download_pdfs(selected, workers=workers, sleep=sleep, fetch=fetch)
        for e in selected:
            err = errors.get(e["url"])
            if err:
                e.pop("path", None)
                e["download_error"] = err

    write_list(out_path, entries, force)
    summary = {
        "listed": len(entries),
        "selected": len(selected),
        "downloaded": 0 if metadata_only else sum(1 for e in selected if "path" in e),
        "failed": sum(1 for v in errors.values() if v),
        "metadata_only": metadata_only,
        "list": str(out_path),
    }
    if sample is not None:
        sp = sample_list_path(out_path)
        write_list(sp, [e for e in selected if "path" in e], force)
        summary["sample_list"] = str(sp)
        summary["seed"] = seed
    return summary


def add_common_args(ap: argparse.ArgumentParser, default_workers: int = 1) -> None:
    ap.add_argument("--out", type=Path, required=True,
                    help="Paper-list JSON to write")
    ap.add_argument("--pdf-dir", type=Path, default=None,
                    help="PDF directory (default: the list path without its .json suffix)")
    ap.add_argument("--metadata-only", action="store_true",
                    help="Write the list only, download no PDFs")
    ap.add_argument("--force", action="store_true",
                    help="Overwrite an existing list (default: refuse)")
    ap.add_argument("--sample", type=int, default=None, metavar="N",
                    help="List everything, download PDFs for a seeded sample of N papers")
    ap.add_argument("--seed", type=int, default=0, help="Seed for --sample (default 0)")
    ap.add_argument("--workers", "--max-workers", dest="workers", type=int,
                    default=default_workers, help="Parallel PDF downloads")
    ap.add_argument("--log-dir", default="logs", help="Directory for the run log (default: logs)")


def resolve_outputs(out_json: str | Path, pdf_dir: str | Path | None) -> tuple[Path, Path]:
    out = Path(out_json)
    return out, (Path(pdf_dir) if pdf_dir is not None else default_pdf_dir(out))


def guard_for(out: Path, sample: Optional[int], force: bool) -> None:
    paths = [out] + ([sample_list_path(out)] if sample is not None else [])
    guard_lists(paths, force)


def log_summary(summary: dict, pdf_dir: Path) -> None:
    if summary.get("metadata_only"):
        log.info("Listed %d papers (metadata only; %d entries carry a planned path, "
                 "no PDFs downloaded)", summary["listed"], summary["selected"])
    else:
        log.info("Listed %d papers; selected %d for download; downloaded %d; failed %d",
                 summary["listed"], summary["selected"], summary["downloaded"], summary["failed"])
    log.info("List -> %s", summary["list"])
    if "sample_list" in summary:
        log.info("Sample list (seed %s) -> %s", summary["seed"], summary["sample_list"])
    if summary["downloaded"]:
        log.info("PDFs -> %s", pdf_dir)


def run_cli_main(fn: Callable[[], Path]) -> int:
    """Run a downloader for the command line: map the library exceptions to an
    exit status with a one-line message."""
    try:
        fn()
    except FileExistsError as e:
        raise SystemExit(str(e))
    except (RuntimeError, ValueError) as e:
        log.error("%s", e)
        return 1
    return 0


# --- proceedings.<conf>.cc listing pages (ICLR, NeurIPS) ---

HASH_RE = re.compile(r"/paper_files/paper/(\d{4})/hash/([0-9a-f]+)-Abstract-([A-Za-z0-9_]+)\.html$")

TRACK_ALIASES = {
    "main": "Conference", "conference": "Conference",
    "db": "Datasets_and_Benchmarks_Track", "datasets": "Datasets_and_Benchmarks_Track",
    "datasets_and_benchmarks": "Datasets_and_Benchmarks_Track",
    "datasets_and_benchmarks_track": "Datasets_and_Benchmarks_Track",
    "position": "Position_Paper_Track", "position_paper_track": "Position_Paper_Track",
    "creative": "Creative_AI_Track", "creative_ai": "Creative_AI_Track",
    "creative_ai_track": "Creative_AI_Track",
}
# NeurIPS: the main conference plus the Datasets and Benchmarks track by default;
# other conferences keep every track.
DEFAULT_TRACKS = {"neurips": ["Conference", "Datasets_and_Benchmarks_Track"]}


def parse_tracks(spec: str | Iterable[str] | None, conf: str) -> Optional[List[str]]:
    """Track selection for proceedings.<conf>.cc. ``spec`` is a comma-separated
    string, a list of track names or aliases, or None (the conference default).
    The string "all" keeps every track. A returned None means keep every track."""
    if spec is None:
        return DEFAULT_TRACKS.get(conf)
    if isinstance(spec, str):
        if spec.strip().lower() == "all":
            return None
        parts = spec.split(",")
    else:
        parts = list(spec)
    out = []
    for t in parts:
        t = t.strip()
        if t:
            out.append(TRACK_ALIASES.get(t.lower(), t))
    return out


def parse_proceedings_page(html: str, base_url: str) -> tuple[list, list]:
    """Return ([{name, url, track}], [see-also page urls]) for one listing page."""
    soup = BeautifulSoup(html, "html.parser")
    papers = []
    for a in soup.find_all("a", href=True):
        href = urljoin(base_url, a["href"])
        m = HASH_RE.search(href)
        if not m:
            continue
        pdf = (href.replace("/hash/", "/file/")
                   .replace("-Abstract-", "-Paper-")
                   .replace(".html", ".pdf"))
        papers.append({"name": clean_text(a.get_text()), "url": pdf, "track": m.group(3)})
    see_also = [urljoin(base_url, a["href"])
                for p in soup.select("p.book-see-also") for a in p.find_all("a", href=True)]
    return papers, see_also


def list_proceedings_cc(conf: str, year: int, tracks: Optional[List[str]] = None,
                        fetch: Callable[[str], str] = fetch_html) -> list:
    """All papers of a proceedings.<conf>.cc year, following the "See also" links:
    a year page may hold one book and link to the others (for example a Creative
    AI book linking to the Main Conference book, which also carries the Datasets
    and Benchmarks and Position Paper tracks). Pages are de-duplicated by URL and
    papers by PDF URL."""
    host = f"https://proceedings.{conf}.cc"
    start = f"{host}/paper_files/paper/{year}"
    year_prefix = f"{host}/paper_files/paper/{year}"
    queue, seen_pages = [start], set()
    by_url: dict = {}
    while queue:
        page = queue.pop(0).rstrip("/")
        if page in seen_pages:
            continue
        seen_pages.add(page)
        papers, see_also = parse_proceedings_page(fetch(page), page + "/")
        for p in papers:
            by_url.setdefault(p["url"], p)
        queue += [u for u in see_also if u.rstrip("/").startswith(year_prefix)
                  and u.rstrip("/") not in seen_pages]
    papers = list(by_url.values())
    counts: dict = {}
    for p in papers:
        counts[p["track"]] = counts.get(p["track"], 0) + 1
    log.info("proceedings.%s.cc %d: %d page(s), tracks %s", conf, year, len(seen_pages), counts)
    if tracks is not None and papers:
        unknown = [t for t in tracks if t not in counts]
        if unknown:
            raise ValueError(f"Track(s) {unknown} not on proceedings.{conf}.cc {year}; "
                             f"available: {sorted(counts)}")
        papers = [p for p in papers if p["track"] in tracks]
    return papers


# --- PMLR volume index (ICML, AISTATS, ...) ---

def pmlr_volume_for(conf: str, year: int) -> int | None:
    idx = http_get("https://proceedings.mlr.press/").text
    soup = BeautifulSoup(idx, "html.parser")
    patt_conf = re.compile(conf, re.I)
    patt_year = re.compile(str(year))
    for li in soup.select("ul.list-unstyled > li"):
        a = li.find("a", href=True)
        if not a:
            continue
        if patt_conf.search(a.text) and patt_year.search(a.text):
            m = re.search(r"/v(\d+)/?$", a["href"])
            if m:
                return int(m.group(1))
    return None


def parse_pmlr_index(html: str) -> list:
    """[{name, url}] for every paper on a PMLR volume index page."""
    soup = BeautifulSoup(html, "html.parser")
    papers = []
    for div in soup.select("div.paper"):
        title_el = div.select_one("p.title")
        pdf_el = div.select_one("p.links a[href$='.pdf']")
        if not (title_el and pdf_el):
            continue
        pdf = pdf_el["href"]
        if not pdf.startswith("http"):
            pdf = f"https://proceedings.mlr.press{pdf}"
        papers.append({"name": clean_text(title_el.get_text()), "url": pdf})
    return papers


def list_pmlr(conf: str, year: int, volume: int | None = None) -> list:
    vol = volume or pmlr_volume_for(conf, year)
    if vol is None:
        return []
    return parse_pmlr_index(http_get(f"https://proceedings.mlr.press/v{vol}/").text)


# --- OpenReview API (when no proceedings site exists) ---

_VENUE_ACCEPTED = re.compile(r"accept|poster|spotlight|oral", re.I)
_VENUE_NOT_ACCEPTED = re.compile(r"submitted to|withdrawn|rejected|desk", re.I)


def venue_string_accepted(venue: str) -> bool:
    """Whether an OpenReview ``venue`` string names an accepted paper.

    Used as the last fallback after the decision replies and ``venueid``. Accepted
    strings name a presentation format or the decision ("ICLR 2025 Poster", "Accept
    (oral)"); the venue string also carries the conference and year for papers that
    were never accepted ("Submitted to ICLR 2025", "ICLR 2025 Conference Withdrawn
    Submission", "ICLR 2025 Conference Desk Rejected Submission"), so those are
    refused whatever else they contain.
    """
    if _VENUE_NOT_ACCEPTED.search(venue):
        return False
    return bool(_VENUE_ACCEPTED.search(venue))


def list_openreview(conf: str, year: int) -> list:
    """List accepted papers through the OpenReview API (api2.openreview.net).
    Needs the optional ``openreview-py`` package."""
    import openreview

    venue_map = {
        "icml": f"ICML.cc/{year}/Conference",
        "iclr": f"ICLR.cc/{year}/Conference",
        "neurips": f"NeurIPS.cc/{year}/Conference",
    }
    venue_id = venue_map.get(conf.lower())
    if not venue_id:
        raise ValueError(
            f"Unknown conference '{conf}' for OpenReview. "
            f"Supported: {list(venue_map.keys())}"
        )

    client = openreview.api.OpenReviewClient(
        baseurl="https://api2.openreview.net"
    )

    submissions = client.get_all_notes(
        invitation=f"{venue_id}/-/Submission",
        details="directReplies",
    )
    log.info("OpenReview: fetched %d submissions", len(submissions))

    accepted = []
    for note in submissions:
        decisions = [
            r for r in (note.details.get("directReplies") or [])
            if "Decision" in (r.get("invitation") or "")
            or "acceptance" in (r.get("invitation") or "").lower()
        ]
        is_accepted = False
        for d in decisions:
            content = d.get("content", {})
            dec_val = content.get("decision", {})
            if isinstance(dec_val, dict):
                dec_val = dec_val.get("value", "")
            if isinstance(dec_val, str) and "accept" in dec_val.lower():
                is_accepted = True
                break

        if not is_accepted:
            venueid = (note.content or {}).get("venueid", {})
            if isinstance(venueid, dict):
                venueid = venueid.get("value", "")
            if isinstance(venueid, str) and "accept" in venueid.lower():
                is_accepted = True

        if not is_accepted:
            venue = (note.content or {}).get("venue", {})
            if isinstance(venue, dict):
                venue = venue.get("value", "")
            if isinstance(venue, str) and venue_string_accepted(venue):
                is_accepted = True

        if is_accepted:
            title_field = (note.content or {}).get("title", {})
            if isinstance(title_field, dict):
                title = title_field.get("value", "Untitled")
            else:
                title = str(title_field) if title_field else "Untitled"
            accepted.append({"name": title,
                             "url": f"https://openreview.net/pdf?id={note.id}"})

    return accepted


# --- entry point ---

SOURCES = ("auto", "proceedings", "pmlr", "openreview")


def list_venue(conference: str, year: int, source: str = "auto",
               tracks: Optional[List[str]] = None, pmlr_volume: int | None = None) -> list:
    """[{name, url, ...}] for a venue from the chosen source. With "auto",
    ICLR and NeurIPS are read from proceedings.<conf>.cc, other conferences
    from PMLR, and OpenReview is tried when the listing is empty."""
    conf = conference.lower()
    if source not in SOURCES:
        raise ValueError(f"unknown source {source!r}; choose one of {SOURCES}")
    papers: list = []
    if source == "auto":
        if conf in {"neurips", "iclr"}:
            log.info("Trying proceedings.%s.cc ...", conf)
            papers = list_proceedings_cc(conf, year, tracks)
        if not papers and conf not in {"neurips", "iclr"}:
            log.info("Trying PMLR ...")
            papers = list_pmlr(conf, year, pmlr_volume)
        if not papers:
            log.info("Falling back to the OpenReview API ...")
            papers = list_openreview(conf, year)
    elif source == "proceedings":
        papers = list_proceedings_cc(conf, year, tracks)
    elif source == "pmlr":
        papers = list_pmlr(conf, year, pmlr_volume)
    elif source == "openreview":
        papers = list_openreview(conf, year)
    return papers


def download_venue(conference: str, year: int, out_json: str | Path,
                   pdf_dir: str | Path | None = None, *,
                   source: str = "auto", tracks: str | Iterable[str] | None = None,
                   pmlr_volume: int | None = None, metadata_only: bool = False,
                   sample: int | None = None, seed: int = 0, force: bool = False,
                   workers: int = 1) -> Path:
    """List one venue, download its PDFs to ``pdf_dir`` and write the paper
    list to ``out_json``. Returns the path of the list written.

    ``tracks`` applies to proceedings.<conf>.cc venues (see ``parse_tracks``);
    ``pmlr_volume`` to PMLR. ``pdf_dir`` defaults to ``default_pdf_dir(out_json)``.
    Raises FileExistsError when the list exists and ``force`` is false,
    ValueError for an unknown track or source, and RuntimeError when no paper
    is found or a page cannot be fetched."""
    conf = conference.lower()
    out, pdfs = resolve_outputs(out_json, pdf_dir)
    guard_for(out, sample, force)
    track_list = parse_tracks(tracks, conf)

    papers = list_venue(conf, year, source=source, tracks=track_list, pmlr_volume=pmlr_volume)
    if not papers:
        raise RuntimeError(f"No papers found for {conf.upper()} {year}")

    log.info("Found %d papers for %s %d", len(papers), conf.upper(), year)
    assign_paths(papers, pdfs)
    summary = finish(papers, out, metadata_only=metadata_only, sample=sample,
                     seed=seed, force=force, workers=workers, sleep=SLEEP)
    log_summary(summary, pdfs)
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="List one conference venue, download its PDFs and write the paper list"
    )
    parser.add_argument("--conference", required=True, help="neurips, iclr, icml, ...")
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--source", choices=list(SOURCES), default="auto",
                        help="Where to list the papers (default: auto-detect)")
    parser.add_argument(
        "--tracks", default=None,
        help="proceedings.cc tracks to keep, comma-separated, or 'all'. Aliases: "
             "main, db, position, creative. Default: NeurIPS main + db; other "
             "conferences all tracks."
    )
    parser.add_argument("--pmlr-volume", type=int, default=None,
                        help="PMLR volume number (skips the volume lookup)")
    add_common_args(parser, default_workers=1)
    args = parser.parse_args(argv)
    setup_logging(run_name="ingest_proceedings", log_dir=args.log_dir)

    return run_cli_main(lambda: download_venue(
        args.conference, args.year, args.out, args.pdf_dir, source=args.source,
        tracks=args.tracks, pmlr_volume=args.pmlr_volume, metadata_only=args.metadata_only,
        sample=args.sample, seed=args.seed, force=args.force, workers=args.workers))


if __name__ == "__main__":
    sys.exit(main())
