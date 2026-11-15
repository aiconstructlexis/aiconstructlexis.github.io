"""Screen a paper list for relevance to large language models.

Input: a paper list JSON as written by the ingest stage, one record per paper with at
least ``name`` (title) and ``path`` (the downloaded PDF). Output: the same list, same
order and schema, with ``is_LLM_paper`` (bool) added to every screened paper, plus a run
report ``<output>.screen_report.json`` (provider, model, prompt fingerprint, counts).

Each paper is classified from the main text of its PDF (the first N pages, where N is the
venue's main-body page limit plus one or two pages of buffer, cut at the References
heading; see ``aiconstructlexis.screen._common.CONFERENCE_PAGE_LIMITS``) with the
``SCREENING_PAPERS_PROMPT`` of the chosen prompt set, which asks for a one-word Yes/No
answer; the verdict is whether the answer starts with "yes". Two modes:

* ``batch`` (default): the Together Batch API, one job per request-file part
  (``aiconstructlexis.screen._batch``). Provider must be ``together``.
* ``sync``: direct chat-completion calls through the provider's OpenAI-compatible endpoint
  (``openai``, ``google`` or ``together``) from a thread pool (``aiconstructlexis.screen._sync``).

Both modes skip papers that already have a verdict and leave papers with a missing PDF
unscreened (``screen_note="missing_pdf"``). A PDF with no extractable text is recorded as
not LLM-related (``is_LLM_paper`` False, ``screen_note="empty_pdf"``) without a model
call. An empty model answer is retried once with a larger output-token cap; a paper whose
answer stays empty, or whose request failed, carries no verdict and ``screen_error``
(``"empty_answer"`` or the error text) and is screened again by the next run. Record
conventions are documented in ``aiconstructlexis.screen._common``.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from aiconstructlexis.providers.clients import PROVIDERS
from aiconstructlexis.screen._batch import screen_batch
from aiconstructlexis.screen._common import DEFAULT_PAGE_LIMIT
from aiconstructlexis.screen._sync import screen_sync
from aiconstructlexis.util.logging import setup_logging

DEFAULT_PROVIDER = "together"
DEFAULT_MODEL = "openai/gpt-oss-120b"
MODES = ("batch", "sync")


def screen_papers(input_json, output_json, provider: str = DEFAULT_PROVIDER,
                  model: str = DEFAULT_MODEL, mode: str = "batch",
                  prompts: str | None = "default", workers: int = 8, max_rpm: int = 3600,
                  poll_interval: int = 60, save_every: int = 50, retry_empty: bool = True,
                  retry_max_tokens: int = 2048, conference: str | None = None) -> Path:
    """Screen the papers in ``input_json`` and write the screened list to ``output_json``.

    Args:
        input_json: Paper list JSON. ``output_json`` may be the same file (screened in place).
        provider: ``together``, ``openai`` or ``google``; batch mode requires ``together``.
        model: Model name as the provider expects it.
        mode: ``batch`` (Together Batch API) or ``sync`` (direct calls).
        prompts: Prompt set: ``"default"`` or a dotted module path defining
            ``SCREENING_PAPERS_PROMPT``.
        workers: sync: concurrent requests; batch: PDF text extraction processes
            (0 uses every CPU, 1 extracts in the calling process).
        max_rpm: sync: requests-per-minute cap shared by the workers.
        poll_interval: batch: seconds between batch status polls.
        save_every: sync: checkpoint the output every N screened papers.
        retry_empty: Retry an empty model answer once with ``retry_max_tokens``.
        retry_max_tokens: Output-token cap for that retry (the first attempt uses 512).
        conference: Venue key for the main-text page limit (neurips, iclr, icml, acl, emnlp,
            naacl); inferred from the input path when None. Unknown venues read
            ``DEFAULT_PAGE_LIMIT`` (12) pages, the same count the extraction stage reads.

    Returns the output path.
    """
    if mode == "batch":
        if provider != "together":
            raise ValueError(
                f"Batch-mode screening runs on the Together Batch API; provider {provider!r} "
                "needs mode='sync'."
            )
        screen_batch(input_json, output_json, model=model, prompts=prompts, workers=workers,
                     poll_interval=poll_interval, retry_empty=retry_empty,
                     retry_max_tokens=retry_max_tokens, conference=conference)
    elif mode == "sync":
        if provider not in PROVIDERS:
            raise ValueError(f"Unknown provider {provider!r}; expected one of {', '.join(PROVIDERS)}")
        screen_sync(input_json, output_json, provider=provider, model=model, prompts=prompts,
                    workers=workers, max_rpm=max_rpm, save_every=save_every,
                    retry_empty=retry_empty, retry_max_tokens=retry_max_tokens,
                    conference=conference)
    else:
        raise ValueError(f"Unknown mode {mode!r}; expected one of {', '.join(MODES)}")
    return Path(output_json)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Screen a paper list for relevance to large language models")
    parser.add_argument("--input", required=True, help="Paper list JSON (from the ingest stage)")
    parser.add_argument("--output", default=None,
                        help="Screened list JSON (default: screen --input in place)")
    parser.add_argument("--provider", default=DEFAULT_PROVIDER, choices=PROVIDERS,
                        help="API provider (batch mode: together only)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model name")
    parser.add_argument("--mode", default="batch", choices=MODES,
                        help="batch: Together Batch API; sync: one chat-completion call per paper")
    parser.add_argument("--prompts", default="default",
                        help="Prompt set: 'default' or a dotted module path defining "
                             "SCREENING_PAPERS_PROMPT")
    parser.add_argument("--workers", type=int, default=8,
                        help="sync: concurrent requests; batch: PDF text extraction processes "
                             "(0 = all CPUs, 1 = no subprocesses)")
    parser.add_argument("--max-rpm", type=int, default=3600, help="sync: requests per minute")
    parser.add_argument("--poll-interval", type=int, default=60,
                        help="batch: seconds between status polls")
    parser.add_argument("--save-every", type=int, default=50,
                        help="sync: checkpoint the output every N papers")
    parser.add_argument("--no-retry-empty", action="store_true",
                        help="Do not retry an empty model answer; flag the paper with "
                             "screen_error=empty_answer")
    parser.add_argument("--retry-max-tokens", type=int, default=2048,
                        help="Output-token cap for the retry after an empty answer (the first "
                             "attempt uses 512, which a reasoning model can spend before answering)")
    parser.add_argument("--conference", default=None,
                        help="Venue key for the main-text page limit (neurips, iclr, icml, acl, "
                             "emnlp, naacl); inferred from the input path when omitted; unknown "
                             f"venues read {DEFAULT_PAGE_LIMIT} pages")
    parser.add_argument("--log-dir", default="logs", help="Directory for the run log")
    args = parser.parse_args(argv)

    setup_logging(run_name="screen", log_dir=args.log_dir)
    return screen_papers(
        args.input, args.output or args.input, provider=args.provider, model=args.model,
        mode=args.mode, prompts=args.prompts, workers=args.workers, max_rpm=args.max_rpm,
        poll_interval=args.poll_interval, save_every=args.save_every,
        retry_empty=not args.no_retry_empty, retry_max_tokens=args.retry_max_tokens,
        conference=args.conference,
    )


if __name__ == "__main__":
    main()
