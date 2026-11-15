# Mind2Web
**Type:** Measurement instrument  
**Supporting papers:** 18  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage is as a real-world web navigation benchmark or dataset built from human demonstrations on real websites. Most definitions describe open-domain, action-annotated tasks, often noting about 2K instructions across 137 websites, and emphasize generalization across tasks, websites, and domains through cross-task, cross-website, and cross-domain settings. Papers differ in emphasis: some call it an offline task planning evaluation, some a demonstration dataset for action prediction, and one paper recasts its tasks as dynamic how-to questions with multiple possible outcomes per step. Evaluation is commonly described with step success rate and element accuracy, while some papers also mention action F1, task-level success rate, or step accuracy.

**What it is claimed to measure.** Papers use it to measure 3 behavioral indicators and 2 constructs. The prevailing measurement claim is web navigation: several papers describe Mind2Web as evaluating agents' capabilities on web navigation tasks or their capability of performing complex instructions on real-world websites. A smaller line of work uses it for action prediction, especially generalization across tasks, websites, and domains, and one paper each reports it as measuring planning, privacy leakage through PII-related action steps, and adaptability.

**Space of uses.** No measurement instrument is explicitly linked to it. In use, papers most often position it as an evaluation benchmark, sometimes paired with WebArena for web navigation evaluation, while other papers use its cross-website and cross-domain test splits to examine domain generality. A smaller line of work treats it as a data source, for example collecting trajectories from it or selecting it as the web-navigation source for benchmark curation and reward-model evaluation.

## Sources

**Mind2Web** (9 papers: [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf), [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf), [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://proceedings.iclr.cc/paper_files/paper/2024/file/52f050499cf82fa8efb588e263f6f3a7-Paper-Conference.pdf), [AgentStudio: A Toolkit for Building General Virtual Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/172fe9f8cc55953bad5c24774bf0142b-Paper-Conference.pdf), [Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents](https://aclanthology.org/2025.acl-long.857.pdf), [Agent Workflow Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bx/wang25bx.pdf), [Thread: A Logic-Based Data Organization Paradigm for How-To Question Answering with Retrieval Augmented Generation](https://aclanthology.org/2025.emnlp-main.923.pdf), [Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6a6891cf1dfc64d664f086cf5976e93-Paper-Conference.pdf), [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf))
> Real-world web navigation benchmark containing human demonstrations across open-domain websites, assessing generalization across tasks, websites, and domains using step success rate and element accuracy.

## Relationships

### → Mind2Web
- **Web navigation** (behavioral indicator): *measured_by*, 6 papers
  > We adopt Mind2Web and WebArena for evaluation for their generalizability and resemblance of real-world web interactions. (Section 2)
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
  - [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf)
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
  - [Agent Workflow Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bx/wang25bx.pdf)
  - [Thread: A Logic-Based Data Organization Paradigm for How-To Question Answering with Retrieval Augmented Generation](https://aclanthology.org/2025.emnlp-main.923.pdf)
- **Action prediction** (behavioral indicator): *measured_by*, 2 papers
  > It provides action prediction tasks that measure the generalization of LLMs across the tasks, websites, and their domains (e.g. travel, shopping) (Section 4.2).
  - [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)
  - [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf)
- **Planning** (construct): *measured_by*, 1 paper
  > SoTA performance on Mind2Web, an ofﬂine task planning evaluation (Section 1).
  - [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)
- **Privacy leakage** (behavioral indicator): *measured_by*, 1 paper
  > We collect 177 action steps that involve diverse PII categories on realistic websites from the Mind2Web dataset, and conduct experiments using one of the most capable generalist web agent frameworks to date. (Abstract)
  - [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf)
- **Adaptability** (construct): *measured_by*, 1 paper
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
