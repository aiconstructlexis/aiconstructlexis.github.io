"""Tests for aiconstructlexis.vote.pair_types: one relationship type per unordered pair."""
import copy
import json

import pytest

from aiconstructlexis.vote.pair_types import (
    ConsolidationError, check_invariants, consolidate, consolidate_pair_types,
)


def rel(src, tgt, ty, papers, quotes=None, **kw):
    quotes = quotes or {p: f"q-{p}" for p in papers}
    r = {"source": src, "target": tgt, "type": ty,
         "papers": [{"conference": "c1", "paper": p, "type_share": 1.0} for p in papers],
         "papers_by_conference": {"c1": list(papers)},
         "paper_count": len(papers), "paper_count_by_conference": {"c1": len(papers)},
         "paper_weight": float(len(papers)), "n_papers_split": 0,
         "evidence": [quotes[p] for p in papers if quotes.get(p)],
         "evidence_by_paper": [{"conference": "c1", "paper": p, "quote": quotes[p]} for p in papers if quotes.get(p)]}
    r.update(kw)
    return r


def net():
    return {
        "constructs": [{"canonical_name": "Reasoning"}, {"canonical_name": "Safety"}],
        "measurements": [{"canonical_name": "MMLU"}],
        "behaviors": [],
        "relationships": [
            rel("Reasoning", "MMLU", "measured_by", ["P1"]),
            rel("MMLU", "Reasoning", "related", ["P2", "P3"]),
            rel("Reasoning", "Safety", "causes", ["P4"]),
            rel("Safety", "Reasoning", "causes", ["P5", "P6"]),
            rel("Reasoning", "Safety", "related", ["P7"], quotes={"P7": "q-P7"}),
            rel("MMLU", "Safety", "related", ["P8"]),
        ],
        "papers": [{"conference": "c1", "paper": f"P{i}"} for i in range(1, 9)],
    }


def by_label(n):
    return {(r["source"], r["type"], r["target"]): r for r in n["relationships"]}


def test_strictest_survivor_absorbs_other_types():
    out, report = consolidate(net(), "strictest")
    rels = by_label(out)
    assert ("MMLU", "related", "Reasoning") not in rels
    m = rels[("Reasoning", "measured_by", "MMLU")]
    assert [p["paper"] for p in m["papers"]] == ["P1", "P2", "P3"]
    assert [p["claim_type"] for p in m["papers"]] == ["measured_by", "related", "related"]
    assert all(p["type_share"] == 1.0 for p in m["papers"])
    assert m["paper_count"] == 3 and m["paper_weight"] == 3.0
    assert m["type_breakdown"] == {"measured_by": 1, "related": 2}
    assert m["consolidated_from"] == [["MMLU", "related", "Reasoning"]]
    assert m["evidence"] == ["q-P1", "q-P2", "q-P3"]
    assert m["papers_by_conference"] == {"c1": ["P1", "P2", "P3"]}
    # untouched single edge keeps its fields
    assert rels[("MMLU", "related", "Safety")] == net()["relationships"][5]
    assert report["pairs_affected"] == 2 and report["edges_merged"] == 2
    assert report["survivor_types"] == {"measured_by": 1, "causes (both directions)": 1}
    assert out["metadata"]["pair_type_consolidation"]["survivor"] == "strictest"
    assert not check_invariants(net(), out)[0]


def test_mutual_causes_keep_both_and_fold_related_into_heavier():
    out, _ = consolidate(net(), "strictest")
    rels = by_label(out)
    assert ("Reasoning", "related", "Safety") not in rels
    light = rels[("Reasoning", "causes", "Safety")]
    heavy = rels[("Safety", "causes", "Reasoning")]
    assert [p["paper"] for p in light["papers"]] == ["P4"]
    assert [p["paper"] for p in heavy["papers"]] == ["P5", "P6", "P7"]
    assert heavy["papers"][2]["claim_type"] == "related" and heavy["type_breakdown"] == {"causes": 2, "related": 1}
    assert heavy["evidence_by_paper"][2]["quote"] == "q-P7"


def test_mutual_causes_weight_tie_splits_folded_paper():
    n = net()
    n["relationships"][3] = rel("Safety", "Reasoning", "causes", ["P5"])  # now 1 vs 1
    out, _ = consolidate(n, "strictest")
    rels = by_label(out)
    for lab in (("Reasoning", "causes", "Safety"), ("Safety", "causes", "Reasoning")):
        p7 = next(p for p in rels[lab]["papers"] if p["paper"] == "P7")
        assert p7["type_share"] == 0.5 and rels[lab]["paper_weight"] == 1.5
    assert not check_invariants(n, out)[0]


def test_majority_survivor_is_the_heaviest_type():
    out, report = consolidate(net(), "majority")
    rels = by_label(out)
    assert ("Reasoning", "measured_by", "MMLU") not in rels
    r = rels[("MMLU", "related", "Reasoning")]
    assert [p["paper"] for p in r["papers"]] == ["P2", "P3", "P1"]
    assert r["type_breakdown"] == {"measured_by": 1, "related": 2}
    assert report["survivor_types"]["related"] == 1
    assert not check_invariants(net(), out)[0]


def test_rerun_is_a_no_op_and_input_not_modified():
    original = net()
    snapshot = copy.deepcopy(original)
    out, _ = consolidate(original, "strictest")
    assert original == snapshot
    again, report = consolidate(out, "strictest")
    assert report["edges_merged"] == 0 and again == out


def test_uncovered_shapes_raise():
    n = net()
    n["relationships"].append(rel("Reasoning", "Safety", "causes", ["P9"]))  # parallel same-direction causes
    with pytest.raises(ConsolidationError):
        consolidate(n, "strictest")


def test_check_invariants_flags_problems():
    bad = net()
    fails, stats = check_invariants(net(), bad)
    assert any("still carry >1 type" in f for f in fails)
    assert stats["pairs_with_multiple_types"] == 2


def test_consolidate_pair_types_writes_files(tmp_path):
    src = tmp_path / "net.json"
    json.dump(net(), open(src, "w"))
    out = consolidate_pair_types(src, out_json=tmp_path / "out.json", report_json=tmp_path / "rep.json")
    assert out == tmp_path / "out.json"
    written = json.load(open(out))
    assert len(written["relationships"]) == 4
    assert json.load(open(src)) == net()
    rep = json.load(open(tmp_path / "rep.json"))
    assert rep["invariants"]["failed"] == [] and rep["relationships_out"] == 4
    # in place, with the other survivor rule
    consolidate_pair_types(src, survivor="majority")
    assert ("MMLU", "related", "Reasoning") in by_label(json.load(open(src)))
    with pytest.raises(ValueError):
        consolidate_pair_types(src, survivor="loudest")
