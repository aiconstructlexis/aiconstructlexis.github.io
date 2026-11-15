# VirtualHome
**Type:** Measurement instrument  
**Supporting papers:** 16  

## State of the Field

**What it is.** Across papers, VirtualHome is most commonly described as a simulated or 3D household environment, variously framed as a simulator, simulation platform, or benchmark for household activities, household task execution, and programs for those activities. The prevailing usage is to test whether generated plans or programs are executable in complex, multi-step tasks with object interactions and goal conditions, and some descriptions add partially observable states and macro-actions. A smaller line of description emphasizes long-horizon and multi-agent tasks with procedural generation, and one paper uses it as one component of ExtendaBench, where the VirtualHome portion contains 605 tasks divided into ultra-short, short, medium, and long subsets.

**What it is claimed to measure.** Papers use VirtualHome to measure 4 constructs and 2 behavioral indicators. Among constructs, it is linked most often to Generalization, including unseen-task and crossover tests across Food Preparation and Entertainment, followed by Cross-domain generalization, Robustness, and Sequential decision-making; among behavioral indicators, it is used for Embodied planning and Task completion. Overall, the reported measurement claims are spread across several targets rather than centered on a single construct.

**Space of uses.** Most papers position VirtualHome as a main evaluation environment for embodied agents, using it to demonstrate planning, re-planning, decision-making, continual instruction following, policy optimization, and test-time adaptation in household settings. Papers often use it alongside other benchmarks such as ALFWorld, BEHAVIOR, Habitat 2.0, ALFRED, and CARLA, and some place it inside broader benchmark suites or extensions rather than using it alone.

**Concerns raised.** Only a small amount of explicit criticism appears: one paper says that although VirtualHome offers long-horizon and multi-agent tasks with procedural generation, it lacks time delays. Another paper describes work in VirtualHome as operating under hard executability conditions, where generated plans are assessed by whether they translate into executable household action programs.

## Sources

**VirtualHome** (10 papers: [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf), [PlaSma: Procedural Knowledge Models for Language-based Planning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2024/file/16bce4070c4e23434451b180348e3814-Paper-Conference.pdf), [Tree-Planner: Efficient Close-loop Task Planning with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d53538ba21c05fa361d2b21704172753-Paper-Conference.pdf), [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf), [Robotouille: An Asynchronous Planning Benchmark for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d033407a1a4b7a75cd5f9e4575ad9fb5-Paper-Conference.pdf), [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf), [Structured Preference Optimization for Vision-Language Long-Horizon Task Planning](https://aclanthology.org/2025.emnlp-main.884.pdf), [Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/b631da756d1573c24c9ba9c702fde5a9-Paper-Datasets_and_Benchmarks_Track.pdf), [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf), [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf))
> VirtualHome is an embodied environment benchmark used to evaluate whether generated plans translate into executable household action programs.

## Relationships

### → VirtualHome
- **Generalization** (construct): *measured_by*, 1 paper
  > Table 1: Comparison of generalization performance on eight unseen tasks, with episodic returns averaged over 100 episodes. In these tasks, we replace the pancake in the original Food Preparation task with other foods like cheese, hamburger, apple pie and pizza
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Sequential decision-making** (construct): *measured_by*, 1 paper
  > We first evaluate our method on two classical sequential decision-making environments with limited action space: Overcooked [5] and VirtualHome [5]
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > Finally, we demonstrate superior performance and robustness of ExRAP via intensive experiments with home robots and autonomous driving scenarios in VirtualHome, ALFRED, and CARLA. (Introduction)
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **Embodied planning** (behavioral indicator): *measured_by*, 1 paper
  > for embodied planning tasks in ScienceWorld and VirtualHome, a successful multi-step plan requires single-step optimality in each planning step.
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)
- **Cross-domain generalization** (construct): *measured_by*, 1 paper
  > We evaluate our WorMI on the VirtualHome and ALFWorld benchmarks, demonstrating superior zero-shot and few-shot performance compared to several LLM-based approaches across a range of unseen domains. These results highlight the framework’s potential for scalable, real-world deployment in embodied agent scenarios where adaptability and data efficiency are essential. (Abstract).
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
- **Task completion** (behavioral indicator): *measured_by*, 1 paper
  > "We evaluate our approach in two embodied environments: VirtualHome (Puig et al., 2018), a 3D simulation environment for household task execution"
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
