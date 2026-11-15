"""Per-entity summaries through a provider's batch API.

For every entity with at least ``min_papers`` papers, this stage gathers everything the
network records about it (its definitions with their papers, its source snippets, every
relationship it takes part in with the claiming papers and evidence quotes, and counts of
the instruments, behavioral indicators and constructs it is linked to) and asks the model
for a sectioned summary, one request per entity so each gets the model's full attention.
The requests go out as batch jobs (the OpenAI Batch API on the Responses endpoint, or the
Gemini batch API), are polled until complete, and the answers are written back onto the
entities as ``characterization`` (the labeled sections joined into one text) and
``characterization_sections`` ({field: text}). The section fields and their display
labels come from the prompt set (``CHARACTERIZE_SECTION_LABELS``), the per-type
instructions from ``CHARACTERIZE_TYPE_GUIDANCE``, and the counts in the context are
computed here so the model never has to count.

Entities below ``min_papers`` get a deterministic summary instead: their first recorded
definition, or ``canonical_definition``. Entities flagged ``expert_removed`` are left
untouched by default, as are entities that already have a summary (``regenerate`` sends
them again); links to removed entities are left out of every context.

Files written next to ``output_json``: ``<output>.batch_jobs.json`` with the batch job
ids (pass it as ``resume_jobs`` to pick up a run whose polling was interrupted) and
``<output>.batch_results.jsonl`` with the raw results.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List

from aiconstructlexis.prompts import load_prompts

logger = logging.getLogger(__name__)

ENTITY_TYPES = ("constructs", "measurements", "behaviors")
PROVIDERS = ("openai", "google")
FAILED_SENTINEL = "__FAILED__"      # the content the batch helpers give a failed request
STATS_TOP_N = 12
STATS_LABELS = {"measurements": "instruments", "behaviors": "behavioral_indicators", "constructs": "constructs"}
SYSTEM_PROMPT = (
    "You are a research assistant specializing in academic knowledge synthesis. "
    "Always respond with valid JSON only."
)
OPENAI_MAX_OUTPUT_TOKENS = 64000
GOOGLE_MAX_TOKENS = 32768
MAX_TOKENS_PER_BATCH = 2_500_000    # estimated input tokens per OpenAI batch (characters / 4)


def prompt_set(prompts):
    """The prompt module for a prompt-set name, or the module itself."""
    return prompts if hasattr(prompts, "CHARACTERIZE_ENTITIES_PROMPT") else load_prompts(prompts)


# ---------------------------------------------------------------- per-entity context

def entity_stats(entity: Dict[str, Any], rels: List[Dict[str, Any]], entity_index: Dict[str, Any]) -> Dict[str, Any]:
    """Counts the summary reports (the model never computes them): how many instruments,
    behavioral indicators and constructs the entity is linked to, each with the most
    frequently linked listed first. ``rels`` are this entity's in-scope links."""
    name = entity["canonical_name"]
    linked = {et: {} for et in STATS_LABELS}
    for r in rels:
        other = r["target"] if r["source"] == name else r["source"]
        slot = linked[entity_index[other][0]].setdefault(other, {"papers": set(), "types": set()})
        slot["papers"] |= {(p.get("conference"), p.get("paper")) for p in r.get("papers") or [] if isinstance(p, dict)}
        slot["types"].add(r.get("type", ""))
    out: Dict[str, Any] = {}
    for et, label in STATS_LABELS.items():
        items = sorted(linked[et].items(), key=lambda kv: (-len(kv[1]["papers"]), kv[0]))
        out[f"linked_{label}_count"] = len(items)
        # Most frequently linked first; paper counts are left out (summaries do not report them).
        out[f"most_linked_{label}"] = [{"name": n, "relationship_types": sorted(v["types"])} for n, v in items[:STATS_TOP_N]]
    return out


def build_entity_context(entity: Dict[str, Any], entity_type: str, relationships: List[Dict[str, Any]],
                         entity_index: Dict[str, Any] = None) -> Dict[str, Any]:
    """Full per-entity context for the model. No truncation: all definitions, snippets and
    relationships involving this entity are included.

    With ``entity_index`` ({canonical name: (type, entity)}), links to entities the site
    hides (expert_removed) are left out and the computed ``stats`` are added."""
    name = entity["canonical_name"]

    definitions = []
    for orig_name, node in (entity.get("original_nodes") or {}).items():
        defn = (node.get("definition") or "").strip()
        papers = node.get("papers", []) or []
        if defn:
            definitions.append({"original_name": orig_name, "definition": defn, "papers": papers})

    snippets = entity.get("source_snippets_evidence") or []

    rels = []
    for r in relationships:
        src = r.get("source") or r.get("canonical_source")
        tgt = r.get("target") or r.get("canonical_target")
        if src == name or tgt == name:
            if entity_index is not None:
                other = tgt if src == name else src
                if other not in entity_index or entity_index[other][1].get("expert_removed"):
                    continue
            evidence = r.get("evidence") or []
            if not evidence:
                evidence = [ri.get("evidence", "") for ri in (r.get("raw_instances") or []) if ri.get("evidence")]
            rels.append({"source": src, "target": tgt, "type": r.get("type", ""),
                         "evidence": evidence, "papers": r.get("papers") or []})

    ctx = {"canonical_name": name, "type": entity_type, "definitions": definitions,
           "source_snippets": snippets, "relationships": rels}
    if entity_index is not None:
        ctx["stats"] = entity_stats(entity, rels, entity_index)
    return ctx


# ---------------------------------------------------------------- batch requests

def fallback_summary(entity: Dict[str, Any]) -> str:
    """Deterministic summary for an entity below the paper threshold: its first definition."""
    for node in (entity.get("original_nodes") or {}).values():
        d = (node.get("definition") or "").strip()
        if d:
            return d
    return entity.get("canonical_definition", "") or ""


def build_requests(network: Dict[str, Any], min_papers: int = 3, skip_characterized: bool = True,
                   provider: str = "openai", model: str = "", effort: str = "high",
                   skip_removed: bool = True, prompts="default") -> List[str]:
    """Batch request lines (JSON strings), one per entity that needs a model call.

    Entities below ``min_papers`` are given their fallback summary in place and get no
    request. ``provider`` "openai" builds Responses API requests for the OpenAI Batch API
    (``/v1/responses``, reasoning effort ``effort``, JSON output); "google" builds
    chat-completion bodies for the Gemini batch API."""
    P = prompt_set(prompts)
    relationships = network.get("relationships") or []
    entity_index = {e.get("canonical_name"): (et, e) for et in ENTITY_TYPES for e in network.get(et) or []}
    lines: List[str] = []
    skipped_fallback = skipped_existing = 0

    for etype in ENTITY_TYPES:
        for idx, entity in enumerate(network.get(etype) or []):
            if skip_removed and entity.get("expert_removed"):
                continue
            # An entity counts as summarized when it has a model summary; the one-sentence
            # fallback of an entity that has since reached min_papers does not count.
            text = (entity.get("characterization") or "").strip()
            if skip_characterized and text and (entity.get("characterization_sections")
                                                or text != fallback_summary(entity).strip()):
                skipped_existing += 1
                continue
            if entity.get("paper_count", 0) < min_papers:
                entity["characterization"] = fallback_summary(entity)
                skipped_fallback += 1
                continue

            ctx = build_entity_context(entity, etype, relationships, entity_index)
            ctx_json = json.dumps([ctx], indent=2)      # the prompt expects array-shaped JSON
            user_prompt = P.CHARACTERIZE_ENTITIES_PROMPT.format(
                entities_json=ctx_json, type_guidance=P.CHARACTERIZE_TYPE_GUIDANCE[etype])
            custom_id = json.dumps({"etype": etype, "idx": idx, "name": entity.get("canonical_name", "")})

            if provider == "openai":
                req = {
                    "custom_id": custom_id,
                    "method": "POST",
                    "url": "/v1/responses",
                    "body": {
                        "model": model,
                        "reasoning": {"effort": effort},
                        "input": [
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": user_prompt},
                        ],
                        "text": {"format": {"type": "json_object"}},
                        "max_output_tokens": OPENAI_MAX_OUTPUT_TOKENS,
                    },
                }
            else:
                req = {
                    "custom_id": custom_id,
                    "body": {
                        "messages": [
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": user_prompt},
                        ],
                        "temperature": 0,
                        "max_tokens": GOOGLE_MAX_TOKENS,
                    },
                }
            lines.append(json.dumps(req, ensure_ascii=False))

    logger.info("Built %d batch requests; %d entities got the fallback summary; %d already summarized",
                len(lines), skipped_fallback, skipped_existing)
    return lines


# ---------------------------------------------------------------- result parsing

def result_text(result: Dict[str, Any]) -> str:
    """The answer text of one batch result (Responses API or chat-completions shape)."""
    body = (result.get("response") or {}).get("body", {}) or {}
    if body.get("object") == "response" or "output" in body:
        parts = [c.get("text", "") for item in body.get("output") or [] if item.get("type") == "message"
                 for c in item.get("content") or [] if c.get("type") == "output_text"]
        return "".join(parts)
    choices = body.get("choices") or []
    if not choices:
        return ""
    return choices[0].get("message", {}).get("content", "") or ""


def parse_json_loose(text: str) -> Any:
    """Strip code fences and think tags, parse JSON; fall back to json_repair."""
    if not text:
        return None
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if fence:
        text = fence.group(1).strip()
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        try:
            from json_repair import repair_json
            repaired = repair_json(text, return_objects=True)
            if isinstance(repaired, (dict, list, str)):
                return repaired
        except Exception:  # noqa: BLE001
            pass
    return None


def compose_sections(etype: str, parsed: Dict[str, Any], prompts="default") -> tuple:
    """Sectioned output ({field: text}) -> (labeled text, sections), or ("", {}) if no section field is present."""
    labels = prompt_set(prompts).CHARACTERIZE_SECTION_LABELS[etype]
    sections = {k: parsed[k].strip() for k, _ in labels if isinstance(parsed.get(k), str) and parsed[k].strip()}
    if not sections:
        return "", {}
    text = "\n\n".join(f"{label} {sections[k]}" for k, label in labels if k in sections)
    return text, sections


def attach_results(network: Dict[str, Any], results: List[Dict[str, Any]], prompts="default") -> Dict[str, int]:
    """Write each result's summary onto the entity its custom_id names (type, index and
    canonical name must match). Returns counts of {ok, parse_failed, missing_target, failed_request}."""
    stats = {"ok": 0, "parse_failed": 0, "missing_target": 0, "failed_request": 0}

    for r in results:
        try:
            cid = json.loads(r.get("custom_id", ""))
        except json.JSONDecodeError:
            cid = {}
        etype = cid.get("etype")
        idx = cid.get("idx")
        canonical_name = cid.get("name", "")
        if etype not in ENTITY_TYPES or not isinstance(idx, int):
            stats["missing_target"] += 1
            continue

        text = result_text(r)
        if text == FAILED_SENTINEL or not text:
            stats["failed_request"] += 1
            continue

        parsed = parse_json_loose(text)
        char_text, sections = "", {}
        if isinstance(parsed, dict):
            char_text, sections = compose_sections(etype, parsed, prompts)
        if char_text:
            pass
        elif isinstance(parsed, dict):
            # A single-key {Canonical Name: text} object is accepted too, tolerating case
            # differences and a "characterization" key.
            if canonical_name and canonical_name in parsed:
                char_text = parsed[canonical_name]
            else:
                for k, v in parsed.items():
                    if isinstance(v, str) and (k.lower() == canonical_name.lower() or k.lower() == "characterization"):
                        char_text = v
                        break
                if not char_text:
                    string_values = [v for v in parsed.values() if isinstance(v, str)]
                    if len(string_values) == 1:
                        char_text = string_values[0]
        elif isinstance(parsed, str):
            char_text = parsed

        if not char_text:
            stats["parse_failed"] += 1
            continue

        entities = network.get(etype) or []
        if 0 <= idx < len(entities) and entities[idx].get("canonical_name", "") == canonical_name:
            entities[idx]["characterization"] = char_text
            if sections:
                entities[idx]["characterization_sections"] = sections
            stats["ok"] += 1
        else:
            stats["missing_target"] += 1

    return stats


# ---------------------------------------------------------------- batch submission and polling

def submit_batches_openai(client, lines: List[str], description: str,
                          max_tokens_per_batch: int = MAX_TOKENS_PER_BATCH) -> List[str]:
    """Upload and create OpenAI batches for /v1/responses, split so each batch stays under
    ``max_tokens_per_batch`` estimated input tokens (characters / 4). Returns the batch ids."""
    chunks, cur, cur_tokens = [], [], 0
    for line in lines:
        t = len(line) // 4
        if cur and cur_tokens + t > max_tokens_per_batch:
            chunks.append(cur)
            cur, cur_tokens = [], 0
        cur.append(line)
        cur_tokens += t
    if cur:
        chunks.append(cur)
    ids = []
    for i, chunk in enumerate(chunks, 1):
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False, encoding="utf-8") as tmp:
            tmp.write("\n".join(chunk) + "\n")
        try:
            with open(tmp.name, "rb") as f:
                file_id = client.files.create(file=f, purpose="batch").id
            batch = client.batches.create(input_file_id=file_id, endpoint="/v1/responses", completion_window="24h",
                                          metadata={"description": f"{description} part {i}/{len(chunks)}"})
            ids.append(batch.id)
            logger.info("OpenAI batch %d/%d: %s (%d requests)", i, len(chunks), batch.id, len(chunk))
        finally:
            os.unlink(tmp.name)
    return ids


def poll_batches_openai(client, ids: List[str], poll_interval: int = 60) -> List[Dict[str, Any]]:
    from aiconstructlexis.extract.batch import poll_batch

    results: List[Dict[str, Any]] = []
    for bid in ids:
        results.extend(poll_batch(client, bid, poll_interval=poll_interval))
    return results


def _submit(provider: str, lines: List[str], description: str, model: str) -> List[str]:
    if provider == "openai":
        from aiconstructlexis.providers.clients import init_openai_client
        return submit_batches_openai(init_openai_client(), lines, description)
    from aiconstructlexis.extract.batch import submit_batch_google
    return [submit_batch_google(lines, description, model)]


def _poll(provider: str, ids: List[str], poll_interval: int) -> List[Dict[str, Any]]:
    if provider == "openai":
        from aiconstructlexis.providers.clients import init_openai_client
        return poll_batches_openai(init_openai_client(), ids, poll_interval=poll_interval)
    from aiconstructlexis.extract.batch import poll_batch_google
    results: List[Dict[str, Any]] = []
    for job in ids:
        results.extend(poll_batch_google(job, poll_interval=poll_interval))
    return results


def job_ids(resume_jobs) -> List[str]:
    """Batch job ids from a list, a comma-separated string or the path of a batch_jobs.json file."""
    if isinstance(resume_jobs, (list, tuple)):
        return [str(j) for j in resume_jobs]
    s = str(resume_jobs)
    if Path(s).is_file():
        loaded = json.loads(Path(s).read_text(encoding="utf-8"))
        return [str(j) for j in loaded] if isinstance(loaded, list) else [str(loaded)]
    return [j.strip() for j in s.split(",") if j.strip()]


# ---------------------------------------------------------------- stage entry

def characterize(input_json, output_json, provider: str = "openai", model: str = "gpt-5.4",
                 reasoning_effort: str = "high", min_papers: int = 3, description: str = "characterize",
                 poll_interval: int = 60, resume_jobs=None, regenerate: bool = False,
                 skip_removed: bool = True, prompts="default") -> Path:
    """Summarize every entity of the network in ``input_json`` and write ``output_json``.

    ``resume_jobs`` (ids, or the ``<output>.batch_jobs.json`` path) polls existing batch
    jobs instead of submitting new ones. Returns the path written."""
    if provider not in PROVIDERS:
        raise ValueError(f"provider must be one of {PROVIDERS}, got {provider!r}")
    P = prompt_set(prompts)
    in_path, out_path = Path(input_json), Path(output_json)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(in_path, encoding="utf-8") as f:
        network = json.load(f)
    logger.info("Loaded %s: %s", in_path, ", ".join(f"{et} {len(network.get(et) or [])}" for et in ENTITY_TYPES))

    # Building the requests also writes the fallback summaries of entities below the threshold.
    lines = build_requests(network, min_papers=min_papers, skip_characterized=not regenerate,
                           provider=provider, model=model, effort=reasoning_effort,
                           skip_removed=skip_removed, prompts=P)
    results: List[Dict[str, Any]] = []
    if resume_jobs is not None:
        ids = job_ids(resume_jobs)
        logger.info("Resuming %s batch job(s): %s", provider, ids)
        results = _poll(provider, ids, poll_interval)
    elif not lines:
        logger.info("Nothing to send to the model; only fallback summaries were written.")
    else:
        ids = _submit(provider, lines, description, model)
        jobs_path = out_path.with_suffix(".batch_jobs.json")
        jobs_path.write_text(json.dumps(ids), encoding="utf-8")
        logger.info("Wrote batch job ids to %s (pass it as resume_jobs to recover)", jobs_path)
        t0 = time.time()
        results = _poll(provider, ids, poll_interval)
        logger.info("Batch finished in %.1f min; %d results", (time.time() - t0) / 60, len(results))

    stats = attach_results(network, results, P)
    logger.info("Results attached: %s", stats)

    total = sum(len(network.get(et) or []) for et in ENTITY_TYPES)
    done = sum(1 for et in ENTITY_TYPES for e in network.get(et) or [] if e.get("characterization"))
    logger.info("Summarized %d / %d entities (%.1f%%)", done, total, 100 * done / max(1, total))

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(network, f, indent=2, ensure_ascii=False)
    logger.info("Wrote %s", out_path)
    raw_path = out_path.with_suffix(".batch_results.jsonl")
    with open(raw_path, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    logger.info("Wrote raw batch results to %s", raw_path)
    return out_path


def main(argv=None) -> None:
    from aiconstructlexis.util.logging import setup_logging

    p = argparse.ArgumentParser(description="Summarize every entity of a network through a batch API.")
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--provider", choices=PROVIDERS, default="openai",
                   help="openai: OpenAI Batch API on the Responses endpoint; google: Gemini batch API")
    p.add_argument("--model", default="gpt-5.4")
    p.add_argument("--reasoning-effort", default="high", help="OpenAI reasoning effort")
    p.add_argument("--min-papers", type=int, default=3,
                   help="entities with fewer papers get their first definition as summary")
    p.add_argument("--description", default="characterize", help="display label of the batch job")
    p.add_argument("--poll-interval", type=int, default=60, help="seconds between status polls")
    p.add_argument("--resume-jobs", default=None,
                   help="poll these jobs instead of submitting: ids separated by commas, or the batch_jobs.json path")
    p.add_argument("--regenerate", action="store_true", help="summarize entities that already have a summary")
    p.add_argument("--include-removed", action="store_true", help="also summarize expert-removed entities")
    p.add_argument("--prompts", default="default", help="prompt set: 'default' or a dotted module path")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args(argv)
    setup_logging(run_name="summarize", log_dir=args.log_dir)
    characterize(input_json=args.input, output_json=args.output, provider=args.provider, model=args.model,
                 reasoning_effort=args.reasoning_effort, min_papers=args.min_papers, description=args.description,
                 poll_interval=args.poll_interval, resume_jobs=args.resume_jobs, regenerate=args.regenerate,
                 skip_removed=not args.include_removed, prompts=args.prompts)


if __name__ == "__main__":
    main()
