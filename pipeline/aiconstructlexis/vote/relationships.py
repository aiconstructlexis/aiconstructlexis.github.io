"""Majority vote on relationships across the extraction models, for the joint network.

Each model's relationship trials propose (source, target, type, evidence) claims per
paper. The vote decides, per paper, which pairs of entities are linked and with which
type:

  Pair-level link vote. Endpoint names are resolved to canonical entities by spelling
      (exact lowercase match, then hyphen/space-normalized match, against canonical
      names, original names and ``name_mapping``). A pair counts for a paper when at
      least ``threshold`` models link it, whatever types they give.
  Strictest type. The paper's type is the strictest type any linking model gave, in the
      order causes > measured_by > correlates > related.
  Direction. Within that type, the direction most models gave wins; a tie keeps both
      directions, each at half weight (``type_share`` 0.5). measured_by always points at
      the measurement instrument; related and correlates store their endpoints sorted.
  Evidence. One quote per (relationship, paper), taken from the trials of the linking
      models (the first non-empty quote given for the chosen label).

Inputs: the joint network JSON (entities with canonical and original names, optional
``name_mapping``) and ``trials``: {venue: trials directory}, each holding
``<model label>/relationship_trials.json`` (paper -> list of trials, each a list of
claims) and, for ``per_paper_resolution``, ``<model label>/entity_trials.json``.

Output: the network's ``relationships`` replaced by the voted ones, each with source,
target, type, papers ([{conference, paper, type_share}]), papers_by_conference,
paper_count, paper_count_by_conference, paper_weight (sum of type_share),
n_papers_split (papers where the linking models gave more than one type), evidence (up
to MAX_EVIDENCE distinct quotes) and evidence_by_paper ([{conference, paper, quote}]).
The network is rewritten in place unless ``out_json`` is given; ``report_json``
receives the run's counts (resolution steps, collisions, guard moves, evidence counts).

Options (all off by default; with none set the output is the plain vote above):

  per_paper_resolution
      A raw endpoint name is resolved in this order: (1) the paper's own memberships,
      i.e. the entities whose ``original_nodes[name].papers`` list this paper (lowercase
      match, then normalized); (2) the entity type the same model gave that name in its
      entity trial for the same paper, which narrows the candidates to that type;
      (3) spelling, as above. Candidates still tied go through one explicit rule, which
      is logged: an entity whose canonical name equals the raw name (exact case, then
      lowercase, then normalized) wins; then the one whose canonical name shares more
      words with the raw name; then one that is not expert-removed; then the one with
      more papers; then the alphabetically first canonical name.
  keep_all_quotes
      ``evidence_by_paper[*].quotes`` keeps every linking model's quote for that paper,
      with the model label and the type that model gave. The displayed quote is the
      first one that names both endpoints (quotes given for the chosen label first, then
      the others, in model order), else the quote the plain vote would show.
  type_guard
      After the vote, each paper's claim goes through ``guard_target``, the type guard
      shared with the curation stage: measured_by runs from a construct or behavior to
      an instrument (a claim from an instrument to a construct or behavior is reversed;
      any other pairing becomes related); causes never touches an instrument (a claim
      with an instrument at either end is dropped); correlates joins two instruments or
      two non-instruments (an instrument with a construct or behavior becomes related);
      related joins anything.
  evidence_check
      Records whether the displayed quote contains a surface name or alias of each
      endpoint (case and hyphen insensitive, plural s/es allowed) as
      ``evidence_by_paper[*].evidence_check = {"source": bool, "target": bool}``.

When any option is set, ``metadata.relationship_vote`` records the options and the
threshold.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
from collections import Counter, defaultdict
from pathlib import Path

from aiconstructlexis.util.logging import setup_logging
from aiconstructlexis.util.names import STRICTNESS

logger = logging.getLogger(__name__)

SYMMETRIC_TYPES = {"related", "correlates"}
ALLOWED_TYPES = set(STRICTNESS)
MAX_EVIDENCE = 10
ENTITY_TYPES = ("constructs", "measurements", "behaviors")


def _norm(s: str) -> str:
    s = (s or "").strip().lower()
    for ch in "-_/":
        s = s.replace(ch, " ")
    return " ".join(s.split())


def make_label(src: str, tgt: str, rtype: str, etype: dict) -> tuple:
    """Canonical (source, target, type): instrument last for measured_by, sorted for symmetric types."""
    if rtype == "measured_by" and etype[src] == "measurements" and etype[tgt] != "measurements":
        src, tgt = tgt, src
    if rtype in SYMMETRIC_TYPES:
        src, tgt = sorted([src, tgt])
    return (src, tgt, rtype)


def decide(by_model: dict, threshold: int) -> dict:
    """One (pair, paper): {model: {label: quote}} -> {label: share}; empty if the pair fails the vote."""
    if len(by_model) < threshold:
        return {}
    n_models = Counter(lab for labs in by_model.values() for lab in labs)
    rtype = min({lab[2] for lab in n_models}, key=STRICTNESS.index)
    candidates = {lab: n for lab, n in n_models.items() if lab[2] == rtype}
    top = max(candidates.values())
    chosen = sorted(lab for lab, n in candidates.items() if n == top)
    return {lab: 1 / len(chosen) for lab in chosen}


# ---------------------------------------------------------------- name resolution

def spelling_maps(net: dict):
    """(nm, nm_norm, etype): the default resolver's dictionaries (last entity written wins)."""
    nm, nm_norm, etype = {}, {}, {}
    for et in ENTITY_TYPES:
        for g in net.get(et, []) or []:
            c = (g.get("canonical_name") or "").strip()
            if not c:
                continue
            etype[c] = et
            nm[c.lower()] = c
            nm_norm[_norm(c)] = c
            for orig in g.get("original_names", []) or []:
                if orig:
                    nm[orig.lower()] = c
                    nm_norm[_norm(orig)] = c
    for orig, canon in (net.get("name_mapping") or {}).items():
        if orig and canon:
            nm.setdefault(orig.lower(), canon)
            nm_norm.setdefault(_norm(orig), canon)
    return nm, nm_norm, etype


def make_spelling_resolver(nm: dict, nm_norm: dict, etype: dict):
    def resolve(s):
        s = (s or "").strip()
        c = nm.get(s.lower()) or nm_norm.get(_norm(s))
        return c if c in etype else None
    return resolve


def load_entity_trial_types(path: Path) -> dict:
    """{paper: {"lower": {name: {types}}, "norm": {name: {types}}}} from one model's entity_trials.json."""
    out = {}
    if not path.is_file():
        return out
    for paper, ptrials in json.load(open(path, encoding="utf-8")).items():
        low, nrm = defaultdict(set), defaultdict(set)
        for trial in ptrials if isinstance(ptrials, list) else []:
            if not isinstance(trial, dict):
                continue
            nn = trial.get("Nomological Network") or trial
            if not isinstance(nn, dict):
                continue
            for et in ENTITY_TYPES:
                for ent in nn.get(et) or []:
                    if isinstance(ent, dict) and (ent.get("name") or "").strip():
                        name = ent["name"].strip()
                        low[name.lower()].add(et)
                        nrm[_norm(name)].add(et)
        out[paper] = {"lower": dict(low), "norm": dict(nrm)}
    return out


class PerPaperResolver:
    """Paper membership first, then the model's own entity typing, then spelling.

    trial_types: {(conf, model): {paper: {"lower": {...}, "norm": {...}}}}, or a callable
    (conf, model) -> that dict, so trials load lazily."""

    def __init__(self, net: dict, etype: dict, trial_types=None):
        self.etype = etype
        self.paper_count = {}
        self.removed = set()
        self.lower, self.normd = defaultdict(set), defaultdict(set)
        self.paper_lower, self.paper_norm = defaultdict(set), defaultdict(set)
        for et in ENTITY_TYPES:
            for g in net.get(et, []) or []:
                c = (g.get("canonical_name") or "").strip()
                if not c:
                    continue
                self.paper_count[c] = g.get("paper_count") or len(g.get("papers") or [])
                if g.get("expert_removed"):
                    self.removed.add(c)
                for n in [c] + [o for o in g.get("original_names", []) or [] if o]:
                    self.lower[n.lower()].add(c)
                    self.normd[_norm(n)].add(c)
                for n, node in (g.get("original_nodes") or {}).items():
                    for p in (node or {}).get("papers") or []:
                        if isinstance(p, (list, tuple)) and len(p) == 2:
                            key = (p[0], p[1])
                        elif isinstance(p, dict):
                            key = (p.get("conference"), p.get("paper"))
                        else:
                            continue
                        self.paper_lower[key + (n.lower(),)].add(c)
                        self.paper_norm[key + (_norm(n),)].add(c)
        # name_mapping fills keys no entity name covers, as setdefault does in the default resolver.
        ent_lower, ent_norm = set(self.lower), set(self.normd)
        for orig, canon in (net.get("name_mapping") or {}).items():
            if orig and canon in etype:
                if orig.lower() not in ent_lower:
                    self.lower[orig.lower()].add(canon)
                if _norm(orig) not in ent_norm:
                    self.normd[_norm(orig)].add(canon)
        self._trial_types = trial_types or {}
        self._trial_cache = {}
        self.method = Counter()
        self.collisions = Counter()   # (surface lower, chosen, candidates) -> mentions
        self.type_mismatch = Counter()  # (surface lower, model types, spelling candidates) -> mentions
        self._cache = {}

    def _types_for(self, conf, model, paper, s):
        key = (conf, model)
        if key not in self._trial_cache:
            tt = self._trial_types
            self._trial_cache[key] = tt(conf, model) if callable(tt) else tt.get(key, {})
        entry = self._trial_cache[key].get(paper)
        if not entry:
            return set()
        return set(entry["lower"].get(s.lower()) or entry["norm"].get(_norm(s)) or ())

    @staticmethod
    def collision_key(s: str, c: str, paper_count: dict, removed=frozenset()):
        """Explicit rule for candidates still tied: canonical == raw name (exact, lowercase,
        normalized), then more words shared between canonical and raw name (Jaccard), then
        an entity that is not expert-removed, then more papers, then alphabetical."""
        ts, tc = set(re.findall(r"[0-9a-z]+", s.lower())), set(re.findall(r"[0-9a-z]+", c.lower()))
        jac = len(ts & tc) / len(ts | tc) if ts | tc else 0.0
        return (c != s, c.lower() != s.lower(), _norm(c) != _norm(s), -round(jac, 6),
                c in removed, -paper_count.get(c, 0), c)

    def resolve(self, raw, conf, paper, model):
        s = (raw or "").strip()
        if not s:
            return None
        ck = (s, conf, paper, model)
        if ck in self._cache:
            return self._cache[ck]
        lo = {c for c in self.lower.get(s.lower(), ()) if c in self.etype}
        no = {c for c in self.normd.get(_norm(s), ()) if c in self.etype}
        spell = lo or no
        allc = lo | no
        chosen, how = None, None
        # 1. the paper's own memberships
        p1 = {c for c in self.paper_lower.get((conf, paper, s.lower()), ()) if c in self.etype}
        if not p1:
            p1 = {c for c in self.paper_norm.get((conf, paper, _norm(s)), ()) if c in self.etype}
        if len(p1) == 1:
            chosen, how = next(iter(p1)), "paper_membership"
        narrow = p1 if p1 else allc
        # 2. the type this model gave the name in its entity trial for this paper
        if chosen is None and narrow:
            types = self._types_for(conf, model, paper, s)
            if types:
                p2 = {c for c in narrow if self.etype[c] in types}
                if len(p2) == 1 and len(narrow) > 1:
                    chosen, how = next(iter(p2)), "entity_trial_type"
                elif p2:
                    narrow = p2
                elif len(allc) >= 1:
                    self.type_mismatch[(s.lower(), tuple(sorted(types)),
                                        tuple(sorted(narrow)))] += 1
        # 3. spelling, with the explicit collision rule
        if chosen is None and narrow:
            final = (narrow & spell) or narrow
            if len(final) == 1:
                chosen, how = next(iter(final)), "spelling"
            else:
                chosen = min(final, key=lambda c: self.collision_key(s, c, self.paper_count, self.removed))
                how = "collision_rule"
                self.collisions[(s.lower(), chosen, tuple(sorted(final)))] += 1
        self.method[how or "unresolved"] += 1
        self._cache[ck] = chosen
        return chosen


# ---------------------------------------------------------------- evidence check

_HYPHENS = "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"


def _ev_variants(s: str) -> set:
    """Lowercased forms with hyphens/underscores/slashes as spaces and as nothing,
    other punctuation as spaces."""
    s = (s or "").lower()
    for h in _HYPHENS:
        s = s.replace(h, "-")
    out = set()
    for rep in (" ", ""):
        t = re.sub(r"[-_/]", rep, s)
        t = " ".join(re.sub(r"[^0-9a-z]+", " ", t).split())
        if t:
            out.add(t)
    return out


_PAT_CACHE = {}


def _pattern(name_form: str):
    p = _PAT_CACHE.get(name_form)
    if p is None:
        p = re.compile(r"(?<![0-9a-z])" + re.escape(name_form) + r"(?:s|es)?(?![0-9a-z])")
        _PAT_CACHE[name_form] = p
    return p


def quote_names(quote: str, name_forms) -> bool:
    """True if any normalized name form occurs in the quote at word boundaries."""
    if not quote:
        return False
    qs = _ev_variants(quote)
    return any(_pattern(f).search(q) for f in name_forms for q in qs)


def surface_forms(net: dict) -> dict:
    """canonical -> set of normalized forms of its canonical name, original names, node names
    and name_mapping aliases."""
    names = defaultdict(set)
    for et in ENTITY_TYPES:
        for g in net.get(et, []) or []:
            c = (g.get("canonical_name") or "").strip()
            if not c:
                continue
            names[c].add(c)
            names[c].update(o for o in g.get("original_names", []) or [] if o)
            names[c].update(n for n in (g.get("original_nodes") or {}) if n)
    for orig, canon in (net.get("name_mapping") or {}).items():
        if orig and canon in names:
            names[canon].add(orig)
    return {c: set().union(*(_ev_variants(n) for n in ns)) for c, ns in names.items()}


# ---------------------------------------------------------------- type guard

INSTRUMENT = "measurements"
CONSTRUCT_OR_BEHAVIOR = ("constructs", "behaviors")


def guard_target(ty, s, t, ts, tt):
    """Which entity types each relationship type may join.

    ``ts`` and ``tt`` are the entity types of source ``s`` and target ``t``. Returns None
    when the pairing is allowed, "drop" when the claims are discarded, or the
    (source, type, target) the claims move to:
      measured_by  construct or behavior -> instrument; instrument -> construct or
                   behavior is reversed; any other pairing (two instruments, or two
                   non-instruments) becomes related.
      causes       no instrument at either end; a claim with an instrument at either end
                   is dropped (such claims describe training-data or method use, which is
                   out of scope).
      correlates   two instruments (score correlations) or two non-instruments; an
                   instrument with a construct or behavior becomes related.
      related      any pairing.
    The curation stage applies the same function to the curated network.
    """
    if ty == "measured_by":
        if ts in CONSTRUCT_OR_BEHAVIOR and tt == INSTRUMENT:
            return None
        if tt in CONSTRUCT_OR_BEHAVIOR and ts == INSTRUMENT:
            return (t, ty, s)
        return (min(s, t), "related", max(s, t))
    if ty == "causes":
        return "drop" if INSTRUMENT in (ts, tt) else None
    if ty == "correlates":
        return (min(s, t), "related", max(s, t)) if (ts == INSTRUMENT) != (tt == INSTRUMENT) else None
    return None


def guard_shares(shares: dict, etype: dict, log: Counter = None) -> dict:
    """Map one (pair, paper)'s {label: share} through the type guard.
    Returns {new label: (share, [original labels])}; dropped labels are left out and
    labels that land on the same new label add their shares."""
    out = {}
    for lab, share in shares.items():
        s, t, ty = lab
        to = guard_target(ty, s, t, etype[s], etype[t])
        if to is None:
            new = lab
        elif to == "drop":
            if log is not None:
                log[f"claims_dropped:{ty}"] += 1
            continue
        else:
            new = (to[0], to[2], to[1])  # guard_target returns (source, type, target)
            if log is not None:
                log[f"claims_moved:{ty}->{to[1]}" + (" (reversed)" if to[1] == ty else "")] += 1
        sh, src = out.get(new, (0.0, []))
        out[new] = (sh + share, src + [lab])
    return out


# ---------------------------------------------------------------- vote

def vote_relationships(
    joint_json: str | Path,
    trials: dict,
    models: list,
    threshold: int = 2,
    out_json: str | Path | None = None,
    per_paper_resolution: bool = False,
    keep_all_quotes: bool = False,
    type_guard: bool = False,
    evidence_check: bool = False,
    report_json: str | Path | None = None,
) -> Path:
    """Run the relationship vote on the joint network and write the result.

    ``trials`` maps each venue label to its trials directory
    (``<dir>/<model label>/relationship_trials.json``); ``models`` are the trial labels.
    The network is rewritten in place unless ``out_json`` is given. Returns the written
    path. See the module docstring for the rule and the options.
    """
    joint_path = Path(joint_json)
    net = json.load(open(joint_path, encoding="utf-8"))
    out_path = Path(out_json) if out_json else joint_path
    options = {"per_paper_resolution": bool(per_paper_resolution),
               "keep_all_quotes": bool(keep_all_quotes),
               "type_guard": bool(type_guard),
               "evidence_check": bool(evidence_check)}
    any_option = any(options.values())

    nm, nm_norm, etype = spelling_maps(net)
    resolve = make_spelling_resolver(nm, nm_norm, etype)

    conf_dirs = {conf: Path(d) for conf, d in trials.items()}
    ppr = None
    route_default, route_new = defaultdict(Counter), defaultdict(Counter)
    if per_paper_resolution:
        ppr = PerPaperResolver(
            net, etype,
            trial_types=lambda conf, model: load_entity_trial_types(
                conf_dirs[conf] / model / "entity_trials.json"))

    # (pair, conf, paper) -> model -> {label: quote}
    votes = defaultdict(lambda: defaultdict(dict))
    for conf, tdir in conf_dirs.items():
        for model in models:
            path = tdir / model / "relationship_trials.json"
            if not path.is_file():
                logger.warning("missing %s", path)
                continue
            for paper, trials in json.load(open(path, encoding="utf-8")).items():
                for trial in trials:
                    if not isinstance(trial, list):
                        continue
                    for r in trial:
                        if not isinstance(r, dict):
                            continue
                        rtype = (r.get("type") or "").strip().lower()
                        if ppr is None:
                            src, tgt = resolve(r.get("source")), resolve(r.get("target"))
                        else:
                            src = ppr.resolve(r.get("source"), conf, paper, model)
                            tgt = ppr.resolve(r.get("target"), conf, paper, model)
                            for raw, new in ((r.get("source"), src), (r.get("target"), tgt)):
                                old = resolve(raw)
                                if old != new:
                                    route_default[_norm(raw)][old] += 1
                                    route_new[_norm(raw)][new] += 1
                        if not (src and tgt) or rtype not in ALLOWED_TYPES or src == tgt:
                            continue
                        lab = make_label(src, tgt, rtype, etype)
                        pair = tuple(sorted([src, tgt]))
                        votes[(pair, conf, paper)][model].setdefault(lab, (r.get("evidence") or "").strip())

    forms = surface_forms(net) if (keep_all_quotes or evidence_check) else None
    guard_log = Counter()
    ev_stats = Counter()

    edges = {}  # label -> aggregate
    stats = Counter()
    split_sets = Counter()
    for (pair, conf, paper), by_model in votes.items():
        shares = decide(by_model, threshold)
        if not shares:
            stats["pair from too few models"] += 1
            continue
        given = {lab[2] for labs in by_model.values() for lab in labs}
        split = len(given) > 1
        if split:
            split_sets[" + ".join(sorted(given, key=STRICTNESS.index))] += 1
        stats["pair kept, models gave >1 type" if split else "pair kept, one type"] += 1
        if len(shares) > 1:
            stats["direction tie, both kept at 0.5"] += 1
        if not type_guard:
            final = {lab: (share, [lab]) for lab, share in shares.items()}
        else:
            final = guard_shares(shares, etype, guard_log)
        for lab, (share, src_labs) in final.items():
            e = edges.setdefault(lab, {"source": lab[0], "target": lab[1], "type": lab[2],
                                       "papers": [], "papers_by_conference": {},
                                       "paper_weight": 0.0, "n_papers_split": 0,
                                       "evidence": [], "evidence_by_paper": []})
            e["papers"].append({"conference": conf, "paper": paper, "type_share": round(share, 4)})
            e["papers_by_conference"].setdefault(conf, []).append(paper)
            e["paper_weight"] += share
            if split:
                e["n_papers_split"] += 1
            quote = next((labs[sl] for sl in src_labs for labs in by_model.values() if labs.get(sl)), "")
            entry_extra = {}
            if forms is not None:
                fs, ft = forms.get(lab[0], set()), forms.get(lab[1], set())
                first = quote
                shown = quote
                if keep_all_quotes:
                    same = [(m, labs[sl], sl[2]) for sl in src_labs for m, labs in by_model.items() if labs.get(sl)]
                    other = [(m, q, ol[2]) for m, labs in by_model.items() for ol, q in labs.items()
                             if ol not in src_labs and q]
                    cands = same + other
                    for m, q, _ in cands:
                        if quote_names(q, fs) and quote_names(q, ft):
                            shown = q
                            break
                    entry_extra["quotes"] = [{"model": m, "type": ty, "quote": q} for m, q, ty in cands]
                    if shown != first:
                        ev_stats["quote changed by keep-all-quotes"] += 1
                if evidence_check:
                    ok_s, ok_t = quote_names(shown, fs), quote_names(shown, ft)
                    entry_extra["evidence_check"] = {"source": ok_s, "target": ok_t}
                    ev_stats["claims checked"] += 1
                    ev_stats["both endpoints named" if ok_s and ok_t else
                             "source only" if ok_s else "target only" if ok_t else "neither named"] += 1
                    if keep_all_quotes:
                        f_s, f_t = quote_names(first, fs), quote_names(first, ft)
                        ev_stats["both endpoints named (default first quote)"] += int(f_s and f_t)
                quote = shown
            if quote:
                ev_entry = {"conference": conf, "paper": paper, "quote": quote}
                ev_entry.update(entry_extra)
                e["evidence_by_paper"].append(ev_entry)
                if quote not in e["evidence"] and len(e["evidence"]) < MAX_EVIDENCE:
                    e["evidence"].append(quote)

    rels = []
    for e in edges.values():
        e["paper_count"] = len(e["papers"])
        e["paper_weight"] = round(e["paper_weight"], 4)
        e["paper_count_by_conference"] = {c: len(ps) for c, ps in e["papers_by_conference"].items()}
        rels.append(e)
    rels.sort(key=lambda r: -r["paper_count"])

    pairs = defaultdict(set)
    for r in rels:
        pairs[tuple(sorted([r["source"], r["target"]]))].add(r["type"])
    logger.info("per (pair, paper): %s", dict(stats))
    logger.info("type sets when models split (strictest first): %s", dict(split_sets.most_common()))
    logger.info("relationships: %d -> %d", len(net.get("relationships") or []), len(rels))
    logger.info("types (relationships): %s", dict(Counter(r["type"] for r in rels)))
    w = Counter()
    for r in rels:
        w[r["type"]] += r["paper_weight"]
    logger.info("types (vote-weighted papers): %s", {k: round(v) for k, v in w.items()})
    logger.info("linked pairs: %d, with >1 type: %d",
                len(pairs), sum(1 for t in pairs.values() if len(t) > 1))
    logger.info("with an evidence quote: %d of %d", sum(1 for r in rels if r["evidence"]), len(rels))

    report = {"flags": options, "threshold": threshold, "per_pair_paper": dict(stats)}
    if any_option:
        if ppr is not None:
            report["resolution_steps"] = dict(ppr.method)
            report["collisions"] = [{"surface": s, "chosen": c, "candidates": list(cs), "mentions": n}
                                    for (s, c, cs), n in ppr.collisions.most_common()]
            report["type_mismatch"] = [{"surface": s, "model_types": list(t), "candidates": list(cs), "mentions": n}
                                       for (s, t, cs), n in ppr.type_mismatch.most_common()]
            report["mentions_rerouted"] = {
                s: {"default": {str(k): v for k, v in route_default[s].items()},
                    "per_paper": {str(k): v for k, v in route_new[s].items()}}
                for s in sorted(route_default, key=lambda s: -sum(route_default[s].values()))}
            logger.info("resolution steps (mentions): %s", dict(ppr.method))
            logger.info("mentions resolved differently from spelling: %d over %d surface names",
                        sum(sum(c.values()) for c in route_default.values()), len(route_default))
        if type_guard:
            report["type_guard"] = dict(guard_log)
            logger.info("type guard (paper claims): %s", dict(guard_log))
        if ev_stats:
            report["evidence"] = dict(ev_stats)
            logger.info("evidence: %s", dict(ev_stats))
        net.setdefault("metadata", {})["relationship_vote"] = {"flags": options, "threshold": threshold}

    net["relationships"] = rels
    out_path.parent.mkdir(parents=True, exist_ok=True)
    json.dump(net, open(out_path, "w"), indent=2, ensure_ascii=False)
    logger.info("Wrote %s", out_path)
    if report_json:
        report_path = Path(report_json)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        json.dump(report, open(report_path, "w"), indent=2, ensure_ascii=False)
        logger.info("Wrote %s", report_path)
    return out_path


def parse_venue_specs(specs: list) -> dict:
    """``venue:dir`` command-line items -> {venue: dir}."""
    out = {}
    for spec in specs:
        if ":" not in spec:
            raise ValueError(f"expected venue:dir, got {spec!r}")
        venue, d = spec.split(":", 1)
        out[venue] = d
    return out


def main(argv=None) -> None:
    p = argparse.ArgumentParser(
        description="Majority vote on relationships: pair-level link vote, strictest type wins.")
    p.add_argument("--joint", required=True, help="joint network JSON")
    p.add_argument("--trials", nargs="+", required=True, metavar="VENUE:DIR",
                   help="per-venue trials directories, as venue:dir")
    p.add_argument("--models", nargs="+", required=True,
                   help="model labels matching <dir>/<label>/ directories")
    p.add_argument("--threshold", type=int, default=2,
                   help="minimum number of models that must link a pair (default: 2)")
    p.add_argument("--out", default=None, help="write here instead of rewriting --joint in place")
    p.add_argument("--per-paper-resolution", action="store_true",
                   help="resolve endpoint names through the paper's memberships, then the "
                        "model's entity typing, then spelling with an explicit collision rule")
    p.add_argument("--keep-all-quotes", action="store_true",
                   help="keep every linking model's quote; show the first naming both endpoints")
    p.add_argument("--type-guard", action="store_true",
                   help="apply the relationship type guard to every paper claim")
    p.add_argument("--evidence-check", action="store_true",
                   help="record whether the shown quote names each endpoint")
    p.add_argument("--report", default=None, help="write a JSON report of the run here")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args(argv)

    setup_logging(run_name="vote_relationships", log_dir=args.log_dir)
    try:
        trials = parse_venue_specs(args.trials)
    except ValueError as e:
        p.error(str(e))
    vote_relationships(
        args.joint, trials, args.models, threshold=args.threshold, out_json=args.out,
        per_paper_resolution=args.per_paper_resolution, keep_all_quotes=args.keep_all_quotes,
        type_guard=args.type_guard, evidence_check=args.evidence_check, report_json=args.report,
    )


if __name__ == "__main__":
    main()
