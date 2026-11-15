"""
Check that a site's data holds what the site reads for the network JSON it was built from.

The in-scope entities of the network (those not flagged ``expert_removed``) must each have
their record at ``data/<type dir>/<slug>.json`` with the matching ``canonical_name`` and the
network's relationships between that entity and the other in-scope entities (partner, type,
direction, paper count and paper weight); no other per-entity file may exist; the graph
bundle's nodes must be exactly the in-scope entities, with every edge between two of them;
and the files the pages fetch must exist: ``paper_urls.json`` and the hand-maintained
``empirical_evidence.json`` always, ``analysis.bundle.json`` and ``analysis_evidence.json``
when the analysis bundle is part of the export, ``layout.json`` when the graph layout is, and,
when the readable mirror is, exactly one ``<slug>.md`` per in-scope entity under
``data/readable/<type dir>/`` and nothing else there.

``check_site_export`` returns the list of problems found (empty means the export is
consistent); the command-line entry point checks everything, prints the problems and exits
with status 1 if there are any.
"""
from __future__ import annotations

import argparse
import json
import logging
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List

from aiconstructlexis.util.names import DATA_SUBDIR, READABLE_SUBDIR, SITE_SUBDIR, slugify

logger = logging.getLogger(__name__)

ALWAYS_REQUIRED_FILES = ("paper_urls.json", "empirical_evidence.json")
ANALYSIS_BUNDLE_FILES = ("analysis.bundle.json", "analysis_evidence.json")
GRAPH_LAYOUT_FILES = ("layout.json",)


def _read(path: Path) -> Any:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def check_site_export(site_dir: str | Path, network_json: str | Path | Dict[str, Any], *,
                      analysis_bundle: bool = True, graph_layout: bool = True,
                      readable: bool = True) -> List[str]:
    """Return the inconsistencies between the site data in ``site_dir`` and ``network_json``.

    The keyword flags say which optional export steps the site was built with; the files of
    a step that is turned off are not required.
    """
    net = network_json if isinstance(network_json, dict) else _read(Path(network_json))
    site = Path(site_dir)
    data = site / DATA_SUBDIR
    problems: List[str] = []

    # Per-entity files: one per in-scope entity, named by its slug, and nothing else.
    records: Dict[str, Dict[str, Any]] = {}
    expected_by_sub: Dict[str, Dict[str, str]] = {}
    for et, sub in SITE_SUBDIR.items():
        expected: Dict[str, str] = {}
        for g in net.get(et) or []:
            if g.get("expert_removed"):
                continue
            name = (g.get("canonical_name") or "").strip()
            slug = slugify(name)
            if slug in expected:
                problems.append(f"{sub}: {expected[slug]!r} and {name!r} share the file {slug}.json")
            expected[slug] = name
        expected_by_sub[sub] = expected
        folder = data / sub
        present = {p.stem for p in folder.glob("*.json")} if folder.is_dir() else set()
        for slug in sorted(set(expected) - present):
            problems.append(f"{sub}/{slug}.json missing for {expected[slug]!r}")
        for slug in sorted(present - set(expected)):
            problems.append(f"{sub}/{slug}.json has no in-scope entity in the network")
        for slug in sorted(set(expected) & present):
            rec = _read(folder / f"{slug}.json")
            if rec.get("canonical_name") != expected[slug]:
                problems.append(f"{sub}/{slug}.json names {rec.get('canonical_name')!r}, "
                                f"network has {expected[slug]!r}")
                continue
            records[expected[slug]] = rec

    in_scope = {name for expected in expected_by_sub.values() for name in expected.values()}

    # Relationships of each record: the network's relationships between that entity and the
    # other in-scope entities, both directions.
    want = {name: Counter() for name in records}
    for r in net.get("relationships") or []:
        if r["source"] not in in_scope or r["target"] not in in_scope:
            continue
        for me, other, d in ((r["source"], r["target"], "outgoing"), (r["target"], r["source"], "incoming")):
            if me in want:
                want[me][(other, r["type"], d, r["paper_count"], round(r["paper_weight"], 3))] += 1
    for name, rec in records.items():
        have = Counter((x["other_canonical_name"], x["relationship_type"], x["direction"], x["paper_count"],
                        round(x["paper_weight"], 3)) for x in rec["relationships"])
        if have != want[name]:
            problems.append(f"relationships differ for {name}: {sum((have - want[name]).values())} extra, "
                            f"{sum((want[name] - have).values())} missing")

    # Graph bundle: the in-scope entities and edges between them only.
    graph_path = data / "graph.bundle.json"
    if graph_path.is_file():
        graph = _read(graph_path)
        nodes = Counter(n.get("name") for n in graph.get("nodes") or [])
        for kind, names in (("duplicated", [n for n, c in nodes.items() if c > 1]),
                            ("not in scope", sorted(set(nodes) - in_scope)),
                            ("missing", sorted(in_scope - set(nodes)))):
            if names:
                problems.append(f"graph.bundle.json: {len(names)} node(s) {kind}: "
                                + ", ".join(sorted(names)[:5]))
        dangling = [e for e in graph.get("edges") or [] if e.get("source") not in nodes or e.get("target") not in nodes]
        if dangling:
            problems.append(f"graph.bundle.json: {len(dangling)} edge(s) touch a node that is not in the bundle")
    else:
        problems.append("graph.bundle.json missing")

    # Readable mirror: one Markdown page per in-scope entity, and nothing else in its folders.
    if readable:
        readable_dir = site / READABLE_SUBDIR
        rel = Path(READABLE_SUBDIR).relative_to(DATA_SUBDIR)
        for sub, expected in expected_by_sub.items():
            folder = readable_dir / sub
            present = {p.name for p in folder.iterdir()} if folder.is_dir() else set()
            pages = {f"{slug}.md": name for slug, name in expected.items()}
            for page in sorted(set(pages) - present):
                problems.append(f"{rel}/{sub}/{page} missing for {pages[page]!r}")
            for name in sorted(present - set(pages)):
                problems.append(f"{rel}/{sub}/{name} is not the page of an in-scope entity")

    required = list(ALWAYS_REQUIRED_FILES)
    if analysis_bundle:
        required += ANALYSIS_BUNDLE_FILES
    if graph_layout:
        required += GRAPH_LAYOUT_FILES
    for name in required:
        if not (data / name).is_file():
            problems.append(f"{name} missing")

    logger.info("in-scope entities %d, records %d, relationships %d",
                len(in_scope), len(records), len(net.get("relationships") or []))
    return problems


def main(argv: List[str] | None = None) -> int:
    from aiconstructlexis.util.logging import setup_logging

    p = argparse.ArgumentParser(description="Check that a site's data matches its network JSON.")
    p.add_argument("site_dir", help="site directory holding data/")
    p.add_argument("network_json", help="network JSON the site was exported from")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args(argv)
    setup_logging(run_name="export_check", log_dir=args.log_dir)

    problems = check_site_export(args.site_dir, args.network_json)
    if problems:
        print(f"FAILED: {len(problems)} problem(s)")
        for msg in problems[:20]:
            print("  -", msg)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
