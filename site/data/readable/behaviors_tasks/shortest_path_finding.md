# Shortest path finding
**Type:** Behavioral indicator  
**Supporting papers:** 10  
**Also known as:** Shortest path prediction, Shortest path identification  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this as a graph task where a model identifies the shortest path between two specified nodes. Most descriptions place it in a weighted, undirected graph and define success as returning the path with the minimum total weight. Some formulations extend the required output to the shortest path and its distance, and one describes a harder exact-path version that asks for the exact sequence of nodes.

**Variants.** Papers use several nearby names, including shortest path finding, shortest path prediction, and shortest path identification. The main variants differ in output and prompting rather than domain: some ask for the actual shortest path, some query the shortest path distance, and one asks for the exact path as a node sequence. One description frames it as a structural task over randomly selected node pairs, with an alternative prompt targeting two specified nodes.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior. Instead, papers describe elicitation directly through task prompts: finding the minimum-weight path between nodes, generating the actual shortest path or its distance, or producing the exact path. The definitions themselves specify success as returning the minimum-weight path, the correct shortest path distance, or the exact sequence of nodes.

**What it is taken as evidence of.** The only construct-level link relates shortest path finding to Graph reasoning, with one paper treating shortest path as one of the graph reasoning tasks it considers alongside graph connectivity and cycle detection. Papers do not otherwise explicitly converge on a construct that this behavior indicates. Beyond constructs, one paper relates the task to State tracking, stating that solving it effectively requires maintaining the state of graph exploration.

## Sources

**Shortest path finding** (1 paper: [Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only](https://proceedings.iclr.cc/paper_files/paper/2025/file/1aa1fde3661b23ba9b043082069fd144-Paper-Conference.pdf))
> The task of identifying the path with the minimum total weight between two specified nodes in a weighted, undirected graph.

**Shortest path prediction** (1 paper: [GOFA: A Generative One-For-All Model for Joint Graph Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/652c104b5b0652a03684efeaf805463b-Paper-Conference.pdf))
> The observable task of identifying and generating the shortest path(s) and their distance between two specified nodes in a graph.

**Shortest path identification** (1 paper: [ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6fc46679a7ba2ec82183cf01b80e5133-Paper-Conference.pdf))
> Generating the exact sequence of nodes representing the shortest path between two nodes in a graph structure.

## Relationships

### Associated with
- **Graph reasoning** (construct), 1 paper
  > We define the length-2 path problem on a graph, and use it as a means to understand other graph reasoning tasks such as graph connectivity, shortest path, and cycle detection. (Section 3.2)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **State tracking** (behavioral indicator), 1 paper
  > In the Shortest Path task, the model must find the shortest path from a given node to another. Intuitively, to effectively solve the problem, the model should maintain the state of its exploration in the graph
  - [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf)
