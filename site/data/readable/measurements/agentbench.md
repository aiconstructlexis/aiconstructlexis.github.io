# AgentBench
**Type:** Measurement instrument  
**Supporting papers:** 8  

## State of the Field

**What it is.** Across papers, the prevailing treatment is of AgentBench as a benchmark or evaluation suite for LLMs as agents, and some definitions use it as a comparison point for multi-round and task-diverse agent evaluation. Papers describe its contents in different ways: as diverse or 8 distinct environments, as environments for intrinsic reasoning and adaptation to environment feedback across OS, DB, HH, KG, WB, and WS, and as agent application tasks such as OS interaction, web browsing, and web shopping. Reported scoring also varies by environment, with success rate for OS, DB, HH, and WB, F1 for KG, and reward score for WS.

**What it is claimed to measure.** Its reported measurement role is distributed across several targets rather than a single construct: papers link it to 7 constructs and 3 behavioral indicators. Commonly named targets include Agency, Decision-making, Knowledge acquisition, Logical reasoning, and Instruction following, and papers also frame it more broadly as evaluating agent performance and core abilities.

**Space of uses.** No measurement instrument is linked to it. Papers nevertheless use it alongside other agent benchmarks, including ToolBench and AgentBoard, and one paper uses it as a comparison point by stating that its own task choice is planning-heavier than AgentBench. Other papers treat it as a direct evaluation setup or main benchmark, for example by following its setup for Webshop validation or by evaluating agent application scenarios with lengthy prompts on AgentBench.

## Sources

**AgentBench** (5 papers: [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf), [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf), [Generative Prompt Internalization](https://aclanthology.org/2025.naacl-long.376.pdf), [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf), [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.308.pdf))
> A benchmark for evaluating LLMs as agents, referenced as a comparison point for multi-round and task-diverse agent evaluation.

## Relationships

### → AgentBench
- **Reasoning** (construct): *measured_by*, 1 paper
  > We present AGENTBENCH, a multi-dimensional benchmark that consists of 8 distinct environments to assess LLM-as-Agent’s reasoning and decision-making abilities.
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > AGENTBENCH thus systematically evaluate an LLM’s core abilities, including following instructions (Ouyang et al., 2022), coding (Chen et al., 2021), knowledge acquisition (Joshi et al., 2017; Talmor et al., 2019), logical reasoning (Srivastava et al., 2023), and commonsense grounding (Shridhar et al., 2020a).
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Knowledge acquisition** (construct): *measured_by*, 1 paper
  > AGENTBENCH thus systematically evaluate an LLM’s core abilities, including following instructions (Ouyang et al., 2022), coding (Chen et al., 2021), knowledge acquisition (Joshi et al., 2017; Talmor et al., 2019), logical reasoning (Srivastava et al., 2023), and commonsense grounding (Shridhar et al., 2020a).
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Logical reasoning** (construct): *measured_by*, 1 paper
  > AGENTBENCH thus systematically evaluate an LLM’s core abilities, including following instructions (Ouyang et al., 2022), coding (Chen et al., 2021), knowledge acquisition (Joshi et al., 2017; Talmor et al., 2019), logical reasoning (Srivastava et al., 2023), and commonsense grounding (Shridhar et al., 2020a).
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > AGENTBENCH thus systematically evaluate an LLM’s core abilities, including following instructions (Ouyang et al., 2022), coding (Chen et al., 2021), knowledge acquisition (Joshi et al., 2017; Talmor et al., 2019), logical reasoning (Srivastava et al., 2023), and commonsense grounding (Shridhar et al., 2020a).
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Agency** (construct): *measured_by*, 1 paper
  > We tested on two standardized agent evaluation benchmarks, AgentBench [57] and Agent-Board [61], each is a collection of diverse tasks for evaluating LMs’ agentic capabilities. (Sec. 4.2)
  - [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **Text-to-SQL** (behavioral indicator): *measured_by*, 1 paper
  > Empirical results from AgentBench indicate that applying CycleQD to LLAMA3-8B-INSTRUCT based models not only enables them to surpass traditional fine-tuning methods in coding, operating systems, and database tasks, but also achieves performance on par with GPT-3.5-TURBO (Section 1).
  - [Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf)
- **Planning** (construct): *measured_by*, 1 paper
  > Concurrently, comprehensive benchmarks like AgentBench (Liu et al., 2023a), ToolBench (Qin et al., 2024), and AgentBoard (Ma et al., 2024) have been established to rigorously assess agent performance in reasoning, planning, and multi-turn interactions.
  - [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf)
- **Collaboration** (behavioral indicator): *measured_by*, 1 paper
  > AgentBench (Liu et al., 2023) and AgentGym (Xi et al., 2024) comprise multiple tasks requiring different LLMs within the system to cooperate and discuss
  - [Compound AI Systems Optimization: A Survey of Methods, Challenges, and Future Directions](https://aclanthology.org/2025.emnlp-main.1463.pdf)
- **Decision-making** (construct): *measured_by*, 1 paper
  > We present AGENTBENCH, a multi-dimensional benchmark that consists of 8 distinct environments to assess LLM-as-Agent’s reasoning and decision-making abilities.
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
