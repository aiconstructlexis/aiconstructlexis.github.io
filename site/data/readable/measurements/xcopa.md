# XCOPA
**Type:** Measurement instrument  
**Supporting papers:** 14  

## State of the Field

**What it is.** Most commonly described as a cross-lingual or multilingual benchmark dataset for commonsense or causal reasoning, XCOPA is framed across definitions as a choice among plausible alternatives across languages. Definitions consistently present it as choosing the more plausible alternative, often the most plausible cause or effect from a premise and question, and papers variously describe the format as choice of plausible alternatives, multiple-choice classification, or binary-choice evaluation.

**What it is claimed to measure.** Papers use XCOPA to measure two constructs, most often Commonsense reasoning and also Reasoning, and no behavioral indicators are linked to it. The measured_by claims describe it as targeting or evaluating commonsense reasoning and reasoning, so the reported measurement uses stay concentrated on reasoning-focused constructs rather than spreading across many different outcomes.

**Space of uses.** Papers usually position XCOPA as one benchmark within multilingual evaluation suites for reasoning or classification, rather than as a standalone protocol. It is often used alongside XNLI, and some papers also pair it with MGSM, XQuAD, and XStoryCloze; one paper notes that it adopts the whole test set for XCOPA. No measurement instrument is linked to it.

**Concerns raised.** A smaller line of discussion raises a scope concern: one paper describes XCOPA as prioritizing multilingual coverage through translated or templated questions while restricting evaluation to a narrow reasoning format, specifically causal inferences.

## Sources

**XCOPA** (6 papers: [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf), [ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](https://aclanthology.org/2025.acl-long.239.pdf), [MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.79.pdf))
> A benchmark dataset for evaluating cross-lingual commonsense reasoning through a choice of plausible alternatives task.

## Relationships

### → XCOPA
- **Commonsense reasoning** (construct): *measured_by*, 4 papers
  > For NLI and reasoning, we use XNLI (Conneau et al., 2018) and XCOPA (Ponti et al., 2020) with zero-shot prompting. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
  - [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf)
  - [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.939.pdf)
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > We evaluate our models on five widely adopted multilingual benchmarks in a zero-shot setting, covering a range of tasks: ... reasoning (XCOPA; Ponti et al., 2020)... (Section 3)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
