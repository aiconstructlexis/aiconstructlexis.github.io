"""The ``lexis`` command.

    lexis run --config CONFIG [--stages s1,s2] [--venues v1 v2] [--dry-run]
    lexis plan --config CONFIG [--stages ...] [--venues ...]
    lexis check-config CONFIG
    lexis stages
    lexis prompts [NAME ...] [--set default]
    lexis check-export SITE_DIR NETWORK_JSON
    lexis version

Every stage can also be run on its own through its module, for example
``python -m aiconstructlexis.vote.relationships --help``.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import List, Optional

from aiconstructlexis import __version__
from aiconstructlexis.config import ConfigError, load_config, to_dict
from aiconstructlexis.pipeline import STAGES, StageError, plan, run

PROMPT_NAMES = (
    "SCREENING_PAPERS_PROMPT", "EXTRACT_ENTITIES_PROMPT", "EXTRACT_RELATIONSHIPS_PROMPT",
    "AGGREGATE_CONSTRUCTS_PROMPT", "AGGREGATE_MEASUREMENTS_PROMPT", "AGGREGATE_BEHAVIORS_PROMPT",
    "MERGE_GROUPS_PROMPT", "CHARACTERIZE_ENTITIES_PROMPT",
)


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="lexis", description="Build the AI Construct Lexis from a configuration file.")
    p.add_argument("--log-dir", default=None, help="where run logs go (default: paths.log_dir of the config, i.e. logs/ next to the config file)")
    p.add_argument("-v", "--verbose", action="store_true", help="debug logging")
    sub = p.add_subparsers(dest="command", required=True)

    r = sub.add_parser("run", help="run the pipeline (all stages, or --stages)")
    r.add_argument("--config", required=True)
    r.add_argument("--stages", default=None, help=f"comma-separated subset of: {','.join(STAGES)}")
    r.add_argument("--venues", nargs="*", default=None, help="venue ids to process (default: all in the config)")
    r.add_argument("--dry-run", action="store_true", help="run only the extract stage as an estimate of its requests and cost, without calling any model")

    pl = sub.add_parser("plan", help="list the steps a run would take, without running them")
    pl.add_argument("--config", required=True)
    pl.add_argument("--stages", default=None)
    pl.add_argument("--venues", nargs="*", default=None)

    c = sub.add_parser("check-config", help="validate a configuration file and print it resolved")
    c.add_argument("config")

    sub.add_parser("stages", help="list the stages in order")

    pr = sub.add_parser("prompts", help="print the prompt texts of a prompt set")
    pr.add_argument("names", nargs="*", help=f"prompt constants to print (default: all of {', '.join(PROMPT_NAMES)})")
    pr.add_argument("--set", dest="prompt_set", default="default", help="prompt set: 'default' or a dotted module path")

    ce = sub.add_parser("check-export", help="check that a site's data matches the network it was exported from")
    ce.add_argument("site_dir")
    ce.add_argument("network_json")

    sub.add_parser("version", help="print the package version")
    return p


def _setup_logging(log_dir: Optional[str], run_name: str, verbose: bool) -> None:
    from aiconstructlexis.util.logging import setup_logging
    setup_logging(run_name=run_name, level=logging.DEBUG if verbose else logging.INFO,
                  log_dir=Path(log_dir) if log_dir else None)


def main(argv: Optional[List[str]] = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "version":
            print(__version__)
            return 0
        if args.command == "stages":
            for s in STAGES:
                print(s)
            return 0
        if args.command == "prompts":
            from aiconstructlexis.prompts import load_prompts
            mod = load_prompts(args.prompt_set)
            names = args.names or list(PROMPT_NAMES)
            unknown = [n for n in names if not hasattr(mod, n)]
            if unknown:
                print(f"error: unknown prompt name(s) {', '.join(unknown)}; choose from {', '.join(PROMPT_NAMES)}", file=sys.stderr)
                return 2
            for name in names:
                text = getattr(mod, name)
                print(f"{'=' * 78}\n{name}\n{'=' * 78}\n{text if isinstance(text, str) else json.dumps(text, indent=2)}\n")
            return 0
        if args.command == "check-config":
            cfg = load_config(args.config)
            print(json.dumps(to_dict(cfg), indent=2))
            print(f"\nOK: {len(cfg.venues)} venue(s), {len(cfg.all_model_labels())} extraction model label(s)", file=sys.stderr)
            return 0
        if args.command == "check-export":
            from aiconstructlexis.export import check_site_export
            problems = check_site_export(site_dir=Path(args.site_dir), network_json=Path(args.network_json))
            if problems:
                print(f"FAILED: {len(problems)} problem(s)")
                for pr in problems[:50]:
                    print("  -", pr)
                return 1
            print("all checks passed")
            return 0
        cfg = load_config(args.config)
        if args.command == "plan":
            for line in plan(cfg, stages=[args.stages] if args.stages else None, venues=args.venues):
                print(line)
            return 0
        if args.command == "run":
            _setup_logging(args.log_dir or str(cfg.paths.log_dir), run_name="lexis", verbose=args.verbose)
            written = run(cfg, stages=[args.stages] if args.stages else None, venues=args.venues, dry_run=args.dry_run)
            for key, path in written.items():
                print(f"{key:>24}  {path}")
            return 0
    except (ConfigError, StageError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130
    except Exception as e:  # a stage failed: report it in one line, with the traceback under -v
        if args.verbose:
            raise
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
