# Node classification
**Type:** Behavioral indicator  
**Supporting papers:** 18  
**Also known as:** Node annotation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats node classification as predicting or assigning a categorical, class, or topic label to nodes in a graph from node features or attributes and graph connectivity or structure. Most descriptions speak of labeling each node or the unknown or unlabeled nodes, sometimes from a partly labeled graph, while some narrow the task to a single target node per graph sample or to predicting the label of a node marked '?' from its neighbors' labels. The expected output is usually one of a discrete set of class labels.

**Variants.** Variants mostly differ in graph setting and available inputs. Papers study text-attributed graphs, semi-supervised transductive node classification on heterophilic graphs, and setups where unknown or unlabeled nodes are predicted from a partly labeled graph; one paper reduces the task to an undirected graph where the node marked '?' must be inferred from neighboring labels. A smaller naming variation calls the LLM's output action 'node annotation'.

**Space of elicitation and scores.** Across papers, node classification is measured by 6 linked instruments, mostly benchmark datasets. The most frequently linked are Cora, CiteSeer, PubMed, ogbn-arxiv, and ogbn-products, and papers often report node classification accuracy on them. A separate instruction-based setup asks which CS sub-category a paper belongs to.

**What it is taken as evidence of.** Papers relate node classification to 1 construct, local reasoning, and no other construct is linked in the papers. One paper states that node classification, alongside link prediction and subgraph classification, primarily depends on the local reasoning capabilities of the graph structure. Separately, one paper reports that link prediction is related to node classification, using models trained on node classification tasks directly for link prediction without fine-tuning.

## Sources

**Node classification** (7 papers: [Can Large Language Models Analyze Graphs like Professionals? A Benchmark, Datasets and Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff417c3993894694e88ffc4d3f53d28b-Paper-Datasets_and_Benchmarks_Track.pdf), [LLM Enhancers for GNNs: An Analysis from the Perspective of Causal Mechanism Identification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25o/gao25o.pdf), [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf), [Can Graph Descriptive Order Affect Solving Graph Problems with LLMs?](https://aclanthology.org/2025.acl-long.321.pdf), [Taming Language Models for Text-attributed Graph Learning with Decoupled Aggregation](https://aclanthology.org/2025.acl-long.173.pdf), [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf), [Exploring the Potential of Large Language Models for Heterophilic Graphs](https://aclanthology.org/2025.naacl-long.269.pdf))
> The task of assigning a categorical label to each node in a graph based on its features and connectivity.

**Node annotation** (1 paper: [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf))
> The observable action of a large language model generating a class label for a given node in a graph.

## Relationships

### Node classification →
- **Cora** (measurement instrument): *measured_by*, 6 papers
  > Node classification accuracy for the Cora, PubMed, ogbn-arxiv, ogbn-products and tape-arxiv23 datasets. (Table 1)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
  - [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
  - [GITA: Graph to Visual and Textual Integration for Vision-Language Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/00295cede6e1600d344b5cd6d9fd4640-Paper-Conference.pdf)
  - [Text-space Graph Foundation Models: Comprehensive Benchmarks and New Insights](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e0b39c69663e9c073739adf547ed778-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Can Large Language Models Act as Ensembler for Multi-GNNs?](https://aclanthology.org/2025.emnlp-main.1470.pdf)
  - [Graph-R1: Incentivizing the Zero-Shot Graph Learning Capability in LLMs via Explicit Reasoning](https://aclanthology.org/2025.emnlp-main.1220.pdf)
- **PubMed** (measurement instrument): *measured_by*, 3 papers
  > Node classification accuracy for the Cora, PubMed, ogbn-arxiv, ogbn-products and tape-arxiv23 datasets. (Table 1)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
  - [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
  - [Can Large Language Models Act as Ensembler for Multi-GNNs?](https://aclanthology.org/2025.emnlp-main.1470.pdf)
- **ogbn-arxiv** (measurement instrument): *measured_by*, 3 papers
  > Node classification accuracy for the Cora, PubMed, ogbn-arxiv, ogbn-products and tape-arxiv23 datasets. (Table 1)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
  - [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
  - [Can Large Language Models Act as Ensembler for Multi-GNNs?](https://aclanthology.org/2025.emnlp-main.1470.pdf)
- **CiteSeer** (measurement instrument): *measured_by*, 3 papers
  > In this paper, we adopt the following TAG datasets widely adopted for node classification: CORA (McCallum et al., 2000), CITESEER (Giles et al., 1998), PUBMED (Sen et al., 2008), OGBN-ARXIV, OGBN-PRODUCTS (Hu et al., 2020b), and WIKICS (Mernyei & Cangea, 2020).
  - [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
  - [GITA: Graph to Visual and Textual Integration for Vision-Language Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/00295cede6e1600d344b5cd6d9fd4640-Paper-Conference.pdf)
  - [Can Large Language Models Act as Ensembler for Multi-GNNs?](https://aclanthology.org/2025.emnlp-main.1470.pdf)
- **ogbn-products** (measurement instrument): *measured_by*, 2 papers
  > Node classification accuracy for the Cora, PubMed, ogbn-arxiv, ogbn-products and tape-arxiv23 datasets. (Table 1)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
  - [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
- **Arxiv** (measurement instrument): *measured_by*, 1 paper
  > Using the node classification task on the Arxiv dataset (see Sect. 3.1) as an example, the instruction is structured as follows: Which arXiv CS sub-category does this paper belong to? (Section 2.3.1)
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)

### Associated with
- **Link prediction** (behavioral indicator), 1 paper
  > We employ models trained on node classification tasks directly for link prediction tasks without any fine-tuning. (Section 3.3)
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)
- **Local reasoning** (construct), 1 paper
  > These tasks [node classification, link prediction, and subgraph classification] primarily depend on the local reasoning capabilities of the graph structure. (Abstract)
  - [Can Large Language Models Tackle Graph Partitioning?](https://aclanthology.org/2025.emnlp-main.792.pdf)
