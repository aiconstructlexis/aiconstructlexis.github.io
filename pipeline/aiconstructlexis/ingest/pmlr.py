"""Ingest stage: list and download every paper of one PMLR volume (ICML, AISTATS, COLT, ...).

Inputs
  The PMLR volume number (volume numbers do not follow the conference year, so
  it is given explicitly), plus the conference name and year used to label
  the run.

Outputs
  A paper-list JSON (``out_json``; see ``aiconstructlexis.ingest.proceedings``
  for the schema, sampling and the no-overwrite rule) and the PDFs under
  ``pdf_dir``, one ``<title slug>.pdf`` per paper. Each entry carries ``name``,
  ``url`` and ``path``. PDFs are served from raw.githubusercontent.com.

Command line
  python -m aiconstructlexis.ingest.pmlr --volume 306 --conference icml --year 2026 --out work/icml26/papers.json
  python -m aiconstructlexis.ingest.pmlr --volume 306 --conference icml --year 2026 --out ... --metadata-only
  python -m aiconstructlexis.ingest.pmlr --volume 306 --conference icml --year 2026 --out ... --sample 50 --seed 0
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from aiconstructlexis.ingest.proceedings import (
    add_common_args, assign_paths, finish, guard_for, http_get, log_summary,
    parse_pmlr_index, resolve_outputs, run_cli_main,
)
from aiconstructlexis.util.logging import setup_logging

log = logging.getLogger(__name__)


def pmlr_index_url(volume: int) -> str:
    return f"https://proceedings.mlr.press/v{volume}/"


def list_pmlr_volume(volume: int) -> list:
    """[{name, url}] for every paper in PMLR volume ``volume``."""
    return parse_pmlr_index(http_get(pmlr_index_url(volume)).text)


def download_pmlr(volume: int, conference: str, year: int, out_json: str | Path,
                  pdf_dir: str | Path | None = None, *, metadata_only: bool = False,
                  sample: int | None = None, seed: int = 0, force: bool = False,
                  workers: int = 12) -> Path:
    """List PMLR volume ``volume``, download its PDFs to ``pdf_dir`` and write
    the paper list to ``out_json``. Returns the path of the list written.

    ``pdf_dir`` defaults to the list path without its suffix. Raises
    FileExistsError when the list exists and ``force`` is false, and
    RuntimeError when the volume index lists no paper or cannot be fetched."""
    out, pdfs = resolve_outputs(out_json, pdf_dir)
    guard_for(out, sample, force)

    log.info("Fetching PMLR v%d index for %s %d ...", volume, conference.upper(), year)
    papers = list_pmlr_volume(volume)
    log.info("Found %d papers in PMLR v%d", len(papers), volume)
    if not papers:
        raise RuntimeError(f"No papers found in PMLR v{volume}")
    assign_paths(papers, pdfs)
    summary = finish(papers, out, metadata_only=metadata_only, sample=sample,
                     seed=seed, force=force, workers=workers)
    log_summary(summary, pdfs)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="List one PMLR volume, download its PDFs and write the paper list")
    ap.add_argument("--volume", type=int, required=True, help="PMLR volume, e.g. 306")
    ap.add_argument("--conference", required=True, help="conference label, e.g. icml")
    ap.add_argument("--year", type=int, required=True)
    add_common_args(ap, default_workers=12)
    args = ap.parse_args(argv)
    setup_logging(run_name="ingest_pmlr", log_dir=args.log_dir)

    return run_cli_main(lambda: download_pmlr(
        args.volume, args.conference, args.year, args.out, args.pdf_dir,
        metadata_only=args.metadata_only, sample=args.sample, seed=args.seed,
        force=args.force, workers=args.workers))


if __name__ == "__main__":
    sys.exit(main())
