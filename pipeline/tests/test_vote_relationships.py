"""Tests for aiconstructlexis.vote.relationships: the link-level vote (strictest type
wins), label canonicalization, and the options per_paper_resolution, keep_all_quotes,
type_guard and evidence_check on a tiny synthetic joint network and trials."""
import json
import random
from pathlib import Path

from aiconstructlexis.vote import relationships as jrv
from aiconstructlexis.vote.relationships import (
    STRICTNESS, decide, guard_target, make_label, vote_relationships,
)

ETYPE = {
    "Reasoning": "constructs", "Safety": "constructs",
    "Refusal": "behaviors", "Code generation": "behaviors",
    "GSM8K": "measurements", "MMLU": "measurements",
}


def L(src, tgt, rtype):
    return make_label(src, tgt, rtype, ETYPE)


def votes(**models):
    """votes(m1=[(src, tgt, type), ...], ...) -> {model: {label: quote}}"""
    return {m: {L(*r): f"{m} quote" for r in rels} for m, rels in models.items()}


# ---- make_label ------------------------------------------------------------

def test_measured_by_instrument_is_always_target():
    assert L("GSM8K", "Reasoning", "measured_by") == ("Reasoning", "GSM8K", "measured_by")
    assert L("Reasoning", "GSM8K", "measured_by") == ("Reasoning", "GSM8K", "measured_by")
    assert L("GSM8K", "Refusal", "measured_by") == ("Refusal", "GSM8K", "measured_by")


def test_measured_by_between_instruments_keeps_direction():
    assert L("GSM8K", "MMLU", "measured_by") == ("GSM8K", "MMLU", "measured_by")
    assert L("MMLU", "GSM8K", "measured_by") == ("MMLU", "GSM8K", "measured_by")


def test_symmetric_types_are_sorted_and_causes_keeps_direction():
    assert L("Safety", "Reasoning", "related") == ("Reasoning", "Safety", "related")
    assert L("Safety", "Reasoning", "correlates") == ("Reasoning", "Safety", "correlates")
    assert L("Safety", "Reasoning", "causes") == ("Safety", "Reasoning", "causes")


# ---- decide ----------------------------------------------------------------

def test_one_model_is_not_enough():
    assert decide(votes(a=[("Reasoning", "Safety", "causes")]), 2) == {}


def test_agreeing_models_keep_their_type():
    v = votes(a=[("Reasoning", "Safety", "related")], b=[("Safety", "Reasoning", "related")])
    assert decide(v, 2) == {("Reasoning", "Safety", "related"): 1.0}


def test_link_counts_even_when_types_differ_and_strictest_wins():
    v = votes(a=[("Reasoning", "Safety", "causes")], b=[("Reasoning", "Safety", "related")])
    assert decide(v, 2) == {("Reasoning", "Safety", "causes"): 1.0}


def test_strictness_order_pairwise():
    # The intended order, written out rather than read from STRICTNESS so a change there is caught.
    pairs = [("causes", "measured_by"), ("causes", "correlates"), ("causes", "related"),
             ("measured_by", "correlates"), ("measured_by", "related"), ("correlates", "related")]
    for strict, loose in pairs:
        v = votes(a=[("Reasoning", "MMLU", strict)], b=[("Reasoning", "MMLU", loose)])
        (lab,) = decide(v, 2)
        assert lab[2] == strict, (strict, loose, lab)


def test_minority_strict_type_still_wins():
    v = votes(a=[("Reasoning", "Safety", "related")], b=[("Reasoning", "Safety", "related")],
              c=[("Safety", "Reasoning", "causes")])
    assert decide(v, 2) == {("Safety", "Reasoning", "causes"): 1.0}


def test_one_model_giving_two_types():
    v = votes(a=[("Reasoning", "Safety", "related"), ("Reasoning", "Safety", "causes")],
              b=[("Reasoning", "Safety", "related")])
    assert decide(v, 2) == {("Reasoning", "Safety", "causes"): 1.0}


def test_opposite_measured_by_directions_agree():
    v = votes(a=[("GSM8K", "Reasoning", "measured_by")], b=[("Reasoning", "GSM8K", "measured_by")])
    assert decide(v, 2) == {("Reasoning", "GSM8K", "measured_by"): 1.0}


def test_causal_direction_majority_and_tie():
    maj = votes(a=[("Reasoning", "Safety", "causes")], b=[("Reasoning", "Safety", "causes")],
                c=[("Safety", "Reasoning", "causes")])
    assert decide(maj, 2) == {("Reasoning", "Safety", "causes"): 1.0}
    tie = votes(a=[("Reasoning", "Safety", "causes")], b=[("Safety", "Reasoning", "causes")])
    assert decide(tie, 2) == {("Reasoning", "Safety", "causes"): 0.5, ("Safety", "Reasoning", "causes"): 0.5}


def test_random_properties():
    rng = random.Random(0)
    names = list(ETYPE)
    for _ in range(5000):
        a, b = rng.sample(names, 2)
        by_model = {}
        for m in rng.sample(["m1", "m2", "m3"], rng.randint(1, 3)):
            labs = {}
            for _ in range(rng.randint(1, 3)):
                src, tgt = (a, b) if rng.random() < 0.5 else (b, a)
                labs[L(src, tgt, rng.choice(STRICTNESS))] = ""
            by_model[m] = labs
        out = decide(by_model, 2)
        if len(by_model) < 2:
            assert out == {}
            continue
        given = {lab for labs in by_model.values() for lab in labs}
        strictest = min({lab[2] for lab in given}, key=STRICTNESS.index)
        assert abs(sum(out.values()) - 1) < 1e-9
        assert {lab[2] for lab in out} == {strictest}
        assert set(out) <= given
        assert all(set(lab[:2]) == {a, b} for lab in out)
        support = {lab: sum(lab in labs for labs in by_model.values()) for lab in given if lab[2] == strictest}
        assert {support[lab] for lab in out} == {max(support.values())}


# ---- guard_target ----------------------------------------------------------

def test_guard_target_rules():
    C, B, M = "constructs", "behaviors", "measurements"
    assert guard_target("measured_by", "Reasoning", "MMLU", C, M) is None
    assert guard_target("measured_by", "Refusal", "MMLU", B, M) is None
    assert guard_target("measured_by", "MMLU", "Reasoning", M, C) == ("Reasoning", "measured_by", "MMLU")
    assert guard_target("measured_by", "Reasoning", "Safety", C, C) == ("Reasoning", "related", "Safety")
    assert guard_target("measured_by", "MMLU", "GSM8K", M, M) == ("GSM8K", "related", "MMLU")
    assert guard_target("causes", "Reasoning", "Safety", C, C) is None
    assert guard_target("causes", "GSM8K", "Reasoning", M, C) == "drop"
    assert guard_target("correlates", "GSM8K", "MMLU", M, M) is None
    assert guard_target("correlates", "Reasoning", "Safety", C, C) is None
    assert guard_target("correlates", "MMLU", "Reasoning", M, C) == ("MMLU", "related", "Reasoning")
    assert guard_target("related", "MMLU", "Reasoning", M, C) is None


# ---- the full vote on a tiny network ---------------------------------------

def ent(name, names=(), nodes=None, papers=1, **kw):
    g = {"canonical_name": name, "original_names": list(names) or [name],
         "original_nodes": {n: {"definition": "", "papers": ps} for n, ps in (nodes or {}).items()},
         "paper_count": papers, "papers": []}
    g.update(kw)
    return g


def tiny_net():
    return {
        "constructs": [
            ent("Instruction following ability", ["Instruction following ability", "Instruction following"],
                {"Instruction following": [["c1", "P1"]]}, papers=50),
            ent("Natural language understanding", ["Natural language understanding", "Language understanding"],
                {"Language understanding": [["c1", "P2"]]}, papers=30),
            ent("Reasoning", papers=40), ent("Safety", papers=20),
        ],
        "measurements": [
            ent("CoLA", ["CoLA"], {"CoLA": [["c1", "P2"]]}, papers=10),
            ent("Cola (compositional image retrieval)", ["Cola", "COLA"], {"Cola": [["c1", "P4"]]}, papers=2),
            ent("MMLU", papers=60), ent("GSM8K", papers=60),
        ],
        "behaviors": [
            ent("Instruction following", ["Instruction following"], {"Instruction following": []}, papers=5),
            ent("Language understanding task performance", ["Language understanding"],
                {"Language understanding": [["c1", "P3"]]}, papers=3),
            ent("Refusal", papers=10), ent("Code generation", papers=10),
        ],
        "relationships": [],
        "name_mapping": {},
    }


def R(s, t, ty, ev):
    return {"source": s, "target": t, "type": ty, "evidence": ev}


def write_trials(d: Path, rel: dict, ent_types: dict = None):
    """rel: {model: {paper: [rels]}}; ent_types: {model: {paper: {type: [names]}}}."""
    for model, papers in rel.items():
        (d / "c1" / model).mkdir(parents=True, exist_ok=True)
        json.dump({p: [rs] for p, rs in papers.items()}, open(d / "c1" / model / "relationship_trials.json", "w"))
    for model, papers in (ent_types or {}).items():
        (d / "c1" / model).mkdir(parents=True, exist_ok=True)
        json.dump({p: [{"Nomological Network": {et: [{"name": n} for n in ns] for et, ns in types.items()}}]
                   for p, types in papers.items()},
                  open(d / "c1" / model / "entity_trials.json", "w"))


def run(d: Path, net: dict, models, report=None, **options):
    path = d / "net.json"
    json.dump(net, open(path, "w"))
    out = d / "out.json"
    written = vote_relationships(path, {"c1": d / "c1"}, models, threshold=2, out_json=out,
                                 report_json=report, **options)
    assert written == out
    return json.load(open(out))


def claims(net):
    return {(r["source"], r["type"], r["target"], p["paper"]): p["type_share"]
            for r in net["relationships"] for p in r["papers"]}


def quotes(net):
    return {(r["source"], r["type"], r["target"], e["paper"]): e for r in net["relationships"]
            for e in r["evidence_by_paper"]}


SCENARIO = {
    # P1: the construct's node holds "Instruction following" for P1.
    "m1": {"P1": [R("Instruction following", "MMLU", "measured_by", "Results are in Table 2.")],
           # P2: "Language understanding" and "Cola" belong to NLU and CoLA in P2.
           "P2": [R("Language understanding", "Cola", "measured_by", "We evaluate language understanding on CoLA.")],
           # P5: no membership; both models typed the name as a construct.
           "P5": [R("instruction following", "GSM8K", "related", "instruction following and GSM8K")],
           # P6: no membership, no entity trial: the collision rule decides.
           "P6": [R("Instruction-following", "Refusal", "related", "instruction following vs refusal")]},
    "m2": {"P1": [R("Instruction following", "MMLU", "measured_by", "We measure instruction-following on MMLU.")],
           "P2": [R("Language understanding", "Cola", "measured_by", "CoLA tests language understanding.")],
           "P5": [R("instruction following", "GSM8K", "related", "x")],
           "P6": [R("Instruction-following", "Refusal", "related", "y")]},
}
ENT_TYPES = {"m1": {"P5": {"constructs": ["Instruction following"]}},
             "m2": {"P5": {"constructs": ["instruction following"]}}}


def test_default_output_uses_spelling_resolution(tmp_path):
    write_trials(tmp_path, SCENARIO, ENT_TYPES)
    out = run(tmp_path, tiny_net(), ["m1", "m2"])
    c = claims(out)
    # Spelling: "instruction following" -> the behavior (written last), Cola -> the image retrieval benchmark.
    assert ("Instruction following", "MMLU", "measured_by", "P1") in {(s, t, ty, p) for s, ty, t, p in c}
    assert ("Language understanding task performance", "measured_by",
            "Cola (compositional image retrieval)", "P2") in c
    assert "relationship_vote" not in (out.get("metadata") or {})
    e = quotes(out)[("Instruction following", "measured_by", "MMLU", "P1")]
    assert set(e) == {"conference", "paper", "quote"} and e["quote"] == "Results are in Table 2."
    r = next(r for r in out["relationships"] if r["type"] == "measured_by" and r["target"] == "MMLU")
    assert r["paper_count"] == 1 and r["paper_weight"] == 1.0 and r["n_papers_split"] == 0
    assert r["papers_by_conference"] == {"c1": ["P1"]} and r["paper_count_by_conference"] == {"c1": 1}
    assert r["evidence"] == ["Results are in Table 2."]


def test_cli_matches_function(tmp_path):
    write_trials(tmp_path, SCENARIO, ENT_TYPES)
    via_function = run(tmp_path, tiny_net(), ["m1", "m2"])
    path = tmp_path / "net.json"
    out = tmp_path / "cli.json"
    jrv.main(["--joint", str(path), "--out", str(out), "--trials", f"c1:{tmp_path / 'c1'}",
              "--models", "m1", "m2", "--threshold", "2", "--log-dir", str(tmp_path / "logs")])
    assert json.load(open(out))["relationships"] == via_function["relationships"]


# ---------------------------------------------------------------- per_paper_resolution

def test_per_paper_resolution(tmp_path):
    write_trials(tmp_path, SCENARIO, ENT_TYPES)
    rep_path = tmp_path / "rep.json"
    out = run(tmp_path, tiny_net(), ["m1", "m2"], report=rep_path, per_paper_resolution=True)
    c = claims(out)
    # paper membership
    assert ("Instruction following ability", "measured_by", "MMLU", "P1") in c
    assert ("Natural language understanding", "measured_by", "CoLA", "P2") in c
    # entity-trial type (both models typed it a construct)
    assert ("GSM8K", "related", "Instruction following ability", "P5") in c
    # collision rule: the canonical name equal to the raw name wins (the behavior)
    assert ("Instruction following", "related", "Refusal", "P6") in c
    rep = json.load(open(rep_path))
    steps = rep["resolution_steps"]
    assert steps["paper_membership"] >= 4 and steps["entity_trial_type"] == 2 and steps["collision_rule"] == 2
    assert rep["collisions"][0]["chosen"] == "Instruction following"
    assert "instruction following" in rep["mentions_rerouted"]
    assert out["metadata"]["relationship_vote"]["flags"]["per_paper_resolution"] is True


def test_collision_rule_order():
    pc = {"A ability": 50, "A": 5, "B big": 300, "B small": 1}
    key = jrv.PerPaperResolver.collision_key
    assert min(["A ability", "A"], key=lambda c: key("A", c, pc)) == "A"           # canonical match
    assert min(["A ability", "A"], key=lambda c: key("a", c, pc)) == "A"           # lowercase match
    # no canonical match: more shared words, then not removed, then more papers
    assert min(["B big", "B small"], key=lambda c: key("b", c, pc)) == "B big"
    assert min(["B big", "B small"], key=lambda c: key("b", c, pc, {"B big"})) == "B small"
    assert min(["Knowledge forgetting", "Knowledge retention"],
               key=lambda c: key("catastrophic forgetting", c, {})) == "Knowledge forgetting"


def test_lowercase_collision_without_membership_uses_rule():
    # "cola" in a paper with no membership and no entity trial: CoLA's canonical matches.
    net = tiny_net()
    r = jrv.PerPaperResolver(net, {g["canonical_name"]: et for et in jrv.ENTITY_TYPES for g in net[et]})
    assert r.resolve("cola", "c1", "P9", "m1") == "CoLA"
    assert r.resolve("Cola", "c1", "P4", "m1") == "Cola (compositional image retrieval)"
    assert r.resolve("COLA", "c1", "P2", "m1") == "CoLA"
    assert r.resolve("Unknown thing", "c1", "P2", "m1") is None


# ---------------------------------------------------------------- keep_all_quotes and evidence_check

def test_keep_all_quotes_and_evidence_check(tmp_path):
    write_trials(tmp_path, SCENARIO, ENT_TYPES)
    base = run(tmp_path, tiny_net(), ["m1", "m2"], report=tmp_path / "r0.json", evidence_check=True)
    e0 = quotes(base)[("Instruction following", "measured_by", "MMLU", "P1")]
    assert e0["quote"] == "Results are in Table 2."
    assert e0["evidence_check"] == {"source": False, "target": False}
    out = run(tmp_path, tiny_net(), ["m1", "m2"], report=tmp_path / "r1.json",
              keep_all_quotes=True, evidence_check=True)
    e1 = quotes(out)[("Instruction following", "measured_by", "MMLU", "P1")]
    assert e1["quote"] == "We measure instruction-following on MMLU."
    assert [q["model"] for q in e1["quotes"]] == ["m1", "m2"]
    assert e1["evidence_check"] == {"source": True, "target": True}
    r0, r1 = json.load(open(tmp_path / "r0.json")), json.load(open(tmp_path / "r1.json"))
    assert r1["evidence"]["both endpoints named"] > r0["evidence"]["both endpoints named"]
    assert r1["evidence"]["quote changed by keep-all-quotes"] >= 1
    # Without keep_all_quotes the papers and shares do not change.
    assert claims(base) == claims(run(tmp_path, tiny_net(), ["m1", "m2"]))


def test_quote_names_matching():
    f = jrv._ev_variants("Instruction following") | jrv._ev_variants("Instruction-following")
    assert jrv.quote_names("We test Instruction-Following here.", f)
    assert jrv.quote_names("instruction following.", f)
    assert not jrv.quote_names("we follow instructions", f)
    assert jrv.quote_names("Hallucinations were frequent", jrv._ev_variants("Hallucination"))
    assert jrv.quote_names("on GSM-8K", jrv._ev_variants("GSM8K"))
    assert not jrv.quote_names("on GSM8KX", jrv._ev_variants("GSM8K"))
    assert not jrv.quote_names("", f)


# ---------------------------------------------------------------- type_guard

GUARD_SCENARIO = {
    "m1": {"P1": [R("Reasoning", "Safety", "measured_by", "q1")],         # construct -> construct
           "P2": [R("GSM8K", "Reasoning", "causes", "q2")],                # causes with an instrument
           "P3": [R("MMLU", "Reasoning", "correlates", "q3")],             # instrument with construct
           "P4": [R("Refusal", "Code generation", "measured_by", "q4")],   # direction tie, two behaviors
           "P5": [R("MMLU", "GSM8K", "correlates", "q5")],                 # two instruments: allowed
           "P6": [R("Reasoning", "MMLU", "measured_by", "q6")]},           # allowed
    "m2": {"P1": [R("Reasoning", "Safety", "measured_by", "r1")],
           "P2": [R("GSM8K", "Reasoning", "causes", "r2")],
           "P3": [R("MMLU", "Reasoning", "correlates", "r3")],
           "P4": [R("Code generation", "Refusal", "measured_by", "r4")],
           "P5": [R("GSM8K", "MMLU", "correlates", "r5")],
           "P6": [R("MMLU", "Reasoning", "measured_by", "r6")]},
}


def test_type_guard_moves_and_drops_claims(tmp_path):
    write_trials(tmp_path, GUARD_SCENARIO)
    plain = run(tmp_path, tiny_net(), ["m1", "m2"])
    guarded = run(tmp_path, tiny_net(), ["m1", "m2"], report=tmp_path / "g.json", type_guard=True)
    c = claims(guarded)
    assert c == {("Reasoning", "related", "Safety", "P1"): 1.0,
                 ("MMLU", "related", "Reasoning", "P3"): 1.0,
                 ("Code generation", "related", "Refusal", "P4"): 1.0,
                 ("GSM8K", "correlates", "MMLU", "P5"): 1.0,
                 ("Reasoning", "measured_by", "MMLU", "P6"): 1.0}
    # The two tied directions of P4 landed on the same related edge and their shares add up;
    # the quote comes from the first of the merged labels in sorted order (m2's direction).
    assert {k: v["quote"] for k, v in quotes(guarded).items()} == {
        ("Reasoning", "related", "Safety", "P1"): "q1",
        ("MMLU", "related", "Reasoning", "P3"): "q3",
        ("Code generation", "related", "Refusal", "P4"): "r4",
        ("GSM8K", "correlates", "MMLU", "P5"): "q5",
        ("Reasoning", "measured_by", "MMLU", "P6"): "q6"}
    rep = json.load(open(tmp_path / "g.json"))
    assert rep["type_guard"]["claims_dropped:causes"] == 1
    assert rep["type_guard"]["claims_moved:measured_by->related"] == 3
    assert rep["type_guard"]["claims_moved:correlates->related"] == 1
    # the unguarded vote had the tie at 0.5 and the causes claim
    cp = claims(plain)
    assert cp[("Refusal", "measured_by", "Code generation", "P4")] == 0.5
    assert ("GSM8K", "causes", "Reasoning", "P2") in cp


def test_all_options_together_run(tmp_path):
    write_trials(tmp_path, {m: {**SCENARIO[m], **GUARD_SCENARIO[m]} for m in ("m1", "m2")}, ENT_TYPES)
    out = run(tmp_path, tiny_net(), ["m1", "m2"], per_paper_resolution=True, keep_all_quotes=True,
              type_guard=True, evidence_check=True)
    assert out["metadata"]["relationship_vote"]["flags"] == {
        "per_paper_resolution": True, "keep_all_quotes": True, "type_guard": True, "evidence_check": True}
    et = {g["canonical_name"]: t for t in jrv.ENTITY_TYPES for g in out[t]}
    for r in out["relationships"]:
        assert guard_target(r["type"], r["source"], r["target"], et[r["source"]], et[r["target"]]) is None
        for e in r["evidence_by_paper"]:
            assert set(e["evidence_check"]) == {"source", "target"} and e["quotes"]
