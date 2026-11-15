# Task completion
**Type:** Behavioral indicator  
**Supporting papers:** 21  
**Also known as:** Household task execution, Indoor task simulation, Graph-structured task execution, Embodied task solving, Household activity completion, Task execution, Open-ended task solving, Task success, Passing unit tests, Completing subjective everyday tasks  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats task completion as reaching the intended end state or user goal of a task, usually under task-specific evaluation criteria. Definitions commonly ask whether "the goal of each task is accomplished", sometimes with a binary "success flag (0/1)", and other papers describe it as fulfilling user requests through sequences of actions, tool calls, or UI interactions. Smaller usages narrow it to accepted predicted task execution, dialogue-game success, satisfaction of specified goal predicates, finishing baseline items in a study procedure, or generated code passing all predefined tests.

**Variants.** Papers study task completion across several settings. A common cluster is embodied and simulated work: household task execution, indoor task simulation through language interaction, household activities defined by predicates with specific counts, and open-ended embodied tasks specified by text or video. Other variants focus on graph-structured tasks with dependencies, branches, and hierarchical levels, web or application tasks translated from natural-language requests into actions, tool-use tasks with real-world API calls, and smaller lines of work on dialogue games and code generation judged by unit or case tests.

**Space of elicitation and scores.** Papers link task completion to 6 measurement instruments. The named instruments include ALFWorld, AitW, Minecraft, MiniWoB++, and VirtualHome, plus one other instrument used for practical web interactions; together they cover text-based indoor simulation, device-control evaluation, more complex embodied environments, and household-task simulation. When papers describe scoring directly, they most often use task-specific evaluation scripts or success rates, including a binary success flag, while some variants use accuracy on graph-structured tasks, quality score in valid dialogue attempts, unit-test pass rates, or time to completion.

**What it is taken as evidence of.** Papers do not converge on a single construct that task completion reflects. Instead, it is linked to 3 constructs: Ambiguity and Context retention are each claimed, in separate papers, to have causal relationships to task completion, while Error recovery is reported as related to it. The recorded claims are task-specific, arguing that ambiguity reduction should lead to improved code accuracy, that losing context leads to incomplete task execution in long multi-step tasks, and that recovering from difficult states accompanies completion of complex instructions.

## Sources

**Task completion** (5 papers: [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/file/c2f71567cd53464161cab3336e8fc865-Paper-Datasets_and_Benchmarks_Track.pdf), [Position: Human Baselines in Model Evaluations Need Rigor and Transparency (With Recommendations & Reporting Checklist)](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25s/wei25s.pdf), [ToolGen: Unified Tool Retrieval and Calling via Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b646bdebeb87dfafe2c6f77a63b564e1-Paper-Conference.pdf), [IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents](https://aclanthology.org/2025.emnlp-main.53.pdf), [AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](https://aclanthology.org/2025.acl-long.381.pdf))
> Successfully reaching the intended end state of a benchmark task as judged by task-specific evaluation scripts.

**Household task execution** (1 paper: [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf))
> Performing a variety of common tasks within a simulated home environment, such as moving objects or operating appliances.

**Indoor task simulation** (1 paper: [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf))
> Completing tasks within a simulated indoor setting, typically guided by text-based interactions and instructions.

**Graph-structured task execution** (1 paper: [What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf))
> Performing a sequence of actions on a task represented as a directed acyclic graph with dependencies, branches, and hierarchical levels.

**Embodied task solving** (1 paper: [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf))
> The observable task of interacting with a simulated physical environment to complete a goal, such as household chores or scientific experiments.

**Household activity completion** (1 paper: [CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf))
> The execution of common domestic tasks within a simulated environment, defined by the satisfaction of a set of specified goals or predicates.

**Task execution** (1 paper: [Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://proceedings.iclr.cc/paper_files/paper/2025/file/75c37811e830bf029584b1c6fac17726-Paper-Conference.pdf))
> Carrying out an accepted predicted task through interaction with tools and the environment.

**Open-ended task solving** (1 paper: [FOUNDER: Grounding Foundation Models in World Models for Open-Ended Embodied Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ee/wang25ee.pdf))
> The observable performance of an agent in accomplishing a wide range of tasks specified in human-intuitive formats like text or video, without task-specific rewards.

**Task success** (1 paper: [Playpen: An Environment for Exploring Learning From Dialogue Game Feedback](https://aclanthology.org/2025.emnlp-main.1517.pdf))
> Achieving the goal of a dialogue game, such as correctly guessing a target word or completing a collaborative objective.

**Passing unit tests** (1 paper: [ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.362.pdf))
> The observable outcome where generated code, when executed against a set of predefined test cases, produces the expected outputs for all cases.

## Relationships

### Task completion →
- **ALFWorld** (measurement instrument): *measured_by*, 2 papers
  > Given only one simple demonstration, AutoManual signiﬁcantly improves task success rates, achieving 97.4% with GPT-4-turbo and 86.2% with GPT-3.5-turbo on ALFWorld benchmark tasks. (Abstract)
  - [AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0142921fad7ef9192bd87229cdafa9d4-Paper-Conference.pdf)
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
- **WebArena** (measurement instrument): *measured_by*, 1 paper
  > This benchmark is particularly suitable for evaluating real-world task completion capabilities due to its focus on practical web interactions. (Section 3.1)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
- **MiniWoB++** (measurement instrument): *measured_by*, 1 paper
  > These manuals allow LLM agents to achieve remarkable success rates of 97.4% with GPT-4-turbo and 86.2% with GPT-3.5-turbo on ALFWorld, 98.3% with GPT-4-turbo and 92.7% with GPT-3.5-turbo on MiniWoB++. (Introduction)
  - [AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0142921fad7ef9192bd87229cdafa9d4-Paper-Conference.pdf)
- **AitW** (measurement instrument): *measured_by*, 1 paper
  > We demonstrate the effectiveness of DigiRL using the Android-in-the-Wild (AitW) dataset, where our 1.3B VLM trained with RL achieves a 49.5% absolute improvement – from 17.7 to 67.2% success rate
  - [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf)
- **VirtualHome** (measurement instrument): *measured_by*, 1 paper
  > "We evaluate our approach in two embodied environments: VirtualHome (Puig et al., 2018), a 3D simulation environment for household task execution"
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
- **Minecraft** (measurement instrument): *measured_by*, 1 paper
  > Finally, we extend FOUNDER to Minecraft, a more complex environments with challenging task instructions and more intricate observations (Section 5).
  - [FOUNDER: Grounding Foundation Models in World Models for Open-Ended Embodied Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ee/wang25ee.pdf)

### → Task completion
- **Ambiguity** (construct): *causes*, 1 paper
  > Based on our definition of ambiguity, we hypothesize that ambiguity reduction should lead to improved code accuracy. (Section 1)
  - [Identifying & Interactively Refining Ambiguous User Goals for Data Visualization Code Generation](https://aclanthology.org/2025.emnlp-main.1283.pdf)
- **Context retention** (construct): *causes*, 1 paper
  > Memory retention mechanisms can be improved as well, especially for handling long, multi-step tasks that span multiple apps. Current agents often lose context during complex tasks or app transitions, which leads to incomplete task execution.
  - [SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf)

### Associated with
- **Error recovery** (construct), 1 paper
  > “DigiRL is able to recover from such states and complete complex instruction as requested”
  - [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf)
