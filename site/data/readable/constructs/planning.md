# Planning
**Type:** Construct  
**Supporting papers:** 204  
**Also known as:** Planning ability, Planning capability, Task prioritization, Planning capabilities, Self-planning, Action deliberation, Reasoning path selection, Basic task solving  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats planning as a latent or cognitive ability to determine, decompose, and sequence steps or actions toward a goal, often in multi-step, long-horizon, partially observable, or constrained settings. Many definitions make goal decomposition explicit, describing planning as turning high-level instructions into sub-instructions, subgoals, or manageable plans, while others stress feasibility under constraints, dynamic adjustment to current state or feedback, or generating a valid chain of actions or tool calls. A smaller line of work narrows the term to pre-answer structuring, such as formulating a structured outline before a detailed response or writing high-level natural language plans before code. Other narrow variants treat task prioritization, action deliberation, reasoning path selection, or basic task solving as planning-related abilities.

**Space of facets.** Papers break the construct into recurring facets including long-horizon planning, high-level natural language planning, task decomposition, constraint-aware or multi-constraint planning, and adaptive planning that updates actions from state, memory, or environmental feedback. Some works further distinguish open-loop from closed-loop planning, or global planning from iterative adjustment during execution. At the naming level, the same label is used for both answer-structure planning and environment-action planning, while nearby labels such as planning capability, planning ability, self-planning, and action deliberation mark narrower slices of the broader construct. Planning is also repeatedly described together with reasoning, tool use, and environmental interaction.

**Space of measurement.** Operationalizations are predominantly benchmark- and environment-based: planning is linked to 13 measurement instruments and 12 behavioral indicators. The most recurrent instruments are Blocksworld, TravelPlanner, and Game of 24, and the papers describe linked measures as planning benchmarks or problems in symbolic, multi-constraint, and multi-step settings. Among behavioral indicators, Tool use and Code generation are the most frequent links, so papers also observe planning through whether models select coherent actions, API calls, or intermediate steps toward a goal. These operationalizations largely match the dominant definitions centered on producing or organizing step sequences for goal achievement.

**Links.** Several papers claim causal relationships from planning to Tool use, Code generation, and Reasoning, and other papers extend this pattern to additional downstream behaviors and constructs. In the opposite direction, papers claim causal relationships from Reasoning and World modeling to planning, alongside other upstream constructs and behaviors. Non-causal links are reported with Pathfinding and a broader set of search-, reasoning-, and decision-making constructs. No correlational link is reported.

## Sources

**Planning** (26 papers: [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf), [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf), [Large Language Models as Automated Aligners for benchmarking Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf), [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf), [Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/03d7e13f0092405804f3a381ade8f3f0-Paper-Conference.pdf), [SmartPlay : A Benchmark for LLMs as Intelligent Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/063d1fadbde557466bf5bcffe814a64e-Paper-Conference.pdf), [THOUGHT PROPAGATION: AN ANALOGICAL APPROACH TO COMPLEX REASONING WITH LARGE LANGUAGE MODELS](https://proceedings.iclr.cc/paper_files/paper/2024/file/2dae7d1ccf1edf76f8ce7c282bdf4730-Paper-Conference.pdf), [Text2Reward: Reward Shaping with Language Models for Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/9941833e8327910ef25daeb9005e4748-Paper-Conference.pdf), [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf), [ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/13250eb13871b3c2c0a0667b54bad165-Paper-Conference.pdf), [Unified Human-Scene Interaction via Prompted Chain-of-Contacts](https://proceedings.iclr.cc/paper_files/paper/2024/file/6a6ecedac816a24f92ad1f444b1edcb0-Paper-Conference.pdf), [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf), [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf), [Revealing the Barriers of Language Agents in Planning](https://aclanthology.org/2025.naacl-long.93.pdf), [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf), [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf), [DAWN-ICL: Strategic Planning of Problem-solving Trajectories for Zero-Shot In-Context Learning](https://aclanthology.org/2025.naacl-long.96.pdf), [Evaluating and Improving Graph to Text Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.513.pdf), [Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://aclanthology.org/2025.naacl-long.83.pdf), [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf), [The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models](https://aclanthology.org/2025.naacl-long.303.pdf), [CogLM: Tracking Cognitive Development of Large Language Models](https://aclanthology.org/2025.naacl-long.4.pdf), [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369.pdf), [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bonatti25a/bonatti25a.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf))
> The ability of a model to formulate a structured plan or outline before generating a detailed response.

**Planning capability** (7 papers: [LLM-Assisted Code Cleaning For Training Accurate Code Generators](https://proceedings.iclr.cc/paper_files/paper/2024/file/41137f3997ade899893ccd3973592d4b-Paper-Conference.pdf), [AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0142921fad7ef9192bd87229cdafa9d4-Paper-Conference.pdf), [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf), [Large Language Models Can Solve Real-World Planning Rigorously with Formal Verification Tools](https://aclanthology.org/2025.naacl-long.176.pdf), [TripCraft: A Benchmark for Spatio-Temporally Fine Grained Travel Planning](https://aclanthology.org/2025.acl-long.834.pdf), [HyperTree Planning: Enhancing LLM Reasoning via Hierarchical Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gui25b/gui25b.pdf), [Coarse-to-Fine Grounded Memory for LLM Agent Planning](https://aclanthology.org/2025.emnlp-main.659.pdf))
> The latent ability to generate correct and useful high-level natural language plans that outline the steps needed to solve a programming problem before implementation.

**Planning ability** (3 papers: [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf), [Chain of Thoughtlessness? An Analysis of CoT in Planning](https://proceedings.neurips.cc/paper_files/paper/2024/file/3365d974ce309623bd8151082d78206c-Paper-Conference.pdf), [The Belief State Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/01b3dea1871f7cea1e0e6be1f2f085bc-Paper-Conference.pdf))
> The ability to choose and sequence operations adaptively based on the current state of the table and the question.

**Task prioritization** (1 paper: [Robotouille: An Asynchronous Planning Benchmark for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d033407a1a4b7a75cd5f9e4575ad9fb5-Paper-Conference.pdf))
> The ability to correctly order subtasks, particularly in asynchronous settings, to maximize efficiency and increase the likelihood of success.

**Planning capabilities** (1 paper: [Tool-Planner: Task Planning with Clusters across Multiple Tools](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f605d59a0dbde101518b552cb616ddf-Paper-Conference.pdf))
> The latent ability to generate and adjust multi-step action sequences for accomplishing goals, especially when external tools are involved.

**Self-planning** (1 paper: [Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://aclanthology.org/2025.emnlp-main.892.pdf))
> The inherent capability of an LLM to create and follow a plan to solve a problem without explicit, step-by-step instructions.

**Action deliberation** (1 paper: [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf))
> The latent ability of an LLM agent to generate and evaluate multiple candidate actions before selecting one, based on reasoning about their likely outcomes.

**Reasoning path selection** (1 paper: [How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark](https://aclanthology.org/2025.emnlp-main.674.pdf))
> Choosing which dependencies and intermediate steps to use when solving a multi-step problem, including avoiding irrelevant or distracting information.

**Basic task solving** (1 paper: [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25f/yang25f.pdf))
> The latent ability to carry out straightforward embodied tasks by producing appropriate action sequences for low to medium difficulty goals.

## Relationships

### Planning →
- **Blocksworld** (measurement instrument): *measured_by*, 4 papers
  > Finally, we validate these results on a real-world task planning benchmark, Blocksworld [22], which directly corresponds to the path-finding problem (see Appendix F). (Introduction).
  - [ALPINE: Unveiling The Planning Capability of Autoregressive Learning in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d848cb2c84f0bba7f1f73cf232734c40-Paper-Conference.pdf)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
  - [Automatic Curriculum Expert Iteration for Reliable LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9083c94382509473bdf5fc2672fc72b3-Paper-Conference.pdf)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
- **TravelPlanner** (measurement instrument): *measured_by*, 4 papers
  > Planning in complex and realistic environments is also a crucial skill for building autonomous agents. Thus, we also select TravelPlanner (Xie et al., 2024), a benchmark designed to evaluate language agents in real-world complex planning with multiple constraints. (Section 4.3)
  - [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf)
  - [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yi25c/yi25c.pdf)
  - [HyperTree Planning: Enhancing LLM Reasoning via Hierarchical Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gui25b/gui25b.pdf)
  - [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf)
- **Tool use** (behavioral indicator): *causes*, 3 papers
  > After the planning step, our agent takes action to construct adaptive VL prompts for the tool models (i.e., VLM/LLM). (Section 1)
  - [Re-Aligning Language to Visual Objects with an Agentic Workflow](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d9057d84a9fc37523bf826232ea6820-Paper-Conference.pdf)
  - [ShortcutsBench: A Large-Scale Real-world Benchmark for API-based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c16a99558b0b4f6b10966ca9bdb98ade-Paper-Conference.pdf)
  - [TC–RAG: Turing–Complete RAG's Case study on Medical LLM Systems](https://aclanthology.org/2025.acl-long.558.pdf)
- **Star Graph Task** (measurement instrument): *measured_by*, 2 papers
  > Specifically, Bachmann & Nagarajan (2024) introduces a simple path finding task that requires basic planning... Figure 5: Star Graph Task: Illustration and Performance Comparison. (Section 4)
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
  - [The Belief State Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/01b3dea1871f7cea1e0e6be1f2f085bc-Paper-Conference.pdf)
- **Logistics** (measurement instrument): *measured_by*, 2 papers
  > planning [Logistics, 53] (Introduction).
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **Game of 24** (measurement instrument): *measured_by*, 2 papers
  > To illustrate these limitations, we conducted experiments using the Game of 24, a simple yet illustrative planning problem with a depth of 3 and a maximum breadth of 48. (Section 3.2)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
  - [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf)
- **Task decomposition** (behavioral indicator): *causes*, 2 papers
  > Using the strategy stored in Planning Memory, we break down complex chemistry problems into hierarchical sub-tasks.
  - [ChemAgent: Self-updating Memories in Large Language Models Improves Chemical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa7f64b45970e6a7f8824781e7e01501-Paper-Conference.pdf)
  - [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **Code generation** (behavioral indicator): *causes*, 2 papers
  > The AEP examples contain planning steps, that outline a possible decomposition of the task (lines 7, 14, 17) to encourage step-by-step thinking and to improve generation quality. (Section 2.3.1)
  - [ASPERA: A Simulated Environment to Evaluate Planning for Complex Action Execution](https://aclanthology.org/2025.acl-long.1234.pdf)
  - [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://proceedings.iclr.cc/paper_files/paper/2025/file/e01c431bbb83153632c0dcfaf8ccda0a-Paper-Conference.pdf)
- **T-Eval** (measurement instrument): *measured_by*, 1 paper
  > We utilize T-Eval (Chen et al., 2023c), which assesses six core competencies: planning, reasoning, retrieval, understanding, instruction following, and reviewing. (Sec. 4.1)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > Additional experiments on other benchmarks like RM-Bench, JudgeBench, and FollowBenchEval further highlight the utility of both planning and reasoning for building robust LLM-as-a-Judge reasoning models. (Abstract)
  - [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf)
- **Mind2Web** (measurement instrument): *measured_by*, 1 paper
  > SoTA performance on Mind2Web, an ofﬂine task planning evaluation (Section 1).
  - [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)
- **Negotiation** (behavioral indicator): *causes*, 1 paper
  > Planning. This step was important to reach a ﬁnal successful deal (row 4); without it, agents’ suggestions may saturate and no longer increase the collective score (Figure 3b). (Section 4.2)
  - [Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation](https://proceedings.neurips.cc/paper_files/paper/2024/file/984dd3db213db2d1454a163b65b84d08-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GTA** (measurement instrument): *measured_by*, 1 paper
  > Fine-grained metrics are designed for tool use, unveiling tool-augmented LLMs’ reasoning and planning capabilities in real-world scenarios. (Section 1)
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Long-horizon task completion** (behavioral indicator): *causes*, 1 paper
  > Relevant studies indicate that the human brain is essential for planning and reflection, while the cerebellum controls low-level actions, both crucial for complex tasks [40, 41]. (Section 2.2)
  - [Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > These findings suggest that the model’s inherent reasoning and planning capabilities developed during pre-training are crucial for general self-improvement. (Section 4.4)
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct): *causes*, 1 paper
  > their planning ability remains a critical bottleneck in tackling complex multi-step reasoning tasks. (ABSTRACT)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **TextWorld** (measurement instrument): *measured_by*, 1 paper
  > Problem Type partial observability, long-term planning and memory, and common sense (Table 1).
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
- **AI2-THOR** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our framework using two distinct environments: a dynamic 8 × 8 GridWorld and a static 3D-rendered kitchen (AI2-THOR)... Our experiments focus on three key aspects: the effectiveness of text-based action representations, causal inference, and planning.
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **AgentBench** (measurement instrument): *measured_by*, 1 paper
  > Concurrently, comprehensive benchmarks like AgentBench (Liu et al., 2023a), ToolBench (Qin et al., 2024), and AgentBoard (Ma et al., 2024) have been established to rigorously assess agent performance in reasoning, planning, and multi-turn interactions.
  - [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > This paper presents how language models can be trained for internal and external planning to improve reasoning in sequential decision-making, using board games as an experimental domain. (Section 1)
  - [Mastering Board Games by External and Internal Planning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schultz25a/schultz25a.pdf)
- **Code reasoning** (construct): *causes*, 1 paper
  > Furthermore, the enhanced planning capability gained through HLP boosts model performance on code reasoning. (Abstract)
  - [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1672.pdf)
- **PlanBench** (measurement instrument): *measured_by*, 1 paper
  > For instance, models frequently demonstrate high performance on standardized test-style questions yet struggle when faced with complex planning or multi-step reasoning challenges, a limitation highlighted by specialized benchmarks like PlanBench (Valmeekam et al., 2022), GPQA (Rein et al., 2023), and HLE (Phan et al., 2025). (Section 2.4)
  - [In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1208.pdf)

### → Planning
- **Reasoning** (construct): *causes*, 3 papers
  > Crucially, the agent needs to perform multi-step reasoning between such information and the current state of the environment to figure out a plan of action
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [ChatCam: Empowering Camera Control through Conversational AI](https://proceedings.neurips.cc/paper_files/paper/2024/file/61dad41cb106aef1154a82965f42df0e-Paper-Conference.pdf)
  - [Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf)
- **World modeling** (construct): *causes*, 2 papers
  > we show that the Code World Models synthesized with it can be successfully used for planning
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [World Modeling Makes a Better Planner: Dual Preference Optimization for Embodied Task Planning](https://aclanthology.org/2025.acl-long.1044.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > LEPA refines the plan through self-reflection, aiming to acquire plans that are instrumental in yielding correct solutions.
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **In-context learning** (construct): *causes*, 1 paper
  > In this work, we explore how to improve the model planning capability through in-context learning (ICL), specifically, what signals can help select the exemplars. (Section Abstract)
  - [Improving Large Language Model Planning with Action Sequence Similarity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b18c6549c77411d92e645027a25838a8-Paper-Conference.pdf)
- **Theory of mind** (construct): *causes*, 1 paper
  > We introduce the Theory of Mind module that scaffolds the high-level planning process by generating hypotheses about other agents' strategies in natural language.
  - [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/12f483f624b378f9f3058d8ecd3c7ff5-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > LLMs often experience hallucinations (Huang et al., 2023), which present two major challenges in planning. First, they might struggle to assess if a plan is achievable given a specific problem description (Aghzal et al., 2023; Kambhampati, 2024). (Section 10)
  - [PlanGenLLMs: A Modern Survey of LLM Planning Capabilities](https://aclanthology.org/2025.acl-long.958.pdf)

### Associated with
- **Pathfinding** (behavioral indicator), 2 papers
  > “The ability to search is fundamental in many important tasks, such as reasoning ..., planning ..., and navigation ...”
  - [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf)
  - [The Factorization Curse: Which Tokens You Predict Underlie the Reversal Curse and More](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbcce87f745072c819204529be843d16-Paper-Conference.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > we posit that the natural language mathematical CoT task is determined by two sub-tasks: step planning task and step calculation task for global logic planning and local mathematical calculation. (Section 4.2)
  - [Unlocking the Capabilities of Thought: A Reasoning Boundary Framework to Quantify and Optimize Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/62ab1c2cb4b03e717005479efb211841-Paper-Conference.pdf)
- **Sequential decision-making** (construct), 1 paper
  > ReAct [23]: This LLM-based planning method integrates reasoning and acting to address sequential decision-making tasks. (Section 4.1.2)
  - [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf)
- **Molecular structure elucidation** (behavioral indicator), 1 paper
  > Solving this task requires AI models to possess the ability to interpret spectral images, engage in complex reasoning, and plan effectively across extended workflows. (Section 1)
  - [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Backtracking** (behavioral indicator), 1 paper
  > Planning problems, however, demand a more sophisticated approach that incorporates: ... Backtracking (the capability to recognize dead-ends and return to previous states to explore alternative paths) (Section 3.1)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **Textual reasoning** (behavioral indicator), 1 paper
  > Text is suitable for semantic analysis and commonsense reasoning, but is not the best format for precise computation and planning, symbolic manipulation, and algorithmic processing and optimization (Kambhampati et al., 2024b; Chen et al., 2024a). (Section 1)
  - [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf)
- **Temporal reasoning** (construct), 1 paper
  > "While these efforts highlight the relevance of temporal reasoning in planning"
  - [TCP: a Benchmark for Temporal Constraint-Based Planning](https://aclanthology.org/2025.emnlp-main.1142.pdf)
- **Causal reasoning** (construct), 1 paper
  > “LLMs have recently shown great promise in planning and reasoning applications. These tasks demand robust systems, which arguably require a causal understanding of the environment.”
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **Plan generation** (behavioral indicator), 1 paper
  > Planning: Plan-and-solve prompting (PS) (Wang et al., 2023) elicits the model to first generate a plan (e.g., numbered steps) and then execute that plan, yielding improvements over standard CoT. (Section 2)
  - [Prior Prompt Engineering for Reinforcement Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1590.pdf)
