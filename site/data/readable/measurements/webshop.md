# WebShop
**Type:** Measurement instrument  
**Supporting papers:** 33  
**Also known as:** Webshop, Web Shopping  

## State of the Field

**What it is.** Most papers describe WebShop as an interactive online shopping or e-commerce simulator benchmark, though a smaller number call it a dataset or task. The recurring setup is that an agent follows a user instruction, navigates web pages with actions such as search and click, and selects product attributes or options to identify and purchase the right item; some definitions emphasize detailed product descriptions and specifications, a large amount of real-world product data, over a million real-world products, or scraped amazon.com pages. Papers differ slightly in format language, calling it a browser environment, network-based simulation environment, interactive web environment, or online shopping dataset, and a few also specify scoring by completion level or dense final rewards from 0 to 1, while one description says performance is based on attribute, option, product type, and price matches within tasks of 30 timesteps.

**What it is claimed to measure.** Across papers that make measurement claims, the usage is concentrated rather than spread across many targets: WebShop is linked to one construct and one behavioral indicator. Several papers use it to measure Decision-making, describing it as simulating an e-commerce environment to test decision-making abilities or using it to evaluate decision-making ability. Several other papers use it to measure Web navigation, calling it a web navigation environment or using it for web navigation.

**Space of uses.** Papers usually deploy WebShop as one component of broader agent benchmark suites, commonly as the web or shopping task alongside ALFWorld, and sometimes within multi-domain evaluations that also include planning, coding, tool-use, or game settings. In these studies it is positioned as a rigorous or representative benchmark for agent evaluation, and papers report outcomes through completion-level rewards or matching-based task scores rather than a single fixed metric. Some papers also frame it as a real-world simulated planning dataset or as part of benchmark collections covering diverse use cases.

**Concerns raised.** Only a smaller line of work raises explicit concerns about WebShop itself. One paper studies Query-Attack and Observation-Attack on the WebShop dataset, and another highlights misaligned actions in this environment, noting that click[Buy Now] is sensitive because of financial risk.

## Sources

**WebShop** (14 papers: [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf), [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf), [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf), [THREAD: Thinking Deeper with Recursive Spawning](https://aclanthology.org/2025.naacl-long.427.pdf), [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf), [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf), [Agentic Knowledgeable Self-awareness](https://aclanthology.org/2025.acl-long.619.pdf), [Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf), [Preemptive Detection and Correction of Misaligned Actions in LLM Agents](https://aclanthology.org/2025.emnlp-main.12.pdf), [Agent Planning with World Knowledge Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf), [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf), [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf), [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf), [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Paper-Conference.pdf))
> A benchmark environment that simulates an online shopping website, where an agent must navigate, search, and select product attributes to find and purchase a specific item based on a user instruction.

**Webshop** (1 paper: [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf))
> A benchmark for evaluating LLM agents on web-based shopping tasks.

**Web Shopping** (1 paper: [Generative Prompt Internalization](https://aclanthology.org/2025.naacl-long.376.pdf))
> A benchmark task where an agent must navigate scraped e-commerce web pages to find a specific product by using click and search actions.

## Relationships

### → WebShop
- **Web navigation** (behavioral indicator): *measured_by*, 5 papers
  > We evaluate LEAP across 3 decision-making domains: ALFWorld, a text-based game, WebShop, a web navigation environment, and Intercode, an interactive coding environment.
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
  - [AgentRM: Enhancing Agent Generalization with Reward Modeling](https://aclanthology.org/2025.acl-long.945.pdf)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
  - [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf)
  - [Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://aclanthology.org/2025.emnlp-main.892.pdf)
- **Decision-making** (construct): *measured_by*, 3 papers
  > We use 100, 500, and 500 instances for Game of 24, WebShop, and ToolBench to evaluate the decision-making ability respectively.
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
  - [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf)
