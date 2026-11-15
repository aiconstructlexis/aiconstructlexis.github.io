# FLAN
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across these papers, FLAN is described as a benchmark or collection of datasets covering diverse NLP tasks, including free-form generation tasks such as translation and summarization, with datasets expressed through natural language instructions. The prevailing usage is as a broad multi-task evaluation set, and papers also describe it as a mix of multiple NLP tasks used as a reference dataset.

**What it is claimed to measure.** Papers use FLAN to measure two constructs, Generalization and Robustness. These measurement claims cover both constructs rather than a single repeated target, and FLAN is also related to one behavioral indicator, Text generation, through descriptions of its free-form generation tasks.

**Space of uses.** Papers mainly position FLAN as a broad evaluation benchmark. It is used as a large multi-task evaluation set, as a reference dataset when demonstrating generalization and robustness, and alongside Wikitext and Gigaword for evaluation across various tasks. No other measurement instrument is linked to it.

## Sources

**FLAN** (2 papers: [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf), [LensLLM: Unveiling Fine-Tuning Dynamics for LLM Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25g/zeng25g.pdf))
> A benchmark of diverse tasks including free-form generation tasks such as translation and summarization, used here as a large multi-task evaluation set.

## Relationships

### → FLAN
- **Generalization** (construct): *measured_by*, 1 paper
  > To demonstrate the generalizability and robustness of our method, we include FLAN (Chung et al., 2024) (a mix of multiple NLP tasks) as reference datasets .
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > To demonstrate the generalizability and robustness of our method, we include FLAN (Chung et al., 2024) (a mix of multiple NLP tasks) as reference datasets .
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)

### Associated with
- **Text generation** (behavioral indicator), 1 paper
  > FLAN is a dataset with more diverse forms of tasks, including free-form generation tasks like translation and summarization. (Section 5)
  - [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)
