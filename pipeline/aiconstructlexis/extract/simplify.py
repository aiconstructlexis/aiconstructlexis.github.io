"""Reduce an extraction file to the fields the harmonization stages read.

Input: the per-paper extraction JSON written by the extraction stage
(``inputs/extraction.json``): a ``{paper_name: record}`` object (a list of
records is also accepted) where each record carries ``result.parsed_text``
with the ``"Nomological Network"`` object and, optionally, ``result.raw_text``.

Output: ``{paper_name: {name, url, path, parsed_text[, raw_text]}}``. The
``parsed_text`` structure is kept exactly as extraction produced it, so the
aggregation and export stages read the same shape.

Rules:
  * ``result.parsed_text`` is used as-is when it is a non-empty dict, even when
    it carries an ``error`` key (later stages decide what to skip).
  * When ``parsed_text`` is a string, or missing, the raw model output
    (``raw_text``) is parsed instead: Markdown fences are removed and the text
    is read as a Python literal, then as JSON, then as JSON without its last
    character (a common trailing-brace defect).
  * Papers with no parseable output are dropped and counted as skipped.
"""

from __future__ import annotations

import argparse
import ast
import json
import logging
from pathlib import Path

from aiconstructlexis.util.logging import log_counts, setup_logging

logger = logging.getLogger(__name__)


def _strip_markdown_fences(text: str) -> str:
    """Remove a ```json ... ``` wrapper if present."""
    s = text.strip()
    if s.startswith("```"):
        lines = s.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        s = "\n".join(lines).strip()
    return s


def _parse_raw_fallback(raw_text):
    """Parse raw model output into a dict ({} when it cannot be parsed)."""
    if not raw_text or not isinstance(raw_text, str):
        return {}
    s = _strip_markdown_fences(raw_text)
    if not s:
        return {}
    if not (s.startswith("{") and s.endswith("}")):
        return {}
    try:
        return ast.literal_eval(s)
    except (ValueError, SyntaxError):
        pass
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        try:
            return json.loads(s[:-1])
        except json.JSONDecodeError:
            return {}
    return {}


def simplify(input_json, output_json, keep_raw: bool = True) -> Path:
    """Write the simplified form of ``input_json`` to ``output_json`` and return its path.

    Each kept record has ``name``, ``url``, ``path`` and ``parsed_text``; with
    ``keep_raw`` the model's ``raw_text`` is kept as well when present.
    """
    input_file, output_file = Path(input_json), Path(output_json)
    logger.info("Loading %s", input_file)
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    is_dict = isinstance(data, dict)
    simplified = {}
    skipped = 0

    for key, paper_data in data.items() if is_dict else enumerate(data):
        if not is_dict:
            key = paper_data.get("name", f"paper_{key}")

        result = paper_data.get("result", {})
        parsed_text = result.get("parsed_text")
        raw_text = result.get("raw_text", "")

        # Prefer the dict extraction already parsed; re-parse raw_text only when needed.
        if isinstance(parsed_text, str):
            parsed_text = _parse_raw_fallback(parsed_text) or _parse_raw_fallback(raw_text)
        elif isinstance(parsed_text, dict) and parsed_text:
            pass  # used as-is, with or without an error key (later stages decide)
        else:
            parsed_text = _parse_raw_fallback(raw_text)

        if not parsed_text or not isinstance(parsed_text, dict):
            skipped += 1
            continue

        entry = {
            "name": paper_data.get("name", key),
            "url": paper_data.get("url", ""),
            "path": paper_data.get("path", ""),
            "parsed_text": parsed_text,
        }
        if keep_raw and raw_text:
            entry["raw_text"] = raw_text
        simplified[key] = entry

    log_counts(logger, "Simplify results", processed=len(simplified), skipped=skipped)
    logger.info("Writing to %s", output_file)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(simplified, f, indent=2, ensure_ascii=False)

    size_mb_in = input_file.stat().st_size / 1024 / 1024
    size_mb_out = output_file.stat().st_size / 1024 / 1024
    logger.info("Saved %s  (%.1fMB -> %.1fMB)", output_file, size_mb_in, size_mb_out)
    return output_file


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Reduce an extraction JSON to the fields the harmonization stages read.")
    parser.add_argument("--input", "-i", required=True, help="Extraction JSON (inputs/extraction.json)")
    parser.add_argument("--output", "-o", default=None,
                        help="Output JSON (default: simplified.json next to the input)")
    parser.add_argument("--no-raw", action="store_true", help="Omit raw_text from the output")
    parser.add_argument("--log-dir", default="logs", help="Directory for the run log (default: logs)")
    return parser


def main(argv=None) -> Path:
    args = build_arg_parser().parse_args(argv)
    setup_logging(run_name="simplify", log_dir=args.log_dir)
    input_file = Path(args.input)
    if not input_file.exists():
        raise SystemExit(f"Input file {input_file} does not exist")
    output_file = Path(args.output) if args.output else input_file.with_name("simplified.json")
    return simplify(input_file, output_file, keep_raw=not args.no_raw)


if __name__ == "__main__":
    main()
