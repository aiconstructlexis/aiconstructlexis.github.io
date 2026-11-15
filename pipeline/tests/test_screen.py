"""Tests for the screening stage with fake clients (no network).

Covers: empty answers are flagged and retried once, missing PDFs stay unscreened,
<think> blocks are stripped, the batch request file is split into as many parts as
Together's limits require, both modes keep the input order and write a run report, and
the dispatcher rejects unsupported provider/mode combinations.
"""
import json
import types
from pathlib import Path
from threading import Lock

import pytest

from aiconstructlexis.screen import _batch as BS
from aiconstructlexis.screen import _common as C
from aiconstructlexis.screen import _sync as SL
from aiconstructlexis.screen import screen as S
from aiconstructlexis.screen import screen_papers


def completion(content):
    return types.SimpleNamespace(choices=[types.SimpleNamespace(message=types.SimpleNamespace(content=content))])


class FakeChat:
    """client.chat.completions.create returning scripted replies; records calls."""

    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = []
        self.chat = types.SimpleNamespace(completions=types.SimpleNamespace(create=self._create))

    def _create(self, **kw):
        self.calls.append(kw)
        r = self.replies.pop(0)
        if isinstance(r, Exception):
            raise r
        return completion(r)


def make_pdf(path: Path, text: str):
    import pymupdf
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), text)
    doc.save(str(path))
    doc.close()


def result_line(cid, content=None, error=None, choices=True):
    body = {"choices": [{"message": {"content": content}}]} if choices else {"choices": []}
    return json.dumps({"custom_id": cid, "response": {"body": body}, "error": error})


# ---- shared helpers ----------------------------------------------------------

def test_strip_reasoning_shapes():
    assert C.strip_reasoning("<think>a</think>Yes") == ("Yes", {"think_closed": True, "think_orphan_close": False, "think_unclosed": False})
    assert C.strip_reasoning("thinking ...</think>No")[0] == "No"
    assert C.strip_reasoning("<think>never closed")[0] == ""
    assert C.strip_reasoning('{"a": "</think>"}')[0] == '{"a": "</think>"}'
    assert C.strip_reasoning(None) == ("", {"think_closed": False, "think_orphan_close": False, "think_unclosed": False})


def test_split_jsonl_lines_packs_in_order_and_rejects_oversized_line():
    lines = ["a" * 10, "b" * 10, "c" * 10]
    assert C.split_jsonl_lines(lines, max_bytes=22) == [["a" * 10, "b" * 10], ["c" * 10]]
    assert C.split_jsonl_lines(lines, max_bytes=10**6, max_requests=1) == [[ln] for ln in lines]
    with pytest.raises(ValueError):
        C.split_jsonl_lines(["x" * 100], max_bytes=50)


def test_page_limit_prefers_explicit_conference_then_path():
    assert C.page_limit(None, "work/venues/iclr24/papers.json") == ("iclr", 11)
    assert C.page_limit("NeurIPS", "work/venues/iclr24/papers.json") == ("neurips", 10)
    assert C.page_limit(None, "work/venues/other/papers.json") == ("", C.DEFAULT_PAGE_LIMIT)
    assert C.DEFAULT_PAGE_LIMIT == 12
    # Every venue reads its main-body limit (8 to 10 pages) plus one or two pages of buffer.
    assert all(10 <= n <= 11 for n in C.CONFERENCE_PAGE_LIMITS.values())


def test_screening_answer_and_set_answer():
    assert C.screening_answer("<think>x</think>Yes.") == (True, "yes.")
    assert C.screening_answer("No") == (False, "no")
    assert C.screening_answer("<think>cut off") == (None, "")
    p = {"name": "p", "screen_note": "missing_pdf", "screen_error": "old"}
    C.set_answer(p, True)
    assert p == {"name": "p", "is_LLM_paper": True}
    C.set_answer(p, None)
    assert "is_LLM_paper" not in p and p["screen_error"] == "empty_answer" and C.needs_screening(p)


# ---- batch screener: pure helpers -------------------------------------------

def test_batch_build_marks_missing_and_empty_pdfs(tmp_path):
    exists = tmp_path / "ok.pdf"
    exists.write_bytes(b"%PDF")
    papers = [{"name": "missing", "path": str(tmp_path / "nope.pdf")},
              {"name": "nopath"},
              {"name": "empty", "path": str(exists)},
              {"name": "good", "path": str(exists)}]
    lines, id_map, counts = BS.build_requests(papers, [0, 1, 2, 3], {2: "  ", 3: "body"}, "m", "PROMPT ")
    assert counts == {"missing_pdf": 2, "empty_pdf": 1}
    for p in papers[:2]:
        assert "is_LLM_paper" not in p and p["screen_note"] == "missing_pdf"
        assert C.needs_screening(p)
    assert papers[2]["is_LLM_paper"] is False and papers[2]["screen_note"] == "empty_pdf"
    assert id_map == {"paper_3": 3}
    body = json.loads(lines[0])["body"]
    assert body["messages"][0]["content"] == "PROMPT body" and body["max_tokens"] == 512


def test_batch_apply_results_flags_empty_and_strips_think():
    papers = [{"name": f"p{i}"} for i in range(7)]
    papers[4]["is_LLM_paper"] = True   # a stale verdict from an earlier run
    papers[6]["is_LLM_paper"] = False
    id_map = {f"paper_{i}": i for i in range(7)}
    lines = [result_line("paper_0", "<think>long reasoning</think>Yes"),
             result_line("paper_1", "<think>reasoning that never closed"),
             result_line("paper_2", ""),
             result_line("paper_3", "No."),
             result_line("paper_4", error={"message": "rate"}),
             "",  # paper_5 has no result line at all
             result_line("paper_6", choices=False)]
    stats, empty = BS.apply_results(papers, id_map, lines)
    assert papers[0]["is_LLM_paper"] is True
    assert empty == [1, 2] and stats["empty_answers"] == 2
    for i in (1, 2):
        assert "is_LLM_paper" not in papers[i] and papers[i]["screen_error"] == "empty_answer"
    assert papers[3]["is_LLM_paper"] is False and "screen_error" not in papers[3]
    # A failed request is not a verdict: the paper carries no is_LLM_paper and is screened again.
    assert papers[4]["screen_error"] == "{'message': 'rate'}" and "is_LLM_paper" not in papers[4]
    assert papers[5]["screen_error"] == "no_result" and "is_LLM_paper" not in papers[5]
    assert papers[6]["screen_error"] == "no_choices" and "is_LLM_paper" not in papers[6]
    assert all(C.needs_screening(papers[i]) for i in (1, 2, 4, 5, 6))
    assert not C.needs_screening(papers[0]) and not C.needs_screening(papers[3])
    assert stats["successes"] == 2 and stats["errors"] == 2 and stats["missing_results"] == 1

    client = FakeChat(["Yes", ""])
    resolved = BS.retry_empty_answers(client, papers, empty, {1: "t1", 2: "t2"}, "m", "P ", 2048)
    assert resolved == 1 and len(client.calls) == 2 and client.calls[0]["max_tokens"] == 2048
    assert papers[1]["is_LLM_paper"] is True and "screen_error" not in papers[1]
    assert papers[2]["screen_error"] == "empty_answer" and "is_LLM_paper" not in papers[2]


def test_batch_request_file_splits_into_three_or_more_parts(tmp_path):
    lines = [json.dumps({"custom_id": f"paper_{i}", "pad": "x" * 100}) for i in range(7)]
    size = len(lines[0].encode()) + 1
    path = tmp_path / "out.batch_requests.jsonl"
    parts = BS.write_request_parts(path, lines, max_bytes=size * 2, max_requests=50_000)
    assert len(parts) == 4 and parts[0].name == "out.batch_requests.part1.jsonl"
    got = [ln for p in parts for ln in p.read_text().splitlines()]
    assert got == lines and len(path.read_text().splitlines()) == 7
    parts = BS.write_request_parts(path, lines, max_bytes=10**9, max_requests=3)
    assert [len(p.read_text().splitlines()) for p in parts] == [3, 3, 1]
    assert BS.write_request_parts(path, lines[:2]) == [path]


# ---- batch screener: end to end with a fake Together client ------------------

class FakeTogether(FakeChat):
    def __init__(self, answers, retry_replies):
        super().__init__(retry_replies)
        self.answers = answers
        self.uploads, self._files, self._jobs = [], {}, {}
        self.files = types.SimpleNamespace(upload=self._upload, content=self._content)
        self.batches = types.SimpleNamespace(create=self._create_batch, retrieve=self._retrieve)

    def _upload(self, file, purpose, check):
        fid = f"file{len(self.uploads)}"
        self.uploads.append(file)
        self._files[fid] = Path(file).read_text()
        return types.SimpleNamespace(id=fid)

    def _create_batch(self, input_file_id, endpoint, model_id):
        bid = f"batch{len(self._jobs)}"
        out = []
        for ln in self._files[input_file_id].splitlines():
            cid = json.loads(ln)["custom_id"]
            out.append(result_line(cid, self.answers[cid]))
        self._files[f"out_{bid}"] = "\n".join(out) + "\n"
        self._jobs[bid] = types.SimpleNamespace(status="COMPLETED", progress=100.0, output_file_id=f"out_{bid}")
        return types.SimpleNamespace(id=bid)

    def _retrieve(self, bid):
        return self._jobs[bid]

    def _content(self, fid):
        return types.SimpleNamespace(text=self._files[fid])


def test_batch_cli_end_to_end(tmp_path, monkeypatch):
    papers = []
    for i in range(6):
        pdf = tmp_path / f"p{i}.pdf"
        make_pdf(pdf, f"Paper {i} about large language models.")
        papers.append({"name": f"Paper {i}", "path": str(pdf)})
    papers.append({"name": "Missing", "path": str(tmp_path / "missing.pdf")})
    papers.append({"name": "Done", "path": str(tmp_path / "missing.pdf"), "is_LLM_paper": True})
    inp = tmp_path / "papers.json"
    inp.write_text(json.dumps(papers))
    answers = {f"paper_{i}": a for i, a in enumerate(["Yes", "No", "<think>x</think>yes", "", "No", "Yes"])}
    client = FakeTogether(answers, retry_replies=["No"])
    monkeypatch.setattr(BS, "_make_client", lambda: client)
    monkeypatch.setattr(BS, "TOGETHER_MAX_FILE_BYTES", 2500)  # each request is ~1 KB, so this forces several parts

    out_path = S.main(["--input", str(inp), "--output", str(tmp_path / "out.json"), "--workers", "1",
                       "--poll-interval", "0", "--log-dir", str(tmp_path / "logs")])
    assert out_path == tmp_path / "out.json"
    assert len(client.uploads) >= 3, client.uploads
    out = json.loads(out_path.read_text())
    assert [p["name"] for p in out] == [p["name"] for p in papers]
    by = {p["name"]: p for p in out}
    assert by["Paper 0"]["is_LLM_paper"] is True and by["Paper 2"]["is_LLM_paper"] is True
    assert by["Paper 3"]["is_LLM_paper"] is False and "screen_error" not in by["Paper 3"]  # answered by the retry
    assert len(client.calls) == 1 and client.calls[0]["max_tokens"] == 2048
    assert "is_LLM_paper" not in by["Missing"] and by["Missing"]["screen_note"] == "missing_pdf"
    assert by["Done"]["is_LLM_paper"] is True and "screen_note" not in by["Done"]
    report = json.loads((tmp_path / "out.screen_report.json").read_text())
    assert report["missing_pdf"] == 1 and report["empty_answers"] == 1 and report["empty_answer_resolved"] == 1
    assert report["mode"] == "batch" and report["provider"] == "together"
    assert report["prompt_set"] == "default" and len(report["prompt_sha256"]) == 16
    assert report["llm_papers"] == 4 and report["papers"] == 8
    assert (tmp_path / "out.batch_results.jsonl").exists()
    # The request contains the shipped screening prompt followed by the PDF text.
    first = json.loads((tmp_path / "out.batch_requests.jsonl").read_text().splitlines()[0])
    content = first["body"]["messages"][0]["content"]
    assert content.startswith(C.get_prompt("default", "SCREENING_PAPERS_PROMPT"))
    assert "Paper 0 about large language models" in content


def test_batch_no_retry_leaves_empty_answers_flagged(tmp_path, monkeypatch):
    pdf = tmp_path / "p.pdf"
    make_pdf(pdf, "A paper.")
    inp = tmp_path / "papers.json"
    inp.write_text(json.dumps([{"name": "P", "path": str(pdf)}]))
    client = FakeTogether({"paper_0": ""}, retry_replies=["Yes"])
    monkeypatch.setattr(BS, "_make_client", lambda: client)
    screen_papers(inp, inp, mode="batch", workers=1, poll_interval=0, retry_empty=False)
    out = json.loads(inp.read_text())
    assert out[0]["screen_error"] == "empty_answer" and "is_LLM_paper" not in out[0]
    assert client.calls == []
    report = json.loads((tmp_path / "papers.screen_report.json").read_text())
    assert report["empty_answer_retried"] == 0 and report["empty_answer_unresolved"] == ["P"]


def test_batch_failed_job_raises(tmp_path, monkeypatch):
    pdf = tmp_path / "p.pdf"
    make_pdf(pdf, "A paper.")
    inp = tmp_path / "papers.json"
    inp.write_text(json.dumps([{"name": "P", "path": str(pdf)}]))
    client = FakeTogether({"paper_0": "Yes"}, retry_replies=[])

    def failing_create(input_file_id, endpoint, model_id):
        client._jobs["batch0"] = types.SimpleNamespace(status="FAILED", progress=0.0, error="quota")
        return types.SimpleNamespace(id="batch0")

    client.batches = types.SimpleNamespace(create=failing_create, retrieve=client._retrieve)
    monkeypatch.setattr(BS, "_make_client", lambda: client)
    with pytest.raises(RuntimeError, match="FAILED"):
        screen_papers(inp, inp, mode="batch", workers=1, poll_interval=0)


def test_already_screened_list_is_copied_to_output(tmp_path, monkeypatch):
    papers = [{"name": "A", "is_LLM_paper": True}, {"name": "B", "is_LLM_paper": False}]
    inp = tmp_path / "in.json"
    inp.write_text(json.dumps(papers))
    monkeypatch.setattr(BS, "_make_client", lambda: FakeTogether({}, []))
    monkeypatch.setattr(SL, "_make_client", lambda provider: FakeChat([]))
    for mode in ("batch", "sync"):
        out = tmp_path / f"{mode}.json"
        assert screen_papers(inp, out, mode=mode, provider="together") == out
        assert json.loads(out.read_text()) == papers


# ---- synchronous screener ----------------------------------------------------

def screen(client, paper, prompt="P ", **kw):
    return SL._screen_one(client, paper, "m", [], Lock(), 10_000, 12, prompt, **kw)


def test_sync_screen_missing_pdf_empty_answer_and_think(tmp_path, monkeypatch):
    pdf = tmp_path / "a.pdf"
    pdf.write_bytes(b"%PDF")
    monkeypatch.setattr(SL, "_extract_main_text", lambda path, max_pages: "main text")

    client = FakeChat([])
    out = screen(client, {"name": "x", "path": str(tmp_path / "none.pdf"), "is_LLM_paper": False})
    assert out["screen_note"] == "missing_pdf" and "is_LLM_paper" not in out and client.calls == []

    client = FakeChat(["", "Yes"])
    out = screen(client, {"name": "x", "path": str(pdf)})
    assert out["is_LLM_paper"] is True and [c["max_tokens"] for c in client.calls] == [512, 2048]

    client = FakeChat(["", "<think>only thinking"])
    out = screen(client, {"name": "x", "path": str(pdf)})
    assert out["screen_error"] == "empty_answer" and "is_LLM_paper" not in out
    assert C.needs_screening(out)

    client = FakeChat([""])
    out = screen(client, {"name": "x", "path": str(pdf)}, retry_empty=False)
    assert out["screen_error"] == "empty_answer" and len(client.calls) == 1

    client = FakeChat(["<think>hmm</think>No"])
    original = {"name": "x", "path": str(pdf), "screen_error": "old"}
    out = screen(client, original)
    assert out["is_LLM_paper"] is False and "screen_error" not in out
    assert original == {"name": "x", "path": str(pdf), "screen_error": "old"}  # input not mutated

    client = FakeChat(["Yes"])
    out = screen(client, {"name": "x", "path": str(pdf)}, prompt="OTHER PROMPT ")
    assert client.calls[0]["messages"][0]["content"] == "OTHER PROMPT main text"

    client = FakeChat([RuntimeError("boom")])
    out = screen(client, {"name": "x", "path": str(pdf), "is_LLM_paper": True})
    assert "is_LLM_paper" not in out and out["screen_error"] == "boom"   # a failed request is not a verdict
    assert C.needs_screening(out)


def test_sync_extract_main_text_reads_pdf_and_tolerates_bad_files(tmp_path):
    pdf = tmp_path / "a.pdf"
    make_pdf(pdf, "Body text here.\nReferences\n[1] Something.")
    text = SL._extract_main_text(str(pdf), 12)
    assert "Body text here." in text and "Something" not in text
    bad = tmp_path / "bad.pdf"
    bad.write_bytes(b"%PDF")
    assert SL._extract_main_text(str(bad), 12) == ""
    assert SL._extract_main_text(str(tmp_path / "none.pdf"), 12) == ""


def test_sync_keeps_order_and_writes_report(tmp_path, monkeypatch):
    papers = []
    for i in range(4):
        pdf = tmp_path / f"{i}.pdf"
        pdf.write_bytes(b"%PDF")
        papers.append({"name": f"P{i}", "path": str(pdf)})
    papers.append({"name": "gone", "path": str(tmp_path / "gone.pdf")})
    papers.append({"name": "P0", "path": str(tmp_path / "0.pdf"), "is_LLM_paper": True})  # duplicate name, done
    inp = tmp_path / "in.json"
    inp.write_text(json.dumps(papers))
    replies = {"text P0": "Yes", "text P1": "No", "text P2": "", "text P3": "Yes"}

    class Client(FakeChat):
        def _create(self, **kw):
            self.calls.append(kw)
            key = kw["messages"][0]["content"].split("\n")[-1]
            return completion(replies[key] if kw["max_tokens"] == 512 or key != "text P2" else "")

    client = Client([])
    seen_providers = []

    def make_client(provider):
        seen_providers.append(provider)
        return client

    monkeypatch.setattr(SL, "_make_client", make_client)
    monkeypatch.setattr(SL, "_extract_main_text",
                        lambda path, max_pages: "\ntext " + {str(tmp_path / f"{i}.pdf"): f"P{i}" for i in range(4)}[path])
    out_path = screen_papers(inp, tmp_path / "out.json", provider="openai", model="m", mode="sync",
                             workers=2, save_every=1)
    assert seen_providers == ["openai"]
    out = json.loads(out_path.read_text())
    assert [p["name"] for p in out] == ["P0", "P1", "P2", "P3", "gone", "P0"]
    assert out[0]["is_LLM_paper"] is True and out[1]["is_LLM_paper"] is False
    assert out[2]["screen_error"] == "empty_answer" and "is_LLM_paper" not in out[2]
    assert out[4]["screen_note"] == "missing_pdf" and "is_LLM_paper" not in out[4]
    assert out[5] == papers[5]
    for call in client.calls:
        assert call["messages"][0]["content"].startswith(C.get_prompt("default", "SCREENING_PAPERS_PROMPT"))
    report = json.loads((tmp_path / "out.screen_report.json").read_text())
    assert report["missing_pdf"] == 1 and report["empty_answer"] == ["P2"] and report["llm_papers"] == 3
    assert report["mode"] == "sync" and report["provider"] == "openai" and report["screened_now"] == 5
    assert report["prompt_set"] == "default" and len(report["prompt_sha256"]) == 16


# ---- dispatcher --------------------------------------------------------------

def test_screen_papers_rejects_unsupported_combinations(tmp_path):
    inp = tmp_path / "in.json"
    inp.write_text("[]")
    with pytest.raises(ValueError, match="mode='sync'"):
        screen_papers(inp, inp, provider="openai", mode="batch")
    with pytest.raises(ValueError, match="Unknown mode"):
        screen_papers(inp, inp, mode="stream")
    with pytest.raises(ValueError, match="Unknown provider"):
        screen_papers(inp, inp, provider="other", mode="sync")
