# HiTab
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Papers most commonly describe HiTab as a benchmark or table reasoning dataset built around hierarchical or otherwise complex tables from government reports and Wikipedia pages. Definitions emphasize multi-level headers, implicit relationships, and complex structural relationships, and they describe the dataset as used for table transformation and question answering; one paper specifies 3,597 tables from HTML government reports and Wikipedia pages and 10,672 QA pairs. One paper also presents it as designed for table-based question answering and table-to-text generation.

**What it is claimed to measure.** Papers use HiTab to measure 1 construct and 2 behavioral indicators. The construct link is table reasoning, while the behavioral indicator links are data-to-text generation and table question answering. Taken together, papers report it as evaluating several related table tasks rather than only one.

**Space of uses.** Papers use HiTab as an evaluation benchmark in experiments on table reasoning, question answering, and generation, and one paper places it among three widely used table reasoning datasets. No other measurement instrument is linked to it, though papers evaluate it alongside WikiTableQuestions, TableBench, and MULTIHIERTT, and one study reports model comparisons on HiTab through QA accuracy.

## Sources

**HiTab** (2 papers: [RelationalCoder: Rethinking Complex Tables via Programmatic Relational Transformation](https://aclanthology.org/2025.acl-long.89.pdf), [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf))
> Benchmark dataset containing complex tables from government reports and Wikipedia pages, used to evaluate table transformation and question answering involving multi-level headers and implicit relationships.

## Relationships

### → HiTab
- **Data-to-text generation** (behavioral indicator): *measured_by*, 1 paper
  > HiTab: A dataset consisting of hierarchical tables, designed for table-based question answering (QA) and table-to-text generation (NLG) (Section 4.1).
  - [QuASAR: A Question-Driven Structure-Aware Approach for Table-to-Text Generation](https://aclanthology.org/2025.acl-long.1300.pdf)
- **Table reasoning** (construct): *measured_by*, 1 paper
  > ROT is evaluated on three widely used table reasoning datasets: WikiTableQuestions (Pasupat and Liang, 2015), HiTab (Cheng et al., 2022), and TableBench (Wu et al., 2024) (Section 3.1)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **Table question answering** (behavioral indicator): *measured_by*, 1 paper
  > Task Category: Table Question Answering (TQA), Task Name: Hierarchical TQA, Dataset: HiTab (2022) (Table 2)
  - [Can GRPO Boost Complex Multimodal Table Understanding?](https://aclanthology.org/2025.emnlp-main.637.pdf)
