# Confirmatory analysis case studies

Code and data for the two confirmatory factor analysis (CFA) case studies in
the appendix "Confirmatory Analysis Case Studies" of the AI Construct Lexis
paper. Both studies take construct-instrument claims recorded in the Lexis
(its `measured_by` relationships), turn them into a latent-variable model, and
test that model against public cross-model benchmark scores. Factor and
construct names are capitalized as in the paper (for example Mathematical
Reasoning, Adversarial Robustness); the Lexis spells the constructs in
sentence case (Mathematical reasoning, Adversarial robustness).

## What the two studies test

**Reasoning** (`reasoning_cfa.py`). The Lexis links Reasoning and
Mathematical Reasoning (a `correlates` relationship) and records ARC-Challenge,
MMLU, WinoGrande and GSM8K as claimed for Reasoning and GSM8K, MATH (of which
MATH-Lvl-5 is the hardest level) and parts of MMLU as claimed for Mathematical
Reasoning. The Open LLM Leaderboard reports no MMLU subset score, so the full
MMLU score stands in for the MMLU-STEM and MMLU-Math claims the Lexis records
for Mathematical Reasoning; this is a limitation of the study. The study adds
one hypothetical claim, an Arithmetic Reasoning construct operationalized by
GSM8K, and asks what CFA can establish about the hierarchy Reasoning >
Mathematical Reasoning > Arithmetic Reasoning from the scores of n = 400 models
on the Hugging Face Open LLM Leaderboard (v1 and v2 joined). The script
reports:

1. the partial correlation of WinoGrande and GSM8K given log10 parameter count;
2. the hierarchical CFA, each indicator on its narrowest claimed construct and
   the constructs linked by structural regressions;
3. the comparison with a one-factor model and with the equivalent two-level
   model in which GSM8K loads on Mathematical Reasoning directly;
4. a bifactor alternative: one general Reasoning factor on every indicator plus
   an orthogonal Numerical factor on the math-claimed indicators.

**Safety** (`safety_cfa.py`). This study tests the safety construct family
under the hierarchy inferred from the literature's instrument claims. The Lexis
records HarmBench as an instrument (`measured_by`) for Safety, Harmlessness and
Adversarial Robustness, BeaverTails and ToxiGen for Safety and Harmlessness,
and TruthfulQA for Safety and Truthfulness; it also records one `related` edge
between Harmlessness and Safety and no edge linking Adversarial Robustness to
Safety or to Harmlessness. In this release each claim the study uses rests on
five papers or fewer, and two of them on a single paper: HarmBench is claimed
for Safety, Harmlessness and Adversarial Robustness by two papers each,
BeaverTails for Safety by one and for Harmlessness by three, ToxiGen for Safety
by five and for Harmlessness by one, TruthfulQA for Safety by five (and for
Truthfulness, which the study does not model, by 48), XSTest for Safety by
three, GCG for Adversarial Robustness by two, and the Harmlessness-Safety
`related` edge by two. The structure tested here, Safety as an umbrella
construct with the two sub-constructs Harmlessness and Adversarial Robustness,
is the authors' inference from HarmBench being claimed for all three constructs
together with the Harmlessness-Safety `related` edge. The study uses only the
Safetywashing chat-model table (Ren et al., NeurIPS 2024; n = 26 open chat
models) because its refusal-based instruments, the HarmBench attack failure
rates, are defined for instruction-tuned chat models; the repository's
base-model table is not used. On that battery the script reports the convergent
correlations between instruments claimed for the same construct, the CFA of the
inferred hierarchy, single Safety-factor models, a two-factor model with
correlated Harmlessness and Adversarial Robustness factors and no Safety
latent, and an exploratory refusal-versus-knowledge alternative (with and
without MMLU as a capability covariate). On the HELM Safety leaderboard
(v1.17.0; n = 87) it reports the correlation of HarmBench and XSTest, the two
Safety-claimed instruments in HELM Safety, and, as an external check, their
correlations with the AIR-Bench 2024 refusal rate (v1.19.0; n = 75 models
joined by name). HELM Safety also reports SimpleSafetyTests and Anthropic Red
Team; the Lexis records neither for Safety (only SimpleSafetyTests for Harmful
content detection and Anthropic Red Team for Harmlessness, one paper each), so
the script reports their correlation separately.

## Layout

```
analysis/
  README.md                 this file
  requirements.txt          pinned Python dependencies
  reasoning_cfa.py          reasoning case study
  safety_cfa.py             safety case study
  prepare_safety_data.py    rebuilds the derived safety files from the raw exports
  data/
    README.md               sources, versions, fetch date, licences
    reasoning/open_llm_leaderboard_v1_v2.csv
    safety/analysis_dataset.json  helm_safety.json  air_refusal.json
    safety/raw/safetywashing_chat.csv  helm_safety_scenarios.json  airbench.json
  results/
    reasoning_results.json  safety_results.json   (written by the scripts)
```

## Setup and run

```
cd analysis
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python reasoning_cfa.py
python safety_cfa.py
python prepare_safety_data.py --check     # derived safety files equal the raw exports
```

Tested with Python 3.14 and semopy 2.3.11. The two case-study scripts print
their results and write a JSON file with every fit index and every parameter
estimate (raw and standardized) to `results/`. All scripts resolve paths
relative to their own location, so they can be run from any working directory.

## Expected headline output

Values as printed by the scripts (standardized estimates; maximum likelihood on
standardized scores).

Reasoning, n = 400:

| quantity | value |
| --- | --- |
| partial r(WinoGrande, GSM8K given log10 params) | 0.66 |
| hierarchical CFA | chi2(4) = 90.9, CFI 0.966, TLI 0.916, RMSEA 0.233 |
| structural coefficients | reasoning -> math +0.92, math -> arithmetic +0.87 |
| hierarchical vs one-factor | delta chi2(1) = 158.5 |
| two-level model (GSM8K on math) | chi2(4) = 90.9, GSM8K loading +0.87 |
| bifactor CFA | chi2(2) = 24.8, CFI 0.991, TLI 0.956, RMSEA 0.169 |
| bifactor loadings, Reasoning | ARC +1.00, MMLU +0.90, WinoGrande +0.97, GSM8K +0.82, MATH-Lvl-5 +0.54 |
| bifactor loadings, Numerical | MMLU +0.29, GSM8K +0.35, MATH-Lvl-5 +0.62 |

Safety, Safetywashing battery, n = 26:

| quantity | value |
| --- | --- |
| Harmlessness block, pairwise r | Direct/BeaverTails +0.08, Direct/ToxiGen +0.18, BeaverTails/ToxiGen -0.44 (mean -0.06) |
| attack-condition block, mean r | +0.87; cross-block mean +0.26 |
| same-construct instrument pairs | mean r +0.02 over 7 pairs (range -0.66 to +0.72) |
| hierarchical CFA | chi2(12) = 45.1, CFI 0.777, TLI 0.610, RMSEA 0.332 |
| hierarchical loadings | Harmlessness +0.33 / +0.66 / -0.59; Adversarial Robustness +0.92 / +0.89 / +0.99; Safety (TruthfulQA) +1.00 |
| hierarchical structural coefficients | safety -> harmlessness -1.00, safety -> advrobust -0.59 |
| one Safety factor, four claimed instruments | chi2(2) = 8.0, p = 0.0185, RMSEA 0.346; loadings +0.33, +0.66, -0.59, -1.00 |
| one Safety factor, six behavioral instruments | chi2(9) = 25.4, CFI 0.868, RMSEA 0.270; ToxiGen -0.24 |
| two correlated factors, Harmlessness and Adversarial Robustness | chi2(8) = 15.6, p = 0.0487, CFI 0.939, TLI 0.886, RMSEA 0.195; Harmlessness factor variance at the zero bound, factor covariance not identified |
| refusal vs knowledge | chi2(13) = 25.3, CFI 0.918, RMSEA 0.194; refusal loadings +0.77 / +0.92 / +0.89 / +0.99; factor r -0.58 |
| refusal vs knowledge, with MMLU | chi2(19) = 31.7, CFI 0.926, RMSEA 0.164; MMLU +0.83, TruthfulQA +0.94, ToxiGen +0.64, BeaverTails -0.71; factor r -0.57 |

Safety, HELM Safety v1.17.0 and AIR-Bench 2024:

| quantity | value |
| --- | --- |
| r(HarmBench, XSTest), n = 87 | 0.21 (p = 0.046) |
| r(HarmBench, AIR-Bench refusal), n = 75 | 0.84 |
| r(XSTest, AIR-Bench refusal), n = 75 | 0.01 |
| r(SimpleSafetyTests, Anthropic Red Team), n = 87 | 0.97 |

## Indicators of the safety models

Columns of `data/safety/analysis_dataset.json`, the Lexis instrument each one
stands for, and the factor it loads on in the hierarchical model
(`HIERARCHICAL` in `safety_cfa.py`). Each indicator loads on the narrowest
construct its Lexis instrument is claimed for; HarmBench is claimed for both
sub-constructs, so its conditions are assigned by whether an attack is applied,
as the rationale column states.

| column | Lexis instrument | factor | rationale |
| --- | --- | --- | --- |
| `harmbench_direct` | HarmBench (DirectRequest condition) | Harmlessness | the plain-request condition of HarmBench, which the Lexis records for Safety, Harmlessness and Adversarial Robustness; without an attack it indicates Harmlessness, the narrower of the two sub-constructs that fits it |
| `harmbench_gcg` | HarmBench (GCG-T attack) | Adversarial Robustness | HarmBench attack condition; the Lexis also records GCG itself as claimed for Adversarial Robustness (two papers) and for Harmlessness (one paper); the study treats the HarmBench attack conditions, GCG among them, as indicators of Adversarial Robustness and keeps the single-paper Harmlessness claim for GCG out of the Harmlessness pair set |
| `harmbench_tap` | HarmBench (TAP-T attack) | Adversarial Robustness | HarmBench attack condition |
| `harmbench_human` | HarmBench (HumanJailbreaks attack) | Adversarial Robustness | HarmBench attack condition |
| `beavertails` | BeaverTails | Harmlessness | claimed for Safety and Harmlessness; Harmlessness is the narrower |
| `toxigen` | ToxiGen | Harmlessness | claimed for Safety and Harmlessness; Harmlessness is the narrower |
| `truthfulqa` | TruthfulQA | Safety | claimed for Safety but for neither sub-construct, so it is the sole indicator of the Safety latent |
| `mmlu` | MMLU | none | general-capability covariate, used only in the exploratory refusal-versus-knowledge model |

`CLAIMED_INSTRUMENTS` in `safety_cfa.py` and the 7-pair same-construct
correlation summary work at the level of the Lexis instrument: HarmBench is
counted once, by its DirectRequest column, and GCG (`harmbench_gcg`) is the
second Adversarial Robustness instrument. TAP-T and HumanJailbreaks enter the
CFA as indicators of Adversarial Robustness but not the pair summary. The
seven pairs are the six pairs among the four Safety-claimed instruments
(HarmBench, BeaverTails, ToxiGen, TruthfulQA; the three Harmlessness pairs are
among them) plus the HarmBench-GCG pair for Adversarial Robustness. The Lexis
also records GCG for Harmlessness (one paper); the study treats the HarmBench
attack conditions, GCG among them, as indicators of Adversarial Robustness and
keeps that single-paper Harmlessness claim for GCG out of the Harmlessness pair
set.

## Notes on the model specifications

- Indicators are standardized before fitting; the scripts report semopy's
  standardized estimates (`Est. Std`).
- Single-indicator latents. In the reasoning hierarchy the Arithmetic factor
  has GSM8K as its only indicator and follows the single-indicator convention:
  loading fixed to 1 (semopy fixes the first loading of each latent) and
  residual variance fixed to 0, giving df = 4. In the safety hierarchy the
  Safety factor has TruthfulQA as its only indicator; its residual variance is
  freely estimated (df = 12) and converges to the zero boundary, which is the
  collapse the case study discusses.
- CFI and TLI. semopy computes these incremental indices against a baseline
  model that inherits every constraint of the fitted model, so they are
  undefined when a residual variance is fixed to zero. Both scripts therefore
  compute CFI and TLI from the standard independence baseline (all indicators
  uncorrelated; chi-square n * (-log det R) on standardized data). For models
  without fixed variances this equals semopy's own baseline, and the scripts
  raise an error if the two ever disagree. Chi-square, p-value (from scipy) and
  RMSEA are unaffected.
- Boundary solutions. Several models end with a variance at its zero bound
  (ARC-Challenge's residual in the reasoning models, TruthfulQA's residual and
  the Harmlessness disturbance in the safety models). semopy may log that its
  optimizer did not converge for such a model; the reported estimates are the
  boundary solutions, which the paper reads as collapse diagnostics rather
  than as precise parameter values.
- The refusal-versus-knowledge models were specified after inspecting the
  data and are exploratory; the paper presents them as alternatives to be
  confirmed on held-out models, not as confirmed structure.

## Data provenance

See `data/README.md` for file-level detail. In short: the reasoning sample is
the Open LLM Leaderboard v1 and v2 join redistributed by
`fboulnois/llm-leaderboard-csv` (release v1.3.0), n = 400. The safety data are
three raw exports, each fetched on 2026-07-27: the Safetywashing chat-model
benchmark table (Ren et al., NeurIPS 2024,
`github.com/centerforaisafety/safetywashing`), the HELM Safety leaderboard
(crfm-helm public release v1.17.0) and the AIR-Bench 2024 leaderboard
(crfm-helm public release v1.19.0). `prepare_safety_data.py` derives the three
JSON files read by `safety_cfa.py` from those raw exports in
`data/safety/raw/`.
