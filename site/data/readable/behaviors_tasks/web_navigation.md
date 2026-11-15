# Web navigation
**Type:** Behavioral indicator  
**Supporting papers:** 47  
**Also known as:** Web browsing, Vision-based web navigation, Web task completion, Webpage interaction, Site navigation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a sequential interaction task in which an agent follows a user instruction or request by taking browser or webpage actions, typically clicking, typing, following links, or filling forms, until the instruction is achieved on a website. Success is most often framed as finding information or completing a goal, though some definitions narrow it to reaching a target section of a site, completing online forms or transactions, or purchasing an item. One paper describes it as a class of sequential decision-making problems where agents interact with web interfaces following user instructions, while another makes the sequence explicit as executable actions used to accomplish the task on the website.

**Variants.** Papers use several near-names for the behavior, most often web browsing alongside web navigation, and a smaller line of work refers to site navigation, web task completion, or webpage interaction. The settings vary from browser use for search and information retrieval to real-website task completion and online shopping, and some benchmarks are described as spanning domains such as travel, shopping, and social media. A more specific variant is vision-based web navigation, where the agent receives only screenshots and acts on numbered interactive elements by clicking or typing.

**Space of elicitation and scores.** Papers measure it with 7 instruments. The most frequently linked are WebArena, WebShop, Mind2Web, GAIA, and WebVoyager, with 2 other instruments also used; across descriptions, these are mostly benchmarks or datasets for realistic web interaction, including a simulated e-commerce environment, live web navigation, and multimodal browsing settings. Scoring is not uniform: one paper reports binary rewards for whether a natural-language instruction is achieved by web navigation, while another adopts step success rate, where a step is successful when both the selected element and the predicted operation are correct.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects. The most common construct link is to Sequential decision-making, with papers treating web navigation as a task of that kind and as requiring interaction with an environment; the only other linked construct is Webpage understanding, where one paper claims a causal relationship from Webpage understanding to Web navigation by saying that difficulty in understanding web pages is a bottleneck for web agents. One paper also relates it to Tool use by defining tool use to include functions such as web browsing.

## Sources

**Web navigation** (7 papers: [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf), [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://proceedings.iclr.cc/paper_files/paper/2024/file/52f050499cf82fa8efb588e263f6f3a7-Paper-Conference.pdf), [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf), [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf), [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694.pdf), [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bonatti25a/bonatti25a.pdf), [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf))
> The task of interacting with websites to find information or complete a goal, which involves understanding HTML structure and performing actions like clicking links and filling forms.

**Web browsing** (3 papers: [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf), [Browsing Lost Unformed Recollections: A Benchmark for Tip-of-the-Tongue Search and Reasoning](https://aclanthology.org/2025.acl-long.406.pdf), [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf))
> Interacting with web browsers to navigate websites, search for information, or complete online forms and transactions.

**Vision-based web navigation** (1 paper: [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ah/zhou25ah.pdf))
> Navigating through web pages using only screenshots as input and performing actions like clicking or typing on numbered interactive elements to complete user tasks.

**Web task completion** (2 papers: [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf), [AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25m/xu25m.pdf))
> Executing a sequence of browser actions to accomplish a user task on a real website.

**Webpage interaction** (1 paper: [WebInject: Prompt Injection Attack to Web Agents](https://aclanthology.org/2025.emnlp-main.104.pdf))
> The process of a web agent taking a sequence of actions to engage with a webpage environment in order to complete a user-specified task.

**Site navigation** (1 paper: [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/4410c0711e9154a7a2d26f9b3816d1ef-Paper-Conference.pdf))
> Using interactive elements such as search functions, links, and menus to locate specific information or reach a target section of a website.

## Relationships

### Web navigation →
- **WebArena** (measurement instrument): *measured_by*, 7 papers
  > WebArena [8]: This web-based benchmark introduces realistic environments by replicating the functionality and data found in popular web domains (e.g., Gitlab, Reddit, Wikipedia). (Section 4.1.1)
  - [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
  - [Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c995a913bc20ca39ce2231b8973be90a-Paper-Conference.pdf)
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
  - [Agent Workflow Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bx/wang25bx.pdf)
  - [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ah/zhou25ah.pdf)
- **Mind2Web** (measurement instrument): *measured_by*, 6 papers
  > We adopt Mind2Web and WebArena for evaluation for their generalizability and resemblance of real-world web interactions. (Section 2)
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
  - [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf)
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
  - [Agent Workflow Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bx/wang25bx.pdf)
  - [Thread: A Logic-Based Data Organization Paradigm for How-To Question Answering with Retrieval Augmented Generation](https://aclanthology.org/2025.emnlp-main.923.pdf)
- **WebShop** (measurement instrument): *measured_by*, 5 papers
  > We evaluate LEAP across 3 decision-making domains: ALFWorld, a text-based game, WebShop, a web navigation environment, and Intercode, an interactive coding environment.
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
  - [AgentRM: Enhancing Agent Generalization with Reward Modeling](https://aclanthology.org/2025.acl-long.945.pdf)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
  - [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf)
  - [Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://aclanthology.org/2025.emnlp-main.892.pdf)
- **GAIA** (measurement instrument): *measured_by*, 2 papers
  > GAIA proposes real-world questions that require a set of fundamental abilities such as reasoning, multi-modality handling, web browsing, and generally tool-use proficiency. (ABSTRACT)
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **WebVoyager** (measurement instrument): *measured_by*, 2 papers
  > We validate PAE on challenging vision-based web navigation, using both real-world and self-hosted websites from WebVoyager and WebArena. (Abstract)
  - [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ah/zhou25ah.pdf)
  - [WebEvolver: Enhancing Web Agent Self-Improvement with Co-evolving World Model](https://aclanthology.org/2025.emnlp-main.454.pdf)
- **MiniWoB++** (measurement instrument): *measured_by*, 2 papers
  > MiniWoB++ (Liu et al., 2018) is an interactive web benchmark, with built-in reward functions. (§4.3)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **VisualWebArena** (measurement instrument): *measured_by*, 1 paper
  > We primarily experiment on VisualWebArena (VWA), a benchmark designed to evaluate multimodal agents performance on across a wide range of web navigation tasks and environments. (Section 4)
  - [ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3b893ba1de12f76020b03f7ae8e1afd-Paper-Conference.pdf)

### → Web navigation
- **Webpage understanding** (construct): *causes*, 1 paper
  > “the difficulty in understanding web pages is a major bottleneck for LLM-based web agents”
  - [Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c995a913bc20ca39ce2231b8973be90a-Paper-Conference.pdf)

### Associated with
- **Sequential decision-making** (construct), 2 papers
  > Large language model (LLM) agents have been applied to sequential decision-making tasks such as web navigation, but without any environment-specific experiences, they often fail in these complex tasks.
  - [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694.pdf)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **Tool use** (behavioral indicator), 1 paper
  > Tool Use: The ability to interact with external tools and APIs, including functions such as web browsing, code execution, and file uploads. (Section 2.1)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
