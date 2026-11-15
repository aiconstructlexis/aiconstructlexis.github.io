"""Tests for aiconstructlexis.extract.multi_model with a fake batch backend: no
API keys, no network, no PDFs. Covers the panel argument and model specs,
fail-loud vs allow_partial, the per-paper cache top-up, the cache-consistency
rule, lower-cased name matching in the votes, run-report counting, dry runs,
the worker count and the CLI."""
import json
import logging
import sys
import types
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from pathlib import Path

import pytest

from aiconstructlexis.extract import multi_model as M
from aiconstructlexis.extract.batch import BatchJobFailed
from aiconstructlexis.prompts import REQUIRED_NAMES, load_prompts
from aiconstructlexis.screen import _common as C

logging.getLogger().setLevel(logging.CRITICAL)


# ---- fake backend ------------------------------------------------------------

def ok(cid, content, finish="stop", usage=(1000, 200)):
    return {"custom_id": cid, "response": {"status_code": 200, "body": {
        "choices": [{"message": {"role": "assistant", "content": content}, "finish_reason": finish}],
        "usage": {"prompt_tokens": usage[0], "completion_tokens": usage[1]}}}, "error": None}


def default_responder(model, req):
    cid = req["custom_id"]
    meta = json.loads(cid)
    paper = meta["paper"]
    if meta["phase"] == "entities":
        return ok(cid, json.dumps({
            "constructs": [{"name": f"Reasoning {paper}"}, {"name": f"only-{model}"}],
            "measurements": [{"name": "GSM8K"}], "behaviors": []}))
    return ok(cid, json.dumps({"relationships": [
        {"source": f"Reasoning {paper}", "target": "GSM8K", "type": "measured_by", "evidence": model}]}))


class FakeBackend:
    def __init__(self, responder=default_responder, fail_submit=(), fail_poll=(), empty_poll=()):
        self.responder = responder
        self.fail_submit, self.fail_poll, self.empty_poll = set(fail_submit), set(fail_poll), set(empty_poll)
        self.jobs = {}
        self.sent = []  # (model, phase, n_requests, description)

    def _submit(self, lines, desc):
        model = json.loads(lines[0])["body"]["model"]
        if model in self.fail_submit:
            raise RuntimeError("upload rejected")
        jid = f"job{len(self.jobs)}"
        self.jobs[jid] = (model, list(lines))
        self.sent.append((model, json.loads(json.loads(lines[0])["custom_id"])["phase"], len(lines), desc))
        return jid

    def submit_batch(self, client, lines, desc, provider="together"):
        return self._submit(lines, desc)

    def submit_batch_google(self, lines, desc, model):
        return self._submit(lines, desc)

    def poll_batch(self, client, job_id, poll_interval=15, raise_on_failure=False, include_errors=False):
        model, lines = self.jobs[job_id]
        if model in self.fail_poll:
            raise BatchJobFailed(f"batch {job_id} ended with status expired")
        if model in self.empty_poll:
            return []
        out = []
        for ln in lines:
            r = self.responder(model, json.loads(ln))
            if r is not None:
                out.append(r)
        return out

    def poll_batch_google(self, job_name, poll_interval=30, raise_on_failure=False):
        return self.poll_batch(None, job_name)

    def requests(self, model=None, phase=None):
        return sum(n for m, ph, n, _ in self.sent if (model is None or m == model) and (phase is None or ph == phase))


@contextmanager
def patched(backend, texts):
    saved = {k: getattr(M, k) for k in ("submit_batch", "poll_batch", "submit_batch_google",
                                        "poll_batch_google", "make_client", "extract_text")}
    M.submit_batch = backend.submit_batch
    M.poll_batch = backend.poll_batch
    M.submit_batch_google = backend.submit_batch_google
    M.poll_batch_google = backend.poll_batch_google
    M.make_client = lambda provider, timeout=600.0: types.SimpleNamespace(provider=provider)
    M.extract_text = lambda path, max_pages=0: texts.get(path, "")
    try:
        yield
    finally:
        for k, v in saved.items():
            setattr(M, k, v)


def make_papers(tmp, names, llm=None):
    papers = [{"name": n, "path": f"/pdfs/{i}.pdf", "is_LLM_paper": (llm or {}).get(n, True)}
              for i, n in enumerate(names)]
    path = Path(tmp) / "papers.json"
    path.write_text(json.dumps(papers))
    texts = {p["path"]: f"Body of {p['name']}" for p in papers}
    return str(path), texts


def run(backend, texts, papers_json, work_dir, **kw):
    """run_extraction against the fake backend (PANEL unless models is given); returns the report it saved."""
    kw.setdefault("models", PANEL)
    with patched(backend, texts):
        out = M.run_extraction(papers_json, work_dir, **kw)
    work_dir = Path(work_dir)
    if kw.get("dry_run"):
        assert out == work_dir / "dry_run" / "dry_run_report.json"
        return json.load(open(out))
    assert out == work_dir / "inputs" / "extraction.json" and out.exists()
    return json.load(open(work_dir / "run_report.json"))


def expect_incomplete(fn):
    with pytest.raises(M.ExtractionIncomplete) as info:
        fn()
    return info.value


def extraction(work_dir):
    return json.load(open(Path(work_dir) / "inputs" / "extraction.json"))


PANEL = [
    {"provider": "google", "model": "gemini-2.5-pro", "label": "gemini25pro"},
    {"provider": "openai", "model": "gpt-5.4-mini", "label": "gpt54mini"},
    {"provider": "together", "model": "Qwen/Qwen3-235B-A22B-Instruct-2507-tput", "label": "qwen3_235b"},
]
MODELS = [m["model"] for m in PANEL]


@contextmanager
def alt_prompt_set(name="lexis_test_prompts.alt"):
    """A prompt set module that differs from the default in its extraction prompts."""
    default = load_prompts("default")
    mod = types.ModuleType(name)
    for const in REQUIRED_NAMES:
        setattr(mod, const, getattr(default, const))
    mod.EXTRACT_ENTITIES_PROMPT = "ALT ENTITIES PROMPT. Return constructs, measurements and behaviors."
    mod.EXTRACT_RELATIONSHIPS_PROMPT = "ALT RELATIONSHIPS PROMPT for {entities_json}"
    sys.modules[name] = mod
    try:
        yield name
    finally:
        sys.modules.pop(name, None)


# ---- the panel -----------------------------------------------------------------

def test_model_spec_parsing():
    assert M.parse_model_spec("together:org/some-model-7b:some_7b") == {
        "provider": "together", "model": "org/some-model-7b", "label": "some_7b"}
    assert M.parse_model_spec("together:org/Some-Model.v2")["label"] == "some_model_v2"
    assert M.parse_model_spec("openai:ft:gpt-4o:org:mylabel")["model"] == "ft:gpt-4o:org"
    two = M.parse_model_specs(["google:gemini-2.5-pro:g,openai:gpt-5.4-mini:o"])
    assert [m["label"] for m in two] == ["g", "o"]
    assert M.parse_model_specs(["google:gemini-2.5-pro:g", "openai:gpt-5.4-mini:o"]) == two
    for bad in (["azure:x:y"], ["together:a:dup", "together:b:dup"], ["together:a:bad/label"], ["together"],
                ["default"], []):
        with pytest.raises(ValueError):
            M.parse_model_specs(bad)


def test_normalize_models_requires_a_panel():
    assert M.normalize_models(["together:org/m:a"]) == [{"provider": "together", "model": "org/m", "label": "a"}]
    assert M.normalize_models(PANEL) == PANEL and M.normalize_models(PANEL)[0] is not PANEL[0]
    cfg = {"provider": "together", "model": "org/some-model", "label": "q",
           "temperature": 0.6, "max_tokens": 32768, "extra_body": {"reasoning_effort": "low"}}
    st = M.model_settings(M.normalize_models([cfg])[0], 0, 16384)
    assert st["temperature"] == 0.6 and st["max_tokens"] == 32768 and st["temperature_sent"]
    assert M.model_settings(PANEL[0], 0, 16384)["temperature"] == 0
    for missing in (None, [], ()):
        with pytest.raises(ValueError, match="No extraction panel"):
            M.normalize_models(missing)
    with pytest.raises(ValueError, match="list of model configs"):
        M.normalize_models("models.json")
    with pytest.raises(ValueError, match="temprature"):
        M.normalize_models([{**cfg, "temprature": 1}])
    with pytest.raises(ValueError, match="price"):
        M.normalize_models([{**cfg, "price": [1]}])


def test_run_extraction_without_a_panel_fails_before_reading_inputs(tmp_path):
    with pytest.raises(TypeError):
        M.run_extraction("nope.json", tmp_path / "sb")
    with pytest.raises(ValueError, match="No extraction panel"):
        M.run_extraction("nope.json", tmp_path / "sb", None)
    with pytest.raises(ValueError, match="No extraction panel"):
        M.run_extraction("nope.json", tmp_path / "sb", [])
    assert not (tmp_path / "sb").exists()


def test_model_price_comes_from_the_model_config():
    assert M.model_price({"model": "org/m", "price": [1, 2]}) == (1, 2)
    assert M.model_price({"model": "org/m"}) is None
    assert M.add_cost({"input_tokens": 1_000_000, "output_tokens": 500_000}, (0.5, 2.0))["est_cost_usd"] == 1.5
    assert M.add_cost({"input_tokens": 1, "output_tokens": 1}, None)["est_cost_usd"] is None


def test_page_limit():
    assert M.page_limit("/data/iclr_2024_papers.json") == ("iclr", 11)
    assert M.page_limit("work/venues/emnlp25/papers.json") == ("emnlp", 10)
    assert M.page_limit("papers.json") == ("", M.DEFAULT_PAGE_LIMIT)
    assert M.page_limit("papers.json", "NeurIPS") == ("neurips", 10)
    assert M.page_limit("papers.json", "other") == ("other", M.DEFAULT_PAGE_LIMIT)
    # One page table and one unknown-venue default, shared with the screening stage.
    assert M.CONFERENCE_PAGE_LIMITS is C.CONFERENCE_PAGE_LIMITS and M.DEFAULT_PAGE_LIMIT == C.DEFAULT_PAGE_LIMIT
    assert M.page_limit("papers.json", "other")[1] == C.page_limit("other", "papers.json")[1] > 0


# ---- a full run --------------------------------------------------------------

def test_run_writes_outputs_meta_and_report(tmp_path):
    url, texts = make_papers(tmp_path, ["P1", "P2", "P3"])
    sb = tmp_path / "sb"
    be = FakeBackend()
    report = run(be, texts, url, sb)
    assert report["status"] == "ok"
    assert be.requests(phase="entities") == 9 and be.requests(phase="relationships") == 9
    out = extraction(sb)
    nn = out["P1"]["result"]["parsed_text"]["Nomological Network"]
    assert {c["name"] for c in nn["constructs"]} == {"Reasoning P1"}  # only-<model> entities dropped
    assert len(nn["relationships"]) == 1
    assert out["P1"]["provider"] == "multi-model" and out["P1"]["model"] == "gemini25pro+gpt54mini+qwen3_235b"
    for m in PANEL:
        d = sb / "trials" / m["label"]
        assert set(json.load(open(d / "entity_trials.json"))) == {"P1", "P2", "P3"}
        meta = json.load(open(d / "meta.json"))
        assert meta["model"] == m["model"]
        assert meta["phases"]["entities"]["prompt_set"] == "default"
        assert meta["phases"]["entities"]["prompt_sha256"] == report["prompt"]["entities"]["prompt_sha256"]
        assert meta["phases"]["entities"]["includes_unfingerprinted_entries"] is False
    assert [m["label"] for m in report["models"]] == [m["label"] for m in PANEL]
    assert report["papers_json"] == url and report["work_dir"] == str(sb)
    g = report["per_model"]["gemini25pro"]["entities"]
    assert g["requests_sent"] == 3 and g["usable"] == 3 and g["input_tokens"] == 3000
    assert g["est_cost_usd"] is None  # no price given
    assert json.load(open(sb / "batch_jobs.json"))
    assert set(json.load(open(sb / "trials" / "merged_entity_trials.json"))) == {"P1", "P2", "P3"}
    assert (sb / "run_reports").is_dir()


# ---- fail loud ---------------------------------------------------------------

def test_failed_submit_stops_without_empty_trials_file(tmp_path):
    url, texts = make_papers(tmp_path, ["P1", "P2"])
    sb = tmp_path / "sb"
    be = FakeBackend(fail_submit={"gpt-5.4-mini"})
    e = expect_incomplete(lambda: run(be, texts, url, sb))
    assert "gpt54mini" in str(e) and "submit failed" in str(e)
    assert not (sb / "trials" / "gpt54mini" / "entity_trials.json").exists()
    assert (sb / "trials" / "gemini25pro" / "entity_trials.json").exists()  # others saved
    assert be.requests(phase="relationships") == 0  # stopped before the second pass
    assert not (sb / "inputs" / "extraction.json").exists()
    assert json.load(open(sb / "run_report.json"))["status"] == "failed"


def test_failed_or_empty_poll_stops(tmp_path):
    for i, kw in enumerate(({"fail_poll": {MODELS[2]}}, {"empty_poll": {MODELS[2]}})):
        sb = tmp_path / f"sb{i}"
        url, texts = make_papers(tmp_path, ["P1", "P2"])
        e = expect_incomplete(lambda: run(FakeBackend(**kw), texts, url, sb))
        assert "qwen3_235b" in str(e)
        assert not (sb / "trials" / "qwen3_235b" / "entity_trials.json").exists()


def test_allow_partial_keeps_going(tmp_path):
    url, texts = make_papers(tmp_path, ["P1", "P2"])
    sb = tmp_path / "sb"
    be = FakeBackend(fail_poll={"gpt-5.4-mini"})
    report = run(be, texts, url, sb, allow_partial=True)
    assert report["status"] == "partial" and report["accepted_problems"]
    assert not (sb / "trials" / "gpt54mini" / "entity_trials.json").exists()
    assert not (sb / "trials" / "gpt54mini" / "relationship_trials.json").exists()
    assert be.requests(model="gpt-5.4-mini", phase="relationships") == 0
    nn = extraction(sb)["P1"]["result"]["parsed_text"]["Nomological Network"]
    assert {c["name"] for c in nn["constructs"]} == {"Reasoning P1"}


# ---- cache top-up ------------------------------------------------------------

def test_cache_is_topped_up_per_paper(tmp_path):
    url, texts = make_papers(tmp_path, ["P1", "P2", "P3"])
    sb = tmp_path / "sb"

    def flaky(model, req):
        meta = json.loads(req["custom_id"])
        if model == "gpt-5.4-mini" and meta["paper"] == "P3":
            return ok(req["custom_id"], "")  # empty output
        return default_responder(model, req)

    e = expect_incomplete(lambda: run(FakeBackend(flaky), texts, url, sb))
    assert "1 of 3 requested papers" in str(e)
    assert set(json.load(open(sb / "trials" / "gpt54mini" / "entity_trials.json"))) == {"P1", "P2"}

    be2 = FakeBackend()
    report = run(be2, texts, url, sb)
    assert report["status"] == "ok"
    assert be2.requests(phase="entities") == 1 and be2.requests(model="gpt-5.4-mini", phase="entities") == 1
    assert be2.requests(phase="relationships") == 9
    assert report["per_model"]["gpt54mini"]["entities"]["cached_papers"] == 2

    be3 = FakeBackend()
    report = run(be3, texts, url, sb)
    assert be3.sent == [] and report["status"] == "ok"


def test_unfingerprinted_partial_cache_is_topped_up_not_trusted_wholesale(tmp_path):
    url, texts = make_papers(tmp_path, ["P1", "P2", "P3"])
    sb = tmp_path / "sb"
    good = json.loads(default_responder("gemini-2.5-pro", {"custom_id": json.dumps(
        {"paper": "P1", "trial": 0, "phase": "entities"})})["response"]["body"]["choices"][0]["message"]["content"])
    d = sb / "trials" / "gemini25pro"
    d.mkdir(parents=True)
    (d / "entity_trials.json").write_text(json.dumps({"P1": [good], "P2": [{"error": "Parse failed"}]}))
    (d / "relationship_trials.json").write_text(json.dumps({"P2": [[]]}))  # made after a parse failure
    be = FakeBackend()
    run(be, texts, url, sb)
    assert be.requests(model="gemini-2.5-pro", phase="entities") == 2  # P2 (parse failure) and P3
    assert be.requests(model="gemini-2.5-pro", phase="relationships") == 3  # stale P2 entry redone
    meta = json.load(open(d / "meta.json"))
    assert meta["phases"]["entities"]["includes_unfingerprinted_entries"] is True


def test_stale_relationship_entry_dropped_even_when_run_stops(tmp_path):
    url, texts = make_papers(tmp_path, ["P1", "P2", "P3"])
    sb = tmp_path / "sb"
    good = json.loads(default_responder("gemini-2.5-pro", {"custom_id": json.dumps(
        {"paper": "P1", "trial": 0, "phase": "entities"})})["response"]["body"]["choices"][0]["message"]["content"])
    d = sb / "trials" / "gemini25pro"
    d.mkdir(parents=True)
    (d / "entity_trials.json").write_text(json.dumps({"P1": [good], "P2": [{"error": "Parse failed"}]}))
    (d / "relationship_trials.json").write_text(json.dumps({"P1": [[{"source": "a", "target": "b",
                                                                      "type": "related"}]], "P2": [[]]}))

    def p3_fails(model, req):
        if model == "gemini-2.5-pro" and json.loads(req["custom_id"])["paper"] == "P3":
            return ok(req["custom_id"], "not json")
        return default_responder(model, req)

    one = ["google:gemini-2.5-pro:gemini25pro"]
    expect_incomplete(lambda: run(FakeBackend(p3_fails), texts, url, sb, models=one, vote_threshold=1))
    assert set(json.load(open(d / "relationship_trials.json"))) == {"P1"}
    be = FakeBackend()
    run(be, texts, url, sb, models=one, vote_threshold=1)
    assert be.requests(phase="entities") == 1 and be.requests(phase="relationships") == 2


def test_cache_from_other_prompt_or_model_is_refused(tmp_path):
    url, texts = make_papers(tmp_path, ["P1"])
    sb = tmp_path / "sb"
    run(FakeBackend(), texts, url, sb)
    with alt_prompt_set() as alt:
        e = expect_incomplete(lambda: run(FakeBackend(), texts, url, sb, prompts=alt))
        assert isinstance(e, M.CacheMismatch) and alt in str(e)
    e = expect_incomplete(lambda: run(FakeBackend(), texts, url, sb,
                                      models=["together:org/another-model:qwen3_235b"], vote_threshold=1))
    assert isinstance(e, M.CacheMismatch)
    # A cache without prompt metadata is accepted for the default set only
    sb2 = tmp_path / "sb2"
    (sb2 / "trials" / "gemini25pro").mkdir(parents=True)
    (sb2 / "trials" / "gemini25pro" / "entity_trials.json").write_text("{}")
    with alt_prompt_set() as alt:
        e = expect_incomplete(lambda: run(FakeBackend(), texts, url, sb2, prompts=alt))
        assert isinstance(e, M.CacheMismatch)
    # Another prompt set in a fresh work directory is used and recorded
    sb3 = tmp_path / "sb3"
    be = FakeBackend()
    with alt_prompt_set() as alt:
        report = run(be, texts, url, sb3, prompts=alt)
    req = json.loads(be.jobs["job0"][1][0])
    assert req["body"]["messages"][1]["content"].startswith("ALT ENTITIES PROMPT")
    assert report["prompt"]["prompt_set"] == alt and report["prompt"]["module"] == alt
    assert json.load(open(sb3 / "trials" / "gemini25pro" / "meta.json"))["phases"]["relationships"]["prompt_set"] == alt
    assert report["prompt"]["entities"]["prompt_sha256"] != M.describe_extraction_prompts()["entities"]["prompt_sha256"]


# ---- name matching in the votes ---------------------------------------------

def variant_responder(model, req):
    meta = json.loads(req["custom_id"])
    name = {"gemini-2.5-pro": "Reasoning", "gpt-5.4-mini": "reasoning"}.get(model, "LLM reasoning")
    if meta["phase"] == "entities":
        return ok(req["custom_id"], json.dumps({"constructs": [{"name": name}], "measurements": [], "behaviors": []}))
    return ok(req["custom_id"], json.dumps({"relationships": []}))


def test_votes_compare_names_lower_cased_only(tmp_path):
    url, texts = make_papers(tmp_path, ["P1"])
    run(FakeBackend(variant_responder), texts, url, tmp_path / "a")
    constructs = extraction(tmp_path / "a")["P1"]["result"]["parsed_text"]["Nomological Network"]["constructs"]
    assert [c["name"].lower() for c in constructs] == ["reasoning"]  # the two case variants count as one, the synonym does not


PANEL_4 = PANEL + [{"provider": "together", "model": "Qwen/Qwen3.5-397B-A17B", "label": "qwen35_397b"}]


def pair_responder(model, req):
    """Entities: 'Reasoning <paper>' from every model, 'Pair' from two of the four, 'only-<model>' from one."""
    r = default_responder(model, req)
    if json.loads(req["custom_id"])["phase"] == "entities" and model in MODELS[:2]:
        body = json.loads(r["response"]["body"]["choices"][0]["message"]["content"])
        body["constructs"].append({"name": "Pair"})
        r["response"]["body"]["choices"][0]["message"]["content"] = json.dumps(body)
    return r


def constructs_of(work_dir, paper="P1"):
    nn = extraction(work_dir)[paper]["result"]["parsed_text"]["Nomological Network"]
    return sorted(c["name"] for c in nn["constructs"])


def test_vote_threshold_is_a_model_count_not_a_majority(tmp_path):
    url, texts = make_papers(tmp_path, ["P1"])
    # Default: two models suffice, even on a four-model panel where a strict majority would be three.
    report = run(FakeBackend(pair_responder), texts, url, tmp_path / "two", models=PANEL_4)
    assert report["vote_threshold"] == 2
    assert constructs_of(tmp_path / "two") == ["Pair", "Reasoning P1"]
    run(FakeBackend(pair_responder), texts, url, tmp_path / "three", models=PANEL_4, vote_threshold=3)
    assert constructs_of(tmp_path / "three") == ["Reasoning P1"]
    run(FakeBackend(pair_responder), texts, url, tmp_path / "one", models=PANEL_4, vote_threshold=1)
    assert constructs_of(tmp_path / "one") == ["Pair", "Reasoning P1"] + sorted(f"only-{m}" for m in MODELS + [PANEL_4[3]["model"]])
    # Relationships stay the union over models at this stage (voted later at the canonical level).
    nn = extraction(tmp_path / "three")["P1"]["result"]["parsed_text"]["Nomological Network"]
    assert len(nn["relationships"]) == 1
    for bad in (0, 5):
        with pytest.raises(ValueError, match="vote_threshold"):
            M.run_extraction("nope.json", tmp_path / "bad", PANEL_4, vote_threshold=bad)


# ---- run report counting -----------------------------------------------------

def test_run_report_counts_truncated_empty_and_more(tmp_path):
    good = json.dumps({"constructs": [{"name": "Reasoning"}], "measurements": [], "behaviors": []})

    def responder(model, req):
        cid = req["custom_id"]
        paper = json.loads(cid)["paper"]
        if json.loads(cid)["phase"] == "relationships":
            return ok(cid, '{"relationships": []}', usage=(500, 10))
        return {
            "T": ok(cid, good[:25], finish="length", usage=(1000, 16384)),        # truncated
            "E": ok(cid, "", usage=(1000, 0)),                                    # empty
            "K": ok(cid, "<think>plan</think>" + good, usage=(1000, 300)),        # think stripped, usable
            "L": ok(cid, "Here you go: " + good, usage=(1000, 300)),              # leading text, parse failure
            "R": {"custom_id": cid, "response": {"status_code": 500, "body": {"error": "boom"}},
                  "error": None},                                                 # request error
            "M": None,                                                            # never returned
            "G": ok(cid, good, usage=(2_000_000, 1_000_000)),                     # usable, big usage
        }[paper]

    url, texts = make_papers(tmp_path, list("TEKLRMG"))
    sb = tmp_path / "sb"
    report = run(FakeBackend(responder), texts, url, sb, allow_partial=True, vote_threshold=1,
                 models=[{"provider": "together", "model": "org/model-a", "label": "m1", "price": [0.60, 3.60]}])
    s = report["per_model"]["m1"]["entities"]
    expect = {"requests_sent": 7, "results_received": 6, "missing_results": 1, "request_errors": 1,
              "empty_outputs": 1, "parse_failures": 2, "truncated_outputs": 1, "think_stripped": 1,
              "leading_text": 1, "usable": 2, "input_tokens": 2_004_000, "output_tokens": 1_016_984}
    assert {k: s[k] for k in expect} == expect, {k: s[k] for k in expect}
    assert s["finish_reasons"]["length"] == 1
    assert s["papers_without_output"] == ["E", "L", "M", "R", "T"]
    assert s["truncated_papers"] == ["T"]
    assert s["pending_papers"] == 7 and s["cached_papers"] == 0
    assert abs(s["est_cost_usd"] - (2.004 * 0.60 + 1.016984 * 3.60)) < 1e-3
    r = report["per_model"]["m1"]["relationships"]
    assert r["requests_sent"] == 2 and r["usable"] == 2
    assert report["per_model"]["m1"]["total_est_cost_usd"] is not None
    assert set(json.load(open(sb / "trials" / "m1" / "entity_trials.json"))) == {"K", "G"}
    assert report["status"] == "partial"


# ---- dry run -----------------------------------------------------------------

def test_dry_run_writes_requests_and_submits_nothing(tmp_path):
    url, texts = make_papers(tmp_path, ["P1", "P2", "P3"])
    sb = tmp_path / "sb"
    be = FakeBackend()

    def no_client(provider, timeout=600.0):
        raise AssertionError("dry run must not create API clients")

    with patched(be, texts):
        M.make_client = no_client
        out = M.run_extraction(url, sb, dry_run=True,
                               models=[{"provider": "together", "model": "org/model-a", "label": "m1",
                                        "price": [0.60, 3.60]},
                                       {"provider": "openai", "model": "gpt-5.4-mini", "label": "gpt54mini"}])
    assert be.sent == [] and out == sb / "dry_run" / "dry_run_report.json"
    assert not (sb / "trials").exists() and not (sb / "run_report.json").exists()
    rep = json.load(open(out))
    assert rep["status"] == "dry_run"
    q = rep["per_model"]["m1"]
    assert q["entities"]["requests"] == 3 and q["relationships"]["requests"] == 3
    assert q["relationships"]["approximate_requests"] == 3
    assert q["entities"]["est_input_tokens"] > 0 and q["entities"]["est_input_cost_usd"] is not None
    assert q["entities"]["output_cost_cap_usd"] == round(3 * 16384 / 1e6 * 3.60, 4)
    assert rep["per_model"]["gpt54mini"]["entities"]["est_input_cost_usd"] is None
    assert rep["per_model"]["gpt54mini"]["entities"]["output_cost_cap_usd"] is None
    lines = (sb / "dry_run" / "m1" / "entities.jsonl").read_text().splitlines()
    assert len(lines) == 3 and json.loads(lines[0])["body"]["model"] == "org/model-a"
    assert rep["token_method"] in ("chars/4", "tiktoken:o200k_base")


def test_dry_run_splits_large_batches_and_uses_cache(tmp_path):
    url, texts = make_papers(tmp_path, [f"P{i}" for i in range(7)])
    sb = tmp_path / "sb"
    run(FakeBackend(), texts, url, sb, models=["together:m1:a"], vote_threshold=1)
    url2, texts2 = make_papers(tmp_path, [f"P{i}" for i in range(10)])
    saved = dict(M.BATCH_FILE_LIMITS)
    M.BATCH_FILE_LIMITS["together"] = (10**9, 1)  # one request per file
    try:
        be = FakeBackend()
        rep = run(be, texts2, url2, sb, models=["together:m1:a"], vote_threshold=1, dry_run=True)
    finally:
        M.BATCH_FILE_LIMITS.clear()
        M.BATCH_FILE_LIMITS.update(saved)
    ent = rep["per_model"]["a"]["entities"]
    assert ent["requests"] == 3 and ent["cached_papers"] == 7 and len(ent["files"]) == 3
    assert (sb / "dry_run" / "a" / "entities.part3.jsonl").exists()
    rel = rep["per_model"]["a"]["relationships"]
    assert rel["requests"] == 3 and rel["approximate_requests"] == 3


def test_real_run_submits_one_batch_per_part(tmp_path):
    url, texts = make_papers(tmp_path, ["P1", "P2", "P3"])
    saved = dict(M.BATCH_FILE_LIMITS)
    M.BATCH_FILE_LIMITS["together"] = (10**9, 1)
    try:
        be = FakeBackend()
        report = run(be, texts, url, tmp_path / "sb", models=["together:m1:a"], vote_threshold=1)
    finally:
        M.BATCH_FILE_LIMITS.clear()
        M.BATCH_FILE_LIMITS.update(saved)
    ent_jobs = [s for s in be.sent if s[1] == "entities"]
    assert len(ent_jobs) == 3 and ent_jobs[0][3] == "entities-a-p1of3"
    assert len(report["per_model"]["a"]["entities"]["jobs"]) == 3


# ---- workers -----------------------------------------------------------------

def test_workers_sizes_the_text_and_polling_pools(tmp_path, monkeypatch):
    sizes = []

    class RecordingPool(ThreadPoolExecutor):
        def __init__(self, max_workers=None, **kw):
            sizes.append(max_workers)
            super().__init__(max_workers=max_workers, **kw)

    monkeypatch.setattr(M, "ThreadPoolExecutor", RecordingPool)
    url, texts = make_papers(tmp_path, ["P1", "P2", "P3"])
    saved = dict(M.BATCH_FILE_LIMITS)
    M.BATCH_FILE_LIMITS["together"] = (10**9, 1)      # three jobs per phase
    try:
        run(FakeBackend(), texts, url, tmp_path / "sb", models=["together:m1:a"], vote_threshold=1, workers=2)
    finally:
        M.BATCH_FILE_LIMITS.clear()
        M.BATCH_FILE_LIMITS.update(saved)
    assert sizes == [2, 2, 2]                          # PDF text, entities polling, relationships polling
    sizes.clear()
    run(FakeBackend(), texts, url, tmp_path / "sb2", models=["together:m1:a"], vote_threshold=1, workers=8)
    assert sizes == [8, 1, 1]                          # one job per phase: the pool is no larger than the jobs
    with pytest.raises(ValueError):
        run(FakeBackend(), texts, url, tmp_path / "sb3", models=["together:m1:a"], vote_threshold=1, workers=0)


# ---- CLI ---------------------------------------------------------------------

def test_cli_requires_the_panel_and_prints_help():
    parser = M.build_arg_parser()
    args = parser.parse_args(["--papers-json", "x", "--work-dir", "y", "--models", "together:org/m:a"])
    assert M.parse_model_specs(args.models) == [{"provider": "together", "model": "org/m", "label": "a"}]
    assert args.max_tokens == 16384 and args.prompts == "default" and args.conference == "auto"
    assert args.vote_threshold == 2 and not args.allow_partial and not args.dry_run and args.log_dir == "logs"
    args = parser.parse_args(["--papers-json", "x", "--work-dir", "y", "--models", "together:org/m:a",
                              "--vote-threshold", "3"])
    assert args.vote_threshold == 3
    with pytest.raises(SystemExit) as info:
        parser.parse_args(["--papers-json", "x", "--work-dir", "y"])
    assert info.value.code == 2
    with pytest.raises(SystemExit) as info:
        parser.parse_args(["--help"])
    assert info.value.code == 0


def test_cli_main_runs_and_returns_output_path(tmp_path):
    url, texts = make_papers(tmp_path, ["P1", "P2"])
    sb = tmp_path / "sb"
    be = FakeBackend()
    with patched(be, texts):
        out = M.main(["--papers-json", url, "--work-dir", str(sb), "--models", "together:org/m:a,openai:gpt-5.4-mini:o",
                      "--conference", "iclr", "--log-dir", str(tmp_path / "logs")])
    logging.getLogger().setLevel(logging.CRITICAL)
    assert out == sb / "inputs" / "extraction.json" and out.exists()
    assert be.requests(phase="entities") == 4
    assert json.load(open(sb / "run_report.json"))["status"] == "ok"
    with patched(be, texts):
        out = M.main(["--papers-json", url, "--work-dir", str(sb), "--models", "together:org/m:a,openai:gpt-5.4-mini:o",
                      "--dry-run", "--log-dir", str(tmp_path / "logs")])
    assert out == sb / "dry_run" / "dry_run_report.json"
    with patched(FakeBackend(fail_submit={"org/m"}), texts):
        with pytest.raises(SystemExit) as info:
            M.main(["--papers-json", url, "--work-dir", str(tmp_path / "sb2"), "--models", "together:org/m:a",
                    "--vote-threshold", "1", "--log-dir", str(tmp_path / "logs")])
    assert info.value.code == 2
