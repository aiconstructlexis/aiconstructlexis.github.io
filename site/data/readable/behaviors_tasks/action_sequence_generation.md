# Action sequence generation
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Multi-step action generation  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this behavior as generating an ordered sequence of actions that an agent can execute to accomplish a task. Most definitions emphasize structured, discrete outputs, such as environment moves, API calls, or website actions, and frame success as reaching an objective or successfully completing the requested task from the current state or user request. A smaller variant uses the name multi-step action generation and describes the same observable behavior as producing discrete actions to complete a task; in the API-based framing, one paper also states that each next action depends on the history actions.

**Variants.** Papers study this behavior in several settings rather than a single task format. The main variants are traversing 2D game maps by producing moves such as move_up or move_left, fulfilling user queries through ordered API calls, completing website tasks through executable web actions, and web navigation settings described as requiring multi-step actions. The naming is mostly action sequence generation, with a smaller use of multi-step action generation.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior. The descriptions instead portray task-specific evaluation of whether the generated sequence takes the agent from its current position to an objective or successfully completes the target task.

**What it is taken as evidence of.** No construct is linked to this behavior as what it is evidence of.

## Sources

**Action sequence generation** (3 papers: [GameTraversalBenchmark: Evaluating Planning Abilities Of Large Language Models Through Traversing 2D Game Maps](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852c8254bc6d904c09db9921157f59b-Paper-Datasets_and_Benchmarks_Track.pdf), [ShortcutsBench: A Large-Scale Real-world Benchmark for API-based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c16a99558b0b4f6b10966ca9bdb98ade-Paper-Conference.pdf), [AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25m/xu25m.pdf))
> The task of producing a structured list of discrete actions (e.g., 'move_up', 'move_left') for an agent to execute in an environment.

**Multi-step action generation** (1 paper: [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf))
> The observable behavior of producing a sequence of discrete actions to complete a task, such as in web navigation.
