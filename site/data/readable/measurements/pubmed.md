# PubMed
**Type:** Measurement instrument  
**Supporting papers:** 20  
**Also known as:** PUBMED, Pubmed  

## State of the Field

**What it is.** Across the surveyed work, the dominant framing treats PubMed as a citation-network or text-attributed graph benchmark derived from the PubMed database, where documents or scientific publications are the nodes and node classification is the usual evaluation task. Some definitions make this more specific by describing it as a biomedical citation network or as publications related to diabetes. A smaller line of work uses the same name for different resources: one paper refers to "PubMed1" as a collection of biomedical paper abstracts used as a representative domain corpus for finetuning, another defines PubMed as medical scientific articles for summarizing authors' conclusions from experiment descriptions, and another uses Scientific Papers (Pubmed) as an out-of-domain benchmark; one graph paper also uses PubMed for node-level and edge-level tasks.

**What it is claimed to measure.** Papers link PubMed to 3 behavioral indicators and 1 construct. The prevailing use is to measure node classification, with papers describing it as a widely adopted or well-established dataset for that task and reporting node classification accuracy on it. Other papers use it to measure link prediction and text summarization, and the only linked construct is zero-shot generalization, so most recorded measurement claims are task-level and centered on node classification.

**Space of uses.** No measurement instrument is linked to PubMed through recorded relationships. In source descriptions, papers usually place it in broader benchmark suites, most often alongside Cora and ogbn-arxiv, with some also pairing it with ogbn-products, Citeseer, and HIV. They typically position it as an evaluation benchmark, though some papers instead use it as a representative domain corpus for finetuning or as an out-of-domain dataset for zero-shot generalization checks.

## Sources

**PubMed** (5 papers: [Dissecting learning and forgetting in language model finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c4de749a4bd8802f0b4033d09a7867db-Paper-Conference.pdf), [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf), [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf), [Graph World Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25p/feng25p.pdf), [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf))
> A citation network dataset derived from the PubMed database where nodes are documents, used to evaluate node classification on text-attributed graphs.

**PUBMED** (1 paper: [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf))
> A citation network dataset from the biomedical domain, used for node classification on text-attributed graphs.

**Pubmed** (2 papers: [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf), [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf))
> A benchmark dataset consisting of scientific publications from the PubMed database related to diabetes, used for node classification.

## Relationships

### → PubMed
- **Node classification** (behavioral indicator): *measured_by*, 3 papers
  > Node classification accuracy for the Cora, PubMed, ogbn-arxiv, ogbn-products and tape-arxiv23 datasets. (Table 1)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
  - [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
  - [Can Large Language Models Act as Ensembler for Multi-GNNs?](https://aclanthology.org/2025.emnlp-main.1470.pdf)
- **Link prediction** (behavioral indicator): *measured_by*, 1 paper
  > We then employ Cora, History, and Amazon ratings to evaluate node classification downstream task performance, PubMed for link prediction task performance, and HIV for graph classification task performance. (Section 4.4)
  - [Text-space Graph Foundation Models: Comprehensive Benchmarks and New Insights](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e0b39c69663e9c073739adf547ed778-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text summarization** (behavioral indicator): *measured_by*, 1 paper
  > We further evaluate the methods on three summarization datasets. ... PubMed (Tang et al., 2023) is a collection of medical scientific articles where the goal is to summarize the conclusions of the authors... (Section 4.1)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Zero-shot generalization** (construct): *measured_by*, 1 paper
  > We evaluate the model capacity for both the OpenWebText test set and seven out-of-domain unseen datasets, used to validate the models' ability in zero-shot generalization. These unseen datasets include Our Penn Tree Bank (PTB)... Wikitext... LM1B, Lambada... AG News... Pubmed
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
