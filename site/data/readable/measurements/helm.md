# HELM
**Type:** Measurement instrument  
**Supporting papers:** 23  

## State of the Field

**What it is.** Across the surveyed work, HELM is most commonly described as Holistic Evaluation of Language Models, a large-scale or aggregate benchmark or framework from Stanford for evaluating language models across a wide range of scenarios and metrics. Definitions repeatedly present it as offering broad evaluation across capabilities, limitations, and risks, and papers place it among comprehensive evaluation suites and foundation-model evaluations. A smaller line of work uses the same name differently, describing HELM as a non-adaptive baseline attack that randomly adds typos, lowercases text, or uses contractions.

**What it is claimed to measure.** Papers link HELM to no constructs, one behavioral indicator, and two other instruments. The only behavioral indicator it is recorded as measuring is multiple-choice question answering: one paper states that HELM uses questions from MMLU, with multiple choice questions and labeled correct answers. In the recorded relationships, the measurement use therefore centers on that single behavioral indicator rather than on any linked construct.

**Space of uses.** Papers commonly use HELM as a broad comparative evaluation or ranking source. One paper reports that HELM and LiveBench are strongly correlated, another uses HELM to rank LLM performance on MMLU, and other papers position HELM alongside Open LLM Leaderboard, BigBench, and ChatbotArena as comprehensive or aggregate evaluations. It is also cited among established benchmark suites in general benchmark listings.

**Concerns raised.** Only a smaller line of work raises explicit reservations. One paper describes aggregate benchmarks such as HELM as proxy measurements of the true capabilities of LLMs, and another presents HELM as one of several knowledge-based and logic-based benchmarks that fail to capture nuanced human preferences.

## Sources

**HELM** (7 papers: [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf), [Language Models can Categorize System Inputs for Performance Analysis](https://aclanthology.org/2025.naacl-long.317.pdf), [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318.pdf), [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf), [Optimizing Adaptive Attacks against Watermarks for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diaa25a/diaa25a.pdf), [A Systematic Analysis of Base Model Choice for Reward Modeling](https://aclanthology.org/2025.emnlp-main.8.pdf), [Preference Learning Algorithms Do Not Learn Preference Rankings](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8ce770a6b25e603fbff4a37f9e31edc-Paper-Conference.pdf))
> Holistic Evaluation of Language Models, a large-scale benchmark from Stanford for evaluating language models across a wide range of scenarios and metrics.

## Relationships

### HELM →
- **LiveBench** (measurement instrument): *correlates*, 1 paper
  > LiveBench and HELM are strongly correlated (Table 1).
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)

### → HELM
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > We started from two LLM leaderboards: (1) HuggingFace’s Open LLM Leaderboard 21; and (2) Stanford’s Holistic Evaluation of Language Models (Helm) (Liang et al., 2023). Both use questions from the Massive Multitask Language Understanding (MMLU) question-answering dataset (Hendrycks et al., 2020), with multiple choice questions and labeled correct answers. (Section 3.1).
  - [Correlated Errors in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25e/kim25e.pdf)

### Associated with
- **MMLU** (measurement instrument), 1 paper
  > "the performance of the ten best-performing LLMs on MMLU (as ranked by HELM (Liang et al., 2023))"
  - [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf)
