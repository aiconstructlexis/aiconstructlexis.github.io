# Self-improvement
**Type:** Construct  
**Supporting papers:** 29  
**Also known as:** Self-evolution, Continuous improvement, Self-improvement capability, Policy improvement, Learning from mistakes, Iterative self-improvement, In-context improvement, Test-time learning, Self-transfer learning, Recursive self-improvement, Self-modification  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing treats self-improvement as a latent ability or capacity of a model or agent to improve its own performance, outputs, or reasoning over time through iterative refinement. Most definitions tie it to analyzing and correcting flaws, reflecting on past attempts, learning from experience or feedback, or generating, verifying, and training on self-produced data, often without human intervention, external process supervision, or stronger teacher models. A smaller line of work narrows the term to in-context or test-time improvement without parameter updates, while other papers frame it as policy improvement or as recursive self-improvement through code modification. Definitions also differ on whether the term names a latent capability or an observable multi-round process of repeated generation, verification, and fine-tuning.

**Space of facets.** Papers use a broad family of near-neighbor labels for this construct, including self-evolution, continuous improvement, learning from mistakes, iterative self-improvement, in-context improvement, test-time learning, self-transfer learning, recursive self-improvement, and self-modification. The shared thread is iterative enhancement from a model's own outputs, experiences, or interactions, but the scope varies: some versions focus on critique, reflection, and correcting flawed rationales, some on improving a policy to achieve higher cumulative rewards, and some on dynamically altering code and operational logic. One paper also describes self-improvement as a mechanism spanning pre-training, post-training, and test-time inference.

**Space of measurement.** Papers link self-improvement to 1 measurement instrument and 4 behavioral indicators. The only named instrument is AIME 2025, presented as a mathematics benchmark for examining test-time learning on high-level mathematical problems. Outside that benchmark, operationalizations repeatedly take the form of iterative procedures, such as generating multiple reasoning paths or outputs, filtering or verifying them, fine-tuning on successful trajectories or verified data, replaying past experience in context, or reflecting on negative solutions; the linked behavioral indicators are code generation, instruction following, self-correction, and self-reflection. These operationalizations mostly match definitions centered on recursive refinement and learning from feedback, while some broader definitions, such as policy improvement or code self-modification, extend beyond the only explicit instrument.

**Links.** Papers most often connect self-improvement to generalization, reasoning, complex reasoning, critique ability, and generation diversity. Several papers claim causal relationships from critique ability and other constructs to self-improvement, while other papers claim causal relationships from self-improvement to generalization, reasoning, complex reasoning, generation diversity, and other abilities; for generalization specifically, the record is mixed, with one paper making a causal claim and another reporting only a related link. Additional papers report related links with other constructs and with the linked behavioral indicators.

## Sources

**Self-evolution** (1 paper: [AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf))
> The ability of a model to autonomously improve its capabilities and reinforce its knowledge utilization through iterative self-generated training, without external process supervision.

**Self-improvement** (8 papers: [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf), [Self-Improving Robust Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bc795afae289ed465a65a3b4b1f4eb7-Paper-Conference.pdf), [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf), [Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning](https://aclanthology.org/2025.naacl-long.519.pdf), [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf), [Training Software Engineering Agents and Verifiers with SWE-Gym](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25g/pan25g.pdf), [SAMULE: Self-Learning Agents Enhanced by Multi-level Reflection](https://aclanthology.org/2025.emnlp-main.839.pdf), [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694.pdf))
> The latent capacity of a model to effectively analyze and correct flaws in its own or others' responses, facilitated by critique ability.

**Continuous improvement** (1 paper: [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability of an LLM agent to enhance its performance on a task over time by learning from a continuous sequence of inputs and feedback.

**Self-improvement capability** (1 paper: [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf))
> The latent ability of a large language model to improve its performance by generating outputs, verifying them, and then updating itself based on the verified data.

**Policy improvement** (2 papers: [Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c4a7643ab90cd62320df95c873a1c6f-Paper-Conference.pdf), [In-Context Reinforcement Learning From Suboptimal Historical Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25d/dong25d.pdf))
> The latent process of refining a strategy or policy in-context to maximize cumulative rewards based on new information discovered through interaction.

**Learning from mistakes** (1 paper: [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf))
> The model's capacity to improve its reasoning by analyzing and correcting flawed rationales, treating errors as opportunities for self-improvement.

**Iterative self-improvement** (1 paper: [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf))
> The observable, multi-round process where a model repeatedly generates data, verifies it, and fine-tunes on the filtered results, leading to changes in its performance and output distribution over time.

**In-context improvement** (1 paper: [Eureka: Human-Level Reward Design via Coding Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf))
> The ability of the LLM to refine and enhance previously generated outputs based on feedback or reflection provided within the context window, enabling iterative optimization without parameter updates.

**Test-time learning** (1 paper: [How Far Can LLMs Improve from Experience? Measuring Test-Time Learning Ability in LLMs with Human Comparison](https://aclanthology.org/2025.emnlp-main.1304.pdf))
> The latent ability of a model to improve its performance through interaction, feedback, and reflection during test time by discovering and applying generalizable strategies beyond memorization.

**Self-transfer learning** (1 paper: [Can RLHF be More Efficient with Imperfect Reward Models? A Policy Coverage Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25o/huang25o.pdf))
> The latent ability of a learning system to improve future policy updates by distilling knowledge from its own past online interactions, forming a self-improving loop.

**Recursive self-improvement** (1 paper: [Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement](https://aclanthology.org/2025.acl-long.1354.pdf))
> The latent ability of an agent to iteratively enhance its own policy and learning algorithm by modifying its code, leading to progressively better performance over time.

**Self-modification** (1 paper: [Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement](https://aclanthology.org/2025.acl-long.1354.pdf))
> The agent's ability to dynamically alter its own code and operational logic during execution based on its reasoning and environmental feedback.

## Relationships

### Self-improvement →
- **Generalization** (construct): *causes*, 2 papers
  > efﬁcient exploration to discover better strategies and solutions autonomously, i.e., self-improving, which can allow agents to generalize across the various tasks in the digital world.
  - [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > These results consistently demonstrate RISE’s effectiveness in enhancing reasoning capabilities for different models. (Section 1)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > imbue an LLM with the capability to recursively detect and correct its previous mistakes in subsequent iterations.
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *causes*, 1 paper
  > our AlphaMath enhances Llama3’s mathematical reasoning capabilities without any annotations, yielding an average improvement of +20 points. (Section 4.6)
  - [AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf)
- **Problem-solving ability** (construct): *causes*, 1 paper
  > Self-improvement through post-training methods such as iterative preference learning has been acclaimed for enhancing the problem-solving capabilities (e.g., mathematical reasoning) of Large Language Models (LLMs) without human intervention. (ABSTRACT)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Generation diversity** (construct): *causes*, 1 paper
  > The evaluation results highlight a critical trade-off in iterative self-improvement: while aiming for higher accuracy, the diversity of outputs, which can be crucial for creativity and robustness in problem-solving, is compromised. (Section 5.2)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **AIME 2025** (measurement instrument): *measured_by*, 1 paper
  > We leverage this most recent mathematics benchmark to examine the test-time learning capabilities of large language models in solving high-level mathematical problems. (Section 3.1)
  - [How Far Can LLMs Improve from Experience? Measuring Test-Time Learning Ability in LLMs with Human Comparison](https://aclanthology.org/2025.emnlp-main.1304.pdf)
- **Complex reasoning** (construct): *causes*, 1 paper
  > an adaptive self-improvement agentic system that enables LLMs to perform such complex reasoning under limited data by iteratively improving their capability through self-generated experience. (Abstract)
  - [Adaptive Self-improvement LLM Agentic System for ML Library Development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25at/zhang25at.pdf)

### → Self-improvement
- **Critique ability** (construct): *causes*, 1 paper
  > Critique ability is crucial for the self-improvement [1, 2] of LLMs, as it enables the effective analysis and correction of flaws in responses [3, 4]. (Introduction)
  - [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **Memory management** (construct): *causes*, 1 paper
  > A robust memory system is a critical component of learning and improvement. The AI agent must be able to recall and integrate information from past negotiations and actions to inform its current and future decision-making processes. This endows the agent with the ability to evolve. (Section 1).
  - [Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy](https://proceedings.neurips.cc/paper_files/paper/2024/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > We believe this result indicates that self-improvement requires a minimal level of instruction following and reasoning capabilities, which is not present in these small models. (Section 4.1)
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **Planning** (construct): *causes*, 1 paper
  > These findings suggest that the model’s inherent reasoning and planning capabilities developed during pre-training are crucial for general self-improvement. (Section 4.4)
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > We believe this result indicates that self-improvement requires a minimal level of instruction following and reasoning capabilities, which is not present in these small models. (Section 4.1)
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **Instruction following ability** (construct): *causes*, 1 paper
  > for SLMs, their weaker instruction-following ability and unreliable self-rewarding can mislead self-improvement.
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > Reflection on self-generated CoT facilitates learning from mistakes. (Section 5.1)
  - [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf)
- **Self-awareness** (construct): *causes*, 1 paper
  > By introspecting these elements, the agent gains an understanding of its own operational state and can adapt accordingly.
  - [Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement](https://aclanthology.org/2025.acl-long.1354.pdf)
- **Metacognition** (construct): *causes*, 1 paper
  > We argue that sustainable, generalized self-improvement requires agents to develop intrinsic metacognitive learning abilities. (Section 1)
  - [Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cw/liu25cw.pdf)

### Associated with
- **Code generation** (behavioral indicator), 1 paper
  > Zelikman et al. (2023) applied recursive self-improvement to code generation, where the target of improvement was the optimizer itself.
  - [Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement](https://aclanthology.org/2025.acl-long.1354.pdf)
- **Stability** (construct), 1 paper
  > We conducted further analysis to investigate the improvements of CER with various metrics, such as cross-template success rate, stability (preservation of old knowledge), and plasticity (acquisition of new knowledge) (Grossberg, 1982; Rolnick et al., 2019) (§5.2, §5.3), demonstrating its generalizability and effectiveness as a self-improvement system.
  - [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694.pdf)
- **Plasticity** (construct), 1 paper
  > We conducted further analysis to investigate the improvements of CER with various metrics, such as cross-template success rate, stability (preservation of old knowledge), and plasticity (acquisition of new knowledge) (Grossberg, 1982; Rolnick et al., 2019) (§5.2, §5.3), demonstrating its generalizability and effectiveness as a self-improvement system.
  - [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694.pdf)
