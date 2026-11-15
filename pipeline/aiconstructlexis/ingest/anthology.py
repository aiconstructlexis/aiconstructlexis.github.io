"""Ingest stage: list and download the main-conference papers of an ACL Anthology venue.

Inputs
  A venue (acl, emnlp, naacl) and year, or an Anthology volume id such as
  ``2026.acl-long``. Only the primary proceedings volume is read (the acl-long and
  naacl-long long-paper volumes, emnlp-main); Findings, workshop and other companion
  volumes are not.

Outputs
  A paper-list JSON (``out_json``; see ``aiconstructlexis.ingest.proceedings``
  for the schema, sampling and the no-overwrite rule) and the PDFs under
  ``pdf_dir``, one ``<paper_id>.pdf`` per paper. Each entry carries ``name``,
  ``url``, ``paper_id`` and ``path``.

Rules
  - Within the volume, the front matter (paper .0), the whole-volume PDF and
    every ``/attachments/`` file (for example responsible-NLP checklists) are
    skipped; only numbered papers with their own PDF are listed.
  - Title pairing: on a volume page each paper is one block, and the PDF badge
    comes before the paper's own ``<strong>`` title. Each title is therefore
    read from its own block, never from the nearest preceding title: the
    block's title link (``/<id>/``) and its PDF badge (``<id>.pdf``) must name
    the same Anthology id, or parsing stops with an error.
  - Title text is joined without stripping each tag, so
    ``for <span>E</span>-commerce`` stays ``for E-commerce``.
  - The parsed (paper_id, title) pairs are cross-checked against the volume
    BibTeX (``https://aclanthology.org/volumes/<vol>.bib``, optionally cached
    under ``bib_cache``); any disagreement stops the run unless the check is
    switched off.

Command line
  python -m aiconstructlexis.ingest.anthology --venue acl --year 2026 --out work/acl26/papers.json
  python -m aiconstructlexis.ingest.anthology --venue emnlp --year 2026 --out ... --metadata-only
  python -m aiconstructlexis.ingest.anthology --volume 2026.acl-long --out ... --sample 50 --seed 0
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from aiconstructlexis.ingest.proceedings import (
    add_common_args, assign_paths, clean_text, finish, guard_for, http_get,
    log_summary, resolve_outputs, run_cli_main,
)
from aiconstructlexis.util.logging import setup_logging

log = logging.getLogger(__name__)

VOLUME_MAP = {
    "acl": "{year}.acl-long",
    "emnlp": "{year}.emnlp-main",
    "naacl": "{year}.naacl-long",
}

BASE_URL = "https://aclanthology.org"
PAPER_ID_RE = re.compile(r"^(\d{4}\.[a-z0-9]+(?:-[a-z0-9]+)*)\.(\d+)$")


def volume_id(venue: str, year: int) -> str:
    return VOLUME_MAP[venue].format(year=year)


# --- titles ---

def title_key(s: str) -> str:
    """Lowercase ASCII letters and digits only (accents folded)."""
    s = unicodedata.normalize("NFKD", s or "").lower()
    return re.sub(r"[^a-z0-9]", "", s)


def titles_agree(a: str, b: str) -> bool:
    return bool(a) and bool(b) and title_key(a) == title_key(b)


_ACCENT = {'"': "\u0308", "'": "\u0301", "`": "\u0300", "^": "\u0302", "~": "\u0303",
           "=": "\u0304", ".": "\u0307", "c": "\u0327", "v": "\u030c", "u": "\u0306",
           "H": "\u030b", "r": "\u030a", "k": "\u0328", "d": "\u0323", "b": "\u0331"}
_LETTERS = {"ss": "\u00df", "o": "\u00f8", "O": "\u00d8", "ae": "\u00e6", "AE": "\u00c6",
            "oe": "\u0153", "OE": "\u0152", "aa": "\u00e5", "AA": "\u00c5", "l": "\u0142",
            "L": "\u0141", "i": "i", "j": "j"}
_NAMED = {"textthreesuperior": "\u00b3", "texttwosuperior": "\u00b2", "textonesuperior": "\u00b9",
          "textendash": "\u2013", "textemdash": "\u2014", "textquoteright": "\u2019",
          "textquoteleft": "\u2018", "textquotedblleft": "\u201c", "textquotedblright": "\u201d",
          "textasciitilde": "~", "textbackslash": "\\", "textbar": "|", "textless": "<",
          "textgreater": ">", "textdegree": "\u00b0", "textregistered": "\u00ae",
          "texttrademark": "\u2122", "textcopyright": "\u00a9", "infty": "\u221e",
          "times": "\u00d7", "cdot": "\u00b7", "pm": "\u00b1", "rightarrow": "\u2192",
          "leftarrow": "\u2190", "to": "\u2192", "leq": "\u2264", "geq": "\u2265",
          "le": "\u2264", "ge": "\u2265", "neq": "\u2260", "approx": "\u2248",
          "Rightarrow": "\u21d2", "Leftarrow": "\u21d0", "textasciicircum": "^",
          "textlangle": "\u27e8", "textrangle": "\u27e9"}
_NAMED.update({f: f for f in ("log", "ln", "exp", "max", "min", "sup", "inf", "lim",
                              "arg", "sin", "cos", "tan", "det", "dim", "Pr")})
_GREEK = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota",
          "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau",
          "upsilon", "phi", "chi", "psi", "omega"]
for _i, _g in enumerate(_GREEK):
    _NAMED[_g] = chr(0x3B1 + _i + (1 if _i >= 17 else 0))  # skip final sigma U+03C2
    _NAMED[_g.capitalize()] = chr(0x391 + _i + (1 if _i >= 17 else 0))
_NAMED.update({"varepsilon": "\u03b5", "vartheta": "\u03d1", "varphi": "\u03c6",
               "varsigma": "\u03c2", "varrho": "\u03f1", "varpi": "\u03d6"})


def clean_bib_title(raw: str) -> str:
    """Readable Unicode title from a BibTeX title field (braces, accents, simple math)."""
    s = raw or ""
    hold = {"&": "\x01", "%": "\x02", "$": "\x03", "#": "\x04", "_": "\x05",
            "{": "\x06", "}": "\x07"}
    s = re.sub(r"\\([&%$#_{}])", lambda m: hold[m.group(1)], s)
    # Math: drop the $ delimiters and super/subscript markers.
    s = re.sub(r"\$([^$]*)\$", lambda m: m.group(1).replace("^", "").replace("_", ""), s)
    letter = r"(\\[ij](?![A-Za-z])|[A-Za-z])"

    def accent(m):
        base = m.group(2) or m.group(3)
        base = _LETTERS.get(base[1:], base) if base.startswith("\\") else base
        return base + _ACCENT[m.group(1)]

    s = re.sub(r"\\([\"'`^~=.])\s*(?:\{\s*" + letter + r"\s*\}|" + letter + ")", accent, s)
    s = re.sub(r"\\([cvuHrkdb])(?:\s*\{\s*" + letter + r"\s*\}|\s+" + letter + ")", accent, s)
    s = re.sub(r"\\(ss|ae|AE|oe|OE|aa|AA|o|O|l|L|i|j)(?![A-Za-z])\s?",
               lambda m: _LETTERS[m.group(1)], s)
    s = re.sub(r"\\([A-Za-z]+)", lambda m: _NAMED.get(m.group(1), ""), s)
    s = s.replace("{", "").replace("}", "").replace("~", " ")
    s = s.replace("---", "\u2014").replace("--", "\u2013")
    s = s.replace("``", "\u201c").replace("''", "\u201d")
    for ch, ph in hold.items():
        s = s.replace(ph, ch)
    return unicodedata.normalize("NFC", clean_text(s))


def clean_page_title(text: str) -> str:
    """Title text from a volume page. A few titles reach the page with raw LaTeX
    commands (e.g. "\\textlangle /think \\textrangle"); those are cleaned like BibTeX."""
    t = clean_text(text)
    return clean_bib_title(t) if re.search(r"\\[A-Za-z]", t) else t


def _bib_field(entry: str, field: str):
    """Raw value of `field` in one BibTeX entry, for "..." or {...} delimiters."""
    m = re.search(rf"^\s*{field}\s*=\s*", entry, re.M)
    if not m:
        return None
    i = m.end()
    if i >= len(entry) or entry[i] not in "\"{":
        return None
    opener = entry[i]
    depth = 0 if opener == '"' else 1
    j = i + 1
    while j < len(entry):
        c = entry[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if opener == "{" and depth == 0:
                return entry[i + 1:j]
        elif c == '"' and opener == '"' and depth == 0:
            return entry[i + 1:j]
        j += 1
    return None


def parse_anthology_bib(text: str) -> dict:
    """{anthology id: raw BibTeX title} for every entry of a volume BibTeX file
    (the @proceedings entry is keyed by the .0 id)."""
    out = {}
    for entry in re.split(r"\n(?=@)", "\n" + (text or "")):
        if not entry.lstrip().startswith("@"):
            continue
        url = _bib_field(entry, "url")
        title = _bib_field(entry, "title")
        if not url or title is None:
            continue
        pid = urlparse(url.strip()).path.strip("/")
        if pid:
            out[pid] = title
    return out


def bib_titles(text: str) -> dict:
    """{paper_id: cleaned title} for the numbered papers (front matter .0 excluded)."""
    out = {}
    for pid, raw in parse_anthology_bib(text).items():
        m = PAPER_ID_RE.match(pid)
        if m and int(m.group(2)) > 0:
            out[pid] = clean_bib_title(raw)
    return out


def load_volume_bib(vol_id: str, cache_dir: Path | None, save: bool = True) -> str:
    """Volume BibTeX text, read from cache_dir/<vol>.bib or downloaded (and then
    cached there when save is true)."""
    if cache_dir is not None:
        cached = Path(cache_dir) / f"{vol_id}.bib"
        if cached.is_file():
            return cached.read_text(encoding="utf-8")
    text = http_get(f"{BASE_URL}/volumes/{vol_id}.bib", timeout=120).text
    if cache_dir is not None and save:
        Path(cache_dir).mkdir(parents=True, exist_ok=True)
        (Path(cache_dir) / f"{vol_id}.bib").write_text(text, encoding="utf-8")
    return text


# --- volume page ---

def _href_id(href: str) -> str:
    return urlparse(urljoin(BASE_URL + "/", href)).path.strip("/")


def _paper_block(tag):
    """Closest ancestor <div> that also holds the paper's badge row."""
    for parent in tag.parents:
        if parent.name == "div" and parent.find(class_="list-button-row"):
            return parent
    return None


def parse_volume_html(html: str, vol_id: str) -> tuple[list, dict]:
    """Papers of one Anthology volume page, each title read from its own block.

    Returns ([{name, url, paper_id}], stats). Raises ValueError when a block's
    PDF badge and title link name different papers, or a block holds more than
    one paper, so a layout change cannot silently re-pair titles."""
    soup = BeautifulSoup(html, "html.parser")
    pid_re = re.compile(rf"^{re.escape(vol_id)}\.(\d+)$")
    pdf_re = re.compile(rf"^{re.escape(vol_id)}\.(\d+)\.pdf$")
    stats = {"front_matter": 0, "no_pdf": [], "attachments": 0, "volume_pdf": 0}
    for a in soup.find_all("a", href=True):
        path = _href_id(a["href"])
        if path.startswith("attachments/"):
            stats["attachments"] += 1
        elif path == f"{vol_id}.pdf":
            stats["volume_pdf"] += 1

    def title_link(strong):
        a = strong.find("a", href=True)
        return a if a is not None and pid_re.match(_href_id(a["href"])) else None

    papers, seen = [], set()
    for strong in soup.find_all("strong"):
        a = title_link(strong)
        if a is None:
            continue
        pid = _href_id(a["href"])
        if int(pid_re.match(pid).group(1)) == 0:
            stats["front_matter"] += 1
            continue
        if pid in seen:
            raise ValueError(f"{pid}: listed twice on the volume page")
        block = _paper_block(strong)
        if block is None:
            raise ValueError(f"{pid}: no paper block with a PDF badge row around its title")
        n_titles = sum(1 for s in block.find_all("strong") if title_link(s) is not None)
        if n_titles != 1:
            raise ValueError(f"{pid}: its block holds {n_titles} paper titles")
        pdfs = {}
        for x in block.find_all("a", href=True):
            path = _href_id(x["href"])
            if pdf_re.match(path):
                pdfs[path[:-len(".pdf")]] = urljoin(BASE_URL + "/", x["href"])
        if not pdfs:
            stats["no_pdf"].append(pid)
            continue
        if set(pdfs) != {pid}:
            raise ValueError(f"{pid}: block PDF link(s) {sorted(pdfs)} do not match its title")
        seen.add(pid)
        papers.append({"name": clean_page_title(a.get_text()), "url": pdfs[pid], "paper_id": pid})
    papers.sort(key=lambda p: int(p["paper_id"].rsplit(".", 1)[1]))
    return papers, stats


def check_against_bib(papers: list, titles: dict, no_pdf=()) -> dict:
    """Compare parsed (paper_id, title) pairs with the volume BibTeX titles."""
    by_id = {p["paper_id"]: p["name"] for p in papers}
    mismatch = [{"paper_id": pid, "page_title": t, "bib_title": titles[pid]}
                for pid, t in by_id.items() if pid in titles and not titles_agree(t, titles[pid])]
    return {
        "papers": len(by_id),
        "bib_papers": len(titles),
        "match": sum(1 for pid, t in by_id.items() if titles_agree(t, titles.get(pid, ""))),
        "mismatch": mismatch,
        "missing_in_bib": sorted(set(by_id) - set(titles)),
        "missing_on_page": sorted(set(titles) - set(by_id) - set(no_pdf)),
        "no_pdf": sorted(no_pdf),
    }


def list_volume(vol_id: str, bib_cache: Path | None, check: bool = True,
                html: str | None = None, bib_text: str | None = None) -> list:
    """Papers of one volume, parsed from its page and (with ``check``) verified
    against the volume BibTeX. Raises RuntimeError when the cross-check fails."""
    if html is None:
        url = f"{BASE_URL}/volumes/{vol_id}/"
        log.info("Fetching: %s", url)
        html = http_get(url, timeout=120).text
    papers, stats = parse_volume_html(html, vol_id)
    log.info("Parsed %d papers (skipped front matter %d, whole-volume PDF links %d, "
             "attachment links %d, no PDF %d)", len(papers), stats["front_matter"],
             stats["volume_pdf"], stats["attachments"], len(stats["no_pdf"]))
    if not check:
        return papers
    bib = bib_text if bib_text is not None else load_volume_bib(vol_id, bib_cache)
    titles = {pid: t for pid, t in bib_titles(bib).items() if pid.rsplit(".", 1)[0] == vol_id}
    rep = check_against_bib(papers, titles, stats["no_pdf"])
    log.info("BibTeX cross-check: %d/%d titles match (%d papers in the BibTeX)",
             rep["match"], rep["papers"], rep["bib_papers"])
    problems = rep["mismatch"] or rep["missing_in_bib"] or rep["missing_on_page"]
    for m in rep["mismatch"][:20]:
        log.warning("MISMATCH %s: page %r vs bib %r", m["paper_id"], m["page_title"], m["bib_title"])
    if rep["missing_in_bib"]:
        log.warning("on page, not in BibTeX: %s", rep["missing_in_bib"][:20])
    if rep["missing_on_page"]:
        log.warning("in BibTeX, not on page: %s", rep["missing_on_page"][:20])
    if problems:
        raise RuntimeError("BibTeX cross-check failed; nothing written "
                           "(inspect, then rerun with the check switched off to accept the page titles)")
    return papers


def resolve_volume(venue: str | None, year: int | None, volume: str | None) -> tuple[str, int, str]:
    """(venue, year, volume id) from a venue/year pair or an explicit volume id."""
    if volume:
        m = re.match(r"^(\d{4})\.([a-z0-9]+)", volume)
        if not m:
            raise ValueError(f"not an Anthology volume id: {volume}")
        return venue or m.group(2), year or int(m.group(1)), volume
    if venue and year:
        if venue not in VOLUME_MAP:
            raise ValueError(f"unknown Anthology venue {venue!r}; choose one of {sorted(VOLUME_MAP)}")
        return venue, year, volume_id(venue, year)
    raise ValueError("give a venue and a year, or a volume id")


def download_anthology(venue: str | None, year: int | None, out_json: str | Path,
                       pdf_dir: str | Path | None = None, *, volume: str | None = None,
                       bib_cache: str | Path | None = None, check_bib: bool = True,
                       metadata_only: bool = False, sample: int | None = None,
                       seed: int = 0, force: bool = False, workers: int = 8) -> Path:
    """List one Anthology volume, download its PDFs to ``pdf_dir`` and write the
    paper list to ``out_json``. Returns the path of the list written.

    ``volume`` overrides ``venue``/``year`` (which may then be None).
    ``bib_cache`` is a directory where volume BibTeX files are kept (None:
    download without caching). ``pdf_dir`` defaults to the list path without
    its suffix. Raises FileExistsError when the list exists and ``force`` is
    false, ValueError for a bad venue or volume id, and RuntimeError when the
    BibTeX cross-check fails or no paper is found."""
    venue, year, vol_id = resolve_volume(venue, year, volume)
    out, pdfs = resolve_outputs(out_json, pdf_dir)
    guard_for(out, sample, force)

    log.info("Listing papers for %s ...", vol_id)
    papers = list_volume(vol_id, Path(bib_cache) if bib_cache is not None else None, check=check_bib)
    if not papers:
        raise RuntimeError(f"No papers found for {vol_id}")
    assign_paths(papers, pdfs, stem=lambda e: e["paper_id"])
    summary = finish(papers, out, metadata_only=metadata_only, sample=sample,
                     seed=seed, force=force, workers=workers)
    log_summary(summary, pdfs)
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="List one ACL Anthology volume, download its PDFs and write the paper list")
    parser.add_argument("--venue", choices=sorted(VOLUME_MAP))
    parser.add_argument("--year", type=int)
    parser.add_argument("--volume", default=None,
                        help="Anthology volume id (e.g. 2026.acl-long); overrides --venue/--year")
    parser.add_argument("--bib-cache", type=Path, default=None,
                        help="Directory where volume BibTeX files are cached (default: no cache)")
    parser.add_argument("--skip-bib-check", action="store_true",
                        help="Do not cross-check titles against the volume BibTeX")
    add_common_args(parser, default_workers=8)
    args = parser.parse_args(argv)
    if not args.volume and not (args.venue and args.year):
        parser.error("give --venue and --year, or --volume")
    setup_logging(run_name="ingest_anthology", log_dir=args.log_dir)

    return run_cli_main(lambda: download_anthology(
        args.venue, args.year, args.out, args.pdf_dir, volume=args.volume,
        bib_cache=args.bib_cache, check_bib=not args.skip_bib_check,
        metadata_only=args.metadata_only, sample=args.sample, seed=args.seed,
        force=args.force, workers=args.workers))


if __name__ == "__main__":
    sys.exit(main())
