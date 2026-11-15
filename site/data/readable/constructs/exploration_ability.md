# Exploration ability
**Type:** Construct  
**Supporting papers:** 25  
**Also known as:** Exploration, Exploration capability, Self-exploration, Parallel search, Search  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats exploration ability as breadth of search: a latent ability, tendency, or process for searching broadly across a solution space and generating varied reasoning trajectories or solution paths. Many definitions stress discovering novel or effective solutions through diverse reasoning paths, multiple candidate answers, or trial-and-error alternatives. A smaller line of work uses the same term for active environment search to locate objects or information, and a few papers narrow it to search over candidate programs or puzzle states. The main disagreement is whether exploration is a latent model property or an observable search behavior, and whether the search happens in reasoning space, an embodied environment, or a program space.

**Space of facets.** Papers use several overlapping labels around this construct. "Self-exploration" is a narrower version centered on identifying flaws in one's reasoning and generating alternative paths without external intervention, while "parallel search" names an observable behavior in which multiple distinct solution paths or program fragments are explored within a single iteration. Several authors also use "search" as a near-synonym for exploration, especially for candidate programs or puzzle moves, and one line of work places exploration alongside backtracking and verification as structural patterns in long reasoning chains. Exploration is also repeatedly contrasted with exploitation, or with only refining existing solutions.

**Space of measurement.** No measurement instrument is linked to it, and papers link it to one behavioral indicator, Sudoku solving. In the papers' own operational language, exploration is made visible through diverse reasoning paths and alternative branches, pass@k relative to pass@1, oversampling or temperature adjustment to increase sampling diversity and maintain entropy, and within-prompt parallel search over different leaf nodes. These proxies mostly match the dominant breadth-of-search framing, though some papers use the same construct for embodied exploration of environments rather than only for reasoning diversity.

**Links.** Only one paper reports that exploration ability is related to Sudoku solving. In that paper, Sudoku solving is described as involving "searching and finding a cell position where we can apply a subset of the strategies," so the recorded relationship is a related link between exploration/search and that task, not a causal or correlational claim. No other links are reported.

## Sources

**Exploration capability** (1 paper: [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf))
> The latent ability of an agent to discover useful states and solution paths in environments that require systematic search over long horizons.

**Exploration** (3 papers: [SFS: Smarter Code Space Search improves LLM Inference Scaling](https://proceedings.iclr.cc/paper_files/paper/2025/file/387982dbf23d9975c7fc45813dd3dabc-Paper-Conference.pdf), [T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25e/hou25e.pdf), [What Makes a Good Reasoning Chain? Uncovering Structural Patterns in Long Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.329.pdf))
> The process of searching broadly across a solution space to discover varied and potentially novel solutions, rather than focusing only on refining existing ones.

**Exploration ability** (2 papers: [MARGE: Improving Math Reasoning with Guided Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25h/gao25h.pdf), [Enhancing Efficiency and Exploration in Reinforcement Learning for LLMs](https://aclanthology.org/2025.emnlp-main.75.pdf))
> The tendency of a model to generate diverse reasoning paths and cover more of the solution space when producing multiple candidate answers.

**Self-exploration** (1 paper: [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf))
> The latent ability of a model to identify flaws in its reasoning and generate alternative solution paths without external intervention.

**Parallel search** (1 paper: [Execution-guided within-prompt search for programming-by-example](https://proceedings.iclr.cc/paper_files/paper/2025/file/98e967164ae2f6811b975d686dece3eb-Paper-Conference.pdf))
> An observable search behavior where the model explores multiple distinct solution paths or program fragments within a single iteration.

**Search** (1 paper: [The KoLMogorov Test: Compression by Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/db1d69ee01c2b42554f8e14e6f8ca8b6-Paper-Conference.pdf))
> The latent ability to explore candidate programs and find one that matches the target sequence under a shortest-program criterion.

## Relationships

### Associated with
- **Sudoku solving** (behavioral indicator), 1 paper
  > “The iterative process of solving Sudokus can be broken down into two steps: (1) searching and finding a cell position where we can apply a subset of the strategies”
  - [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf)
