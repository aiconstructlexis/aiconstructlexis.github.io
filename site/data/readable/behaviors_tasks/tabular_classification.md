# Tabular classification
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the papers, the prevailing use is as a supervised prediction task over structured tables: predicting a categorical label for a data point represented by tabular features. The definitions do not introduce alternative success criteria or judging schemes, and one paper discusses the task in sample-efficiency terms, noting that test-time training reduces the number of required samples for tabular classification by about 3 to 5 times.

**Variants.** The only explicit setting attached to the behavior is its use with in-context learning, described as leveraging the in-context learning capability of large language models for tabular classification with training-free adaptability across diverse datasets. Beyond that framing, the papers do not name additional subtasks, domains, or modalities.

**Space of elicitation and scores.** No measurement instrument is linked to it. The papers therefore do not identify a recurring elicitation or scoring tool for this behavior, although one study operationalizes progress through required sample size and reports fewer samples under test-time training.

**What it is taken as evidence of.** Papers do not converge on tabular classification as evidence of multiple broader constructs. The only linked construct is In-context learning, and that connection is recorded as related rather than measured, correlational, or causal: one paper treats tabular classification as a setting for leveraging in-context learning.

## Sources

**Tabular classification** (1 paper: [Test-Time Training Provably Improves Transformers as In-context Learners](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gozeten25a/gozeten25a.pdf))
> The task of predicting a categorical label for a data point represented by a set of structured, tabular features.

## Relationships

### Associated with
- **In-context learning** (construct), 1 paper
  > Leveraging the in-context learning (ICL) capability of Large Language Models (LLMs) for tabular classification has gained significant attention for its training-free adaptability across diverse datasets. (Abstract)
  - [TabFlex: Scaling Tabular Learning to Millions with Linear Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25b/zeng25b.pdf)
