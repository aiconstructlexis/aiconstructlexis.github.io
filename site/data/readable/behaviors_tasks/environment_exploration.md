# Environment exploration
**Type:** Behavioral indicator  
**Supporting papers:** 10  
**Also known as:** Information collection, Active information gathering, Active exploration, Exploration  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is active interaction with an environment to gather information, often to verify conditions, update an internal world-state representation, or reduce uncertainty under partial observations. In embodied and visual settings, this commonly means moving, looking around, and adjusting viewpoint to obtain visual inputs, locate landmarks or target objects, or answer a question. A smaller line of work uses the same behavior in a codebase environment, where agents inspect the codebase and execute commands to understand the current system state.

**Variants.** Papers use several nearby labels for this behavior, including active exploration, information collection, and active information gathering. A common variant centers on embodied navigation and visual search, including collection sub-tasks that gather requisite information and refine the observation view for higher-quality inputs, and exploration sub-tasks that identify landmarks or target objects with a "Move and Look Around" strategy. Other variants place the behavior in reachability-constrained or partially observed environments, in task completion when object positions are not fully specified, and in novelty-seeking visits to new states or regions; papers also relate it to embodied planning and embodied question answering, describing exploration-integrated planning and question answering that requires active exploration.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior in the papers. Instead, papers operationalize it through task setups and sub-task labels, such as collection and exploration sub-tasks, moving and looking around from multiple viewpoints, or executing commands to inspect a codebase environment.

**What it is taken as evidence of.** At the construct level, papers link it only to Long-horizon planning. That link is recorded as related: a paper describes plans composed of sub-tasks, including collection sub-tasks that gather requisite information. No construct is linked through measured_by, causes, or correlates relations.

## Sources

**Environment exploration** (2 papers: [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf), [SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25l/guo25l.pdf))
> The observable action of an agent interacting with its environment to gather information, verify conditions, and update its internal representation of the world state.

**Information collection** (1 paper: [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf))
> The observable behavior of gathering specific details from visual observations, often involving fine-grained adjustments to viewpoint or focus to improve input quality.

**Active information gathering** (1 paper: [ProcWorld: Benchmarking Large Model Planning in Reachability-Constrained Environments](https://aclanthology.org/2025.emnlp-main.635.pdf))
> The behavior of strategically exploring the environment to reduce uncertainty, such as navigating to new locations or interacting with objects to reveal hidden states.

**Active exploration** (1 paper: [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf))
> Moving through an environment to gather visual information needed to answer a question.

**Exploration** (3 papers: [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf), [Large Language Models as Generalizable Policies for Embodied Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/8f9461d11e8ce9b0b28b21bfc645d74e-Paper-Conference.pdf), [Motif: Intrinsic Motivation from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/a8de97fa77a09258b22880c230a83445-Paper-Conference.pdf))
> The observable behavior of systematically scanning the environment to locate target objects, using strategies like moving and looking around from multiple viewpoints.

## Relationships

### Associated with
- **Embodied planning** (behavioral indicator), 1 paper
  > we employ an exploration-integrated task planning scheme, in which the information-based exploration is incorporated into the LLM-based planning process. (Introduction)
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **Embodied question answering** (behavioral indicator), 1 paper
  > Embodied Question Answering (EQA) ... must actively explore its environment to answer questions posed in natural language. (Section 1)
  - [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf)
- **Long-horizon planning** (construct), 1 paper
  > Based on these requirements, a plan is created consisting of three distinct types of sub-tasks: (1) Collection sub-tasks gather the requisite information... (Section 3.2)
  - [CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://aclanthology.org/2025.emnlp-main.630.pdf)
