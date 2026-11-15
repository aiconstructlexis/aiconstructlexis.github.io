# Chain of thought
**Type:** Behavioral indicator  
**Supporting papers:** 327  
**Also known as:** Explicit reasoning, Chain-of-thought generation, Chain-of-thought reasoning, Step-by-step reasoning, Step-by-step solution generation, Reasoning path generation, Rationale generation, Thought generation, Reasoning generation, Reasoning trace generation, Step-by-step reasoning generation, Multi-step reasoning generation, Intermediate reasoning generation, Reasoning chain generation, Stepwise reasoning, Intermediate step generation, Chain-of-thought computation, Hierarchical thought generation, Multi-branch reasoning, Search trajectory verbalization, Chain-of-thought inference, Reasoning chain construction, Inner monologue generation, Reasoning context generation, Silent chain-of-thought generation, Explicit Chain-of-Thought generation, Intermediate instruction generation, Reasoning step generation, Logic generation, Step-by-step execution, Structured response generation, Continuous thought generation, Structured chain-of-thought generation, Natural language chain-of-thought generation, Program chain-of-thought generation, Chain-of-Thought Reasoning, Intermediate token generation, Reasoned explanation generation, Multi-step reasoning, Step-wise reasoning  

## State of the Field

**Space of definitions.** Across papers, the dominant usage treats chain of thought as the observable production of intermediate, step-by-step reasoning before a final answer. Most definitions require a visible rationale, explanation, reasoning path, or trace that leads from the problem to an answer, score, label, plan, ranking, or action, and some make the endpoint explicit by asking the model to derive the result step by step and give the answer at the end. A smaller line broadens the behavior beyond explicit natural language, describing intermediate tokens or scratchpads, executable program steps, continuous latent thoughts, or fixed <THINK> tokens that simulate internal reasoning.

**Variants.** Most papers study nearby variants under names such as chain-of-thought generation, chain-of-thought reasoning, step-by-step reasoning, rationale generation, and reasoning trace generation. The recurring settings are math and other multi-step problem solving, multimodal reasoning, retrieval and multi-document QA, tool use and agents, and judging or classification. Smaller variants make the trace more structured or more implicit, for example hierarchical or multi-branch traces, verbalized search trajectories, knowledge-triple chains, and program, silent, or continuous forms of thought.

**Space of elicitation and scores.** Papers link chain of thought to 12 measurement instruments. The most frequent instrument links are GSM8K, StrategyQA, LLM-as-a-judge, AIME, and G-Eval, and some papers use LLM-as-a-judge specifically to assess intermediate reasoning steps or the reasoning trace. Overall, the measurement mix includes task benchmarks, automated judging, and human review, alongside several other linked instruments.

**What it is taken as evidence of.** Papers link chain of thought to 17 constructs. The prevailing construct links are reasoning-centered: several papers claim a causal relationship from Chain of thought to Reasoning, followed by Mathematical reasoning, Interpretability and explainability, Chain-of-thought reasoning, and Expressive power, while some other construct links are recorded as relatedness claims rather than causal ones. The usage is therefore broad rather than tied to a single agreed construct, although most links stay within the reasoning family.

## Sources

**Explicit reasoning** (1 paper: [REARANK: Reasoning Re-ranking Agent via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.125.pdf))
> The model generates a visible, step-by-step justification for its decisions, such as relevance assessments during reranking, before producing a final output.

**Chain-of-thought generation** (5 papers: [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf), [Ask, and it shall be given: On the Turing completeness of prompting](https://proceedings.iclr.cc/paper_files/paper/2025/file/123d3e814e257e0781e5d328232ead9b-Paper-Conference.pdf), [TRACT: Regression-Aware Fine-tuning Meets Chain-of-Thought Reasoning for LLM-as-a-Judge](https://aclanthology.org/2025.acl-long.147.pdf), [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf), [Chain of Thought Empowers Transformers to Solve Inherently Serial Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/3309b4112c9f04a993f2bbdd0274bba1-Paper-Conference.pdf))
> The observable model output of generating a sequence of intermediate steps that lead to a final answer.

**Chain-of-thought reasoning** (17 papers: [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf), [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf), [ToolHop: A Query-Driven Benchmark for Evaluating Large Language Models in Multi-Hop Tool Use](https://aclanthology.org/2025.acl-long.150.pdf), [Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/erdogan25a/erdogan25a.pdf), [SoundMind: RL-Incentivized Logic Reasoning for Audio-Language Models](https://aclanthology.org/2025.emnlp-main.27.pdf), [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf), [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf), [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf), [Large Language Models as Automated Aligners for benchmarking Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf), [MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b063829b922fdeb4fa3472dd3471ff43-Paper-Conference.pdf), [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf), [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf), [Aggregation Artifacts in Subjective Tasks Collapse Large Language Models' Posteriors](https://aclanthology.org/2025.naacl-long.284.pdf), [CogLM: Tracking Cognitive Development of Large Language Models](https://aclanthology.org/2025.naacl-long.4.pdf), [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf), [IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models](https://aclanthology.org/2025.naacl-long.139.pdf), [VisDoM: Multi-Document QA with Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.310.pdf))
> The task of generating a step-by-step explanation (a 'chain of thought') that leads to the final answer for a complex reasoning problem, often involving both text and images.

**Step-by-step reasoning** (4 papers: [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf), [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf), [Stepwise Reasoning Disruption Attack of LLMs](https://aclanthology.org/2025.acl-long.251.pdf), [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf))
> The observable behavior of generating a sequence of intermediate steps or a rationale that leads to the final answer, typically prompted by a Chain-of-Thought strategy.

**Step-by-step solution generation** (4 papers: [SciInstruct: a Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02ee6b7295f720407b56c457b34c54d5-Paper-Datasets_and_Benchmarks_Track.pdf), [WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c04aea54c2a60a632a47bd451cd2849-Paper-Conference.pdf), [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf), [The Emperor's New Reasoning: Format Imitation Overshadows Genuine Mathematical Understanding in SFT](https://aclanthology.org/2025.emnlp-main.1067.pdf))
> The behavior of producing a detailed, sequential reasoning process (chain-of-thought) leading to a final answer for a given problem.

**Reasoning path generation** (4 papers: [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf), [ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2025/file/9c77f2ce42151b2c2e26d2cf47f99564-Paper-Conference.pdf), [Beyond Surface Simplicity: Revealing Hidden Reasoning Attributes for Precise Commonsense Diagnosis](https://aclanthology.org/2025.acl-long.627.pdf), [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.24.pdf))
> The behavior of generating a step-by-step explanation or sequence of intermediate thoughts (Chain-of-Thought) that leads from a problem statement to its solution.

**Rationale generation** (3 papers: [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf), [Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf), [Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference](https://aclanthology.org/2025.acl-long.340.pdf))
> The behavior of producing a chain of reasoning or explanation for a decision or confidence level when prompted.

**Thought generation** (3 papers: [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf), [Lean-STaR: Learning to Interleave Thinking and Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5357781c204d4412e44ed9cbcdb08d5-Paper-Conference.pdf), [Accelerating Large Language Model Reasoning via Speculative Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25di/wang25di.pdf))
> The specific action of producing one or more candidate intermediate reasoning steps (thoughts) from a given state in a problem-solving process.

**Reasoning generation** (3 papers: [Large Language Models' Expert-level Global History Knowledge Benchmark (HiST-LLM)](https://proceedings.neurips.cc/paper_files/paper/2024/file/38cc5cba8e513547b96bc326e25610dc-Paper-Datasets_and_Benchmarks_Track.pdf), [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf), [Hidden in Plain Sight: Evaluation of the Deception Detection Capabilities of LLMs in Multimodal Settings](https://aclanthology.org/2025.acl-long.1497.pdf))
> Producing a short explanation of evidence and reasoning before giving the final answer.

**Reasoning trace generation** (3 papers: [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf), [Improving Reasoning Performance in Large Language Models via Representation Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e73c39cc428c7d264d9820319f31e79-Paper-Conference.pdf), [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf))
> The observable act of autoregressively producing a sequence of reasoning steps from a given problem or prompt.

**Step-by-step reasoning generation** (3 papers: [Unlocking the Capabilities of Thought: A Reasoning Boundary Framework to Quantify and Optimize Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/62ab1c2cb4b03e717005479efb211841-Paper-Conference.pdf), [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf), [Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions](https://aclanthology.org/2025.acl-long.843.pdf))
> The action of verbalizing a sequence of intermediate steps that lead to a final answer for a given problem.

**Multi-step reasoning generation** (2 papers: [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf), [Spontaneous Giving and Calculated Greed in Language Models](https://aclanthology.org/2025.emnlp-main.267.pdf))
> The observable process of generating a sequence of intermediate steps, or a reasoning trajectory, to solve a problem.

**Intermediate reasoning generation** (2 papers: [Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf), [TurnaboutLLM: A Deductive Reasoning Benchmark from Detective Games](https://aclanthology.org/2025.emnlp-main.101.pdf))
> The behavior of generating an explicit reasoning paragraph that identifies relevant passages and explains the rationale before producing the final answer.

**Reasoning chain generation** (2 papers: [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf), [Thinking Out Loud: Do Reasoning Models Know When They're Right?](https://aclanthology.org/2025.emnlp-main.73.pdf))
> The observable behavior of producing a step-by-step textual explanation that details the logic leading to a specific prediction.

**Stepwise reasoning** (2 papers: [Training Large Language Models for Retrieval-Augmented Question Answering through Backtracking Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/80790082a3b0e4fa9061730ee876f5ba-Paper-Conference.pdf), [How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark](https://aclanthology.org/2025.emnlp-main.674.pdf))
> The behavior of generating a sequence of intermediate analytical steps or reasoning chains before producing a final answer, particularly when processing multiple documents.

**Intermediate step generation** (1 paper: [How Far Can Transformers Reason? The Globality Barrier and Inductive Scratchpad](https://proceedings.neurips.cc/paper_files/paper/2024/file/3107e4bdb658c79053d7ef59cbc804dd-Paper-Conference.pdf))
> The observable behavior of a model generating a sequence of intermediate computations or reasoning steps (a scratchpad) before producing a final answer.

**Chain-of-thought computation** (1 paper: [On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf))
> The observable behavior of generating a series of intermediate reasoning steps before producing a final answer.

**Hierarchical thought generation** (1 paper: [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf))
> The generation of a structured reasoning process that includes both a high-level, generalized solution template and a detailed, step-by-step explanation of critical steps.

**Multi-branch reasoning** (1 paper: [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf))
> The process of generating multiple, distinct reasoning trajectories from a single prompt or intermediate state.

**Search trajectory verbalization** (1 paper: [System 1.x: Learning to Balance Fast and Slow Planning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/605e59e78284907aa4fce5280838def3-Paper-Conference.pdf))
> Outputting a step-by-step textual representation of explored states and actions during search.

**Chain-of-thought inference** (1 paper: [Training Nonlinear Transformers for Chain-of-Thought Inference: A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf))
> Generating stepwise reasoning outputs for a query when the prompt includes examples with intermediate steps.

**Reasoning chain construction** (1 paper: [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf))
> Iteratively building a sequence of logically connected knowledge triples that support answering a given question.

**Inner monologue generation** (1 paper: [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ae/xu25ae.pdf))
> Producing explicit, intermediate reasoning steps in natural language that reflect the agent’s thought process before taking actions.

**Reasoning context generation** (1 paper: [Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25at/yang25at.pdf))
> Producing step-by-step logical justifications or intermediate reasoning steps for question-answer pairs, enriching the knowledge base with explainable inference patterns.

**Silent chain-of-thought generation** (1 paper: [On the Power of Context-Enhanced Learning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25p/zhu25p.pdf))
> The model's production of a fixed number of <THINK> tokens during output, simulating internal reasoning without explicit intermediate steps in the final answer.

**Explicit Chain-of-Thought generation** (1 paper: [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36.pdf))
> The observable behavior of generating intermediate reasoning steps in natural language before providing a final answer.

**Intermediate instruction generation** (1 paper: [Large Language Models as Realistic Microservice Trace Generators](https://aclanthology.org/2025.emnlp-main.4.pdf))
> The observable behavior of explicitly generating natural language reasoning steps, such as arithmetic and logical checks, between generation stages to ensure constraint adherence.

**Reasoning step generation** (1 paper: [NOVER: Incentive Training for Language Models via Verifier-Free Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.378.pdf))
> Producing intermediate reasoning tokens (e.g., justifications, decompositions) before arriving at a final answer, often enclosed in specific tags.

**Logic generation** (1 paper: [AQuilt: Weaving Logic and Self-Inspection into Low-Cost, High-Relevance Data Synthesis for Specialist LLMs](https://aclanthology.org/2025.emnlp-main.293.pdf))
> Producing intermediate reasoning steps that justify the answer to a question, based on unlabeled input and task type.

**Step-by-step execution** (1 paper: [Metric Calculating Benchmark: Code-Verifiable Complicate Instruction Following Benchmark for Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf))
> The observable behavior of generating a sequence of intermediate outputs that follow a prescribed procedural rubric, including tokenization, n-gram generation, and numerical computation.

**Structured response generation** (1 paper: [Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens](https://aclanthology.org/2025.emnlp-main.171.pdf))
> The behavior of generating a response that is segmented into logically discrete reasoning steps, often marked by transitional phrases like "Step 1:", "Step 2:", etc.

**Continuous thought generation** (1 paper: [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36.pdf))
> Autoregressively generating a sequence of continuous latent representations as intermediate reasoning steps before producing an answer.

**Structured chain-of-thought generation** (1 paper: [Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.1216.pdf))
> Producing explicit multi-step reasoning traces before the final answer, often with labeled planning, captioning, reasoning, and summary sections.

**Natural language chain-of-thought generation** (1 paper: [Parrot: A Training Pipeline Enhances Both Program CoT and Natural Language CoT for Reasoning](https://aclanthology.org/2025.emnlp-main.1366.pdf))
> The observable behavior of producing a step-by-step reasoning rationale in natural language to solve a problem.

**Program chain-of-thought generation** (1 paper: [Parrot: A Training Pipeline Enhances Both Program CoT and Natural Language CoT for Reasoning](https://aclanthology.org/2025.emnlp-main.1366.pdf))
> Generating executable code snippets that represent the reasoning steps for solving a mathematical problem, which can be verified by an interpreter.

**Chain-of-Thought Reasoning** (1 paper: [Predicting Emergent Abilities with Infinite Resolution Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e6d14709eae0cbc49a1d19d87fb8b21-Paper-Conference.pdf))
> Generating intermediate reasoning steps before producing a final answer, often used to improve performance on complex reasoning tasks.

**Intermediate token generation** (1 paper: [The Expressive Power of Transformers with Chain of Thought](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f59721c106ea80f613299039112f651-Paper-Conference.pdf))
> The observable action of a model producing a sequence of intermediate computational steps or "thoughts" before outputting a final answer.

**Reasoned explanation generation** (1 paper: [Language Models are Crossword Solvers](https://aclanthology.org/2025.naacl-long.104.pdf))
> Producing step-by-step justifications for answers to cryptic clues, particularly using chain-of-thought prompting.

**Multi-step reasoning** (4 papers: [CER: Confidence Enhanced Reasoning in LLMs](https://aclanthology.org/2025.acl-long.390.pdf), [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.622.pdf), [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf), [S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.475.pdf))
> A reasoning process that breaks down a problem into a sequence of explicit intermediate steps or thoughts to reach a final solution.

**Step-wise reasoning** (2 papers: [Progressive Multimodal Reasoning via Active Retrieval](https://aclanthology.org/2025.acl-long.180.pdf), [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.577.pdf))
> Generating a sequence of intermediate logical steps leading to a final answer, often in the form of structured explanations or derivations.

## Relationships

### Chain of thought →
- **Reasoning** (construct): *causes*, 21 papers
  > This suggests that reasoning improvements from PPO may be due to increased chain-of-thought abilities. (Section 3.2).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Iterative Reasoning Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/d37c9ad425fe5b65304d500c6edcba00-Paper-Conference.pdf)
  - [OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/85f1225db986e629289f402c46eff1a4-Paper-Conference.pdf)
  - [Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf)
  - [Reasoning with Latent Thoughts: On the Power of Looped Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/2676109d49d1eb26d6bc584a8f556305-Paper-Conference.pdf)
  - [ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2025/file/9c77f2ce42151b2c2e26d2cf47f99564-Paper-Conference.pdf)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
  - [Automatic Curriculum Expert Iteration for Reliable LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9083c94382509473bdf5fc2672fc72b3-Paper-Conference.pdf)
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.584.pdf)
  - [RATIONALYST: Pre-training Process-Supervision for Improving Reasoning](https://aclanthology.org/2025.acl-long.1288.pdf)
  - [SoftCoT: Soft Chain-of-Thought for Efficient Reasoning with LLMs](https://aclanthology.org/2025.acl-long.1137.pdf)
  - [Nudging: Inference-time Alignment of LLMs via Guided Decoding](https://aclanthology.org/2025.acl-long.623.pdf)
  - [TokenSkip: Controllable Chain-of-Thought Compression in LLMs](https://aclanthology.org/2025.emnlp-main.165.pdf)
  - [DART: Distilling Autoregressive Reasoning to Silent Thought](https://aclanthology.org/2025.emnlp-main.256.pdf)
  - [Taking Notes Brings Focus? Towards Multi-Turn Multimodal Dialogue Learning](https://aclanthology.org/2025.emnlp-main.1690.pdf)
  - [Prior Prompt Engineering for Reinforcement Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1590.pdf)
  - [Steering LLM Reasoning Through Bias-Only Adaptation](https://aclanthology.org/2025.emnlp-main.467.pdf)
  - [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 8 papers
  > "tasks involving chain-of-thought (Wei et al., 2022b) reasoning: StrategyQA (Geva et al., 2021) and GSM8K Cobbe et al. (2021)"
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
  - [An Empirical Study of LLM Reasoning Ability Under Strict Output Length Constraint](https://aclanthology.org/2025.emnlp-main.389.pdf)
  - [Expanding before Inferring: Enhancing Factuality in Large Language Models through Premature Layers Interpolation](https://aclanthology.org/2025.emnlp-main.645.pdf)
- **Mathematical reasoning** (construct): *causes*, 7 papers
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [CoTFormer: A Chain of Thought Driven Architecture with Budget-Adaptive Computation Cost at Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf)
  - [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf)
  - [An Efficient and Precise Training Data Construction Framework for Process-supervised Reward Model in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.216.pdf)
  - [Can LLMs Help Uncover Insights about LLMs? A Large-Scale, Evolving Literature Analysis of Frontier LLMs](https://aclanthology.org/2025.acl-long.998.pdf)
  - [RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b77d5b896c321a29277524a98a50215-Paper-Conference.pdf)
  - [Understanding Chain-of-Thought in LLMs through Information Theory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ton25a/ton25a.pdf)
- **Interpretability and explainability** (construct): *causes*, 5 papers
  > We leverage the augmented patient context to enable LLMs to generate step-by-step reasoning chains, enhancing both interpretability and prediction accuracy in clinical tasks. (Section 1)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
  - [MolRAG: Unlocking the Power of Large Language Models for Molecular Property Prediction](https://aclanthology.org/2025.acl-long.755.pdf)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
  - [RTQA : Recursive Thinking for Complex Temporal Knowledge Graph Question Answering with Large Language Models](https://aclanthology.org/2025.emnlp-main.499.pdf)
  - [DSG-MCTS: A Dynamic Strategy-Guided Monte Carlo Tree Search for Diversified Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.532.pdf)
- **Mathematical problem solving** (behavioral indicator): *causes*, 5 papers
  > The seminal work of chain-of-thought (CoT) (Wei et al., 2022) is an excellent example of how enriching reasoning details, by decomposing reasoning traces into steps, improves its problem-solving capability (Section 1).
  - [Think Smarter not Harder: Adaptive Reasoning with Inference Aware Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25s/yu25s.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
  - [Enhancing Chain-of-Thought Reasoning via Neuron Activation Differential Analysis](https://aclanthology.org/2025.emnlp-main.817.pdf)
  - [Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/c239bac713017b0b2257b7622bf8aab3-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct): *causes*, 4 papers
  > Large language models are capable of solving tasks that require complex multi-step reasoning by generating solutions in a step-by-step chain-of-thought format (Section 1).
  - [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf)
  - [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf)
  - [Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf)
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 3 papers
  > "tasks involving chain-of-thought (Wei et al., 2022b) reasoning: StrategyQA (Geva et al., 2021) and GSM8K Cobbe et al. (2021)"
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [Expanding before Inferring: Enhancing Factuality in Large Language Models through Premature Layers Interpolation](https://aclanthology.org/2025.emnlp-main.645.pdf)
- **Answer generation** (behavioral indicator): *causes*, 3 papers
  > Extracting reasoning chains from multi-document artefacts can help contextualize curated evidence for final answer generation.
  - [VisDoM: Multi-Document QA with Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.310.pdf)
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.584.pdf)
  - [From Reasoning to Answer: Empirical, Attention-Based and Mechanistic Insights into Distilled DeepSeek R1 Models](https://aclanthology.org/2025.emnlp-main.198.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > For evaluating intermediate reasoning steps, we randomly select 200 samples and use a strong reasoning model, OpenAI-o3, to identify any errors within the reasoning process (Section 3.3).
  - [Code Execution as Grounded Supervision for LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1260.pdf)
  - [SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas](https://aclanthology.org/2025.emnlp-main.1716.pdf)
- **Expressive power** (construct): *causes*, 2 papers
  > we demonstrate that functions computed by Automata, Turing machines, or sparse circuits can be emulated by an ARDT using these intermediate “chain-of-thought” computations. (Section 3)
  - [On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf)
  - [Lower Bounds for Chain-of-Thought Reasoning in Hard-Attention Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bavandpour25a/bavandpour25a.pdf)
- **Symbolic reasoning** (construct): *causes*, 2 papers
  > The three categories which benefited the most from CoT are symbolic reasoning, math, and logical reasoning, with average improvements of 14.2, 12.3, 6.9, respectively. (Section 3)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [Can LLMs Help Uncover Insights about LLMs? A Large-Scale, Evolving Literature Analysis of Frontier LLMs](https://aclanthology.org/2025.acl-long.998.pdf)
- **In-context learning** (construct): *causes*, 2 papers
  > The foundational method for inducing in-context learning is the chain of thought approach
  - [Chain of Thoughtlessness? An Analysis of CoT in Planning](https://proceedings.neurips.cc/paper_files/paper/2024/file/3365d974ce309623bd8151082d78206c-Paper-Conference.pdf)
  - [Linear-Time Demonstration Selection for In-Context Learning via Gradient Estimation](https://aclanthology.org/2025.emnlp-main.832.pdf)
- **Logical reasoning** (construct): *causes*, 2 papers
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [Understanding Chain-of-Thought in LLMs through Information Theory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ton25a/ton25a.pdf)
- **Hallucination** (behavioral indicator): *causes*, 2 papers
  > Asking the Constructor to complete the whole chain reduces hallucination, and avoids a sub-optimal greedy approach. (Section 3.2)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)
  - [Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594.pdf)
- **Exploration** (behavioral indicator): *causes*, 1 paper
  > The single configuration that succeeds in our experiments involves a combination of GPT-4 and an “enhanced” prompt that (a) provides a suggestive hint to explore, (b) externally summarizes the history of interaction into per-arm averages, and (c) asks the LLM to use zero-shot chain-of-thought reasoning [74, 41]. (Introduction)
  - [Can large language models explore in-context?](https://proceedings.neurips.cc/paper_files/paper/2024/file/d951f73c521d069fefbb73396df01424-Paper-Conference.pdf)
- **Algorithmic reasoning** (construct): *causes*, 1 paper
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **MathVerse** (measurement instrument): *measured_by*, 1 paper
  > As shown in Table 1 for the MathVerse benchmark, MAVIS-7B achieves the best overall scores in both CoT evaluation and accuracy among open-source MLLMs... (Section 4.2)
  - [MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine](https://proceedings.iclr.cc/paper_files/paper/2025/file/db36dcad6baee298a34ffca324b84b09-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > To examine how retrieval heads effect reasoning tasks, we test Mistrial-7B-Instruct-v0.2 on MMLU (Hendrycks et al., 2020), MuSiQue and GSM8K (Cobbe et al., 2021), with and without chain-of-thought (CoT) reasoning. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **MuSiQue** (measurement instrument): *measured_by*, 1 paper
  > To examine how retrieval heads effect reasoning tasks, we test Mistrial-7B-Instruct-v0.2 on MMLU (Hendrycks et al., 2020), MuSiQue and GSM8K (Cobbe et al., 2021), with and without chain-of-thought (CoT) reasoning. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > “Human evaluation of KARE-generated reasoning chains is presented in Appendix H.”
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Reward hacking** (behavioral indicator): *causes*, 1 paper
  > Our analysis shows that CoT reasoning is crucial for unlocking DPO’s potential, as it mitigates reward hacking... (Abstract)
  - [Uncovering the Impact of Chain-of-Thought Reasoning for Direct Preference Optimization: Lessons from Text-to-SQL](https://aclanthology.org/2025.acl-long.1031.pdf)
- **AIME** (measurement instrument): *measured_by*, 1 paper
  > We assess both models on the challenging American Invitational Mathematics Examination (AIME 24) benchmark. (Section 3.3, Chain-of-Thought Reasoning Evaluation).
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
- **Molecular property prediction** (behavioral indicator): *causes*, 1 paper
  > Chain-of-Thought (CoT) improves the reasoning ability of LLMs in molecular property prediction by decomposing complex SMILES data processing into stepwise sub-tasks, overcoming the limitations of direct question-answering approaches. (Section 3.3)
  - [MolRAG: Unlocking the Power of Large Language Models for Molecular Property Prediction](https://aclanthology.org/2025.acl-long.755.pdf)
- **Groundedness** (construct): *causes*, 1 paper
  > ...we instruct the LLM to generate a chain-of-knowledge (CoK) (Wang et al., 2024a), where free-form thoughts are replaced with document-grounded knowledge triples to ensure factual reliability. (Section 3.2)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)
- **Backtracking** (behavioral indicator): *causes*, 1 paper
  > we prove by construction that decoder-only Transformers can decide 3-SAT, in a non-uniform model of computation, using backtracking and deduction via Chain-of-Thought (CoT). (Section 1)
  - [Can Transformers Reason Logically? A Study in SAT Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25d/pan25d.pdf)
- **Task generalization** (construct): *causes*, 1 paper
  > In contrast, we found that incorporating Chain-of-Thought (CoT) reasoning — adding intermediate reasoning steps to the prompt — allows Transformers to easily generalize to unseen tasks. (Section 1)
  - [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf)
- **Parity checking** (behavioral indicator): *causes*, 1 paper
  > Transformers empirically struggle to learn it on longer inputs (e.g. Bhattamishra et al., 2020a; Del´etang et al., 2023; Butoi et al., 2024; Hahn & Rofin, 2024), and this difficulty is resolved by a CoT consisting of the parities of increasing prefixes, as in Figure 1 (e.g. Anil et al., 2022). (Section 1)
  - [Lower Bounds for Chain-of-Thought Reasoning in Hard-Attention Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bavandpour25a/bavandpour25a.pdf)
- **Overthinking** (behavioral indicator): *causes*, 1 paper
  > However, this approach [chain-of-thought (CoT) reasoning] often leads to unnecessarily long and verbose reasoning traces, resulting in high inference cost and latency. This overthinking phenomenon has become a practical bottleneck... (Introduction)
  - [Answer Convergence as a Signal for Early Stopping in Reasoning](https://aclanthology.org/2025.emnlp-main.904.pdf)
- **Dialogue state tracking** (behavioral indicator): *causes*, 1 paper
  > The results in Table 4 show that incorporating the CoT from Step 1 provides an approximately 10% improvement in zero-shot accuracy by offering a more robust representation for each turn. (Section 4.6)
  - [From Schema to State: Zero-Shot Scheme-Only Dialogue State Tracking via Diverse Synthetic Dialogue and Step-by-Step Distillation](https://aclanthology.org/2025.emnlp-main.85.pdf)
- **Machine translation** (behavioral indicator): *causes*, 1 paper
  > both models approach 0% accuracy on multi-hop translations when CoT is disabled, indicating the necessity of CoT on SYNC.
  - [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf)
- **Problem solving** (behavioral indicator): *causes*, 1 paper
  > Another line of work has shown that allowing LLMs to generate intermediate “reasoning” steps, or “chain-of-thoughts” (CoTs) can significantly improve their final answer (Wei et al., 2022; Nye et al., 2021; Zhou et al., 2023). (Section 5)
  - [Learning How Hard to Think: Input-Adaptive Allocation of LM Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf)

### → Chain of thought
- **Instruction following ability** (construct): *causes*, 1 paper
  > When a model struggles to follow instructions accurately, generating CoT explanations becomes more difficult. (Section 3.3)
  - [MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](https://aclanthology.org/2025.acl-long.736.pdf)
- **Mathematical problem solving** (behavioral indicator): *causes*, 1 paper
  > we task the LIMS method with enabling a model to behave with chain-of-thought generation when a math problem is sensed, following “math(x) →chain of thought(x)”. (Section 4.1)
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
- **Context retrieval** (behavioral indicator): *causes*, 1 paper
  > CoT reasoning, which involves decomposing complex tasks into smaller steps, heavily depends on accurately retrieving detailed information from the input. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)

### Associated with
- **System 2 thinking** (construct), 2 papers
  > In fast mode, a Transformer will output a final solution without any reasoning steps, whereas the intermediate steps of thinking, such as a search trace for finding a short path, will be generated along with the plan in slow mode. (Section 1)
  - [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [What Happened in LLMs Layers when Trained for Fast vs. Slow Thinking: A Gradient Perspective](https://aclanthology.org/2025.acl-long.1545.pdf)
- **Explanation generation** (behavioral indicator), 1 paper
  > Zelikman et al. (2022) introduced the the Self-Taught Reasoners method, used rationalization to generate chain-of-thought (CoT) reasoning (Sec. 5.2).
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
- **Tool use** (behavioral indicator), 1 paper
  > we opt for the framework of the ReAct agent that performs step-by-step reasoning for tool usage... In each step, the agent generates thought and corresponding code to execute tools.
  - [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf)
- **Compositional reasoning** (construct), 1 paper
  > “This format includes step-by-step operations and intermediate results, allowing the model to learn the individual components of compositional tasks.”
  - [Teaching Arithmetic to Small Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Pattern matching** (construct), 1 paper
  > hint that basic pattern matching rather than in context learning of general algorithmic procedures may better explain the improvements seen from chain of thought.
  - [Chain of Thoughtlessness? An Analysis of CoT in Planning](https://proceedings.neurips.cc/paper_files/paper/2024/file/3365d974ce309623bd8151082d78206c-Paper-Conference.pdf)
- **G-Eval** (measurement instrument), 1 paper
  > Furthermore, we report G-EVAL (Liu et al., 2023a), an auto-CoT prompting framework, and the current state-of-the-art in NLG evaluation. (Section 5.1)
  - [CSEval: Towards Automated, Multi-Dimensional, and Reference-Free Counterspeech Evaluation using Auto-Calibrated LLMs](https://aclanthology.org/2025.naacl-long.279.pdf)
- **Safety reasoning** (construct), 1 paper
  > “We enable LLMs to identify safety risks through step-by-step analysis by self-improving chain-of-thought (CoT) reasoning with safety awareness.”
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **lm-evaluation-harness** (measurement instrument), 1 paper
  > We use a fork of EleutherAI's LM Evaluation Harness with minor modiﬁcations. We use the default settings for evaluation, except for increasing the maximum number of allowed generated tokens from 256 to 1000, as we notice that the default setting did not allow some models to complete their full chain-of-thought reasoning before being truncated.
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MathGAP** (measurement instrument), 1 paper
  > "MathGAP generates problem statements and chain-of-thought reasoning traces according to specifications about their arithmetic proof structure"
  - [MathGAP: Out-of-Distribution Evaluation on Problems with Arbitrarily Complex Proofs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9c2ab8d429044e0c35bcece2ff6d123-Paper-Conference.pdf)
- **Zero-shot inference** (behavioral indicator), 1 paper
  > “Zero-shot with Chain-of-Thought (CoT) incorporates CoT reasoning prompts to generate intermediate reasoning steps before the final answer”
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > training LLMs to generate code first and then output the CoT to explain reasoning steps for code generation is more effective. (Abstract)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **Latent reasoning** (construct), 1 paper
  > DART (Distilling Autoregressive Reasoning to Silent Thought), a novel framework that enables the LLMs to internalize the autoregressive CoT into non-autoregressive Silent Thought (ST) with an excellent efficiency-efficacy trade-off. (Section 1)
  - [DART: Distilling Autoregressive Reasoning to Silent Thought](https://aclanthology.org/2025.emnlp-main.256.pdf)
- **Privacy leakage** (behavioral indicator), 1 paper
  > it has been shown in (Jiang et al., 2025; Wu et al., 2025) that reasoning traces can carry more sensitive information than final answers (Section 2)
  - [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf)
- **LASER** (measurement instrument), 1 paper
  > "Promote step-by-step reasoning: We promoted chain-of-thought reasoning by asking the LLM to return its response in the format: (Word count of original sentence; list of non-penalizable errors; list of major penalizable errors; list of minor penalizable errors; total penalty; score)."
  - [LASER: An LLM-based ASR Scoring and Evaluation Rubric](https://aclanthology.org/2025.emnlp-main.1257.pdf)
