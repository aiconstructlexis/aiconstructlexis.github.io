"""Checks on the per-entity summaries, with an optional single retry of hard failures.

Reads the network the summaries were built from (``input_json``) and the summarized
network (``output_json``), rewords the phrases of each summary that refer to the model's
input rather than to the papers (WORDING: "across the provided sources" becomes "across
the papers", "source snippets" becomes "quoted passages"), checks every entity that was
sent to the model, and writes ``<output>.checks.json``. With ``retry``, each entity with a
hard problem is sent once more through the OpenAI Responses API (standard endpoint, same
prompt and settings); the retry is kept only when it has fewer hard problems. The
summarized network is rewritten in place when a summary was reworded or replaced.

Hard problems (retried): no sections at all (the request failed or did not parse); an em
dash or a spaced en dash; a banned word ("crucial", "important", ...) the input does not use
in the same phrase; a paper or surface-name count in digits; wording about the input itself
("stats", "the data provided"); a number found nowhere in the input; more than two paper
titles; a link count ("linked to 12 instruments") that differs from the input's stats, or a
zero link count in digits. Soft flags (reported, not retried): an entity of the network
named in a link section but absent from the input; derived counts ("plus 40 other
instruments"); empty sections (the prompt allows them when the input has nothing for a
section); interpretive words; causal verbs; counts of two or more written as words.

The written summary also reports token usage and an estimated cost from the raw batch
results when ``<output>.batch_results.jsonl`` is present.
"""
from __future__ import annotations

import argparse
import collections
import json
import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from aiconstructlexis.summarize.characterize import (SYSTEM_PROMPT, OPENAI_MAX_OUTPUT_TOKENS, STATS_TOP_N,
                                                     build_entity_context, compose_sections, prompt_set)

logger = logging.getLogger(__name__)

TYPES = ("constructs", "measurements", "behaviors")
EM_DASH = "\u2014"
SPACED_EN_DASH = " \u2013 "
BANNED = re.compile(r"\b(crucial|important|essential|significant|key(?!-)|notably)\b", re.I)
PAPER_COUNTS = re.compile(r"\b\d[\d,]*\s+(?:papers?|surface names?)\b", re.I)
COUNT_WORDS = re.compile(r"\b(?:two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|a dozen)\s+"
                         r"(?:papers?|surface names?)\b", re.I)
META = re.compile(r"\b(stats|this set|provided (?:snippets|data|sources|literature|papers)|the data provided|"
                  r"available data|source snippets?|in the record|recorded here)\b", re.I)

# Phrases that describe the model's input instead of the papers. The input is the papers'
# definitions, quotes and relationships, so each phrase is replaced by its referent:
# "the papers", "the literature", "the definitions", "the quoted passages" or "the recorded
# relationships". Applied in order; whatever is left is caught by META.
# One word of a name: no space and no sentence punctuation, though "2.0" or "GPT-4o" pass.
_WORD = r"[^\s.,;:!?]+(?:\.[^\s.,;:!?]+)*"
_VERBS = {"indicates": "indicate", "shows": "show", "identifies": "identify", "specifies": "specify",
          "includes": "include", "details": "describe", "situates": "situate", "does not elaborate": "do not elaborate"}
WORDING = [
    (r"\b(A|a)cross the (?:provided|available) (?:sources|literature|data|papers|materials?)\b", r"\1cross the papers"),
    (r"\b(A|a)cross the available definitions\b", r"\1cross the definitions"),
    (r"\b(B|b)ased on the (?:provided|available) data\b", lambda m: ("In" if m.group(1) == "B" else "in") + " the papers"),
    (r"\bIn all provided cases\b", "In all cases"),
    (r"\b(I|i)n the provided (?:data|sources|materials)\b", r"\1n the papers"),
    (r"\b(I|i)n the provided literature\b", r"\1n the literature"),
    (r"\b(W|w)ithin the provided literature\b", r"\1ithin the literature"),
    (r"\b(T|t)he (?:provided|available) data (also )?(" + "|".join(map(re.escape, _VERBS)) + r")\b",
     lambda m: f"{m.group(1)}he papers {m.group(2) or ''}{_VERBS[m.group(3)]}"),
    (r"\b(T|t)he provided literature\b", r"\1he literature"),
    (r"\b(T|t)he provided (?:sources|papers)\b", r"\1he papers"),
    (r"\b(T|t)he provided materials\b", r"\1he papers"),
    (r"\bThe provided work suggests\b", "The papers suggest"),
    (r"\bThe single provided source defines\b", "The single paper defines"),
    (r"\bThe provided source describes\b", "The paper describes"),
    (r"\bThe provided information positions\b", "Papers position"),
    (r"\bin the supplied relationships\b", "in the recorded relationships"),
    (r"\b(T|t)he (?:available|provided) relationships\b", r"\1he recorded relationships"),
    (r"\b(T|t)he papers represented here\b", r"\1he papers"),
    (r"\bthe provided links\b", "the recorded links"),
    (r"\bThe only description provided places\b", "The only description places"),
    (r"\b(T|t)he only characterization provided\b", r"\1he only characterization"),
    (r"\bThe descriptions provided all\b", "The descriptions all"),
    (r"\b([Pp]apers?) in this set\b", r"\1"),
    (r"\bin this set of papers\b", "in these papers"),
    (r"\b(T|t)he available (definitions|evidence|description)\b", r"\1he \2"),
    (r"\bThe available usage organizes\b", "Usage in the papers organizes"),
    (r"\bThe available operational detail\b", "The operational detail in the papers"),
    (r"\bthe available definition and snippet\b", "the definition and quoted passage"),
    (r"\bThe available definition places\b", "The one definition places"),
    (r"\bIn the available definition,", "In the one definition,"),
    (r"\bIn the available usage snippet,", "In the one quoted passage,"),
    (r"\b(T|t)he available (?:usage |relationship |source )?snippet(s?)\b", r"\1he quoted passage\2"),
    (r"\bin the available work\b", "in the papers"),
    (r"\b([Rr]elationship|[Uu]sage|[Ss]ource) snippet(s?)\b",
     lambda m: ("Q" if m.group(1)[0].isupper() else "q") + "uoted passage" + m.group(2)),
    (r"\b(D|d)efinitions and snippets\b", r"\1efinitions and quoted passages"),
    (r"\b(D|d)escriptions and snippets\b", r"\1escriptions and quoted passages"),
    (r"\b(T|t)he accompanying snippet(s?)\b", r"\1he accompanying quoted passage\2"),
    (r"\bRelated snippets\b", "Related quoted passages"),
    (r"\bthe surrounding snippets\b", "the surrounding quoted passages"),
    (r"\bits snippets\b", "its quoted passages"),
    # "reports that X is reported to correlate with": the report is stated twice (X is one to six words).
    (r"\b([Rr])eports that (" + _WORD + r"(?: " + _WORD + r"){0,5}) is reported to correlate with\b",
     r"\1eports that \2 correlates with"),
]
_WORDING = [(re.compile(p), r) for p, r in WORDING]
# A bare "snippet" is the pipeline's word for a quote. Papers also say "code snippet", "text
# snippet" or "a snippet of conversation", so a snippet owned by one of those words, a snippet
# inside quotation marks, and entities about code are left alone.
_SNIPPET_WORD = re.compile(r"\b(S|s)nippet(s?)(?![\w-])(?! of )")
_SNIPPET_OWNERS = {"code", "text", "book", "suffix", "sql", "conversation", "dialogue", "program"}
# "the available papers" and similar: the papers themselves, not the model's input.
_AVAILABLE = re.compile(r"\b(T|t)he available (papers?|work|uses?|usages?|operationalizations?|operational|materials?|"
                        r"measurements?|claims|literature|explicit|behaviors?|sources?|relations|discussion|task|"
                        r"descriptions?|definitions?|evidence|framings?|records?|links|examples|studies)\b")
# Not covered, since the papers use them in their own sense: "the available context", "options",
# "functions", "tools", "training data".


def _quoted_spans(text):
    """Character spans inside quotation marks, curly or straight (straight ones paired per paragraph)."""
    spans = [m.span() for m in re.finditer("\u201c[^\u201d]*\u201d", text)]
    pos = 0
    for para in text.split("\n\n"):
        marks = [pos + m.start() for m in re.finditer('"', para)]
        spans += [(a, b + 1) for a, b in zip(marks[0::2], marks[1::2])]
        pos += len(para) + 2
    return spans


def normalize_wording(text: str, name: str = "") -> str:
    """``text`` with the input-referring phrases of WORDING replaced by their referents."""
    if not text:
        return text
    for rx, repl in _WORDING:
        text = rx.sub(repl, text)
    text = _AVAILABLE.sub(lambda m: f"{m.group(1)}he " + {"usage": "usage in the papers", "work": "papers"}.get(m.group(2), m.group(2)),
                          text)
    if "code" in name.lower():
        return text
    spans = _quoted_spans(text)

    def quoted(m):
        if any(a <= m.start() < b for a, b in spans):
            return m.group(0)
        owner = re.search(r"([\w-]+) $", text[max(0, m.start() - 25):m.start()])
        if owner and owner.group(1).lower() in _SNIPPET_OWNERS:
            return m.group(0)
        return ("Q" if m.group(1) == "S" else "q") + "uoted passage" + m.group(2)

    return _SNIPPET_WORD.sub(quoted, text)


def normalize_entity(etype, entity, prompts="default") -> bool:
    """Reword the sections of one summary and recompose it; True when anything changed."""
    sections = entity.get("characterization_sections")
    if not sections:
        return False
    new = {k: normalize_wording(v, entity.get("canonical_name") or "") for k, v in sections.items()}
    if new == sections:
        return False
    text, secs = compose_sections(etype, new, prompts)
    entity["characterization_sections"] = secs
    entity["characterization"] = text
    return True
CAUSAL_VERBS = re.compile(r"\b(causes|caused|drives|improves|leads to)\b", re.I)
INTERPRETIVE = re.compile(r"\b(suggests?|suggesting|indicat(?:es|ing) that|reflects?|reflecting|underscor\w*|"
                          r"highlight\w*|implies|implying|demonstrat\w* that|reveals?|signal\w*|likely|presumably|"
                          r"maturing|under-?studied|growing interest|increasingly)\b", re.I)
NUMBER = re.compile(r"(?<![\w.])\d+(?:,\d{3})*(?:\.\d+)?(?!\d)")
THOUSANDS = re.compile(r"(?<=\d)(?:, ?|[\s\u202f\u2009])(?=\d{3}\b)")  # 14,042 = 14 042 = 14, 042
# Batch API prices in USD per 1M tokens (input, output), used for the cost line
# (batch_cost_usd) of the checks report; the standard endpoint costs twice as much.
PRICES = {"gpt-5.4": (1.25, 7.5)}

# Summary fields that describe the entity's links (field names of the default prompt set).
LINK_FIELDS = ("measurement", "links", "evidence_of", "measures", "usage")
# "linked to 12 measurement instruments": a link count, which must equal the stats count.
# "and 23 other instruments" does not match (the count of the links not named).
LINK_COUNT = re.compile(r"\b(\d+)\s+(?:linked\s+|distinct\s+|different\s+)?"
                        r"(measurement instruments?|instruments?|behavioral indicators?|constructs?)\b")
_LINK_COUNT_KEY = {"measurement instrument": "linked_instruments_count", "instrument": "linked_instruments_count",
                   "behavioral indicator": "linked_behavioral_indicators_count", "construct": "linked_constructs_count"}


def in_scope(entity, min_papers):
    return not entity.get("expert_removed") and entity.get("paper_count", 0) >= min_papers


def names_in(ctx):
    """Names and titles from the input, longest first, so banned words inside them are not flagged."""
    names = {ctx["canonical_name"]}
    names |= {d.get("original_name") or "" for d in ctx["definitions"]}
    names |= {s.get("paper") or "" for s in ctx["source_snippets"]}
    names |= {r.get("source") or "" for r in ctx["relationships"]} | {r.get("target") or "" for r in ctx["relationships"]}
    return sorted((n for n in names if len(n) > 3), key=len, reverse=True)


def source_phrase(text, m, blob_lower):
    """True when the word and a neighbor appear together in the input, as in "faithfulness to important inputs"."""
    before = re.findall(r"[\w-]+", text[:m.start()])[-1:]
    after = re.findall(r"[\w-]+", text[m.end():])[:1]
    word = m.group(0).lower()
    return any(f"{b.lower()} {word}" in blob_lower for b in before) or any(f"{word} {a.lower()}" in blob_lower for a in after)


def titles_in(ctx):
    return {s["paper"] for s in ctx["source_snippets"] if s.get("paper")} | {
        p[1] for d in ctx["definitions"] for p in d.get("papers") or [] if isinstance(p, list) and len(p) > 1}


def _distinctive(name):
    """True for a name that reads as a name in prose: several words, or a single word with a
    capital after its first letter or a digit (MMLU, GSM8K). Single ordinary words such as
    "Planning" or "Counting" also occur as plain words and are left out."""
    return len(name) >= 4 and (" " in name.strip() or any(c.isupper() or c.isdigit() for c in name[1:]))


def _named_in(name, text):
    """``name`` occurs in ``text`` as written, or with its first letter in lower case."""
    forms = {name, name[:1].lower() + name[1:]}
    return any(re.search(r"(?<![\w-])" + re.escape(f) + r"(?![\w-])", text) for f in forms)


def check(etype, entity, ctx, prompts="default", entity_names=None):
    """(hard problems, soft flags) for one entity's summary.

    ``entity_names`` (the network's in-scope canonical names) enables the check that the
    link sections name no entity absent from the entity's input."""
    hard, soft = [], []
    labels = prompt_set(prompts).CHARACTERIZE_SECTION_LABELS[etype]
    sections = entity.get("characterization_sections") or {}
    missing = [k for k, _ in labels if not (sections.get(k) or "").strip()]
    if len(missing) == len(labels):
        return ["no sections (request failed or did not parse)"], []
    if missing:
        soft.append(f"empty sections: {', '.join(missing)}")
    text = entity.get("characterization") or ""
    if EM_DASH in text:
        hard.append("em dash")
    if SPACED_EN_DASH in text:
        hard.append("spaced en dash")
    plain = text
    for n in names_in(ctx):
        plain = plain.replace(n, " ")
    blob_lower = json.dumps(ctx, ensure_ascii=False).lower()
    banned = sorted({m.group(0).lower() for m in BANNED.finditer(plain) if not source_phrase(plain, m, blob_lower)})
    if banned:
        hard.append(f"banned words: {', '.join(banned)}")
    counts = PAPER_COUNTS.findall(text)
    if counts:
        hard.append(f"counts in digits: {', '.join(counts)}")
    meta = sorted({m.lower() for m in META.findall(text)})
    if meta:
        hard.append(f"meta wording: {', '.join(meta)}")
    blob = THOUSANDS.sub("", json.dumps(ctx, ensure_ascii=False))
    # Small counts, up to the length of the stats lists, appear in ordinary prose.
    small = {str(i) for i in range(STATS_TOP_N + 1)}
    unknown = sorted({n for n in NUMBER.findall(THOUSANDS.sub("", text))
                      if n.replace(",", "") not in small and n.replace(",", "") not in blob})
    # "plus 40 other instruments": a linked count minus the up to five items named.
    derived = {str(v - k) for key, v in (ctx.get("stats") or {}).items()
               if key.endswith("_count") and isinstance(v, int) for k in range(1, 6)}
    if [n for n in unknown if n.replace(",", "") in derived]:
        soft.append(f"derived counts: {', '.join(n for n in unknown if n.replace(',', '') in derived)}")
    unknown = [n for n in unknown if n.replace(",", "") not in derived]
    if unknown:
        hard.append(f"numbers not in input: {', '.join(unknown)}")
    named = sum(1 for t in titles_in(ctx) if t and t in text)
    if named > 2:
        hard.append(f"{named} paper titles")
    stats = ctx.get("stats") or {}
    wrong, zeros = [], []
    for m in LINK_COUNT.finditer(text):
        want = stats.get(_LINK_COUNT_KEY[m.group(2).lower().rstrip("s")])
        if int(m.group(1)) == 0:
            zeros.append(m.group(0))      # the prompt asks for "no measurement instrument is linked"
        elif isinstance(want, int) and int(m.group(1)) != want:
            wrong.append(f"{m.group(0)} (input: {want})")
    if wrong:
        hard.append(f"link counts that differ from the input: {'; '.join(wrong)}")
    if zeros:
        hard.append(f"zero link counts in digits: {'; '.join(zeros)}")
    if entity_names:
        P = prompt_set(prompts)
        links = " ".join(sections.get(k) or "" for k in LINK_FIELDS)
        # Words the prompt itself uses ("human evaluation", "LLM-as-a-judge") are not names here.
        known = blob_lower + " " + (P.CHARACTERIZE_ENTITIES_PROMPT + P.CHARACTERIZE_TYPE_GUIDANCE[etype]).lower()
        own = (ctx.get("canonical_name") or "").lower()
        absent = [n for n in entity_names
                  if _distinctive(n) and n.lower() != own and n.lower() in links.lower()
                  and n.lower() not in known and _named_in(n, links)]
        if absent:
            # Reported, not retried: ordinary phrases such as "question answering" are also entity names.
            soft.append(f"entities not in the input: {', '.join(absent[:8])}")
    for label, rx in (("interpretive words", INTERPRETIVE), ("causal verbs", CAUSAL_VERBS), ("counts in words", COUNT_WORDS)):
        found = sorted({m.lower() for m in rx.findall(text)})
        if found:
            soft.append(f"{label}: {', '.join(found)}")
    return hard, soft


def batch_usage(results_path):
    """Token totals and the model, effort and status the batch echoed, from the raw results."""
    usage = collections.Counter()
    echo = collections.Counter()
    for line in open(results_path, encoding="utf-8"):
        r = json.loads(line)
        body = (r.get("response") or {}).get("body") or {}
        u = body.get("usage") or {}
        usage["input"] += u.get("input_tokens", 0)
        usage["output"] += u.get("output_tokens", 0)
        usage["reasoning"] += (u.get("output_tokens_details") or {}).get("reasoning_tokens", 0)
        usage["requests"] += 1
        echo[(body.get("model"), (body.get("reasoning") or {}).get("effort"), body.get("status"))] += 1
    return usage, echo


def retry_one(client, model, effort, etype, ctx, prompts="default"):
    """One synchronous Responses API call with the batch prompt and settings."""
    P = prompt_set(prompts)
    prompt = P.CHARACTERIZE_ENTITIES_PROMPT.format(entities_json=json.dumps([ctx], indent=2),
                                                   type_guidance=P.CHARACTERIZE_TYPE_GUIDANCE[etype])
    resp = client.responses.create(model=model, reasoning={"effort": effort},
                                   input=[{"role": "system", "content": SYSTEM_PROMPT},
                                          {"role": "user", "content": prompt}],
                                   text={"format": {"type": "json_object"}}, max_output_tokens=OPENAI_MAX_OUTPUT_TOKENS)
    parsed = json.loads(resp.output_text)
    text, sections = compose_sections(etype, parsed, P)
    return {"characterization": text, "characterization_sections": sections,
            "usage": (resp.usage.input_tokens, resp.usage.output_tokens), "model": resp.model}


def check_characterizations(input_json, output_json, min_papers: int = 3, retry: bool = False,
                            model: str = "gpt-5.4", reasoning_effort: str = "high", workers: int = 8,
                            prompts="default", client=None) -> dict:
    """Check the summaries in ``output_json`` against the network in ``input_json`` they were
    built from; write ``<output>.checks.json`` and return its summary. With ``retry``,
    entities with hard problems are sent once more (``client`` defaults to the OpenAI client)."""
    P = prompt_set(prompts)
    src = json.load(open(input_json, encoding="utf-8"))
    out = json.load(open(output_json, encoding="utf-8"))
    index = {e["canonical_name"]: (et, e) for et in TYPES for e in src.get(et) or []}
    contexts, report = {}, {}
    normalized = 0
    entity_names = sorted({e["canonical_name"] for et in TYPES for e in src.get(et) or []
                           if not e.get("expert_removed")}, key=len, reverse=True)
    for et in TYPES:
        for i, e in enumerate(out.get(et) or []):
            if not in_scope(e, min_papers):
                continue
            s = src[et][i]
            if s["canonical_name"] != e["canonical_name"]:
                raise ValueError(f"{output_json} does not line up with {input_json}: {et}[{i}] is "
                                 f"{e['canonical_name']!r} there and {s['canonical_name']!r} here")
            ctx = build_entity_context(s, et, src.get("relationships") or [], index)
            contexts[(et, i)] = ctx
            if normalize_entity(et, e, P):
                normalized += 1
            hard, soft = check(et, e, ctx, P, entity_names)
            report[(et, i)] = {"name": e["canonical_name"], "type": et, "hard": hard, "soft": soft}

    retries = {"attempted": 0, "kept": 0, "still_failing": 0, "errors": 0, "input_tokens": 0, "output_tokens": 0}
    failing = [k for k, v in report.items() if v["hard"]]
    if retry and failing:
        if client is None:
            from aiconstructlexis.providers.clients import init_openai_client
            client = init_openai_client()
        retries["attempted"] = len(failing)

        def job(key):
            et, i = key
            return key, retry_one(client, model, reasoning_effort, et, contexts[key], P)

        with ThreadPoolExecutor(workers) as ex:
            futs = [ex.submit(job, k) for k in failing]
            for f in as_completed(futs):
                try:
                    key, r = f.result()
                except Exception as exc:  # noqa: BLE001
                    retries["errors"] += 1
                    logger.warning("retry error: %s", exc)
                    continue
                et, i = key
                retries["input_tokens"] += r["usage"][0]
                retries["output_tokens"] += r["usage"][1]
                trial = dict(out[et][i], characterization=r["characterization"],
                             characterization_sections=r["characterization_sections"])
                normalize_entity(et, trial, P)
                hard, soft = check(et, trial, contexts[key], P, entity_names)
                before = report[key]["hard"]
                if r["characterization"] and len(hard) < len(before):
                    out[et][i] = trial
                    report[key].update(hard=hard, soft=soft, retried="kept", hard_before_retry=before)
                    retries["kept"] += 1
                else:
                    report[key].update(retried="kept original", retry_hard=hard)
                if report[key]["hard"]:
                    retries["still_failing"] += 1

    if normalized or retries["attempted"]:
        tmp = Path(output_json).with_suffix(".tmp.json")
        tmp.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        tmp.replace(output_json)
        logger.info("Rewrote %s: %d summaries reworded; retries %s", output_json, normalized, retries)

    rows = list(report.values())
    hard_kinds = collections.Counter(h.split(":")[0] for r in rows for h in r["hard"])
    soft_kinds = collections.Counter(s.split(":")[0] for r in rows for s in r["soft"])
    words = sorted(len((out[et][i].get("characterization") or "").split()) for et, i in report)
    results_path = Path(output_json).with_suffix(".batch_results.jsonl")
    usage, echo = batch_usage(results_path) if results_path.exists() else (collections.Counter(), collections.Counter())
    pin, pout = PRICES.get(model, (0, 0))
    summary = {
        "entities_checked": len(rows),
        "reworded": normalized,
        "by_type": dict(collections.Counter(r["type"] for r in rows)),
        "with_hard_problems": sum(1 for r in rows if r["hard"]),
        "hard_problem_kinds": dict(hard_kinds),
        "soft_flag_kinds": dict(soft_kinds),
        "words": {"median": words[len(words) // 2] if words else 0, "min": words[0] if words else 0,
                  "max": words[-1] if words else 0},
        "batch_usage": dict(usage),
        "batch_cost_usd": round(usage["input"] / 1e6 * pin + usage["output"] / 1e6 * pout, 2),
        "batch_echo": {f"{m} | effort {e} | {s}": n for (m, e, s), n in echo.items()},
        "retries": retries,
        "retry_cost_usd": round(retries["input_tokens"] / 1e6 * pin * 2 + retries["output_tokens"] / 1e6 * pout * 2, 2),
    }
    checks_path = Path(output_json).with_suffix(".checks.json")
    if checks_path.exists():
        # A check run without retries keeps the record of an earlier retry pass.
        prev = json.loads(checks_path.read_text(encoding="utf-8"))
        ps = prev.get("summary") or {}
        if not retry and (ps.get("retries") or {}).get("attempted"):
            summary["retries"], summary["retry_cost_usd"] = ps["retries"], ps.get("retry_cost_usd", 0)
        prev_rows = {(r["type"], r["name"]): r for r in prev.get("entities") or []}
        for r in rows:
            for k in ("retried", "hard_before_retry", "retry_hard"):
                if k not in r and k in prev_rows.get((r["type"], r["name"]), {}):
                    r[k] = prev_rows[(r["type"], r["name"])][k]
    checks_path.write_text(json.dumps({"summary": summary, "entities": rows}, indent=2, ensure_ascii=False),
                           encoding="utf-8")
    logger.info("Checked %d summaries; %d with hard problems; wrote %s",
                len(rows), summary["with_hard_problems"], checks_path)
    for r in rows:
        if r["hard"]:
            logger.info("  %s | %s | %s", r["type"][:-1], r["name"], "; ".join(r["hard"]))
    return summary


def main(argv=None) -> None:
    from aiconstructlexis.util.logging import setup_logging

    ap = argparse.ArgumentParser(description="Check the per-entity summaries and optionally retry hard failures once.")
    ap.add_argument("--input", required=True, help="network the summaries were built from")
    ap.add_argument("--output", required=True, help="summarized network (rewritten with --retry)")
    ap.add_argument("--min-papers", type=int, default=3)
    ap.add_argument("--retry", action="store_true", help="retry entities with hard problems once")
    ap.add_argument("--model", default="gpt-5.4")
    ap.add_argument("--reasoning-effort", default="high")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--prompts", default="default", help="prompt set: 'default' or a dotted module path")
    ap.add_argument("--log-dir", default="logs")
    args = ap.parse_args(argv)
    setup_logging(run_name="summarize_checks", log_dir=args.log_dir)
    summary = check_characterizations(input_json=args.input, output_json=args.output, min_papers=args.min_papers,
                                      retry=args.retry, model=args.model, reasoning_effort=args.reasoning_effort,
                                      workers=args.workers, prompts=args.prompts)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
