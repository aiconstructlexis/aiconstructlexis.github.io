# Sequential decision-making
**Type:** Construct  
**Supporting papers:** 11  
**Also known as:** Multi-step decision-making  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats it as a capability for selecting, sequencing, and executing actions over multiple steps to accomplish a task or goal. Most descriptions add temporal or interactive dependence, either that each action depends on previous outcomes or that the sequence is carried out with environmental feedback in an interactive setting. A smaller framing casts it as the task of training policies to make a series of choices over time to achieve a goal, shifting the emphasis from an ability to a policy-learning problem.

**Space of facets.** Papers use both "sequential decision-making" and "multi-step decision-making" for closely similar ideas centered on ordered action sequences over time. Some descriptions place it alongside planning and reasoning, for example by describing methods that integrate reasoning and acting to address sequential decision-making tasks, while another explicitly distinguishes sequential decision-making tasks from general problem-solving tasks. A more specific usage appears in evaluation language that refers to classical sequential decision-making environments with limited action space.

**Space of measurement.** Operationalization is concentrated in 3 linked measurement instruments, all benchmark or environment-style evaluations: ALFWorld is used most often, followed by ToolBench and VirtualHome. Papers describe ALFWorld as a benchmark or open-source environment for sequential decision-making scenarios, ToolBench as containing intricate multi-step decision tasks, and VirtualHome as a classical environment with limited action space. The construct is also linked to 3 behavioral indicators, most visibly web navigation and robotic manipulation, plus 1 other indicator. These operationalizations line up with definitions that emphasize multi-step action sequences, interaction, and environmental feedback.

**Links.** In the relationship evidence, more than one paper relates it to web navigation, treating web navigation as a sequential decision-making task that requires interaction with an environment. One paper relates robotic manipulation to it by describing such tasks as requiring complex sequential decision-making. Another paper relates it to planning and reasoning, describing a planning method that integrates reasoning and acting to address sequential decision-making tasks. One paper also claims a causal relationship from strategy generation to sequential decision-making, based on reported gains for planning over direct response generation on benchmarks that include decision-making tasks. No correlational links are reported.

## Sources

**Sequential decision-making** (1 paper: [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf))
> The ability to perform a series of actions in an interactive environment where each action depends on the outcomes of previous ones.

**Multi-step decision-making** (1 paper: [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf))
> Selecting and sequencing actions over multiple steps to accomplish a task or instruction.

## Relationships

### Sequential decision-making →
- **ALFWorld** (measurement instrument): *measured_by*, 2 papers
  > We use one benchmark to evaluate the performance in sequential decision-making scenarios: ALFWorld (Shridhar et al., 2020) (Section 3.4)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **VirtualHome** (measurement instrument): *measured_by*, 1 paper
  > We first evaluate our method on two classical sequential decision-making environments with limited action space: Overcooked [5] and VirtualHome [5]
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **ToolBench** (measurement instrument): *measured_by*, 1 paper
  > conduct extensive experiments on Game of 24 (Yao et al., 2023), WebShop (Yao et al., 2022a), ToolBench (Qin et al., 2023c) and RestBench (Song et al., 2023), which contains intricate multi-step decision tasks involving diverse scenarios.
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)

### → Sequential decision-making
- **Strategy generation** (behavioral indicator): *causes*, 1 paper
  > CODEPLAN consistently and significantly outperforms directly generating responses without planning, yielding a relative 25.1% performance gain averaged across 13 challenging reasoning benchmarks spanning mathematical reasoning, symbolic reasoning, instruction-following, multi-hop question answering, and decision-making tasks.
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)

### Associated with
- **Web navigation** (behavioral indicator), 2 papers
  > Large language model (LLM) agents have been applied to sequential decision-making tasks such as web navigation, but without any environment-specific experiences, they often fail in these complex tasks.
  - [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694.pdf)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **Planning** (construct), 1 paper
  > ReAct [23]: This LLM-based planning method integrates reasoning and acting to address sequential decision-making tasks. (Section 4.1.2)
  - [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf)
- **Reasoning** (construct), 1 paper
  > ReAct [23]: This LLM-based planning method integrates reasoning and acting to address sequential decision-making tasks. (Section 4.1.2)
  - [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf)
- **Robotic manipulation** (behavioral indicator), 1 paper
  > Many of these tasks, such as natural language dialogue or robotic control, require complex sequential decision-making. (Section 1)
  - [Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9531a3e64e6167c7e1e671157082682-Paper-Conference.pdf)
