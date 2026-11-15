# Long-horizon planning
**Type:** Construct  
**Supporting papers:** 34  
**Also known as:** Long-term planning, High-level planning, Long-term reasoning, Long-horizon reasoning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage describes long-horizon planning as the capacity to produce, formulate, or execute coherent sequences of actions over many steps to achieve complex, distant, or sometimes multiple concurrent goals. Recurring qualifiers are interdependent actions, constraints, partial observability, and maintaining coherence across extended action or interaction sequences. A smaller line of work uses nearby labels such as long-term planning, high-level planning, long-term reasoning, and long-horizon reasoning, shifting emphasis from action sequencing to high-level strategy adaptation over time or sustained reasoning across multiple rounds.

**Space of facets.** Papers most often systematize the construct hierarchically. One account says a bi-level approach decomposes long-horizon planning problems into several short-horizon problems, while others define it through decomposition of complex objectives or high-level instructions into coordinated subtasks, sequential grounded sub-goals, and low-level actions. In one embodied formulation, plans are further broken into subtask types such as environment exploration and navigation. Terminology also overlaps, with some papers treating planning and reasoning labels as near substitutes for maintaining a coherent path to a distant goal.

**Space of measurement.** The construct is linked to 2 measurement instruments and 7 behavioral indicators. The only explicit measurement link is TravelPlanner, described as a benchmark that tests long-horizon planning under user-defined constraints; Minecraft is also linked as an open-ended platform for exploring such capabilities, though that link is recorded as related rather than measured_by. Among behavioral indicators, the named links include embodied planning, environment exploration, and navigation, alongside other indicators. Beyond those links, papers operationalize the construct with benchmark or environment setups that stress long texts, multiple interactions, concurrent objectives, error handling, sequential instruction chains, partially observable embodied settings, long desktop workflows, and full-trajectory feedback. These operationalizations mostly track the dominant definition of extended multi-step action planning, though some align more with reasoning-oriented variants by emphasizing coherent multi-turn reasoning or complete trajectory context.

**Links.** A few papers claim causal relationships from task decomposition to long-horizon planning, with one framework saying subtasks enhance agents' ability to complete complex, long-horizon tasks, and from self-correction to long-horizon planning, where self-refinement is said to iteratively improve a generated plan and improve the ability to plan ahead. Related links also connect it to hierarchical planning, embodied planning, and long-term memory, alongside other tasks, environments, and subtasks. One related task is explicitly described as not requiring the same degree of long-term planning as harder benchmarks. No correlational relationships are reported.

## Sources

**Long-horizon planning** (7 papers: [Learning Grounded Action Abstractions from Language](https://proceedings.iclr.cc/paper_files/paper/2024/file/99dec5837aae1a7459960c6121b9e3b8-Paper-Conference.pdf), [SmartPlay : A Benchmark for LLMs as Intelligent Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/063d1fadbde557466bf5bcffe814a64e-Paper-Conference.pdf), [Vision-Language Foundation Models as Effective Robot Imitators](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf), [Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d6e85e88495104442af94c98e899659-Paper-Conference.pdf), [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://proceedings.iclr.cc/paper_files/paper/2025/file/394c7c30ea87b5c3521b4d9e9d419071-Paper-Conference.pdf), [DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance by Adaptive Tree Traversal](https://aclanthology.org/2025.acl-long.973.pdf), [DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation](https://aclanthology.org/2025.emnlp-main.58.pdf))
> Producing action sequences that achieve a goal over many steps or with multiple concurrent objectives.

**Long-term planning** (2 papers: [Large Language Models Play StarCraft II:Benchmarks and A Chain of Summarization Approach](https://proceedings.neurips.cc/paper_files/paper/2024/file/f0ebc318e2df08360b2df559e81602e5-Paper-Conference.pdf), [ProcWorld: Benchmarking Large Model Planning in Reachability-Constrained Environments](https://aclanthology.org/2025.emnlp-main.635.pdf))
> The capacity to formulate and adapt high-level strategies that unfold over an extended period to achieve a final goal.

**High-level planning** (1 paper: [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf))
> The capacity to generate and execute long-horizon, goal-directed plans under constraints, requiring decomposition of complex objectives into coordinated subtasks.

**Long-term reasoning** (2 papers: [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf), [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c493d23af93118975cdbc32cbe7323f5-Paper-Conference.pdf))
> The latent ability to maintain coherent and effective reasoning over multiple interaction rounds to achieve a distant goal.

**Long-horizon reasoning** (1 paper: [Structured Preference Optimization for Vision-Language Long-Horizon Task Planning](https://aclanthology.org/2025.emnlp-main.884.pdf))
> The ability of a model to generate and maintain a coherent, multi-step plan to achieve a complex goal over an extended sequence of actions.

## Relationships

### Long-horizon planning →
- **TravelPlanner** (measurement instrument): *measured_by*, 1 paper
  > TravelPlanner (TP) (Xie et al., 2024), which tests long-horizon planning under user-defined constraints (Section 5.1)
  - [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf)

### → Long-horizon planning
- **Task decomposition** (behavioral indicator): *causes*, 1 paper
  > allows agents to: (1) plan subtasks required to complete the task ... This framework enhances agents' ability to complete complex, long-horizon tasks
  - [Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d6e85e88495104442af94c98e899659-Paper-Conference.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > “self-refinement ... iteratively improves a previously generated plan” and “bidirectional dependency ... thus improving its ability to plan ahead”
  - [Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cd/li25cd.pdf)

### Associated with
- **Hierarchical planning** (construct), 1 paper
  > This bi-level planning approach decomposes long-horizon planning problems into several short-horizon problems. (Section 2)
  - [Learning Grounded Action Abstractions from Language](https://proceedings.iclr.cc/paper_files/paper/2024/file/99dec5837aae1a7459960c6121b9e3b8-Paper-Conference.pdf)
- **Embodied planning** (behavioral indicator), 1 paper
  > embodied scenarios pose greater challenges, requiring long-term planning in intricate contexts with high-dimensional state spaces and tangible interactions.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
- **Sudoku solving** (behavioral indicator), 1 paper
  > Sudoku is a task which doesn't require the same degree of long-term planning as some harder benchmarks
  - [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf)
- **Theorem proving** (behavioral indicator), 1 paper
  > "the whole-proof generation model is trained to perform long-term planning for theorem proving"
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
- **Long-term memory** (construct), 1 paper
  > “long-horizontal reasoning due to the partial observability of complex GCC tasks, which also leads to the demand for long-term memory to maintain past useful experiences”
  - [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf)
- **Minecraft** (measurement instrument), 1 paper
  > Compared with other embodied benchmarks, Minecraft is an open-ended platform suitable for exploring building agents with long-horizon planning capabilities (Fan et al., 2022).
  - [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dj/li25dj.pdf)
- **Navigation** (behavioral indicator), 1 paper
  > Based on these requirements, a plan is created consisting of three distinct types of sub-tasks: ... (3) Navigation sub-tasks enable efficient access to specific areas, thereby narrowing the exploration scope. (Section 3.2)
  - [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf)
- **Environment exploration** (behavioral indicator), 1 paper
  > Based on these requirements, a plan is created consisting of three distinct types of sub-tasks: (1) Collection sub-tasks gather the requisite information... (Section 3.2)
  - [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf)
