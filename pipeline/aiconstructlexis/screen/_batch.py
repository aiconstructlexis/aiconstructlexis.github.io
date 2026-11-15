"""Batch-mode screening through the Together Batch API.

Steps:
  1. Extract the main text of each unscreened paper's PDF in parallel
     (pymupdf, one process per worker; the text is cut at the References heading).
  2. Build a JSONL file with one chat-completion request per paper.
  3. Upload to Together and create one batch job per file part; the file is split
     to stay under Together's 100 MB / 50,000-request limits.
  4. Poll until every job has completed.
  5. Download the results and merge them back into the paper list.
  6. Retry empty answers once with a direct call (``retry_empty``).

A PDF with no extractable text is recorded as not LLM-related (``is_LLM_paper`` False,
``screen_note="empty_pdf"``) and sent to no model. A request that comes back with an error,
without choices or without any result line leaves the paper without a verdict and sets
``screen_error``, so the next run screens it again.

Outputs, next to ``output_json``: ``<output>.batch_requests.jsonl`` (and ``.partN.jsonl``
when split), ``<output>.batch_results.jsonl`` and ``<output>.screen_report.json``.
Record conventions are documented in ``aiconstructlexis.screen._common``.
"""
from __future__ import annotations

import json
import logging
import multiprocessing as mp
import re
import time
from pathlib import Path

from tqdm.auto import tqdm

from aiconstructlexis.screen._common import (
    SCREEN_MAX_TOKENS,
    load_papers,
    mark_missing_pdf,
    needs_screening,
    page_limit,
    pdf_missing,
    same_file,
    screening_answer,
    set_answer,
    split_jsonl_lines,
    start_report,
    utc_timestamp,
    write_papers,
    write_screen_report,
)

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "openai/gpt-oss-120b"

# Together Batch API: 100 MB per input file, 50,000 requests per batch (5% byte margin).
TOGETHER_MAX_FILE_BYTES = 95_000_000
TOGETHER_MAX_REQUESTS = 50_000


def _extract_one(args: tuple[int, str, int]) -> tuple[int, str]:
    """Extract main body text from a single PDF. Runs in a worker process."""
    idx, pdf_path, max_pages = args
    if not pdf_path or not Path(pdf_path).exists():
        return idx, ""
    try:
        import pymupdf
        doc = pymupdf.open(pdf_path)
        n = min(max_pages, len(doc))
        text = "\n".join(doc[i].get_text() for i in range(n))
        doc.close()
    except Exception:
        return idx, ""

    m = re.search(r'\n\s*(References|REFERENCES|Bibliography)\s*\n', text)
    if m:
        text = text[:m.start()]
    return idx, text


def _make_client():
    """Together SDK client; the Batch API (file upload, batch jobs) is only reachable through it."""
    from aiconstructlexis.providers.clients import init_together_sdk_client

    try:
        return init_together_sdk_client()
    except ImportError as e:
        raise ImportError(f"{e} Batch-mode screening needs it; use mode='sync' otherwise.") from e


def build_requests(papers: list, pending: list, texts: dict, model: str,
                   prompt: str) -> tuple[list, dict, dict]:
    """Build one request per screenable paper. Marks missing/empty PDFs in place.

    Returns (jsonl_lines, id_map {custom_id: paper index}, counts).
    """
    lines, id_map = [], {}
    counts = {"missing_pdf": 0, "empty_pdf": 0}
    for i in pending:
        if pdf_missing(papers[i]):
            mark_missing_pdf(papers[i])
            counts["missing_pdf"] += 1
            continue
        text = texts.get(i, "")
        if not text.strip():
            papers[i]["is_LLM_paper"] = False
            papers[i]["screen_note"] = "empty_pdf"
            papers[i].pop("screen_error", None)
            counts["empty_pdf"] += 1
            continue
        custom_id = f"paper_{i}"
        id_map[custom_id] = i
        request = {
            "custom_id": custom_id,
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt + text}
                ],
                "max_tokens": SCREEN_MAX_TOKENS,
                "temperature": 0,
            },
        }
        lines.append(json.dumps(request))
    return lines, id_map, counts


def write_request_parts(jsonl_path: Path, lines: list,
                        max_bytes: int = TOGETHER_MAX_FILE_BYTES,
                        max_requests: int = TOGETHER_MAX_REQUESTS) -> list:
    """Write the full request file, plus .partN.jsonl files when it must be split.

    Returns the list of files to upload (the full file when one part suffices).
    """
    jsonl_path.write_text("".join(ln + "\n" for ln in lines))
    parts = split_jsonl_lines(lines, max_bytes, max_requests)
    if len(parts) <= 1:
        return [jsonl_path]
    out = []
    for n, part in enumerate(parts, 1):
        part_path = jsonl_path.with_suffix(f".part{n}.jsonl")
        part_path.write_text("".join(ln + "\n" for ln in part))
        out.append(part_path)
    logger.info("Split %.1fMB JSONL into %d parts (%s lines)", jsonl_path.stat().st_size / 1e6,
                len(parts), " + ".join(str(len(p)) for p in parts))
    return out


def apply_results(papers: list, id_map: dict, result_lines) -> tuple[dict, list]:
    """Merge batch result lines into papers. Returns (stats, empty_answer_indices)."""
    stats = {"successes": 0, "errors": 0, "empty_answers": 0, "missing_results": 0}
    empty, seen = [], set()
    for line in result_lines:
        if not line.strip():
            continue
        result = json.loads(line)
        custom_id = result.get("custom_id")
        idx = id_map.get(custom_id)
        if idx is None:
            continue
        seen.add(custom_id)
        if result.get("error"):
            papers[idx].pop("is_LLM_paper", None)
            papers[idx]["screen_error"] = str(result["error"])
            stats["errors"] += 1
            continue
        body = (result.get("response") or {}).get("body") or {}
        choices = body.get("choices", [])
        if not choices:
            papers[idx].pop("is_LLM_paper", None)
            papers[idx]["screen_error"] = "no_choices"
            stats["errors"] += 1
            continue
        is_llm, _ = screening_answer(choices[0].get("message", {}).get("content", ""))
        set_answer(papers[idx], is_llm)
        if is_llm is None:
            empty.append(idx)
            stats["empty_answers"] += 1
        else:
            stats["successes"] += 1
    missing = set(id_map) - seen
    for cid in missing:
        # No result line at all: leave unscreened and flag it, so a rerun picks it up.
        papers[id_map[cid]].pop("is_LLM_paper", None)
        papers[id_map[cid]]["screen_error"] = "no_result"
    stats["missing_results"] = len(missing)
    return stats, empty


def retry_empty_answers(client, papers: list, indices: list, texts: dict, model: str,
                        prompt: str, max_tokens: int) -> int:
    """Retry papers with empty answers once via direct calls. Returns how many got a verdict."""
    resolved = 0
    for idx in indices:
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt + texts.get(idx, "")}],
                max_tokens=max_tokens,
                temperature=0,
            )
            content = resp.choices[0].message.content if resp.choices else ""
        except Exception as e:  # noqa: BLE001
            logger.warning("Empty-answer retry failed for %s: %s", papers[idx].get("name", "")[:60], e)
            continue
        is_llm, _ = screening_answer(content)
        set_answer(papers[idx], is_llm)
        if is_llm is not None:
            resolved += 1
    return resolved


def extract_texts(papers: list, pending: list, max_pages: int, workers: int) -> dict[int, str]:
    """Main text of every pending paper whose PDF exists, keyed by paper index.

    ``workers`` is the number of extraction processes: 0 uses every CPU, 1 extracts in the
    calling process.
    """
    extract_args = [(i, papers[i].get("path") or "", max_pages) for i in pending
                    if not pdf_missing(papers[i])]
    texts: dict[int, str] = {}
    n_workers = workers or mp.cpu_count()
    if n_workers <= 1:
        for a in tqdm(extract_args, desc="Extracting text", unit="paper"):
            idx, text = _extract_one(a)
            texts[idx] = text
    elif extract_args:
        logger.info("Extracting text with %d workers (pymupdf)...", n_workers)
        with mp.Pool(n_workers) as pool:
            for idx, text in tqdm(
                pool.imap_unordered(_extract_one, extract_args, chunksize=32),
                total=len(extract_args),
                desc="Extracting text",
                unit="paper",
            ):
                texts[idx] = text
    return texts


def screen_batch(input_json, output_json, model: str = DEFAULT_MODEL, prompts: str | None = "default",
                 workers: int = 8, poll_interval: int = 60, retry_empty: bool = True,
                 retry_max_tokens: int = 2048, conference: str | None = None) -> dict:
    """Screen every unscreened paper in ``input_json`` through the Together Batch API.

    Writes the screened list to ``output_json`` (which may be the input file) and the run
    report next to it. Returns the run report. Papers that already carry a verdict are
    left untouched, so a run can be resumed.
    """
    prompt, report = start_report(input_json, output_json, "together", model, "batch", prompts)
    logger.info("Screening prompt set %s (sha %s)", report["prompt_set"], report["prompt_sha256"])

    client = _make_client()

    papers = load_papers(input_json)
    logger.info("Loaded %d papers from %s", len(papers), input_json)

    conf, max_pages = page_limit(conference, input_json)
    logger.info("Conference: %s, extracting first %d pages per paper", conf or "unknown", max_pages)

    pending = [i for i, p in enumerate(papers) if needs_screening(p)]
    already = len(papers) - len(pending)
    logger.info("Already screened: %d, remaining: %d", already, len(pending))

    if not pending:
        llm_count = sum(1 for p in papers if p.get("is_LLM_paper"))
        logger.info("All done. %d/%d are LLM papers.", llm_count, len(papers))
        if not same_file(input_json, output_json):
            write_papers(output_json, papers)
        report.update({"requests": 0, "llm_papers": llm_count, "papers": len(papers),
                       "finished_at": utc_timestamp()})
        return report

    # Step 1: text extraction (missing PDFs are not opened)
    texts = extract_texts(papers, pending, max_pages, workers)

    # Step 2: request file
    jsonl_path = Path(output_json).with_suffix(".batch_requests.jsonl")
    logger.info("Building JSONL at %s", jsonl_path)
    lines, id_map, counts = build_requests(papers, pending, texts, model, prompt)
    report.update(counts)
    report["requests"] = len(lines)
    logger.info("Built %d requests (%d empty PDFs, %d missing PDFs left unscreened)",
                len(id_map), counts["empty_pdf"], counts["missing_pdf"])

    if not id_map:
        logger.info("No papers to screen. Writing output.")
        write_papers(output_json, papers)
        report["report_file"] = str(write_screen_report(output_json, report))
        return report

    # Step 3: split into as many files as Together's limits require
    jsonl_parts = write_request_parts(jsonl_path, lines, TOGETHER_MAX_FILE_BYTES, TOGETHER_MAX_REQUESTS)
    report["batch_files"] = [str(p) for p in jsonl_parts]

    # Step 4: upload and create one batch job per part
    batch_ids = []
    for part_path in jsonl_parts:
        logger.info("Uploading %s (%.1fMB)...", part_path.name, part_path.stat().st_size / 1e6)
        file_resp = client.files.upload(file=str(part_path), purpose="batch-api", check=False)
        file_id = file_resp.id
        logger.info("Uploaded file: %s", file_id)

        batch = client.batches.create(
            input_file_id=file_id,
            endpoint="/v1/chat/completions",
            model_id=model,
        )
        bid = batch.job.id if hasattr(batch, 'job') else batch.id
        batch_ids.append(bid)
        logger.info("Batch job created: %s", bid)
    report["batch_ids"] = batch_ids

    # Step 5: poll every batch job until completion
    logger.info("Polling %d batch job(s) (interval=%ds)...", len(batch_ids), poll_interval)
    completed_statuses = {}
    while len(completed_statuses) < len(batch_ids):
        for bid in batch_ids:
            if bid in completed_statuses:
                continue
            status = client.batches.retrieve(bid)
            state = str(getattr(status.status, "value", status.status))
            progress = getattr(status, "progress", None) or 0
            logger.info("Batch %s: status=%s progress=%.1f%%", bid, state, progress)

            if state.upper() == "COMPLETED":
                completed_statuses[bid] = status
            elif state.upper() in ("FAILED", "EXPIRED", "CANCELLED"):
                error = getattr(status, "error", "unknown")
                logger.error("Batch job %s %s: %s", bid, state, error)
                raise RuntimeError(f"Batch job {bid} {state}: {error}")

        if len(completed_statuses) < len(batch_ids):
            time.sleep(poll_interval)

    # Step 6: download and parse the results of every batch job
    all_result_text = []
    for bid in batch_ids:
        output_file_id = completed_statuses[bid].output_file_id
        logger.info("Downloading results from %s (batch %s)...", output_file_id, bid)
        result_resp = client.files.content(output_file_id)
        result_text = result_resp.text if hasattr(result_resp, 'text') else result_resp.read().decode()
        all_result_text.append(result_text.strip())

    combined_result = "\n".join(all_result_text)
    results_path = Path(output_json).with_suffix(".batch_results.jsonl")
    results_path.write_text(combined_result)
    logger.info("Results saved to %s", results_path)

    stats, empty = apply_results(papers, id_map, combined_result.split("\n"))
    logger.info("Parsed results: %d successes, %d errors, %d empty answers, %d missing results",
                stats["successes"], stats["errors"], stats["empty_answers"], stats["missing_results"])
    report.update(stats)

    # Step 7: retry empty answers once (direct calls)
    report["empty_answer_retried"] = 0
    report["empty_answer_resolved"] = 0
    if empty and retry_empty:
        logger.info("Retrying %d empty answers once (max_tokens=%d)", len(empty), retry_max_tokens)
        report["empty_answer_retried"] = len(empty)
        report["empty_answer_resolved"] = retry_empty_answers(
            client, papers, empty, texts, model, prompt, retry_max_tokens)
    still_empty = [papers[i].get("name", "") for i in empty
                   if papers[i].get("screen_error") == "empty_answer"]
    report["empty_answer_unresolved"] = still_empty
    if still_empty:
        logger.warning("%d papers still have empty answers and stay unscreened "
                       "(screen_error=empty_answer); a rerun will try them again", len(still_empty))

    llm_count = sum(1 for p in papers if p.get("is_LLM_paper"))
    write_papers(output_json, papers)
    report["llm_papers"] = llm_count
    report["papers"] = len(papers)
    report["finished_at"] = utc_timestamp()
    report["report_file"] = str(write_screen_report(output_json, report))
    logger.info("Output: %d/%d LLM papers. Written to %s (report %s)", llm_count, len(papers),
                output_json, report["report_file"])
    return report
