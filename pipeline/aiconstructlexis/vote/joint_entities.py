"""Canonical-level majority vote on the entities of the joint (cross-venue) network.

The rule is the one of ``aiconstructlexis.vote.entities`` applied per venue: for each
entity, venue and paper, the models that proposed any member name of the entity for that
paper are counted, and the (entity, venue, paper) credit stands when at least
``threshold`` models contributed. Votes are counted at the canonical level, so surface
variants of one concept count as one vote.

Inputs
  - the joint network JSON (after the cross-venue union and merge), whose entities carry
    ``canonical_name`` and ``original_names``, plus an optional ``name_mapping``;
  - ``trials``: {venue: trials directory}, each directory holding
    ``<model label>/entity_trials.json`` for the models of that venue (a model missing
    from one venue is skipped with a warning).

Output: each entity's ``papers`` ([{"conference", "paper"}]), ``papers_by_conference``,
``paper_count`` and ``paper_count_by_conference`` are replaced by the credits that passed
the vote, and a ``_canonical_mv`` record (threshold, papers seen, papers kept) is added.
Entities with no passing paper are dropped. The network is rewritten in place unless
``out_json`` is given.
"""
from __future__ import annotations

import argparse
import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List

from aiconstructlexis.util.logging import setup_logging
from aiconstructlexis.vote.entities import ENTITY_TYPES, build_name_mapping, canonical_sets

logger = logging.getLogger(__name__)


def collect_joint_contributions(
    net: Dict[str, Any],
    trials: Dict[str, str | Path],
    models: list,
) -> Dict[str, Dict[str, Dict[str, Dict[str, set]]]]:
    """{entity type: canonical -> venue -> paper -> set(models that contributed)}."""
    nm = build_name_mapping(net)
    canon_sets = canonical_sets(net)
    contrib: Dict[str, Dict[str, Dict[str, Dict[str, set]]]] = {
        et: defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
        for et in ENTITY_TYPES
    }
    for conf, trials_dir in trials.items():
        for model in models:
            path = Path(trials_dir) / model / "entity_trials.json"
            if not path.is_file():
                logger.warning("missing %s", path)
                continue
            with open(path) as f:
                model_trials = json.load(f)
            for paper, paper_trials in model_trials.items():
                for trial in paper_trials:
                    if not isinstance(trial, dict):
                        continue
                    nn = trial.get("Nomological Network") or trial
                    if not isinstance(nn, dict):
                        continue
                    for et in ENTITY_TYPES:
                        for ent in nn.get(et, []) or []:
                            if not isinstance(ent, dict):
                                continue
                            raw = (ent.get("name") or "").strip()
                            if not raw:
                                continue
                            canon = nm.get(raw.lower())
                            if canon and canon in canon_sets[et]:
                                contrib[et][canon][conf][paper].add(model)
    return contrib


def apply_joint_mv(net: Dict[str, Any], contrib, threshold: int) -> Dict[str, Dict[str, int]]:
    """Replace each entity's paper fields by the (venue, paper) credits that passed the vote.

    Returns per-type counts: {etype: {kept, dropped}}.
    """
    stats: Dict[str, Dict[str, int]] = {}
    for et in ENTITY_TYPES:
        new_groups: List[Dict[str, Any]] = []
        dropped = 0
        for g in net.get(et, []) or []:
            canon = (g.get("canonical_name") or "").strip()
            cmap = contrib[et].get(canon, {})
            valid = []
            pbc: Dict[str, List[str]] = {}
            for conf, papers in cmap.items():
                for paper, paper_models in papers.items():
                    if len(paper_models) >= threshold:
                        valid.append({"conference": conf, "paper": paper})
                        pbc.setdefault(conf, []).append(paper)
            if not valid:
                dropped += 1
                continue
            g["papers"] = valid
            g["papers_by_conference"] = pbc
            g["paper_count"] = len(valid)
            g["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
            g["_canonical_mv"] = {
                "threshold": threshold,
                "n_papers_total": sum(len(p) for p in cmap.values()),
                "n_papers_mv": len(valid),
            }
            new_groups.append(g)
        logger.info("%s: kept=%d, dropped=%d", et, len(new_groups), dropped)
        net[et] = new_groups
        stats[et] = {"kept": len(new_groups), "dropped": dropped}
    return stats


def vote_joint_entities(
    joint_json: str | Path,
    trials: Dict[str, str | Path],
    models: list,
    threshold: int = 2,
    out_json: str | Path | None = None,
) -> Path:
    """Run the canonical-level entity vote on the joint network.

    ``trials`` maps each venue label to its trials directory. The network is rewritten in
    place unless ``out_json`` is given. Returns the written path.
    """
    joint_path = Path(joint_json)
    with open(joint_path) as f:
        net = json.load(f)
    contrib = collect_joint_contributions(net, trials, list(models))
    apply_joint_mv(net, contrib, threshold)
    out_path = Path(out_json) if out_json else joint_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(net, f, indent=2)
    logger.info("Wrote %s", out_path)
    return out_path


def parse_venue_specs(specs: List[str]) -> Dict[str, str]:
    """``venue:path`` command-line items -> {venue: path}."""
    out: Dict[str, str] = {}
    for spec in specs:
        if ":" not in spec:
            raise ValueError(f"expected venue:path, got {spec!r}")
        venue, path = spec.split(":", 1)
        out[venue] = path
    return out


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Canonical-level majority vote on the entities of the joint network.")
    parser.add_argument("--joint", required=True, help="joint network JSON")
    parser.add_argument("--trials", nargs="+", required=True, metavar="VENUE:DIR",
                        help="per-venue trials directories, as venue:dir")
    parser.add_argument("--models", nargs="+", required=True,
                        help="model labels matching <dir>/<label>/ directories")
    parser.add_argument("--threshold", type=int, default=2,
                        help="minimum number of models that must contribute (default: 2)")
    parser.add_argument("--out", default=None, help="write here instead of rewriting --joint")
    parser.add_argument("--log-dir", default="logs")
    args = parser.parse_args(argv)

    setup_logging(run_name="vote_joint_entities", log_dir=args.log_dir)
    try:
        trials = parse_venue_specs(args.trials)
    except ValueError as e:
        parser.error(str(e))
    vote_joint_entities(args.joint, trials, args.models, threshold=args.threshold,
                        out_json=args.out)


if __name__ == "__main__":
    main()
