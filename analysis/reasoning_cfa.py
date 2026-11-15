"""Reasoning case study: confirmatory factor analysis of the hierarchy
Reasoning > Mathematical Reasoning > Arithmetic Reasoning.

The AI Construct Lexis records Reasoning and Mathematical Reasoning as
correlated constructs (a `correlates` relationship) and lists the benchmarks
claimed to operationalize them (ARC-Challenge, MMLU, WinoGrande and GSM8K for
Reasoning; GSM8K, MATH, of which MATH-Lvl-5 is the hardest level, and parts of
MMLU for Mathematical Reasoning). The Open LLM Leaderboard reports no MMLU
subset score, so the full MMLU score stands in for the MMLU-STEM and MMLU-Math
claims. The case study adds one hypothetical claim, an Arithmetic Reasoning
construct operationalized by GSM8K, and asks what confirmatory factor analysis
can establish about the resulting hierarchy from benchmark scores alone.

Data: the joined Hugging Face Open LLM Leaderboard v1 and v2 sample
(data/reasoning/open_llm_leaderboard_v1_v2.csv, n = 400 models). All models
are fitted by maximum likelihood in semopy on standardized scores and
reported with standardized estimates.

Run from this directory:  python reasoning_cfa.py
Writes results/reasoning_results.json.
"""
from __future__ import annotations

import json
import re
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import semopy
from scipy import stats

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "reasoning" / "open_llm_leaderboard_v1_v2.csv"
OUT = HERE / "results" / "reasoning_results.json"

INDICATORS = ["arc", "mmlu", "winogrande", "gsm8k", "math_lvl5"]
LABELS = {
    "arc": "ARC-Challenge",
    "mmlu": "MMLU",
    "winogrande": "WinoGrande",
    "gsm8k": "GSM8K",
    "math_lvl5": "MATH-Lvl-5",
}

# Approach 1: each indicator loads on its narrowest claimed construct; the
# broader constructs reach it through structural regressions. GSM8K is the
# only Arithmetic indicator, so the Arithmetic factor follows the
# single-indicator convention: loading fixed to 1 (semopy fixes the first
# loading of every latent to 1) and residual variance fixed to 0.
HIERARCHICAL = """
reasoning  =~ arc + winogrande
math       =~ mmlu + math_lvl5
arithmetic =~ gsm8k
math       ~ reasoning
arithmetic ~ math
gsm8k ~~ 0*gsm8k
"""

# Comparison: one general factor over the five indicators.
ONE_FACTOR = "g =~ arc + winogrande + mmlu + math_lvl5 + gsm8k"

# Equivalent two-level model: GSM8K loads directly on Mathematical Reasoning.
TWO_LEVEL = """
reasoning =~ arc + winogrande
math      =~ mmlu + math_lvl5 + gsm8k
math      ~ reasoning
"""

# Approach 2: bifactor model with a general Reasoning factor on every
# indicator and an orthogonal Numerical factor on the math-claimed ones.
BIFACTOR = """
reasoning =~ arc + mmlu + math_lvl5 + winogrande + gsm8k
numerical =~ mmlu + math_lvl5 + gsm8k
reasoning ~~ 0*numerical
"""


# ---------------------------------------------------------------------------
# Fitting helpers
# ---------------------------------------------------------------------------
def standardize(frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    sub = frame[columns]
    return (sub - sub.mean()) / sub.std()


def independence_baseline(Z: pd.DataFrame) -> tuple[float, int]:
    """Chi-square and degrees of freedom of the independence (null) model.

    semopy derives CFI and TLI from a baseline model that inherits every
    constraint of the fitted model. When a residual variance is fixed to zero,
    that baseline is degenerate and the two indices are undefined, so both
    case studies compute them from the standard independence baseline (all
    indicators uncorrelated), whose maximum-likelihood chi-square on
    standardized data is n * (-log det R). For models without fixed variances
    this equals semopy's own baseline, which fit_model verifies.
    """
    n, p = Z.shape
    R = np.corrcoef(Z.to_numpy(), rowvar=False)
    _, logdet = np.linalg.slogdet(R)
    return float(-n * logdet), p * (p - 1) // 2


def latents_of(spec: str) -> list[str]:
    return [line.split("=~")[0].strip() for line in spec.splitlines() if "=~" in line]


def observed_of(spec: str, Z: pd.DataFrame) -> list[str]:
    return [c for c in Z.columns if re.search(rf"\b{re.escape(c)}\b", spec)]


def fit_model(name: str, spec: str, Z: pd.DataFrame) -> dict:
    """Fit `spec` on the standardized indicators it names and collect fit
    indices and parameter estimates (raw and standardized)."""
    cols = observed_of(spec, Z)
    data = Z[cols]
    model = semopy.Model(spec)
    model.fit(data)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        s = semopy.calc_stats(model).T.squeeze()

    chi2, df = float(s["chi2"]), int(s["DoF"])
    base_chi2, base_df = independence_baseline(data)
    cfi = 1.0 - max(chi2 - df, 0.0) / max(base_chi2 - base_df, chi2 - df, 1e-12)
    tli = ((base_chi2 / base_df) - (chi2 / df)) / ((base_chi2 / base_df) - 1.0)
    # semopy's baseline chi-square is infinite when a variance is fixed to
    # zero; whenever it is finite, semopy's CFI and TLI must agree with ours.
    if np.isfinite(float(s["chi2 Baseline"])):
        for key, value in (("CFI", cfi), ("TLI", tli)):
            own = float(s[key])
            if abs(own - value) > 1e-6:
                raise RuntimeError(f"{name}: {key} {value:.6f} disagrees with semopy's {own:.6f}")

    fit = {
        "n": int(len(data)),
        "df": df,
        "chi2": chi2,
        "p": float(stats.chi2.sf(chi2, df)),
        "CFI": float(cfi),
        "TLI": float(tli),
        "RMSEA": float(s["RMSEA"]),
        "baseline_chi2": base_chi2,
        "baseline_df": base_df,
    }
    params = []
    for _, r in model.inspect(std_est=True).iterrows():
        params.append({
            "lval": r["lval"], "op": r["op"], "rval": r["rval"],
            "estimate": float(r["Estimate"]),
            "std_estimate": None if pd.isna(r["Est. Std"]) else float(r["Est. Std"]),
            "fixed": bool(r["Std. Err"] == "-"),
        })
    return {"name": name, "spec": spec.strip(), "latents": latents_of(spec),
            "observed": cols, "fit": fit, "parameters": params}


def std_of(result: dict, lval: str, rval: str, op: str = "~") -> float:
    for p in result["parameters"]:
        if p["op"] == op and p["lval"] == lval and p["rval"] == rval:
            return p["std_estimate"]
    raise KeyError((lval, op, rval))


def report(result: dict) -> None:
    f = result["fit"]
    latents = set(result["latents"])
    print(f"\n== {result['name']} ==")
    print(f"  chi2({f['df']}) = {f['chi2']:.1f}, p = {f['p']:.3g}, "
          f"CFI = {f['CFI']:.3f}, TLI = {f['TLI']:.3f}, RMSEA = {f['RMSEA']:.3f}")
    print("  standardized loadings:")
    for lat in result["latents"]:
        items = [p for p in result["parameters"]
                 if p["op"] == "~" and p["rval"] == lat and p["lval"] not in latents]
        print(f"    {lat:10s} " + ", ".join(
            f"{LABELS.get(p['lval'], p['lval'])} {p['std_estimate']:+.2f}" for p in items))
    structural = [p for p in result["parameters"]
                  if p["op"] == "~" and p["lval"] in latents and p["rval"] in latents]
    if structural:
        print("  standardized structural coefficients:")
        for p in structural:
            print(f"    {p['rval']} -> {p['lval']}: {p['std_estimate']:+.2f}")
    at_bound = [p["lval"] for p in result["parameters"]
                if p["op"] == "~~" and p["lval"] == p["rval"] and not p["fixed"]
                and p["lval"] not in latents and abs(p["estimate"]) < 1e-6]
    if at_bound:
        print("  residual variances at the zero boundary: "
              + ", ".join(LABELS.get(v, v) for v in at_bound))


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def partial_corr(frame: pd.DataFrame, x: str, y: str, given: str) -> float:
    """Pearson correlation of x and y after regressing each on `given`."""
    g = frame[given]

    def residual(v):
        return v - np.polyval(np.polyfit(g, v, 1), g)

    return float(np.corrcoef(residual(frame[x]), residual(frame[y]))[0, 1])


def main() -> None:
    d = pd.read_csv(DATA)
    n = len(d)
    print("Reasoning case study: Open LLM Leaderboard v1 and v2 joined sample")
    print(f"n = {n} models")

    corr = d[INDICATORS + ["log10_params"]].corr()
    print("\nPearson correlations:")
    print(corr.rename(index=LABELS, columns=LABELS).round(2).to_string())

    r_partial = partial_corr(d, "winogrande", "gsm8k", "log10_params")
    r_raw = float(corr.loc["winogrande", "gsm8k"])
    print(f"\nr(WinoGrande, GSM8K) = {r_raw:.2f}")
    print(f"partial r(WinoGrande, GSM8K | log10 params) = {r_partial:.2f}")

    Z = standardize(d, INDICATORS)
    hier = fit_model("Hierarchical CFA: reasoning > math > arithmetic (Approach 1)", HIERARCHICAL, Z)
    report(hier)
    one = fit_model("One-factor comparison model", ONE_FACTOR, Z)
    report(one)
    delta = one["fit"]["chi2"] - hier["fit"]["chi2"]
    delta_df = one["fit"]["df"] - hier["fit"]["df"]
    delta_p = float(stats.chi2.sf(delta, delta_df))
    print(f"\n  hierarchical vs one-factor: delta chi2({delta_df}) = {delta:.1f}, p = {delta_p:.3g}")

    two = fit_model("Two-level model: gsm8k loads on math directly", TWO_LEVEL, Z)
    report(two)
    print(f"\n  chi2 difference between the three-level and two-level models: "
          f"{abs(two['fit']['chi2'] - hier['fit']['chi2']):.2e}")
    print(f"  GSM8K loading on math in the two-level model: {std_of(two, 'gsm8k', 'math'):+.2f}; "
          f"beta math -> arithmetic in the three-level model: {std_of(hier, 'arithmetic', 'math'):+.2f}")

    bif = fit_model("Bifactor CFA: general reasoning + orthogonal numerical (Approach 2)", BIFACTOR, Z)
    report(bif)
    print("  communalities h2 = lambda_R^2 + lambda_N^2:")
    communalities = {}
    for ind in ["arc", "mmlu", "winogrande", "gsm8k", "math_lvl5"]:
        lr = std_of(bif, ind, "reasoning")
        ln = std_of(bif, ind, "numerical") if ind in ("mmlu", "math_lvl5", "gsm8k") else None
        h2 = lr ** 2 + (ln ** 2 if ln is not None else 0.0)
        communalities[ind] = {"lambda_reasoning": lr, "lambda_numerical": ln, "h2": h2}
        ln_txt = f"{ln:+.2f}" if ln is not None else "  -- "
        print(f"    {LABELS[ind]:13s} lambda_R {lr:+.2f}  lambda_N {ln_txt}  h2 {100 * h2:.0f}%")

    print("\nFit summary")
    print(f"{'model':14s} {'chi2':>7s} {'df':>3s} {'CFI':>6s} {'TLI':>6s} {'RMSEA':>6s}")
    for label, res in (("hierarchical", hier), ("one-factor", one),
                       ("two-level", two), ("bifactor", bif)):
        f = res["fit"]
        print(f"{label:14s} {f['chi2']:7.1f} {f['df']:3d} {f['CFI']:6.3f} {f['TLI']:6.3f} {f['RMSEA']:6.3f}")

    OUT.parent.mkdir(exist_ok=True)
    results = {
        "data": DATA.relative_to(HERE).as_posix(),
        "n": n,
        "indicators": INDICATORS,
        "correlations": corr.round(6).to_dict(),
        "r_winogrande_gsm8k": r_raw,
        "partial_r_winogrande_gsm8k_given_log10_params": r_partial,
        "models": {"hierarchical": hier, "one_factor": one, "two_level": two, "bifactor": bif},
        "hierarchical_vs_one_factor": {"delta_chi2": delta, "delta_df": delta_df, "p": delta_p},
        "bifactor_communalities": communalities,
        "software": {"semopy": semopy.__version__, "pandas": pd.__version__,
                     "numpy": np.__version__},
    }
    OUT.write_text(json.dumps(results, indent=1))
    print(f"\nwrote {OUT.relative_to(HERE).as_posix()}")


if __name__ == "__main__":
    main()
