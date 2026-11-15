"""Helpers shared by the batch and synchronous screeners.

A screened paper list keeps the schema of the input list and adds these keys:

* ``is_LLM_paper`` (bool): the screening verdict. Absent while a paper is unscreened.
* ``screen_note``: ``"missing_pdf"`` when the PDF was not found (no verdict; the paper is
  screened by the next run) or ``"empty_pdf"`` when the PDF had no extractable text. A PDF
  without text is recorded as not LLM-related (verdict False) without a model call.
* ``screen_error``: ``"empty_answer"`` when the model returned nothing after the retry,
  ``"no_result"`` / ``"no_choices"`` when a batch returned nothing for the request, or the
  provider's error text. A paper with ``screen_error`` carries no verdict and is screened
  again by the next run.

The run report written next to the output (``<output>.screen_report.json``) records the
provider, model, prompt fingerprint and the counts of each outcome.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

from aiconstructlexis.prompts import describe_prompt, get_prompt
from aiconstructlexis.util.json_tools import split_jsonl_lines, strip_reasoning

# Pages of main text read per venue, in screening and in extraction: the venue's main-body
# page limit plus one or two pages of buffer for formatting variation; references and
# appendices are not read.
CONFERENCE_PAGE_LIMITS: dict[str, int] = {
    "neurips": 10,
    "iclr": 11,
    "icml": 10,
    "acl": 10,
    "emnlp": 10,
    "naacl": 10,
}
# Pages read for a venue not in the table, in both stages.
DEFAULT_PAGE_LIMIT = 12

# Output-token cap for the first screening attempt. Reasoning models spend part of this
# budget on thinking tokens; an empty visible answer is retried with a larger cap.
SCREEN_MAX_TOKENS = 512


def detect_conference(input_path: str | Path) -> str:
    """Infer the venue key from the input file path ("" when none matches)."""
    p = str(input_path).lower()
    for conf in CONFERENCE_PAGE_LIMITS:
        if conf in p:
            return conf
    return ""


def page_limit(conference: str | None, input_path: str | Path) -> tuple[str, int]:
    """(venue key, number of main-text pages to read) for a run.

    ``conference`` wins when given; otherwise the venue is inferred from the input path.
    Unknown venues read DEFAULT_PAGE_LIMIT pages.
    """
    conf = (conference or "").strip().lower() or detect_conference(input_path)
    return conf, CONFERENCE_PAGE_LIMITS.get(conf, DEFAULT_PAGE_LIMIT)


def needs_screening(p: dict) -> bool:
    """No verdict yet, a failed or empty request, or a PDF that was missing last time."""
    return ("is_LLM_paper" not in p or "screen_error" in p
            or p.get("screen_note") == "missing_pdf")


def pdf_missing(p: dict) -> bool:
    path = p.get("path") or ""
    return not path or not Path(path).exists()


def mark_missing_pdf(p: dict) -> None:
    p.pop("is_LLM_paper", None)
    p.pop("screen_error", None)
    p["screen_note"] = "missing_pdf"


def screening_answer(content) -> tuple[bool | None, str]:
    """Interpret a screening reply. Returns (is_llm, clean_text); is_llm is None when empty."""
    text, _ = strip_reasoning(content or "")
    answer = text.strip().lower()
    if not answer:
        return None, ""
    return answer.startswith("yes"), answer


def set_answer(p: dict, is_llm: bool | None) -> None:
    """Store a screening verdict; an empty answer leaves the paper unscreened."""
    if is_llm is None:
        p.pop("is_LLM_paper", None)
        p["screen_error"] = "empty_answer"
    else:
        p["is_LLM_paper"] = is_llm
        p.pop("screen_error", None)
        if p.get("screen_note") == "missing_pdf":
            p.pop("screen_note")


def utc_timestamp() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load_papers(input_json: str | Path) -> list:
    with open(input_json, encoding="utf-8") as f:
        return json.load(f)


def write_papers(output_json: str | Path, papers: list) -> Path:
    path = Path(output_json)
    path.write_text(json.dumps(papers, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def start_report(input_json, output_json, provider: str, model: str, mode: str,
                 prompts: str | None) -> tuple[str, dict]:
    """Load the screening prompt and open the run report.

    Returns (prompt_text, report). The report carries the prompt set name, module and
    sha256 fingerprint so an output can be traced to the exact prompt that produced it.
    """
    prompt = get_prompt(prompts, "SCREENING_PAPERS_PROMPT")
    info = describe_prompt(prompts, "SCREENING_PAPERS_PROMPT")
    report = {
        "input": str(input_json), "output": str(output_json), "mode": mode,
        "provider": provider, "model": model,
        "prompt_set": info["prompt_set"], "prompt_module": info["module"],
        "prompt_sha256": info["sha256"],
        "started_at": utc_timestamp(),
    }
    return prompt, report


def report_path(output_json: str | Path) -> Path:
    return Path(output_json).with_suffix(".screen_report.json")


def write_screen_report(output_json: str | Path, report: dict) -> Path:
    path = report_path(output_json)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def same_file(a: str | Path, b: str | Path) -> bool:
    return Path(a).resolve() == Path(b).resolve()
