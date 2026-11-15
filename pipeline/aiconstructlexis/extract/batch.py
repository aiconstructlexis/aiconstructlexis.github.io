"""Two-pass extraction requests, provider batch APIs and per-paper voting.

This module holds the building blocks of the extraction stage, which the
multi-model stage (``aiconstructlexis.extract.multi_model``) combines.

Two passes per paper:
  1. entities: the entity prompt plus the paper text; the model returns the
     constructs, measurement instruments and behaviors it finds;
  2. relationships: the relationship prompt, the entities kept after voting,
     and the paper text; the model returns relationships among those entities.

Requests are OpenAI-format JSONL lines (``custom_id`` is a JSON object with
``paper``, ``trial`` and ``phase``). The same lines are submitted through the
OpenAI Batch API, Together's batch API (together SDK) or, converted to inline
requests, Google's batch API (google-genai SDK); results from every provider
are normalised to the OpenAI result shape before parsing. Model reasoning
(``<think>`` blocks) is removed from completions before JSON parsing, and each
result is classified (ok, empty, parse_failed, wrong_schema, request_error,
plus truncation and token-usage flags) for the run report.

Per-paper voting (``majority_vote_entities`` / ``majority_vote_relationships``):
an entity or relationship is kept when at least ``threshold`` trials propose it,
names being compared lower-cased and through the optional name mapping. With
``threshold=1`` the vote is a union.
"""

from __future__ import annotations

import json
import logging
import os
import re
import tempfile
import time
from pathlib import Path

from aiconstructlexis.prompts import DEFAULT_PROMPT_SET, get_prompt, load_prompts, prompt_sha256
from aiconstructlexis.providers.clients import (
    init_google_client,
    init_google_openai_compatible_client,
    init_openai_client,
)
from aiconstructlexis.util.json_tools import clean_messy_string, clean_to_dict, strip_reasoning
from aiconstructlexis.util.pdf import extract_text_from_pdf

logger = logging.getLogger(__name__)

_FAILED_SENTINEL = "__FAILED__"

# Batch input-file limits per provider: (max bytes per file, max requests per batch).
# Together: 100 MB and 50,000 requests; OpenAI: 200 MB and 50,000 requests.
# The byte limits below keep a 5% margin. Google batches are uploaded through
# the native SDK (2 GB file limit) and are not split.
BATCH_FILE_LIMITS = {
    "together": (95_000_000, 50_000),
    "openai": (190_000_000, 50_000),
}

# System messages for the two extraction phases. They are part of the prompt
# fingerprint recorded with every trials cache (see describe_extraction_prompts).
ENTITY_SYSTEM_MESSAGE = "Respond with valid JSON only. Extract entities (constructs, measurements, behaviors) — no relationships."
RELATIONSHIP_SYSTEM_MESSAGE = "Respond with valid JSON only. Extract relationships between the provided entities."


class BatchJobFailed(RuntimeError):
    """A batch job ended in a failed/cancelled/expired state or produced no output.

    Raised only when a poll helper is called with raise_on_failure=True; by
    default such a job yields an empty result list.
    """


def load_papers(path: str):
    """Papers flagged ``is_LLM_paper`` in a paper-list JSON, deduplicated by (name, path).

    Duplicates can come from scraping (e.g. truncated titles), and the OpenAI
    batch API rejects a whole batch on duplicate custom_ids.
    """
    with open(path) as f:
        papers = json.load(f)
    seen = set()
    out = []
    n_dupes = 0
    for p in papers:
        if not p.get("is_LLM_paper", False):
            continue
        key = (p.get("name", ""), p.get("path", ""))
        if key in seen:
            n_dupes += 1
            continue
        seen.add(key)
        out.append(p)
    if n_dupes:
        logger.warning(
            "load_papers: dropped %d duplicate (name, path) entries from %s",
            n_dupes, path,
        )
    return out


def extract_text(pdf_path: str, max_pages: int = 0) -> str:
    """Text of a PDF (first ``max_pages`` pages when > 0), capped at 500,000 characters."""
    text = extract_text_from_pdf(pdf_path, max_pages=max_pages) or ""
    if len(text) > 500_000:
        text = text[:500_000] + "\n\n[... text truncated ...]"
    return text


def parse_json_response(raw: str) -> dict:
    """Parse a completion into a dict: strip reasoning and Markdown fences, then
    read JSON, repairing quoting defects when strict parsing fails.
    Returns {"error": "Parse failed"} when nothing dict-like can be recovered."""
    raw, _ = strip_reasoning(raw)
    fence = re.search(r"^```(?:json)?\s*\n(.*?)\n```\s*$", raw, re.DOTALL)
    if fence:
        raw = fence.group(1).strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        parsed = clean_to_dict(clean_messy_string(raw))
        if isinstance(parsed, str):
            try:
                parsed = json.loads(parsed)
            except json.JSONDecodeError:
                parsed = clean_to_dict(clean_messy_string(parsed))
        return parsed if isinstance(parsed, dict) else {"error": "Parse failed"}


def _is_reasoning_model(model: str) -> bool:
    """True when the model's chat-completions endpoint rejects the temperature parameter.

    Unless the caller sets ``send_temperature``, request bodies for these models leave
    temperature out and those for every other model include it.
    """
    m = model.lower()
    # OpenAI o3 and o4 families (o3, o4-mini, ...).
    if any(m.startswith(p) for p in ("o3", "o4")):
        return True
    # gpt-5 and gpt-5-mini by exact name; other gpt-5.x names (gpt-5.4, gpt-5.4-mini) do not match.
    if m == "gpt-5" or m == "gpt-5-mini":
        return True
    # Together thinking models.
    if "thinking" in m or "-r1" in m:
        return True
    return False


def _token_limit_key(model: str) -> str:
    """Return the correct token limit parameter name for this model.
    OpenAI reasoning/frontier models (o3, o4-mini, gpt-5*) need 'max_completion_tokens';
    others use 'max_tokens'."""
    m = model.lower()
    if any(m.startswith(p) for p in ("o3", "o4", "gpt-5", "gpt-4.1")):
        return "max_completion_tokens"
    return "max_tokens"


def _extraction_prompts(prompts=None):
    """(EXTRACT_ENTITIES_PROMPT, EXTRACT_RELATIONSHIPS_PROMPT) of a prompt set.

    ``prompts`` names a prompt set as understood by ``aiconstructlexis.prompts``
    ("default", or a dotted module path); None means the default set.
    """
    return (get_prompt(prompts, "EXTRACT_ENTITIES_PROMPT"),
            get_prompt(prompts, "EXTRACT_RELATIONSHIPS_PROMPT"))


def describe_extraction_prompts(prompts=None) -> dict:
    """Prompt set, source module and short sha256 of each phase's prompt text.

    The hashes cover the prompt template and the system message, so a change
    to either shows up as a different fingerprint. Trials caches record this
    fingerprint and are only reused by runs with the same one.
    """
    name = prompts or DEFAULT_PROMPT_SET
    ent_prompt, rel_prompt = _extraction_prompts(name)
    return {
        "prompt_set": name,
        "module": load_prompts(name).__name__,
        "entities": {
            "prompt_name": "EXTRACT_ENTITIES_PROMPT",
            "prompt_sha256": prompt_sha256(ent_prompt),
            "system_sha256": prompt_sha256(ENTITY_SYSTEM_MESSAGE),
        },
        "relationships": {
            "prompt_name": "EXTRACT_RELATIONSHIPS_PROMPT",
            "prompt_sha256": prompt_sha256(rel_prompt),
            "system_sha256": prompt_sha256(RELATIONSHIP_SYSTEM_MESSAGE),
        },
    }


def _request_body(model, system_msg, user_content, temperature, max_tokens,
                  send_temperature, extra_body):
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_content},
        ],
        _token_limit_key(model): max_tokens,
    }
    if send_temperature is None:
        send_temperature = not _is_reasoning_model(model)
    if send_temperature:
        body["temperature"] = temperature
    if extra_body:
        for k, v in extra_body.items():
            if k in ("model", "messages"):
                raise ValueError(f"extra_body may not override {k!r}")
            body[k] = v
    return body


def build_entity_jsonl(papers, paper_texts, model, temperature, n_trials,
                       prompts=None, max_tokens=16384,
                       send_temperature=None, extra_body=None):
    """Build JSONL lines for entity extraction: one request per paper and trial.

    Papers without text are skipped. Options:
      prompts           prompt set name (None = the default set).
      max_tokens        output-token cap (16384).
      send_temperature  True/False forces sending temperature; None decides
                        with _is_reasoning_model(model).
      extra_body        dict of extra request-body fields (provider specific).
    """
    entities_prompt, _ = _extraction_prompts(prompts)

    lines = []
    for paper in papers:
        name = paper["name"]
        text = paper_texts[name]
        if not text.strip():
            continue
        user_content = f"{entities_prompt}\n\n---\nPaper text (extracted from PDF):\n\n{text}"
        for trial in range(n_trials):
            custom_id = json.dumps({"paper": name, "trial": trial, "phase": "entities"})
            body = _request_body(model, ENTITY_SYSTEM_MESSAGE, user_content, temperature,
                                 max_tokens, send_temperature, extra_body)
            line = {
                "custom_id": custom_id,
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": body,
            }
            lines.append(json.dumps(line, ensure_ascii=False))
    return lines


def _entity_name(ent) -> str:
    if isinstance(ent, dict):
        return ent.get("name", "")
    if isinstance(ent, str):
        return ent
    return ""


def build_relationship_jsonl(papers, paper_texts, voted_entities, model, temperature, n_trials,
                             prompts=None, max_tokens=16384,
                             send_temperature=None, extra_body=None):
    """Build JSONL lines for relationship extraction from each paper's kept entities.

    Papers without text or without entities are skipped. The optional
    arguments mean the same as in build_entity_jsonl.
    """
    _, relationships_prompt = _extraction_prompts(prompts)

    lines = []
    for paper in papers:
        name = paper["name"]
        text = paper_texts[name]
        if not text.strip():
            continue
        entities = voted_entities.get(name)
        if not entities:
            continue

        entity_names = {
            "constructs": [_entity_name(c) for c in entities.get("constructs", [])],
            "measurements": [_entity_name(m) for m in entities.get("measurements", [])],
            "behaviors": [_entity_name(b) for b in entities.get("behaviors", [])],
        }
        entities_json_str = json.dumps(entity_names, indent=2, ensure_ascii=False)
        rel_prompt = relationships_prompt.format(entities_json=entities_json_str)
        user_content = f"{rel_prompt}\n\n---\nPaper text (extracted from PDF):\n\n{text}"

        for trial in range(n_trials):
            custom_id = json.dumps({"paper": name, "trial": trial, "phase": "relationships"})
            body = _request_body(model, RELATIONSHIP_SYSTEM_MESSAGE, user_content, temperature,
                                 max_tokens, send_temperature, extra_body)
            line = {
                "custom_id": custom_id,
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": body,
            }
            lines.append(json.dumps(line, ensure_ascii=False))
    return lines


def estimate_tokens(text: str) -> tuple[int, str]:
    """Estimate token count: tiktoken (o200k_base) if installed, else len(text) / 4.

    Returns (n_tokens, method).
    """
    try:
        import tiktoken  # type: ignore
        enc = tiktoken.get_encoding("o200k_base")
        return len(enc.encode(text, disallowed_special=())), "tiktoken:o200k_base"
    except Exception:  # noqa: BLE001
        return (len(text) + 3) // 4, "chars/4"


def result_content(r: dict) -> str:
    """Visible text of one OpenAI-format batch result line ("" if absent)."""
    resp = r.get("response") or {}
    body = resp.get("body") or {}
    choices = body.get("choices") or []
    if not choices:
        return ""
    msg = choices[0].get("message") or {}
    return msg.get("content") or ""


def result_finish_reason(r: dict):
    """finish_reason of one batch result line, normalized to lower case (None if absent).

    Gemini's "MAX_TOKENS" is mapped to "length" by poll_batch_google.
    """
    body = ((r.get("response") or {}).get("body")) or {}
    choices = body.get("choices") or []
    fr = choices[0].get("finish_reason") if choices else None
    return fr.lower() if isinstance(fr, str) else fr


def result_usage(r: dict) -> dict:
    """Token usage {'input', 'output', 'reasoning'} from one batch result line.

    Reads chat-completions usage (prompt_tokens / completion_tokens), the
    responses-API names (input_tokens / output_tokens) and reasoning-token
    details when present. Missing values are 0.
    """
    body = ((r.get("response") or {}).get("body")) or {}
    u = body.get("usage") or {}
    inp = u.get("prompt_tokens", u.get("input_tokens", 0)) or 0
    out = u.get("completion_tokens", u.get("output_tokens", 0)) or 0
    details = u.get("completion_tokens_details") or u.get("output_tokens_details") or {}
    reasoning = (details.get("reasoning_tokens") if isinstance(details, dict) else 0) or u.get("reasoning_tokens", 0) or 0
    return {"input": int(inp), "output": int(out), "reasoning": int(reasoning)}


def result_is_error(r: dict) -> bool:
    """True when a batch result line is a request-level failure."""
    if r.get("error"):
        return True
    resp = r.get("response")
    if resp is None:
        return True
    status = resp.get("status_code")
    if isinstance(status, int) and status >= 400:
        return True
    body = resp.get("body") or {}
    if isinstance(body, dict) and body.get("error"):
        return True
    return result_content(r) == _FAILED_SENTINEL


TRUNCATION_FINISH_REASONS = ("length", "max_tokens", "max_output_tokens")


def classify_result(r: dict, phase: str | None = None) -> dict:
    """Classify one batch result line for the run report.

    status is one of:
      request_error  the request failed (error line, HTTP >= 400, sentinel);
      empty          no visible text after removing reasoning;
      parse_failed   text present but not parseable as a JSON object;
      wrong_schema   JSON parsed but lacks the phase's expected keys;
      ok             usable output (parsed is set).
    Flags: truncated (finish_reason says the token cap was hit),
    think_stripped (reasoning tags were removed from the text),
    leading_text (non-JSON text before the JSON object, a sign that
    reasoning or prose leaked into the answer), reasoning_field (the message
    carried a separate reasoning field).
    """
    out = {
        "status": "ok", "parsed": None,
        "finish_reason": result_finish_reason(r),
        "usage": result_usage(r),
        "truncated": False, "think_stripped": False,
        "leading_text": False, "reasoning_field": False,
    }
    out["truncated"] = out["finish_reason"] in TRUNCATION_FINISH_REASONS
    if result_is_error(r):
        out["status"] = "request_error"
        return out
    body = ((r.get("response") or {}).get("body")) or {}
    choices = body.get("choices") or []
    msg = (choices[0].get("message") or {}) if choices else {}
    out["reasoning_field"] = bool(msg.get("reasoning") or msg.get("reasoning_content"))
    raw = result_content(r)
    text, info = strip_reasoning(raw)
    out["think_stripped"] = any(info.values())
    if not text:
        out["status"] = "empty"
        return out
    unfenced = text
    fence = re.search(r"^```(?:json)?\s*\n(.*?)\n```\s*$", text, re.DOTALL)
    if fence:
        unfenced = fence.group(1).strip()
    brace = unfenced.find("{")
    out["leading_text"] = brace > 0 and bool(unfenced[:brace].strip())
    parsed = parse_json_response(raw)
    if not isinstance(parsed, dict) or (set(parsed) == {"error"} and parsed.get("error") == "Parse failed"):
        out["status"] = "parse_failed"
        return out
    if phase == "entities":
        nn = parsed.get("Nomological Network")
        keys = ("constructs", "measurements", "behaviors")
        if not (isinstance(nn, dict) or any(k in parsed for k in keys)):
            out["status"] = "wrong_schema"
            return out
    elif phase == "relationships":
        if not isinstance(parsed.get("relationships"), list):
            out["status"] = "wrong_schema"
            return out
    out["parsed"] = parsed
    return out


def submit_batch(client, jsonl_lines: list, description: str, provider: str = "together") -> str:
    """Write JSONL to temp file, upload, and create batch job. Returns job ID.

    Works with Together, OpenAI, and Google (via OpenAI-compat endpoint).
    """
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False, encoding="utf-8")
    for line in jsonl_lines:
        tmp.write(line + "\n")
    tmp.close()
    logger.info("Uploading %d requests from %s (%s, provider=%s)", len(jsonl_lines), tmp.name, description, provider)

    try:
        if provider == "together":
            file_resp = client.files.upload(file=Path(tmp.name), purpose="batch-api", check=False)
            file_id = file_resp.id
        else:
            # OpenAI and Google (via OpenAI-compat) use client.files.create
            with open(tmp.name, "rb") as f:
                file_resp = client.files.create(file=f, purpose="batch")
            file_id = file_resp.id
        logger.info("Uploaded file: %s", file_id)

        batch_resp = client.batches.create(
            input_file_id=file_id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
        )
        # Together wraps in .job, OpenAI/Google don't
        job_id = getattr(getattr(batch_resp, 'job', None), 'id', None) or batch_resp.id
        logger.info("Batch job created: %s", job_id)
        if getattr(batch_resp, 'warning', None):
            logger.warning("Batch warning: %s", batch_resp.warning)
    finally:
        os.unlink(tmp.name)

    return job_id


def _retry_call(fn, *, op: str, max_retries: int = 6, initial_backoff: float = 5.0):
    """Invoke fn() with exponential backoff on transient network errors."""
    backoff = initial_backoff
    last_exc = None
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            last_exc = e
            msg = str(e).lower()
            # Retry on DNS/socket/transient network errors
            transient = any(k in msg for k in (
                "connection", "nodename", "timeout", "timed out",
                "temporarily unavailable", "broken pipe", "reset by peer",
                "resolving", "resolve", "dns", "ssl", "eof occurred",
            ))
            if not transient and attempt > 0:
                # Non-transient; give up after first try
                raise
            if attempt == max_retries - 1:
                raise
            logger.warning(
                "%s attempt %d/%d failed: %s; sleeping %.1fs and retrying",
                op, attempt + 1, max_retries, str(e)[:120], backoff,
            )
            time.sleep(backoff)
            backoff = min(backoff * 2, 120.0)
    raise last_exc  # type: ignore[misc]


def _file_text(content) -> str:
    """Decode a files.content() response across provider SDKs."""
    if isinstance(content, bytes):
        return content.decode('utf-8')
    if hasattr(content, 'content') and isinstance(content.content, bytes):
        return content.content.decode('utf-8')
    if hasattr(content, 'text') and callable(content.text):
        return content.text()
    if hasattr(content, 'text'):
        return content.text
    if hasattr(content, 'read'):
        return content.read().decode('utf-8')
    return str(content)


def poll_batch(client, job_id: str, poll_interval: int = 15,
               raise_on_failure: bool = False, include_errors: bool = False) -> list:
    """Poll until batch completes, then download and parse results.

    Works with Together, OpenAI, and Google (via OpenAI-compat endpoint).
    Transient network errors during polling/download are retried with backoff.

    With raise_on_failure=False (the default) a failed, cancelled or expired
    job, or one with no output file, returns []. With raise_on_failure=True
    those cases raise BatchJobFailed instead.
    include_errors=True also downloads the job's error file (if any) and
    appends its lines, so failed requests can be counted.
    """
    if raise_on_failure or include_errors:
        return _poll_batch_strict(client, job_id, poll_interval,
                                  raise_on_failure=raise_on_failure,
                                  include_errors=include_errors)
    while True:
        status = _retry_call(
            lambda: client.batches.retrieve(job_id),
            op=f"batches.retrieve({job_id[:20]})",
        )
        st = status.status
        # Try to get progress info
        done = getattr(status, 'request_counts', None)
        if done:
            completed = getattr(done, 'completed', '?')
            total = getattr(done, 'total', '?')
            failed = getattr(done, 'failed', 0)
            logger.info("Batch %s: status=%s, completed=%s/%s (failed=%s)", job_id, st, completed, total, failed)
        else:
            logger.info("Batch %s: status=%s", job_id, st)

        st_lower = st.lower() if st else ""
        if st_lower == "completed":
            break
        elif st_lower in ("failed", "cancelled", "expired"):
            logger.error("Batch %s ended with status: %s", job_id, st)
            errors = getattr(status, 'errors', None)
            if errors:
                logger.error("Errors: %s", errors)
            return []

        time.sleep(poll_interval)

    output_file_id = status.output_file_id
    if not output_file_id:
        logger.error("No output file for batch %s", job_id)
        return []

    content = _retry_call(
        lambda: client.files.content(output_file_id),
        op=f"files.content({str(output_file_id)[:20]})",
    )
    text = _file_text(content)

    results = []
    for line in text.strip().split("\n"):
        if line.strip():
            results.append(json.loads(line))
    logger.info("Downloaded %d results from batch %s", len(results), job_id)
    return results


def _poll_batch_strict(client, job_id: str, poll_interval: int,
                       raise_on_failure: bool, include_errors: bool) -> list:
    """poll_batch with explicit failure handling (see poll_batch)."""
    while True:
        status = _retry_call(
            lambda: client.batches.retrieve(job_id),
            op=f"batches.retrieve({job_id[:20]})",
        )
        st = status.status
        done = getattr(status, 'request_counts', None)
        if done:
            logger.info("Batch %s: status=%s, completed=%s/%s (failed=%s)", job_id, st,
                        getattr(done, 'completed', '?'), getattr(done, 'total', '?'),
                        getattr(done, 'failed', 0))
        else:
            logger.info("Batch %s: status=%s", job_id, st)
        st_lower = str(getattr(st, "value", st) or "").lower()
        if st_lower == "completed":
            break
        if st_lower in ("failed", "cancelled", "canceled", "expired"):
            errors = getattr(status, 'errors', None) or getattr(status, 'error', None)
            logger.error("Batch %s ended with status: %s (%s)", job_id, st, errors)
            if raise_on_failure:
                raise BatchJobFailed(f"batch {job_id} ended with status {st}: {errors}")
            return []
        time.sleep(poll_interval)

    results = []
    output_file_id = getattr(status, "output_file_id", None)
    error_file_id = getattr(status, "error_file_id", None)
    if output_file_id:
        content = _retry_call(lambda: client.files.content(output_file_id),
                              op=f"files.content({str(output_file_id)[:20]})")
        for line in _file_text(content).strip().split("\n"):
            if line.strip():
                results.append(json.loads(line))
    if include_errors and error_file_id:
        content = _retry_call(lambda: client.files.content(error_file_id),
                              op=f"files.content({str(error_file_id)[:20]})")
        n_err = 0
        for line in _file_text(content).strip().split("\n"):
            if line.strip():
                results.append(json.loads(line))
                n_err += 1
        logger.warning("Batch %s: %d request(s) in the error file", job_id, n_err)
    if not output_file_id:
        logger.error("No output file for batch %s (error file: %s)", job_id, error_file_id)
        if raise_on_failure:
            raise BatchJobFailed(f"batch {job_id} completed with no output file "
                                 f"(error file: {error_file_id})")
    logger.info("Downloaded %d results from batch %s", len(results), job_id)
    return results


def submit_batch_google(jsonl_lines: list, description: str, model: str) -> str:
    """Submit a batch through the google-genai SDK. Returns the job name.

    The OpenAI-format lines are converted to Gemini inline requests: system and
    user messages are joined into one user turn; temperature and the token cap
    are carried over, other request-body fields are not.
    """
    from google.genai import types

    client = init_google_client()

    # Convert OpenAI-format JSONL lines to Gemini inline requests
    inline_requests = []

    for idx, line_str in enumerate(jsonl_lines):
        req = json.loads(line_str)
        custom_id = req["custom_id"]
        body = req["body"]
        messages = body.get("messages", [])

        # Combine system + user messages into a single user prompt
        parts = []
        for msg in messages:
            parts.append(msg["content"])
        combined_text = "\n\n".join(parts)

        gen_config = {}
        if "temperature" in body:
            gen_config["temperature"] = body["temperature"]
        max_tok_key = "max_completion_tokens" if "max_completion_tokens" in body else "max_tokens"
        if max_tok_key in body:
            gen_config["max_output_tokens"] = body[max_tok_key]

        inline_req = {
            "key": custom_id,
            "request": {
                "contents": [{"parts": [{"text": combined_text}], "role": "user"}],
            },
        }
        if gen_config:
            inline_req["request"]["generation_config"] = gen_config

        inline_requests.append(inline_req)

    logger.info("Submitting %d Google batch requests (%s, model=%s)", len(inline_requests), description, model)

    # Write to temp JSONL file and upload
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False, encoding="utf-8")
    for req in inline_requests:
        tmp.write(json.dumps(req, ensure_ascii=False) + "\n")
    tmp.close()

    try:
        uploaded_file = client.files.upload(
            file=tmp.name,
            config=types.UploadFileConfig(display_name=description, mime_type="jsonl"),
        )
        logger.info("Uploaded file: %s", uploaded_file.name)

        batch_job = client.batches.create(
            model=model,
            src=uploaded_file.name,
            config={"display_name": description},
        )
        job_name = batch_job.name
        logger.info("Google batch job created: %s", job_name)
    finally:
        os.unlink(tmp.name)

    return job_name


def _gemini_finish_reason(fr):
    """Map a Gemini finish reason to the OpenAI vocabulary ("MAX_TOKENS" -> "length")."""
    if fr is None:
        return None
    name = getattr(fr, "name", None) or str(fr)
    name = name.split(".")[-1].upper()
    return {"MAX_TOKENS": "length", "STOP": "stop"}.get(name, name.lower())


def _gemini_usage(prompt, candidates, thoughts) -> dict:
    """OpenAI-style usage from Gemini counts. Billed output = answer + thinking tokens."""
    prompt, candidates, thoughts = int(prompt or 0), int(candidates or 0), int(thoughts or 0)
    return {
        "prompt_tokens": prompt,
        "completion_tokens": candidates + thoughts,
        "completion_tokens_details": {"reasoning_tokens": thoughts},
    }


def _gemini_result(custom_id, text, finish_reason=None, usage=None) -> dict:
    body = {"choices": [{"message": {"content": text}}]}
    if finish_reason is not None:
        body["choices"][0]["finish_reason"] = finish_reason
    if usage is not None:
        body["usage"] = usage
    return {"custom_id": custom_id, "response": {"body": body}}


def poll_batch_google(job_name: str, poll_interval: int = 30,
                      raise_on_failure: bool = False) -> list:
    """Poll Google batch job until complete, convert results to OpenAI-compat format.

    Transient network errors during polling/download are retried with backoff
    so a brief DNS/connection blip doesn't lose the batch results.

    Each converted result carries choices[0].message.content plus
    (when Google reports them) choices[0].finish_reason ("length" for
    MAX_TOKENS) and an OpenAI-style usage block in which completion_tokens
    includes thinking tokens.

    raise_on_failure=False (default) returns [] for a failed, cancelled or
    expired job; True raises BatchJobFailed instead.
    """
    client = init_google_client()

    while True:
        batch_job = _retry_call(
            lambda: client.batches.get(name=job_name),
            op=f"google.batches.get({job_name[:20]})",
        )
        state = batch_job.state.name if hasattr(batch_job.state, 'name') else str(batch_job.state)
        logger.info("Google batch %s: state=%s", job_name, state)

        if state == "JOB_STATE_SUCCEEDED":
            break
        elif state in ("JOB_STATE_FAILED", "JOB_STATE_CANCELLED", "JOB_STATE_EXPIRED"):
            logger.error("Google batch %s ended with state: %s", job_name, state)
            if raise_on_failure:
                raise BatchJobFailed(f"Google batch {job_name} ended with state {state}: "
                                     f"{getattr(batch_job, 'error', None)}")
            return []

        time.sleep(poll_interval)

    # Download and convert results to OpenAI-compat format
    results = []

    # Try inline responses first
    dest = batch_job.dest
    if hasattr(dest, 'inlined_responses') and dest.inlined_responses:
        for resp in dest.inlined_responses:
            key = getattr(resp, 'key', '') or ''
            if hasattr(resp, 'response') and resp.response:
                # Extract text from Gemini response
                text = ""
                if hasattr(resp.response, 'text'):
                    text = resp.response.text or ""
                elif hasattr(resp.response, 'candidates') and resp.response.candidates:
                    parts = resp.response.candidates[0].content.parts
                    text = parts[0].text if parts else ""
                fr, usage = None, None
                try:
                    cands = getattr(resp.response, 'candidates', None) or []
                    if cands:
                        fr = _gemini_finish_reason(getattr(cands[0], 'finish_reason', None))
                    um = getattr(resp.response, 'usage_metadata', None)
                    if um is not None:
                        usage = _gemini_usage(getattr(um, 'prompt_token_count', 0),
                                              getattr(um, 'candidates_token_count', 0),
                                              getattr(um, 'thoughts_token_count', 0))
                except Exception:  # noqa: BLE001
                    pass
                results.append(_gemini_result(key, text, fr, usage))
            elif hasattr(resp, 'error') and resp.error:
                logger.warning("Google batch result error for %s: %s", key, resp.error)
                results.append({
                    "custom_id": key,
                    "response": {"body": {"choices": [{"message": {"content": _FAILED_SENTINEL}}]}},
                })
    # Try file-based results
    elif hasattr(dest, 'file_name') and dest.file_name:
        file_content = _retry_call(
            lambda: client.files.download(file=dest.file_name),
            op=f"google.files.download({dest.file_name[:20]})",
        )
        if isinstance(file_content, bytes):
            text = file_content.decode('utf-8')
        else:
            text = str(file_content)
        for line in text.strip().split("\n"):
            if not line.strip():
                continue
            results.append(gemini_file_line_to_result(json.loads(line)))

    logger.info("Downloaded %d results from Google batch %s", len(results), job_name)
    return results


def gemini_file_line_to_result(entry: dict) -> dict:
    """Convert one line of a Gemini batch output file to the OpenAI-compat result shape.

    The answer text joins every non-thought text part of the first candidate
    (the SDK's .text property does the same for inline results). A line with
    an error and no response becomes the _FAILED_SENTINEL content.
    """
    key = entry.get("key", "")
    response = entry.get("response") or {}
    if not response and entry.get("error"):
        logger.warning("Google batch result error for %s: %s", key, entry.get("error"))
        return {"custom_id": key,
                "response": {"body": {"choices": [{"message": {"content": _FAILED_SENTINEL}}]}}}
    resp_text, fr, usage = "", None, None
    if isinstance(response, dict):
        candidates = response.get("candidates", [])
        if candidates:
            parts = (candidates[0].get("content") or {}).get("parts", []) or []
            resp_text = "".join(p.get("text", "") or "" for p in parts
                                if isinstance(p, dict) and not p.get("thought"))
            fr = _gemini_finish_reason(candidates[0].get("finishReason"))
        um = response.get("usageMetadata")
        if isinstance(um, dict):
            usage = _gemini_usage(um.get("promptTokenCount"), um.get("candidatesTokenCount"),
                                  um.get("thoughtsTokenCount"))
    return _gemini_result(key, resp_text, fr, usage)


def make_client(provider: str, timeout: float = 600.0):
    """API client for batch submission and polling with ``provider``.

    together: the together SDK client (its batch API is not reachable through
    the OpenAI-compatible endpoint); openai: the OpenAI client; google: the
    OpenAI-compatible Gemini endpoint (Google batches go through
    submit_batch_google / poll_batch_google instead).
    """
    if provider == "together":
        from aiconstructlexis.providers.clients import init_together_sdk_client

        return init_together_sdk_client(timeout=timeout)
    if provider == "openai":
        return init_openai_client()
    if provider == "google":
        return init_google_openai_compatible_client()
    raise ValueError(f"Unknown provider: {provider}")


def majority_vote_entities(trials_by_paper, n_trials, name_mapping, threshold=None):
    """Vote on entities per paper. Returns {paper_name: {constructs, measurements, behaviors}}.

    Names are compared lower-cased and through ``name_mapping`` so that surface
    variants of one concept count as one vote; the longest entity record of a
    kept name is returned. threshold=None means a strict majority of
    ``n_trials``; threshold=1 gives the union.
    """
    from collections import Counter

    if threshold is None:
        threshold = (n_trials // 2) + 1
    voted = {}

    for paper_name, trials in trials_by_paper.items():
        paper_result = {}
        for etype in ("constructs", "measurements", "behaviors"):
            canon_counts = Counter()
            canon_to_best = {}
            for trial_parsed in trials:
                nomnet = trial_parsed.get("Nomological Network") or {
                    k: trial_parsed.get(k, []) for k in ("constructs", "measurements", "behaviors")
                }
                entities = nomnet.get(etype, [])
                seen = set()
                for ent in entities:
                    # A model occasionally returns a bare string instead of an entity object.
                    if isinstance(ent, str):
                        raw = ent.strip()
                    elif isinstance(ent, dict):
                        raw = (ent.get("name", "") or "").strip()
                    else:
                        continue
                    if not raw:
                        continue
                    canon = name_mapping.get(raw.lower(), raw.lower())
                    if canon in seen:
                        continue
                    seen.add(canon)
                    canon_counts[canon] += 1
                    if canon not in canon_to_best or len(json.dumps(ent)) > len(json.dumps(canon_to_best[canon])):
                        canon_to_best[canon] = ent

            kept = [canon_to_best[c] for c, cnt in canon_counts.items() if cnt >= threshold]
            paper_result[etype] = kept
            logger.debug("%s / %s: %d unique, %d voted (threshold=%d)",
                         paper_name[:40], etype, len(canon_counts), len(kept), threshold)

        voted[paper_name] = paper_result
        c, m, b = len(paper_result["constructs"]), len(paper_result["measurements"]), len(paper_result["behaviors"])
        logger.info("[%s] voted entities: C=%d M=%d B=%d", paper_name[:50], c, m, b)

    return voted


def majority_vote_relationships(trials_by_paper, n_trials, name_mapping, threshold=None):
    """Vote on relationships per paper, keyed by (source, target, type) after
    lower-casing and name mapping; the record with the longest evidence is kept.
    threshold=None means a strict majority of ``n_trials``; threshold=1 gives the union."""
    from collections import Counter

    if threshold is None:
        threshold = (n_trials // 2) + 1
    voted = {}

    for paper_name, trials in trials_by_paper.items():
        key_counts = Counter()
        key_to_best = {}
        for trial_rels in trials:
            seen = set()
            for rel in trial_rels:
                src = name_mapping.get((rel.get("source", "") or "").strip().lower(),
                                       (rel.get("source", "") or "").strip().lower())
                tgt = name_mapping.get((rel.get("target", "") or "").strip().lower(),
                                       (rel.get("target", "") or "").strip().lower())
                rtype = (rel.get("type", "") or "").strip().lower()
                key = (src, tgt, rtype)
                if key in seen:
                    continue
                seen.add(key)
                key_counts[key] += 1
                if key not in key_to_best or len(str(rel.get("evidence", ""))) > len(str(key_to_best[key].get("evidence", ""))):
                    key_to_best[key] = rel

        kept = [key_to_best[k] for k, cnt in key_counts.items() if cnt >= threshold]
        voted[paper_name] = kept
        logger.info("[%s] voted relationships: %d", paper_name[:50], len(kept))

    return voted
