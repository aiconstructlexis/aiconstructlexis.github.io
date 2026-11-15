# RedPajama
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** REDPAJAMA, Redpajama  

## State of the Field

**What it is.** Across papers, the prevailing framing is a pretraining or training corpus of web text. Definitions describe it as a multi-domain pretraining corpus used to sample general web data for language modeling perplexity, as an open-source project creating a large, high-quality dataset for training language models, and as a pre-training dataset derived from CommonCrawl; one paper specifically uses the CommonCrawl split. Another paper uses it as a calibration dataset, describing it as a large collection of web text meant to represent typical input distributions.

**What it is claimed to measure.** Papers link RedPajama to one construct and no behavioral indicators. The only reported measurement claim is that it measures Editing locality: in model editing work, locality data is described as the irrelevant data of the editing process. The measurement claims therefore center on a single construct rather than being spread across many targets.

**Space of uses.** Papers use RedPajama in several operational roles, and no other measurement instrument is linked to it. It appears as evaluation data for language modeling perplexity on general web data, as part of averaged throughput simulations alongside SlimPajama and PG19, as a source dataset and baseline in data selection work, and as calibration data for post-training quantization; one paper also compares a method with the Redpajama data cleaning pipeline.

## Sources

**REDPAJAMA** (1 paper: [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf))
> A multi-domain pretraining corpus from which samples are used to evaluate language modeling perplexity on general web data.

**RedPajama** (2 papers: [Relaxed Recursive Transformers: Effective Parameter Sharing with Layer-wise LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d6a55225cebbdc16fbb0e45c5bdf2b-Paper-Conference.pdf), [GuidedQuant: Large Language Model Quantization via Exploiting End Loss Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25d/kim25d.pdf))
> An open-source project to create a large, high-quality dataset for training language models, used here for simulating generation throughput.

**Redpajama** (1 paper: [Data Selection via Optimal Control for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf))
> A pre-training dataset derived from the CommonCrawl corpus, used as a source and baseline for data selection.

## Relationships

### → RedPajama
- **Editing locality** (construct): *measured_by*, 1 paper
  > measure retention of pretraining data (xloc) from the base model: RedPajama
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
