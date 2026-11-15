"""Minimum-paper filter for one venue's harmonized network.

Keeps only the entities supported by at least ``min_papers`` papers (default 2) and the
relationships whose two endpoints survive, then rebuilds ``name_mapping`` from the
surviving entities (canonical name and original names -> canonical name). This runs
after the entity vote and before a venue's network joins the others, so the joint network
only receives concepts that recur within a venue.

The input file is left untouched; the output goes to ``output_json`` or, by default, to
the input name with ``.multi_paper`` inserted before the extension.
"""
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path

from aiconstructlexis.util.logging import setup_logging

logger = logging.getLogger(__name__)

ENTITY_TYPES = ("constructs", "measurements", "behaviors")


def filter_network(net: dict, min_papers: int) -> dict:
    """Apply the filter to a loaded network in place and return it."""
    kept_canon: set = set()
    for et in ENTITY_TYPES:
        items = net.get(et, []) or []
        kept = [g for g in items if g.get("paper_count", 0) >= min_papers]
        net[et] = kept
        for g in kept:
            kept_canon.add(g.get("canonical_name", ""))
        logger.info("  %s: %d -> %d (dropped %d with paper_count < %d)",
                    et, len(items), len(kept), len(items) - len(kept), min_papers)

    rels = net.get("relationships", []) or []
    kept_rels = [r for r in rels
                 if r.get("source") in kept_canon and r.get("target") in kept_canon]
    logger.info("  relationships: %d -> %d (both endpoints surviving)", len(rels), len(kept_rels))
    net["relationships"] = kept_rels

    nm = {}
    for et in ENTITY_TYPES:
        for g in net[et]:
            c = g.get("canonical_name", "").strip()
            if not c:
                continue
            nm[c] = c
            for orig in g.get("original_names", []) or []:
                if orig:
                    nm[orig] = c
    net["name_mapping"] = nm
    return net


def filter_min_papers(
    input_json: str | Path,
    output_json: str | Path | None = None,
    min_papers: int = 2,
) -> Path:
    """Write the filtered network and return its path."""
    in_path = Path(input_json)
    out_path = Path(output_json) if output_json else \
        in_path.with_name(in_path.stem + ".multi_paper" + in_path.suffix)

    with open(in_path) as f:
        net = json.load(f)
    logger.info("Loaded %s", in_path)
    filter_network(net, min_papers)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(net, f, indent=2)
    logger.info("Wrote %s", out_path)
    return out_path


def main(argv=None) -> None:
    p = argparse.ArgumentParser(
        description="Keep the entities with at least N papers and the relationships among them.")
    p.add_argument("--input", required=True, help="harmonized network JSON")
    p.add_argument("--output", default=None,
                   help="output path (default: input name with .multi_paper before the extension)")
    p.add_argument("--min-papers", type=int, default=2,
                   help="drop entities with paper_count below this (default: 2)")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args(argv)

    setup_logging(run_name="vote_filter", log_dir=args.log_dir)
    filter_min_papers(args.input, args.output, min_papers=args.min_papers)


if __name__ == "__main__":
    main()
