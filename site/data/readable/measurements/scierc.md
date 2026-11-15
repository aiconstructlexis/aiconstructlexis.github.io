# SciERC
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across the papers, SciERC is treated as a computer science evaluation resource, but the descriptions are not identical. One paper presents it as an evaluation task in SciRIFF-Eval for relation extraction, with a computer science abstract as input and six entity types as output. Another paper describes it as a computer science dataset for text classification over scientific articles, focused on identifying entities, relations, and coreference.

**What it is claimed to measure.** Papers use SciERC to measure two behavioral indicators, Information extraction and Knowledge graph construction, and no construct is linked to it. The more direct framing is that it measures Information extraction, stated as "IE(Rel)" with a CS abstract and six entity types as the task format. Another paper reports it as measuring Knowledge graph construction by using it as one of the domain-specific datasets with golden ground truth KGs.

**Space of uses.** Papers use SciERC within broader evaluation setups, and no measurement instrument is linked to it. In one usage it appears inside SciRIFF-Eval as the relation extraction task over computer science abstracts. In another, it is grouped with REBEL-Sub, GenWiki, and the Windows-centric subset of Re-DocRED as one of the domain-specific datasets used for experiments with golden ground truth knowledge graphs.

## Sources

**SciERC** (2 papers: [SciRIFF: A Resource to Enhance Language Model Instruction-Following over Scientific Literature](https://aclanthology.org/2025.emnlp-main.310.pdf), [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf))
> An evaluation task in SciRIFF-Eval for relation extraction, requiring the identification of six entity types from a computer science abstract.

## Relationships

### → SciERC
- **Information extraction** (behavioral indicator): *measured_by*, 1 paper
  > “SciERC | IE(Rel) | CS abstract | 6 entity types”
  - [SciRIFF: A Resource to Enhance Language Model Instruction-Following over Scientific Literature](https://aclanthology.org/2025.emnlp-main.310.pdf)
- **Knowledge graph construction** (behavioral indicator): *measured_by*, 1 paper
  > In our study, we conduct experiments on two general datasets (REBEL-Sub (Huguet Cabot and Navigli, 2021) and GenWiki (Jin et al., 2020)) and two domain-specific datasets (SCIERC (Luan et al., 2018) and the Windows-centric subset of Re-DocRED (Tan et al., 2022)) with golden ground truth KGs (Section 5.1.1).
  - [Can LLMs be Good Graph Judge for Knowledge Graph Construction?](https://aclanthology.org/2025.emnlp-main.554.pdf)
