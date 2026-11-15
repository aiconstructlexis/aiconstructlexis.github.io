# NLGraph
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across papers, NLGraph is most commonly described as a benchmark or evaluation framework for graph reasoning tasks presented in natural language. Some definitions frame it broadly as assessing whether language models can handle graph tasks and basic graph properties, including counting node degrees or finding shortest paths, while one usage narrows to the shortest-path subset, where models find the shortest path between two nodes in a weighted undirected graph.

**What it is claimed to measure.** The recorded measurement claims link NLGraph to two constructs, Reasoning and Generalization, and no behavioral indicators. Papers use it to measure Reasoning in benchmark suites, and another paper reports that simpler tasks in NLGraph evaluate Generalization, so the measurement claims are spread across more than one construct rather than centered on a single one.

**Space of uses.** Papers position NLGraph as an evaluation benchmark for graph-task performance, sometimes as an extensive framework and sometimes through a specific subset or simpler tasks. One line of use employs only the shortest-path subset, and another refers to the simpler tasks in NLGraph when evaluating generalization. No measurement instrument is linked to it, though papers discuss it alongside GPT4Graph, GraphInstruct, and GraphQA.

## Sources

**NLGraph** (4 papers: [Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only](https://proceedings.iclr.cc/paper_files/paper/2025/file/1aa1fde3661b23ba9b043082069fd144-Paper-Conference.pdf), [ALPINE: Unveiling The Planning Capability of Autoregressive Learning in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d848cb2c84f0bba7f1f73cf232734c40-Paper-Conference.pdf), [Can Large Language Models Analyze Graphs like Professionals? A Benchmark, Datasets and Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff417c3993894694e88ffc4d3f53d28b-Paper-Datasets_and_Benchmarks_Track.pdf), [GITA: Graph to Visual and Textual Integration for Vision-Language Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/00295cede6e1600d344b5cd6d9fd4640-Paper-Conference.pdf))
> A graph reasoning benchmark used here for the shortest-path subtask, where models find the shortest path between two nodes in a weighted undirected graph.

## Relationships

### → NLGraph
- **Reasoning** (construct): *measured_by*, 1 paper
  > reasoning (GSM8k (Cobbe et al., 2021), Knowledge Crosswords (Ding et al., 2024), NLGraph (Wang et al., 2024a; Zhang et al., 2024a)) (Section 3).
  - [Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > The simpler tasks in NLGraph evaluate the generalization and robustness of MA-GTS. (Section 5.1)
  - [MA-GTS: A Multi-Agent Framework for Solving Complex Graph Problems in Real-World Applications](https://aclanthology.org/2025.emnlp-main.973.pdf)
