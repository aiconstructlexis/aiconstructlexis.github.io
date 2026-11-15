"""Curation overlay: apply reviewer operations to a joint network.

After the vote stages, domain experts review the entity catalog and the relationships.
Their decisions are recorded as operations, one JSON object per line of a JSONL file, and
this stage applies them to the network. Keeping the review as data means the network can
be rebuilt from the extraction outputs and the same review applied again, and every change to the
catalog is traceable to one line. The input file is left untouched.

Entity references
-----------------
An entity is addressed by its type and its canonical name in the input network::

    {"type": "construct", "name": "Mathematical reasoning"}

Types are ``construct``, ``measurement`` and ``behavior``. A destination (the ``to`` of a
move_alias line, a part of a split) that names no input entity refers to the entity that
ends up with that type and name after the overlay's renames and retypes; failing that, a
new entity of that type and name is created. New entities are matched ignoring case,
hyphens and spacing, so lines sending names to "Fact checking" and "Fact-checking" fill
one entity.

Entity operations
-----------------
Every operation may carry an optional free-text ``"reason"``. One example per operation:

move_alias
    A surface name, its node (definition and papers) and its snippets move to another
    entity. Chains (A -> B, then B -> C for one name) are followed to C. When two lines
    move the same name out of the same entity, the later line wins and the earlier one is
    reported as a conflict; opposite moves (A -> B and B -> A) are settled by the later
    line as well.

    {"op": "move_alias", "name": "Passage retrieval", "from": {"type": "behavior", "name": "Text generation"}, "to": {"type": "behavior", "name": "Information retrieval"}}

remove_alias
    The name, its node and its snippets are dropped from the entity.

    {"op": "remove_alias", "entity": {"type": "behavior", "name": "Text generation"}, "name": "Codon prediction", "reason": "not a model behavior"}

split
    Parts of an entity become entities of their own. Each part names the entity it goes
    to (an existing entity of that type and name, or a new one) and the surface names
    that go there; the part named after the entity itself stays. A name a move_alias or
    remove_alias line already handles is left to that line, and an entity's own canonical
    name never leaves it this way.

    {"op": "split", "entity": {"type": "behavior", "name": "Text generation"}, "into": [{"name": "Text generation", "type": "behavior", "names": ["Text generation", "Open-ended generation"]}, {"name": "Code generation", "type": "behavior", "names": ["Code generation", "Program synthesis"]}]}

set_type
    The entity moves to another type list.

    {"op": "set_type", "entity": {"type": "behavior", "name": "Calibration"}, "to": "construct"}

rename
    The canonical name changes; the old name stays as a surface name.

    {"op": "rename", "entity": {"type": "construct", "name": "Structural reasoning"}, "to": "Structured reasoning"}

merge
    The listed entities become one. Lines whose entity lists overlap form one cluster;
    the ``into`` entity with the most papers survives, takes the cluster's
    ``canonical_name`` (the last line's), and the other canonical names stay as surface
    names.

    {"op": "merge", "entities": [{"type": "construct", "name": "Performance"}, {"type": "construct", "name": "General ability"}], "into": {"type": "construct", "name": "General ability"}, "canonical_name": "General ability"}

remove_entity / restore_entity
    Set or clear ``expert_removed`` (``expert_removed_reason`` holds the reason). Removed
    entities stay in the network, so the export can keep them for transparency while the
    interface hides them. An entity this overlay merges away cannot be removed or
    restored (reported as a conflict).

    {"op": "remove_entity", "entity": {"type": "behavior", "name": "Retrieval-augmented generation"}, "reason": "A generation method, not a model behavior"}
    {"op": "restore_entity", "entity": {"type": "behavior", "name": "Backtracking"}}

set_summary
    Replaces the entity's summary (``characterization``) with the given text. The
    summarize stage leaves entities that already have a summary alone unless asked to
    regenerate them.

    {"op": "set_summary", "entity": {"type": "construct", "name": "Calibration"}, "text": "..."}

Paper credits
-------------
An entity's paper list records the papers the vote credited it with. Credits follow
surface names through the papers recorded on each name's node: a credit leaves an entity
with a name when that name's node is the only node of the entity listing the paper, and
arrives with a name when the node lists the paper and the name's previous entity held the
credit. Merged entities hold the union of their members' credits; a new entity that no
credit reaches keeps the papers its nodes were recorded in. Entities left with no surface
names or no papers are dropped. The pipeline recomputes relationships from the extraction
trials afterwards (see ``rerun_vote`` below), so relationships follow the new membership.

Relationship operations
-----------------------
A claim is one paper's support for one relationship, addressed by ``source``, ``type``,
``target`` and ``paper`` written as ``"<venue>:<title>"``. Endpoints are canonical names as
they stand after the entity operations (a renamed entity is addressed by its new name).
Relationships of type related and correlates store their endpoints in sorted order, as the
vote does, whatever order a line gives.

retract_claim
    The paper no longer supports the relationship; a relationship left with no papers is
    dropped.

    {"op": "retract_claim", "source": "Mathematical reasoning", "type": "measured_by", "target": "GSM8K", "paper": "iclr25:On Speeding Up Language Model Evaluation", "reason": "the two terms only co-occur"}

retype
    The paper's claim keeps its endpoints and changes type (then goes through the type
    guard like every claim).

    {"op": "retype", "source": "Mathematical reasoning", "type": "measured_by", "target": "GSM8K", "paper": "acl25:DavIR: Data Selection via Implicit Reward for Large Language Models", "to": "related"}

move_claim
    The claim moves to another relationship (other endpoints, direction or type), keeping
    its evidence quote unless ``quote`` gives a new one. Landing on an existing claim of
    the same paper merges the two and keeps the existing quote.

    {"op": "move_claim", "source": "Reasoning", "type": "measured_by", "target": "GSM8K", "paper": "iclr24:Some Paper", "to": {"source": "Mathematical reasoning", "type": "measured_by", "target": "GSM8K"}}

add_claim
    Adds a paper's claim with the given quote; when the claim exists, only its quote is
    replaced.

    {"op": "add_claim", "source": "Mathematical reasoning", "type": "measured_by", "target": "GSM8K", "paper": "icml25:Some Paper", "quote": "we use the standard GSM8K and MATH benchmarks"}

A line whose claim is not in the network, or whose endpoints name no entity, is skipped
and listed in the report.

Type guard
----------
After the operations every relationship goes through the type guard (``guard_target`` of
aiconstructlexis.vote.relationships), which enforces which entity types each relationship
type may join:

measured_by   construct or behavior -> measurement instrument. An instrument -> construct
              or behavior relationship is reversed; any other pairing (two instruments,
              or two non-instruments) becomes related.
causes        no instrument at either end; a relationship with an instrument at either
              end is dropped with its claims (such claims describe the use of a dataset
              in training or a method, not a causal link between properties of a model).
correlates    two instruments (benchmark score correlations) or two non-instruments; an
              instrument paired with a construct or behavior becomes related.
related       any pairing.

A relationship with an endpoint whose entity type is not a single type is left unchecked
and counted in the report.

Moved claims merge into an existing claim of that paper on the new relationship, keeping
its quote. Afterwards each paper's type_share is recomputed as 1 divided by the number of
relationships that paper supports on the same pair of entities (a direction tie keeps
0.5), and paper_count, paper_weight, papers_by_conference, paper_count_by_conference and
the evidence lists are rebuilt from the papers.

Order of application
--------------------
1. Entity operations: moves and removals (with chains and conflicts), split parts no
   move line covers, retypes, renames, merges, removals and restorations, summaries.
2. Paper credits are updated, empty entities are dropped, the entity lists are re-sorted
   and the name mapping is rebuilt.
3. With ``rerun_vote``, the network is written and ``rerun_vote(network_json, out_json)``
   recomputes the relationships from the extraction trials (the pipeline passes the
   relationship vote). Without it, relationship endpoints are mapped through the renames
   and merges, and relationships of dropped entities are removed.
4. Relationship operations, then the type guard.

Outputs: the network at ``out_json`` and, with ``report_json``, a report that lists what
each line did (applied, skipped, stale or conflict, with the reason).
"""
from __future__ import annotations

import argparse
import copy
import json
import logging
from collections import Counter, defaultdict
from pathlib import Path

from aiconstructlexis.vote.relationships import guard_target

logger = logging.getLogger(__name__)

ENTITY_TYPES = ("constructs", "measurements", "behaviors")
SINGULAR = {"constructs": "construct", "measurements": "measurement", "behaviors": "behavior"}
PLURAL = {v: k for k, v in SINGULAR.items()}
ENTITY_OPS = ("move_alias", "remove_alias", "split", "set_type", "rename", "merge",
              "remove_entity", "restore_entity", "set_summary")
RELATIONSHIP_OPS = ("retract_claim", "retype", "move_claim", "add_claim")
UNDIRECTED = ("related", "correlates")
MAX_EVIDENCE = 10          # distinct quotes kept per relationship, as in the vote
TYPE_GUARD_RULE = ("measured_by: construct or behavior -> instrument (instrument -> construct or behavior "
                   "reversed, other pairings related); causes: no instrument at either end (else dropped); "
                   "correlates: two instruments or two non-instruments (else related); related: any")


class OverlayError(ValueError):
    """An overlay line is malformed."""


def norm(s: str) -> str:
    """Name key ignoring case, hyphens, underscores, slashes and spacing."""
    s = (s or "").strip().lower()
    for ch in "-_/":
        s = s.replace(ch, " ")
    return " ".join(s.split())


def plural_type(t, line_no=None) -> str:
    """'construct' or 'constructs' -> 'constructs' (and so on for the other types)."""
    if t in PLURAL:
        return PLURAL[t]
    if t in SINGULAR:
        return t
    where = f"line {line_no}: " if line_no is not None else ""
    raise OverlayError(f"{where}unknown entity type {t!r}; expected construct, measurement or behavior")


def read_overlay(path) -> list:
    """[(line number, operation)] from a JSONL file; blank lines are skipped."""
    out = []
    with open(path, encoding="utf-8") as f:
        for no, raw in enumerate(f, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                op = json.loads(raw)
            except json.JSONDecodeError as e:
                raise OverlayError(f"line {no}: not valid JSON ({e})") from None
            if not isinstance(op, dict) or op.get("op") not in ENTITY_OPS + RELATIONSHIP_OPS:
                raise OverlayError(f"line {no}: 'op' must be one of {', '.join(ENTITY_OPS + RELATIONSHIP_OPS)}")
            out.append((no, op))
    return out


# ------------------------------------------------------------------ entity operations

class Net:
    """The network as mutable entity objects, addressed by object identity."""

    def __init__(self, net: dict):
        self.net = net
        self.ents = []                       # live entity dicts
        self.etype = {}                      # id(entity) -> type list name
        self.created = set()                 # ids of entities this overlay created
        for et in ENTITY_TYPES:
            for g in net.get(et) or []:
                self.ents.append(g)
                self.etype[id(g)] = et
        self.by_key = {(self.etype[id(g)], g["canonical_name"]): g for g in self.ents}

    def names(self, g) -> list:
        """Every surface name the entity holds: original_names plus nodes not listed there."""
        seen, out = set(), []
        for n in list(g.get("original_names") or []) + list((g.get("original_nodes") or {}).keys()):
            if n not in seen:
                seen.add(n)
                out.append(n)
        return out

    def has(self, g, name) -> bool:
        return name in (g.get("original_names") or []) or name in (g.get("original_nodes") or {})

    def take(self, g, name):
        """Detach a surface name from g; returns (node or None, snippets)."""
        g["original_names"] = [n for n in (g.get("original_names") or []) if n != name]
        node = (g.get("original_nodes") or {}).pop(name, None)
        snips = [s for s in (g.get("source_snippets_evidence") or []) if s.get("original_name") == name]
        g["source_snippets_evidence"] = [s for s in (g.get("source_snippets_evidence") or [])
                                         if s.get("original_name") != name]
        return node, snips

    def put(self, g, name, node, snips) -> None:
        if name not in g.setdefault("original_names", []):
            g["original_names"].append(name)
        if node is not None:
            nodes = g.setdefault("original_nodes", {})
            if name in nodes:
                have = {tuple(p) for p in nodes[name].get("papers") or []}
                nodes[name]["papers"] = (nodes[name].get("papers") or []) + \
                    [p for p in node.get("papers") or [] if tuple(p) not in have]
            else:
                nodes[name] = node
        g.setdefault("source_snippets_evidence", []).extend(snips)

    def create(self, et: str, name: str):
        g = {"canonical_name": name, "original_names": [], "original_nodes": {},
             "source_snippets_evidence": [], "papers_by_conference": {}, "papers": [],
             "paper_count": 0, "paper_count_by_conference": {}, "characterization": ""}
        self.ents.append(g)
        self.etype[id(g)] = et
        self.created.add(id(g))
        self.by_key[(et, name)] = g
        return g

    def find(self, et: str, name: str):
        """Live entity of this type whose canonical name matches, ignoring case, hyphens and spacing."""
        g = self.by_key.get((et, name))
        if g is not None and any(g is e for e in self.ents):
            return g
        key = norm(name)
        for e in self.ents:
            if self.etype[id(e)] == et and norm(e["canonical_name"]) == key:
                return e
        return None


def _node_papers(g) -> set:
    return {tuple(p) for node in (g.get("original_nodes") or {}).values() for p in node.get("papers") or []}


def apply_entity_operations(net: dict, lines: list) -> tuple:
    """Apply the entity operations in ``lines`` ([(line_no, op)]) to a copy of ``net``.

    Returns (network, report, canon_map). ``canon_map`` maps each input canonical name to
    the canonical name of the live entity holding it now (the entity it became, or the one
    that holds the name as a surface name), or None when it is gone;
    names shared by entities of two types that ended up apart are left out.
    """
    net = copy.deepcopy(net)
    N = Net(net)
    report = {"status": {}, "notes": [], "created": [], "dropped": [], "conflicts": []}
    inputs = list(N.ents)
    input_type = dict(N.etype)
    input_by_key = dict(N.by_key)
    input_names = {id(g): g["canonical_name"] for g in inputs}
    old_papers = {id(g): {(p["conference"], p["paper"]) for p in g.get("papers") or []} for g in inputs}
    by_obj = {id(g): g for g in inputs}

    def status(no, s, why=""):
        report["status"][str(no)] = s if not why else f"{s}: {why}"

    def ref(no, r, field):
        if not isinstance(r, dict) or not r.get("name") or not r.get("type"):
            raise OverlayError(f'line {no}: "{field}" must be {{"type": ..., "name": ...}}')
        return plural_type(r["type"], no), str(r["name"])

    def resolve(no, r, field):
        """The input entity a reference names: exact type and name, else ignoring case and hyphens."""
        et, name = ref(no, r, field)
        g = input_by_key.get((et, name))
        if g is None:
            key = norm(name)
            g = next((e for e in inputs if input_type[id(e)] == et and norm(e["canonical_name"]) == key), None)
        return g

    # Final (type, name) of each input entity after renames, retypes and merges: a destination
    # that names no input entity reuses an existing entity only if that entity ends up as it.
    renames, retypes, merged_away = {}, {}, set()
    for no, f in lines:
        if f["op"] == "rename":
            g = resolve(no, f.get("entity"), "entity")
            if g is not None and f.get("to"):
                renames[id(g)] = str(f["to"])
        elif f["op"] == "set_type":
            g = resolve(no, f.get("entity"), "entity")
            if g is not None:
                retypes[id(g)] = plural_type(f.get("to"), no)
        elif f["op"] == "merge":
            into = resolve(no, f["into"], "into") if f.get("into") else None
            for r in f.get("entities") or []:
                g = resolve(no, r, "entities")
                if g is not None and g is not into:
                    merged_away.add(id(g))
    final_key = {id(g): (retypes.get(id(g), input_type[id(g)]), norm(renames.get(id(g), g["canonical_name"])))
                 for g in inputs if id(g) not in merged_away}

    def dest_of(no, r):
        """Destination entity of a move: an input entity, one that ends up with that name, or a new one."""
        et, name = ref(no, r, "to")
        g = input_by_key.get((et, name))
        if g is not None:
            return g
        key = (et, norm(name))
        g = next((e for e in N.ents if id(e) in N.created
                  and (N.etype[id(e)], norm(e["canonical_name"])) == key), None)
        if g is None:
            g = next((e for e in N.ents if final_key.get(id(e)) == key), None)
            if g is not None:
                report["notes"].append(f"line {no}: {name} ({SINGULAR[et]}) is {g['canonical_name']} "
                                       "after its rename or retype")
        if g is None:
            g = N.create(et, name)
            report["created"].append({"type": SINGULAR[et], "canonical_name": name, "line": no})
        return g

    moved_out = defaultdict(set)   # id(entity) -> names an operation took out of it
    removed_names = set()
    moves = []                     # (source entity, target entity or None, name, node papers)

    # ---- 1. member operations: moves and removals, with chains and conflicts ----
    member_ops = {}   # (id(source entity), name) -> (line_no, op)
    for no, f in lines:
        if f["op"] not in ("move_alias", "remove_alias"):
            continue
        field = "from" if f["op"] == "move_alias" else "entity"
        src = resolve(no, f.get(field), field)
        if src is None:
            status(no, "stale", "source entity not in the network")
            continue
        name = f.get("name")
        if not name:
            raise OverlayError(f'line {no}: {f["op"]} needs a "name"')
        key = (id(src), name)
        if key in member_ops:
            prev_no = member_ops[key][0]
            status(prev_no, "conflict", f"superseded by line {no}")
            report["conflicts"].append([prev_no, no])
        member_ops[key] = (no, f)

    chained = set()     # (id(entity), name) a chain routed a name through
    cycle_losers = {}   # line number -> the later line that settled the cycle

    def final_target(src, name):
        """Follow A -> B -> C chains for one name; returns the entity, or None for a removal.
        A cycle (A -> B and B -> A: each side says the other holds the name's home) is settled
        by the later line: its destination is the home, and the earlier lines are conflicts."""
        path, seen, cur = [], [], src
        while True:
            entry = member_ops.get((id(cur), name))
            if entry is None:
                return cur
            no, f = entry
            if f["op"] == "remove_alias":
                return None
            d = dest_of(no, f.get("to"))
            if d is cur:
                return cur
            path.append(entry)
            seen.append(cur)
            if cur is not src:
                chained.add((id(cur), name))
            if any(d is e for e in seen):
                start = next(i for i, e in enumerate(seen) if e is d)
                cyc = path[start:]
                last = max(cyc, key=lambda e: e[0])
                for e in cyc:
                    if e is not last:
                        cycle_losers[e[0]] = last[0]
                return dest_of(last[0], last[1].get("to"))
            cur = d

    for (sid, name), (no, f) in member_ops.items():
        if f["op"] == "move_alias" and N.has(by_obj[sid], name):
            final_target(by_obj[sid], name)      # records which lines a chain carries out

    for (sid, name), (no, f) in sorted(member_ops.items(), key=lambda kv: kv[1][0]):
        src = by_obj[sid]
        if not N.has(src, name):
            if (sid, name) in chained:
                status(no, "applied", "carried out through a chain from another entity")
            else:
                status(no, "stale", "name not in the source entity")
            continue
        if f["op"] == "remove_alias":
            node, _ = N.take(src, name)
            moved_out[id(src)].add(name)
            moves.append((src, None, name, (node or {}).get("papers") or []))
            removed_names.add(name)
            status(no, "applied")
            continue
        tgt = final_target(src, name)
        node, snips = N.take(src, name)
        moved_out[id(src)].add(name)
        moves.append((src, tgt, name, (node or {}).get("papers") or []))
        if tgt is None:
            removed_names.add(name)
            status(no, "applied", "chained into a removal")
        else:
            N.put(tgt, name, node, snips)
            status(no, "applied")

    for lno, winner in cycle_losers.items():
        report["status"][str(lno)] = f"conflict: opposite move settled by line {winner}"
        report["conflicts"].append([lno, winner])

    # ---- 2. split parts that no move line carries out ----
    covered = set(member_ops)
    for no, f in lines:
        if f["op"] != "split":
            continue
        src = resolve(no, f.get("entity"), "entity")
        if src is None:
            status(no, "stale", "entity not in the network")
            continue
        moved = []
        for part in f.get("into") or []:
            pname = str(part.get("name") or part.get("canonical_name") or "").strip()
            pet = plural_type(part.get("type") or SINGULAR[N.etype[id(src)]], no)
            pending = [n for n in part.get("names") or []
                    if N.has(src, n) and (id(src), n) not in covered and n != src["canonical_name"]]
            if not pending or not pname or pname.lower() == src["canonical_name"].lower():
                continue
            tgt = N.find(pet, pname)
            if tgt is src:
                continue
            if tgt is None:
                tgt = N.create(pet, pname)
                report["created"].append({"type": SINGULAR[pet], "canonical_name": pname, "line": no})
            for n in pending:
                node, snips = N.take(src, n)
                moved_out[id(src)].add(n)
                moves.append((src, tgt, n, (node or {}).get("papers") or []))
                N.put(tgt, n, node, snips)
                moved.append(f"{n} -> {tgt['canonical_name']}")
        status(no, "applied", ("parts carried out by move lines" if not moved
                               else "also moved " + "; ".join(moved)))

    # ---- 3. retype ----
    for no, f in lines:
        if f["op"] != "set_type":
            continue
        g = resolve(no, f.get("entity"), "entity")
        if g is None:
            status(no, "stale", "entity not in the network")
            continue
        N.etype[id(g)] = plural_type(f.get("to"), no)
        status(no, "applied")

    # ---- 4. rename (the old name stays as a surface name) ----
    for no, f in lines:
        if f["op"] != "rename":
            continue
        g = resolve(no, f.get("entity"), "entity")
        if g is None:
            status(no, "stale", "entity not in the network")
            continue
        if not f.get("to"):
            raise OverlayError(f'line {no}: rename needs a "to" name')
        old = g["canonical_name"]
        if old not in g.setdefault("original_names", []) and old not in moved_out[id(g)]:
            g["original_names"].append(old)
        g["canonical_name"] = str(f["to"])
        status(no, "applied")

    # ---- 5. merges, one per cluster ----
    parent = {}

    def root(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    merge_lines = [(no, f) for no, f in lines if f["op"] == "merge"]
    members_of = {}
    for no, f in merge_lines:
        ents, missing = [], False
        for r in f.get("entities") or []:
            g = resolve(no, r, "entities")
            if g is None:
                missing = True
            elif not any(g is e for e in ents):
                ents.append(g)
        if missing:
            status(no, "stale", "a cluster member is not in the network")
        members_of[no] = ents
        for e in ents[1:]:
            parent[root(id(e))] = root(id(ents[0]))
    clusters = defaultdict(list)
    for no, f in merge_lines:
        if members_of[no]:
            clusters[root(id(members_of[no][0]))].append((no, f))
    lineage = {id(g): [g] for g in N.ents}
    for cl in clusters.values():
        members = []
        for no, f in cl:
            for e in members_of[no]:
                if not any(e is m for m in members):
                    members.append(e)
        if len(members) < 2:
            continue
        names = {f.get("canonical_name") for no, f in cl if f.get("canonical_name")}
        if len(names) > 1:
            report["notes"].append(f"merge cluster of {[m['canonical_name'] for m in members]} has names "
                                   f"{sorted(names)}; using the last line's")
        intos = [resolve(no, f["into"], "into") for no, f in cl if f.get("into")]
        intos = [g for g in intos if g is not None] or members
        surv = max(intos, key=lambda g: (len(old_papers.get(id(g), ())), g["canonical_name"]))
        cname = max(cl, key=lambda e: e[0])[1].get("canonical_name") or surv["canonical_name"]
        surv.setdefault("original_names", [])
        for g in members:
            if g is surv:
                continue
            for n in N.names(g):
                node, snips = N.take(g, n)
                N.put(surv, n, node, snips)
            if g["canonical_name"] not in surv["original_names"] and g["canonical_name"] not in moved_out[id(g)]:
                surv["original_names"].append(g["canonical_name"])
            lineage[id(surv)].extend(lineage.pop(id(g), [g]))
            N.ents = [e for e in N.ents if e is not g]
        old = surv["canonical_name"]
        if old != cname and old not in surv["original_names"] and old not in moved_out[id(surv)]:
            surv["original_names"].append(old)
        surv["canonical_name"] = cname
        if surv.get("expert_removed") and not all(m.get("expert_removed") for m in members):
            report["notes"].append(f"merge into the removed entity {old} keeps it removed")
        for no, f in cl:
            if str(no) not in report["status"]:
                status(no, "applied", f"cluster of {len(members)} -> {cname}")

    # ---- 6. remove / restore / summary ----
    def live(g):
        """The live entity an input entity resolves to (follows merges)."""
        for e in N.ents:
            if e is g or any(o is g for o in lineage.get(id(e), [])):
                return e
        return None

    for no, f in lines:
        if f["op"] not in ("remove_entity", "restore_entity", "set_summary"):
            continue
        g0 = resolve(no, f.get("entity"), "entity")
        g = live(g0) if g0 is not None else None
        if g is None:
            status(no, "stale", "entity not in the network or no longer live")
            continue
        if f["op"] != "set_summary" and g is not g0:
            status(no, "conflict", f"entity was merged into {g['canonical_name']}; not applied to the survivor")
            continue
        if f["op"] == "remove_entity":
            g["expert_removed"] = True
            g["expert_removed_reason"] = str(f.get("reason") or "")
        elif f["op"] == "restore_entity":
            g["expert_removed"] = False
            g.pop("expert_removed_reason", None)
        else:
            g["characterization"] = str(f.get("text") or "")
            g.pop("characterization_sections", None)
        status(no, "applied")

    for no, f in lines:
        report["status"].setdefault(str(no), "not_applied")

    # ---- 7. paper credits, empty entities, lists and name mapping ----
    _reassign_papers(N, lineage, old_papers, moves, report)
    keep = []
    for g in N.ents:
        if not N.names(g):
            report["dropped"].append({"type": SINGULAR[N.etype[id(g)]], "canonical_name": g["canonical_name"],
                                      "why": "no surface names left"})
        elif g["paper_count"] == 0:
            report["dropped"].append({"type": SINGULAR[N.etype[id(g)]], "canonical_name": g["canonical_name"],
                                      "why": "no papers"})
        else:
            keep.append(g)
    N.ents = keep
    for et in ENTITY_TYPES:
        net[et] = sorted((g for g in N.ents if N.etype[id(g)] == et), key=lambda g: g["canonical_name"].lower())
    net["name_mapping"] = rebuild_name_mapping(N, net.get("name_mapping") or {}, removed_names)

    owner = {}
    for g in N.ents:
        for o in lineage.get(id(g), []):
            owner[id(o)] = g
    targets = defaultdict(set)
    for o in inputs:
        g = owner.get(id(o))
        name = input_names[id(o)]
        # A dropped entity's name lives on where the name went as a surface name, if anywhere.
        targets[name].add(g["canonical_name"] if g is not None else net["name_mapping"].get(name))
    canon_map = {name: next(iter(ts)) for name, ts in targets.items() if len(ts) == 1}

    counts = Counter(s.split(":")[0] for s in report["status"].values())
    report["summary"] = {"status_counts": dict(counts),
                         "entities": {et: len(net[et]) for et in ENTITY_TYPES},
                         "created_and_kept": sum(1 for g in N.ents if id(g) in N.created),
                         "dropped": len(report["dropped"])}
    return net, report, canon_map


def _reassign_papers(N, lineage, old_papers, moves, report) -> None:
    """Paper credits follow surface names through the node paper lists (see the module docstring)."""
    owner = {}
    for g in N.ents:
        for o in lineage.get(id(g), []):
            owner[id(o)] = g
    lost_by, gained_by = defaultdict(set), defaultdict(set)
    for src, tgt, name, papers in moves:
        ps = {tuple(p) for p in papers}
        if not ps:
            continue
        s_live = owner.get(id(src))
        if s_live is not None:
            lost_by[id(s_live)] |= ps
        if tgt is not None:
            t_live = owner.get(id(tgt), tgt)
            gained_by[id(t_live)] |= ps & old_papers.get(id(src), set())
    gained_total = lost_total = fallback = 0
    for g in N.ents:
        olds = [o for o in lineage.get(id(g), []) if id(o) in old_papers]
        base = set().union(*[old_papers[id(o)] for o in olds]) if olds else set()
        lost = lost_by.get(id(g), set()) - _node_papers(g)
        papers = (base - lost) | gained_by.get(id(g), set())
        if not papers and id(g) in N.created:
            papers = _node_papers(g)
            fallback += 1 if papers else 0
        gained_total += len(papers - base)
        lost_total += len(base - papers)
        pbc = defaultdict(list)
        for conf, paper in sorted(papers):
            pbc[conf].append(paper)
        g["papers"] = [{"conference": c, "paper": p} for c in pbc for p in pbc[c]]
        g["papers_by_conference"] = dict(pbc)
        g["paper_count"] = len(g["papers"])
        g["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
    report["paper_links_gained"] = gained_total
    report["paper_links_lost"] = lost_total
    report["new_entities_on_node_papers"] = fallback


def rebuild_name_mapping(N, old_nm: dict, removed_names: set) -> dict:
    """Surface name -> canonical name for the live entities; mappings of the input that point
    at a name now held elsewhere follow it, and removed names drop out."""
    nm = {}
    for g in N.ents:
        for n in N.names(g) + [g["canonical_name"]]:
            nm.setdefault(n, g["canonical_name"])
    by_old = {}
    for g in N.ents:
        for n in N.names(g):
            by_old.setdefault(n, g["canonical_name"])
    for orig, canon in old_nm.items():
        if orig in nm or orig in removed_names:
            continue
        if canon in by_old:
            nm[orig] = by_old[canon]
    return nm


# ------------------------------------------------------------ relationship operations

def split_paper(p):
    conf, _, title = p.partition(":")
    return conf, title


def type_guard(edges, meta, etypes, report, log, guard=None):
    """Enforce the type constraints on edges ({key: {paper: claim}}) in place.

    ``guard`` defaults to ``guard_target``, the type-guard rule of the relationship vote
    (aiconstructlexis.vote.relationships).
    """
    guard = guard or guard_target
    for k in list(edges):
        papers = edges[k]
        s, ty, t = k
        if not papers:
            continue
        ts, tt = etypes.get(s, set()), etypes.get(t, set())
        if len(ts) != 1 or len(tt) != 1:
            report["guard_skipped_ambiguous_type"] += 1
            continue
        to = guard(ty, s, t, next(iter(ts)), next(iter(tt)))
        if to is None:
            continue
        log.append({"source": s, "type": ty, "target": t, "papers": len(papers),
                    "action": "dropped" if to == "drop" else f"moved to {to[0]} --{to[1]}--> {to[2]}"})
        edges[k] = {}
        if to == "drop":
            report[f"guard_claims_dropped:{ty}"] += len(papers)
            continue
        cur = edges.setdefault(to, {})
        if to not in meta:
            meta[to] = {"_n_papers_split_in": 0}
            report["guard_relationships_created"] += 1
        for pk, v in papers.items():
            if pk in cur:
                cur[pk]["quote"] = cur[pk]["quote"] or v["quote"]
            else:
                cur[pk] = dict(v)
        report[f"guard_claims_moved:{ty}->{to[1]}"] += len(papers)


def _sorted_key(s, ty, t):
    if ty in UNDIRECTED:
        return (min(s, t), ty, max(s, t))
    return (s, ty, t)


def apply_relationship_operations(net: dict, lines: list, canon_map: dict | None = None) -> tuple:
    """Apply the relationship operations in ``lines`` ([(line_no, op)]) and the type guard to
    a copy of ``net``. ``canon_map`` (input canonical name -> live name or None) maps the
    endpoints of the input relationships first. Returns (network, report)."""
    N = copy.deepcopy(net)
    canon_map = canon_map or {}
    names = {g["canonical_name"] for et in ENTITY_TYPES for g in N.get(et) or []}
    etypes = defaultdict(set)
    for et in ENTITY_TYPES:
        for g in N.get(et) or []:
            etypes[g["canonical_name"]].add(et)
    report = Counter()
    # edge -> {(conf, paper): {"share", "quote"}}, keeping the input's paper order
    edges, meta = {}, {}
    for r in N.get("relationships") or []:
        s = canon_map.get(r["source"], r["source"])
        t = canon_map.get(r["target"], r["target"])
        if s is None or t is None or s == t:
            report["relationships_dropped_with_entities"] += 1
            report["claims_dropped_with_entities"] += len(r.get("papers") or [])
            continue
        k = _sorted_key(s, r["type"], t)
        quotes = {(e["conference"], e["paper"]): e.get("quote") or "" for e in r.get("evidence_by_paper") or []}
        papers = {}
        for p in r["papers"]:
            pk = (p["conference"], p["paper"])
            papers[pk] = {"share": p.get("type_share", 1.0), "quote": quotes.get(pk, "")}
        if k in edges:
            cur = edges[k]
            for pk, v in papers.items():
                if pk in cur:
                    cur[pk]["quote"] = cur[pk]["quote"] or v["quote"]
                else:
                    cur[pk] = v
            report["relationships_merged_after_entity_changes"] += 1
            continue
        edges[k] = papers
        meta[k] = {x: v for x, v in r.items() if x not in ("source", "type", "target", "papers", "papers_by_conference",
                                                          "paper_count", "paper_count_by_conference", "paper_weight",
                                                          "evidence", "evidence_by_paper", "n_papers_split")}
        meta[k]["_n_papers_split_in"] = r.get("n_papers_split", 0)

    def claim_of(no, o):
        s, ty, t, p = o.get("source"), o.get("type"), o.get("target"), o.get("paper")
        if not (s and ty and t):
            raise OverlayError(f'line {no}: {o["op"]} needs "source", "type" and "target"')
        if not isinstance(p, str) or ":" not in p:
            raise OverlayError(f'line {no}: "paper" must be "<venue>:<title>"')
        return _sorted_key(s, ty, t), split_paper(p)

    def destination(no, o, k):
        if o["op"] == "retype":
            if not o.get("to"):
                raise OverlayError(f'line {no}: retype needs a "to" type')
            return _sorted_key(k[0], str(o["to"]), k[2])
        to = o.get("to")
        if not isinstance(to, dict) or not to:
            raise OverlayError(f'line {no}: move_claim needs a "to" object with source, type and/or target')
        return _sorted_key(to.get("source", k[0]), to.get("type", k[1]), to.get("target", k[2]))

    status = {}
    skipped, unknown_endpoint = [], []
    for no, o in lines:
        k, pk = claim_of(no, o)
        op = o["op"]
        if op == "retract_claim":
            if pk not in edges.get(k, {}):
                status[str(no)] = "skipped: claim not in the network"
                skipped.append(no)
                continue
            edges[k].pop(pk)
            report["claims_retracted"] += 1
        elif op in ("retype", "move_claim"):
            k2 = destination(no, o, k)
            if pk not in edges.get(k, {}):
                status[str(no)] = "skipped: claim not in the network"
                skipped.append(no)
                continue
            if k2[0] not in names or k2[2] not in names:
                status[str(no)] = "skipped: unknown endpoint"
                skipped.append(no)
                unknown_endpoint.append(no)
                continue
            moved = edges[k].pop(pk)
            cur = edges.setdefault(k2, {})
            if k2 not in meta:
                meta[k2] = {"_n_papers_split_in": 0}
                report["relationships_created"] += 1
            quote = o.get("quote") or moved["quote"]
            if pk in cur:
                cur[pk]["quote"] = cur[pk]["quote"] or quote
                report["claims_merged_into_existing"] += 1
            else:
                cur[pk] = {"share": 1.0, "quote": quote}
            report["claims_moved"] += 1
        else:   # add_claim
            if k[0] not in names or k[2] not in names:
                status[str(no)] = "skipped: unknown endpoint"
                skipped.append(no)
                unknown_endpoint.append(no)
                continue
            cur = edges.setdefault(k, {})
            if k not in meta:
                meta[k] = {"_n_papers_split_in": 0}
                report["relationships_created"] += 1
            if pk in cur:
                cur[pk]["quote"] = o.get("quote") or cur[pk]["quote"]
                report["quotes_replaced"] += 1
            else:
                cur[pk] = {"share": 1.0, "quote": o.get("quote") or ""}
                report["claims_added"] += 1
        status[str(no)] = "applied"
        report["lines_applied"] += 1
    report["lines_skipped"] = len(skipped)

    guard_log = []
    type_guard(edges, meta, etypes, report, guard_log, guard_target)

    # recompute type_share per (unordered pair, paper)
    per_pair = Counter()
    for (s, ty, t), papers in edges.items():
        for pk in papers:
            per_pair[(frozenset((s, t)), pk)] += 1
    rels = []
    for k, papers in edges.items():
        if not papers:
            report["relationships_dropped"] += 1
            continue
        s, ty, t = k
        r = {"source": s, "target": t, "type": ty, "papers": [], "papers_by_conference": {}}
        r.update({x: v for x, v in meta[k].items() if not x.startswith("_n_papers")})
        weight, ev, evp = 0.0, [], []
        for pk, v in papers.items():
            share = round(1 / per_pair[(frozenset((s, t)), pk)], 4)
            r["papers"].append({"conference": pk[0], "paper": pk[1], "type_share": share})
            r["papers_by_conference"].setdefault(pk[0], []).append(pk[1])
            weight += share
            if v["quote"]:
                evp.append({"conference": pk[0], "paper": pk[1], "quote": v["quote"]})
                if v["quote"] not in ev and len(ev) < MAX_EVIDENCE:
                    ev.append(v["quote"])
        r["paper_count"] = len(r["papers"])
        r["paper_weight"] = round(weight, 4)
        r["n_papers_split"] = min(meta[k]["_n_papers_split_in"], len(r["papers"]))
        r["paper_count_by_conference"] = {c: len(ps) for c, ps in r["papers_by_conference"].items()}
        r["evidence"] = ev
        r["evidence_by_paper"] = evp
        rels.append(r)
    rels.sort(key=lambda r: -r["paper_count"])
    N["relationships"] = rels
    report["relationships_in"] = len(net.get("relationships") or [])
    report["relationships_out"] = len(rels)
    report["claims_in"] = sum(len(r["papers"]) for r in net.get("relationships") or [])
    report["claims_out"] = sum(r["paper_count"] for r in rels)
    return N, dict(report, status=status, skipped=skipped, unknown_endpoint=unknown_endpoint,
                   type_guard=guard_log, type_guard_rule_from=guard_target.__module__)


# ------------------------------------------------------------------------- stage entry

def apply_overlay(network_json, overlay_jsonl, out_json, report_json=None, rerun_vote=None) -> Path:
    """Apply the reviewer operations in ``overlay_jsonl`` to the network in ``network_json``
    and write the result to ``out_json`` (and a report to ``report_json``).

    ``rerun_vote(network_json, out_json)``, when given, is called between the entity and the
    relationship operations with the network written to ``out_json``; it recomputes the
    relationships (the pipeline passes the relationship vote) and writes them to the same
    path. Returns the path written.
    """
    network_json, out_json = Path(network_json), Path(out_json)
    with open(network_json, encoding="utf-8") as f:
        net = json.load(f)
    lines = read_overlay(overlay_jsonl)
    entity_lines = [(no, op) for no, op in lines if op["op"] in ENTITY_OPS]
    rel_lines = [(no, op) for no, op in lines if op["op"] in RELATIONSHIP_OPS]
    logger.info("Overlay %s: %d entity operations, %d relationship operations",
                overlay_jsonl, len(entity_lines), len(rel_lines))

    net, ereport, canon_map = apply_entity_operations(net, entity_lines)
    logger.info("Entity operations: %s; paper links gained %d, lost %d", ereport["summary"],
                ereport["paper_links_gained"], ereport["paper_links_lost"])

    out_json.parent.mkdir(parents=True, exist_ok=True)
    if rerun_vote is not None:
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(net, f, indent=2, ensure_ascii=False)
        logger.info("Recomputing relationships for %s", out_json)
        rerun_vote(out_json, out_json)
        with open(out_json, encoding="utf-8") as f:
            net = json.load(f)
        canon_map = None

    net, rreport = apply_relationship_operations(net, rel_lines, canon_map)
    logger.info("Relationship operations: applied %d, skipped %d; relationships %d -> %d; type guard rule from %s",
                rreport.get("lines_applied", 0), rreport.get("lines_skipped", 0),
                rreport["relationships_in"], rreport["relationships_out"], rreport["type_guard_rule_from"])

    net.setdefault("metadata", {})["curation"] = {
        "overlay": Path(overlay_jsonl).name,
        "lines": len(lines),
        "entity_operations": ereport["summary"]["status_counts"],
        "relationship_operations": {"applied": rreport.get("lines_applied", 0),
                                    "skipped": rreport.get("lines_skipped", 0)},
        "type_guard": TYPE_GUARD_RULE,
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(net, f, indent=2, ensure_ascii=False)
    logger.info("Wrote %s", out_json)

    if report_json is not None:
        report = {"overlay": str(overlay_jsonl), "lines": len(lines), "entities": ereport,
                  "relationships": rreport}
        Path(report_json).parent.mkdir(parents=True, exist_ok=True)
        with open(report_json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        logger.info("Wrote %s", report_json)
    return out_json


def main(argv=None) -> None:
    from aiconstructlexis.util.logging import setup_logging

    p = argparse.ArgumentParser(description="Apply a JSONL of reviewer operations to a joint network.")
    p.add_argument("--network", required=True, help="joint network JSON (left untouched)")
    p.add_argument("--overlay", required=True, help="JSONL of operations, one per line")
    p.add_argument("--out", required=True, help="where the curated network is written")
    p.add_argument("--report", default=None, help="where the per-line report is written (default: <out>.report.json)")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args(argv)
    setup_logging(run_name="curate_overlay", log_dir=args.log_dir)
    report = args.report or str(Path(args.out).with_suffix(".report.json"))
    apply_overlay(network_json=args.network, overlay_jsonl=args.overlay, out_json=args.out, report_json=report)


if __name__ == "__main__":
    main()
