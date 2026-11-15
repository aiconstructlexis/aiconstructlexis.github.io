"""Deterministic relationship aggregation (no LLM calls).

Reads the simplified extraction JSON (raw relationships per paper) and a harmonized network
(canonical entity groups and ``name_mapping``), and rebuilds the network's relationships at
the canonical level:

1. The source and target of each raw relationship are mapped to canonical names through
   the harmonized name mapping (original name -> canonical name, completed with every
   group's canonical and original names).
2. A name that is not in the mapping is looked up after normalization (case, hyphens,
   underscores, slashes, punctuation and whitespace are ignored), so minor surface
   variants still resolve; a name that still does not resolve is kept as it is.
3. Relationships are bucketed by (canonical source, canonical target, type). ``related``
   and ``correlates`` are symmetric, so (A, B) and (B, A) share a bucket; ``causes`` and
   ``measured_by`` keep their direction. Self-loops are dropped.
4. Each bucket unions the evidence and the papers of its raw rows and counts the papers.

``aggregate_relationships(simplified_json, harmonized_json, out_json=None)`` writes the
aggregated relationships into the harmonized network (in place unless ``out_json`` is
given). The output keeps the harmonized network's schema; ``relationships`` becomes a list
of ``{"source", "target", "type", "evidence", "papers", "paper_count"}`` sorted by
descending paper count, then source and target.
"""
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple

from aiconstructlexis.util.logging import setup_logging

logger = logging.getLogger(__name__)

_UNICODE_HYPHENS = "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"


def _normalize(name: str) -> str:
    """Aggressive normalization for fuzzy lookup against the canonical map."""
    if not name:
        return ""
    s = name.strip().lower()
    for uh in _UNICODE_HYPHENS:
        s = s.replace(uh, "-")
    for ch in "-_/":
        s = s.replace(ch, " ")
    s = "".join(c if (c.isalnum() or c.isspace()) else " " for c in s)
    s = " ".join(s.split())
    return s


def build_canonical_lookup(network: Dict[str, Any]) -> Dict[str, str]:
    """Build a robust original_name -> canonical_name mapping.

    Combines (in order of precedence):
      - explicit name_mapping field if present
      - canonical_name -> canonical_name identity
      - original_names -> canonical_name from each group
    Each name is also indexed by its normalized form so we can fall back
    when an extracted relationship name doesn't exactly match a stored form.
    """
    lookup: Dict[str, str] = {}
    norm_lookup: Dict[str, str] = {}

    # Explicit mapping (if any)
    for orig, canon in (network.get("name_mapping") or {}).items():
        if orig and canon:
            lookup[orig] = canon
            norm_lookup[_normalize(orig)] = canon

    # From each group
    for etype in ("constructs", "measurements", "behaviors"):
        for g in network.get(etype, []) or []:
            canon = g.get("canonical_name", "")
            if not canon:
                continue
            lookup[canon] = canon
            norm_lookup[_normalize(canon)] = canon
            for orig in g.get("original_names", []) or []:
                if orig:
                    lookup.setdefault(orig, canon)
                    norm_lookup.setdefault(_normalize(orig), canon)

    return {"exact": lookup, "norm": norm_lookup}


def resolve(name: str, lookup: Dict[str, Dict[str, str]]) -> str:
    """Map a raw relationship endpoint name to its canonical, or return as-is."""
    if not name:
        return name
    name = name.strip()
    if name in lookup["exact"]:
        return lookup["exact"][name]
    n = _normalize(name)
    if n in lookup["norm"]:
        return lookup["norm"][n]
    # No match: keep the original name (it will surface as an orphan)
    return name


# Symmetric relationship types: (A, B, type) and (B, A, type) refer to the same edge.
# Asymmetric types must keep direction.
SYMMETRIC_TYPES = {"related", "correlates"}


def _bucket_key(src: str, tgt: str, rtype: str) -> Tuple[str, str, str]:
    """Build the dedup key. For symmetric types, sort the endpoints so that
    A->B and B->A map to the same bucket. For asymmetric types, keep direction."""
    if rtype in SYMMETRIC_TYPES:
        a, b = sorted([src, tgt])
        return (a, b, rtype)
    return (src, tgt, rtype)


def aggregate(simplified: Dict[str, Any], network: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], Dict[str, int]]:
    """Aggregate all raw relationships from simplified extraction into canonical
    relationships.

    Dedup behaviour:
      - `related` and `correlates` are treated as symmetric: (A, B) and (B, A) are one edge
      - `causes` and `measured_by` keep direction: A->B and B->A are different edges
      - Self-loops (A == B) are dropped
    """
    lookup = build_canonical_lookup(network)

    buckets: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    n_raw = 0
    n_resolved = 0
    n_unresolved_src = 0
    n_unresolved_tgt = 0
    n_self_loops = 0

    for paper_name, paper_data in simplified.items():
        # Skip non-paper entries
        if not isinstance(paper_data, dict):
            continue
        # Schema: paper_data["parsed_text"]["Nomological Network"]["relationships"]
        nn = (paper_data.get("parsed_text") or {}).get("Nomological Network")
        if nn is None:
            nn = paper_data.get("Nomological Network") or paper_data
        if not isinstance(nn, dict):
            continue
        rels = nn.get("relationships") or []
        for rel in rels:
            if not isinstance(rel, dict):
                continue
            n_raw += 1
            src_raw = (rel.get("source") or "").strip()
            tgt_raw = (rel.get("target") or "").strip()
            rtype = (rel.get("type") or "").strip().lower()
            if not src_raw or not tgt_raw or not rtype:
                continue
            src = resolve(src_raw, lookup)
            tgt = resolve(tgt_raw, lookup)
            if src not in lookup["exact"] and _normalize(src) not in lookup["norm"]:
                n_unresolved_src += 1
            if tgt not in lookup["exact"] and _normalize(tgt) not in lookup["norm"]:
                n_unresolved_tgt += 1
            # Drop self-loops
            if src == tgt:
                n_self_loops += 1
                continue
            n_resolved += 1
            key = _bucket_key(src, tgt, rtype)
            if key not in buckets:
                # Use the bucket's chosen ordering (already sorted for symmetric types)
                buckets[key] = {
                    "source": key[0],
                    "target": key[1],
                    "type": rtype,
                    "evidence": [],
                    "papers": [],
                    "paper_count": 0,
                }
            bucket = buckets[key]
            ev = rel.get("evidence")
            if ev:
                if isinstance(ev, list):
                    for e in ev:
                        if e and e not in bucket["evidence"]:
                            bucket["evidence"].append(e)
                elif ev not in bucket["evidence"]:
                    bucket["evidence"].append(ev)
            if paper_name and paper_name not in bucket["papers"]:
                bucket["papers"].append(paper_name)
            bucket["paper_count"] = len(bucket["papers"])

    aggregated = list(buckets.values())
    aggregated.sort(key=lambda r: (-r["paper_count"], r["source"], r["target"]))
    return aggregated, {
        "n_raw": n_raw,
        "n_resolved": n_resolved,
        "n_aggregated": len(aggregated),
        "n_unresolved_src": n_unresolved_src,
        "n_unresolved_tgt": n_unresolved_tgt,
        "n_self_loops_dropped": n_self_loops,
    }


def _load_json(path) -> Any:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def aggregate_relationships(simplified_json, harmonized_json, out_json=None) -> Path:
    """Rebuild the relationships of a harmonized network from the raw extraction.

    Reads the simplified extraction JSON and the harmonized network, aggregates the raw
    relationships at the canonical level (see ``aggregate``) and writes the network with
    its ``relationships`` replaced to ``out_json`` (default: ``harmonized_json`` itself).
    Returns the path written.
    """
    simplified = _load_json(simplified_json)
    network = _load_json(harmonized_json)
    logger.info(
        "Aggregating relationships of %d papers against %d constructs, %d measurements, "
        "%d behaviors",
        len(simplified), len(network.get("constructs", [])),
        len(network.get("measurements", [])), len(network.get("behaviors", [])),
    )
    aggregated, stats = aggregate(simplified, network)
    logger.info(
        "Relationships: %d raw -> %d aggregated (%.1f%% reduction); unresolved sources %d, "
        "unresolved targets %d, self-loops dropped %d",
        stats["n_raw"], stats["n_aggregated"],
        100 * (1 - stats["n_aggregated"] / max(stats["n_raw"], 1)),
        stats["n_unresolved_src"], stats["n_unresolved_tgt"], stats["n_self_loops_dropped"],
    )
    network["relationships"] = aggregated
    out_path = Path(out_json) if out_json else Path(harmonized_json)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(network, f, indent=2)
    logger.info("Wrote %s", out_path)
    return out_path


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Aggregate the raw relationships of a simplified extraction at the "
                    "canonical level of a harmonized network (deterministic, no LLM)."
    )
    parser.add_argument("--simplified", required=True, help="Simplified extraction JSON")
    parser.add_argument("--harmonized", required=True, help="Harmonized network JSON")
    parser.add_argument("--out", default=None,
                        help="Write here instead of rewriting --harmonized in place")
    parser.add_argument("--log-dir", default="logs", help="Directory for the run log")
    args = parser.parse_args(argv)

    setup_logging(run_name="aggregate_relationships", log_dir=args.log_dir)
    aggregate_relationships(args.simplified, args.harmonized, out_json=args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
