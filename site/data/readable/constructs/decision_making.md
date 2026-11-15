# Decision-making
**Type:** Construct  
**Supporting papers:** 45  
**Also known as:** Decision-making Ability, Decision-making ability, Decision-making capability, Activity evaluation, Decision-level ability, High-level reasoning  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats decision-making as a latent or underlying capability for goal-directed choice and action. Most commonly, papers describe it as supporting sequential action selection and policy formation in interactive environments, or more broadly as the capacity to plan, make choices, and take actions autonomously to accomplish complex tasks or goals. Smaller strands recast it as an observable process, namely evaluating candidate activities by their effects on desire states, or as a high-level reasoning capacity that either plans steps toward abstract goals or connects high-level decisions with low-level control. The main disagreement is between broad latent-capacity framings and narrower process- or control-oriented ones.

**Space of facets.** The terminology is not uniform: papers use labels such as decision-making capability, decision-making ability, decision-level ability, activity evaluation, and high-level reasoning for overlapping phenomena. One paper explicitly splits a skill into a decision-level component, described as problem solving, diagnosis, and planning, versus an action-level component, described as execution or implementation, and warns against conflating reasoning skills with action skills. Other papers organize the construct around candidate activity evaluation against imagined desire states, or around the link between high-level decisions and low-level control, so the same umbrella term covers both choice formation and its translation into action.

**Space of measurement.** Papers operationalize decision-making through 6 linked instruments and 2 behavioral indicators, with direct measurement claims centered on task benchmarks and environments. The most frequently linked instruments are ALFWorld and WebShop, followed by AgentBench, Game of 24, and T-Eval, plus 1 other instrument; the cited descriptions say these tools test decision-making in text-based games, web navigation or e-commerce settings, multi-environment agent evaluation, and multi-step API use. These operationalizations mostly match definitions centered on planning and action selection in interactive settings, and less directly capture definitions that foreground desire-state evaluation or the connection between high-level decisions and low-level control.

**Links.** No causal or correlational claims are recorded. Papers instead relate decision-making to 2 behavioral indicators and 4 constructs, most explicitly stock trading and diagram understanding, and constructs such as webpage understanding, visual perception, and strategic reasoning, plus 1 other related construct. The recorded language ranges from financial choices such as trading strategies and portfolio optimization, to flowchart interpretation for automation, decision-making, and analysis, to a study that says it decouples webpage understanding from decision making of LLM agents, and to descriptions of decision-making as a complex task requiring several abilities.

## Sources

**Decision-making capability** (2 papers: [On the Modeling Capabilities of Large Language Models for Sequential Decision Making](https://proceedings.iclr.cc/paper_files/paper/2025/file/368cba57d00902c752eaa9e4770bbbbe-Paper-Conference.pdf), [VLASCD: A Visual Language Action Model for Simultaneous Chatting and Decision Making](https://aclanthology.org/2025.emnlp-main.468.pdf))
> The latent ability of an LLM to support sequential action selection and policy formation across interactive environments.

**Decision-making Ability** (1 paper: [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf))
> The general capability of an agent to plan, make decisions, and take actions to accomplish complex tasks autonomously.

**Decision-making ability** (1 paper: [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf))
> The underlying cognitive capacity of an agent to perceive its environment, make choices, and select appropriate actions to achieve a goal.

**Activity evaluation** (1 paper: [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf))
> The observable process of an agent assessing the potential impact of each candidate activity on its internal desire states.

**Decision-level ability** (1 paper: [A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf))
> The latent cognitive capacity for problem-solving, diagnosis, and planning required to determine a course of action for a given skill.

**High-level reasoning** (1 paper: [SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cm/zhang25cm.pdf))
> The latent ability of an autonomous driving system to connect high-level decisions, such as 'the car should slow to a stop', with low-level control signals.

## Relationships

### Decision-making →
- **ALFWorld** (measurement instrument): *measured_by*, 4 papers
  > We select 5 tasks: SciWorld (Wang et al., 2022), Alfworld (Shridhar et al., 2020), BabyAI (Chevalier-Boisvert et al., 2018), PDDL (Vallati et al., 2015), and Jericho (Hausknecht et al., 2020), all of them are testing models’ decision-making ability. (Section 4.1)
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
  - [Efficient Reinforcement Learning with Large Language Model Priors](https://proceedings.iclr.cc/paper_files/paper/2025/file/797be96e4481c3fe5d675c1ba5352969-Paper-Conference.pdf)
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
  - [Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25n/feng25n.pdf)
- **WebShop** (measurement instrument): *measured_by*, 3 papers
  > We use 100, 500, and 500 instances for Game of 24, WebShop, and ToolBench to evaluate the decision-making ability respectively.
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
  - [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf)
- **Game of 24** (measurement instrument): *measured_by*, 1 paper
  > We use 100, 500, and 500 instances for Game of 24, WebShop, and ToolBench to evaluate the decision-making ability respectively.
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **ToolBench** (measurement instrument): *measured_by*, 1 paper
  > We use 100, 500, and 500 instances for Game of 24, WebShop, and ToolBench to evaluate the decision-making ability respectively.
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **T-Eval** (measurement instrument): *measured_by*, 1 paper
  > “we conduct experiments using an OOD benchmark, T-Eval, a widely-used benchmark to evaluate the multi-step decision-making capability of LLMs to utilize APIs.”
  - [WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d7259031023c5aa463187c4a31c95c8-Paper-Conference.pdf)
- **AgentBench** (measurement instrument): *measured_by*, 1 paper
  > We present AGENTBENCH, a multi-dimensional benchmark that consists of 8 distinct environments to assess LLM-as-Agent’s reasoning and decision-making abilities.
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)

### Associated with
- **Stock trading** (behavioral indicator), 1 paper
  > Decision-Making assesses the model’s proficiency in making informed financial decisions, such as developing trading strategies and optimizing investment portfolios (Paiva et al., 2019).
  - [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Webpage understanding** (construct), 1 paper
  > “we decouple web page understanding from decision making of LLM agents”
  - [Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c995a913bc20ca39ce2231b8973be90a-Paper-Conference.pdf)
- **Visual perception** (construct), 1 paper
  > Decision-making is a complex task requiring various abilities. Several common ones are evaluated across all games: (1) Perception...
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > Decision-making is a complex task requiring various abilities. Several common ones are evaluated across all games: ... (2) Arithmetic Reasoning...
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Strategic reasoning** (construct), 1 paper
  > Decision-making is a complex task requiring various abilities. Several common ones are evaluated across all games: ... (4) Strategic Reasoning...
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Diagram understanding** (behavioral indicator), 1 paper
  > Accurate interpretation of flowcharts is essential for tasks such as automation, decision-making, and analysis.
  - [Beyond End-to-End VLMs: Leveraging Intermediate Text Representations for Superior Flowchart Understanding](https://aclanthology.org/2025.naacl-long.180.pdf)
