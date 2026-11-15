"""Build the three derived data files of the safety case study from the raw
leaderboard exports in data/safety/raw/.

  raw/safetywashing_chat.csv        -> analysis_dataset.json
  raw/helm_safety_scenarios.json    -> helm_safety.json
  raw/airbench.json                 -> air_refusal.json

Run from this directory:
  python prepare_safety_data.py           rebuild the derived files
  python prepare_safety_data.py --check   rebuild in memory and compare with
                                          the shipped derived files
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "safety"
RAW = DATA / "raw"

# Safetywashing battery columns kept for the analysis. The HarmBench columns
# are the "all"-category aggregates of each attack condition.
BATTERY_COLUMNS = {
    "model": "model",
    "harmbench_direct": "HarmBench-DirectRequest-all",
    "harmbench_gcg": "HarmBench-GCG-T-all",
    "harmbench_tap": "HarmBench-TAP-T-all",
    "harmbench_human": "HarmBench-HumanJailbreaks-all",
    "beavertails": "beavertails",
    "toxigen": "toxigen",
    "safety_bench": "safety_bench",
    "truthfulqa": "truthfulqa_mc1",
    "mmlu": "mmlu",
    "gsm8k": "gsm8k",
    "model_size": "model_size",
}

# HELM Safety "Accuracy" table columns kept for the analysis.
HELM_COLUMNS = {
    "mean": "Mean score",
    "harmbench": "HarmBench - LM Evaluated Safety score",
    "sst": "SimpleSafetyTests - LM Evaluated Safety score",
    "bbq": "BBQ - BBQ accuracy",
    "redteam": "Anthropic Red Team - LM Evaluated Safety score",
    "xstest": "XSTest - LM Evaluated Safety score",
}
AIR_COLUMN = "Refusal Rate"


def table_rows(table: dict) -> dict[str, dict[str, float | None]]:
    """Turn a HELM leaderboard table into {model: {column: value}}."""
    header = [h["value"] for h in table["header"]]
    rows = {}
    for row in table["rows"]:
        values = [cell.get("value") for cell in row]
        rows[values[0]] = dict(zip(header[1:], values[1:]))
    return rows


def build_battery() -> list[dict]:
    frame = pd.read_csv(RAW / "safetywashing_chat.csv")
    sub = frame[list(BATTERY_COLUMNS.values())].copy()
    sub.columns = list(BATTERY_COLUMNS.keys())
    return [{k: (v if isinstance(v, str) else float(v)) for k, v in rec.items()}
            for rec in sub.to_dict(orient="records")]


def build_helm() -> dict[str, dict]:
    tables = json.loads((RAW / "helm_safety_scenarios.json").read_text())
    accuracy = next(t for t in tables if t["title"] == "Accuracy")
    rows = table_rows(accuracy)
    return {model: {key: row[col] for key, col in HELM_COLUMNS.items()}
            for model, row in rows.items()}


def build_air() -> dict[str, float | None]:
    tables = json.loads((RAW / "airbench.json").read_text())
    rows = table_rows(tables[0])
    return {model: row[AIR_COLUMN] for model, row in rows.items()}


def flatten(obj, prefix=""):
    """Yield (path, value) for every leaf of a nested JSON object."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from flatten(v, f"{prefix}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from flatten(v, f"{prefix}[{i}]")
    else:
        yield prefix, obj


def compare(name: str, built, shipped) -> list[str]:
    """Numerical comparison of two JSON objects; returns the differences."""
    a = dict(flatten(built))
    b = dict(flatten(shipped))
    problems = [f"{name}: path only in rebuilt: {p}" for p in a.keys() - b.keys()]
    problems += [f"{name}: path only in shipped: {p}" for p in b.keys() - a.keys()]
    for path in a.keys() & b.keys():
        x, y = a[path], b[path]
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            if not math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-12):
                problems.append(f"{name}: {path}: rebuilt {x!r} vs shipped {y!r}")
        elif x != y:
            problems.append(f"{name}: {path}: rebuilt {x!r} vs shipped {y!r}")
    return problems


OUTPUTS = {
    "analysis_dataset.json": build_battery,
    "helm_safety.json": build_helm,
    "air_refusal.json": build_air,
}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true",
                        help="compare the rebuilt files with the shipped ones instead of writing")
    args = parser.parse_args(argv)

    problems = []
    for filename, build in OUTPUTS.items():
        built = build()
        target = DATA / filename
        if args.check:
            shipped = json.loads(target.read_text())
            diffs = compare(filename, built, shipped)
            n = len(built)
            status = "matches" if not diffs else f"{len(diffs)} differences"
            print(f"{filename}: {n} records, {status}")
            problems += diffs
        else:
            target.write_text(json.dumps(built, indent=1) + "\n")
            print(f"wrote {target.relative_to(HERE).as_posix()} ({len(built)} records)")
    for line in problems[:50]:
        print("  " + line)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
