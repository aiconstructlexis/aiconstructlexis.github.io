# GlobalOpinionQA
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** GLOBALOPINIONQA  

## State of the Field

**What it is.** Across the papers, GlobalOpinionQA is most commonly described as a dataset or benchmark built from the World Values Survey and the Pew Global Attitudes Survey, intended to capture diverse perspectives on global issues and align model responses with human opinions across regions. Definitions largely converge on cross-national survey questions and answers, and one paper further describes it as comprising around 2.5K questions. Some papers frame it more specifically as a multiple-choice evaluation of model opinions against aggregated population opinions from different countries, while others treat it as a template that preserves the original questions and response options for consistent formatting. A smaller line of work uses subsets of countries such as C′1 and C3, and one paper converts the original within-country answer distribution into a single answer by selecting the highest-probability choice.

**What it is claimed to measure.** Across the papers, it is used to measure three constructs, Personalization, Pluralistic alignment, and Social bias, and no behavioral indicators are linked to it. In work on Personalization, papers use it as one of the multiple-choice QA datasets proposed to measure steerability for specific users or social groups. In work on Pluralistic alignment, it is reported as one of the datasets for quantifying distributional alignment. In work on Social bias, papers use it to assess model opinions relative to aggregated population opinions from different countries, with the stated goal of identifying bias in representing diverse viewpoints.

**Space of uses.** Papers position it in several ways: as a benchmark for human values and opinions, as an evaluation set for sampled countries, and as a template for keeping survey questions and response options consistent. It is used alongside OpinionQA in personalization and distributional-alignment studies, and one paper also presents it alongside NYT Book Opinions when describing datasets for quantifying distributional alignment. No other measurement instrument is linked to it.

## Sources

**GlobalOpinionQA** (4 papers: [Few-shot Personalization of LLMs with Mis-aligned Responses](https://aclanthology.org/2025.naacl-long.598.pdf), [Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations](https://aclanthology.org/2025.naacl-long.162.pdf), [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf), [Benchmarking Distributional Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.2.pdf))
> A dataset of questions and answers from cross-national surveys (World Values Survey and PEW Global Attitudes Survey) designed to capture diverse perspectives on global issues.

**GLOBALOPINIONQA** (1 paper: [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf))
> Benchmark aggregating Pew Global Attitudes Survey and World Values Survey to assess alignment of model responses with human opinions across regions.

## Relationships

### → GlobalOpinionQA
- **Social bias** (construct): *measured_by*, 1 paper
  > GlobalOpinionQA (Durmus et al., 2024) uses multiple-choice questions to assess the opinions stated by a model relative to aggregated population opinions from different countries. The goal is to identify model bias in representing diverse viewpoints. (Section 3)
  - [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf)
- **Personalization** (construct): *measured_by*, 1 paper
  > For the experiments, we first use two multiple-choice QA datasets proposed to measure the steerability of LLMs for specific users (or social groups): OpinionQA (Santurkar et al., 2023) and GlobalOpinionQA (Durmus et al., 2023). (Section 4.1)
  - [Few-shot Personalization of LLMs with Mis-aligned Responses](https://aclanthology.org/2025.naacl-long.598.pdf)
- **Pluralistic alignment** (construct): *measured_by*, 1 paper
  > In this section, we describe three datasets for quantifying distributional alignment – OpinionQA (Santurkar et al., 2023), GlobalOpinionQA (Durmus et al., 2024), and a new non-political subjective opinion dataset, NYT Book Opinions.
  - [Benchmarking Distributional Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.2.pdf)
