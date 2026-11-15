# Link prediction
**Type:** Behavioral indicator  
**Supporting papers:** 16  

## State of the Field

**Space of definitions.** The most prevalent framing treats link prediction as a knowledge-graph task: predicting missing relations or entities, sometimes narrowed to finding the most plausible tail entity for a query such as (h, r, ?). Some papers use a broader graph formulation instead, describing it as inferring whether an edge or connection exists between two nodes. Evaluation is explicitly described with Mean Reciprocal Rank and Hit@N in one line of work, while another reports link prediction accuracy.

**Variants.** Papers study both knowledge-graph and broader graph settings. In knowledge-graph work, link prediction appears alongside triple classification or as part of knowledge graph completion, and one setup states that "the edges connected to these removed nodes were then used as prediction targets." Other papers treat it as a downstream graph task, including a few-shot setting, and it is often discussed alongside node classification.

**Space of elicitation and scores.** Across papers, link prediction is measured by five instruments, all used as datasets: FB15k-237, CiteSeer, Cora, PubMed, and WN18RR. The scoring language varies by setting: knowledge-graph papers explicitly mention Mean Reciprocal Rank and Hit@N, while one paper reports link prediction accuracies on Cora and CiteSeer.

**What it is taken as evidence of.** Across the recorded links, papers relate link prediction to two constructs rather than using it as direct evidence of one agreed construct: Local reasoning and Task generalization. One paper describes link prediction, together with node classification and subgraph classification, as tasks that "primarily depend on the local reasoning capabilities of the graph structure," while another relates it to task generalization by using models trained on node classification directly for link prediction without fine-tuning.

## Sources

**Link prediction** (3 papers: [Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf), [Generalization Principles for Inference over Text-Attributed Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bq/wang25bq.pdf), [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf))
> The specific task of predicting missing relations or entities in a knowledge graph, evaluated using metrics like MRR and Hit@N.

## Relationships

### Link prediction →
- **FB15k-237** (measurement instrument): *measured_by*, 2 papers
  > We carry out experiments on the KG link prediction and triple classification tasks, where the popular datasets WN18RR (Dettmers et al., 2018) and FB15k-237 (Toutanova and Chen, 2015) as well as FB15k-237N (Lv et al., 2022) are utilized.
  - [Self-supervised Quantized Representation for Seamlessly Integrating Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.acl-long.667.pdf)
  - [Enhancing Large Language Model for Knowledge Graph Completion via Structure-Aware Alignment-Tuning](https://aclanthology.org/2025.emnlp-main.1061.pdf)
- **PubMed** (measurement instrument): *measured_by*, 1 paper
  > We then employ Cora, History, and Amazon ratings to evaluate node classification downstream task performance, PubMed for link prediction task performance, and HIV for graph classification task performance. (Section 4.4)
  - [Text-space Graph Foundation Models: Comprehensive Benchmarks and New Insights](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e0b39c69663e9c073739adf547ed778-Paper-Datasets_and_Benchmarks_Track.pdf)
- **WN18RR** (measurement instrument): *measured_by*, 1 paper
  > We carry out experiments on the KG link prediction and triple classification tasks, where the popular datasets WN18RR (Dettmers et al., 2018) and FB15k-237 (Toutanova and Chen, 2015) as well as FB15k-237N (Lv et al., 2022) are utilized.
  - [Self-supervised Quantized Representation for Seamlessly Integrating Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.acl-long.667.pdf)
- **Cora** (measurement instrument): *measured_by*, 1 paper
  > our model achieved link prediction accuracies of 95.40% on Cora and 76.14% on CiteSeer, indicating the strong generalization capability of our method. (Section 4.2)
  - [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf)
- **CiteSeer** (measurement instrument): *measured_by*, 1 paper
  > our model achieved link prediction accuracies of 95.40% on Cora and 76.14% on CiteSeer, indicating the strong generalization capability of our method. (Section 4.2)
  - [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf)

### Associated with
- **Node classification** (behavioral indicator), 1 paper
  > We employ models trained on node classification tasks directly for link prediction tasks without any fine-tuning. (Section 3.3)
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)
- **Knowledge graph completion** (behavioral indicator), 1 paper
  > our work focuses on KGC, specifically addressing two tasks: (i) triple classification, assessing the correctness of a given triple (h, r, t), and (ii) link prediction, identifying the most plausible tail entity t for a given query (h, r, ?). (Section 3)
  - [Enhancing Large Language Model for Knowledge Graph Completion via Structure-Aware Alignment-Tuning](https://aclanthology.org/2025.emnlp-main.1061.pdf)
- **Local reasoning** (construct), 1 paper
  > These tasks [node classification, link prediction, and subgraph classification] primarily depend on the local reasoning capabilities of the graph structure. (Abstract)
  - [Can Large Language Models Tackle Graph Partitioning?](https://aclanthology.org/2025.emnlp-main.792.pdf)
- **Task generalization** (construct), 1 paper
  > We employ models trained on node classification tasks directly for link prediction tasks without any fine-tuning. (Section 3.3)
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)
