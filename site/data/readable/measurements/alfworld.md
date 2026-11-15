# ALFWorld
**Type:** Measurement instrument  
**Supporting papers:** 47  
**Also known as:** AlfWorld, Alfworld  

## State of the Field

**What it is.** Across the papers, ALFWorld is most commonly described as a text-based or text-only household environment for embodied agents, variously called a game suite, benchmark, simulator, or dataset. The prevailing description is that agents follow natural language instructions and act through high-level or low-level text actions to complete housework tasks such as navigation, object manipulation, picking, cleaning, heating, or moving objects; several papers also say it is based on, or aligned with, ALFRED and implemented in TextWorld. A smaller line of work emphasizes logs or next-action prediction rather than online interaction, describing navigation logs from a text-based world simulator. Papers also describe it as having six task types and 134 unseen environments or evaluation tasks.

**What it is claimed to measure.** Papers use it to measure 8 constructs and 2 behavioral indicators, so its claimed targets are spread across several framings rather than concentrated on a single one. The prevailing use is for decision-making, followed by generalization and sequential decision-making; among behavioral indicators, task completion and embodied planning are the linked uses. In the papers, these uses are phrased as testing models' decision-making ability, evaluating generalization on unseen tasks, and assessing performance in embodied or sequential scenarios.

**Space of uses.** No measurement instrument is linked to it. Papers more often position it as the embodied or decision-making benchmark within broader evaluation suites, often alongside WebShop, HotPotQA, PDDL, TextCraft, and ScienceWorld. Some descriptions explicitly group it under labels such as embodied, embodied decision, or high-level decision-making, and one paper uses GPT-3.5-Turbo to evaluate task trajectories on it.

**Concerns raised.** One paper highlights a concern specific to some tasks: Clean, Heat, and Cool are described as having irreversible effects, which makes them a setting for evaluating misaligned actions in physical task execution.

## Sources

**AlfWorld** (3 papers: [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf), [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf), [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf))
> An embodied task benchmark based on the ALFRED dataset, where an agent must follow high-level language instructions to complete household tasks in a simulated environment using low-level text actions.

**ALFWorld** (9 papers: [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a0d3ae989a382ce6e50312bc35bf7e1-Paper-Conference.pdf), [THOUGHT PROPAGATION: AN ANALOGICAL APPROACH TO COMPLEX REASONING WITH LARGE LANGUAGE MODELS](https://proceedings.iclr.cc/paper_files/paper/2024/file/2dae7d1ccf1edf76f8ce7c282bdf4730-Paper-Conference.pdf), [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf), [THREAD: Thinking Deeper with Recursive Spawning](https://aclanthology.org/2025.naacl-long.427.pdf), [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf), [Agentic Knowledgeable Self-awareness](https://aclanthology.org/2025.acl-long.619.pdf), [Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf), [Preemptive Detection and Correction of Misaligned Actions in LLM Agents](https://aclanthology.org/2025.emnlp-main.12.pdf))
> A text-based game suite of interactive housework environments used to evaluate LLM-agent planning and task completion.

**Alfworld** (2 papers: [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf), [Latent Factor Models Meets Instructions: Goal-conditioned Latent Factor Discovery without Task Supervision](https://aclanthology.org/2025.naacl-long.554.pdf))
> Alfworld is an interactive agent benchmark used to evaluate task completion in household-style environments.

## Relationships

### → ALFWorld
- **Decision-making** (construct): *measured_by*, 4 papers
  > We select 5 tasks: SciWorld (Wang et al., 2022), Alfworld (Shridhar et al., 2020), BabyAI (Chevalier-Boisvert et al., 2018), PDDL (Vallati et al., 2015), and Jericho (Hausknecht et al., 2020), all of them are testing models’ decision-making ability. (Section 4.1)
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
  - [Efficient Reinforcement Learning with Large Language Model Priors](https://proceedings.iclr.cc/paper_files/paper/2025/file/797be96e4481c3fe5d675c1ba5352969-Paper-Conference.pdf)
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
  - [Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25n/feng25n.pdf)
- **Generalization** (construct): *measured_by*, 3 papers
  > AlFWorld and ScienceWorld include unseen tasks to evaluate the agent’s generalization ability. (Section 4.1)
  - [Agent Planning with World Knowledge Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf)
  - [Efficient Reinforcement Learning with Large Language Model Priors](https://proceedings.iclr.cc/paper_files/paper/2025/file/797be96e4481c3fe5d675c1ba5352969-Paper-Conference.pdf)
  - [Divide and Conquer: Grounding LLMs as Efficient Decision-Making Agents via Offline Hierarchical Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25q/hu25q.pdf)
- **Task completion** (behavioral indicator): *measured_by*, 2 papers
  > Given only one simple demonstration, AutoManual signiﬁcantly improves task success rates, achieving 97.4% with GPT-4-turbo and 86.2% with GPT-3.5-turbo on ALFWorld benchmark tasks. (Abstract)
  - [AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0142921fad7ef9192bd87229cdafa9d4-Paper-Conference.pdf)
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
- **Sequential decision-making** (construct): *measured_by*, 2 papers
  > We use one benchmark to evaluate the performance in sequential decision-making scenarios: ALFWorld (Shridhar et al., 2020) (Section 3.4)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **Embodied planning** (behavioral indicator): *measured_by*, 1 paper
  > “We conduct experiments on three representative agent tasks: Complex Reasoning (HotpotQA (Yang et al., 2018)), Embodied Decision (ALFWorld (Shridhar et al., 2020)), and Interactive Programming (InterCode (Yang et al., 2023))”
  - [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf)
- **Cross-domain generalization** (construct): *measured_by*, 1 paper
  > We evaluate our WorMI on the VirtualHome and ALFWorld benchmarks, demonstrating superior zero-shot and few-shot performance compared to several LLM-based approaches across a range of unseen domains. These results highlight the framework’s potential for scalable, real-world deployment in embodied agent scenarios where adaptability and data efficiency are essential. (Abstract).
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
- **Commonsense knowledge** (construct): *measured_by*, 1 paper
  > "The main challenge of this benchmark is to locate the target object and fulfill household work with commonsense knowledge of LLMs."
  - [Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf)
- **Natural language understanding** (construct): *measured_by*, 1 paper
  > ALFWorld (Shridhar et al., 2020) provides a text-based household task environment that for natural language understanding and embodied reasoning. (Section 5.1)
  - [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf)
- **Embodied reasoning** (construct): *measured_by*, 1 paper
  > ALFWorld (Shridhar et al., 2020) provides a text-based household task environment that for natural language understanding and embodied reasoning. (Section 5.1)
  - [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf)
- **Physical world understanding** (construct): *measured_by*, 1 paper
  > results from the ALFWorld environment demonstrate the impact of process rewards on physical reasoning (Section 4.2).
  - [AgentPro: Enhancing LLM Agents with Automated Process Supervision](https://aclanthology.org/2025.emnlp-main.506.pdf)
