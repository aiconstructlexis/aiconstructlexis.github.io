"""One relationship type per unordered entity pair.

The relationship vote settles types within one paper, so two papers can leave the same
pair of entities on different types; related and correlates store their endpoints
sorted, so an opposite-direction related edge is the same unordered pair wearing a
second type; and curation operations that retype or redirect claims can land on a
(source, type, target) that already exists beside another type on the same pair. This
pass makes every unordered pair carry exactly one relationship type. The only exception
is causes in both directions (mutual causation), which is kept.

Rules per unordered pair {A, B} with more than one relationship, with the strictness
order of the relationship vote, causes > measured_by > correlates > related:

  Mutual causes: both causes edges stay; the papers of any related/correlates edges on
      the pair are folded into the causes direction with the larger paper_weight; on a
      weight tie each folded paper goes to both directions at 0.5 share (the vote's
      direction-tie rule).
  survivor="strictest" (default): the surviving type is the strictest type present, and
      its single edge absorbs every other edge's papers (causes, else measured_by, which
      after the type guard is unique and already construct/behavior -> instrument, else
      correlates over related).
  survivor="majority": the surviving type is the one with the greatest total paper_weight
      across the pair's edges, strictness breaking ties; the survivor is that type's
      heaviest edge (undirected types keep sorted-endpoint storage, as the vote does).

Fold mechanics, per paper keyed (conference, paper): a paper already on the survivor
keeps its claim and quote, and a folded quote only fills a gap; otherwise the paper is
appended with its quote. Provenance: every paper on a merged edge gets ``claim_type``,
the type of the edge it came from (the survivor's own papers get the survivor type), and
the merged edge gets ``type_breakdown`` ({type: n papers}) and ``consolidated_from`` (the
folded (source, type, target) triples), so a claim's original type stays visible inside
the surviving edge. ``type_share`` (1 / final edges on the pair the paper supports),
paper_count, paper_weight, papers_by_conference, paper_count_by_conference,
evidence_by_paper, evidence (up to MAX_EVIDENCE quotes) and n_papers_split (the inputs'
sum, capped at paper_count) are recomputed; the survivor's other fields are kept.
Entities, papers and every other section are untouched, and rerunning on consolidated
output is a no-op.

Invariants checked after the pass: no unordered pair carries more than one type, no
directed pair has parallel edges, every both-direction pair is causes/causes, the set of
(pair, conference, paper) claims is conserved, no claim sits on more than one final edge
of its pair outside a mutual-causes pair, and type_share matches the membership count
everywhere. The network is not written when any check fails.
"""
from __future__ import annotations

import argparse
import copy
import json
import logging
import os
from collections import Counter, defaultdict
from pathlib import Path

from aiconstructlexis.util.logging import setup_logging
from aiconstructlexis.util.names import STRICTNESS

logger = logging.getLogger(__name__)

SYMMETRIC_TYPES = {"related", "correlates"}
DIRECTED_TYPES = {"causes", "measured_by"}
MAX_EVIDENCE = 10  # as in the relationship vote


class ConsolidationError(RuntimeError):
    """The network has a shape this pass does not cover, or an invariant failed."""


def pair_key(r) -> tuple:
    return tuple(sorted((r["source"], r["target"])))


def edge_label(r) -> tuple:
    return (r["source"], r["type"], r["target"])


def weight(r) -> float:
    return round(r.get("paper_weight", 0.0), 4)


def describe(r) -> str:
    return f"{r['source']} -[{r['type']}]-> {r['target']} ({r['paper_count']}p, w={weight(r)})"


def fold_into(targets, folded) -> None:
    """Fold the papers of the `folded` edges into each edge in `targets`, in place.

    Two targets mean a mutual-causes weight tie: each folded paper lands on both causes
    directions, and the membership recount then puts it at 0.5 on each. The final
    type_share and the derived fields are recomputed afterwards by recompute().
    """
    for tgt in targets:
        tgt.setdefault("evidence_by_paper", [])
        quoted = {(e["conference"], e["paper"]) for e in tgt["evidence_by_paper"]}
        on_edge = {(p["conference"], p["paper"]) for p in tgt["papers"]}
        for p in tgt["papers"]:
            p.setdefault("claim_type", tgt["type"])
        n_split = tgt.get("n_papers_split", 0)
        cfrom = [list(lab) for lab in tgt.get("consolidated_from") or []]
        for f in folded:
            n_split += f.get("n_papers_split", 0)
            cfrom.append(list(edge_label(f)))
            fquotes = {(e["conference"], e["paper"]): e for e in f.get("evidence_by_paper") or []}
            for p in f["papers"]:
                pk = (p["conference"], p["paper"])
                if pk not in on_edge:
                    tgt["papers"].append({"conference": pk[0], "paper": pk[1],
                                          "type_share": p.get("type_share", 1.0),
                                          "claim_type": p.get("claim_type", f["type"])})
                    on_edge.add(pk)
                # A paper already on the survivor keeps its claim and quote;
                # a folded quote only fills a gap.
                if pk not in quoted and pk in fquotes:
                    tgt["evidence_by_paper"].append(dict(fquotes[pk]))
                    quoted.add(pk)
        tgt["consolidated_from"] = cfrom
        tgt["_n_split_in"] = n_split


def recompute(r, member) -> None:
    """Rebuild a merged edge's derived fields from its papers and quotes."""
    for p in r["papers"]:
        p["type_share"] = round(1 / member[(p["conference"], p["paper"])], 4)
    r["paper_count"] = len(r["papers"])
    r["paper_weight"] = round(sum(p["type_share"] for p in r["papers"]), 4)
    pbc = {}
    for p in r["papers"]:
        pbc.setdefault(p["conference"], []).append(p["paper"])
    r["papers_by_conference"] = pbc
    r["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
    ev = []
    for e in r.get("evidence_by_paper") or []:
        q = e.get("quote") or ""
        if q and q not in ev and len(ev) < MAX_EVIDENCE:
            ev.append(q)
    r["evidence"] = ev
    r["n_papers_split"] = min(r.pop("_n_split_in", r.get("n_papers_split", 0)), r["paper_count"])
    bd = Counter(p.get("claim_type", r["type"]) for p in r["papers"])
    r["type_breakdown"] = {t: bd[t] for t in STRICTNESS if t in bd}


def consolidate(net, mode: str = "strictest"):
    """Return (new net, report). Pure: the input net is not modified."""
    N = copy.deepcopy(net)
    rels = N.get("relationships") or []
    by_pair = defaultdict(list)
    for r in rels:
        by_pair[pair_key(r)].append(r)
    report = {"survivor_mode": mode, "relationships_in": len(rels),
              "pairs_affected": 0, "edges_merged": 0}
    actions, survivor_types = Counter(), Counter()
    pair_log = []
    dropped = set()

    for pk in sorted(by_pair):
        group = by_pair[pk]
        if len(group) < 2:
            continue
        report["pairs_affected"] += 1
        edges_in = [describe(r) for r in group]
        causes = [r for r in group if r["type"] == "causes"]
        c_dirs = {(r["source"], r["target"]) for r in causes}
        if len(causes) != len(c_dirs) or len(causes) > 2:
            raise ConsolidationError(f"parallel same-direction causes edges on {pk}: "
                                     "the rules assume none")
        if len(c_dirs) == 2:
            # Mutual causation: both directions stay.
            others = [r for r in group if r["type"] != "causes"]
            if any(r["type"] not in SYMMETRIC_TYPES for r in others):
                raise ConsolidationError(f"mutual causes beside a directed non-causes edge on {pk}: "
                                         "not covered by the rules")
            if not others:
                actions["keep_both"] += 1
                pair_log.append({"pair": list(pk), "action": "keep_both", "edges_in": edges_in,
                                 "survivors": [list(edge_label(r)) for r in causes],
                                 "merged": []})
                continue
            w0, w1 = weight(causes[0]), weight(causes[1])
            targets = causes if w0 == w1 else [causes[0] if w0 > w1 else causes[1]]
            folded, action = others, "keep_both_fold_undirected"
            survivor_types["causes (both directions)"] += 1
        else:
            if mode == "strictest":
                stype = min({r["type"] for r in group}, key=STRICTNESS.index)
            else:
                wt = defaultdict(float)
                for r in group:
                    wt[r["type"]] += weight(r)
                top = round(max(wt.values()), 4)
                stype = min((t for t, v in wt.items() if round(v, 4) == top),
                            key=STRICTNESS.index)
            cands = [r for r in group if r["type"] == stype]
            if mode == "strictest" and len(cands) > 1:
                raise ConsolidationError(f"more than one {stype} edge on {pk}: "
                                         "the rules assume a single survivor")
            # majority: the surviving type's heaviest edge sets the direction.
            surv = max(cands, key=lambda r: (weight(r), r["source"]))
            if stype in SYMMETRIC_TYPES and surv["source"] > surv["target"]:
                surv["source"], surv["target"] = surv["target"], surv["source"]  # as make_label
            targets, folded = [surv], [r for r in group if r is not surv]
            action = ("fold_undirected_into_directed" if stype in DIRECTED_TYPES
                      else "merge_same_direction")
            survivor_types[stype] += 1
        fold_into(targets, folded)
        dropped.update(id(f) for f in folded)
        report["edges_merged"] += len(folded)
        actions[action] += 1
        finals = [r for r in group if id(r) not in dropped]
        member = Counter()
        for r in finals:
            for p in r["papers"]:
                member[(p["conference"], p["paper"])] += 1
        for r in finals:
            if "_n_split_in" in r:  # a fold target; untouched edges keep their fields
                recompute(r, member)
        pair_log.append({"pair": list(pk), "action": action, "edges_in": edges_in,
                         "survivors": [list(edge_label(r)) for r in finals],
                         "merged": [list(edge_label(f)) for f in folded]})

    out = [r for r in rels if id(r) not in dropped]
    out.sort(key=lambda r: -r["paper_count"])
    N["relationships"] = out
    report["relationships_out"] = len(out)
    report["actions"] = dict(actions)
    report["survivor_types"] = dict(survivor_types)
    report["pairs"] = pair_log
    if report["edges_merged"]:  # a rerun that merges nothing leaves the net byte-identical
        N.setdefault("metadata", {})["pair_type_consolidation"] = {
            "rule": "one relationship type per unordered pair; mutual causes kept; "
                    f"survivor by {mode} with strictness causes > measured_by > correlates "
                    "> related; folded papers keep claim_type, merged edges carry "
                    "type_breakdown and consolidated_from",
            "survivor": mode,
            "pairs_affected": report["pairs_affected"],
            "edges_merged": report["edges_merged"],
        }
    return N, report


def check_invariants(in_net, out_net):
    """Post-run checks.

    Returns (failures, stats): failures is a list of messages, empty when all pass.
    """
    fails = []
    rels = out_net.get("relationships") or []
    types_by_pair, dirs_by_pair = defaultdict(set), defaultdict(set)
    directed = Counter()
    for r in rels:
        pk = pair_key(r)
        types_by_pair[pk].add(r["type"])
        dirs_by_pair[pk].add((r["source"], r["target"]))
        directed[(r["source"], r["target"])] += 1
    multi = sorted(pk for pk, ts in types_by_pair.items() if len(ts) > 1)
    if multi:
        fails.append(f"{len(multi)} unordered pairs still carry >1 type, e.g. {multi[:3]}")
    dup = sorted(k for k, n in directed.items() if n > 1)
    if dup:
        fails.append(f"{len(dup)} directed pairs with parallel edges, e.g. {dup[:3]}")
    bidir = sorted(pk for pk, ds in dirs_by_pair.items() if len(ds) > 1)
    bad_bidir = [pk for pk in bidir if types_by_pair[pk] != {"causes"}]
    if bad_bidir:
        fails.append(f"{len(bad_bidir)} both-direction pairs that are not causes/causes, "
                     f"e.g. {bad_bidir[:3]}")

    def claim_set(net):
        return {(pair_key(r), p["conference"], p["paper"])
                for r in net.get("relationships") or [] for p in r["papers"]}

    ci, co = claim_set(in_net), claim_set(out_net)
    if ci != co:
        fails.append(f"claims not conserved: {len(ci - co)} lost, {len(co - ci)} invented")
    member = Counter()
    for r in rels:
        for p in r["papers"]:
            member[(pair_key(r), p["conference"], p["paper"])] += 1
    # Exactly one final edge per claim, except on a mutual-causes pair (direction
    # ties and the mutual-causes tie-fold legitimately sit on both directions at 0.5).
    over = [k for k, n in member.items()
            if n > 2 or (n == 2 and types_by_pair[k[0]] != {"causes"})]
    if over:
        fails.append(f"{len(over)} claims on more than one final edge of their pair "
                     f"outside a mutual-causes pair, e.g. {sorted(over)[:3]}")
    bad_share = sum(1 for r in rels for p in r["papers"]
                    if abs(p.get("type_share", 1.0)
                           - round(1 / member[(pair_key(r), p["conference"], p["paper"])], 4)) > 1e-9)
    if bad_share:
        fails.append(f"{bad_share} paper claims whose type_share is not "
                     "1/(final edges supported on the pair)")
    for et in ("constructs", "measurements", "behaviors", "papers"):
        if len(in_net.get(et) or []) != len(out_net.get(et) or []):
            fails.append(f"{et} changed size: only relationships may change")
    stats = {"both_direction_pairs": len(bidir),
             "both_direction_all_causes": not bad_bidir,
             "pairs_with_multiple_types": len(multi)}
    return fails, stats


def write_json(obj, path: Path, indent: int) -> None:
    """Symlink-safe atomic write: the temp file replaces the resolved target."""
    real = Path(os.path.realpath(path))
    real.parent.mkdir(parents=True, exist_ok=True)
    tmp = real.with_name(real.name + ".tmp")
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=indent, ensure_ascii=False)
    os.replace(tmp, real)


def run_consolidation(net, survivor: str = "strictest"):
    """consolidate() plus the invariant checks. Returns (new net, report); the report's
    ``invariants`` entry holds the failures (empty when all pass) and the pair statistics."""
    N, report = consolidate(net, survivor)
    fails, stats = check_invariants(net, N)
    report["invariants"] = {"failed": fails, **stats}

    logger.info("survivor mode: %s", survivor)
    logger.info("relationships: %d -> %d", report["relationships_in"], report["relationships_out"])
    logger.info("affected unordered pairs (>1 edge): %d, edges merged: %d",
                report["pairs_affected"], report["edges_merged"])
    logger.info("actions: %s", dict(sorted(report["actions"].items())))
    logger.info("survivor types: %s", dict(sorted(report["survivor_types"].items())))
    logger.info("both-direction pairs after: %d (all causes/causes: %s)",
                stats["both_direction_pairs"], stats["both_direction_all_causes"])
    for f in fails:
        logger.error("INVARIANT FAILED: %s", f)
    if not fails:
        logger.info("invariants: all pass")
    return N, report


def consolidate_pair_types(
    input_json: str | Path,
    out_json: str | Path | None = None,
    survivor: str = "strictest",
    report_json: str | Path | None = None,
) -> Path:
    """Consolidate the relationship types of ``input_json`` and write the result.

    ``survivor`` is "strictest" or "majority" (see the module docstring). The network is
    rewritten in place unless ``out_json`` is given; ``report_json`` receives the run's
    report. Raises ConsolidationError, and writes nothing, when an invariant fails.
    Returns the written path.
    """
    if survivor not in ("strictest", "majority"):
        raise ValueError(f"survivor must be 'strictest' or 'majority', got {survivor!r}")
    net = json.load(open(input_json, encoding="utf-8"))
    out_path = Path(out_json or input_json)
    N, report = run_consolidation(net, survivor)
    if report_json:
        write_json(report, Path(report_json), indent=2)
        logger.info("Wrote %s", report_json)
    fails = report["invariants"]["failed"]
    if fails:
        raise ConsolidationError("not writing: invariant checks failed: " + "; ".join(fails))
    write_json(N, out_path, indent=1)
    logger.info("Wrote %s", out_path)
    return out_path


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description="One relationship type per unordered entity pair "
                                            "(mutual causes kept).")
    p.add_argument("--input", required=True, help="network JSON")
    p.add_argument("--out", default=None, help="write here instead of rewriting --input in place")
    p.add_argument("--report", default=None, help="write a JSON report of the run here")
    p.add_argument("--dry-run", action="store_true", help="log the summary; write no network")
    p.add_argument("--survivor", choices=("strictest", "majority"), default="strictest",
                   help="surviving type per pair: strictest type present (default), or the "
                        "type with the most vote-weighted papers, strictness breaking ties")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args(argv)

    setup_logging(run_name="vote_pair_types", log_dir=args.log_dir)
    if args.dry_run:
        net = json.load(open(args.input, encoding="utf-8"))
        _, report = run_consolidation(net, args.survivor)
        if args.report:
            write_json(report, Path(args.report), indent=2)
            logger.info("Wrote %s", args.report)
        logger.info("Dry run: %s not written", args.out or args.input)
        return
    try:
        consolidate_pair_types(args.input, out_json=args.out, survivor=args.survivor,
                               report_json=args.report)
    except ConsolidationError as e:
        raise SystemExit(str(e))


if __name__ == "__main__":
    main()
