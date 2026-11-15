# ReDial
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across papers, ReDial is described in two distinct ways rather than with a single settled format. One paper introduces it as Reasoning with Dialect Queries, a human-annotated benchmark with over 1.2K parallel Standardized English and African American Vernacular English query pairs spanning algorithm, logic, math, and integrated reasoning tasks, and describes it as an end-to-end SE-AAVE parallel dataset for reasoning. Another paper uses the same name for a movie recommendation dialogue dataset, described as a collection of movie recommendation conversations annotated with user satisfaction labels and used in task-oriented dialogue experiments.

**What it is claimed to measure.** Papers use ReDial to measure one construct and one behavioral indicator. The construct link is Reasoning, with a paper describing ReDial as a dataset for reasoning tasks, while the behavioral indicator link is Conversational recommendation, with another paper treating ReDial as one of two real-world conversational recommendation benchmarks. The measurement claims therefore point to two different targets rather than converging on only one.

**Space of uses.** In experiments, papers place ReDial alongside other dialogue benchmarks rather than in isolation. One paper uses it with INSPIRED as a conversational recommendation benchmark, while another uses it with SGD and MWOZ as one of three task-oriented dialogue datasets and reports F1-scores on it.

## Sources

**ReDial** (2 papers: [Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks](https://aclanthology.org/2025.acl-long.317.pdf), [LLM-guided Plan and Retrieval: A Strategic Alignment for Interpretable User Satisfaction Estimation in Dialogue](https://aclanthology.org/2025.naacl-long.523.pdf))
> Reasoning with Dialect Queries, a human-annotated benchmark of over 1.2K parallel Standardized English and African American Vernacular English prompts across algorithm, logic, math, and integrated reasoning tasks.

## Relationships

### → ReDial
- **Reasoning** (construct): *measured_by*, 1 paper
  > We introduce ReDial (Reasoning with Dialect Queries), the first high-quality, end-to-end human-annotated SE-AAVE parallel dataset for reasoning tasks (Section 2).
  - [Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks](https://aclanthology.org/2025.acl-long.317.pdf)
- **Conversational recommendation** (behavioral indicator): *measured_by*, 1 paper
  > We have conducted extensive experiments on two real-world CRS benchmarks, namely ReDial (Li et al., 2018) and INSPIRED (Hayati et al., 2020)... (Section 1)
  - [Beyond Single Labels: Improving Conversational Recommendation through LLM-Powered Data Augmentation](https://aclanthology.org/2025.acl-long.758.pdf)
