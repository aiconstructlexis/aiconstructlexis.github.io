# ScienceWorld
**Type:** Measurement instrument  
**Supporting papers:** 15  
**Also known as:** SciWorld  

## State of the Field

**What it is.** Across papers, the prevailing description is a text-based or textual simulation benchmark, or interactive environment, for basic or elementary science experiments. Definitions repeatedly say agents receive natural-language goals and must interact with objects by navigating, manipulating objects, and observing outcomes; several papers also frame it as an embodied or embodied-AI setting for long-horizon, large-action-space tasks. A smaller line of work emphasizes the abilities it requires, describing it as involving long-term memory, subtask decomposition, and scientific and commonsense knowledge, and one paper uses the surface form SciWorld for science-oriented interactive tasks.

**What it is claimed to measure.** Papers use ScienceWorld to measure 3 constructs and 2 behavioral indicators. The most recurrent construct framing is generalization, including evaluation on unseen tasks; a smaller set of papers uses it to measure commonsense knowledge and task decomposition ability. It is also reported as measuring embodied planning and scientific experimentation, so papers attach it to several distinct capabilities rather than only one.

**Space of uses.** Papers commonly use ScienceWorld alongside ALFWorld, and one paper also positions it with VirtualHome for embodied planning tasks. They usually treat it as a representative interactive or embodied evaluation environment, reporting average scores on it, using it for unseen-task evaluation, or evaluating scientific tasks within it; one paper using the name SciWorld places it among benchmarks covering web, embodied, tool use and game scenarios. Papers do not link it to other measurement instruments.

## Sources

**ScienceWorld** (6 papers: [Policy Improvement using Language Feedback Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4d4f7cf206bb00f9a38a5b6ae92cf79a-Paper-Conference.pdf), [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf), [SELFGOAL: Your Language Agents Already Know How to Achieve High-level Goals](https://aclanthology.org/2025.naacl-long.36.pdf), [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf), [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf), [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf))
> A textual simulation benchmark for basic science experiments used to evaluate instruction following in long-horizon, large-action-space settings.

**SciWorld** (1 paper: [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf))
> A benchmark for evaluating LLM agents on science-oriented interactive tasks.

## Relationships

### → ScienceWorld
- **Generalization** (construct): *measured_by*, 2 papers
  > AlFWorld and ScienceWorld include unseen tasks to evaluate the agent’s generalization ability. (Section 4.1)
  - [Agent Planning with World Knowledge Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf)
  - [Divide and Conquer: Grounding LLMs as Efficient Decision-Making Agents via Offline Hierarchical Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25q/hu25q.pdf)
- **Embodied planning** (behavioral indicator): *measured_by*, 1 paper
  > for embodied planning tasks in ScienceWorld and VirtualHome, a successful multi-step plan requires single-step optimality in each planning step.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
- **Scientific experimentation** (behavioral indicator): *measured_by*, 1 paper
  > ScienceWorld (Wang et al., 2022a) is an interactive benchmark designed for embodied science experiments. (Section 4.1)
  - [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf)
- **Task decomposition ability** (construct): *measured_by*, 1 paper
  > We choose ScienceWorld (Wang et al., 2022), a complex interactive environment requiring skills in long-term memory, sub-task decomposition, and scientific and commonsense knowledge. (Section 4.2)
  - [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf)
- **Commonsense knowledge** (construct): *measured_by*, 1 paper
  > We choose ScienceWorld (Wang et al., 2022), a complex interactive environment requiring skills in long-term memory, sub-task decomposition, and scientific and commonsense knowledge. (Section 4.2)
  - [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf)
