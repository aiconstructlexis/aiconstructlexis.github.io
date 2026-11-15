"""Tests for aiconstructlexis.extract.batch: reasoning stripping, result
classification, JSONL splitting, Gemini result conversion, the strict poll
mode, request-body options, prompt fingerprints and the per-paper votes
(no API keys, no network, no PDFs)."""
import json
import logging
import types

import pytest

from aiconstructlexis.extract import batch as B
from aiconstructlexis.util.json_tools import split_jsonl_lines

logging.getLogger().setLevel(logging.WARNING)


def res(content, finish="stop", usage=None, error=None, status=200, msg_extra=None, cid="x"):
    msg = {"role": "assistant", "content": content}
    msg.update(msg_extra or {})
    body = {"choices": [{"message": msg, "finish_reason": finish}]}
    if usage:
        body["usage"] = usage
    return {"custom_id": cid, "response": {"status_code": status, "body": body}, "error": error}


# ---- strip_reasoning / parse_json_response -----------------------------------

def test_strip_reasoning_shapes():
    assert B.strip_reasoning('<think>a</think>{"x":1}')[0] == '{"x":1}'
    t, info = B.strip_reasoning('plan step 1\nplan step 2</think>\n\n{"x":1}')
    assert t == '{"x":1}' and info["think_orphan_close"]
    t, info = B.strip_reasoning("<think>still thinking when the cap hit")
    assert t == "" and info["think_unclosed"]
    # A literal tag inside JSON text is left alone
    assert B.strip_reasoning('{"e": "a </think> b"}')[0] == '{"e": "a </think> b"}'
    assert B.strip_reasoning(None)[0] == ""
    assert B.strip_reasoning("plain")[0] == "plain"


def test_parse_json_response_shapes():
    assert B.parse_json_response('{"a": 1}') == {"a": 1}
    assert B.parse_json_response('<think>x</think>{"a":1}') == {"a": 1}
    assert B.parse_json_response('```json\n{"a": 1}\n```') == {"a": 1}
    assert B.parse_json_response("garbage") == {"error": "Parse failed"}
    assert B.parse_json_response("") == {"error": "Parse failed"}
    assert B.parse_json_response('thinking...</think>{"a":1}') == {"a": 1}
    # Single-quoted keys are repaired
    assert B.parse_json_response("{'a': 1}") == {"a": 1}


# ---- classify_result ---------------------------------------------------------

ENT_OK = json.dumps({"constructs": [{"name": "Reasoning"}], "measurements": [], "behaviors": []})


def test_classify_statuses_and_flags():
    c = B.classify_result(res(ENT_OK, usage={"prompt_tokens": 10, "completion_tokens": 5}), "entities")
    assert c["status"] == "ok" and c["usage"] == {"input": 10, "output": 5, "reasoning": 0}
    c = B.classify_result(res('{"constructs": [{"name": "Rea', finish="length"), "entities")
    assert c["status"] == "parse_failed" and c["truncated"]
    c = B.classify_result(res("", finish="length"), "entities")
    assert c["status"] == "empty" and c["truncated"]
    c = B.classify_result(res("<think>never ends", finish="length"), "entities")
    assert c["status"] == "empty" and c["think_stripped"] and c["truncated"]
    c = B.classify_result(res("<think>hm</think>" + ENT_OK), "entities")
    assert c["status"] == "ok" and c["think_stripped"]
    c = B.classify_result(res("Sure, here it is: " + ENT_OK), "entities")
    assert c["leading_text"] and c["status"] == "parse_failed"
    c = B.classify_result(res('{"foo": 1}'), "entities")
    assert c["status"] == "wrong_schema"
    c = B.classify_result(res('{"relationships": {}}'), "relationships")
    assert c["status"] == "wrong_schema"
    c = B.classify_result(res('{"relationships": []}'), "relationships")
    assert c["status"] == "ok"
    c = B.classify_result(res(ENT_OK, msg_extra={"reasoning": "chain"}), "entities")
    assert c["reasoning_field"]
    assert B.classify_result(res(B._FAILED_SENTINEL), "entities")["status"] == "request_error"
    assert B.classify_result(res(ENT_OK, error={"code": "x"}), "entities")["status"] == "request_error"
    assert B.classify_result(res(ENT_OK, status=500), "entities")["status"] == "request_error"
    assert B.classify_result({"custom_id": "x", "response": None, "error": {"m": 1}})["status"] == "request_error"
    # OpenAI reasoning-token details
    u = B.result_usage(res(ENT_OK, usage={"prompt_tokens": 3, "completion_tokens": 9,
                                          "completion_tokens_details": {"reasoning_tokens": 4}}))
    assert u == {"input": 3, "output": 9, "reasoning": 4}


# ---- split_jsonl_lines -------------------------------------------------------

def test_split_into_parts_preserving_order():
    lines = [json.dumps({"i": i, "pad": "x" * 50}) for i in range(10)]
    size = len(lines[0].encode()) + 1
    parts = split_jsonl_lines(lines, max_bytes=size * 3, max_requests=None)
    assert [len(p) for p in parts] == [3, 3, 3, 1]
    assert [ln for p in parts for ln in p] == lines
    parts = split_jsonl_lines(lines, max_bytes=10**9, max_requests=4)
    assert [len(p) for p in parts] == [4, 4, 2]
    assert split_jsonl_lines([], 100, 10) == []
    with pytest.raises(ValueError):
        split_jsonl_lines(["y" * 200], max_bytes=100)


# ---- Gemini conversion -------------------------------------------------------

def test_gemini_file_line_conversion():
    line = {"key": "k1", "response": {
        "candidates": [{"content": {"parts": [{"text": "think", "thought": True},
                                              {"text": '{"a": '}, {"text": "1}"}]},
                        "finishReason": "MAX_TOKENS"}],
        "usageMetadata": {"promptTokenCount": 100, "candidatesTokenCount": 20, "thoughtsTokenCount": 30}}}
    r = B.gemini_file_line_to_result(line)
    assert r["custom_id"] == "k1"
    assert B.result_content(r) == '{"a": 1}'
    assert B.result_finish_reason(r) == "length"
    assert B.result_usage(r) == {"input": 100, "output": 50, "reasoning": 30}
    err = B.gemini_file_line_to_result({"key": "k2", "error": {"code": 3}})
    assert B.result_content(err) == B._FAILED_SENTINEL
    plain = B.gemini_file_line_to_result({"key": "k3", "response": {
        "candidates": [{"content": {"parts": [{"text": "x"}]}, "finishReason": "STOP"}]}})
    assert B.result_content(plain) == "x" and B.result_finish_reason(plain) == "stop"


# ---- poll_batch strict mode --------------------------------------------------

class _Status:
    def __init__(self, status, output_file_id=None, error_file_id=None):
        self.status = status
        self.output_file_id = output_file_id
        self.error_file_id = error_file_id
        self.request_counts = None


class FakeClient:
    def __init__(self, status, files):
        self._status = status
        self._files = files
        self.batches = types.SimpleNamespace(retrieve=lambda job_id: self._status)
        self.files = types.SimpleNamespace(content=lambda fid: self._files[fid].encode())


def test_poll_batch_default_contract_and_strict_mode():
    failed = FakeClient(_Status("failed"), {})
    assert B.poll_batch(failed, "job1", poll_interval=0) == []
    with pytest.raises(B.BatchJobFailed, match="job1"):
        B.poll_batch(failed, "job1", poll_interval=0, raise_on_failure=True)
    no_out = FakeClient(_Status("completed", None, "errf"),
                        {"errf": json.dumps({"custom_id": "a", "error": {"m": 1}})})
    assert B.poll_batch(no_out, "job2", poll_interval=0) == []
    with pytest.raises(B.BatchJobFailed):
        B.poll_batch(no_out, "job2", poll_interval=0, raise_on_failure=True)
    ok = FakeClient(_Status("COMPLETED", "outf", "errf"),
                    {"outf": json.dumps(res("{}", cid="a")) + "\n",
                     "errf": json.dumps({"custom_id": "b", "error": {"m": 1}})})
    assert [r["custom_id"] for r in B.poll_batch(ok, "job3", poll_interval=0)] == ["a"]
    both = B.poll_batch(ok, "job3", poll_interval=0, raise_on_failure=True, include_errors=True)
    assert [r["custom_id"] for r in both] == ["a", "b"]


# ---- request body options ----------------------------------------------------

def test_request_body_options():
    papers, texts = [{"name": "A"}], {"A": "text"}
    body = json.loads(B.build_entity_jsonl(papers, texts, "gpt-5.4-mini", 0, 1)[0])["body"]
    assert body["max_completion_tokens"] == 16384 and body["temperature"] == 0
    assert body["messages"][0]["content"] == B.ENTITY_SYSTEM_MESSAGE
    body = json.loads(B.build_entity_jsonl(papers, texts, "org/some-model", 0.6, 1,
                                           max_tokens=32768, send_temperature=False,
                                           extra_body={"reasoning_effort": "low"})[0])["body"]
    assert body["max_tokens"] == 32768 and "temperature" not in body
    assert body["reasoning_effort"] == "low"
    body = json.loads(B.build_entity_jsonl(papers, texts, "o3", 0.2, 1, send_temperature=True)[0])["body"]
    assert body["temperature"] == 0.2
    with pytest.raises(ValueError):
        B.build_entity_jsonl(papers, texts, "m", 0, 1, extra_body={"messages": []})
    # Papers without text or without entities get no request
    assert B.build_entity_jsonl([{"name": "E"}], {"E": "  "}, "m", 0, 2) == []
    voted = {"A": {"constructs": [{"name": "Reasoning"}], "measurements": ["GSM8K"], "behaviors": []}}
    lines = B.build_relationship_jsonl(papers + [{"name": "N"}], {"A": "text", "N": "text"}, voted, "m", 0, 2)
    assert len(lines) == 2
    user = json.loads(lines[0])["body"]["messages"][1]["content"]
    assert '"GSM8K"' in user and "Reasoning" in user and user.endswith("text")
    assert json.loads(json.loads(lines[1])["custom_id"]) == {"paper": "A", "trial": 1, "phase": "relationships"}


def test_prompt_fingerprints_describe_the_default_set():
    info = B.describe_extraction_prompts()
    assert info["prompt_set"] == "default" and info["module"] == "aiconstructlexis.prompts.default"
    assert info["entities"]["prompt_name"] == "EXTRACT_ENTITIES_PROMPT"
    assert len(info["entities"]["prompt_sha256"]) == 16 and len(info["relationships"]["system_sha256"]) == 16
    assert B.describe_extraction_prompts("default") == info


# ---- per-paper votes ---------------------------------------------------------

def test_majority_vote_entities_and_relationships():
    trials = {"P": [
        {"constructs": [{"name": "Reasoning"}, {"name": "Only once"}], "measurements": [], "behaviors": []},
        {"Nomological Network": {"constructs": [{"name": "reasoning", "definition": "longer record"}],
                                 "measurements": [], "behaviors": []}},
        {"constructs": ["LLM reasoning"], "measurements": [], "behaviors": []},
    ]}
    voted = B.majority_vote_entities(trials, 3, {})
    assert [c["name"] for c in voted["P"]["constructs"]] == ["reasoning"]  # longest record of the kept name
    voted = B.majority_vote_entities(trials, 3, {"llm reasoning": "reasoning"}, threshold=3)
    assert len(voted["P"]["constructs"]) == 1
    assert len(B.majority_vote_entities(trials, 3, {}, threshold=1)["P"]["constructs"]) == 3
    rels = {"P": [
        [{"source": "Reasoning", "target": "GSM8K", "type": "measured_by", "evidence": "short"}],
        [{"source": "reasoning", "target": "gsm8k", "type": "Measured_By", "evidence": "a longer quote"}],
        [{"source": "X", "target": "Y", "type": "causes"}],
    ]}
    voted = B.majority_vote_relationships(rels, 3, {})
    assert len(voted["P"]) == 1 and voted["P"][0]["evidence"] == "a longer quote"
    assert len(B.majority_vote_relationships(rels, 3, {}, threshold=1)["P"]) == 2


def test_load_papers_keeps_flagged_papers_once(tmp_path):
    papers = [{"name": "A", "path": "a.pdf", "is_LLM_paper": True},
              {"name": "A", "path": "a.pdf", "is_LLM_paper": True},
              {"name": "B", "path": "b.pdf", "is_LLM_paper": False},
              {"name": "C", "path": "c.pdf", "is_LLM_paper": True},
              {"name": "D", "path": "d.pdf", "screen_error": "rate limit"},   # unjudged: no verdict yet
              {"name": "E", "path": "e.pdf", "screen_note": "missing_pdf"}]
    p = tmp_path / "papers.json"
    p.write_text(json.dumps(papers))
    assert [x["name"] for x in B.load_papers(p)] == ["A", "C"]


def test_make_client_rejects_unknown_provider():
    with pytest.raises(ValueError):
        B.make_client("azure")
