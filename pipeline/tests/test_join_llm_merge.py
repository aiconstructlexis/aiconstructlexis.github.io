"""Tests for aiconstructlexis.join.llm_merge: response decoding, cross-batch candidate
pairs, the blocked cross-batch pass and the end-to-end merge. The LLM call and the
thematic batching (which live in the harmonize package) are replaced by fakes, so no API
is called."""
import json
import re

import pytest

from aiconstructlexis.join import llm_merge as jm


def g(name, papers=1):
    return {"canonical_name": name, "original_names": [name],
            "papers_by_conference": {"c": [f"{name}-{i}" for i in range(papers)]}, "paper_count": papers}


def rows(prompt):
    m = re.search(r"\*\*Input groups:\*\*\n(.*?)\n\nReturn only", prompt, re.S)
    assert m, "the merge prompt should carry the input groups"
    return json.loads(m.group(1))


def chunk_batches(names, batch_size):
    """Deterministic stand-in for the thematic batching: consecutive chunks."""
    return [list(range(i, min(i + batch_size, len(names)))) for i in range(0, len(names), batch_size)]


@pytest.fixture
def fake_batches(monkeypatch):
    monkeypatch.setattr(jm, "make_batches", chunk_batches)


def identity_llm(calls):
    def fake(prompt, provider, model, **kw):
        calls.append((prompt, kw))
        return {"groups": {r["canonical_name"]: [r["id"]] for r in rows(prompt)}, "ungrouped": []}
    return fake


def test_candidate_pairs_rules_and_cross_batch_filter():
    names = ["BIG-Bench Hard", "BBH", "BigBench Hard", "Mathematical reasoning", "Math reasoning", "GSM8K"]
    pairs = jm.candidate_pairs(names, "measurements")
    got = {(names[e["a"]], names[e["b"]]): set(e["reasons"]) for e in pairs}
    assert "acronym" in got[("BIG-Bench Hard", "BBH")]
    assert "same_normalized_key" in got[("BIG-Bench Hard", "BigBench Hard")]
    assert not any("GSM8K" in k for k in got)
    # with first-pass batches, pairs that already shared a batch are left out
    batches = [{0}, {0}, {1}, {2}, {3}, {4}]
    got2 = {(names[e["a"]], names[e["b"]]) for e in jm.candidate_pairs(names, "measurements", batches)}
    assert ("BIG-Bench Hard", "BBH") not in got2 and ("BIG-Bench Hard", "BigBench Hard") in got2
    c = {(names[e["a"]], names[e["b"]]) for e in jm.candidate_pairs(names, "constructs")}
    assert ("Mathematical reasoning", "Math reasoning") in c


def test_blocking_keys():
    assert jm._concept_key("Mathematical reasoning capability") == "math reasoning ability"
    assert jm._concept_key("Reading comprehension") == "reading understanding"
    assert jm._concept_key("Natural language understanding (NLU)") == "natural language understanding"
    assert jm._concept_key("Answer refusal") == jm._concept_key("Refusal answer")  # two-word names are sorted
    assert jm._instrument_key("The SQuAD v2.0 benchmark") == "squad2"
    assert jm._instrument_key("BIG-Bench Hard (BBH)") == "bigbenchhard"
    assert jm._blocking_key("GSM8K", "measurements") == "gsm8k"
    assert jm._blocking_key("Safety", "constructs") == "safety"


def test_decode_id_groups():
    groups = [g("A"), g("B"), g("C")]
    assert jm._decode_id_groups({"groups": {"X": [0, 1], "Y": [1]}}, groups) == {0: "X", 1: "X", 2: "C"}
    assert jm._decode_id_groups({"groups": {"X": [0]}, "ungrouped": [2]}, groups) == {0: "X", 1: "B", 2: "C"}
    assert jm._decode_id_groups("garbage", groups) == {}
    assert jm._decode_id_groups({"groups": "not a dict"}, groups) == {}


def test_parse_handles_fenced_json_and_dicts():
    assert jm._parse({"groups": {}}) == {"groups": {}}
    assert jm._parse('```json\n{"groups": {"A": [0]}}\n```') == {"groups": {"A": [0]}}
    assert jm._parse('{"groups": {"A": [0]}, }') == {"groups": {"A": [0]}}  # repaired


def test_apply_id_to_canon_merges_metadata():
    groups = [g("A", 2), g("B", 1)]
    groups[0]["canonical_definition"] = "def A"
    merged = jm._apply_id_to_canon(groups, {0: "A", 1: "A"})
    assert len(merged) == 1
    m = merged[0]
    assert m["canonical_name"] == "A" and m["paper_count"] == 3
    assert m["original_names"] == ["A", "B"]
    assert m["paper_count_by_conference"] == {"c": 3}
    assert m["papers"] == [{"conference": "c", "paper": p} for p in ["A-0", "A-1", "B-0"]]


def test_blocked_pass_merges_cross_batch_duplicate(monkeypatch, fake_batches):
    seen = []

    def fake(prompt, provider, model, **kw):
        seen.append((prompt, kw))
        rs = rows(prompt)
        present = {r["canonical_name"] for r in rs}
        both = {"BIG-Bench Hard", "BBH"} <= present  # merges only when it sees both
        by = {}
        for r in rs:
            name = "BIG-Bench Hard" if both and r["canonical_name"] in ("BIG-Bench Hard", "BBH") else r["canonical_name"]
            by.setdefault(name, []).append(r["id"])
        return {"groups": by, "ungrouped": []}

    monkeypatch.setattr(jm, "call_llm_for_aggregation", fake)
    # batch size 2 puts the duplicates in different first-pass batches
    groups = [g("BIG-Bench Hard", 3), g("Zebra QA"), g("Apple QA"), g("BBH", 2)]
    out = jm.merge_one_type(groups, "measurements", "openai", "gpt-5.4", 2, cross_batch="blocked",
                            llm_kwargs=jm.llm_options(reasoning_effort="medium"))
    assert all(kw == {"reasoning_effort": "medium"} for _, kw in seen)
    assert all(p.startswith("You are merging groups of measurements") for p, _ in seen)
    names = sorted(x["canonical_name"] for x in out)
    assert names == ["Apple QA", "BIG-Bench Hard", "Zebra QA"], names
    merged = next(x for x in out if x["canonical_name"] == "BIG-Bench Hard")
    assert merged["paper_count"] == 5 and "BBH" in merged["original_names"]
    # without a cross-batch pass the two stay apart
    off = jm.merge_one_type(groups, "measurements", "openai", "gpt-5.4", 2, cross_batch="off")
    assert len(off) == 4


def test_report_mode_makes_no_extra_call_and_auto_global_pass(monkeypatch, fake_batches):
    calls = []
    monkeypatch.setattr(jm, "call_llm_for_aggregation", identity_llm(calls))
    groups = [g("BIG-Bench Hard"), g("Zebra QA"), g("Apple QA"), g("BBH")]
    jm.merge_one_type(groups, "measurements", "x", "y", 2, cross_batch="report")
    assert len(calls) == 2  # two first-pass batches, no cross-batch call
    calls.clear()
    jm.merge_one_type(groups, "measurements", "x", "y", 2)  # auto: 4 groups > 2, no global pass
    assert len(calls) == 2
    calls.clear()
    jm.merge_one_type(groups, "measurements", "x", "y", 4)  # auto: global pass runs
    assert len(calls) == 2


def test_failed_batch_keeps_its_groups(monkeypatch, fake_batches):
    monkeypatch.setattr(jm.time, "sleep", lambda s: None)

    def failing(prompt, provider, model, **kw):
        raise RuntimeError("provider down")

    monkeypatch.setattr(jm, "call_llm_for_aggregation", failing)
    groups = [g("A"), g("B"), g("C")]
    out = jm.merge_one_type(groups, "constructs", "x", "y", 2, cross_batch="off")
    assert sorted(x["canonical_name"] for x in out) == ["A", "B", "C"]


def test_merge_joint_network_end_to_end(tmp_path, monkeypatch, fake_batches):
    calls = []

    def fake(prompt, provider, model, **kw):
        calls.append(kw)
        rs = rows(prompt)
        by = {}
        for r in rs:
            name = "Reasoning" if r["canonical_name"] in ("Reasoning", "Reasoning ability") else r["canonical_name"]
            by.setdefault(name, []).append(r["id"])
        return {"groups": by, "ungrouped": []}

    monkeypatch.setattr(jm, "call_llm_for_aggregation", fake)
    net = {
        "metadata": {"joint_of": ["a", "b"]},
        "constructs": [g("Reasoning", 2), g("Reasoning ability", 1), g("Safety", 1)],
        "measurements": [g("MMLU", 1)],
        "behaviors": [],
        "relationships": [{"source": "Reasoning", "target": "MMLU", "type": "measured_by", "papers": []}],
        "papers": [],
    }
    src = tmp_path / "union.json"
    json.dump(net, open(src, "w"))
    out = tmp_path / "merged.json"
    written = jm.merge_joint_network(src, out, "google", "gemini-2.5-pro", batch_size=500,
                                     reasoning_effort="high")
    assert written == out
    merged = json.load(open(out))
    assert sorted(c["canonical_name"] for c in merged["constructs"]) == ["Reasoning", "Safety"]
    r = next(c for c in merged["constructs"] if c["canonical_name"] == "Reasoning")
    assert r["paper_count"] == 3 and "Reasoning ability" in r["original_names"]
    assert merged["relationships"] == net["relationships"] and merged["metadata"] == net["metadata"]
    assert all(kw == {"reasoning_effort": "high"} for kw in calls)
    assert sorted(p.name for p in tmp_path.iterdir()) == ["merged.json", "union.json"]
    with pytest.raises(ValueError):
        jm.merge_joint_network(src, out, "google", "gemini-2.5-pro", cross_batch_pass="sometimes")
