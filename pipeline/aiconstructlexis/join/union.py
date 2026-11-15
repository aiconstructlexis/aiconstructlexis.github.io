"""Cross-venue union: one joint network from several venues' harmonized networks.

Inputs are the per-venue networks after the entity vote and the minimum-paper filter,
given as {venue label: path}. The stage:

  1. unions entities at canonical name (case-insensitive): when the same canonical name
     appears in several venues, ``original_names``, ``original_nodes``,
     ``source_snippets_evidence``, ``characterizations`` and ``canonical_definition`` are
     merged, and papers are kept per venue in ``papers_by_conference`` (``papers`` becomes
     a list of {"conference", "paper"} records, ``paper_count_by_conference`` the counts);
  2. unions relationships by (source, target, type), lowercased, pooling evidence and
     papers across venues (the longer display name of an endpoint is kept);
  3. optionally (``postmerge``) collapses canonical names that normalize to the same key
     (case, hyphens, plurals, filler suffixes, synonym nouns) with the normalizer of
     ``aiconstructlexis.harmonize.residuals``; the entity with more papers (then the
     shorter name) survives and ``name_mapping`` is rebuilt.

Output: a network JSON with ``metadata`` ({"joint_of": [venues], "n_conferences"}),
the three entity lists, ``relationships``, ``papers`` ([{"conference", "paper"}]) and
``paper_count_by_conference``. The semantic cross-venue merge is a separate stage
(``aiconstructlexis.join.llm_merge``).
"""
from __future__ import annotations

import argparse
import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

from aiconstructlexis.util.logging import setup_logging

logger = logging.getLogger(__name__)

ENTITY_TYPES = ("constructs", "measurements", "behaviors")


def _norm_key(name: str) -> str:
    """Lowercased, trimmed key for first-pass union by canonical name."""
    return (name or "").strip().lower()


def merge_group_into(target: Dict[str, Any], source: Dict[str, Any], conf: str) -> None:
    """Merge one group's metadata into another, prefixing papers with conf tag."""
    # original_names
    tn = set(target.setdefault("original_names", []))
    for n in source.get("original_names", []) or []:
        if n and n not in tn:
            target["original_names"].append(n)
            tn.add(n)
    # original_nodes (dict of original_name -> {definition, papers})
    on = target.setdefault("original_nodes", {})
    for k, v in (source.get("original_nodes") or {}).items():
        if k not in on:
            on[k] = {"definition": v.get("definition", ""),
                     "papers": [(conf, p) for p in (v.get("papers") or [])]}
        else:
            existing = {tuple(p) if isinstance(p, list) else p
                        for p in on[k].get("papers") or []}
            for p in v.get("papers") or []:
                tag = (conf, p)
                if tag not in existing:
                    on[k].setdefault("papers", []).append(tag)
                    existing.add(tag)
    # source_snippets_evidence
    sse = target.setdefault("source_snippets_evidence", [])
    sse_set = {json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s) for s in sse}
    for s in source.get("source_snippets_evidence") or []:
        sig = json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s)
        if sig not in sse_set:
            sse.append(s)
            sse_set.add(sig)
    # papers: kept per venue in papers_by_conference
    pbc = target.setdefault("papers_by_conference", {})
    pbc.setdefault(conf, [])
    existing_pbc = set(pbc[conf])
    for p in source.get("papers") or []:
        if p not in existing_pbc:
            pbc[conf].append(p)
            existing_pbc.add(p)
    # characterization: kept per venue in characterizations; the first non-empty one is promoted
    char = (source.get("characterization") or "").strip()
    if char:
        chars = target.setdefault("characterizations", {})
        chars[conf] = char
        # Promote to top-level "characterization" if not set
        if not target.get("characterization"):
            target["characterization"] = char
    # canonical_definition: prefer non-empty
    if not target.get("canonical_definition") and source.get("canonical_definition"):
        target["canonical_definition"] = source["canonical_definition"]


def build_joint_entities(inputs: List[Tuple[str, Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
    out = {"constructs": [], "measurements": [], "behaviors": []}
    for etype in out:
        by_key: Dict[str, Dict[str, Any]] = {}
        for conf, net in inputs:
            for g in net.get(etype, []) or []:
                canon = (g.get("canonical_name") or "").strip()
                if not canon:
                    continue
                key = _norm_key(canon)
                if key not in by_key:
                    new_g = {
                        "canonical_name": canon,
                        "original_names": [],
                        "original_nodes": {},
                        "source_snippets_evidence": [],
                        "papers_by_conference": {},
                    }
                    by_key[key] = new_g
                merge_group_into(by_key[key], g, conf)
        # Compute aggregate paper counts and flatten papers list (with conf tag)
        groups = []
        for g in by_key.values():
            pbc = g.get("papers_by_conference", {})
            all_papers = []
            for conf, papers in pbc.items():
                for p in papers:
                    all_papers.append({"conference": conf, "paper": p})
            g["papers"] = all_papers
            g["paper_count"] = len(all_papers)
            g["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
            groups.append(g)
        out[etype] = groups
    return out


def build_joint_relationships(inputs: List[Tuple[str, Dict[str, Any]]]) -> List[Dict[str, Any]]:
    by_key: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for conf, net in inputs:
        for r in net.get("relationships", []) or []:
            src = (r.get("source") or "").strip()
            tgt = (r.get("target") or "").strip()
            rtype = (r.get("type") or "").strip().lower()
            if not src or not tgt or not rtype:
                continue
            key = (_norm_key(src), _norm_key(tgt), rtype)
            if key not in by_key:
                by_key[key] = {
                    "source": src,
                    "target": tgt,
                    "type": rtype,
                    "evidence": [],
                    "papers": [],
                    "papers_by_conference": {},
                    "paper_count": 0,
                }
            tgt_rel = by_key[key]
            # Prefer longer, more specific display name
            if len(src) > len(tgt_rel["source"]):
                tgt_rel["source"] = src
            if len(tgt) > len(tgt_rel["target"]):
                tgt_rel["target"] = tgt
            ev_set = set(tgt_rel.get("evidence") or [])
            for e in r.get("evidence") or []:
                if e and e not in ev_set:
                    tgt_rel["evidence"].append(e)
                    ev_set.add(e)
            pbc = tgt_rel.setdefault("papers_by_conference", {})
            pbc.setdefault(conf, [])
            ex = set(pbc[conf])
            # Per-conf rels may have papers as either list[str] or
            # list[{"conference":..,"paper":..}] (after the relationship vote).
            for p in r.get("papers") or []:
                if isinstance(p, dict):
                    p_name = p.get("paper")
                else:
                    p_name = p
                if p_name and p_name not in ex:
                    pbc[conf].append(p_name)
                    ex.add(p_name)
                    tgt_rel["papers"].append({"conference": conf, "paper": p_name})
                    tgt_rel["paper_count"] += 1
    rels = list(by_key.values())
    rels.sort(key=lambda r: (-r["paper_count"], r["source"], r["target"]))
    return rels


def deterministic_post_merge(network: Dict[str, Any]) -> Dict[str, Any]:
    """Collapse canonical names that normalize to the same key, in place.

    Uses the normalizer and name-mapping builder of the per-venue residual collapse
    (``aiconstructlexis.harmonize.residuals``) and unions the joint-network fields
    (``papers_by_conference``, ``original_nodes``, ``characterizations``, ...).
    """
    from aiconstructlexis.harmonize.residuals import normalize, rebuild_name_mapping

    for et in ENTITY_TYPES:
        items = network.get(et, []) or []
        if not items:
            continue
        by_norm: Dict[str, List[int]] = defaultdict(list)
        for i, g in enumerate(items):
            c = g.get("canonical_name", "")
            if c:
                by_norm[normalize(c)].append(i)

        new_items: List[Dict[str, Any]] = []
        merged_count = 0
        for norm_key, idxs in by_norm.items():
            if len(idxs) == 1:
                new_items.append(items[idxs[0]])
                continue
            # Pick winner: highest paper_count, tiebreak shorter name
            winner_idx = max(
                idxs,
                key=lambda i: (
                    items[i].get("paper_count", 0),
                    -len(items[i].get("canonical_name", "")),
                ),
            )
            winner = dict(items[winner_idx])
            for j in idxs:
                if j == winner_idx:
                    continue
                src = items[j]
                # original_names
                wn = set(winner.get("original_names") or [])
                for n in src.get("original_names") or []:
                    if n not in wn:
                        winner.setdefault("original_names", []).append(n)
                        wn.add(n)
                # papers_by_conference
                wpbc = winner.setdefault("papers_by_conference", {})
                for conf, ps in (src.get("papers_by_conference") or {}).items():
                    existing = set(wpbc.setdefault(conf, []))
                    for p in ps:
                        if p not in existing:
                            wpbc[conf].append(p)
                            existing.add(p)
                # original_nodes
                wnodes = winner.setdefault("original_nodes", {})
                for k, v in (src.get("original_nodes") or {}).items():
                    if k not in wnodes:
                        wnodes[k] = v
                # source_snippets_evidence
                wsse = winner.setdefault("source_snippets_evidence", [])
                wset = {json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s) for s in wsse}
                for s in src.get("source_snippets_evidence") or []:
                    sig = json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s)
                    if sig not in wset:
                        wsse.append(s)
                        wset.add(sig)
                # characterizations dict
                wchars = winner.setdefault("characterizations", {})
                for conf, ch in (src.get("characterizations") or {}).items():
                    if conf not in wchars:
                        wchars[conf] = ch
                if not winner.get("characterization") and src.get("characterization"):
                    winner["characterization"] = src["characterization"]
                merged_count += 1
            # Recompute aggregate paper info
            pbc = winner.get("papers_by_conference", {})
            winner["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
            all_papers = [{"conference": c, "paper": p} for c, ps in pbc.items() for p in ps]
            winner["papers"] = all_papers
            winner["paper_count"] = len(all_papers)
            new_items.append(winner)

        network[et] = new_items
        logger.info("  post-merge %s: %d -> %d (-%d)", et, len(items), len(new_items), merged_count)

    network["name_mapping"] = rebuild_name_mapping(network)
    return network


def join_networks(inputs: List[Tuple[str, Dict[str, Any]]], postmerge: bool = True) -> Dict[str, Any]:
    """Union already-loaded per-venue networks ([(venue, network), ...]) into a joint network."""
    logger.info("Building joint entities")
    joint = build_joint_entities(inputs)
    for et in ENTITY_TYPES:
        logger.info("  %s: %d (after canonical-name union)", et, len(joint[et]))

    logger.info("Building joint relationships")
    joint_rels = build_joint_relationships(inputs)
    logger.info("  relationships: %d", len(joint_rels))

    network: Dict[str, Any] = {
        "metadata": {
            "joint_of": [c for c, _ in inputs],
            "n_conferences": len(inputs),
        },
        "constructs": joint["constructs"],
        "measurements": joint["measurements"],
        "behaviors": joint["behaviors"],
        "relationships": joint_rels,
    }

    # All papers across venues
    all_papers = []
    for conf, net in inputs:
        for p in net.get("papers", []) or []:
            all_papers.append({"conference": conf, "paper": p})
    network["papers"] = all_papers
    network["paper_count_by_conference"] = {
        conf: len(net.get("papers", []) or []) for conf, net in inputs
    }

    if postmerge:
        logger.info("Deterministic post-merge of surface variants")
        network = deterministic_post_merge(network)

    for et in ENTITY_TYPES:
        n = len(network[et])
        n_multi = sum(1 for g in network[et] if g.get("paper_count", 0) >= 2)
        n_cross = sum(1 for g in network[et] if len(g.get("paper_count_by_conference", {})) >= 2)
        logger.info("  %s: %d total | %d (>=2 papers) | %d (in more than one venue)",
                    et, n, n_multi, n_cross)
    logger.info("  relationships: %d", len(network["relationships"]))
    logger.info("  papers: %d", len(network["papers"]))
    return network


def build_joint_network(
    inputs: Dict[str, str | Path],
    output_json: str | Path,
    postmerge: bool = True,
) -> Path:
    """Union the per-venue networks ``inputs`` ({venue: path}) into ``output_json``.

    Returns the written path.
    """
    loaded: List[Tuple[str, Dict[str, Any]]] = []
    for conf, path in inputs.items():
        with open(path) as f:
            net = json.load(f)
        loaded.append((conf, net))
        logger.info("Loaded [%s] %s: %s  relationships=%d", conf, path,
                    "  ".join(f"{et}={len(net.get(et, []) or [])}" for et in ENTITY_TYPES),
                    len(net.get("relationships", []) or []))

    network = join_networks(loaded, postmerge=postmerge)

    out_path = Path(output_json)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(network, f, indent=2)
    logger.info("Wrote %s", out_path)
    return out_path


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Union several venues' harmonized networks into one joint network.")
    parser.add_argument("--inputs", nargs="+", required=True, metavar="VENUE:PATH",
                        help="per-venue harmonized network files, as venue:path")
    parser.add_argument("--output", required=True, help="joint network JSON to write")
    parser.add_argument("--no-postmerge", action="store_true",
                        help="skip the deterministic post-merge of surface variants")
    parser.add_argument("--log-dir", default="logs")
    args = parser.parse_args(argv)

    setup_logging(run_name="join_union", log_dir=args.log_dir)
    inputs: Dict[str, str] = {}
    for spec in args.inputs:
        if ":" not in spec:
            parser.error(f"bad input spec (need venue:path): {spec}")
        conf, path = spec.split(":", 1)
        inputs[conf] = path
    build_joint_network(inputs, args.output, postmerge=not args.no_postmerge)


if __name__ == "__main__":
    main()
