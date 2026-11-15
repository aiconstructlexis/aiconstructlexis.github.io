# ogbn-arxiv
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** OGBN-ARXIV  

## State of the Field

**What it is.** Across the surveyed work, the prevailing description is a large-scale citation network benchmark for node classification in text-attributed graphs. Papers commonly describe nodes as papers, usually with title and abstract text, and edges as citations; some definitions further specify that it is an Open Graph Benchmark dataset, a directed graph of arXiv papers, or more specifically arXiv computer science papers.

**What it is claimed to measure.** Papers link ogbn-arxiv to 2 behavioral indicators and no constructs. The dominant use is to measure Node classification, with relationship evidence describing node classification accuracy on ogbn-arxiv and listing it among datasets widely adopted for node classification; a smaller line of work uses it to measure Zero-shot classification, described as an initial investigation into leveraging GPT-3.5 on the dataset.

**Space of uses.** Papers usually position it as one benchmark within broader multi-dataset evaluations, often alongside Cora and PubMed, and sometimes with ogbn-products, CiteSeer, or Wiki-CS. It appears in performance tables and comparative experiments for node classification, and papers also use it for zero-shot classification checks and report results such as top-1 performance on ogbn-arxiv.

**Concerns raised.** Reported concerns center on scalability and text coverage. Papers note that LLM prediction cost is much higher than that of GNNs, making it less scalable for large datasets such as OGBN-ARXIV, and another description places ogbn-arxiv among benchmarks with limited textual information primarily associated with nodes.

## Sources

**ogbn-arxiv** (4 papers: [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf), [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf), [Revisiting, Benchmarking and Understanding Unsupervised Graph Domain Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2c548b2ed3141400d86a235eaa6fad0-Paper-Datasets_and_Benchmarks_Track.pdf), [TEG-DB: A Comprehensive Dataset and Benchmark of Textual-Edge Graphs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7054d2c49863c1c41be1d53f4377b82a-Paper-Datasets_and_Benchmarks_Track.pdf))
> Large-scale citation network dataset used for benchmarking node classification in text-attributed graphs, where nodes represent papers with titles and abstracts, and edges represent citations.

**OGBN-ARXIV** (1 paper: [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf))
> A large-scale citation network dataset from the Open Graph Benchmark, representing a directed graph of arXiv papers.

## Relationships

### → ogbn-arxiv
- **Node classification** (behavioral indicator): *measured_by*, 3 papers
  > Node classification accuracy for the Cora, PubMed, ogbn-arxiv, ogbn-products and tape-arxiv23 datasets. (Table 1)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
  - [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
  - [Can Large Language Models Act as Ensembler for Multi-GNNs?](https://aclanthology.org/2025.emnlp-main.1470.pdf)
- **Zero-shot classification** (behavioral indicator): *measured_by*, 1 paper
  > To assess the potential of LLMs in enhancing representation learning for TAGs, we conducted an initial investigation into leveraging GPT-3.5 for zero-shot classification on the ogbn-arxiv dataset. (Section 1)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
