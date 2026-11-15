# Task decomposition
**Type:** Behavioral indicator  
**Supporting papers:** 62  
**Also known as:** Program decomposition, Subtask decomposition, Request decomposition, Problem decomposition, Subgoal generation, Subtask identification, Plan decomposition, Subgoal proposal, Subgoal setting, Sub-goal decomposition, Constraint decomposition, Action decomposition, Requirement analysis, High-level instruction generation, High-level planning, Sub-instruction prediction, Subgoal decomposition, Task planning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats task decomposition as breaking a complex, high-level goal, instruction, query, or problem into smaller and more manageable subtasks, sub-actions, or subgoals. Most descriptions make these units concrete and actionable, often as ordered steps or structured plans, and some further require feasibility from current observations and memory or specify dependencies and execution order. A smaller line of work treats it as a latent ability to hierarchically break down problems, rather than only as an overt generated plan.

**Variants.** Papers use several neighboring names for this behavior, including program, problem, request, and plan decomposition, along with subgoal generation or setting. The settings are varied: code generation and modular functions, tool and web agent planning, multi-agent robot instructions, multimodal queries represented as computation graphs, and math or control problems where the output is intermediate statements or STL constraints. Other papers recast the behavior as sub-instruction prediction, constraint decomposition, action decomposition, requirement analysis, or high-level planning.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers operationalize it through the decomposition they ask models to produce, such as step-by-step language plans, subtasks with dependencies and execution order, reusable functions or modules, computation graphs, or intermediate subgoals and constraints.

**What it is taken as evidence of.** Papers link task decomposition to five constructs, and the prevailing links are planning-oriented. A few papers claim a causal relationship from Planning to task decomposition, another line of work claims a causal relationship from task decomposition to Long-horizon planning, and smaller lines of work describe it as related to Multi-step planning, Scientific reasoning, and Task planning. Because these links mix directions and relation types, the papers do not converge on a single construct that it is taken to evidence.

## Sources

**Program decomposition** (1 paper: [Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bc4f74e35bcfe8cfe43b0a860786d6a-Paper-Conference.pdf))
> The observable behavior of breaking down a complex programming problem into smaller, more manageable sub-problems, often represented as distinct functions.

**Task decomposition** (8 papers: [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf), [HyperTree Planning: Enhancing LLM Reasoning via Hierarchical Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gui25b/gui25b.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf), [Grounding Language Plans in Demonstrations Through Counterfactual Perturbations](https://proceedings.iclr.cc/paper_files/paper/2024/file/be62c4a943675195ff5a2a98d5b9724f-Paper-Conference.pdf), [Towards Robust Multi-Modal Reasoning via Model Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c78ae0c1140902bf3a430b1725bcc4e-Paper-Conference.pdf), [Transformers Provably Solve Parity Efficiently with Chain of Thought](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e2986deda273d8fb903342841fcc4dc-Paper-Conference.pdf), [Adversaries Can Misuse Combinations of Safe Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jones25a/jones25a.pdf), [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf))
> The observable process of breaking down a complex, high-level goal into a series of smaller, more manageable sub-tasks or sub-actions.

**Subtask decomposition** (1 paper: [Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d6e85e88495104442af94c98e899659-Paper-Conference.pdf))
> The observable action of breaking down a high-level language instruction into a sequence of smaller, feasible subtasks based on current observations and memory.

**Request decomposition** (1 paper: [Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf))
> The observable behavior of an LLM breaking down a user's ambiguous, high-level request into a sequence of concrete, actionable steps.

**Problem decomposition** (2 papers: [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf), [ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search](https://aclanthology.org/2025.acl-long.538.pdf))
> The observable action of breaking down a complex question or problem into a structured plan of simpler, actionable steps.

**Subgoal generation** (2 papers: [Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf), [HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model](https://aclanthology.org/2025.acl-long.1575.pdf))
> The observable action of producing a set of intermediate mathematical statements (subgoals) from a current goal state by applying theorems or transformation rules.

**Subtask identification** (1 paper: [What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf))
> Observably decomposing a complex task instruction into its constituent subtasks based on semantic content.

**Subgoal proposal** (1 paper: [PDE-Controller: LLMs for Autoformalization and Reasoning of PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/soroco25a/soroco25a.pdf))
> The observable generation of intermediate STL constraints (subgoals) intended to improve the solution of a primary PDE control problem when solved sequentially.

**Plan decomposition** (1 paper: [AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf))
> Breaking down high-level AutoML plans into role-specific sub-tasks assigned to specialized agents, such as data preprocessing or model search.

**Subgoal setting** (1 paper: [Prior Prompt Engineering for Reinforcement Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1590.pdf))
> Generating intermediate steps or subgoals that break a problem into smaller parts.

**Sub-goal decomposition** (1 paper: [System 1.x: Learning to Balance Fast and Slow Planning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/605e59e78284907aa4fce5280838def3-Paper-Conference.pdf))
> The observable action of breaking down a larger planning problem into a series of smaller, intermediate sub-problems, each with its own start and end state.

**Constraint decomposition** (1 paper: [DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/73d6c3e4b214deebbbf8256e26d2cf45-Paper-Conference.pdf))
> The observable task of splitting a target VRP into individual constraints represented by keywords.

**Action decomposition** (1 paper: [LLM Meets Scene Graph: Can Large Language Models Understand and Generate Scene Graphs? A Benchmark and Empirical Study](https://aclanthology.org/2025.acl-long.1036.pdf))
> The process of identifying and separating a complex narrative into a sequence of discrete actions to be represented as individual scene graphs.

**Requirement analysis** (1 paper: [From Informal to Formal – Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs](https://aclanthology.org/2025.acl-long.1310.pdf))
> The observable behavior of taking a high-level goal in natural language and breaking it down into a series of detailed steps, also in natural language.

**High-level instruction generation** (1 paper: [Hierarchical-Task-Aware Multi-modal Mixture of Incremental LoRA Experts for Embodied Continual Learning](https://aclanthology.org/2025.acl-long.1379.pdf))
> Producing decomposed sub-task plans from high-level goals and environmental observations, such as generating 'Pick up the blue book' from 'Read a book under the light'.

**High-level planning** (1 paper: [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf))
> Generating a small set of task milestones or subtasks from a visual preview or textual description of a GUI goal.

**Sub-instruction prediction** (1 paper: [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf))
> Generating a sequence of intermediate natural language instructions that decompose a high-level user request into actionable steps.

**Subgoal decomposition** (1 paper: [SELFGOAL: Your Language Agents Already Know How to Achieve High-level Goals](https://aclanthology.org/2025.naacl-long.36.pdf))
> Breaking a high-level goal into more concrete subgoals during interaction with an environment.

**Task planning** (2 papers: [Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://aclanthology.org/2025.naacl-long.83.pdf), [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44.pdf))
> The observable behavior of decomposing a complex user request into a sequence of subtasks with dependencies and execution order, each optimized for single-tool execution.

## Relationships

### Task decomposition →
- **Long-horizon planning** (construct): *causes*, 1 paper
  > allows agents to: (1) plan subtasks required to complete the task ... This framework enhances agents' ability to complete complex, long-horizon tasks
  - [Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d6e85e88495104442af94c98e899659-Paper-Conference.pdf)
- **STEM problem solving** (behavioral indicator): *causes*, 1 paper
  > This decomposition enhances the understanding of individual components and their interactions, facilitating the resolution of the original problem in a structured manner (Johnson et al., 2017).
  - [ChemAgent: Self-updating Memories in Large Language Models Improves Chemical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa7f64b45970e6a7f8824781e7e01501-Paper-Conference.pdf)
- **Premature termination** (behavioral indicator): *causes*, 1 paper
  > The primary responsibility of the Planning Agent is doing macro-level planning through task decomposition to prevent premature termination. (Section 3.3)
  - [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf)
- **Tool use** (behavioral indicator): *causes*, 1 paper
  > Through its task decomposition mechanism, Smurfs transforms long-context tasks into simpler ones, enabling the untrained model to effectively utilize external tools for managing complex tasks. (Section 4.1)
  - [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf)
- **Scene graph generation** (behavioral indicator): *causes*, 1 paper
  > Our analysis indicates that these models fail to effectively decompose discrete scenes from a complex narrative, leading to a bottleneck when generating scene graphs.
  - [LLM Meets Scene Graph: Can Large Language Models Understand and Generate Scene Graphs? A Benchmark and Empirical Study](https://aclanthology.org/2025.acl-long.1036.pdf)

### → Task decomposition
- **Planning** (construct): *causes*, 2 papers
  > Using the strategy stored in Planning Memory, we break down complex chemistry problems into hierarchical sub-tasks.
  - [ChemAgent: Self-updating Memories in Large Language Models Improves Chemical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa7f64b45970e6a7f8824781e7e01501-Paper-Conference.pdf)
  - [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)

### Associated with
- **Scientific reasoning** (construct), 1 paper
  > PDE-Controller ... enhances scientific reasoning by proposing novel subgoals to improve open-loop control utility. (Section 1)
  - [PDE-Controller: LLMs for Autoformalization and Reasoning of PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/soroco25a/soroco25a.pdf)
- **Multi-step planning** (construct), 1 paper
  > In this work, we formalize natural planning—distinct from classical AI planning (which is not the focus of this work)—as the process of decomposing an input problem x into an ordered sequence of intermediate subgoals that guide its solution. (Section 3.1)
  - [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1087.pdf)
- **Task planning** (construct), 1 paper
  > The current solution of task planning is purely based on LLMs and involves two stages [45, 46]. The first stage involves request decomposition, where a user’s ambiguous request is broken down into concrete steps via LLMs. (Section 2.2)
  - [Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf)
- **Problem solving** (behavioral indicator), 1 paper
  > Solving real-world problems with LLM agents can be structured into a multi-stage procedure: • Decomposition of the problem: The procedure begins by breaking down a complex question into an actionable plan characterized by simpler steps. (Section 3).
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > RL-GPT decomposes the task into “find a tree" and “cut a log", solving the former with code generation and the latter with RL.
  - [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator), 1 paper
  > "we decompose the retrieval into three sub-processes, including problem decomposition, single-constraint resolution, and context merging."
  - [DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/73d6c3e4b214deebbbf8256e26d2cf45-Paper-Conference.pdf)
