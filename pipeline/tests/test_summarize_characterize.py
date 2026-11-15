"""Tests for the summary stage without a network: request building, fallback summaries,
result parsing and attachment, job-id parsing."""
import importlib
import json

import pytest

from aiconstructlexis.prompts import load_prompts
S = importlib.import_module("aiconstructlexis.summarize.characterize")   # aiconstructlexis.summarize.characterize resolves to the re-exported function, so the module is loaded by name

P = load_prompts("default")


def entity(name, n_papers, definition="A definition.", removed=False, summary=""):
    e = {"canonical_name": name,
         "original_nodes": {name: {"definition": definition, "papers": [["iclr24", f"{name} paper {i}"] for i in range(n_papers)]}},
         "source_snippets_evidence": [{"original_name": name, "paper": f"{name} paper 0", "source_snippets": ["quote"]}],
         "papers": [{"conference": "iclr24", "paper": f"{name} paper {i}"} for i in range(n_papers)],
         "paper_count": n_papers, "characterization": summary}
    if removed:
        e["expert_removed"] = True
    return e


def network():
    return {"constructs": [entity("Reasoning", 4), entity("Rare", 1, definition="Rare def")],
            "measurements": [entity("GSM8K", 3), entity("Out of scope", 5, removed=True)],
            "behaviors": [entity("Done", 3, summary="already")],
            "relationships": [
                {"source": "Reasoning", "type": "measured_by", "target": "GSM8K", "evidence": ["ev"],
                 "papers": [{"conference": "iclr24", "paper": "Reasoning paper 0"}]},
                {"source": "Reasoning", "type": "measured_by", "target": "Out of scope", "evidence": ["out of scope ev"],
                 "papers": [{"conference": "iclr24", "paper": "Reasoning paper 1"}]}]}


def requests_by_name(lines):
    return {json.loads(json.loads(l)["custom_id"])["name"]: json.loads(l) for l in lines}


def test_build_requests_openai_shape_fallbacks_and_skips():
    net = network()
    lines = S.build_requests(net, min_papers=3, provider="openai", model="gpt-5.4", effort="high")
    reqs = requests_by_name(lines)
    assert set(reqs) == {"Reasoning", "GSM8K"}          # Rare: fallback; Out of scope: removed; Done: has a summary
    r = reqs["Reasoning"]
    assert r["url"] == "/v1/responses" and r["method"] == "POST"
    assert r["body"]["model"] == "gpt-5.4" and r["body"]["reasoning"] == {"effort": "high"}
    assert r["body"]["text"] == {"format": {"type": "json_object"}}
    assert r["body"]["input"][0] == {"role": "system", "content": S.SYSTEM_PROMPT}
    user = r["body"]["input"][1]["content"]
    assert "Return: {\"definition\"" in user and '"canonical_name": "Reasoning"' in user
    assert json.loads(r["custom_id"]) == {"etype": "constructs", "idx": 0, "name": "Reasoning"}
    assert net["constructs"][1]["characterization"] == "Rare def"
    assert net["behaviors"][0]["characterization"] == "already"


def test_build_requests_google_shape_and_regenerate():
    net = network()
    lines = S.build_requests(net, min_papers=3, provider="google", model="gemini-2.5-pro", skip_characterized=False)
    reqs = requests_by_name(lines)
    assert set(reqs) == {"Reasoning", "GSM8K", "Done"}
    body = reqs["Done"]["body"]
    assert body["temperature"] == 0 and body["max_tokens"] == S.GOOGLE_MAX_TOKENS
    assert [m["role"] for m in body["messages"]] == ["system", "user"]
    assert "Return: {\"definition\", " not in body["messages"][1]["content"]
    assert '"evidence_of"' in body["messages"][1]["content"]       # behavior guidance


def test_context_leaves_out_links_to_removed_entities_and_counts_the_rest():
    net = network()
    index = {e["canonical_name"]: (et, e) for et in S.ENTITY_TYPES for e in net[et]}
    ctx = S.build_entity_context(net["constructs"][0], "constructs", net["relationships"], index)
    assert [r["target"] for r in ctx["relationships"]] == ["GSM8K"]
    assert ctx["stats"]["linked_instruments_count"] == 1
    assert ctx["stats"]["most_linked_instruments"] == [{"name": "GSM8K", "relationship_types": ["measured_by"]}]
    assert ctx["stats"]["linked_constructs_count"] == 0 and ctx["definitions"][0]["definition"] == "A definition."


def responses_result(custom_id, text):
    return {"custom_id": custom_id,
            "response": {"body": {"object": "response", "output": [
                {"type": "reasoning"}, {"type": "message", "content": [{"type": "output_text", "text": text}]}]}}}


def chat_result(custom_id, text):
    return {"custom_id": custom_id, "response": {"body": {"choices": [{"message": {"content": text}}]}}}


def test_attach_results_composes_labeled_sections_in_order():
    net = network()
    cid = json.dumps({"etype": "constructs", "idx": 0, "name": "Reasoning"})
    answer = {"links": "Linked to GSM8K.", "definition": "Most papers frame it as an ability.", "measurement": "",
              "systematization": "Facets vary."}
    stats = S.attach_results(net, [responses_result(cid, json.dumps(answer))])
    assert stats == {"ok": 1, "parse_failed": 0, "missing_target": 0, "failed_request": 0}
    e = net["constructs"][0]
    assert e["characterization_sections"] == {"definition": "Most papers frame it as an ability.",
                                              "systematization": "Facets vary.", "links": "Linked to GSM8K."}
    labels = dict(P.CHARACTERIZE_SECTION_LABELS["constructs"])
    assert e["characterization"] == (f"{labels['definition']} Most papers frame it as an ability.\n\n"
                                     f"{labels['systematization']} Facets vary.\n\n{labels['links']} Linked to GSM8K.")


def test_attach_results_handles_fenced_single_key_failed_and_mismatched_results():
    net = network()
    cid = json.dumps({"etype": "measurements", "idx": 0, "name": "GSM8K"})
    fenced = "```json\n" + json.dumps({"GSM8K": "A benchmark of grade-school problems."}) + "\n```"
    wrong = json.dumps({"etype": "measurements", "idx": 1, "name": "GSM8K"})
    stats = S.attach_results(net, [chat_result(cid, fenced), chat_result(wrong, "{\"GSM8K\": \"x\"}"),
                                   chat_result(cid, S.FAILED_SENTINEL), chat_result(cid, "not json at all"),
                                   {"custom_id": "garbage", "response": {}}])
    assert stats == {"ok": 1, "parse_failed": 1, "missing_target": 2, "failed_request": 1}
    assert net["measurements"][0]["characterization"] == "A benchmark of grade-school problems."
    assert "characterization_sections" not in net["measurements"][0]


def test_parse_json_loose_strips_think_tags_and_repairs():
    assert S.parse_json_loose("<think>hm</think>{\"a\": 1}") == {"a": 1}
    assert S.parse_json_loose("{\"a\": 1,}") == {"a": 1}
    assert S.parse_json_loose("") is None


def test_job_ids_from_list_string_and_file(tmp_path):
    assert S.job_ids(["b1", "b2"]) == ["b1", "b2"]
    assert S.job_ids("b1, b2") == ["b1", "b2"]
    p = tmp_path / "x.batch_jobs.json"
    p.write_text(json.dumps(["b7"]))
    assert S.job_ids(p) == ["b7"]
    p.write_text(json.dumps("batches/123"))
    assert S.job_ids(str(p)) == ["batches/123"]


def test_characterize_rejects_unknown_provider(tmp_path):
    with pytest.raises(ValueError):
        S.characterize(tmp_path / "in.json", tmp_path / "out.json", provider="together")


def test_characterize_with_only_fallbacks_writes_output_without_a_client(tmp_path):
    net = network()
    net["constructs"] = [entity("Rare", 1, definition="Rare def")]
    net["measurements"], net["behaviors"], net["relationships"] = [], [], []
    src = tmp_path / "in.json"
    src.write_text(json.dumps(net))
    out = S.characterize(src, tmp_path / "out" / "characterized.json", min_papers=3)
    result = json.loads(out.read_text())
    assert result["constructs"][0]["characterization"] == "Rare def"
    assert (tmp_path / "out" / "characterized.batch_results.jsonl").read_text() == ""
    assert not (tmp_path / "out" / "characterized.batch_jobs.json").exists()


def test_build_requests_requests_an_entity_that_carries_only_its_fallback():
    net = network()
    net["behaviors"].append(entity("Grown", 3, definition="Grown def", summary="Grown def"))
    reqs = requests_by_name(S.build_requests(net, min_papers=3, provider="openai", model="gpt-5.4", effort="high"))
    assert "Grown" in reqs and "Done" not in reqs
