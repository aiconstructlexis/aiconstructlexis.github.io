"""Tests for the minimum-paper filter."""
import json

from aiconstructlexis.vote.filter import filter_min_papers, filter_network


def ent(name, n, names=()):
    return {"canonical_name": name, "original_names": list(names) or [name], "paper_count": n,
            "papers": [f"P{i}" for i in range(n)]}


def net():
    return {
        "constructs": [ent("Reasoning", 3, ["Reasoning", "Reasoning ability"]), ent("Rare", 1)],
        "measurements": [ent("MMLU", 2), ent("Tiny", 1)],
        "behaviors": [ent("Refusal", 2)],
        "relationships": [
            {"source": "Reasoning", "target": "MMLU", "type": "measured_by"},
            {"source": "Rare", "target": "MMLU", "type": "measured_by"},
            {"source": "Reasoning", "target": "Tiny", "type": "measured_by"},
            {"source": "Refusal", "target": "Reasoning", "type": "related"},
        ],
        "name_mapping": {"Rare": "Rare", "Reasoning": "Reasoning", "stale": "Gone"},
        "papers": ["P0", "P1", "P2"],
    }


def test_filter_network_drops_entities_relationships_and_rebuilds_mapping():
    out = filter_network(net(), 2)
    assert [g["canonical_name"] for g in out["constructs"]] == ["Reasoning"]
    assert [g["canonical_name"] for g in out["measurements"]] == ["MMLU"]
    assert [g["canonical_name"] for g in out["behaviors"]] == ["Refusal"]
    assert [(r["source"], r["target"]) for r in out["relationships"]] == [
        ("Reasoning", "MMLU"), ("Refusal", "Reasoning")]
    assert out["name_mapping"] == {"Reasoning": "Reasoning", "Reasoning ability": "Reasoning",
                                   "MMLU": "MMLU", "Refusal": "Refusal"}
    assert out["papers"] == ["P0", "P1", "P2"]  # other sections untouched


def test_threshold_three_and_one():
    assert [g["canonical_name"] for g in filter_network(net(), 3)["constructs"]] == ["Reasoning"]
    assert filter_network(net(), 3)["measurements"] == [] and filter_network(net(), 3)["relationships"] == []
    full = filter_network(net(), 1)
    assert len(full["relationships"]) == 4


def test_filter_min_papers_writes_default_name(tmp_path):
    src = tmp_path / "harmonized.json"
    json.dump(net(), open(src, "w"))
    out = filter_min_papers(src)
    assert out == tmp_path / "harmonized.multi_paper.json"
    assert json.load(open(src)) == net()  # input untouched
    written = json.load(open(out))
    assert [g["canonical_name"] for g in written["constructs"]] == ["Reasoning"]
    explicit = filter_min_papers(src, tmp_path / "sub" / "out.json", min_papers=3)
    assert explicit == tmp_path / "sub" / "out.json"
    assert json.load(open(explicit))["measurements"] == []
