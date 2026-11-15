"""Catalog invariant: every original node has at least one paper.

An original node is one extracted surface name of an entity, with the definition the
extraction gave it and the papers it was extracted from. Paper lists can shrink after
extraction (a paper screened out on a rerun, or a PDF that could not be extracted), and a
node whose paper list is empty would show a definition on the site with no paper behind it.
This stage removes such nodes so that every definition shown is traceable to a paper.

A node is dropped only when its paper list is empty; entity paper lists, summaries and
relationships are left as they are. Running it twice changes nothing the second time.
"""
from __future__ import annotations

import argparse
import json
import logging
from collections import Counter
from pathlib import Path

logger = logging.getLogger(__name__)

ENTITY_TYPES = ("constructs", "measurements", "behaviors")


def drop_orphans(net: dict) -> dict:
    """Remove original nodes with no papers, in place. Returns {"stats", "examples"}."""
    stats = Counter()
    examples = []
    for et in ENTITY_TYPES:
        for g in net.get(et) or []:
            nodes = g.get("original_nodes") or {}
            orphans = [name for name, node in nodes.items() if not (node.get("papers") or [])]
            for name in orphans:
                if (nodes[name].get("definition") or "").strip():
                    stats["definitions dropped"] += 1
                del nodes[name]
                stats["nodes dropped"] += 1
                if len(examples) < 5:
                    examples.append(f"{g['canonical_name']} <- {name}")
            if orphans:
                stats["entities touched"] += 1
                if not any((n.get("definition") or "").strip() for n in nodes.values()):
                    stats["entities left with no definition"] += 1
    return {"stats": dict(stats), "examples": examples}


def drop_orphan_definitions(input_json, output_json) -> dict:
    """Read ``input_json``, drop nodes with no papers and write ``output_json`` (the two may
    be the same path). Returns the report of :func:`drop_orphans`."""
    with open(input_json, encoding="utf-8") as f:
        net = json.load(f)
    report = drop_orphans(net)
    logger.info("Orphan nodes: %s", report["stats"] or "none")
    Path(output_json).parent.mkdir(parents=True, exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(net, f, indent=2, ensure_ascii=False)
    logger.info("Wrote %s", output_json)
    return report


def main(argv=None) -> None:
    from aiconstructlexis.util.logging import setup_logging

    ap = argparse.ArgumentParser(description="Drop original nodes whose paper list is empty.")
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--dry-run", action="store_true", help="report only; write nothing")
    ap.add_argument("--log-dir", default="logs")
    args = ap.parse_args(argv)
    setup_logging(run_name="curate_cleanup", log_dir=args.log_dir)
    if args.dry_run:
        with open(args.input, encoding="utf-8") as f:
            report = drop_orphans(json.load(f))
    else:
        report = drop_orphan_definitions(args.input, args.output)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
