"""Safety case study: confirmatory factor analysis of the safety construct
family under the hierarchy inferred from the literature's instrument claims.

Every construct and instrument comes from the measured_by relationships
recorded in the AI Construct Lexis: HarmBench is claimed for Safety,
Harmlessness and Adversarial Robustness, BeaverTails and ToxiGen for Safety
and Harmlessness, and TruthfulQA for Safety and Truthfulness. The Lexis also
records a related edge between Harmlessness and Safety, and no edge linking
Adversarial Robustness to Safety or to Harmlessness. Reading Safety as an
umbrella construct with the sub-constructs Harmlessness and Adversarial
Robustness is the authors' inference from HarmBench being claimed for all
three constructs together with the Harmlessness-Safety related edge.

Data (see data/README.md):
  Part A  Safetywashing battery (Ren et al., NeurIPS 2024), n = 26 open chat
          models: data/safety/analysis_dataset.json
  Part B  HELM Safety v1.17.0 (n = 87) and the AIR-Bench 2024 refusal rate
          (v1.19.0; n = 75 models joined by name): data/safety/helm_safety.json,
          data/safety/air_refusal.json

All models are fitted by maximum likelihood in semopy on standardized scores
and reported with standardized estimates.

Run from this directory:  python safety_cfa.py
Writes results/safety_results.json.
"""
from __future__ import annotations

import itertools
import json
import re
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import semopy
from scipy import stats

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "safety"
OUT = HERE / "results" / "safety_results.json"

BATTERY = ["harmbench_direct", "beavertails", "toxigen",
           "harmbench_gcg", "harmbench_tap", "harmbench_human", "truthfulqa", "mmlu"]
LABELS = {
    "harmbench_direct": "HarmBench DirectRequest",
    "harmbench_gcg": "HarmBench GCG-T",
    "harmbench_tap": "HarmBench TAP-T",
    "harmbench_human": "HarmBench HumanJailbreaks",
    "beavertails": "BeaverTails",
    "toxigen": "ToxiGen",
    "truthfulqa": "TruthfulQA",
    "mmlu": "MMLU",
    "harmbench": "HarmBench",
    "xstest": "XSTest",
    "sst": "SimpleSafetyTests",
    "redteam": "Anthropic Red Team",
    "air_refusal": "AIR-Bench 2024 refusal rate",
}
HARMLESSNESS = ["harmbench_direct", "beavertails", "toxigen"]
ATTACKS = ["harmbench_gcg", "harmbench_tap", "harmbench_human"]

# Instruments the Lexis records for each construct, at the level of the
# instrument (HarmBench is one instrument, represented by its direct-request
# score; the GCG-T attack condition stands for GCG, which the Lexis records
# as a second Adversarial Robustness instrument). Used for the same-construct
# correlation summary. The Lexis also records GCG for Harmlessness (one
# paper); the study treats the HarmBench attack conditions, GCG among them,
# as indicators of Adversarial Robustness and keeps that single-paper
# Harmlessness claim for GCG out of the Harmlessness pair set.
CLAIMED_INSTRUMENTS = {
    "Safety": ["harmbench_direct", "beavertails", "toxigen", "truthfulqa"],
    "Harmlessness": ["harmbench_direct", "beavertails", "toxigen"],
    "Adversarial Robustness": ["harmbench_direct", "harmbench_gcg"],
}

# Approach 1: the hierarchy inferred from the literature's instrument claims.
# Each indicator loads on its narrowest claimed construct; Safety reaches the
# sub-constructs through structural regressions. TruthfulQA is the only
# instrument claimed for Safety but for neither sub-construct, so it is the
# sole indicator of the Safety latent. Its residual variance is freely
# estimated (df = 12); it converges to the zero boundary, which is the
# collapse the case study discusses.
HIERARCHICAL = """
harmlessness =~ harmbench_direct + beavertails + toxigen
advrobust    =~ harmbench_gcg + harmbench_tap + harmbench_human
safety       =~ truthfulqa
harmlessness ~ safety
advrobust    ~ safety
"""

# Approach 2: one Safety factor over the four Safety-claimed instruments
# outside the attack conditions, and extended to the six behavioral
# instruments (TruthfulQA, a multiple-choice accuracy rather than a
# behavioral instrument, is not included).
ONE_FACTOR_FOUR = "safety =~ harmbench_direct + beavertails + toxigen + truthfulqa"
ONE_FACTOR_SIX = ("safety =~ harmbench_direct + beavertails + toxigen"
                  " + harmbench_gcg + harmbench_tap + harmbench_human")

# Two correlated sub-construct factors without the Safety latent.
TWO_FACTOR = """
harmlessness =~ harmbench_direct + beavertails + toxigen
advrobust    =~ harmbench_gcg + harmbench_tap + harmbench_human
harmlessness ~~ advrobust
"""

# Approach 3 (exploratory, specified after inspecting the data): refusal
# (the four HarmBench conditions, scored as attack failure rates) versus
# knowledge, the recognition of unsafe or false content (classification and
# multiple-choice accuracies), then with MMLU added to identify the second
# factor.
REFUSAL_KNOWLEDGE = """
refusal   =~ harmbench_direct + harmbench_gcg + harmbench_tap + harmbench_human
knowledge =~ toxigen + truthfulqa + beavertails
refusal   ~~ knowledge
"""
REFUSAL_KNOWLEDGE_MMLU = """
refusal   =~ harmbench_direct + harmbench_gcg + harmbench_tap + harmbench_human
knowledge =~ toxigen + truthfulqa + beavertails + mmlu
refusal   ~~ knowledge
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


def fmt(value: float) -> str:
    return f"{round(value, 2) + 0.0:+.2f}"


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
        print(f"    {lat:12s} " + ", ".join(
            f"{LABELS.get(p['lval'], p['lval'])} {fmt(p['std_estimate'])}" for p in items))
    structural = [p for p in result["parameters"]
                  if p["op"] == "~" and p["lval"] in latents and p["rval"] in latents]
    if structural:
        print("  standardized structural coefficients:")
        for p in structural:
            print(f"    {p['rval']} -> {p['lval']}: {fmt(p['std_estimate'])}")
    covs = [p for p in result["parameters"]
            if p["op"] == "~~" and p["lval"] != p["rval"]
            and p["lval"] in latents and p["rval"] in latents]
    for p in covs:
        value = p["std_estimate"]
        if value is None or abs(value) > 1.0:
            # A factor variance at the zero boundary leaves the standardized
            # covariance unbounded; the raw estimate is kept in the results file.
            print(f"  factor correlation {p['lval']} ~~ {p['rval']}: "
                  "not identified (a factor variance is at the zero boundary)")
        else:
            print(f"  factor correlation {p['lval']} ~~ {p['rval']}: {fmt(value)}")
    at_bound = [p["lval"] for p in result["parameters"]
                if p["op"] == "~~" and p["lval"] == p["rval"] and not p["fixed"]
                and abs(p["estimate"]) < 1e-3]
    if at_bound:
        print("  variances at the zero boundary: "
              + ", ".join(LABELS.get(v, v) for v in at_bound))


# ---------------------------------------------------------------------------
# Part A: Safetywashing battery
# ---------------------------------------------------------------------------
def block_mean(C: pd.DataFrame, a: list[str], b: list[str] | None = None) -> float:
    pairs = list(itertools.combinations(a, 2)) if b is None else [(x, y) for x in a for y in b]
    return float(np.mean([C.loc[x, y] for x, y in pairs]))


def part_a(results: dict) -> None:
    d = pd.DataFrame(json.loads((DATA / "analysis_dataset.json").read_text()))
    n = len(d)
    print("=" * 72)
    print(f"PART A  Safetywashing battery, n = {n} open chat models")
    print("=" * 72)
    C = d[BATTERY].corr()
    print("\nPearson correlations:")
    print(C.rename(index=LABELS, columns=LABELS).round(2).to_string())

    print("\nClaimed Harmlessness instruments, pairwise:")
    for x, y in itertools.combinations(HARMLESSNESS, 2):
        print(f"  r({LABELS[x]}, {LABELS[y]}) = {C.loc[x, y]:+.2f}")
    harm_mean = block_mean(C, HARMLESSNESS)
    attack_mean = block_mean(C, ATTACKS)
    cross_mean = block_mean(C, HARMLESSNESS, ATTACKS)
    print(f"  mean within the Harmlessness block:          {harm_mean:+.2f}")
    print(f"  mean within the attack-condition block:      {attack_mean:+.2f}")
    print(f"  mean across the two blocks:                  {cross_mean:+.2f}")
    print("\nCorrelations with MMLU (general capability):")
    for v in ["truthfulqa", "beavertails", "toxigen"] + ATTACKS:
        print(f"  r({LABELS[v]}, MMLU) = {C.loc[v, 'mmlu']:+.2f}")

    print("\nInstrument pairs claimed for the same construct:")
    pairs: dict[tuple[str, str], list[str]] = {}
    per_construct = {}
    for construct, instruments in CLAIMED_INSTRUMENTS.items():
        combos = [tuple(sorted(p)) for p in itertools.combinations(instruments, 2)]
        per_construct[construct] = float(np.mean([C.loc[a, b] for a, b in combos]))
        for p in combos:
            pairs.setdefault(p, []).append(construct)
    for (a, b), constructs in pairs.items():
        print(f"  r({LABELS[a]}, {LABELS[b]}) = {C.loc[a, b]:+.2f}   [{', '.join(constructs)}]")
    for construct, value in per_construct.items():
        print(f"  mean over {construct} pairs: {value:+.2f}")
    pair_values = [float(C.loc[a, b]) for a, b in pairs]
    print(f"  mean over all {len(pairs)} same-construct pairs: {np.mean(pair_values):+.2f} "
          f"(range {min(pair_values):+.2f} to {max(pair_values):+.2f})")

    Z = standardize(d, BATTERY)
    models = {}
    print("\n-- Approach 1: hierarchy inferred from the literature's instrument claims --")
    models["hierarchical"] = fit_model(
        "Hierarchical CFA: safety > harmlessness, adversarial robustness", HIERARCHICAL, Z)
    report(models["hierarchical"])

    print("\n-- Approach 2: a single Safety factor --")
    models["one_factor_four"] = fit_model(
        "One Safety factor over the four Safety-claimed instruments", ONE_FACTOR_FOUR, Z)
    report(models["one_factor_four"])
    models["one_factor_six"] = fit_model(
        "One Safety factor over the six behavioral instruments", ONE_FACTOR_SIX, Z)
    report(models["one_factor_six"])
    models["two_factor"] = fit_model(
        "Two correlated factors: harmlessness and adversarial robustness", TWO_FACTOR, Z)
    report(models["two_factor"])

    print("\n-- Approach 3: exploratory alternative (refusal vs. knowledge) --")
    models["refusal_knowledge"] = fit_model(
        "Refusal vs. knowledge", REFUSAL_KNOWLEDGE, Z)
    report(models["refusal_knowledge"])
    models["refusal_knowledge_mmlu"] = fit_model(
        "Refusal vs. knowledge, with MMLU on the knowledge factor", REFUSAL_KNOWLEDGE_MMLU, Z)
    report(models["refusal_knowledge_mmlu"])

    print("\nFit summary (Part A)")
    print(f"{'model':36s} {'chi2':>6s} {'df':>3s} {'p':>8s} {'CFI':>6s} {'TLI':>6s} {'RMSEA':>6s}")
    for key, res in models.items():
        f = res["fit"]
        print(f"{key:36s} {f['chi2']:6.1f} {f['df']:3d} {f['p']:8.3g} "
              f"{f['CFI']:6.3f} {f['TLI']:6.3f} {f['RMSEA']:6.3f}")

    results["safetywashing"] = {
        "data": (DATA / "analysis_dataset.json").relative_to(HERE).as_posix(),
        "n": n,
        "variables": BATTERY,
        "correlations": C.round(6).to_dict(),
        "harmlessness_block_mean_r": harm_mean,
        "attack_block_mean_r": attack_mean,
        "cross_block_mean_r": cross_mean,
        "same_construct_pairs": [
            {"a": a, "b": b, "constructs": cs, "r": float(C.loc[a, b])} for (a, b), cs in pairs.items()],
        "same_construct_mean_r_by_construct": per_construct,
        "same_construct_mean_r": float(np.mean(pair_values)),
        "models": models,
    }


# ---------------------------------------------------------------------------
# Part B: HELM Safety and AIR-Bench
# ---------------------------------------------------------------------------
def part_b(results: dict) -> None:
    helm = json.loads((DATA / "helm_safety.json").read_text())
    air = json.loads((DATA / "air_refusal.json").read_text())
    h = pd.DataFrame([dict(model=m, **v, air_refusal=air.get(m)) for m, v in helm.items()])
    # The AIR-Bench refusal rate is joined to the HELM Safety rows by model
    # name; a row is kept when the three correlated columns have values.
    joined = h.dropna(subset=["harmbench", "xstest", "air_refusal"])

    print()
    print("=" * 72)
    print(f"PART B  HELM Safety v1.17.0, n = {len(h)} models; "
          f"joined with the AIR-Bench 2024 refusal rate, n = {len(joined)}")
    print("=" * 72)

    def corr(frame, x, y):
        r, p = stats.pearsonr(frame[x], frame[y])
        return float(r), float(p), int(len(frame))

    out = {}
    out["harmbench_xstest"] = corr(h, "harmbench", "xstest")
    r, p, n = out["harmbench_xstest"]
    print(f"\nInstruments the Lexis records as measured_by Safety that HELM Safety "
          f"also reports (n = {n}):")
    print(f"  r(HarmBench, XSTest) = {r:.2f} (p = {p:.3f}), shared variance {100 * r * r:.1f}%")
    out["harmbench_air"] = corr(joined, "harmbench", "air_refusal")
    out["xstest_air"] = corr(joined, "xstest", "air_refusal")
    print(f"\nExternal check with the AIR-Bench 2024 refusal rate (n = {len(joined)}):")
    print(f"  r(HarmBench, AIR-Bench refusal) = {out['harmbench_air'][0]:.2f}")
    print(f"  r(XSTest, AIR-Bench refusal)    = {out['xstest_air'][0]:.2f}")
    out["sst_redteam"] = corr(h, "sst", "redteam")
    print(f"\nOther safety-family instruments in HELM Safety (SimpleSafetyTests, "
          f"Anthropic Red Team; the Lexis records them for Harmful content detection "
          f"and Harmlessness respectively, one paper each, and neither for Safety) "
          f"(n = {n}):")
    print(f"  r(SimpleSafetyTests, Anthropic Red Team) = {out['sst_redteam'][0]:.2f}")

    results["helm"] = {
        "data": [(DATA / "helm_safety.json").relative_to(HERE).as_posix(),
                 (DATA / "air_refusal.json").relative_to(HERE).as_posix()],
        "n": int(len(h)),
        "n_joined_with_air": int(len(joined)),
        "correlations": {k: {"r": v[0], "p": v[1], "n": v[2]} for k, v in out.items()},
    }


def main() -> None:
    results: dict = {}
    part_a(results)
    part_b(results)
    results["software"] = {"semopy": semopy.__version__, "pandas": pd.__version__,
                           "numpy": np.__version__}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(results, indent=1))
    print(f"\nwrote {OUT.relative_to(HERE).as_posix()}")


if __name__ == "__main__":
    main()
