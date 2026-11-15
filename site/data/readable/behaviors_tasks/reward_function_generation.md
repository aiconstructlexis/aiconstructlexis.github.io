# Reward function generation
**Type:** Behavioral indicator  
**Supporting papers:** 9  
**Also known as:** Dense reward code generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is the production of executable reward-function code for a simulation or reinforcement learning task. Most papers describe it as generating the part of the environment or task code that specifies the agent's objective or reward signal, usually from a task description together with environment code, goal descriptions, or low-level states. A narrower variant describes the behavior as dense reward code generation, where the model produces a shaped dense reward program from a natural-language goal. Papers vary in how they state success: some focus on returning code that defines a scalar reward whose cumulative maximization defines the task, while others describe outputting code such that a downstream objective is maximized or code that correctly uses environment attributes to encourage a specified tactic.

**Variants.** Papers study this behavior under the names reward function generation and dense reward code generation. The settings are varied but mostly involve simulations or environment code: definitions mention robotics and games, simulated worlds where reward generation appears alongside simulator dynamics or termination functions, multi-agent coordination where the reward encodes a desired coordination behavior such as a passing tactic, and robot subtasks trained with reinforcement learning. Some papers also place it next to related code-generation targets such as task specifications, scene configurations, and simulator dynamics rather than treating reward code in isolation.

**Space of elicitation and scores.** No measurement instrument is linked to it. In the task formulations themselves, papers usually elicit the behavior by giving a natural-language goal or task description together with environment code information or low-level states and asking for an executable reward program, sometimes in a required format such as "def reward(self) -> float" or as a function from state and action variables to a scalar value. When scoring is stated directly, papers describe either maximizing an objective over the generated reward code or verifying that the function correctly uses provided environment attributes to encourage the target behavior.

**What it is taken as evidence of.** Papers do not consistently present this behavior as evidence of a broader construct. Only one construct is linked, Commonsense reasoning, and one paper claims a causal relationship from Commonsense reasoning to Reward function generation, saying that reward generation from natural-language task descriptions leverages LLMs' "commonsense understanding of human behavior."

## Sources

**Reward function generation** (6 papers: [FactorSim: Generative Simulation via Factorized Representation](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f35ec2f7f403ef2c83d65b581df10bc-Paper-Conference.pdf), [OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/d40d7cbe7210f8a13ea0149eeae9c6de-Paper-Conference.pdf), [Eureka: Human-Level Reward Design via Coding Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf), [LLM-Assisted Semantically Diverse Teammate Generation for Efficient Multi-agent Coordination](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dq/li25dq.pdf), [R*: Efficient Reward Design via Reward Structure Evolution and Parameter Alignment Optimization with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25v/li25v.pdf), [Hazards in Daily Life? Enabling Robots to Proactively Detect and Resolve Anomalies](https://aclanthology.org/2025.naacl-long.379.pdf))
> The task of generating code for reward functions that specify the objectives for an agent within a simulation.

**Dense reward code generation** (1 paper: [Text2Reward: Reward Shaping with Language Models for Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/9941833e8327910ef25daeb9005e4748-Paper-Conference.pdf))
> The observable action of the LLM producing an executable program that defines a dense, shaped reward function based on a natural language goal.

## Relationships

### → Reward function generation
- **Commonsense reasoning** (construct): *causes*, 1 paper
  > In recent works, large language models (LLMs) have been used for reward generation from natural language task descriptions, leveraging their extensive instruction tuning and commonsense understanding of human behavior. (Abstract)
  - [REvolve: Reward Evolution with Large Language Models using Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc8ee7c7ab5b5f6b1615045dfb617ed6-Paper-Conference.pdf)
