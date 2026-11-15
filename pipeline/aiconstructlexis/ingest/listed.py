"""Download the papers of an existing paper list.

A release ships its screened paper lists (``lexis/paper_lists/<venue>.json``: title, url,
is_LLM_paper); this stage turns such a list into the per-venue ``papers.json`` the rest of
the pipeline reads, fetching the PDFs into ``pdf_dir`` and recording their paths. Records
keep their screening decision, so the screening stage has nothing to do for them.

    python -m aiconstructlexis.ingest.listed --list lexis/paper_lists/iclr24.json \\
        --out runs/venues/iclr24/papers.json --pdf-dir runs/pdfs/iclr24
"""
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Callable, Optional

from aiconstructlexis.ingest.proceedings import (assign_paths, download_pdfs, log_summary, resolve_outputs,
                                                 run_cli_main, select_sample, slugify, write_list)

log = logging.getLogger(__name__)


def normalize_entries(records: list) -> list:
    """Paper-list records in the pipeline's shape: ``name``, ``url`` and whatever else they carry."""
    out = []
    for p in records:
        if not isinstance(p, dict):
            continue
        name = (p.get("name") or p.get("title") or "").strip()
        url = (p.get("url") or p.get("pdf_url") or p.get("openreview_url") or "").strip()
        if not name or not url:
            continue
        e = {k: v for k, v in p.items() if k not in ("title", "path", "name", "url", "pdf_url", "openreview_url")}
        e["name"] = name
        e["url"] = url
        out.append(e)
    return out


def download_listed(paper_list_json: str | Path, out_json: str | Path, pdf_dir: str | Path | None = None, *,
                    only_flagged: bool = True, sample: Optional[int] = None, seed: int = 0, workers: int = 4,
                    force: bool = True, fetch: Callable[[str, Path], Optional[str]] | None = None) -> Path:
    """Write ``out_json`` from ``paper_list_json`` and download the PDFs into ``pdf_dir``.

    With ``only_flagged`` (the default) PDFs are fetched only for records whose
    ``is_LLM_paper`` is true, or for every record when the list carries no screening
    decision; with ``sample`` only a seeded sample of that many of them is fetched. Records
    that are not fetched keep no ``path``. PDFs already present are not downloaded again.
    Returns the path of the list written.
    """
    src = Path(paper_list_json)
    with open(src, encoding="utf-8") as f:
        records = json.load(f)
    if isinstance(records, dict):
        records = list(records.values())
    entries = normalize_entries(records)
    if not entries:
        raise RuntimeError(f"{src} holds no usable paper records (each needs a title and a url)")
    out, pdfs = resolve_outputs(out_json, pdf_dir)

    screened = any("is_LLM_paper" in e for e in entries)
    wanted = [e for e in entries if not (only_flagged and screened) or e.get("is_LLM_paper") is True]
    if sample is not None and sample < len(wanted):
        chosen = select_sample(wanted, sample, seed)
        wanted = [e for e in wanted if e["url"] in chosen]
    assign_paths(wanted, pdfs, stem=lambda e: str(e.get("paper_id") or slugify(e["name"])))
    errors = download_pdfs(wanted, workers=workers, fetch=fetch)
    for e in wanted:
        err = errors.get(e["url"])
        if err:
            e.pop("path", None)
            e["download_error"] = err
    write_list(out, entries, force)
    log_summary({"listed": len(entries), "selected": len(wanted),
                 "downloaded": sum(1 for e in wanted if "path" in e),
                 "failed": sum(1 for v in errors.values() if v), "metadata_only": False,
                 "list": str(out)}, pdfs)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Download the papers of an existing paper list.")
    ap.add_argument("--list", required=True, help="paper-list JSON (title|name, url, optional is_LLM_paper)")
    ap.add_argument("--out", type=Path, required=True, help="paper-list JSON to write")
    ap.add_argument("--pdf-dir", type=Path, default=None,
                    help="PDF directory (default: the list path without its .json suffix)")
    ap.add_argument("--all", action="store_true", help="download every record, not only the screened-in ones")
    ap.add_argument("--sample", type=int, default=None, metavar="N", help="download a seeded sample of N papers")
    ap.add_argument("--seed", type=int, default=0, help="seed for --sample (default 0)")
    ap.add_argument("--workers", type=int, default=4, help="parallel PDF downloads")
    ap.add_argument("--log-dir", default="logs", help="directory for the run log (default: logs)")
    args = ap.parse_args(argv)

    from aiconstructlexis.util.logging import setup_logging
    setup_logging(run_name="ingest_listed", log_dir=args.log_dir)
    return run_cli_main(lambda: download_listed(args.list, args.out, args.pdf_dir, only_flagged=not args.all,
                                               sample=args.sample, seed=args.seed, workers=args.workers))


if __name__ == "__main__":
    raise SystemExit(main())
