"""Synchronous screening: one chat-completion request per paper.

Reads a paper list JSON, extracts the main text of each unscreened paper's PDF, sends the
screening prompt through the provider's OpenAI-compatible chat-completions endpoint
(``openai``, ``google`` or ``together``) from a thread pool under a requests-per-minute
cap, and writes the list back with an ``is_LLM_paper`` flag. The output is checkpointed
every ``save_every`` papers and written in the input order at the end.

Papers that already carry a verdict are skipped, so a run can be resumed. A PDF with no
extractable text is recorded as not LLM-related (``is_LLM_paper`` False,
``screen_note="empty_pdf"``) without a model call. An empty answer (after removing
``<think>`` blocks) is retried once with a larger output-token cap. A request that fails
leaves the paper without a verdict (``screen_error`` holds the error text) so that the next
run screens it again. The run report is written next to the output as
``<output>.screen_report.json``. Record conventions are documented in
``aiconstructlexis.screen._common``.
"""
from __future__ import annotations

import copy
import logging
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock

from tqdm.auto import tqdm

from aiconstructlexis.providers.clients import init_client
from aiconstructlexis.screen._common import (
    SCREEN_MAX_TOKENS,
    load_papers,
    needs_screening,
    page_limit,
    same_file,
    start_report,
    strip_reasoning,
    utc_timestamp,
    write_papers,
    write_screen_report,
)
from aiconstructlexis.util.logging import log_counts, log_step
from aiconstructlexis.util.pdf import extract_text_from_pdf

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "openai/gpt-oss-120b"


def _make_client(provider: str):
    """OpenAI-compatible chat-completions client for the given provider."""
    return init_client(provider, openai_compatible=True)


def _extract_main_text(pdf_path: str, max_pages: int) -> str:
    """Main body text of a PDF: the first ``max_pages`` pages, cut at the References heading.

    Returns "" when the file is missing or cannot be read.
    """
    if not Path(pdf_path).exists():
        return ""
    try:
        return extract_text_from_pdf(pdf_path, max_pages=max_pages)
    except Exception as e:
        logger.debug("PDF extraction failed for %s: %s", pdf_path, e)
        return ""


def _call_screen(client, model: str, user_content: str, max_tokens: int,
                 paper_name: str, max_retries: int = 3):
    """One screening call with retries on transient errors. Returns the reply text.

    Raises the last exception when the call cannot be completed.
    """
    for attempt in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_content}],
                # Reasoning models emit thinking tokens before the final answer; with a
                # tiny budget the visible content comes back empty.
                max_tokens=max_tokens,
                temperature=0,
            )
            return (resp.choices[0].message.content if resp.choices else "") or ""
        except Exception as e:
            status = getattr(e, "status_code", None)
            retryable = status in (429, 500, 502, 503, 529) or type(e).__name__ in (
                "APITimeoutError", "APIConnectionError", "Timeout", "ConnectionError"
            )
            if retryable and attempt < max_retries - 1:
                delay = min(2.0 * (2 ** attempt) + random.uniform(0, 1), 60.0)
                logger.warning(
                    "Retry %d/%d for %s: %s (sleep %.1fs)",
                    attempt + 1, max_retries - 1,
                    paper_name[:50], e, delay,
                )
                time.sleep(delay)
            else:
                raise
    raise RuntimeError("unreachable")


def _screen_one(client, paper: dict, model: str,
                rate_timestamps: list, rate_lock: Lock,
                max_rpm: int, max_pages: int, prompt: str,
                retry_max_tokens: int = 2048, retry_empty: bool = True) -> dict:
    """Classify one paper. Returns an updated copy of the paper dict.

    A missing PDF is left unscreened (screen_note="missing_pdf"); a PDF without text gets
    the verdict False (screen_note="empty_pdf"). An empty answer is retried once with
    retry_max_tokens when ``retry_empty`` is set; if still empty the paper is left
    unscreened with screen_error="empty_answer". A failed request also leaves the paper
    unscreened, with the error text in screen_error.
    """
    paper = copy.deepcopy(paper)
    pdf_path = paper.get("path") or ""
    if not pdf_path or not Path(pdf_path).exists():
        paper.pop("is_LLM_paper", None)
        paper.pop("screen_error", None)
        paper["screen_note"] = "missing_pdf"
        return paper

    text = _extract_main_text(pdf_path, max_pages)
    if not text.strip():
        paper["is_LLM_paper"] = False
        paper["screen_note"] = "empty_pdf"
        paper.pop("screen_error", None)
        return paper

    user_content = prompt + text
    budgets = (SCREEN_MAX_TOKENS, retry_max_tokens) if retry_empty else (SCREEN_MAX_TOKENS,)
    for attempt, max_tokens in enumerate(budgets):
        # Sliding-window rate limiting
        sleep_time = 0.0
        with rate_lock:
            now = time.time()
            rate_timestamps[:] = [t for t in rate_timestamps if now - t < 60]
            if len(rate_timestamps) >= max_rpm:
                sleep_time = 60.0 - (now - rate_timestamps[0]) + 0.1
        if sleep_time > 0:
            time.sleep(sleep_time)
        with rate_lock:
            rate_timestamps.append(time.time())

        try:
            content = _call_screen(client, model, user_content, max_tokens, paper["name"])
        except Exception as e:
            logger.error("FAILED %s: %s", paper["name"][:60], e)
            paper.pop("is_LLM_paper", None)
            paper["screen_error"] = str(e)
            return paper
        # Strip <think>...</think> blocks that some reasoning models emit
        clean, _ = strip_reasoning(content)
        answer = clean.strip().lower()
        if answer:
            paper["is_LLM_paper"] = answer.startswith("yes")
            paper.pop("screen_error", None)
            if paper.get("screen_note") == "missing_pdf":
                paper.pop("screen_note")
            return paper
        if attempt == 0 and len(budgets) > 1:
            logger.warning("Empty answer for %s; retrying once (max_tokens=%d)",
                           paper["name"][:60], retry_max_tokens)

    paper.pop("is_LLM_paper", None)
    paper["screen_error"] = "empty_answer"
    return paper


def screen_sync(input_json, output_json, provider: str = "together", model: str = DEFAULT_MODEL,
                prompts: str | None = "default", workers: int = 8, max_rpm: int = 3600,
                save_every: int = 50, retry_empty: bool = True, retry_max_tokens: int = 2048,
                conference: str | None = None) -> dict:
    """Screen every unscreened paper in ``input_json`` with direct chat-completion calls.

    Writes the screened list to ``output_json`` (which may be the input file) and the run
    report next to it. Returns the run report.
    """
    prompt, report = start_report(input_json, output_json, provider, model, "sync", prompts)
    logger.info("Screening prompt set %s (sha %s)", report["prompt_set"], report["prompt_sha256"])

    papers = load_papers(input_json)
    logger.info("Loaded %d papers from %s", len(papers), input_json)

    conf, max_pages = page_limit(conference, input_json)
    logger.info("Conference: %s, extracting first %d pages per paper", conf or "unknown", max_pages)

    pending = [i for i, p in enumerate(papers) if needs_screening(p)]
    logger.info("Already screened: %d, remaining: %d", len(papers) - len(pending), len(pending))

    if not pending:
        llm_count = sum(1 for p in papers if p.get("is_LLM_paper"))
        logger.info("All done. %d/%d are LLM papers.", llm_count, len(papers))
        if not same_file(input_json, output_json):
            write_papers(output_json, papers)
        report.update({"papers": len(papers), "screened_now": 0, "llm_papers": llm_count,
                       "finished_at": utc_timestamp()})
        return report

    client = _make_client(provider)
    rate_timestamps: list[float] = []
    rate_lock = Lock()
    done: dict[int, dict] = {}   # index -> screened copy (written only by this thread)
    output_path = Path(output_json)

    def _current():
        return [done.get(i, p) for i, p in enumerate(papers)]

    def _save_checkpoint():
        write_papers(output_path, _current())

    with log_step(logger, "screening", total=len(pending), model=model):
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {
                pool.submit(
                    _screen_one, client, papers[i], model,
                    rate_timestamps, rate_lock, max_rpm,
                    max_pages, prompt, retry_max_tokens, retry_empty,
                ): i
                for i in pending
            }
            done_count = 0
            for fut in tqdm(as_completed(futures), total=len(futures),
                            unit="paper", desc="Screening"):
                done[futures[fut]] = fut.result()
                done_count += 1
                if done_count % save_every == 0:
                    _save_checkpoint()
                    logger.info(
                        "Checkpoint: %d/%d done", done_count, len(pending),
                    )

    # Final save, in input order
    final = _current()
    write_papers(output_path, final)

    llm_count = sum(1 for p in final if p.get("is_LLM_paper"))
    # Papers left unscreened (no PDF) carry no is_LLM_paper; they are not "non-LLM".
    non_llm = sum(1 for p in final if "is_LLM_paper" in p and not p["is_LLM_paper"])
    errors = sum(1 for p in final if "screen_error" in p)
    screened = [done[i] for i in pending]
    report.update({
        "papers": len(final), "screened_now": len(screened), "llm_papers": llm_count,
        "errors": errors,
        "missing_pdf": sum(1 for p in screened if p.get("screen_note") == "missing_pdf"),
        "empty_pdf": sum(1 for p in screened if p.get("screen_note") == "empty_pdf"),
        "empty_answer": [p.get("name", "") for p in screened if p.get("screen_error") == "empty_answer"],
        "finished_at": utc_timestamp(),
    })
    log_counts(
        logger, "screening_results",
        total=len(final), llm_papers=llm_count, non_llm=non_llm,
        errors=errors, missing_pdf=report["missing_pdf"], empty_answer=len(report["empty_answer"]),
    )
    report["report_file"] = str(write_screen_report(output_path, report))
    logger.info("Output written to %s (report %s)", output_path, report["report_file"])
    return report
