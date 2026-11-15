"""Multi-model extraction with a majority vote across models.

Every paper is sent once to each model of a panel, in two passes (entities, then
relationships among each model's own entities), through the providers' batch
APIs. An entity is kept for a paper when at least ``vote_threshold`` models
propose it (default 2, the ``voting.threshold`` of a pipeline config; names
compared lower-cased). Relationships are kept as the union over models; the
per-venue relationship vote, with the same threshold, happens later at the
canonical-entity level.

Inputs
  papers_json   a screened paper list (``name``, ``path`` to the PDF, ``url``,
                ``is_LLM_paper``); only flagged papers are extracted.
  models        the panel, required: ``{provider, model, label[, temperature,
                max_tokens, price]}`` entries (the ``extraction.models`` of a
                pipeline config), or ``provider:model:label`` specs on the
                command line. Callers of ``run_extraction`` may add two more
                keys per model: ``send_temperature`` (False omits the
                temperature from the request) and ``extra_body`` (a dict
                merged into the request body); a pipeline config does not
                accept them.
  prompts       the prompt set (``aiconstructlexis.prompts``; "default").

Outputs under ``work_dir``
  trials/<label>/entity_trials.json          {paper: [parsed entity output]}
  trials/<label>/relationship_trials.json    {paper: [[relationship, ...]]}
  trials/<label>/meta.json                   model, prompt fingerprint, settings
  trials/merged_{entity,relationship}_trials.json   all models' trials per paper
  inputs/extraction.json                     the voted per-paper extraction
  run_report.json (+ run_reports/<run>.json) per-model, per-pass counts
  batch_jobs.json                            submitted job ids
  dry_run/                                   request files and estimates (dry run)

Rules
  * Fail loud. A batch that fails to submit, fails while polling, or leaves a
    requested paper without usable output stops the run with
    ExtractionIncomplete after saving whatever did succeed; nothing is written
    for a model that produced nothing. ``allow_partial`` logs the gaps and
    continues.
  * Per-paper cache. Trials files are reused for the papers they cover and
    only missing papers are requested, so an interrupted run is resumed by
    running it again.
  * Cache consistency. ``meta.json`` records the model and the prompt
    fingerprint (sha256 of the prompt template and system message) of each
    pass; trials made with a different model or prompt set are refused rather
    than mixed into the vote.
  * Paper text is limited to the venue's main-text page count
    (``CONFERENCE_PAGE_LIMITS``, shared with the screening stage), detected
    from the paper-list path or given explicitly; a venue not in the table
    reads ``DEFAULT_PAGE_LIMIT`` pages, as screening does.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from aiconstructlexis.extract.batch import (
    BATCH_FILE_LIMITS,
    _is_reasoning_model,
    build_entity_jsonl,
    build_relationship_jsonl,
    classify_result,
    describe_extraction_prompts,
    estimate_tokens,
    extract_text,
    load_papers,
    majority_vote_entities,
    majority_vote_relationships,
    make_client,
    poll_batch,
    poll_batch_google,
    submit_batch,
    submit_batch_google,
)
from aiconstructlexis.prompts import DEFAULT_PROMPT_SET
from aiconstructlexis.screen._common import CONFERENCE_PAGE_LIMITS, DEFAULT_PAGE_LIMIT
from aiconstructlexis.util.json_tools import split_jsonl_lines
from aiconstructlexis.util.logging import get_run_id, log_counts, log_step, setup_logging

logger = logging.getLogger(__name__)

PROVIDERS = ("google", "openai", "together")
PHASES = ("entities", "relationships")
DEFAULT_MAX_TOKENS = 16384
DEFAULT_VOTE_THRESHOLD = 2

_MODEL_CFG_KEYS = {"provider", "model", "label", "temperature", "max_tokens",
                   "send_temperature", "extra_body", "price"}
_LABEL_RE = re.compile(r"^[A-Za-z0-9_.-]+$")


class ExtractionIncomplete(RuntimeError):
    """The run stopped because a batch failed or papers lack usable output."""


class CacheMismatch(ExtractionIncomplete):
    """A trials cache was produced with a different model or prompt."""


# ---------------------------------------------------------------------------
# Model list
# ---------------------------------------------------------------------------

def _auto_label(model: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", model.split("/")[-1].lower()).strip("_")


def parse_model_spec(spec: str) -> dict:
    """Parse 'provider:model:label' (or 'provider:model', label derived).

    The provider is the first field and the label the last; anything between
    is the model string, so model names may contain ':' when a label is given.
    """
    parts = spec.strip().split(":")
    if len(parts) < 2 or not all(parts):
        raise ValueError(f"Bad model spec {spec!r}; expected provider:model:label")
    if len(parts) == 2:
        provider, model = parts
        label = _auto_label(model)
    else:
        provider, label = parts[0], parts[-1]
        model = ":".join(parts[1:-1])
    return {"provider": provider.strip().lower(), "model": model.strip(), "label": label.strip()}


def validate_models(models: list) -> list:
    if not models:
        raise ValueError("No extraction panel given: models must list at least one "
                         "{provider, model, label} entry (extraction.models in a pipeline config)")
    seen = set()
    for m in models:
        unknown = set(m) - _MODEL_CFG_KEYS
        if unknown:
            raise ValueError(f"Unknown model config key(s) {sorted(unknown)} in {m}")
        for k in ("provider", "model", "label"):
            if not isinstance(m.get(k), str) or not m[k]:
                raise ValueError(f"Model config needs a non-empty {k!r}: {m}")
        if m["provider"] not in PROVIDERS:
            raise ValueError(f"Unknown provider {m['provider']!r} in {m}; expected one of {PROVIDERS}")
        if not _LABEL_RE.match(m["label"]):
            raise ValueError(f"Label {m['label']!r} must match {_LABEL_RE.pattern} (it names a directory)")
        if m["label"] in seen:
            raise ValueError(f"Duplicate model label {m['label']!r}")
        seen.add(m["label"])
        if m.get("extra_body") is not None and not isinstance(m["extra_body"], dict):
            raise ValueError(f"extra_body must be an object in {m}")
        if m.get("price") is not None:
            p = m["price"]
            if not (isinstance(p, (list, tuple)) and len(p) == 2):
                raise ValueError(f"price must be [input, output] per million tokens in {m}")
    return models


def parse_model_specs(values: list) -> list:
    """--models values: provider:model:label entries, space or comma separated."""
    specs = [s for v in values for s in v.split(",") if s.strip()]
    return validate_models([parse_model_spec(s) for s in specs])


def normalize_models(models) -> list:
    """Model configs from a list of config dicts or of ``provider:model:label`` strings."""
    if not models:
        return validate_models([])
    if isinstance(models, (str, Path)) or not isinstance(models, (list, tuple)):
        raise ValueError(f"models must be a list of model configs or provider:model:label specs, "
                         f"got {type(models).__name__}")
    if all(isinstance(m, str) for m in models):
        return parse_model_specs(list(models))
    return validate_models([dict(m) for m in models])


def model_settings(cfg: dict, temperature: float, max_tokens: int) -> dict:
    """Effective per-model request settings (config overrides, else the run defaults)."""
    send_t = cfg.get("send_temperature")
    return {
        "temperature": cfg.get("temperature", temperature),
        "max_tokens": int(cfg.get("max_tokens", max_tokens)),
        "send_temperature": send_t,
        "temperature_sent": (not _is_reasoning_model(cfg["model"])) if send_t is None else bool(send_t),
        "extra_body": cfg.get("extra_body"),
    }


def model_price(cfg: dict):
    """(input, output) USD per million tokens from the model config, or None when it has no price."""
    if cfg.get("price") is None:
        return None
    return tuple(cfg["price"])


# ---------------------------------------------------------------------------
# Result processing and the run report
# ---------------------------------------------------------------------------

STAT_KEYS = ("requests_sent", "results_received", "missing_results", "unexpected_results",
             "duplicate_results", "request_errors", "empty_outputs", "parse_failures",
             "wrong_schema", "truncated_outputs", "think_stripped", "leading_text",
             "reasoning_field", "usable", "input_tokens", "output_tokens", "reasoning_tokens")


def new_stats() -> dict:
    s = {k: 0 for k in STAT_KEYS}
    s["finish_reasons"] = {}
    return s


def _paper_of(custom_id: str) -> str:
    try:
        return json.loads(custom_id).get("paper", "")
    except (json.JSONDecodeError, AttributeError):
        return ""


def process_phase_results(phase: str, results: list, sent_ids) -> tuple[dict, dict, list]:
    """Classify a phase's raw results against the custom_ids that were sent.

    Returns (usable_by_paper, stats, problem_papers):
      usable_by_paper  {paper: [trial]}; an entity trial is the parsed dict, a
                       relationship trial is its list of relationship dicts;
      stats            counts for the run report (see STAT_KEYS), finish_reasons
                       and truncated_papers;
      problem_papers   sorted papers that were sent but have no usable output.
    """
    sent_ids = list(sent_ids)
    sent = set(sent_ids)
    stats = new_stats()
    stats["requests_sent"] = len(sent)
    finish = Counter()
    seen, usable, truncated = set(), {}, set()
    status_key = {"request_error": "request_errors", "empty": "empty_outputs",
                  "parse_failed": "parse_failures", "wrong_schema": "wrong_schema", "ok": "usable"}
    for r in results:
        cid = r.get("custom_id", "")
        if cid not in sent:
            stats["unexpected_results"] += 1
            continue
        if cid in seen:
            stats["duplicate_results"] += 1
            continue
        seen.add(cid)
        stats["results_received"] += 1
        c = classify_result(r, phase)
        stats[status_key[c["status"]]] += 1
        if c["truncated"]:
            truncated.add(_paper_of(cid))
        for flag, key in (("truncated", "truncated_outputs"), ("think_stripped", "think_stripped"),
                          ("leading_text", "leading_text"), ("reasoning_field", "reasoning_field")):
            if c[flag]:
                stats[key] += 1
        stats["input_tokens"] += c["usage"]["input"]
        stats["output_tokens"] += c["usage"]["output"]
        stats["reasoning_tokens"] += c["usage"]["reasoning"]
        finish[str(c["finish_reason"])] += 1
        if c["status"] == "ok":
            trial = c["parsed"]
            if phase == "relationships":
                trial = [x for x in trial.get("relationships", []) if isinstance(x, dict)]
            usable.setdefault(_paper_of(cid), []).append(trial)
    stats["missing_results"] = len(sent - seen)
    stats["finish_reasons"] = dict(finish)
    stats["truncated_papers"] = sorted(truncated)
    problem = sorted({_paper_of(cid) for cid in sent_ids} - set(usable))
    return usable, stats, problem


def add_cost(stats: dict, price) -> dict:
    """Set stats['est_cost_usd'] from token counts and (input, output) USD per million."""
    if not price:
        stats["est_cost_usd"] = None
    else:
        stats["est_cost_usd"] = round(stats["input_tokens"] / 1e6 * price[0]
                                      + stats["output_tokens"] / 1e6 * price[1], 4)
    return stats


# ---------------------------------------------------------------------------
# Per-paper trials cache
# ---------------------------------------------------------------------------

TRIAL_FILES = {"entities": "entity_trials.json", "relationships": "relationship_trials.json"}


def _atomic_write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def usable_entity_trial(t) -> bool:
    if not isinstance(t, dict):
        return False
    if set(t) == {"error"}:
        return False
    return isinstance(t.get("Nomological Network"), dict) or any(
        k in t for k in ("constructs", "measurements", "behaviors"))


def covered_papers(phase: str, cache: dict) -> set:
    """Papers a cached trials dict covers with a usable output."""
    if phase == "entities":
        return {p for p, trials in cache.items()
                if isinstance(trials, list) and any(usable_entity_trial(t) for t in trials)}
    return {p for p, trials in cache.items()
            if isinstance(trials, list) and any(isinstance(t, list) for t in trials)}


def load_trials_cache(work_dir: Path, cfg: dict, phase: str, prompt_info: dict) -> tuple[dict, bool]:
    """Load trials/<label>/<phase file> if present, applying the cache-consistency rule.

    Trials are reused only when meta.json records the same model and the same
    prompt fingerprint for the phase as this run; otherwise CacheMismatch is
    raised. Returns (cache, unfingerprinted): a trials file without a meta.json
    entry for the phase has no fingerprint; it is accepted for the default
    prompt set (with a warning) and refused for any other.
    """
    model_dir = work_dir / "trials" / cfg["label"]
    path = model_dir / TRIAL_FILES[phase]
    meta_path = model_dir / "meta.json"
    meta = json.load(open(meta_path, encoding="utf-8")) if meta_path.exists() else {}
    if meta.get("model") and meta["model"] != cfg["model"]:
        raise CacheMismatch(
            f"{model_dir} holds trials from model {meta['model']!r}, but label {cfg['label']!r} "
            f"now points to {cfg['model']!r}. Use another work directory or another label.")
    if not path.exists():
        return {}, False
    pmeta = (meta.get("phases") or {}).get(phase)
    prompt_set = prompt_info["prompt_set"]
    want = prompt_info[phase]
    if pmeta is None:
        if prompt_set != DEFAULT_PROMPT_SET:
            raise CacheMismatch(
                f"{path} has no prompt metadata (assumed to come from the {DEFAULT_PROMPT_SET} "
                f"prompt set) but this run uses prompt set {prompt_set}. Use another work "
                f"directory for the {prompt_set} run.")
        logger.warning("[%s] %s has no meta.json entry; assuming the %s prompt set",
                       cfg["label"], path.name, DEFAULT_PROMPT_SET)
    else:
        same = (pmeta.get("prompt_set") == prompt_set
                and pmeta.get("prompt_sha256") == want["prompt_sha256"]
                and pmeta.get("system_sha256") == want["system_sha256"])
        if not same:
            raise CacheMismatch(
                f"{path} was produced with prompt set {pmeta.get('prompt_set')} "
                f"(sha {pmeta.get('prompt_sha256')}), this run uses {prompt_set} "
                f"(sha {want['prompt_sha256']}). Use another work directory, or move the "
                f"old trials away.")
    try:
        with open(path) as f:
            cache = json.load(f)
    except json.JSONDecodeError as e:
        raise CacheMismatch(f"{path} is not valid JSON ({e}); move it away and rerun") from e
    if not isinstance(cache, dict):
        raise CacheMismatch(f"{path} is not a {{paper: trials}} object")
    return cache, pmeta is None


def write_trials_meta(work_dir: Path, cfg: dict, phase: str, prompt_info: dict, settings: dict,
                      n_papers: int, unfingerprinted: bool = False) -> None:
    """Record model, prompt fingerprint and request settings for a phase's trials file.

    unfingerprinted=True notes that the file also holds entries that were made
    without prompt metadata.
    """
    model_dir = work_dir / "trials" / cfg["label"]
    meta_path = model_dir / "meta.json"
    meta = json.load(open(meta_path, encoding="utf-8")) if meta_path.exists() else {}
    meta.update({"label": cfg["label"], "provider": cfg["provider"], "model": cfg["model"]})
    meta.setdefault("phases", {})[phase] = {
        "prompt_set": prompt_info["prompt_set"],
        "prompt_module": prompt_info["module"],
        "prompt_sha256": prompt_info[phase]["prompt_sha256"],
        "system_sha256": prompt_info[phase]["system_sha256"],
        "temperature": settings["temperature"] if settings["temperature_sent"] else None,
        "max_tokens": settings["max_tokens"],
        "extra_body": settings["extra_body"],
        "papers": n_papers,
        "includes_unfingerprinted_entries": bool(unfingerprinted) or bool(
            ((meta.get("phases") or {}).get(phase) or {}).get("includes_unfingerprinted_entries")),
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    _atomic_write_json(meta_path, meta)


# ---------------------------------------------------------------------------
# Batch submission and polling
# ---------------------------------------------------------------------------

def _phase_tag(phase: str) -> str:
    return "entities" if phase == "entities" else "rels"


def plan_parts(provider: str, lines: list) -> list:
    """Split a request list into batch files within the provider's limits."""
    if provider in BATCH_FILE_LIMITS:
        max_bytes, max_requests = BATCH_FILE_LIMITS[provider]
        return split_jsonl_lines(lines, max_bytes, max_requests)
    return [lines] if lines else []


def new_job_record(cfg: dict, phase: str, lines: list) -> dict:
    return {"label": cfg["label"], "phase": phase, "provider": cfg["provider"],
            "model": cfg["model"], "n_requests": len(lines), "jobs": [], "client": None}


def submit_model_phase(cfg: dict, phase: str, lines: list, rec: dict | None = None) -> dict:
    """Submit one model's requests for a phase (split into parts within the
    provider's file limits). Job ids are appended to rec["jobs"] as each part
    is accepted, so a failure on a later part keeps the earlier ids.

    Raises on any submission error (the caller decides what to do).
    """
    provider, model, label = cfg["provider"], cfg["model"], cfg["label"]
    desc = f"{_phase_tag(phase)}-{label}"
    rec = rec if rec is not None else new_job_record(cfg, phase, lines)
    if provider == "google":
        rec["jobs"].append(submit_batch_google(lines, desc, model))
        return rec
    rec["client"] = make_client(provider)
    parts = plan_parts(provider, lines)
    for i, part in enumerate(parts, 1):
        d = desc if len(parts) == 1 else f"{desc}-p{i}of{len(parts)}"
        rec["jobs"].append(submit_batch(rec["client"], part, d, provider=provider))
    return rec


def poll_job(rec: dict, job_id: str) -> list:
    if rec["provider"] == "google":
        return poll_batch_google(job_id, poll_interval=30, raise_on_failure=True)
    return poll_batch(rec["client"], job_id, poll_interval=20,
                      raise_on_failure=True, include_errors=True)


def _record_jobs(work_dir: Path, records: list) -> None:
    """Append submitted job ids to <work_dir>/batch_jobs.json right away, so an
    interruption while polling does not lose them."""
    path = work_dir / "batch_jobs.json"
    data = json.load(open(path, encoding="utf-8")) if path.exists() else []
    for r in records:
        data.append({k: v for k, v in r.items() if k != "client"}
                    | {"run_id": get_run_id(),
                       "submitted_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    _atomic_write_json(path, data)


def run_phase_batches(phase: str, work: dict, work_dir: Path, workers: int = 5) -> dict:
    """Submit every model's batch for a phase, then poll the jobs, up to
    ``workers`` at a time.

    work: {label: (cfg, lines)}. Returns {label: {"results": [...],
    "jobs": [...], "errors": [...]}}. Errors are collected, not raised.
    """
    out = {label: {"results": [], "jobs": [], "errors": []} for label in work}
    records = {}
    for label, (cfg, lines) in work.items():
        logger.info("[%s] Submitting %s batch: %d requests", label, phase, len(lines))
        rec = new_job_record(cfg, phase, lines)
        try:
            submit_model_phase(cfg, phase, lines, rec)
        except Exception as e:  # noqa: BLE001
            logger.error("[%s] %s batch submit failed: %s", label, phase, e)
            out[label]["errors"].append(f"submit failed: {type(e).__name__}: {e}")
        if rec["jobs"]:
            records[label] = rec
            out[label]["jobs"] = list(rec["jobs"])
    if records:
        _record_jobs(work_dir, list(records.values()))

    tasks = [(label, rec, job_id) for label, rec in records.items() for job_id in rec["jobs"]]
    if not tasks:
        return out

    def _poll(task):
        label, rec, job_id = task
        try:
            return label, job_id, poll_job(rec, job_id), None
        except Exception as e:  # noqa: BLE001
            return label, job_id, [], f"poll failed for {job_id}: {type(e).__name__}: {e}"

    with ThreadPoolExecutor(max_workers=min(workers, len(tasks))) as ex:
        for label, job_id, results, err in ex.map(_poll, tasks):
            if err:
                logger.error("[%s] %s %s", label, phase, err)
                out[label]["errors"].append(err)
            elif not results:
                msg = f"batch {job_id} returned no results"
                logger.error("[%s] %s %s", label, phase, msg)
                out[label]["errors"].append(msg)
            else:
                logger.info("[%s] %s batch %s done: %d results", label, phase, job_id, len(results))
            out[label]["results"].extend(results)
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def merge_trials(all_entity_trials, all_rel_trials):
    """Merge per-model trial dicts into unified trial lists per paper.
    Each model's output becomes one 'trial' in the combined list."""
    merged_entities = {}
    for model_trials in all_entity_trials:
        for paper, trials in model_trials.items():
            merged_entities.setdefault(paper, []).extend(trials)

    merged_rels = {}
    for model_trials in all_rel_trials:
        for paper, trials in model_trials.items():
            merged_rels.setdefault(paper, []).extend(trials)

    return merged_entities, merged_rels


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Multi-model extraction: each paper to every model of the panel, two passes, "
                    "then a majority vote across models.")
    parser.add_argument("--papers-json", required=True,
                        help="Paper list JSON (name, path, url, is_LLM_paper); only flagged papers run")
    parser.add_argument("--work-dir", required=True,
                        help="Output directory (trials/, inputs/, run_report.json)")
    parser.add_argument("--temperature", type=float, default=0)
    parser.add_argument("--max-papers", type=int, default=0, help="Only the first N papers (0 = all)")
    parser.add_argument("--workers", type=int, default=5,
                        help="Threads for PDF text extraction and for polling the submitted batch "
                             "jobs (default 5)")
    parser.add_argument("--conference", default="auto",
                        help="Venue name for the main-text page limit (default: detected from the "
                             f"paper-list path; unknown venues read {DEFAULT_PAGE_LIMIT} pages, as in "
                             "screening)")
    parser.add_argument("--vote-threshold", type=int, default=DEFAULT_VOTE_THRESHOLD,
                        help="Models that must propose an entity for a paper before it is kept "
                             f"(default {DEFAULT_VOTE_THRESHOLD}; 1 keeps every proposal)")
    parser.add_argument("--prompts", default=DEFAULT_PROMPT_SET,
                        help="Prompt set: 'default' or a dotted module path defining the same constants")
    parser.add_argument("--models", nargs="+", required=True,
                        help="The extraction panel: provider:model:label entries (space or comma "
                             "separated); the label names the model's trials directory")
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS,
                        help=f"Output-token cap per request (default {DEFAULT_MAX_TOKENS})")
    parser.add_argument("--allow-partial", action="store_true",
                        help="Keep going when a batch fails or papers lack usable output")
    parser.add_argument("--dry-run", action="store_true",
                        help="Build the batch request files and estimate tokens; submit nothing")
    parser.add_argument("--log-dir", default="logs", help="Directory for the run log (default: logs)")
    return parser


def _write_report(work_dir: Path, report: dict) -> Path:
    report["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    path = work_dir / "run_report.json"
    _atomic_write_json(path, report)
    hist = work_dir / "run_reports" / f"run_{time.strftime('%Y%m%d_%H%M%S')}_{get_run_id()}.json"
    _atomic_write_json(hist, report)
    return path


def _log_phase_table(phase: str, per_model: dict) -> None:
    logger.info("Run report, %s:", phase)
    logger.info("  %-18s %6s %6s %6s %5s %5s %5s %5s %5s %6s %10s %10s %9s",
                "model", "sent", "recv", "usable", "miss", "err", "empty", "parse", "trunc",
                "leak", "in_tok", "out_tok", "cost$")
    for label, rep in per_model.items():
        s = rep.get(phase)
        if not s:
            continue
        cost = s.get("est_cost_usd")
        logger.info("  %-18s %6d %6d %6d %5d %5d %5d %5d %5d %6d %10d %10d %9s",
                    label[:18], s["requests_sent"], s["results_received"], s["usable"],
                    s["missing_results"], s["request_errors"], s["empty_outputs"],
                    s["parse_failures"] + s["wrong_schema"], s["truncated_outputs"],
                    s["leading_text"], s["input_tokens"], s["output_tokens"],
                    "n/a" if cost is None else f"{cost:.2f}")


_PHASE_HINT = ("Usable outputs were saved; rerun to request only the missing papers, or set "
               "allow_partial (--allow-partial) to accept the gaps.")


def _fail_or_warn(problems: list, allow_partial: bool, work_dir: Path, report: dict, where: str):
    if not problems:
        return
    for p in problems:
        logger.error("%s: %s", where, p)
    if allow_partial:
        logger.warning("allow_partial: continuing despite %d problem(s) in %s", len(problems), where)
        report.setdefault("accepted_problems", []).extend(problems)
        return
    report["status"] = "failed"
    report["failures"] = problems
    path = _write_report(work_dir, report)
    raise ExtractionIncomplete(
        f"{where}: {len(problems)} problem(s); stopping before anything else is written. "
        f"{_PHASE_HINT} Details: {path}\n  - " + "\n  - ".join(problems[:20]))


def _dry_run(models, papers, paper_texts, work_dir, prompts, prompt_info, caches,
             temperature, max_tokens) -> dict:
    """Write the request JSONL files each model would submit and estimate tokens/cost."""
    out_dir = work_dir / "dry_run"
    rep = {"status": "dry_run", "prompt": prompt_info, "per_model": {}, "token_method": None}
    print(f"\nDRY RUN: nothing submitted. Request files under {out_dir}")
    print(f"{'model':<18} {'phase':<13} {'requests':>8} {'files':>5} {'MB':>8} "
          f"{'in_tokens':>12} {'in_cost$':>9} {'out_cap_cost$':>13}")
    for cfg in models:
        label = cfg["label"]
        st = model_settings(cfg, temperature, max_tokens)
        price = model_price(cfg)
        ent_cache = caches[label]["entities"]
        covered_e = covered_papers("entities", ent_cache)
        pending_e = [p for p in papers if paper_texts[p["name"]].strip() and p["name"] not in covered_e]
        lines_by_phase = {"entities": build_entity_jsonl(
            pending_e, paper_texts, cfg["model"], st["temperature"], 1,
            prompts=prompts, max_tokens=st["max_tokens"],
            send_temperature=st["send_temperature"], extra_body=st["extra_body"])}

        # Relationship requests: exact for papers whose entities are cached,
        # approximate (empty entity list) for papers whose entities are not known yet.
        usable_e = {p: [t for t in ent_cache[p] if usable_entity_trial(t)] for p in covered_e}
        model_entities = majority_vote_entities(usable_e, 1, {}, threshold=1) if usable_e else {}
        covered_r = (covered_papers("relationships", caches[label]["relationships"])
                     - {p["name"] for p in pending_e})
        rel_papers = [p for p in papers if paper_texts[p["name"]].strip() and p["name"] not in covered_r]
        placeholder = {"constructs": [], "measurements": [], "behaviors": [], "_placeholder": True}
        ents_for_rel = {p["name"]: model_entities.get(p["name"], placeholder) for p in rel_papers}
        n_approx = sum(1 for p in rel_papers if p["name"] not in model_entities)
        lines_by_phase["relationships"] = build_relationship_jsonl(
            rel_papers, paper_texts, ents_for_rel, cfg["model"], st["temperature"], 1,
            prompts=prompts, max_tokens=st["max_tokens"],
            send_temperature=st["send_temperature"], extra_body=st["extra_body"])

        rep["per_model"][label] = {"provider": cfg["provider"], "model": cfg["model"],
                                   "price_per_m": price, "settings": st}
        for phase, lines in lines_by_phase.items():
            parts = plan_parts(cfg["provider"], lines)
            files = []
            for i, part in enumerate(parts, 1):
                name = f"{phase}.jsonl" if len(parts) == 1 else f"{phase}.part{i}.jsonl"
                fp = out_dir / label / name
                fp.parent.mkdir(parents=True, exist_ok=True)
                fp.write_text("".join(ln + "\n" for ln in part), encoding="utf-8")
                files.append(str(fp))
            n_tok, method = 0, None
            for ln in lines:
                body = json.loads(ln)["body"]
                t, method = estimate_tokens("\n".join(m["content"] for m in body["messages"]))
                n_tok += t
            rep["token_method"] = rep["token_method"] or method
            size_mb = sum(len(ln.encode("utf-8")) + 1 for ln in lines) / 1e6
            in_cost = round(n_tok / 1e6 * price[0], 4) if price else None
            cap_cost = round(len(lines) * st["max_tokens"] / 1e6 * price[1], 4) if price else None
            entry = {"requests": len(lines), "files": files, "size_mb": round(size_mb, 2),
                     "est_input_tokens": n_tok, "est_input_cost_usd": in_cost,
                     "output_cost_cap_usd": cap_cost,
                     "cached_papers": len(covered_e if phase == "entities" else covered_r)}
            if phase == "relationships":
                entry["approximate_requests"] = n_approx
            rep["per_model"][label][phase] = entry
            fmt = lambda v: "n/a" if v is None else f"{v:.2f}"  # noqa: E731
            print(f"{label[:18]:<18} {phase:<13} {len(lines):>8} {len(parts):>5} {size_mb:>8.1f} "
                  f"{n_tok:>12,} {fmt(in_cost):>9} {fmt(cap_cost):>13}")
    print(f"Token estimate method: {rep['token_method'] or 'n/a'}. Relationship requests for papers "
          f"without entities yet use an empty entity list (approximate).")
    _atomic_write_json(out_dir / "dry_run_report.json", rep)
    print(f"Dry-run report: {out_dir / 'dry_run_report.json'}\n")
    return rep


def page_limit(papers_json, conference: str = "auto") -> tuple[str, int]:
    """(venue, max_pages) for a run: the venue is given, or detected from the
    paper-list path; a venue not in ``CONFERENCE_PAGE_LIMITS`` reads
    ``DEFAULT_PAGE_LIMIT`` pages, the same count the screening stage reads."""
    conf = (conference or "auto").lower()
    if conf == "auto":
        p_lower = str(papers_json).lower()
        conf = next((c for c in CONFERENCE_PAGE_LIMITS if c in p_lower), "")
    return conf, CONFERENCE_PAGE_LIMITS.get(conf, DEFAULT_PAGE_LIMIT)


def run_extraction(papers_json, work_dir, models, temperature: float = 0,
                   max_tokens: int = DEFAULT_MAX_TOKENS, workers: int = 5, max_papers: int = 0,
                   allow_partial: bool = False, dry_run: bool = False,
                   prompts: str = DEFAULT_PROMPT_SET, conference: str = "auto",
                   vote_threshold: int = DEFAULT_VOTE_THRESHOLD) -> Path:
    """Run the multi-model extraction and return the path of ``<work_dir>/inputs/extraction.json``.

    papers_json    paper list JSON; only entries flagged ``is_LLM_paper`` run.
    work_dir       output directory (see the module docstring for its layout).
    models         the panel: a list of model config dicts or of
                   ``provider:model:label`` strings; ValueError when empty.
    temperature, max_tokens   request defaults; a model config may override them.
    workers        threads for PDF text extraction and for polling the submitted
                   batch jobs (at least 1).
    max_papers     only the first N papers (0 = all).
    allow_partial  continue past failed batches and papers without usable output.
    dry_run        write the request files and estimates under ``dry_run/`` and
                   submit nothing; returns the dry-run report path.
    prompts        prompt set name ("default" or a dotted module path).
    conference     venue for the main-text page limit ("auto" detects it from the path).
    vote_threshold models that must propose an entity for a paper before it is
                   kept (``voting.threshold`` of a pipeline config); between 1
                   and the panel size.

    Raises ExtractionIncomplete (or its subclass CacheMismatch) when the run
    cannot complete and ``allow_partial`` is False.
    """
    models = normalize_models(models)
    if workers < 1:
        raise ValueError(f"workers must be at least 1, got {workers}")
    if not 1 <= vote_threshold <= len(models):
        raise ValueError(f"{len(models)} model(s) cannot reach vote_threshold={vote_threshold}; "
                         f"it must be between 1 and the panel size")
    prompts = prompts or DEFAULT_PROMPT_SET

    prompt_info = describe_extraction_prompts(prompts)
    logger.info("Prompt set %s (%s): entities sha %s, relationships sha %s", prompt_info["prompt_set"],
                prompt_info["module"], prompt_info["entities"]["prompt_sha256"],
                prompt_info["relationships"]["prompt_sha256"])
    logger.info("Models: %s", ", ".join(f"{m['label']}={m['provider']}:{m['model']}" for m in models))
    for m in models:
        if m["provider"] == "google" and m.get("extra_body"):
            logger.warning("[%s] extra_body is ignored for Google batches (only temperature and "
                           "the token cap are converted)", m["label"])

    papers_json = str(papers_json)
    work_dir = Path(work_dir)

    report = {
        "run_id": get_run_id(), "status": "running", "dry_run": bool(dry_run),
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "papers_json": papers_json, "work_dir": str(work_dir),
        "prompt": prompt_info,
        "max_tokens": max_tokens, "temperature": temperature,
        "vote_threshold": vote_threshold,
        "allow_partial": bool(allow_partial),
        "models": [{**m, "settings": model_settings(m, temperature, max_tokens),
                    "price_per_m": model_price(m)} for m in models],
        "per_model": {m["label"]: {} for m in models},
    }

    papers = load_papers(papers_json)
    if max_papers > 0:
        papers = papers[:max_papers]
    logger.info("Loaded %d papers", len(papers))
    report["n_papers"] = len(papers)

    conf, max_pages = page_limit(papers_json, conference)
    logger.info("Conference: %s, max_pages=%d", conf or "unknown", max_pages)

    with log_step(logger, "Extract PDF text", n_papers=len(papers)):
        def _extract_one(p):
            pdf_path = p.get("path", "")
            if not pdf_path:
                return p["name"], ""
            try:
                return p["name"], extract_text(pdf_path, max_pages=max_pages) or ""
            except Exception:
                return p["name"], ""

        paper_texts = {}
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futures = {ex.submit(_extract_one, p): p for p in papers}
            for fut in as_completed(futures):
                name, text = fut.result()
                paper_texts[name] = text
                if not text.strip():
                    logger.warning("No text for: %s", name[:60])
    report["papers_without_text"] = sorted(p["name"] for p in papers if not paper_texts[p["name"]].strip())
    selected_names = {p["name"] for p in papers}

    # Per-model caches (the cache-consistency rule refuses another model's or prompt's trials).
    caches, unfingerprinted = {}, {}
    for m in models:
        caches[m["label"]], unfingerprinted[m["label"]] = {}, {}
        for ph in PHASES:
            caches[m["label"]][ph], unfingerprinted[m["label"]][ph] = load_trials_cache(
                work_dir, m, ph, prompt_info)

    if dry_run:
        _dry_run(models, papers, paper_texts, work_dir, prompts, prompt_info, caches,
                 temperature, max_tokens)
        return work_dir / "dry_run" / "dry_run_report.json"

    work_dir.mkdir(parents=True, exist_ok=True)
    (work_dir / "inputs").mkdir(exist_ok=True)
    (work_dir / "trials").mkdir(exist_ok=True)
    settings = {m["label"]: model_settings(m, temperature, max_tokens) for m in models}

    def _run_phase(phase, pending_by_label, builder):
        work = {}
        for cfg in models:
            label = cfg["label"]
            pending = pending_by_label.get(label, [])
            report["per_model"][label].setdefault(phase, new_stats())
            rep = report["per_model"][label][phase]
            rep["cached_papers"] = len(covered_papers(phase, caches[label][phase]) & selected_names)
            rep["pending_papers"] = len(pending)
            if not pending:
                logger.info("[%s] %s: all %d papers cached", label, phase, rep["cached_papers"])
                continue
            lines = builder(cfg, pending)
            if lines:
                work[label] = (cfg, lines)
        if not work:
            return []
        with log_step(logger, f"{phase} extraction (all models parallel)", n_models=len(work)):
            outcomes = run_phase_batches(phase, work, work_dir, workers)

        problems = []
        for label, (cfg, lines) in work.items():
            oc = outcomes[label]
            sent_ids = [json.loads(ln)["custom_id"] for ln in lines]
            usable, stats, problem_papers = process_phase_results(phase, oc["results"], sent_ids)
            stats.update({"cached_papers": report["per_model"][label][phase]["cached_papers"],
                          "pending_papers": len(pending_by_label[label]), "jobs": oc["jobs"],
                          "batch_errors": oc["errors"], "papers_without_output": problem_papers})
            add_cost(stats, model_price(cfg))
            report["per_model"][label][phase] = stats
            model_dir = work_dir / "trials" / label
            if usable:
                cache = caches[label][phase]
                for paper, trials in usable.items():
                    cache[paper] = trials
                _atomic_write_json(model_dir / TRIAL_FILES[phase], cache)
                write_trials_meta(work_dir, cfg, phase, prompt_info, settings[label], len(cache),
                                  unfingerprinted=unfingerprinted[label][phase])
            for err in oc["errors"]:
                problems.append(f"[{label}] {phase}: {err}")
            if problem_papers:
                problems.append(f"[{label}] {phase}: {len(problem_papers)} of {len(sent_ids)} "
                                f"requested papers have no usable output (request errors "
                                f"{stats['request_errors']}, missing {stats['missing_results']}, "
                                f"empty {stats['empty_outputs']}, parse failures "
                                f"{stats['parse_failures'] + stats['wrong_schema']}, truncated "
                                f"{stats['truncated_outputs']})")
        _log_phase_table(phase, report["per_model"])
        return problems

    # Pass 1: entities
    def _entity_builder(cfg, pending):
        st = settings[cfg["label"]]
        return build_entity_jsonl(pending, paper_texts, cfg["model"], st["temperature"], 1,
                                  prompts=prompts, max_tokens=st["max_tokens"],
                                  send_temperature=st["send_temperature"], extra_body=st["extra_body"])

    with_text = [p for p in papers if paper_texts[p["name"]].strip()]
    ent_pending = {}
    for cfg in models:
        covered = covered_papers("entities", caches[cfg["label"]]["entities"])
        ent_pending[cfg["label"]] = [p for p in with_text if p["name"] not in covered]
    problems = _run_phase("entities", ent_pending, _entity_builder)
    # A relationship entry cached for a paper whose entities were only obtained
    # in this run predates those entities, so it is dropped and requested
    # again. This happens before any stop, so a rerun cannot mistake the entry
    # for a covered paper.
    fresh_entities = {}
    for cfg in models:
        label = cfg["label"]
        fresh_entities[label] = ({p["name"] for p in ent_pending[label]}
                                 & covered_papers("entities", caches[label]["entities"]))
        stale = fresh_entities[label] & set(caches[label]["relationships"])
        if stale:
            logger.warning("[%s] dropping %d cached relationship entries made before their "
                           "entities existed", label, len(stale))
            for name in stale:
                caches[label]["relationships"].pop(name, None)
            _atomic_write_json(work_dir / "trials" / label / TRIAL_FILES["relationships"],
                               caches[label]["relationships"])

    _fail_or_warn(problems, allow_partial, work_dir, report, "Entity phase")

    # Each model's own entities (union over its usable trials, selected papers only).
    model_entity_trials = {}
    for cfg in models:
        cache = caches[cfg["label"]]["entities"]
        model_entity_trials[cfg["label"]] = {
            p: [t for t in cache[p] if usable_entity_trial(t)]
            for p in covered_papers("entities", cache) & selected_names}

    # Pass 2: relationships among each model's own entities
    rel_entities = {}

    def _rel_builder(cfg, pending):
        st = settings[cfg["label"]]
        return build_relationship_jsonl(pending, paper_texts, rel_entities[cfg["label"]], cfg["model"],
                                        st["temperature"], 1, prompts=prompts,
                                        max_tokens=st["max_tokens"],
                                        send_temperature=st["send_temperature"],
                                        extra_body=st["extra_body"])

    rel_pending = {}
    for cfg in models:
        label = cfg["label"]
        rel_entities[label] = majority_vote_entities(model_entity_trials[label], 1, {}, threshold=1)
        covered = covered_papers("relationships", caches[label]["relationships"])
        rel_pending[label] = [p for p in with_text
                           if p["name"] in rel_entities[label] and p["name"] not in covered]
    problems = _run_phase("relationships", rel_pending, _rel_builder)
    _fail_or_warn(problems, allow_partial, work_dir, report, "Relationship phase")

    for cfg in models:
        label = cfg["label"]
        me = rel_entities[label]
        rels = {p: t for p, t in caches[label]["relationships"].items() if p in selected_names}
        log_counts(logger, f"[{label}] Done",
                   constructs=sum(len(v.get("constructs", [])) for v in me.values()),
                   measurements=sum(len(v.get("measurements", [])) for v in me.values()),
                   behaviors=sum(len(v.get("behaviors", [])) for v in me.values()),
                   relationships=sum(len(r) for rl in rels.values() for r in rl if isinstance(r, list)))

    # Assemble all_entity_trials and all_rel_trials in model order (selected papers only)
    all_entity_trials, all_rel_trials = [], []
    for cfg in models:
        label = cfg["label"]
        all_entity_trials.append(model_entity_trials[label])
        all_rel_trials.append({p: [t for t in trials if isinstance(t, list)]
                               for p, trials in caches[label]["relationships"].items()
                               if p in selected_names})

    n_models = len(models)
    merged_entities, merged_rels = merge_trials(all_entity_trials, all_rel_trials)

    with log_step(
        logger, "Majority vote",
        n_models=n_models, threshold=vote_threshold,
    ):
        voted_entities = majority_vote_entities(merged_entities, n_models, {}, threshold=vote_threshold)
        # Relationships are the union over models (threshold=1): every
        # relationship any model extracted is kept here, and the relationship
        # vote with vote_threshold is taken later at the canonical-entity level.
        voted_rels = majority_vote_relationships(merged_rels, n_models, {}, threshold=1)

    # Save merged trials
    with open(work_dir / "trials" / "merged_entity_trials.json", "w") as f:
        json.dump(merged_entities, f, indent=2, ensure_ascii=False)
    with open(work_dir / "trials" / "merged_relationship_trials.json", "w") as f:
        json.dump(merged_rels, f, indent=2, ensure_ascii=False)

    # Assemble output
    model_labels = "+".join(m["label"] for m in models)
    results = {}
    for paper in papers:
        name = paper["name"]
        entities = voted_entities.get(name, {"constructs": [], "measurements": [], "behaviors": []})
        rels = voted_rels.get(name, [])

        nn = {
            "constructs": entities.get("constructs", []),
            "measurements": entities.get("measurements", []),
            "behaviors": entities.get("behaviors", []),
            "relationships": rels,
        }

        results[name] = {
            "provider": "multi-model",
            "model": model_labels,
            "title": name,
            "result": {
                "raw_text": "",
                "parsed_text": {
                    "Nomological Network": nn,
                    "Title": name,
                },
            },
            "processed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "attempts": 1,
            "name": paper.get("name", ""),
            "url": paper.get("url", ""),
            "path": paper.get("path", ""),
            "is_LLM_paper": True,
        }

    out_path = work_dir / "inputs" / "extraction.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    logger.info("Saved final extraction to %s", out_path)

    total_c = sum(len(v.get("constructs", [])) for v in voted_entities.values())
    total_m = sum(len(v.get("measurements", [])) for v in voted_entities.values())
    total_b = sum(len(v.get("behaviors", [])) for v in voted_entities.values())
    total_r = sum(len(v) for v in voted_rels.values())
    log_counts(
        logger, f"DONE ({n_models} models, {len(papers)} papers)",
        constructs=total_c, measurements=total_m,
        behaviors=total_b, relationships=total_r,
    )

    for label, rep in report["per_model"].items():
        costs = [rep[ph].get("est_cost_usd") for ph in PHASES if ph in rep]
        rep["total_est_cost_usd"] = (round(sum(costs), 4)
                                     if costs and all(c is not None for c in costs) else None)
    report["status"] = "partial" if report.get("accepted_problems") else "ok"
    report["output"] = str(out_path)
    report_path = _write_report(work_dir, report)
    logger.info("Run report: %s", report_path)
    return out_path


def main(argv=None) -> Path:
    args = build_arg_parser().parse_args(argv)
    setup_logging(run_name="extract", log_dir=args.log_dir)
    try:
        return run_extraction(
            args.papers_json, args.work_dir, parse_model_specs(args.models),
            temperature=args.temperature, max_tokens=args.max_tokens, workers=args.workers,
            max_papers=args.max_papers, allow_partial=args.allow_partial, dry_run=args.dry_run,
            prompts=args.prompts, conference=args.conference, vote_threshold=args.vote_threshold)
    except ExtractionIncomplete as e:
        logger.error("STOPPED: %s", e)
        sys.exit(2)


if __name__ == "__main__":
    main()
