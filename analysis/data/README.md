# Data for the confirmatory analysis case studies

All files are public leaderboard exports or straightforward column selections
from them. The two case-study scripts in the parent directory read only the
files marked "used by" below; `prepare_safety_data.py` reads the raw safety
exports and writes the derived safety files.

## reasoning/

### `open_llm_leaderboard_v1_v2.csv` (used by `reasoning_cfa.py`)

Joined sample of language models that appear on both the Hugging Face Open LLM
Leaderboard v1 (archived June 2024) and v2 (June 2024 onwards), as
redistributed in machine-readable form by `fboulnois/llm-leaderboard-csv`
(release v1.3.0). Joining v1 and v2 by model name yields n = 400 rows.

| column | source | content |
| --- | --- | --- |
| `fullname` | v1, v2 | Hugging Face model id |
| `arc` | v1 | ARC-Challenge, 25-shot multiple-choice accuracy (%) |
| `mmlu` | v1 | MMLU, 5-shot accuracy (%) |
| `winogrande` | v1 | WinoGrande, 5-shot multiple-choice accuracy (%) |
| `gsm8k` | v1 | GSM8K, 5-shot exact match (%) |
| `math_lvl5` | v2 | MATH-Lvl-5, 4-shot accuracy (%), competition mathematics, hardest level only |
| `log10_params` | v2 | log10 of the parameter count in billions |

Within each leaderboard all scores come from the same lm-evaluation-harness
pipeline. Seven model names occur twice (two v2 entries matched one v1 entry
and differ only in `math_lvl5`); the sample is used as is, n = 400.

## safety/

### Raw exports (`safety/raw/`, fetched 2026-07-27)

| file | source | content |
| --- | --- | --- |
| `safetywashing_chat.csv` | Safetywashing, Ren et al., NeurIPS 2024, `github.com/centerforaisafety/safetywashing` | benchmark table for the 26 open chat models (183 columns) |
| `helm_safety_scenarios.json` | HELM Safety leaderboard, crfm-helm public release v1.17.0 | leaderboard tables for 87 models; the "Accuracy" table holds the LM-judged safety scores for HarmBench, SimpleSafetyTests, Anthropic Red Team and XSTest, BBQ accuracy, and their mean |
| `airbench.json` | AIR-Bench 2024 leaderboard, crfm-helm public release v1.19.0 | refusal rates for 87 models, overall and per AIR category |

### Derived files (used by `safety_cfa.py`)

`prepare_safety_data.py` rebuilds these from the raw exports;
`prepare_safety_data.py --check` verifies that the shipped files equal the
rebuilt ones.

| file | records | content |
| --- | --- | --- |
| `analysis_dataset.json` | 26 | per model: the "all"-category HarmBench attack failure rates under DirectRequest, GCG-T, TAP-T and HumanJailbreaks; BeaverTails, ToxiGen and SafetyBench accuracies; TruthfulQA MC1; MMLU; GSM8K; parameter count |
| `helm_safety.json` | 87 | per model: mean score and the HarmBench, SimpleSafetyTests, BBQ, Anthropic Red Team and XSTest scores of the HELM Safety "Accuracy" table |
| `air_refusal.json` | 87 | per model: AIR-Bench 2024 overall refusal rate |

75 of the 87 AIR-Bench models share a name with a HELM Safety model; the
external refusal check in `safety_cfa.py` uses that join.

In the Safetywashing export every variable is already oriented so that higher
is better (the HarmBench columns are attack failure rates); the derived file
copies the values unchanged. `analysis_dataset.json` also carries SafetyBench,
GSM8K and `model_size`, which the CFA does not use: SafetyBench is not a
Lexis-recorded instrument for Safety or Harmlessness, GSM8K is a reasoning
benchmark, and the parameter count is kept for reference.

## Licences

The exports carry no licence statement of their own. Their reuse is governed
by the terms of the respective sources: the Safetywashing repository, the
HELM project (Center for Research on Foundation Models, Stanford), and the
Hugging Face Open LLM Leaderboard as redistributed by
`fboulnois/llm-leaderboard-csv`. The files are included here unchanged (raw
exports) or as column selections (derived files) to make the case studies
reproducible.
