# CrossCodeEval
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats CrossCodeEval as a repository-level, cross-file benchmark. One definition describes it broadly as evaluating code generation and understanding, while another presents it more narrowly as a diverse, multilingual benchmark, and also as a repository-level code completion dataset, for cross-file code completion.

**What it is claimed to measure.** Papers link it to 1 behavioral indicator, Code completion, and to no constructs. The recorded use converges on that single indicator: one paper uses CrossCodeEval to measure code completion in repository-level, cross-file settings, specifically for code Fill-in-the-Middle scenarios.

**Space of uses.** In use, papers report performance on CrossCodeEval as an evaluation dataset for repository-level code completion. One paper uses it alongside CrossCodeLongEval and RepoEval to evaluate repository-level code Fill-in-the-Middle in cross-file scenarios, and a survey mentions it together with RepoBench when discussing repository-level tasks.

## Sources

**CrossCodeEval** (2 papers: [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf), [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf))
> A benchmark for evaluating cross-file, repository-level code generation and understanding.

## Relationships

### → CrossCodeEval
- **Code completion** (behavioral indicator): *measured_by*, 1 paper
  > we also evaluate the effectiveness of HLP on repository-level code Fill-in-the-Middle in cross-file scenarios via CrossCodeEval (Ding et al., 2023), CrossCodeLongEval (Wu et al., 2024), and RepoEval (Zhang et al., 2023). (Section 4.2)
  - [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1672.pdf)
