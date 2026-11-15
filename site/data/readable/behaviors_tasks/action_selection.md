# Action selection
**Type:** Behavioral indicator  
**Supporting papers:** 19  
**Also known as:** Decision-making, Driving decision making, Autonomous decision making, High-level action selection, Arm selection, Activity selection, Target selection, Secret action selection, Candidate action selection  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats action selection as the observable act of choosing one action, move, or arm from a set of available candidates, usually conditioned on the current state or context and sometimes on the goal, interaction history, or past feedback. Success is commonly phrased as selecting the optimal, most appropriate, most plausible, or highest-scoring option, and several definitions make the output explicit, for example by having the agent "output the next action" or choose exactly one listed option. A smaller line of work broadens it to decision-making tasks that require selecting valid actions, or even action sequences, to achieve goals in dynamic or uncertain environments.

**Variants.** Papers study this behavior across web agents, games, embodied environments, autonomous driving, robotics, and bandit settings. The most common alternate label is decision-making, while narrower variants include driving decision making, high-level action selection, arm selection, and candidate action selection. Other single-paper formulations specialize it to daily activities or to choosing targets in sequential and hidden-role games.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers operationalize it directly in the task: the model is asked to output the next action, choose exactly one option from a fixed menu of arms or robot actions, or pick the better action from candidate pairs. Some papers also describe look-ahead simulation, evaluation mechanisms, or reward-model scores as guides for the selection, and bandit formulations frame choices as maximizing cumulative reward.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior is taken to reflect. It is linked to 7 constructs, but the recorded relations mostly run in the other direction: reasoning, commonsense knowledge, exploration-exploitation tradeoff, and logical reasoning are each claimed to have a causal relationship to action selection, model selection ability is reported as related to it, and 2 other constructs are linked by additional causal claims. Separately, tool use and multiple-choice question answering are reported as related to action selection.

## Sources

**Action selection** (6 papers: [WebEvolver: Enhancing Web Agent Self-Improvement with Co-evolving World Model](https://aclanthology.org/2025.emnlp-main.454.pdf), [Policy Learning from Tutorial Books via Understanding, Rehearsing and Introspecting](https://proceedings.neurips.cc/paper_files/paper/2024/file/21cf8411ed825614e00006a1d9aab7e4-Paper-Conference.pdf), [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf), [GAMEBoT: Transparent Assessment of LLM Reasoning in Games](https://aclanthology.org/2025.acl-long.378.pdf), [World Modeling Makes a Better Planner: Dual Preference Optimization for Embodied Task Planning](https://aclanthology.org/2025.acl-long.1044.pdf), [EVOLvE: Evaluating and Optimizing LLMs For In-Context Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25b/nie25b.pdf))
> The process of choosing the optimal action from a set of candidates, often guided by a look-ahead or evaluation mechanism.

**Decision-making** (3 papers: [Mars: Situated Inductive Reasoning in an Open-World Environment](https://proceedings.neurips.cc/paper_files/paper/2024/file/1fb6d0b52f5e41b11392841a66dbfe7d-Paper-Datasets_and_Benchmarks_Track.pdf), [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf), [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf))
> Performing tasks that require selecting and executing specific actions in different contexts based on induced rules.

**Driving decision making** (1 paper: [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf))
> Selecting high-level driving actions or meta-actions from scene descriptions and prior experience.

**Autonomous decision making** (1 paper: [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf))
> The task of a system making choices and taking actions independently to achieve goals in a given environment.

**High-level action selection** (1 paper: [Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d6e85e88495104442af94c98e899659-Paper-Conference.pdf))
> Choosing discrete robot actions such as navigation, pickup, placement, opening, closing, cleaning, or toggling to advance the task.

**Arm selection** (1 paper: [Can large language models explore in-context?](https://proceedings.neurips.cc/paper_files/paper/2024/file/d951f73c521d069fefbb73396df01424-Paper-Conference.pdf))
> Choosing one action from a fixed set of bandit arms at each time step.

**Activity selection** (1 paper: [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf))
> The observable process of an agent choosing a single action to execute from a set of evaluated candidates based on which one best satisfies its intrinsic motivations.

**Target selection** (1 paper: [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf))
> Choosing which opponent to attack or target in a sequential elimination game.

**Secret action selection** (1 paper: [Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25h/xu25h.pdf))
> Choosing targets for elimination, investigation, or protection during the night phase, based on hidden role and private information.

**Candidate action selection** (1 paper: [Boosting Virtual Agent Learning and Reasoning: A Step-Wise, Multi-Dimensional, and Generalist Reward Model with Benchmark](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25b/miao25b.pdf))
> The process of choosing between two or more candidate actions at a given step based on reward model scoring.

## Relationships

### → Action selection
- **Reasoning** (construct): *causes*, 2 papers
  > In the Reasoning module, we utilize the experiences derived from the Memory module and the common-sense knowledge of the LLM to perform decision-making for the current traffic scenario. (Section 3.3)
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
  - [Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf)
- **Commonsense knowledge** (construct): *causes*, 1 paper
  > In the Reasoning module, we utilize the experiences derived from the Memory module and the common-sense knowledge of the LLM to perform decision-making for the current traffic scenario. (Section 3.3)
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
- **Scene understanding** (construct): *causes*, 1 paper
  > the scene understanding module in LeapAD is designed to selectively identify critical objects, simplifying the description of the surrounding environment and reducing the load on decision-making processes. (Section 3.2)
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **Logical reasoning** (construct): *causes*, 1 paper
  > The Analytic Process relies on logical reasoning, employing rational thinking to analyze complex situations and make safe driving decisions. (Section 3.3)
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **World modeling** (construct): *causes*, 1 paper
  > a World-model-augmented (WMA) web agent, which simulates the outcomes of its actions for better decision-making. (ABSTRACT)
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
- **Exploration-exploitation tradeoff** (construct): *causes*, 1 paper
  > “LLMs often struggle to balance exploration and exploitation, which hinders their ability to navigate extensive state spaces efficiently.”
  - [Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/837ff662214b04e7ea8c43f095fe0dd7-Paper-Conference.pdf)

### Associated with
- **Tool use** (behavioral indicator), 2 papers
  > “Actions involve selecting which tool to call and the input to that tool.”
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)
- **Model selection ability** (construct), 1 paper
  > RestoreAgent can provide the best decisions, including which image restoration tasks need to be performed, the order of their execution, and which model is most suitable for each task. (Section 3.2.1)
  - [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator), 1 paper
  > Large language models (LLMs) (Touvron et al., 2023; Databricks, 2024; Abdin et al., 2024) have demonstrated remarkable capabilities in various decision-making tasks, including multi-choice question answering and tool usage (Section 1)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)
