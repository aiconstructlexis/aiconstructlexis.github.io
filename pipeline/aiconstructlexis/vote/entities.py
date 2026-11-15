"""Canonical-level majority vote on the entities of one venue's harmonized network.

Extraction runs several models on every paper, and harmonization groups their surface
names into canonical entities. The vote is counted at the canonical level so that surface
variants of one concept count as one vote: for each entity and paper, every model that
proposed any member name of that entity for that paper contributes one vote, and the
(entity, paper) credit stands when at least ``threshold`` models contributed. An entity's
``paper_count`` therefore reflects its cross-model support, not the agreement of the
models on one spelling.

Inputs
  - a harmonized network JSON with ``constructs``, ``measurements`` and ``behaviors``
    (each entity has ``canonical_name`` and ``original_names``) and an optional
    ``name_mapping`` of surface name -> canonical name;
  - a trials directory holding ``<model label>/entity_trials.json`` for each model: a
    mapping from paper to its list of extraction trials, each trial a dict whose
    "Nomological Network" (or the trial itself) lists ``constructs``, ``measurements``
    and ``behaviors`` as ``{"name": ...}`` records.

Output: the same network with each entity's ``papers`` and ``paper_count`` replaced by the
papers that passed the vote, plus a ``_canonical_mv`` record (threshold, papers seen,
papers kept). Entities with no passing paper are dropped when ``drop_zero`` is set. The
network is rewritten in place (atomically) unless ``out_json`` is given.

A member name is credited only to the entity type that owns its canonical entity, so a
measurement name never adds a vote to a construct of the same spelling.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Set

from aiconstructlexis.util.logging import setup_logging

logger = logging.getLogger(__name__)

ENTITY_TYPES = ("constructs", "measurements", "behaviors")


def build_name_mapping(network: Dict[str, Any]) -> Dict[str, str]:
    """Lowercased surface name -> canonical name, from every entity and ``name_mapping``."""
    nm: Dict[str, str] = {}
    for etype in ENTITY_TYPES:
        for g in network.get(etype, []) or []:
            canon = (g.get("canonical_name") or "").strip()
            if not canon:
                continue
            nm[canon.strip().lower()] = canon
            for orig in g.get("original_names", []) or []:
                if orig:
                    nm[orig.strip().lower()] = canon
    # name_mapping fills the keys no entity name covers (surface variants collapsed earlier).
    for orig, canon in (network.get("name_mapping") or {}).items():
        if orig and canon:
            nm.setdefault(orig.strip().lower(), canon)
    return nm


def canonical_sets(network: Dict[str, Any]) -> Dict[str, Set[str]]:
    """{entity type: set of canonical names of that type}."""
    return {
        et: {(g.get("canonical_name") or "").strip()
             for g in network.get(et, []) or []
             if (g.get("canonical_name") or "").strip()}
        for et in ENTITY_TYPES
    }


def collect_canonical_contributions(
    trials_dir: Path,
    models: list,
    name_mapping: Dict[str, str],
    canon_sets: Dict[str, Set[str]],
) -> Dict[str, Dict[str, Dict[str, Set[str]]]]:
    """For each entity type, build canonical -> paper -> set(models that contributed).

    ``canon_sets`` restricts which canonical names count for each type, so a measurement
    canonical does not add votes to the construct ledger.
    """
    contributions: Dict[str, Dict[str, Dict[str, Set[str]]]] = {
        "constructs": defaultdict(lambda: defaultdict(set)),
        "measurements": defaultdict(lambda: defaultdict(set)),
        "behaviors": defaultdict(lambda: defaultdict(set)),
    }
    for model in models:
        path = Path(trials_dir) / model / "entity_trials.json"
        if not path.is_file():
            logger.warning("missing trials for %s: %s", model, path)
            continue
        with open(path) as f:
            trials = json.load(f)
        for paper, paper_trials in trials.items():
            for trial in paper_trials:
                if not isinstance(trial, dict):
                    continue
                nn = trial.get("Nomological Network") or trial
                if not isinstance(nn, dict):
                    continue
                for etype in ENTITY_TYPES:
                    for ent in nn.get(etype, []) or []:
                        if not isinstance(ent, dict):
                            continue
                        raw = (ent.get("name") or "").strip()
                        if not raw:
                            continue
                        canon = name_mapping.get(raw.lower())
                        if canon is None:
                            continue
                        # Credit only the entity type that owns this canonical name.
                        if canon in canon_sets.get(etype, set()):
                            contributions[etype][canon][paper].add(model)
    return contributions


def apply_mv(
    network: Dict[str, Any],
    contributions: Dict[str, Dict[str, Dict[str, Set[str]]]],
    threshold: int,
    drop_zero_papers: bool = False,
) -> Dict[str, Dict[str, int]]:
    """Replace each entity's ``papers`` and ``paper_count`` by the papers that passed the vote.

    Returns per-type counts: {etype: {kept, dropped, papers_added, papers_removed}}.
    """
    stats: Dict[str, Dict[str, int]] = {}
    for etype in ENTITY_TYPES:
        kept_groups = []
        dropped = 0
        papers_added = 0
        papers_removed = 0
        for g in network.get(etype, []) or []:
            canon = (g.get("canonical_name") or "").strip()
            old_papers = set(g.get("papers", []) or [])
            paper_models = contributions[etype].get(canon, {})
            mv_papers = {p for p, ms in paper_models.items() if len(ms) >= threshold}
            if not mv_papers and drop_zero_papers:
                dropped += 1
                continue
            papers_added += len(mv_papers - old_papers)
            papers_removed += len(old_papers - mv_papers)
            g["papers"] = sorted(mv_papers)
            g["paper_count"] = len(mv_papers)
            g["_canonical_mv"] = {
                "threshold": threshold,
                "n_papers_total": len(paper_models),
                "n_papers_mv": len(mv_papers),
            }
            kept_groups.append(g)
        network[etype] = kept_groups
        stats[etype] = {
            "kept": len(kept_groups),
            "dropped": dropped,
            "papers_added": papers_added,
            "papers_removed": papers_removed,
        }
    return stats


def write_json_atomic(obj: Any, path: Path, indent: int = 2) -> None:
    """Write ``obj`` to ``path`` through a temporary file in the same directory."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=indent)
    os.replace(tmp, path)


def vote_entities(
    harmonized_json: str | Path,
    trials_dir: str | Path,
    models: list,
    threshold: int = 2,
    drop_zero: bool = True,
    out_json: str | Path | None = None,
) -> Path:
    """Run the canonical-level entity vote on one venue's harmonized network.

    ``models`` are the trial labels (``<trials_dir>/<label>/entity_trials.json``). The
    network is rewritten in place unless ``out_json`` is given. Returns the written path.
    """
    h_path = Path(harmonized_json)
    with open(h_path) as f:
        network = json.load(f)
    logger.info("Loaded %s: %s", h_path,
                "  ".join(f"{et}={len(network.get(et, []) or [])}" for et in ENTITY_TYPES))

    name_mapping = build_name_mapping(network)
    logger.info("Name mapping: %d entries", len(name_mapping))

    contributions = collect_canonical_contributions(
        Path(trials_dir), list(models), name_mapping, canonical_sets(network),
    )
    logger.info("Applying canonical vote with threshold=%d", threshold)
    stats = apply_mv(network, contributions, threshold, drop_zero_papers=drop_zero)
    for et, s in stats.items():
        logger.info("  %s: kept=%d, dropped=%d, papers added=%d, removed=%d",
                    et, s["kept"], s["dropped"], s["papers_added"], s["papers_removed"])

    out_path = Path(out_json) if out_json else h_path
    write_json_atomic(network, out_path)
    logger.info("Wrote %s", out_path)
    return out_path


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Canonical-level majority vote on the entities of a harmonized network.")
    parser.add_argument("--harmonized", required=True, help="harmonized network JSON")
    parser.add_argument("--trials-dir", required=True,
                        help="directory holding <model label>/entity_trials.json per model")
    parser.add_argument("--models", nargs="+", required=True,
                        help="model labels matching <trials-dir>/<label>/ directories")
    parser.add_argument("--threshold", type=int, default=2,
                        help="minimum number of models that must contribute (default: 2)")
    parser.add_argument("--drop-zero", action=argparse.BooleanOptionalAction, default=True,
                        help="drop entities with no paper passing the vote (default: on)")
    parser.add_argument("--out", default=None, help="write here instead of rewriting --harmonized")
    parser.add_argument("--log-dir", default="logs")
    args = parser.parse_args(argv)

    setup_logging(run_name="vote_entities", log_dir=args.log_dir)
    vote_entities(args.harmonized, args.trials_dir, args.models, threshold=args.threshold,
                  drop_zero=args.drop_zero, out_json=args.out)


if __name__ == "__main__":
    main()
