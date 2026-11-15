# ACE05
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** ACE  

## State of the Field

**What it is.** Across the papers, ACE05 is most commonly described as a news-domain information extraction benchmark. Definitions present it either broadly, as covering named entity recognition, relation extraction, and event extraction over news text, or more narrowly as a sentence-level event extraction dataset with news articles annotated for 33 event types, with one quoted passage adding that the documents come from 6 news sources. Some authors shorten the name to ACE for a news event detection dataset with 33 event types, while one paper uses the surface form ACE differently, for a 21-question multiple-choice computational-thinking assessment aimed at the Bloom levels Analyzing, Evaluating, and Creating.

**What it is claimed to measure.** Papers use it to measure 1 behavioral indicator, Event detection, and it is linked to no constructs. The recorded claim is concentrated rather than spread across many outcomes: one paper benchmarks an event detection system on ACE alongside other domain datasets.

**Space of uses.** Papers use ACE05 alongside other benchmarks rather than in isolation. It appears with CASIE and PHEE in evaluations from the TextEE framework, and with ACE04 in a broader suite reporting results on 16 information extraction benchmarks. One paper explicitly positions ACE05 as "the most widely used benchmark dataset for SEE," while another uses ACE as one of several event detection datasets spanning news, epidemiology, and biomedical domains.

## Sources

**ACE05** (2 papers: [Soft Syntactic Reinforcement for Neural Event Extraction](https://aclanthology.org/2025.naacl-long.479.pdf), [Label Drop for Multi-Aspect Relation Modeling in Universal Information Extraction](https://aclanthology.org/2025.naacl-long.259.pdf))
> Benchmark dataset for information extraction that includes named entity recognition, relation extraction, and event extraction tasks over news text.

**ACE** (2 papers: [DiCoRe: Enhancing Zero-shot Event Detection via Divergent-Convergent LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1038.pdf), [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf))
> Automatic Content Extraction (ACE) dataset for event detection in news texts, containing 33 event types and widely used for structured information extraction evaluation.

## Relationships

### → ACE05
- **Event detection** (behavioral indicator): *measured_by*, 1 paper
  > We benchmark SNARE on ED datasets from three domains: ACE (Doddington et al., 2004) (news), SPEED (Parekh et al., 2024c) (epidemiology), and GENIA2011 (Kim et al., 2011) (biomedical). (Section 1)
  - [SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1039.pdf)
