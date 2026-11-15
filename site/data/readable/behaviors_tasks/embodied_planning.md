# Embodied planning
**Type:** Behavioral indicator  
**Supporting papers:** 13  
**Also known as:** Task planning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats embodied planning as generating a sequence of actions for an agent to execute, or use to interact with, a simulated or physical environment in order to achieve a goal. Definitions agree on action-sequence generation in embodied settings, sometimes adding domains such as household or scientific settings, while a smaller line uses the nearby label task planning for generating or refining robotic action plans from natural-language goals and failure feedback. For success, one measurement-oriented formulation says that a successful multi-step plan requires single-step optimality at each planning step.

**Variants.** Papers study this behavior in both simulated and physical environments, and the named settings include robotic tasks, household settings, and scientific settings. Some authors call the behavior task planning, especially when plans are generated or refined from natural-language goals and failure feedback, while one paper operationalizes it through ALFWorld under the label embodied decision. A smaller line also relates embodied planning to environment exploration through an exploration-integrated task planning scheme.

**Space of elicitation and scores.** Papers measure it with 4 instruments: ALFWorld, BabyAI, ScienceWorld, and VirtualHome. These instruments are used as embodied task settings, and the clearest scoring statement appears for ScienceWorld and VirtualHome, where a successful multi-step plan requires single-step optimality in each planning step. Other papers simply place BabyAI under embodied planning and ALFWorld under an embodied decision task category.

**What it is taken as evidence of.** Papers do not present a single agreed construct that embodied planning indicates. Instead, it is linked to 3 constructs: one paper claims a causal relationship from In-context learning to embodied planning, saying that in-context example selection affects the performance of LLM-based task planners; another claims a causal relationship from Commonsense knowledge to embodied planning in task planning; and a separate paper relates embodied planning to Long-horizon planning, describing embodied scenarios as requiring long-term planning in intricate contexts.

## Sources

**Embodied planning** (2 papers: [Benchmarking Agentic Workflow Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/adbe936993aa7cf41e45054d8b72f183-Paper-Conference.pdf), [AgentRM: Enhancing Agent Generalization with Reward Modeling](https://aclanthology.org/2025.acl-long.945.pdf))
> The task of generating a sequence of actions for an agent to execute within a simulated or physical environment.

**Task planning** (2 papers: [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf), [ExploraCoder: Advancing Code Generation for Multiple Unseen APIs via Planning and Chained Exploration](https://aclanthology.org/2025.acl-long.887.pdf))
> Generating or refining action plans for robotic tasks from natural-language goals and failure feedback.

## Relationships

### Embodied planning →
- **ScienceWorld** (measurement instrument): *measured_by*, 1 paper
  > for embodied planning tasks in ScienceWorld and VirtualHome, a successful multi-step plan requires single-step optimality in each planning step.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
- **VirtualHome** (measurement instrument): *measured_by*, 1 paper
  > for embodied planning tasks in ScienceWorld and VirtualHome, a successful multi-step plan requires single-step optimality in each planning step.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
- **ALFWorld** (measurement instrument): *measured_by*, 1 paper
  > “We conduct experiments on three representative agent tasks: Complex Reasoning (HotpotQA (Yang et al., 2018)), Embodied Decision (ALFWorld (Shridhar et al., 2020)), and Interactive Programming (InterCode (Yang et al., 2023))”
  - [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf)
- **BabyAI** (measurement instrument): *measured_by*, 1 paper
  > Babyai for embodied planning (Section 4.2)
  - [AgentRM: Enhancing Agent Generalization with Reward Modeling](https://aclanthology.org/2025.acl-long.945.pdf)

### → Embodied planning
- **In-context learning** (construct): *causes*, 1 paper
  > These experiments confirm that the in-context example selecting strategy has a significant impact on the performance of LLM-based task planners (Section 6.1).
  - [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf)
- **Commonsense knowledge** (construct): *causes*, 1 paper
  > Large language models(LLMs) trained on massive corpora are generally considered to have acquired common sense knowledge for task planning
  - [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/8ec46cecdae5407662899c5f6698cd8b-Paper-Conference.pdf)

### Associated with
- **Environment exploration** (behavioral indicator), 1 paper
  > we employ an exploration-integrated task planning scheme, in which the information-based exploration is incorporated into the LLM-based planning process. (Introduction)
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **Long-horizon planning** (construct), 1 paper
  > embodied scenarios pose greater challenges, requiring long-term planning in intricate contexts with high-dimensional state spaces and tangible interactions.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
