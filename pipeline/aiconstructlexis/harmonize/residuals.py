"""Deterministic collapse of residual surface-variant duplicates after LLM harmonization.

Operates on a harmonized network JSON and merges entity groups (within each type) whose
canonical names differ only by:

- case, hyphenation, whitespace or punctuation, and a parenthetical ("BIG-Bench Hard (BBH)");
- a filler suffix, singular or plural ("X ability" / "X abilities" / "X capability" /
  "X capacity" / "X skill" / "X proficiency" / "X performance", and for instruments
  "X benchmark" / "X dataset" / "X evaluation" / "X judge" / "X framework" / "X task");
- a simple plural of the last word (s / es / ies);
- synonym nouns ("X comprehension" / "X awareness" / "X understanding";
  "X recognition" / "X identification");
- morphological variants ("Logical" / "Logic", "Numerical" / "Numeric",
  "Mathematical" / "Math");
- equivalent modality prefixes ("Multi-modal" / "Multimodal" / "Cross-modal");
- stopwords, and the word order of two-word names ("answer refusal" / "refusal answer").

When several groups collapse to one normalized form, the group with the highest
paper_count wins (ties: the shorter canonical name); the other groups' original_names,
papers, original_nodes and source_snippets_evidence are unioned into it. The
``name_mapping`` is then rebuilt and, when the simplified extraction JSON is given, the
relationships are re-aggregated against the updated mapping
(aiconstructlexis.harmonize.relationships).

``collapse_residuals(harmonized_json, simplified_json=None, out_json=None)`` writes the
result to ``out_json`` (default: ``harmonized_json`` itself) and keeps the network's schema.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

from aiconstructlexis.harmonize.relationships import aggregate as aggregate_raw_relationships
from aiconstructlexis.util.logging import setup_logging

logger = logging.getLogger(__name__)

_UNICODE_HYPHENS = "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"

_FILLER_SUFFIXES = (
    " abilities", " ability",
    " capabilities", " capability",
    " capacities", " capacity",
    " skills", " skill",
    " proficiencies", " proficiency",
    " performance",
    # Generic instrument/dataset suffixes
    " benchmark", " benchmarks",
    " dataset", " datasets",
    " evaluation", " evaluations",
    " judge", " judgment",
    " framework",
    " task", " tasks",
)

_SYNONYM_NOUNS = [
    ("comprehension", "understanding"),
    ("awareness", "understanding"),
    ("identification", "recognition"),
]

_MORPHOLOGY = [
    ("logical", "logic"),
    ("numerical", "numeric"),
    ("mathematical", "math"),
    ("multi modal", "multimodal"),
    ("cross modal", "multimodal"),
    ("x modal", "multimodal"),
    ("visio linguistic", "vision language"),
    ("visual linguistic", "vision language"),
]


def normalize(name: str) -> str:
    if not name:
        return ""
    s = name.strip().lower()
    for uh in _UNICODE_HYPHENS:
        s = s.replace(uh, "-")
    # Strip parenthetical acronyms / qualifiers: "BIG-Bench Hard (BBH)" -> "BIG-Bench Hard"
    s = re.sub(r"\s*\([^)]*\)\s*", " ", s)
    for ch in "-_/":
        s = s.replace(ch, " ")
    s = "".join(c if (c.isalnum() or c.isspace()) else " " for c in s)
    s = " ".join(s.split())
    # Strip trailing filler suffixes; repeat in case of stacked suffixes like
    # "X benchmark dataset" -> "X benchmark" -> "X"
    changed = True
    while changed:
        changed = False
        for suf in _FILLER_SUFFIXES:
            if s.endswith(suf):
                s = s[: -len(suf)].rstrip()
                changed = True
                break
    # Synonym nouns (per-word substitution at boundaries)
    for src, dst in _SYNONYM_NOUNS:
        s = re.sub(rf'\b{re.escape(src)}\b', dst, s)
    # Morphological variants (multi-word ones first to avoid overlap)
    for src, dst in sorted(_MORPHOLOGY, key=lambda x: -len(x[0])):
        s = re.sub(rf'\b{re.escape(src)}\b', dst, s)
    # Simple plural, applied to the last word only so "across" does not become "acros"
    parts = s.split()
    if parts:
        last = parts[-1]
        if last.endswith("ies") and len(last) > 3:
            parts[-1] = last[:-3] + "y"
        elif last.endswith("ses") and len(last) > 3:
            parts[-1] = last[:-2]
        elif last.endswith("s") and not last.endswith("ss") and len(last) > 1:
            parts[-1] = last[:-1]
        s = " ".join(parts)
    # Drop stopwords ("to", "of", "the", ...). Keep single-character tokens
    # (digits, acronym pieces) since they may carry meaning like "Llama Guard 2".
    _STOP = {"a", "an", "the", "of", "to", "for", "in", "on", "with", "by",
             "and", "or", "as"}
    parts = [p for p in s.split() if p not in _STOP]
    s = " ".join(parts)
    # Sort tokens to catch word-order swaps ("refusal answer" / "answer refusal").
    # Only two-word names are folded, so that a domain qualifier in a longer name
    # ("medical", "visual", "audio", ...) keeps its meaning.
    if len(parts) == 2:
        s = " ".join(sorted(parts))
    return " ".join(s.split())


def _union_into(winner: Dict[str, Any], loser: Dict[str, Any]) -> None:
    """Merge loser's metadata into winner in-place."""
    # original_names
    wn = set(winner.get("original_names") or [])
    for n in loser.get("original_names") or []:
        if n not in wn:
            winner.setdefault("original_names", []).append(n)
            wn.add(n)
    # papers
    wp = set(winner.get("papers") or [])
    for p in loser.get("papers") or []:
        if p not in wp:
            winner.setdefault("papers", []).append(p)
            wp.add(p)
    winner["paper_count"] = len(winner.get("papers") or [])
    # original_nodes
    wn_nodes = winner.setdefault("original_nodes", {})
    for k, v in (loser.get("original_nodes") or {}).items():
        if k not in wn_nodes:
            wn_nodes[k] = v
        else:
            # Merge papers under this original_node too
            existing_papers = set(wn_nodes[k].get("papers") or [])
            for p in v.get("papers") or []:
                if p not in existing_papers:
                    wn_nodes[k].setdefault("papers", []).append(p)
                    existing_papers.add(p)
    # source_snippets_evidence
    we = winner.setdefault("source_snippets_evidence", [])
    we_set = {json.dumps(s, sort_keys=True) if isinstance(s, dict) else s for s in we}
    for s in loser.get("source_snippets_evidence") or []:
        sig = json.dumps(s, sort_keys=True) if isinstance(s, dict) else s
        if sig not in we_set:
            we.append(s)
            we_set.add(sig)


def collapse(groups: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int]:
    """Collapse groups whose canonical_name normalizes to the same form.

    Returns (groups, number of groups merged away). Within a collapsed set the group with
    the highest paper_count wins (ties: the shorter canonical name) and the others'
    metadata is unioned into it; groups whose canonical name is unique keep their order.
    """
    by_norm: Dict[str, List[int]] = defaultdict(list)
    for i, g in enumerate(groups):
        c = g.get("canonical_name", "")
        if c:
            by_norm[normalize(c)].append(i)

    keep: set = set()
    merged_count = 0
    out: List[Dict[str, Any]] = []
    consumed: set = set()
    for norm_key, idx_list in by_norm.items():
        if len(idx_list) == 1:
            keep.add(idx_list[0])
        else:
            # Pick winner: highest paper_count; tiebreak shorter canonical
            winner_idx = max(
                idx_list,
                key=lambda i: (
                    groups[i].get("paper_count", 0),
                    -len(groups[i].get("canonical_name", "")),
                ),
            )
            winner = dict(groups[winner_idx])  # shallow copy
            for i in idx_list:
                if i == winner_idx:
                    continue
                _union_into(winner, groups[i])
                merged_count += 1
                consumed.add(i)
            out.append(winner)
            consumed.add(winner_idx)
    # Add the singletons
    for i, g in enumerate(groups):
        if i in keep and i not in consumed:
            out.append(g)
    return out, merged_count


def rebuild_name_mapping(network: Dict[str, Any]) -> Dict[str, str]:
    nm: Dict[str, str] = {}
    for etype in ("constructs", "measurements", "behaviors"):
        for g in network.get(etype, []) or []:
            c = g.get("canonical_name", "")
            if not c:
                continue
            nm[c] = c
            for orig in g.get("original_names") or []:
                if orig:
                    nm[orig] = c
    return nm


def _load_json(path) -> Any:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def collapse_residuals(harmonized_json, simplified_json=None, out_json=None) -> Path:
    """Collapse residual surface-variant duplicates in a harmonized network.

    Collapses the groups of each entity type (see ``collapse``), rebuilds ``name_mapping``
    and, when ``simplified_json`` is given, re-aggregates the relationships against the
    updated mapping. Writes the network to ``out_json`` (default: ``harmonized_json``
    itself) and returns the path written.
    """
    net = _load_json(harmonized_json)

    logger.info(
        "Before: constructs %d, measurements %d, behaviors %d, relationships %d",
        len(net.get("constructs", [])), len(net.get("measurements", [])),
        len(net.get("behaviors", [])), len(net.get("relationships", [])),
    )

    total_merged = 0
    for et in ("constructs", "measurements", "behaviors"):
        items = net.get(et, []) or []
        if not items:
            continue
        before = len(items)
        net[et], merged = collapse(items)
        total_merged += merged
        if merged > 0:
            logger.info("  %s: %d -> %d (-%d)", et, before, len(net[et]), merged)
        else:
            logger.info("  %s: %d (no residual duplicates)", et, before)
    logger.info("Total residual merges: %d", total_merged)

    net["name_mapping"] = rebuild_name_mapping(net)
    logger.info("Rebuilt name_mapping: %d entries", len(net["name_mapping"]))

    if simplified_json:
        logger.info("Re-aggregating relationships against the updated mapping")
        aggregated, stats = aggregate_raw_relationships(_load_json(simplified_json), net)
        net["relationships"] = aggregated
        logger.info(
            "  Raw relationships %d -> aggregated %d; unresolved sources %d, "
            "unresolved targets %d",
            stats["n_raw"], stats["n_aggregated"],
            stats["n_unresolved_src"], stats["n_unresolved_tgt"],
        )

    out_path = Path(out_json) if out_json else Path(harmonized_json)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(net, f, indent=2)
    logger.info("Wrote %s", out_path)
    return out_path


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Collapse residual surface-variant duplicates of a harmonized network "
                    "and rebuild its name mapping (deterministic, no LLM)."
    )
    parser.add_argument("--harmonized", required=True, help="Harmonized network JSON")
    parser.add_argument("--simplified", default=None,
                        help="Simplified extraction JSON; if given, the relationships are "
                             "re-aggregated against the updated mapping")
    parser.add_argument("--out", default=None,
                        help="Write here instead of rewriting --harmonized in place")
    parser.add_argument("--log-dir", default="logs", help="Directory for the run log")
    args = parser.parse_args(argv)

    setup_logging(run_name="collapse_residuals", log_dir=args.log_dir)
    collapse_residuals(args.harmonized, simplified_json=args.simplified, out_json=args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
