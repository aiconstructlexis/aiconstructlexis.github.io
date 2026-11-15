# Agency
**Type:** Construct  
**Supporting papers:** 15  
**Also known as:** Agentic ability, Agentic capabilities, Agentic capability, Autonomy, Agent-oriented abilities, Model autonomy, Goal-directed behavior, Agentic abilities, Real-world application  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats agency as a capacity for autonomous, purposeful action in an environment, usually over multiple steps or turns and often tied to planning, decision-making, and task completion. Definitions commonly describe acting without human intervention or external control, and one formulation explicitly equates agency with strategic decision-making through action selection that leads to different outcomes. Smaller lines of work narrow the construct to particular settings, such as operating systems and GUI interaction, software engineering environments, or practical deployment, while others frame it as goal-directed behavior sustained across turns rather than responses driven by immediate context or imitation.

**Space of facets.** In practice, papers break the construct into recurring subfunctions such as planning, acting in environments, tool use, long-context understanding, and real-world application. One line of work explicitly decomposes agentic capabilities into workflow, tool use or function call, long-context understanding, and real-world application, while other papers use neighboring labels such as autonomy, model autonomy, agent-oriented abilities, and goal-directed behavior for overlapping aspects. The terminology is therefore not fully uniform: some authors use it for a general-purpose agent capacity across diverse environments, whereas others use nearby terms for narrower facets such as tool selection or independent decision-making.

**Space of measurement.** Papers link agency to 5 measurement instruments, all task benchmarks or testbeds: AgentBench, AgentBoard, AndroidControl, GUI-Odyssey, and OSWorld. These instruments operationalize agency through diverse agent tasks, including standardized collections for evaluating LMs' agentic capabilities, mobile agent benchmarks, and a challenging OS agent testbed. Papers also link it to 1 behavioral indicator, but that link is used as an antecedent of agency rather than as a direct measure, so operationalization is mostly benchmark performance in interactive environments.

**Links.** Among the 4 linked constructs, coding ability and consistency are reported as related to agency. One paper ties coding ability to agency by stating that programming capabilities measured by HumanEval receive weight in defining agentic capabilities, and another relates agency to consistency by describing tasks with heavy reasoning or agentic demands as settings where models can occasionally achieve exceptional results while average performance falls short of demonstrated potential. Separately, papers claim causal relationships from grounding and world modeling to agency, and from Self-reflection to agency, describing emergent agentic abilities as strongly dependent on those abilities.

## Sources

**Agentic capability** (2 papers: [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf), [Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zainullina25a/zainullina25a.pdf))
> The general capacity to autonomously interact with operating systems and complete multi-step tasks through GUI interactions, encompassing planning, action execution, and environment response handling.

**Agentic ability** (1 paper: [VideoWebArena: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf))
> The latent capacity of a model to act autonomously to accomplish tasks within an environment.

**Agentic capabilities** (2 papers: [BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0b1515be276f6ba82b4f2b25e50bef0-Paper-Conference.pdf), [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf))
> The ability of a model to act autonomously and purposefully to achieve complex goals in an environment.

**Autonomy** (2 papers: [BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b2fa23e4ef0f7ac6c4f01d7998e6237-Paper-Conference.pdf), [PaperBench: Evaluating AI’s Ability to Replicate AI Research](https://raw.githubusercontent.com/mlresearch/v267/main/assets/starace25a/starace25a.pdf))
> The capacity of an embodied agent to make informed, independent decisions without external control.

**Agent-oriented abilities** (1 paper: [DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf))
> The latent capacity to perform agent-like functions such as selecting tools or acting in tool-using workflows.

**Agency** (1 paper: [Moral Alignment for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2b1bad4756ceee8f408e16b8e6e4383-Paper-Conference.pdf))
> The capacity of a system to make strategic decisions by selecting actions in an environment that lead to different outcomes.

**Model autonomy** (1 paper: [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/7e3767db483c942b883eb4f8cfb74e31-Paper-Conference.pdf))
> The capability of an AI agent to operate and solve complex, multi-step problems without human intervention.

**Goal-directed behavior** (1 paper: [LMRL Gym: Benchmarks for Multi-Turn Reinforcement Learning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abdulhai25a/abdulhai25a.pdf))
> The latent tendency of an agent to pursue a specific objective over multiple interaction turns, rather than generating responses based on immediate context or imitation.

**Agentic abilities** (1 paper: [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf))
> The latent capacity of an LLM to function as a general-purpose agent across diverse environments by perceiving, planning, and acting over multiple turns.

**Real-world application** (1 paper: [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf))
> The latent ability to operate effectively in practical deployment scenarios requiring coordination of multiple capabilities such as tool use, planning, and environmental interaction.

## Relationships

### Agency →
- **AgentBoard** (measurement instrument): *measured_by*, 1 paper
  > We tested on two standardized agent evaluation benchmarks, AgentBench [57] and Agent-Board [61], each is a collection of diverse tasks for evaluating LMs’ agentic capabilities. (Sec. 4.2)
  - [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **AgentBench** (measurement instrument): *measured_by*, 1 paper
  > We tested on two standardized agent evaluation benchmarks, AgentBench [57] and Agent-Board [61], each is a collection of diverse tasks for evaluating LMs’ agentic capabilities. (Sec. 4.2)
  - [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **OSWorld** (measurement instrument): *measured_by*, 1 paper
  > In this study, we benchmark our approach on the challenging OS agent testbed, OSWorld (Xie et al., 2024). (Section 4.3)
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
- **AndroidControl** (measurement instrument): *measured_by*, 1 paper
  > “We examine five distinct agent benchmarks across three different platforms: AndroidControl (Li et al., 2024) and GUI-Odyssey (Lu et al., 2024a) for mobile agents”
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
- **GUI-Odyssey** (measurement instrument): *measured_by*, 1 paper
  > “We examine five distinct agent benchmarks across three different platforms: AndroidControl (Li et al., 2024) and GUI-Odyssey (Lu et al., 2024a) for mobile agents”
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)

### → Agency
- **Grounding** (construct): *causes*, 1 paper
  > Emergent agentic abilities are strongly dependent on basic abilities like grounding, world modeling, and self-reflection.
  - [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)
- **World modeling** (construct): *causes*, 1 paper
  > Emergent agentic abilities are strongly dependent on basic abilities like grounding, world modeling, and self-reflection.
  - [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > Emergent agentic abilities are strongly dependent on basic abilities like grounding, world modeling, and self-reflection.
  - [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Coding ability** (construct), 1 paper
  > We observe that the ﬁtted weights assign signiﬁcant importance to programming capabilities (HumanEval) on both benchmarks, underscoring its signiﬁcance in deﬁning the agentic capabilities of LMs. (Sec. 4.2)
  - [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **Consistency** (construct), 1 paper
  > when it comes to tasks requiring heavy reasoning or agentic capabilities, a major challenge persists: while the models occasionally achieve exceptional results, their average performance often falls short of their demonstrated potential. (Section 1)
  - [Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zainullina25a/zainullina25a.pdf)
