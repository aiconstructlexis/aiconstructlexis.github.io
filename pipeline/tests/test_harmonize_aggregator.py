"""Tests of aiconstructlexis.harmonize.aggregator without API calls: the LLM is faked.

Covered: id-based group decoding, failed-batch handling (no retries by default, retries
and the stop policy as options, failed steps not checkpointed), the seed name mapping (a plain
mapping or a release artifact, ambiguous entries skipped) and name_mapping_out, the empty
relationship list left for the deterministic aggregation,
cross-batch merge decoding, and the OpenAI Responses call used with a reasoning effort.
"""
import json
import re
from pathlib import Path

import pytest

import aiconstructlexis.harmonize.aggregator as agg


# ---------------------------------------------------------------- helpers

def rows_from_prompt(prompt: str) -> list:
    """The JSON rows embedded in a grouping or merge prompt."""
    m = re.search(r"\*\*Input (?:rows|groups):\*\*\n(.*?)\n\nReturn only", prompt, re.S)
    assert m, prompt[:200]
    return json.loads(m.group(1))


def group_by_first_word(rows):
    groups = {}
    for r in rows:
        name = r.get("name") or r.get("canonical_name") or ""
        groups.setdefault(name.split()[0].capitalize() if name else "X", []).append(r["id"])
    return {"groups": groups, "ungrouped": []}


def is_grouping_prompt(prompt: str) -> bool:
    return "Input rows" in prompt or "Input groups" in prompt


class FakeLLM:
    """Scripted responses per call; a callable entry is called with the prompt."""

    def __init__(self, script=None, default=group_by_first_word):
        self.script = list(script or [])
        self.default = default
        self.prompts = []

    def __call__(self, prompt, provider="x", model="y", **kw):
        self.prompts.append((prompt, kw))
        assert is_grouping_prompt(prompt), prompt[:200]
        if self.script:
            step = self.script.pop(0)
            if isinstance(step, Exception):
                raise step
            return step(prompt) if callable(step) else step
        return self.default(rows_from_prompt(prompt))


def batch(*names):
    return [{"name": n, "definition": n, "paper": f"P{i}"} for i, n in enumerate(names)]


def paper(constructs=(), measurements=(), relationships=()):
    return {"parsed_text": {"Nomological Network": {
        "constructs": [{"name": n, "description": n.lower()} for n in constructs],
        "measurements": [{"name": n, "description": n.lower()} for n in measurements],
        "behaviors": [],
        "relationships": list(relationships),
    }}}


METADATA_KEYS = {"total_papers", "error_count", "aggregation_method", "provider", "model", "statistics"}


@pytest.fixture(autouse=True)
def default_run_options():
    agg.configure_run()
    yield
    agg.configure_run()


@pytest.fixture
def install(monkeypatch):
    def _install(fake):
        monkeypatch.setattr(agg, "call_llm_for_aggregation", fake)
        return fake
    return _install


# ---------------------------------------------------------------- collected nodes

def test_construct_without_definition_gets_an_empty_one():
    data = {
        "paper 1": {"parsed_text": {"Nomological Network": {
            "constructs": [{"name": "Reasoning"}, {"name": "Safety", "description": "Avoiding harm."},
                           {"name": "Calibration", "definitions": ["Confidence tracks accuracy."]}],
            "measurements": [{"name": "GSM8K"}],
            "behaviors": [{"name": "Refusal"}],
            "relationships": []}}},
    }
    nodes, errors = agg.collect_all_nodes_with_definitions(data)
    assert errors == 0
    assert [(n["name"], n["definition"]) for n in nodes["constructs"]] == [
        ("Reasoning", ""), ("Safety", "Avoiding harm."), ("Calibration", "Confidence tracks accuracy.")]
    assert [(n["name"], n["definition"]) for n in nodes["measurements"]] == [("GSM8K", "")]
    assert [(n["name"], n["definition"]) for n in nodes["behaviors"]] == [("Refusal", "")]


def test_enriched_groups_record_the_paper_of_the_kept_definition():
    rows = [
        {"name": "Reasoning", "definition": "", "paper": "P0"},
        {"name": "Reasoning ability", "definition": "Drawing inferences.", "paper": "P1"},
        {"name": "Reasoning ability", "definition": "Multi-step inference.", "paper": "P2"},
        {"name": "Reasoning", "definition": "Inference.", "paper": "P3"},
    ]
    groups = [{"canonical_name": "Reasoning", "original_names": ["Reasoning", "Reasoning ability"]}]
    out = agg.enrich_groups_with_paper_info(groups, rows, "constructs")
    assert out[0]["original_nodes"] == {
        # the first definition encountered is kept; an empty one names no paper
        "Reasoning": {"definition": "", "definition_paper": "", "papers": ["P0", "P3"]},
        "Reasoning ability": {"definition": "Drawing inferences.", "definition_paper": "P1", "papers": ["P1", "P2"]},
    }
    assert out[0]["papers"] == ["P0", "P1", "P2", "P3"] and out[0]["paper_count"] == 4
    # the merges keep the field next to the definition
    a = {"canonical_name": "Reasoning", "original_names": ["Reasoning"], "papers": ["P3"], "paper_count": 1,
         "original_nodes": {"Reasoning": {"definition": "Inference.", "definition_paper": "P3", "papers": ["P3"]}}}
    b = {"canonical_name": "reasoning", "original_names": ["Reasoning"], "papers": ["P4"], "paper_count": 1,
         "original_nodes": {"Reasoning": {"definition": "Thinking.", "definition_paper": "P4", "papers": ["P4"]}}}
    merged = agg._exact_match_merge([a, b])
    assert len(merged) == 1
    assert merged[0]["original_nodes"] == {
        "Reasoning": {"definition": "Inference.", "definition_paper": "P3", "papers": ["P3", "P4"]}}
    rebuilt = agg._reconstruct_merged_group("Reasoning", [0, 1], [a, b])
    assert rebuilt["original_nodes"] == {
        "Reasoning": {"definition": "Inference.", "definition_paper": "P3", "papers": ["P3", "P4"]}}


# ---------------------------------------------------------------- decoding

def test_decoder_keeps_a_shared_id_in_both_groups():
    b = batch("Reasoning", "Reasoning ability", "Logic")
    out = agg._decode_id_groups({"groups": {"A": [0, 1], "B": [1, 2]}}, b, "constructs", 1)
    assert [g["original_names"] for g in out] == [["Reasoning", "Reasoning ability"], ["Reasoning ability", "Logic"]]


def test_decoder_unlisted_ids_become_singletons():
    b = batch("Reasoning", "Logic", "Memory")
    out = agg._decode_id_groups({"groups": {"A": [0]}, "ungrouped": [1]}, b, "constructs", 1)
    assert [(g["canonical_name"], g["original_names"]) for g in out] == [
        ("A", ["Reasoning"]), ("Logic", ["Logic"]), ("Memory", ["Memory"]),
    ]


def test_decoder_rejects_non_id_format():
    b = batch("Reasoning")
    assert agg._decode_id_groups({"groups": [{"canonical_name": "A"}]}, b, "constructs", 1) is None
    assert agg._decode_id_groups("text", b, "constructs", 1) is None


def test_merge_decoding_keeps_every_listed_assignment(install):
    groups = [{"canonical_name": n, "original_names": [n], "papers": [f"P{i}"], "original_nodes": {}}
              for i, n in enumerate(["A", "B", "C"])]
    install(FakeLLM([{"groups": {"X": [0, 1], "Y": [1, 2]}, "ungrouped": [0]}]))
    out = agg._merge_groups_batch(groups, "constructs", "p", "m")
    assert len(out) == 3  # X, Y and the ungrouped copy of A
    assert sorted(g["canonical_name"] for g in out) == ["A", "X", "Y"]


# ---------------------------------------------------------------- failed batches

def test_failed_batch_is_logged_not_retried_and_not_checkpointed(install, tmp_path):
    calls = {"n": 0}

    def fake(prompt, provider="x", model="y", **kw):
        if "Input rows" in prompt and '"name": "Reasoning"' in prompt:
            calls["n"] += 1
            raise RuntimeError("api down")      # the constructs batch fails
        return group_by_first_word(rows_from_prompt(prompt))
    install(fake)

    data = {f"P{i}": paper(constructs=["Reasoning"], measurements=["GSM8K"]) for i in range(2)}
    (tmp_path / "in.json").write_text(json.dumps(data))
    out = tmp_path / "out.json"
    res = agg.aggregate_network_llm(tmp_path / "in.json", out, provider="x", model="y", batch_size=100)
    assert calls["n"] == 1  # no retry by default
    assert res["constructs"] == []  # the failed batch's names are missing from the output
    assert [g["canonical_name"] for g in res["measurements"]] == ["Gsm8k"]
    failed = json.loads((tmp_path / "out.failed_batches.json").read_text())
    assert failed[0]["node_type"] == "constructs" and failed[0]["names"] == ["Reasoning"]
    assert set(res["metadata"]) == METADATA_KEYS
    assert json.loads(out.read_text())["metadata"] == res["metadata"]


def test_failed_step_not_in_checkpoint(install, monkeypatch, tmp_path):
    saved = []
    monkeypatch.setattr(agg, "_save_checkpoint",
                        lambda path, data: saved.append(list(data.get("completed_steps", []))))

    def fake(prompt, provider="x", model="y", **kw):
        if "Input rows" in prompt and '"name": "Reasoning"' in prompt:
            raise RuntimeError("api down")
        return group_by_first_word(rows_from_prompt(prompt))
    install(fake)

    data = {"P0": paper(constructs=["Reasoning"], measurements=["GSM8K"],
                        relationships=[{"source": "Reasoning", "target": "GSM8K", "type": "measured_by"}])}
    (tmp_path / "in.json").write_text(json.dumps(data))
    agg.aggregate_network_llm(tmp_path / "in.json", tmp_path / "out.json", provider="x", model="y")
    assert all("constructs" not in steps for steps in saved), saved
    assert any("measurements" in steps for steps in saved)


def test_failed_batch_retried_then_stops(install):
    agg.configure_run(batch_retries=2, on_batch_failure="stop")
    fake = install(FakeLLM([RuntimeError("api down")] * 10))
    with pytest.raises(agg.BatchFailureError):
        agg.group_nodes_llm(batch("Reasoning", "Logic"), "constructs", batch_size=100)
    assert len(fake.prompts) == 3  # 1 + 2 retries
    assert agg._RUN["failed_batches"][0]["names"] == ["Logic", "Reasoning"]


def test_failed_batch_recovers_on_retry(install):
    agg.configure_run(batch_retries=2)
    install(FakeLLM([RuntimeError("api down")]))
    out = agg.group_nodes_llm(batch("Reasoning", "Logic"), "constructs", batch_size=100)
    names = sorted(n for g in out["groups"] for n in g["original_names"])
    assert names == ["Logic", "Reasoning"] and not agg._RUN["failed_batches"]


def test_warn_policy_goes_on_after_retries(install):
    agg.configure_run(batch_retries=1, on_batch_failure="warn")
    fake = install(FakeLLM([RuntimeError("api down")] * 10))
    out = agg.group_nodes_llm(batch("Reasoning", "Logic"), "constructs", batch_size=100)
    assert out == {"groups": []}
    assert len(fake.prompts) == 2
    assert agg._RUN["failed_batches"][0]["attempts"] == 2


def test_configure_run_rejects_unknown_failure_policy():
    with pytest.raises(ValueError):
        agg.configure_run(on_batch_failure="ignore")


# ---------------------------------------------------------------- name mapping and relationships

def test_seed_rewritten_unless_mapping_out_given(install, tmp_path):
    install(FakeLLM())
    data = {"P0": paper(constructs=["Reasoning"])}
    (tmp_path / "in.json").write_text(json.dumps(data))
    seed = tmp_path / "seed.json"
    seed.write_text(json.dumps({"Old": "Old"}))
    agg.aggregate_network_llm(tmp_path / "in.json", tmp_path / "out.json", provider="x", model="y",
                              name_mapping_path=seed)
    assert "Reasoning" in json.loads(seed.read_text())  # updated in place by default
    seed.write_text(json.dumps({"Old": "Old"}))
    agg.aggregate_network_llm(tmp_path / "in.json", tmp_path / "out.json", provider="x", model="y",
                              name_mapping_path=seed, name_mapping_out=tmp_path / "new_map.json")
    assert json.loads(seed.read_text()) == {"Old": "Old"}
    assert "Reasoning" in json.loads((tmp_path / "new_map.json").read_text())


def test_seed_plain_mapping_skips_ambiguous_entries(tmp_path):
    seed = tmp_path / "seed.json"
    seed.write_text(json.dumps({"Reasoning": "Reasoning", "reasoning skill": "Reasoning",
                                "memory": ["Episodic memory", "Temporal grounding"]}))
    assert agg._load_name_mapping(seed) == ({"Reasoning": "Reasoning", "reasoning skill": "Reasoning"}, False)
    assert agg._load_name_mapping(tmp_path / "missing.json") == ({}, False)
    assert agg._load_name_mapping(None) == ({}, False)
    seed.write_text(json.dumps([["Reasoning", "Reasoning"]]))
    with pytest.raises(ValueError, match="JSON object"):
        agg._load_name_mapping(seed)


def test_seed_release_artifact_uses_its_name_mapping_and_is_never_rewritten(install, tmp_path):
    artifact = {"metadata": {"name": "AI Construct Lexis", "version": "0.0.1"},
                "constructs": [{"canonical_name": "Reasoning", "original_names": ["Reasoning", "reasoning skill"]}],
                "measurements": [], "behaviors": [], "relationships": [], "papers": [],
                "name_mapping": {"Reasoning": "Reasoning", "reasoning skill": "Reasoning",
                                 "memory": ["Episodic memory", "Temporal grounding"]}}
    seed = tmp_path / "ai_construct_lexis_v0.0.1.json"
    seed.write_text(json.dumps(artifact))
    before = seed.read_bytes()
    assert agg._load_name_mapping(seed) == ({"Reasoning": "Reasoning", "reasoning skill": "Reasoning"}, True)

    fake = install(FakeLLM())
    (tmp_path / "in.json").write_text(json.dumps({"P0": paper(constructs=["reasoning skill", "memory"])}))
    res = agg.aggregate_network_llm(tmp_path / "in.json", tmp_path / "out.json", provider="x", model="y",
                                    name_mapping_path=seed)
    assert seed.read_bytes() == before                      # no name_mapping_out: the artifact stays as it is
    rows = rows_from_prompt(fake.prompts[0][0])
    prior = {r["name"]: r.get("_prior_canonical") for r in rows}
    assert prior == {"reasoning skill": "Reasoning", "memory": None}   # the ambiguous entry is not a seed
    assert res["name_mapping"]["Reasoning"] == "Reasoning"
    assert all(isinstance(v, str) for v in res["name_mapping"].values())
    # with name_mapping_out the updated mapping is written there; the artifact itself is refused
    agg.aggregate_network_llm(tmp_path / "in.json", tmp_path / "out.json", provider="x", model="y",
                              name_mapping_path=seed, name_mapping_out=tmp_path / "map.json")
    assert json.loads((tmp_path / "map.json").read_text())["reasoning skill"] == "Reasoning"
    assert seed.read_bytes() == before
    with pytest.raises(ValueError, match="seed network itself"):
        agg.aggregate_network_llm(tmp_path / "in.json", tmp_path / "out.json", provider="x", model="y",
                                  name_mapping_path=seed, name_mapping_out=seed)
    assert seed.read_bytes() == before


def test_harmonize_leaves_relationships_to_the_deterministic_stage(install, tmp_path):
    fake = install(FakeLLM())
    data = {f"P{i}": paper(constructs=["Reasoning", "Reasoning ability"], measurements=["GSM8K"],
                           relationships=[{"source": "Reasoning", "target": "GSM8K", "type": "measured_by"}])
            for i in range(2)}
    (tmp_path / "in.json").write_text(json.dumps(data))
    seed = tmp_path / "seed.json"
    seed.write_text(json.dumps({"Reasoning": "Reasoning"}))
    out = agg.harmonize(tmp_path / "in.json", tmp_path / "out.json", provider="x", model="y",
                        name_mapping=seed, name_mapping_out=tmp_path / "map.json")
    assert out == Path(tmp_path / "out.json") and out.exists()
    res = json.loads(out.read_text())
    assert res["relationships"] == []
    assert res["metadata"]["statistics"]["total_relationships"] == 0
    assert all(is_grouping_prompt(p) for p, _ in fake.prompts), "only grouping prompts are sent"
    written = json.loads((tmp_path / "map.json").read_text())
    assert written["GSM8K"] == "Gsm8k" and written["Reasoning ability"] == "Reasoning"
    assert res["name_mapping"] == written
    assert json.loads(seed.read_text()) == {"Reasoning": "Reasoning"}
    assert set(res["metadata"]) == METADATA_KEYS
    assert set(res) == {"metadata", "constructs", "measurements", "behaviors", "relationships",
                        "name_mapping", "papers"}
    assert not (tmp_path / ".out_checkpoint.json").exists()


# ---------------------------------------------------------------- OpenAI reasoning call

def test_openai_reasoning_uses_responses_api_without_temperature(monkeypatch):
    seen = {}

    class Resp:
        status = "completed"
        output_text = '{"groups": {"A": [0]}}'

    class Client:
        class responses:
            @staticmethod
            def create(**kw):
                seen.update(kw)
                return Resp()

    monkeypatch.setattr(agg, "init_openai_client", lambda: Client())
    out = agg.call_llm_for_aggregation("prompt", "openai", "gpt-5.4", reasoning_effort="medium",
                                       max_output_tokens=5000)
    assert out == {"groups": {"A": [0]}}
    assert seen["model"] == "gpt-5.4" and seen["reasoning"] == {"effort": "medium"}
    assert seen["max_output_tokens"] == 5000 and "temperature" not in seen
    assert seen["text"] == {"format": {"type": "json_object"}}
    Resp.status = "incomplete"
    with pytest.raises(RuntimeError, match="incomplete"):
        agg.call_llm_for_aggregation("prompt", "openai", "gpt-5.4", reasoning_effort="high", max_retries=1)


def test_llm_kwargs_follow_run_options():
    assert agg._llm_kwargs() == {}
    agg.configure_run(reasoning_effort="low", max_output_tokens=10)
    assert agg._llm_kwargs() == {"reasoning_effort": "low", "max_output_tokens": 10}
