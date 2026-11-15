"""Tests for the cross-venue union (aiconstructlexis.join.union)."""
import json

from aiconstructlexis.join.union import build_joint_network, join_networks


def ent(name, names, papers, nodes=None, **kw):
    g = {"canonical_name": name, "original_names": names, "papers": papers, "paper_count": len(papers),
         "original_nodes": {n: {"definition": f"def {n}", "papers": ps} for n, ps in (nodes or {}).items()},
         "source_snippets_evidence": [{"paper": papers[0], "snippet": f"{name} snippet"}] if papers else []}
    g.update(kw)
    return g


def venue_a():
    return {
        "constructs": [ent("Reasoning", ["Reasoning"], ["A1", "A2"], {"Reasoning": ["A1", "A2"]},
                           characterization="Reasoning in venue a", canonical_definition="")],
        "measurements": [ent("MMLU", ["MMLU"], ["A1"])],
        "behaviors": [],
        "relationships": [{"source": "Reasoning", "target": "MMLU", "type": "measured_by",
                           "papers": ["A1"], "evidence": ["ea"]}],
        "papers": ["A1", "A2"],
    }


def venue_b():
    return {
        "constructs": [ent("reasoning", ["Reasoning", "Reasoning skills"], ["B1"], {"Reasoning skills": ["B1"]},
                           canonical_definition="the capacity to reason"),
                       ent("Reasoning ability", ["Reasoning ability"], ["B2", "B3"]),
                       ent("Safety", ["Safety"], ["B1"])],
        "measurements": [ent("MMLU", ["MMLU", "Massive Multitask Language Understanding"], ["B1", "B2"])],
        "behaviors": [],
        "relationships": [{"source": "Reasoning", "target": "MMLU", "type": "measured_by",
                           "papers": [{"conference": "x", "paper": "B1"}], "evidence": ["ea", "eb"]},
                          {"source": "Safety", "target": "Reasoning", "type": "related", "papers": ["B1"]}],
        "papers": ["B1", "B2", "B3"],
    }


def test_union_at_canonical_name_without_postmerge():
    out = join_networks([("a", venue_a()), ("b", venue_b())], postmerge=False)
    assert out["metadata"] == {"joint_of": ["a", "b"], "n_conferences": 2}
    names = [g["canonical_name"] for g in out["constructs"]]
    assert names == ["Reasoning", "Reasoning ability", "Safety"]  # case-insensitive union, first spelling kept
    r = out["constructs"][0]
    assert r["original_names"] == ["Reasoning", "Reasoning skills"]
    assert r["papers_by_conference"] == {"a": ["A1", "A2"], "b": ["B1"]}
    assert r["papers"] == [{"conference": "a", "paper": "A1"}, {"conference": "a", "paper": "A2"},
                           {"conference": "b", "paper": "B1"}]
    assert r["paper_count"] == 3 and r["paper_count_by_conference"] == {"a": 2, "b": 1}
    assert r["original_nodes"]["Reasoning"]["papers"] == [("a", "A1"), ("a", "A2")]
    assert r["original_nodes"]["Reasoning skills"]["papers"] == [("b", "B1")]
    assert r["characterizations"] == {"a": "Reasoning in venue a"} and r["characterization"] == "Reasoning in venue a"
    assert r["canonical_definition"] == "the capacity to reason"
    assert len(r["source_snippets_evidence"]) == 2
    mmlu = out["measurements"][0]
    assert mmlu["original_names"] == ["MMLU", "Massive Multitask Language Understanding"]
    assert mmlu["paper_count_by_conference"] == {"a": 1, "b": 2}
    # relationships: pooled by (source, target, type); papers given as strings or records
    rels = {(r["source"], r["target"], r["type"]): r for r in out["relationships"]}
    m = rels[("Reasoning", "MMLU", "measured_by")]
    assert m["papers"] == [{"conference": "a", "paper": "A1"}, {"conference": "b", "paper": "B1"}]
    assert m["paper_count"] == 2 and m["evidence"] == ["ea", "eb"]
    assert m["papers_by_conference"] == {"a": ["A1"], "b": ["B1"]}
    assert ("Safety", "Reasoning", "related") in rels
    assert out["papers"] == [{"conference": "a", "paper": p} for p in ["A1", "A2"]] + \
                            [{"conference": "b", "paper": p} for p in ["B1", "B2", "B3"]]
    assert out["paper_count_by_conference"] == {"a": 2, "b": 3}
    assert "name_mapping" not in out


def test_build_joint_network_writes_file(tmp_path):
    a, b = tmp_path / "a.json", tmp_path / "b.json"
    json.dump(venue_a(), open(a, "w"))
    json.dump(venue_b(), open(b, "w"))
    out = build_joint_network({"a": a, "b": b}, tmp_path / "joint" / "union.json", postmerge=False)
    assert out == tmp_path / "joint" / "union.json"
    net = json.load(open(out))
    assert net["metadata"]["joint_of"] == ["a", "b"]
    assert [g["canonical_name"] for g in net["constructs"]] == ["Reasoning", "Reasoning ability", "Safety"]


def test_postmerge_collapses_surface_variants():
    out = join_networks([("a", venue_a()), ("b", venue_b())], postmerge=True)
    names = [g["canonical_name"] for g in out["constructs"]]
    # "Reasoning ability" normalizes to "reasoning": folded into Reasoning, which has more papers
    assert names == ["Reasoning", "Safety"]
    r = out["constructs"][0]
    assert r["paper_count"] == 5 and r["papers_by_conference"] == {"a": ["A1", "A2"], "b": ["B1", "B2", "B3"]}
    assert "Reasoning ability" in r["original_names"]
    assert out["name_mapping"]["Reasoning ability"] == "Reasoning"
    assert out["name_mapping"]["Safety"] == "Safety"
