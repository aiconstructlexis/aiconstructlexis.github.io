# Pathfinding
**Type:** Behavioral indicator  
**Supporting papers:** 13  
**Also known as:** Graph path finding, Route finding, Spatial pathfinding, Path planning, Route planning, Path finding, Graph search, Search ability  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage treats pathfinding as producing a valid route from a start point to a goal in a structured space, most often a graph or grid. Papers variously require the output to be the constituent edges of the correct path, a sequence of nodes, actions, coordinates, or directional moves, and one next-step formulation asks for "the next vertex on the path from the start to the goal vertex." Success is usually framed as correctness or validity of the path under task constraints, though some formulations add conditions such as avoiding holes, retrieving keys before unlocking doors, or reaching the goal through a full trajectory.

**Variants.** Most variants study graph or grid navigation and use labels such as graph path finding, route finding, graph search, route planning, and path planning. These cover directed graphs, Frozen Lake style grids that require avoiding holes, maze tasks, grid worlds with dependencies such as move, pick up, and unlock, visual navigation that outputs a full sequence of directions, and agent path planning as a trajectory to a designated goal. A smaller line of work broadens the label to "search ability," either as a latent capacity to find a correct next step or path on graph-like problems, or as the ability to formulate queries, retrieve documents, and use external information in multi-hop question answering; another uses "path planning" for planning how to combine VideoAPI outputs, sequentially or in parallel.

**Space of elicitation and scores.** Only one measurement instrument is linked to pathfinding, Star Graph Task, which one paper uses to measure a simple path finding task that "requires basic planning." Outside that named instrument, papers usually elicit the behavior directly by asking for a next vertex, a full node or edge path, an action sequence, coordinates, or directions in graph and grid environments. Scoring is mostly by whether the produced path is correct or valid, while one path-planning study additionally has GPT-4o rate the reasonableness of a designed path on a 1-5 scale.

**What it is taken as evidence of.** Only one construct is linked to pathfinding, Planning. The recorded link is "related": papers say search is fundamental in tasks including planning, and describe a simple path finding task as one that "requires basic planning." No other construct link is recorded, so papers that connect pathfinding to a construct connect it to Planning.

## Sources

**Graph path finding** (1 paper: [Beyond Autoregression: Discrete Diffusion for Complex Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1b3d1e2cf53bb28cabd801bd58b3521-Paper-Conference.pdf))
> Given a graph-like input with start and goal nodes, the model outputs the constituent edges of the correct path.

**Route finding** (1 paper: [Enhancing Graph Of Thought: Enhancing Prompts with LLM Rationales and Dynamic Temperature Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/c87245c9e8882bc1b6d4ec343d430e71-Paper-Conference.pdf))
> Producing a valid path from a start location to a destination while obeying constraints in a grid world.

**Pathfinding** (3 papers: [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf), [seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs](https://aclanthology.org/2025.emnlp-main.1714.pdf), [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf))
> Solving navigation tasks by generating a sequence of actions or coordinates to reach a goal location from a start point.

**Path planning** (2 papers: [GAMap: Zero-Shot Object Goal Navigation with Multi-Scale Geometric-Affordance Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/459d93dad139eb084c365d40a57eada3-Paper-Conference.pdf), [VQAGuider: Guiding Multimodal Large Language Models to Answer Complex Video Questions](https://aclanthology.org/2025.acl-long.385.pdf))
> The process of computing a sequence of actions or a trajectory for an agent to follow to travel from its current position to a designated goal location.

**Route planning** (1 paper: [Mind's Eye of LLMs: Visualization-of-Thought Elicits Spatial Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/a45296e83b19f656392e0130d9e53cb1-Paper-Conference.pdf))
> A sub-task of visual navigation where the model must generate the complete sequence of directional moves to travel from a starting point to a destination.

**Path finding** (2 papers: [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf), [Metastable Dynamics of Chain-of-Thought Reasoning: Provable Benefits of Search, RL and Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25aj/kim25aj.pdf))
> The task of generating a sequence of nodes that constitutes a valid path from a starting node to a target node within a given graph structure.

**Graph search** (1 paper: [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf))
> Predicting the next vertex on a path from a start vertex toward a goal vertex in a directed graph.

**Search ability** (1 paper: [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf))
> The latent capacity of a model to find a correct next step or path toward a goal across graph-like or reasoning problems.

## Relationships

### Pathfinding →
- **Star Graph Task** (measurement instrument): *measured_by*, 1 paper
  > Specifically, Bachmann & Nagarajan (2024) introduces a simple path finding task that requires basic planning... Figure 5: Star Graph Task: Illustration and Performance Comparison. (Section 4)
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)

### Associated with
- **Planning** (construct), 2 papers
  > “The ability to search is fundamental in many important tasks, such as reasoning ..., planning ..., and navigation ...”
  - [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf)
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
