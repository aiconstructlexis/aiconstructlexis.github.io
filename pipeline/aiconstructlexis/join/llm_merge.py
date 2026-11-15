"""Semantic cross-venue merge of the joint network with an LLM.

The union stage joins venues at canonical name, so one concept under different names in
different venues ("Factuality" and "Factuality and faithfulness") is still two entities.
This stage runs the merge-groups prompt (``MERGE_GROUPS_PROMPT`` of the prompt set) over
each entity type: entities are packed into batches by token signature so that related
names sit in the same batch (``aiconstructlexis.harmonize.batching.make_batches``), each
batch is sent as a numbered list of {id, canonical_name, original_names,
canonical_definition}, and the model returns ``{"groups": {canonical name: [ids]},
"ungrouped": [ids]}``. Ids the response leaves out keep their own name. Groups given the
same canonical name are merged: the one with the most papers is the seed and takes the
chosen name; original_names, papers_by_conference, original_nodes,
source_snippets_evidence and characterizations are unioned; papers, paper_count and
paper_count_by_conference are recomputed. A batch whose call fails three times is left as
it is.

Cross-batch pass (``cross_batch_pass``), after the per-batch merges:
  "auto" (default)  one global pass over all merged groups, which only runs when they fit
                    in a single batch (at most ``batch_size`` groups); otherwise nothing.
  "blocked"         candidate pairs of groups that were in different first-pass batches
                    are found by three deterministic blocking rules (same normalized key,
                    IDF-weighted token Jaccard >= ``min_overlap``, one name the acronym of
                    the other), grouped into connected components, packed into batches of
                    at most ``batch_size`` groups and sent to the merge prompt.
  "report"          the candidate pairs are found and counted in the log, with no extra
                    LLM call.
  "off"             nothing.

LLM calls go through ``aiconstructlexis.harmonize.aggregator.call_llm_for_aggregation``;
``reasoning_effort`` and ``max_output_tokens`` are passed on for the models that take
them. Relationships and every other section of the network are left as they are.
"""
from __future__ import annotations

import argparse
import json
import logging
import math
import re
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from aiconstructlexis.prompts import load_prompts
from aiconstructlexis.util.logging import setup_logging

logger = logging.getLogger(__name__)

ENTITY_TYPES = ("constructs", "measurements", "behaviors")
CROSS_BATCH_MODES = ("auto", "blocked", "report", "off")


def call_llm_for_aggregation(prompt: str, provider: str, model: str, **kwargs) -> Any:
    """The harmonization stage's LLM call, imported when first needed."""
    from aiconstructlexis.harmonize.aggregator import call_llm_for_aggregation as call
    return call(prompt, provider, model, **kwargs)


def make_batches(names: List[str], batch_size: int) -> List[List[int]]:
    """The harmonization stage's batch packing by token signature, imported when first needed."""
    from aiconstructlexis.harmonize.batching import make_batches as batches
    return batches(names, batch_size=batch_size)


def llm_options(reasoning_effort: Optional[str] = None,
                max_output_tokens: Optional[int] = None) -> Dict[str, Any]:
    """Keyword arguments for the LLM call, from the stage's options."""
    kw: Dict[str, Any] = {}
    if reasoning_effort:
        kw["reasoning_effort"] = reasoning_effort
    if max_output_tokens:
        kw["max_output_tokens"] = max_output_tokens
    return kw


def _llm(prompt: str, provider: str, model: str, llm_kwargs: Optional[Dict[str, Any]] = None) -> Any:
    return call_llm_for_aggregation(prompt, provider, model, **(llm_kwargs or {}))


def _slim(g: Dict[str, Any]) -> Dict[str, Any]:
    out = {"canonical_name": g.get("canonical_name", "")}
    onames = g.get("original_names") or []
    if onames:
        out["original_names"] = onames
    cd = (g.get("canonical_definition") or "").strip()
    if cd:
        out["canonical_definition"] = cd
    return out


def _decode_id_groups(result: Any, groups: List[Dict[str, Any]]) -> Dict[int, str]:
    """id -> canonical name from a merge-groups response ({} when it is not a dict of groups)."""
    if not isinstance(result, dict):
        return {}
    grp_dict = result.get("groups")
    if not isinstance(grp_dict, dict):
        return {}
    out: Dict[int, str] = {}
    seen: set = set()
    for canon, ids in grp_dict.items():
        if not isinstance(ids, list):
            continue
        for raw in ids:
            try:
                idx = int(raw)
            except (ValueError, TypeError):
                continue
            if 0 <= idx < len(groups) and idx not in seen:
                out[idx] = canon
                seen.add(idx)
    # ungrouped: keep the original canonical_name
    for raw in (result.get("ungrouped") or []):
        try:
            idx = int(raw)
        except (ValueError, TypeError):
            continue
        if 0 <= idx < len(groups) and idx not in seen:
            out[idx] = groups[idx].get("canonical_name", "")
            seen.add(idx)
    # ids the response leaves out keep their own name (a singleton group)
    for i in range(len(groups)):
        if i not in seen:
            out[i] = groups[i].get("canonical_name", "")
    return out


def _merge_groups_joint(winner: Dict[str, Any], loser: Dict[str, Any]) -> None:
    """Merge joint-network metadata from `loser` into `winner` in place."""
    # original_names
    wn = set(winner.get("original_names") or [])
    for n in loser.get("original_names") or []:
        if n not in wn:
            winner.setdefault("original_names", []).append(n)
            wn.add(n)
    # papers_by_conference
    wpbc = winner.setdefault("papers_by_conference", {})
    for conf, ps in (loser.get("papers_by_conference") or {}).items():
        ex = set(wpbc.setdefault(conf, []))
        for p in ps:
            if p not in ex:
                wpbc[conf].append(p)
                ex.add(p)
    # original_nodes
    wnodes = winner.setdefault("original_nodes", {})
    for k, v in (loser.get("original_nodes") or {}).items():
        if k not in wnodes:
            wnodes[k] = v
    # source_snippets_evidence
    wsse = winner.setdefault("source_snippets_evidence", [])
    wset = {json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s) for s in wsse}
    for s in loser.get("source_snippets_evidence") or []:
        sig = json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s)
        if sig not in wset:
            wsse.append(s)
            wset.add(sig)
    # characterizations
    wchars = winner.setdefault("characterizations", {})
    for conf, ch in (loser.get("characterizations") or {}).items():
        if conf not in wchars:
            wchars[conf] = ch
    if not winner.get("characterization") and loser.get("characterization"):
        winner["characterization"] = loser["characterization"]


def _apply_id_to_canon(groups: List[Dict[str, Any]],
                       id_to_canon: Dict[int, str]) -> List[Dict[str, Any]]:
    """Group input groups by their assigned canonical name and merge metadata."""
    by_canon: Dict[str, List[int]] = {}
    for i, c in id_to_canon.items():
        by_canon.setdefault(c, []).append(i)
    out: List[Dict[str, Any]] = []
    for canon, idxs in by_canon.items():
        # Pick the seed: the input group with highest paper_count
        winner_idx = max(idxs, key=lambda i: groups[i].get("paper_count", 0))
        winner = dict(groups[winner_idx])
        winner["canonical_name"] = canon  # use the LLM-chosen canonical name
        for j in idxs:
            if j == winner_idx:
                continue
            _merge_groups_joint(winner, groups[j])
        # Recompute aggregate paper info
        pbc = winner.get("papers_by_conference", {})
        winner["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
        all_papers = [{"conference": c, "paper": p} for c, ps in pbc.items() for p in ps]
        winner["papers"] = all_papers
        winner["paper_count"] = len(all_papers)
        out.append(winner)
    return out


def _origins(id_to_canon: Dict[int, str], batch_of: Dict[int, int]) -> List[set]:
    """First-pass batches behind each group _apply_id_to_canon returns, in its order."""
    by_canon: Dict[str, List[int]] = {}
    for i, c in id_to_canon.items():
        by_canon.setdefault(c, []).append(i)
    return [{batch_of[i] for i in idxs} for idxs in by_canon.values()]


# ---------------------------------------------------------------- cross-batch blocking
#
# Blocking keys for candidate duplicate pairs. A concept key (constructs, behaviors) is the
# lowercased name with alias parentheticals dropped, the ability family spelled "ability",
# filler suffixes removed, synonym nouns and morphological variants folded, the last word
# singularized, stopwords dropped and two-word names sorted. An instrument key
# (measurements) keeps only letters, digits, "+" and "#", drops generic suffixes and a
# leading "the", and folds version spellings ("v2.0" -> "2").

_STOP = {"a", "an", "the", "of", "to", "for", "in", "on", "with", "by", "and", "or", "as"}
_GENERIC_INSTRUMENT_WORDS = {"benchmark", "benchmarks", "dataset", "datasets", "evaluation", "test",
                             "set", "suite", "task", "tasks", "corpus"}
_UNICODE_HYPHENS = "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"
_FILLER_SUFFIXES = (" performance", " benchmark", " benchmarks", " dataset", " datasets",
                    " evaluation", " evaluations", " judge", " judgment", " framework",
                    " task", " tasks")
_ABILITY_WORDS = [
    (r"capabilities|capacities|skills|proficiencies", "abilities"),
    (r"capability|capacity|skill|proficiency", "ability"),
]
_SYNONYM_NOUNS = [("comprehension", "understanding"), ("awareness", "understanding")]
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
_INSTRUMENT_SUFFIXES = (" benchmarks", " benchmark", " datasets", " dataset",
                        " tasks", " task", " performance")
_GENERIC_PARENS = {"benchmark", "dataset", "data set", "corpus", "task", "suite"}


def _initials(text: str) -> str:
    """Initials of a phrase: words split on spaces, hyphens and camel case; digits whole."""
    toks = re.findall(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|\d+", text)
    return "".join(t if t.isdigit() else t[0] for t in toks).lower()


def _initials_nostop(text: str) -> str:
    toks = re.findall(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|\d+", text)
    return "".join(t if t.isdigit() else t[0] for t in toks if t.lower() not in _STOP).lower()


def _is_alias_paren(base: str, paren: str) -> bool:
    """True when the parenthetical is an acronym of the base ("BIG-Bench Hard (BBH)"),
    the base is an acronym of it ("NLU (Natural language understanding)"), or it is a
    generic word ("(benchmark)"). Anything else is a disambiguating qualifier."""
    p = paren.strip()
    if not p:
        return True
    if p.lower() in _GENERIC_PARENS:
        return True
    pa = re.sub(r"[^0-9a-z]", "", p.lower())
    ba = re.sub(r"[^0-9a-z]", "", base.lower())
    if len(pa) >= 2 and pa in (_initials(base), _initials_nostop(base)) and len(_initials(base)) >= 2:
        return True
    if len(ba) >= 2 and ba in (_initials(p), _initials_nostop(p)) and len(_initials(p)) >= 2:
        return True
    return False


def _handle_parens(name: str) -> str:
    """Drop alias parentheticals, keep the content of disambiguating ones (as words)."""
    out = name
    for m in reversed(list(re.finditer(r"\(([^)]*)\)", name))):
        base = (name[:m.start()] + name[m.end():]).strip()
        keep = "" if _is_alias_paren(base, m.group(1)) else f" {m.group(1)} "
        out = out[:m.start()] + keep + out[m.end():]
    return " ".join(out.split())


def _clean_hyphens(name: str) -> str:
    s = (name or "").strip()
    for uh in _UNICODE_HYPHENS:
        s = s.replace(uh, "-")
    return s


def _concept_key(name: str) -> str:
    """Blocking key for a construct or behavior name."""
    if not name:
        return ""
    s = _handle_parens(_clean_hyphens(name)).lower()
    for pat, rep in _ABILITY_WORDS:
        s = re.sub(rf"\b(?:{pat})\b", rep, s)
    for ch in "-_/":
        s = s.replace(ch, " ")
    s = "".join(c if (c.isalnum() or c.isspace() or c in "+#") else " " for c in s)
    s = " ".join(s.split())
    changed = True
    while changed:
        changed = False
        for suf in _FILLER_SUFFIXES:
            if s.endswith(suf) and len(s) > len(suf):
                s = s[: -len(suf)].rstrip()
                changed = True
                break
    for src, dst in _SYNONYM_NOUNS:
        s = re.sub(rf"\b{re.escape(src)}\b", dst, s)
    for src, dst in sorted(_MORPHOLOGY, key=lambda x: -len(x[0])):
        s = re.sub(rf"\b{re.escape(src)}\b", dst, s)
    parts = s.split()
    if parts:
        last = parts[-1]
        if last.endswith("ies") and len(last) > 3:
            parts[-1] = last[:-3] + "y"
        elif last.endswith("ses") and len(last) > 3:
            parts[-1] = last[:-2]
        elif last.endswith("s") and not last.endswith("ss") and len(last) > 1:
            parts[-1] = last[:-1]
    parts = [p for p in parts if p not in _STOP]
    if len(parts) == 2:
        parts = sorted(parts)
    return " ".join(parts)


def _instrument_key(name: str) -> str:
    """Blocking key for a measurement instrument name."""
    if not name:
        return ""
    s = _handle_parens(_clean_hyphens(name)).lower()
    s = re.sub(r"^the\s+", "", s)
    changed = True
    while changed:
        changed = False
        for suf in _INSTRUMENT_SUFFIXES:
            if s.endswith(suf) and len(s) > len(suf):
                s = s[: -len(suf)].rstrip()
                changed = True
                break
    s = re.sub(r"(?<![a-z0-9])v(?=\d)", "", s)          # "SQuAD v2.0" -> "SQuAD 2.0"
    s = re.sub(r"(?<=\d)\.0(?![0-9])", "", s)           # "2.0" -> "2"
    s = re.sub(r"(?<=\d)\.(?=\d)", "\u0000", s)          # keep dots between digits
    s = "".join(c for c in s if c.isalnum() or c in "+#\u0000")
    return s.replace("\u0000", ".")


def _blocking_key(name: str, node_type: str) -> str:
    return _instrument_key(name) if node_type == "measurements" else _concept_key(name)


def _tokens(name: str, node_type: str) -> set:
    if node_type == "measurements":
        toks = set(re.findall(r"[a-z0-9]+", (name or "").lower()))
        return {t for t in toks if t not in _STOP and t not in _GENERIC_INSTRUMENT_WORDS}
    return set(_concept_key(name).split())


def candidate_pairs(names: List[str], node_type: str, batches: Optional[List[set]] = None,
                    min_overlap: float = 0.5, max_per_group: int = 30) -> List[Dict[str, Any]]:
    """Deterministic candidate duplicate pairs (i < j). With `batches` (the first-pass
    batches behind each group), only pairs that never shared a batch are returned.
    Rules: same blocking key; IDF-weighted token Jaccard >= min_overlap; acronym."""
    n = len(names)
    toks = [_tokens(x, node_type) for x in names]
    df = Counter(t for ts in toks for t in ts)
    idf = {t: math.log((n + 1) / (c + 0.5)) for t, c in df.items()}
    keys = [_blocking_key(x, node_type) for x in names]
    compact = [re.sub(r"[^a-z0-9]", "", (x or "").lower()) for x in names]
    inits = [_initials(x) for x in names]

    def cross(i, j):
        return batches is None or not (batches[i] & batches[j])

    found: Dict[Tuple[int, int], Dict[str, Any]] = {}

    def add(i, j, reason, score):
        if i == j or not cross(i, j):
            return
        a, b = min(i, j), max(i, j)
        e = found.setdefault((a, b), {"a": a, "b": b, "reasons": [], "score": 0.0})
        if reason not in e["reasons"]:
            e["reasons"].append(reason)
        e["score"] = max(e["score"], score)

    by_key = defaultdict(list)
    for i, k in enumerate(keys):
        if k:
            by_key[k].append(i)
    for idxs in by_key.values():
        for x in range(len(idxs)):
            for y in range(x + 1, len(idxs)):
                add(idxs[x], idxs[y], "same_normalized_key", 1.0)
    by_compact = defaultdict(list)
    for i, c in enumerate(compact):
        if len(c) >= 2:
            by_compact[c].append(i)
    expansions = defaultdict(list)  # short name -> longer names it abbreviates
    for j, ini in enumerate(inits):
        if len(ini) >= 3:  # two-letter acronyms are too ambiguous ("CB")
            for i in by_compact.get(ini, []):
                if i != j and compact[j] != ini:
                    expansions[i].append(j)
    for i, js in expansions.items():
        if len(js) <= 3:  # an acronym that fits many names is ambiguous
            for j in js:
                add(i, j, "acronym", 0.9)
    index = defaultdict(list)
    for i, ts in enumerate(toks):
        for t in ts:
            index[t].append(i)
    per_group = Counter()
    scored = []
    for i, ts in enumerate(toks):
        if not ts:
            continue
        cands = set()
        for t in ts:
            if df[t] <= 200:  # very common tokens alone do not make a candidate
                cands.update(j for j in index[t] if j > i)
        for j in cands:
            inter = ts & toks[j]
            union = ts | toks[j]
            w = sum(idf[t] for t in inter) / sum(idf[t] for t in union)
            if w >= min_overlap:
                scored.append((w, i, j))
    for w, i, j in sorted(scored, key=lambda x: (-x[0], x[1], x[2])):
        if per_group[i] >= max_per_group or per_group[j] >= max_per_group:
            continue
        if cross(i, j):
            per_group[i] += 1
            per_group[j] += 1
        add(i, j, "token_overlap", round(w, 4))
    return sorted(found.values(), key=lambda e: (-e["score"], e["a"], e["b"]))


def _components(n_items: int, pairs: List[Dict[str, Any]]) -> List[List[int]]:
    parent = list(range(n_items))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for e in pairs:
        ra, rb = find(e["a"]), find(e["b"])
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)
    linked = {e["a"] for e in pairs} | {e["b"] for e in pairs}
    comps = defaultdict(list)
    for i in sorted(linked):
        comps[find(i)].append(i)
    return [v for _, v in sorted(comps.items())]


def _pack(components: List[List[int]], names: List[str], batch_size: int) -> List[List[int]]:
    """Pack components into batches of at most batch_size; split larger ones by name order."""
    pieces = []
    for comp in components:
        if len(comp) <= batch_size:
            pieces.append(comp)
        else:
            comp = sorted(comp, key=lambda i: names[i].lower())
            pieces.extend(comp[k:k + batch_size] for k in range(0, len(comp), batch_size))
    batches, cur = [], []
    for piece in sorted(pieces, key=len, reverse=True):
        placed = False
        for b in batches:
            if len(b) + len(piece) <= batch_size:
                b.extend(piece)
                placed = True
                break
        if not placed:
            batches.append(list(piece))
    return batches


def _parse(result: Any) -> Any:
    if isinstance(result, str):
        text = result.strip()
        fence = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
        if fence:
            text = fence.group(1).strip()
        try:
            result = json.loads(text)
        except json.JSONDecodeError:
            try:
                from json_repair import repair_json
                result = repair_json(text, return_objects=True)
            except Exception:
                result = {}
    return result


def blocked_cross_batch_pass(merged: List[Dict[str, Any]], node_type: str, provider: str, model: str,
                             batch_size: int, origins: List[set],
                             call_llm: bool = True, min_overlap: float = 0.5,
                             llm_kwargs: Optional[Dict[str, Any]] = None,
                             prompts=None) -> List[Dict[str, Any]]:
    """Merge candidate duplicates that the first pass never saw in one batch (see module docstring)."""
    P = prompts or load_prompts()
    names = [g.get("canonical_name", "") for g in merged]
    pairs = candidate_pairs(names, node_type, origins, min_overlap=min_overlap)
    reasons = Counter(r for e in pairs for r in e["reasons"])
    logger.info("  Cross-batch candidates: %d pairs (%s)", len(pairs), dict(reasons))
    if not call_llm or not pairs:
        return merged
    comps = _components(len(merged), pairs)
    llm_batches = _pack(comps, names, batch_size)
    logger.info("  Blocked cross-batch pass: %d groups in %d components, %d LLM batches",
                sum(len(c) for c in comps), len(comps), len(llm_batches))
    id_to_canon = {i: g.get("canonical_name", "") for i, g in enumerate(merged)}
    for bnum, idxs in enumerate(llm_batches, 1):
        batch_groups = [merged[i] for i in idxs]
        slim_groups = [{"id": j, **_slim(g)} for j, g in enumerate(batch_groups)]
        prompt = P.MERGE_GROUPS_PROMPT.format(node_type=node_type,
                                              groups_json=json.dumps(slim_groups, indent=2))
        result = None
        for attempt in range(3):
            try:
                result = _llm(prompt, provider, model, llm_kwargs)
                break
            except Exception as e:
                logger.warning("    cross-batch %d/%d attempt %d: %s", bnum, len(llm_batches), attempt + 1, e)
                if attempt < 2:
                    time.sleep(5 * (attempt + 1))
        if result is None:
            logger.warning("  cross-batch batch %d failed; its %d groups are left as they are", bnum, len(idxs))
            continue
        local = _decode_id_groups(_parse(result), batch_groups)
        for j, i in enumerate(idxs):
            id_to_canon[i] = local.get(j, batch_groups[j].get("canonical_name", ""))
    out = _apply_id_to_canon(merged, id_to_canon)
    logger.info("  After blocked cross-batch merge: %d groups", len(out))
    return out


def merge_one_type(groups: List[Dict[str, Any]], node_type: str,
                   provider: str, model: str, batch_size: int,
                   cross_batch: str = "auto",
                   min_overlap: float = 0.5, llm_kwargs: Optional[Dict[str, Any]] = None,
                   prompts=None) -> List[Dict[str, Any]]:
    """Run the LLM merge pass on one entity type, packing related names into the same batch.

    ``llm_kwargs`` are passed on to the LLM call (see ``llm_options``); ``prompts`` is a
    loaded prompt set (the default set when None).
    """
    P = prompts or load_prompts()
    logger.info("=== Merging %s (start: %d) ===", node_type, len(groups))
    if len(groups) <= 1:
        return groups
    names = [g.get("canonical_name", "") for g in groups]
    batch_idx_lists = make_batches(names, batch_size=batch_size)
    logger.info("  Packed into %d batches (target size %d)", len(batch_idx_lists), batch_size)

    # id -> canonical assignments accumulated across batches
    full_id_to_canon: Dict[int, str] = {}

    for bnum, idxs in enumerate(batch_idx_lists, 1):
        batch_groups = [groups[i] for i in idxs]
        slim_groups = [{"id": j, **_slim(g)} for j, g in enumerate(batch_groups)]
        groups_json = json.dumps(slim_groups, indent=2)
        prompt = P.MERGE_GROUPS_PROMPT.format(
            node_type=node_type, groups_json=groups_json,
        )
        for attempt in range(3):
            try:
                result = _llm(prompt, provider, model, llm_kwargs)
                break
            except Exception as e:
                logger.warning("    batch %d/%d attempt %d: %s", bnum, len(batch_idx_lists), attempt + 1, e)
                if attempt == 2:
                    result = None
                else:
                    time.sleep(5 * (attempt + 1))
        if result is None:
            # The batch's groups are kept as they are.
            for j, idx in enumerate(idxs):
                full_id_to_canon[idx] = groups[idx].get("canonical_name", "")
            continue
        local_map = _decode_id_groups(_parse(result), batch_groups)
        coverage = sum(1 for v in local_map.values() if v)
        logger.info("  batch %d/%d: %d groups from %d input (%d/%d covered)",
                    bnum, len(batch_idx_lists), len(set(local_map.values())), len(batch_groups),
                    coverage, len(batch_groups))
        for j, idx in enumerate(idxs):
            full_id_to_canon[idx] = local_map.get(j, batch_groups[j].get("canonical_name", ""))

    # Apply the per-batch decisions to the original groups
    merged = _apply_id_to_canon(groups, full_id_to_canon)
    logger.info("  After per-batch merges: %d groups", len(merged))

    if cross_batch in ("blocked", "report"):
        batch_of = {i: b for b, idxs in enumerate(batch_idx_lists) for i in idxs}
        origins = _origins(full_id_to_canon, batch_of)
        return blocked_cross_batch_pass(merged, node_type, provider, model, batch_size, origins,
                                        call_llm=(cross_batch == "blocked"),
                                        min_overlap=min_overlap, llm_kwargs=llm_kwargs, prompts=P)
    if cross_batch == "off":
        return merged

    # "auto": one global pass over the merged groups, when they fit in a single batch.
    if len(merged) <= batch_size:
        slim_groups = [{"id": j, **_slim(g)} for j, g in enumerate(merged)]
        groups_json = json.dumps(slim_groups, indent=2)
        prompt = P.MERGE_GROUPS_PROMPT.format(
            node_type=node_type, groups_json=groups_json,
        )
        try:
            result = _llm(prompt, provider, model, llm_kwargs)
            local_map = _decode_id_groups(_parse(result), merged)
            merged = _apply_id_to_canon(merged, local_map)
            logger.info("  After cross-batch global merge: %d groups", len(merged))
        except Exception as e:
            logger.warning("  cross-batch merge failed: %s", e)
    else:
        logger.info("  Global cross-batch pass skipped (%d groups > batch size %d); "
                    "the 'blocked' cross-batch pass handles larger inputs", len(merged), batch_size)

    return merged


def _load_network(input_json: str | Path) -> Dict[str, Any]:
    with open(input_json) as f:
        net = json.load(f)
    logger.info("Loaded %s: %s  relationships=%d", input_json,
                "  ".join(f"{et}={len(net.get(et, []) or [])}" for et in ENTITY_TYPES),
                len(net.get("relationships", []) or []))
    return net


def merge_joint_network(
    input_json: str | Path,
    output_json: str | Path,
    provider: str,
    model: str,
    batch_size: int = 500,
    types: Optional[List[str]] = None,
    reasoning_effort: Optional[str] = None,
    max_output_tokens: Optional[int] = None,
    cross_batch_pass: Optional[str] = None,
    min_overlap: float = 0.5,
    prompts: str = "default",
) -> Path:
    """Run the LLM merge over ``types`` (default: all three entity types) and write the result.

    ``cross_batch_pass`` is one of "auto" (the default when None), "blocked", "report"
    or "off"; ``prompts`` names the prompt set. Returns the output path.
    """
    cross = cross_batch_pass or "auto"
    if cross not in CROSS_BATCH_MODES:
        raise ValueError(f"cross_batch_pass must be one of {CROSS_BATCH_MODES}, got {cross!r}")
    P = load_prompts(prompts)
    llm_kwargs = llm_options(reasoning_effort, max_output_tokens)
    out_path = Path(output_json)

    net = _load_network(input_json)
    for et in (types or list(ENTITY_TYPES)):
        net[et] = merge_one_type(
            net.get(et, []) or [], et,
            provider, model, batch_size,
            cross_batch=cross, min_overlap=min_overlap,
            llm_kwargs=llm_kwargs, prompts=P,
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(net, f, indent=2)
    logger.info("Wrote %s", out_path)
    return out_path


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Semantic cross-venue merge of the joint network's entities with an LLM.")
    parser.add_argument("--input", required=True, help="joint network JSON")
    parser.add_argument("--output", required=True, help="merged network JSON to write")
    parser.add_argument("--provider", default="google", help="openai, google or together")
    parser.add_argument("--model", default="gemini-2.5-pro")
    parser.add_argument("--batch-size", type=int, default=500)
    parser.add_argument("--types", nargs="+", default=list(ENTITY_TYPES),
                        help="entity types to merge (default: all three)")
    parser.add_argument("--reasoning-effort", default=None,
                        choices=["none", "minimal", "low", "medium", "high", "xhigh"],
                        help="reasoning effort for models that take one")
    parser.add_argument("--max-output-tokens", type=int, default=None)
    parser.add_argument("--cross-batch-pass", choices=list(CROSS_BATCH_MODES), default=None,
                        help="auto (default) | blocked | report | off")
    parser.add_argument("--min-overlap", type=float, default=0.5,
                        help="IDF-weighted token Jaccard for a cross-batch candidate pair")
    parser.add_argument("--prompts", default="default", help="prompt set (module name)")
    parser.add_argument("--log-dir", default="logs")
    args = parser.parse_args(argv)

    setup_logging(run_name="join_llm_merge", log_dir=args.log_dir)
    merge_joint_network(
        args.input, args.output, args.provider, args.model, batch_size=args.batch_size,
        types=args.types, reasoning_effort=args.reasoning_effort,
        max_output_tokens=args.max_output_tokens, cross_batch_pass=args.cross_batch_pass,
        min_overlap=args.min_overlap, prompts=args.prompts,
    )


if __name__ == "__main__":
    main()
