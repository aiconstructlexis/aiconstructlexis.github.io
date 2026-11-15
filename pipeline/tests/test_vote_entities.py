"""Tests for the canonical-level entity votes (one venue and joint) on synthetic trials."""
import json

from aiconstructlexis.vote.entities import build_name_mapping, vote_entities
from aiconstructlexis.vote.joint_entities import vote_joint_entities


def ent(name, names=(), papers=()):
    return {"canonical_name": name, "original_names": list(names) or [name],
            "papers": list(papers), "paper_count": len(papers)}


def write_entity_trials(trials_dir, model, per_paper):
    """per_paper: {paper: {entity type: [names]}} -> <trials_dir>/<model>/entity_trials.json"""
    d = trials_dir / model
    d.mkdir(parents=True, exist_ok=True)
    json.dump({p: [{"Nomological Network": {et: [{"name": n} for n in ns] for et, ns in types.items()}}]
               for p, types in per_paper.items()}, open(d / "entity_trials.json", "w"))


def venue_net():
    return {
        "constructs": [ent("Reasoning", ["Reasoning", "Reasoning ability"], ["P1", "P9"]),
                       ent("Safety", papers=["P1"])],
        "measurements": [ent("GSM8K", ["GSM8K", "GSM-8K"])],
        "behaviors": [],
        "relationships": [],
        "name_mapping": {"reasoning capability": "Reasoning"},
    }


def write_venue_trials(d):
    write_entity_trials(d, "m1", {"P1": {"constructs": ["Reasoning ability"], "measurements": ["GSM8K"]},
                                  "P2": {"constructs": ["Reasoning"]},
                                  "P3": {"measurements": ["Reasoning"]}})
    write_entity_trials(d, "m2", {"P1": {"constructs": ["reasoning"], "measurements": ["gsm-8k"]},
                                  "P3": {"constructs": ["Reasoning"]}})
    write_entity_trials(d, "m3", {"P1": {"constructs": ["Reasoning capability"]},
                                  "P4": {"constructs": ["Safety"]}})


def test_build_name_mapping_covers_all_names_and_name_mapping():
    nm = build_name_mapping(venue_net())
    assert nm["reasoning"] == "Reasoning" and nm["reasoning ability"] == "Reasoning"
    assert nm["gsm-8k"] == "GSM8K" and nm["reasoning capability"] == "Reasoning"


def test_vote_entities_counts_canonical_votes_per_paper(tmp_path):
    write_venue_trials(tmp_path / "trials")
    path = tmp_path / "h.json"
    json.dump(venue_net(), open(path, "w"))
    out = vote_entities(path, tmp_path / "trials", ["m1", "m2", "m3"], threshold=2, drop_zero=True)
    assert out == path  # rewritten in place
    net = json.load(open(path))
    reasoning = next(g for g in net["constructs"] if g["canonical_name"] == "Reasoning")
    # P1: three models through three surface forms; P3: m1 named it as a measurement, so one construct vote
    assert reasoning["papers"] == ["P1"] and reasoning["paper_count"] == 1
    assert reasoning["_canonical_mv"] == {"threshold": 2, "n_papers_total": 3, "n_papers_mv": 1}
    # Safety: one vote only -> dropped
    assert [g["canonical_name"] for g in net["constructs"]] == ["Reasoning"]
    gsm = net["measurements"][0]
    assert gsm["papers"] == ["P1"] and gsm["paper_count"] == 1


def test_vote_entities_keep_zero_and_out_json(tmp_path):
    write_venue_trials(tmp_path / "trials")
    path = tmp_path / "h.json"
    json.dump(venue_net(), open(path, "w"))
    out = vote_entities(path, tmp_path / "trials", ["m1", "m2", "m3"], threshold=2, drop_zero=False,
                        out_json=tmp_path / "voted.json")
    assert out == tmp_path / "voted.json"
    assert json.load(open(path)) == venue_net()  # input untouched
    net = json.load(open(out))
    safety = next(g for g in net["constructs"] if g["canonical_name"] == "Safety")
    assert safety["papers"] == [] and safety["paper_count"] == 0
    # threshold 1 keeps every paper any model named
    vote_entities(path, tmp_path / "trials", ["m1", "m2", "m3"], threshold=1, out_json=tmp_path / "t1.json")
    reasoning = next(g for g in json.load(open(tmp_path / "t1.json"))["constructs"]
                     if g["canonical_name"] == "Reasoning")
    assert reasoning["papers"] == ["P1", "P2", "P3"]


def test_vote_entities_missing_model_is_skipped(tmp_path):
    write_venue_trials(tmp_path / "trials")
    path = tmp_path / "h.json"
    json.dump(venue_net(), open(path, "w"))
    vote_entities(path, tmp_path / "trials", ["m1", "m2", "absent"], threshold=2)
    net = json.load(open(path))
    assert [g["canonical_name"] for g in net["constructs"]] == ["Reasoning"]


def joint_net():
    return {
        "constructs": [{"canonical_name": "Reasoning", "original_names": ["Reasoning", "Reasoning ability"],
                        "papers": [], "paper_count": 0},
                       {"canonical_name": "Safety", "original_names": ["Safety"], "papers": [], "paper_count": 0}],
        "measurements": [], "behaviors": [], "relationships": [], "name_mapping": {},
    }


def test_vote_joint_entities_counts_per_venue(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    write_entity_trials(a, "m1", {"P1": {"constructs": ["Reasoning"]}, "P2": {"constructs": ["Safety"]}})
    write_entity_trials(a, "m2", {"P1": {"constructs": ["reasoning ability"]}})
    write_entity_trials(b, "m1", {"Q1": {"constructs": ["Reasoning"]}})
    write_entity_trials(b, "m2", {"Q1": {"constructs": ["Reasoning"]}, "Q2": {"constructs": ["Reasoning"]}})
    path = tmp_path / "joint.json"
    json.dump(joint_net(), open(path, "w"))
    out = vote_joint_entities(path, {"a": a, "b": b}, ["m1", "m2"], threshold=2, out_json=tmp_path / "v.json")
    net = json.load(open(out))
    assert [g["canonical_name"] for g in net["constructs"]] == ["Reasoning"]  # Safety had one vote
    r = net["constructs"][0]
    assert r["papers"] == [{"conference": "a", "paper": "P1"}, {"conference": "b", "paper": "Q1"}]
    assert r["papers_by_conference"] == {"a": ["P1"], "b": ["Q1"]}
    assert r["paper_count"] == 2 and r["paper_count_by_conference"] == {"a": 1, "b": 1}
    assert r["_canonical_mv"] == {"threshold": 2, "n_papers_total": 3, "n_papers_mv": 2}
