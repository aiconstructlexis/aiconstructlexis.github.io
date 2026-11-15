# Plan generation
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Transition pathway generation, Meta-plan generation, Action plan generation, Dialogue logic flow generation, Multi-step planning, Task planning  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage is the direct production of a sequence of actions or steps meant to solve a planning problem or achieve a specified goal. Many papers phrase this as moving from an initial state to a goal state, or as generating reasonable solutions for given tasks, and some make the directness explicit by describing a complete plan produced "without the help of any external planning library" or other external planner. A smaller range of formulations narrows the output to numbered steps, a step-by-step action plan, or an ordered sequence of API function calls.

**Variants.** Papers study this behavior in several task-specific forms. The most recurring alternate label is task planning, used for generating discrete steps for a high-level task and for step-by-step plans from safety guard inputs; smaller lines of work treat it as multi-step planning for ordered API calls, meta-plan generation for collaborative long-term decomposition into subtasks, transition pathway generation for textual material transformations from a source to a target with specified properties, and a turn-level dialogue flow that specifies intentions, slot-value pairs, and reasoning before utterance realization. Some authors also describe it more generally as producing a sequence of actions or thoughts toward a goal.

**Space of elicitation and scores.** Only one measurement instrument is linked to this behavior, VAL. In one paper, the plan produced from LLM-as-Planner is validated using VAL against ground-truth DFs and PFs, so the linked operationalization here is plan validation rather than a broader set of scoring tools.

**What it is taken as evidence of.** Construct links are narrow in the papers: the only linked construct is Planning, and the recorded relationship is that plan generation is related to it. One paper describes plan-and-solve prompting as first eliciting a plan, such as numbered steps, and then executing that plan. Beyond constructs, papers also relate plan generation to two other behavioral indicators, Collaboration and Code generation, through collaborative creation and refinement of meta-plans and through code generated from an outlined plan.

## Sources

**Plan generation** (6 papers: [Leveraging Environment Interaction for Automated PDDL Translation and Planning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/44af065477781e7f8a8589b14a62c489-Paper-Conference.pdf), [Revealing the Barriers of Language Agents in Planning](https://aclanthology.org/2025.naacl-long.93.pdf), [Language Models Can Infer Action Semantics for Symbolic Planners from Environment Feedback](https://aclanthology.org/2025.naacl-long.440.pdf), [System 1.x: Learning to Balance Fast and Slow Planning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/605e59e78284907aa4fce5280838def3-Paper-Conference.pdf), [Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/erdogan25a/erdogan25a.pdf), [LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60.pdf))
> The observable behavior of an LLM directly producing a sequence of actions intended to solve a planning problem, without translating to a formal language or using an external planner.

**Transition pathway generation** (1 paper: [MatExpert: Decomposing Materials Discovery By Mimicking Human Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d6850f4c82520793f738d98a72aab9d-Paper-Conference.pdf))
> The observable task of generating a textual, step-by-step plan outlining the necessary modifications to transform a source material into a target material with specified properties.

**Meta-plan generation** (1 paper: [CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf))
> The observable process where agents collaboratively analyze a task, discuss, and create a high-level, long-term plan that decomposes the task into subtasks with assigned steps.

**Action plan generation** (1 paper: [Interactive Speculative Planning: Enhance Agent Efficiency through Co-design of System and User Interface](https://proceedings.iclr.cc/paper_files/paper/2025/file/25458943db16e0f78f748ca5bc34fff6-Paper-Conference.pdf))
> The observable production of a sequence of actions or thoughts intended to achieve a specific goal.

**Dialogue logic flow generation** (1 paper: [From Schema to State: Zero-Shot Scheme-Only Dialogue State Tracking via Diverse Synthetic Dialogue and Step-by-Step Distillation](https://aclanthology.org/2025.emnlp-main.85.pdf))
> Creating a turn-level plan that specifies intentions, relevant slot-value pairs, and explanatory reasoning before utterance realization.

**Multi-step planning** (1 paper: [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.308.pdf))
> Producing an ordered sequence of API function calls as a solution plan to achieve a goal derived from a natural language task description.

**Task planning** (2 papers: [Flow-of-Options: Diversified and Improved LLM Reasoning by Thinking Through Options](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nair25c/nair25c.pdf), [GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiang25a/xiang25a.pdf))
> The behavior of an LLM generating a sequence of discrete steps required to complete a given high-level task.

## Relationships

### Plan generation →
- **VAL** (measurement instrument): *measured_by*, 1 paper
  > the plan produced from LLM-as-Planner is validated using VAL (Howey et al., 2004) against the ground-truth DFs and PFs provided above. (Section 4.2).
  - [On the Limit of Language Models as Planning Formalizers](https://aclanthology.org/2025.acl-long.242.pdf)

### Associated with
- **Collaboration** (behavioral indicator), 1 paper
  > CaPo enables agents to collaboratively create and refine long-term, strategic, and coherent meta-plans through multi-turn discussions.
  - [CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > In the second step, a complete code is generated based on the outlined plan by Agent B. (Section 4.1.1)
  - [Code-Generated Graph Representations Using Multiple LLM Agents for Material Properties Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25an/huang25an.pdf)
- **Planning** (construct), 1 paper
  > Planning: Plan-and-solve prompting (PS) (Wang et al., 2023) elicits the model to first generate a plan (e.g., numbered steps) and then execute that plan, yielding improvements over standard CoT. (Section 2)
  - [Prior Prompt Engineering for Reinforcement Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1590.pdf)
