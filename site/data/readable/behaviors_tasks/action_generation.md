# Action generation
**Type:** Behavioral indicator  
**Supporting papers:** 13  
**Also known as:** Executable action generation, Candidate action generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is the production of a concrete action to be executed in an environment, often as structured output that names the action and any parameters such as position or value. This is most commonly formulated as the next step given the current state, for example a GUI action based on the task, page, and history, or a navigation control action from the current location toward a goal or route. A smaller line of work makes the success criterion explicit as executability, defining good outputs as actions that are valid and can be carried out rather than invalid or nonsensical ones.

**Variants.** Most papers study it in GUI and computer control settings, where the model outputs actions such as click, scroll, input, or type text. Smaller variants appear in urban navigation, where the output is the next control action such as ascend or turn right, and in embodied robotics, where the model predicts low-level action sequences, including pose changes and end-effector status, sometimes as discrete action tokens generated autoregressively. Papers also name narrower forms such as executable action generation and candidate action generation, the latter described as sampling possible next inquiry actions from a masked action space.

**Space of elicitation and scores.** No measurement instrument is linked to it. In practice, papers elicit it by conditioning on the current task, GUI page, action history, route or goal, or visual and linguistic inputs, and asking for the next action or a sequence of actions. For the executable-action variant, one paper scores it as the proportion of generated actions that are executable at each timestep, calling this executability.

**What it is taken as evidence of.** Only one construct is linked to it, Reasoning. The recorded link is a causal claim from Reasoning to Action generation: one paper describes complex GUI tasks as moving from perception and understanding, to "Reason and plan", to execution of the desired action. No other construct link is recorded.

## Sources

**Action generation** (6 papers: [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf), [UrbanVideo-Bench: Benchmarking Vision-Language Models on Embodied Intelligence with Video Data in Urban Spaces](https://aclanthology.org/2025.acl-long.1558.pdf), [UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25w/zhang25w.pdf), [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://aclanthology.org/2025.emnlp-main.212.pdf), [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://proceedings.iclr.cc/paper_files/paper/2024/file/52f050499cf82fa8efb588e263f6f3a7-Paper-Conference.pdf), [ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation](https://aclanthology.org/2025.naacl-long.244.pdf))
> Producing a structured output that specifies an action to be taken (e.g., 'click', 'type text') and its associated parameters, such as position or value.

**Executable action generation** (1 paper: [HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model](https://aclanthology.org/2025.acl-long.1575.pdf))
> Producing actions that are valid and can be successfully executed within the environment, as opposed to invalid or nonsensical actions.

**Candidate action generation** (1 paper: [DDO: Dual-Decision Optimization for LLM-Based Medical Consultation via Multi-Agent Collaboration](https://aclanthology.org/2025.emnlp-main.1340.pdf))
> The model or policy samples a set of possible next inquiry actions from a masked action space.

## Relationships

### → Action generation
- **Reasoning** (construct): *causes*, 1 paper
  > For vision-based agents, completing a complex GUI task typically involves several steps, each requiring the model to: (1) Perceive and understand... (2) Reason and plan... (3) Execute: perform the desired action on the target GUI element.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
