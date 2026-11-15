"""
Build the data files behind the site's analysis tools page (tools.html).

Reads the network JSON and the site's ``graph.bundle.json`` and writes two compact files
into ``<site_dir>/data/``:

  analysis.bundle.json    nodes, edges and per-edge paper lists (loaded when the page opens)
  analysis_evidence.json  per-edge, per-paper verbatim quotes (loaded on first use)

Nodes come from the graph bundle, so the tools show exactly the entities the network graph
shows; only edges whose endpoints are both present are kept. Rows are positional arrays
whose field names are listed in ``meta``:

  nodes  [name, type code (c/m/b), paper_count, definition (first 400 characters)]
  edges  [source index, target index, type, paper_count, paper_weight, paper indices, type shares]
  papers [title, conference]

Rerun this stage after every site export.
"""
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, List
from aiconstructlexis.util.names import DATA_SUBDIR

logger = logging.getLogger(__name__)

TYPE_CODE = {"construct": "c", "measurement": "m", "behavior": "b"}


def build_analysis_bundle(network_json: str | Path, site_dir: str | Path) -> Dict[str, int]:
    """Write analysis.bundle.json and analysis_evidence.json for the site in ``site_dir``.

    Returns the node, edge and paper counts of the bundle.
    """
    in_path = Path(network_json)
    joint = json.load(open(in_path, encoding="utf-8"))
    data_dir = Path(site_dir) / DATA_SUBDIR
    graph = json.load(open(data_dir / "graph.bundle.json", encoding="utf-8"))

    nodes = sorted(graph["nodes"], key=lambda n: (n["type"], n["name"].lower()))
    node_idx = {n["name"]: i for i, n in enumerate(nodes)}
    out_nodes = [
        [n["name"], TYPE_CODE[n["type"]], n.get("paper_count", 0), (n.get("definition") or "")[:400]]
        for n in nodes
    ]

    papers = []
    paper_idx = {}

    def pid(conf: str, title: str) -> int:
        key = (conf, title)
        if key not in paper_idx:
            paper_idx[key] = len(papers)
            papers.append([title, conf])
        return paper_idx[key]

    edges = []
    evidence = []
    for r in joint["relationships"]:
        s, t = r["source"], r["target"]
        if s not in node_idx or t not in node_idx:
            continue
        rows = r.get("papers") or []
        plist = [pid(x["conference"], x["paper"]) for x in rows]
        shares = [round(float(x.get("type_share", 1.0)), 3) for x in rows]
        edges.append([
            node_idx[s], node_idx[t], r["type"],
            r.get("paper_count", len(plist)),
            round(float(r.get("paper_weight", len(plist))), 2),
            plist, shares,
        ])
        quotes = {}
        for q in r.get("evidence_by_paper") or []:
            quotes.setdefault(pid(q["conference"], q["paper"]), q.get("quote", ""))
        evidence.append([[k, v] for k, v in quotes.items()])

    metadata = joint.get("metadata", {}) or {}
    meta = {
        "built_from": "AI Construct Lexis data",
        "version": str(metadata.get("version") or ""),
        "joint_of": metadata.get("venues") or metadata.get("joint_of", []),
        "n_nodes": len(out_nodes),
        "n_edges": len(edges),
        "n_papers": len(papers),
        "node_fields": ["name", "type", "paper_count", "definition"],
        "edge_fields": ["source", "target", "type", "paper_count", "paper_weight", "papers", "type_shares"],
        "paper_fields": ["title", "conference"],
    }
    with open(data_dir / "analysis.bundle.json", "w") as f:
        json.dump({"meta": meta, "nodes": out_nodes, "edges": edges, "papers": papers},
                  f, separators=(",", ":"))
    with open(data_dir / "analysis_evidence.json", "w") as f:
        json.dump({"built_from": meta["built_from"], "evidence": evidence}, f, separators=(",", ":"))

    for name in ("analysis.bundle.json", "analysis_evidence.json"):
        logger.info("  %s: %d KB", name, (data_dir / name).stat().st_size // 1024)
    logger.info("  %d nodes, %d edges, %d papers", meta["n_nodes"], meta["n_edges"], meta["n_papers"])
    if meta["n_edges"] != graph.get("edge_count", len(graph["edges"])):
        logger.warning("graph.bundle.json has %d edges; the site export and %s may be out of sync.",
                       len(graph["edges"]), in_path.name)
    return {"nodes": meta["n_nodes"], "edges": meta["n_edges"], "papers": meta["n_papers"]}


def main(argv: List[str] | None = None) -> None:
    from aiconstructlexis.util.logging import setup_logging

    p = argparse.ArgumentParser(description="Build the data files behind the site's analysis tools page.")
    p.add_argument("--input", required=True, help="network JSON the site was exported from")
    p.add_argument("--site", required=True, help="site directory holding data/")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args(argv)
    setup_logging(run_name="export_analysis_bundle", log_dir=args.log_dir)
    build_analysis_bundle(args.input, args.site)


if __name__ == "__main__":
    main()
