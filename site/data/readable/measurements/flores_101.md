# Flores-101
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** FLORES-101  

## State of the Field

**What it is.** Across definitions, Flores-101 is most commonly described as a multilingual benchmark dataset with aligned translations or translation pairs across 101 languages. Papers variously describe the content as professionally translated sentences, aligned translations, or human-written translation pairs, and one usage specifically refers to the devtest. A smaller description treats it more broadly as a benchmark for machine translation and cross-lingual generation, with BLEU and COMET used to assess translation quality.

**What it is claimed to measure.** In the linked literature, papers use Flores-101 to measure Machine translation. It is linked to 1 behavioral indicator, Machine translation, and to no constructs, so the reported use converges on a single behavioral indicator rather than spreading across multiple constructs. The relationship evidence describes it as an evaluation set for translation, as a benchmark for translation tasks from FLORES-101, and as covering bidirectional Eng→X and X→Eng machine translation.

**Space of uses.** Papers most often position Flores-101 as an evaluation benchmark, using it to test models on translation tasks and multilingual capabilities. It appears as an evaluation set, as the devtest used to test each model, and as one of several benchmarks for multilingual general and cross-lingual generation; one study also performs interventions on Flores-101, with input texts sampled from the dataset, for qualitative evaluation in a machine translation context. No other measurement instrument is linked to it.

## Sources

**Flores-101** (2 papers: [KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.458.pdf), [Large Language Models Share Representations of Latent Grammatical Concepts Across Typologically Diverse Languages](https://aclanthology.org/2025.naacl-long.312.pdf))
> A benchmark dataset consisting of sentences professionally translated across 101 languages, used for qualitative evaluation of interventions in a machine translation context.

**FLORES-101** (1 paper: [AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment](https://aclanthology.org/2025.emnlp-main.328.pdf))
> Benchmark for evaluating machine translation and cross-lingual generation across 101 languages, using BLEU and COMET metrics to assess translation quality.

## Relationships

### → Flores-101
- **Machine translation** (behavioral indicator): *measured_by*, 5 papers
  > In Table 10, we used the translation dataset Flores-101 [Fan et al., 2021] as the evaluation set (Section A.5)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
  - [KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.458.pdf)
  - [Byte Latent Transformer: Patches Scale Better Than Tokens](https://aclanthology.org/2025.acl-long.453.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
