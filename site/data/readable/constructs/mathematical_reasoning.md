# Mathematical reasoning
**Type:** Construct  
**Supporting papers:** 601  
**Also known as:** Arithmetic reasoning, Algebraic manipulation, Math reasoning, Multi-step math reasoning, Numerical reasoning, Mathematical ability, Quantitative reasoning, Mathematical Reasoning, Mathematical capability, Mathematical problem-solving, Mathematical intelligence, Asymptotic reasoning, Mathematical understanding, Arithmetic ability, Numeric reasoning, Arithmetic computation capability, Mathematical world-model, Math knowledge, Multistep mathematical reasoning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats mathematical reasoning as a latent model ability to solve mathematical problems through rigorous, stepwise logic, usually combining numerical calculation with multi-step deduction. Most definitions ground it in math word problems or natural-language prompts, often at grade-school or arithmetic level, while a smaller line broadens it to symbolic manipulation, theorem proving, geometry, statistics, optimization, visual contexts, or formal and informal mathematical content. The main variation is between broad latent capacity and narrower task framings: some papers describe the observable solving of problems or production of correct multi-step answers, while a few recast it as mathematical intelligence, a mathematical world-model, or benchmark-reflected math knowledge.

**Space of facets.** Papers divide the construct into nearby facets such as arithmetic, numerical, quantitative, multistep, and algebraic reasoning, and some isolate narrower abilities such as asymptotic reasoning or arithmetic computation within a larger reasoning process. Other uses extend it to formal proof construction, optimization modeling, and visual mathematical reasoning over geometry, counting, comparison, or spatial relations. Terminology overlaps heavily, with mathematical reasoning used alongside math reasoning, mathematical ability, mathematical capability, mathematical understanding, and mathematical problem-solving, while a few papers place it next to broader notions such as mathematical intelligence, a mathematical world-model, or math knowledge; one paper also decomposes natural-language mathematical CoT into step planning and step calculation.

**Space of measurement.** Operationalization is dominated by benchmark performance: papers link mathematical reasoning to 65 measurement instruments, most often GSM8K, MATH, SVAMP, AQuA-RAT, and MATH-500. These instruments are mainly dataset-based evaluations of grade-school and arithmetic word problems, broader competition or exam mathematics, and out-of-domain variants, but they also include multilingual benchmarks such as MGSM, visual math benchmarks such as MathVista, and formal mathematics benchmarks such as miniF2F. Mathematical reasoning is also linked to 12 behavioral indicators, led by Chain of thought, Formal theorem proving, Backward reasoning, Code generation, and Data analysis; overall, the measurements usually match definitions that stress multi-step problem solving, while also extending the construct to visual, multilingual, spoken, table-based, and formal-proof settings.

**Links.** Several papers claim a causal relationship from Chain of thought to mathematical reasoning, and a smaller line makes the same kind of claim from Formal theorem proving, Coding ability, and other linked behaviors or constructs. Mathematical reasoning is reported to correlate with Reasoning, and Complex reasoning is related to mathematical reasoning. Papers also report many additional causal, correlational, and related links, including to memorization, planning, table or textual reasoning, autoformalization, and tool use.

## Sources

**Arithmetic reasoning** (3 papers: [Localized Zeroth-Order Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cef1316eaef9bd99da46f63334dc031-Paper-Conference.pdf), [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chu25c/chu25c.pdf), [Knowledge Editing through Chain-of-Thought](https://aclanthology.org/2025.emnlp-main.540.pdf))
> Solving mathematical word problems that require understanding the text and performing arithmetic calculations.

**Algebraic manipulation** (1 paper: [CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf))
> Manipulating symbolic or mathematical expressions to derive or simplify scientific results.

**Mathematical reasoning** (4 papers: [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf), [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf), [Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf), [SDGO: Self-Discrimination-Guided Optimization for Consistent Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.253.pdf))
> Solving math problems that require rigorous logic and stepwise computation.

**Math reasoning** (2 papers: [Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf), [Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance](https://aclanthology.org/2025.emnlp-main.500.pdf))
> Solving grade-school math problems that require intermediate reasoning steps before giving a final answer.

**Multi-step math reasoning** (1 paper: [Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4006ff54a7bbda74c09bad6f7586f5b-Paper-Conference.pdf))
> Solving mathematical problems that require multiple intermediate reasoning steps before producing an answer.

**Numerical reasoning** (2 papers: [From Few to Many: Self-Improving Many-Shot Reasoners Through Iterative Optimization and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f22dfaee68dd71f784a82a684b4404bb-Paper-Conference.pdf), [LightThinker: Thinking Step-by-Step Compression](https://aclanthology.org/2025.emnlp-main.673.pdf))
> Solving problems that require arithmetic or quantitative inference from text.

**Quantitative reasoning** (3 papers: [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf), [OpenWebMath: An Open Dataset of High-Quality Mathematical Web Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf), [Regress, Don’t Guess: A Regression-like Loss on Number Tokens for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zausinger25a/zausinger25a.pdf))
> The latent ability of a model to understand and solve mathematical problems, particularly those presented in natural language that require numerical and logical steps.

**Mathematical ability** (6 papers: [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf), [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf), [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf), [Redundancy Principles for MLLMs Benchmarks](https://aclanthology.org/2025.acl-long.612.pdf), [Attention-Level Speculation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cai25g/cai25g.pdf), [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://aclanthology.org/2025.emnlp-main.167.pdf))
> The latent ability to solve arithmetic and word problems and handle math-oriented prompts correctly.

**Mathematical Reasoning** (1 paper: [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf))
> The capability to solve mathematical and logic-based problems requiring step-by-step deduction.

**Mathematical problem-solving** (1 paper: [Token-Supervised Value Models for Enhancing Mathematical Problem-Solving Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0801fccb1d705a9e6747e138d9a0056a-Paper-Conference.pdf))
> The latent ability to solve math word problems by producing correct multi-step reasoning and final answers.

**Mathematical capability** (2 papers: [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf), [Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law](https://aclanthology.org/2025.acl-long.1157.pdf))
> The model's ability to solve mathematical problems, particularly those requiring arithmetic and logical steps.

**Asymptotic reasoning** (1 paper: [HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf))
> The model's ability to find approximate analytical solutions to complex mathematical problems by analyzing their behavior in limiting cases, such as when a parameter is very large or very small.

**Mathematical intelligence** (1 paper: [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf))
> The broader latent quality reflected by benchmark performance that is intended to track genuine mathematical ability more faithfully and linearly than traditional tests.

**Mathematical understanding** (1 paper: [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf))
> The latent capability to solve grade-school math problems that require multi-step numerical reasoning.

**Arithmetic ability** (1 paper: [A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf))
> The capacity to solve grade-school or similar numerical computation problems.

**Numeric reasoning** (1 paper: [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to extract numerical information from product metadata and perform calculations to answer questions.

**Arithmetic computation capability** (1 paper: [MedCalc-Bench: Evaluating Large Language Models for Medical Calculations](https://proceedings.neurips.cc/paper_files/paper/2024/file/99e81750f3fdfcaf9613db2dbf4bd623-Paper-Datasets_and_Benchmarks_Track.pdf))
> The model's underlying ability to perform mathematical operations like addition, subtraction, and exponentiation correctly as part of a larger reasoning process.

**Mathematical world-model** (1 paper: [Can Transformers Do Enumerative Geometry?](https://proceedings.iclr.cc/paper_files/paper/2025/file/aee2f03ecb2b2c1ea55a43946b651cfd-Paper-Conference.pdf))
> An internalized, coherent understanding of mathematical concepts, relationships, and structures that goes beyond surface-level pattern matching.

**Math knowledge** (1 paper: [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf))
> The extent of an LLM's competence on math-related content, as reflected by performance patterns across math benchmarks.

**Multistep mathematical reasoning** (1 paper: [Training on the Test Task Confounds Evaluation and Emergence](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab8c971c2ccd12bac0ab249f75e2c16d-Paper-Conference.pdf))
> The latent ability to perform a sequence of logical and mathematical steps to arrive at a solution for a quantitative problem.

## Relationships

### Mathematical reasoning →
- **GSM8K** (measurement instrument): *measured_by*, 235 papers
  > We evaluate DTV on three quantitative reasoning datasets: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021) and MultiArith (Roy & Roth, 2016).
  - [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf)
  - [MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/15425f2df99aa1ba52712c9a4afc8536-Paper-Conference.pdf)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
  - [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c400474e8a36d0812fdee52739288b12-Paper-Conference.pdf)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
  - [BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf)
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
  - [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf)
  - [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf)
  - [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf)
  - [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf)
  - [Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL](https://proceedings.iclr.cc/paper_files/paper/2024/file/b84b9d1fe05c5e74d8f9466f063327a5-Paper-Conference.pdf)
  - [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf)
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
  - [OpenWebMath: An Open Dataset of High-Quality Mathematical Web Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf)
  - [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](https://proceedings.neurips.cc/paper_files/paper/2024/file/f5198bc255e1d5f959edd6d1d1a86fab-Paper-Conference.pdf)
  - [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Parameter Competition Balancing for Model Merging](https://proceedings.neurips.cc/paper_files/paper/2024/file/99fc8bc48b917c301a80cb74d91c0c06-Paper-Conference.pdf)
  - [VB-LoRA: Extreme Parameter Efficient Fine-Tuning with Vector Banks](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e0d38c676d5855bcfab7f6d29d20ad9-Paper-Conference.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [Metacognitive Capabilities of LLMs: An Exploration in Mathematical Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/2318d75a06437eaa257737a5cf3ab83c-Paper-Conference.pdf)
  - [On Giant's Shoulders: Effortless Weak to Strong by Dynamic Logits Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/34ec1286b2ccd4794c5ca4ad078b7150-Paper-Conference.pdf)
  - [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf)
  - [Instance-adaptive Zero-shot Chain-of-Thought Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/e304e04a6f455dd82f8a85a0a3679493-Paper-Conference.pdf)
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
  - [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
  - [Localized Zeroth-Order Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cef1316eaef9bd99da46f63334dc031-Paper-Conference.pdf)
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
  - [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf)
  - [LoQT: Low-Rank Adapters for Quantized Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0c6bc641a56bebee9d985b937307367-Paper-Conference.pdf)
  - [Unchosen Experts Can Contribute Too: Unleashing MoE Models’ Power by Self-Contrast](https://proceedings.neurips.cc/paper_files/paper/2024/file/f77012b463892a3f2ac56d3a6086fc5b-Paper-Conference.pdf)
  - [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf)
  - [Learning from Teaching Regularization: Generalizable Correlations Should be Easy to Imitate](https://proceedings.neurips.cc/paper_files/paper/2024/file/01ce1ae7f94d139e4917f9e4425a4f38-Paper-Conference.pdf)
  - [AutoPSV: Automated Process-Supervised Verifier](https://proceedings.neurips.cc/paper_files/paper/2024/file/9246aa822579d9b29a140ecdac36ad60-Paper-Conference.pdf)
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [ReMI: A Dataset for Reasoning with Multiple Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ea56c0baacac9f7764257a43a93c90a-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Toward Self-Improvement of LLMs via Imagination, Searching, and Criticizing](https://proceedings.neurips.cc/paper_files/paper/2024/file/5e5853f35164e434015716a8c2a66543-Paper-Conference.pdf)
  - [SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf)
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
  - [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf)
  - [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/bea94fe9c5573e74294657f692069d89-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [B-STaR: Monitoring and Balancing Exploration and Exploitation in Self-Taught Reasoners](https://proceedings.iclr.cc/paper_files/paper/2025/file/c8db30c6f024a3f667232ed7ba5b6d47-Paper-Conference.pdf)
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
  - [The Unreasonable Ineffectiveness of the Deeper Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbabc2f70de2dd09f491a8715ec3e80f-Paper-Conference.pdf)
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
  - [Scaling up Masked Diffusion Models on Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce1c1ff5d94079dea348a2317a889281-Paper-Conference.pdf)
  - [DARE the Extreme: Revisiting Delta-Parameter Pruning For Fine-Tuned Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0074bea472f8b9b839fa2d50ce67595-Paper-Conference.pdf)
  - [A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf)
  - [WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c04aea54c2a60a632a47bd451cd2849-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
  - [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
  - [Balancing Act: Diversity and Consistency in Large Language Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5554e55d7a21e62d0d7a028ec0ea1c7-Paper-Conference.pdf)
  - [Training on the Test Task Confounds Evaluation and Emergence](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab8c971c2ccd12bac0ab249f75e2c16d-Paper-Conference.pdf)
  - [MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/abbbb25cddb2c2cd08714e6bfa2f0634-Paper-Conference.pdf)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf)
  - [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf)
  - [MathGAP: Out-of-Distribution Evaluation on Problems with Arbitrarily Complex Proofs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9c2ab8d429044e0c35bcece2ff6d123-Paper-Conference.pdf)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf)
  - [Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3064f7a0ca2328ecb41a3aef6177d68-Paper-Conference.pdf)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbc461518c59a2a8d64e70e2c38c4a0e-Paper-Conference.pdf)
  - [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf)
  - [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf)
  - [ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2025/file/9c77f2ce42151b2c2e26d2cf47f99564-Paper-Conference.pdf)
  - [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
  - [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf)
  - [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
  - [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf)
  - [UGMathBench: A Diverse and Dynamic Benchmark for Undergraduate-Level Mathematical Reasoning with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c3af3531df85264decc31382cb319781-Paper-Conference.pdf)
  - [Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4006ff54a7bbda74c09bad6f7586f5b-Paper-Conference.pdf)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
  - [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf)
  - [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
  - [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf)
  - [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf)
  - [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf)
  - [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf)
  - [Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning](https://aclanthology.org/2025.naacl-long.519.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf)
  - [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf)
  - [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf)
  - [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf)
  - [Self-Pluralising Culture Alignment for Large Language Models](https://aclanthology.org/2025.naacl-long.350.pdf)
  - [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf)
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)
  - [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf)
  - [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf)
  - [S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.475.pdf)
  - [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf)
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.584.pdf)
  - [Fusing Highly Specialized Language Models for Comprehensive Expertise](https://aclanthology.org/2025.acl-long.42.pdf)
  - [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.503.pdf)
  - [RATIONALYST: Pre-training Process-Supervision for Improving Reasoning](https://aclanthology.org/2025.acl-long.1288.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [From Informal to Formal – Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs](https://aclanthology.org/2025.acl-long.1310.pdf)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [ScaleBiO: Scalable Bilevel Optimization for LLM Data Reweighting](https://aclanthology.org/2025.acl-long.1543.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
  - [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf)
  - [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
  - [YuLan-Mini: Pushing the Limits of Open Data-efficient Language Model](https://aclanthology.org/2025.acl-long.268.pdf)
  - [Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law](https://aclanthology.org/2025.acl-long.1157.pdf)
  - [How to Mitigate Overfitting in Weak-to-strong Generalization?](https://aclanthology.org/2025.acl-long.784.pdf)
  - [Unleashing LLM Reasoning Capability via Scalable Question Synthesis from Scratch](https://aclanthology.org/2025.acl-long.658.pdf)
  - [Pretraining Context Compressor for Large Language Models with Embedding-Based Memory](https://aclanthology.org/2025.acl-long.1394.pdf)
  - [DavIR: Data Selection via Implicit Reward for Large Language Models](https://aclanthology.org/2025.acl-long.452.pdf)
  - [MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mencattini25a/mencattini25a.pdf)
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)
  - [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yi25c/yi25c.pdf)
  - [Regress, Don’t Guess: A Regression-like Loss on Number Tokens for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zausinger25a/zausinger25a.pdf)
  - [LoRA-One: One-Step Full Gradient Could Suffice for Fine-Tuning Large Language Models, Provably and Efficiently](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ax/zhang25ax.pdf)
  - [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf)
  - [Sketch to Adapt: Fine-Tunable Sketches for Efficient LLM Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bs/zhang25bs.pdf)
  - [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cu/zhang25cu.pdf)
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)
  - [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25g/su25g.pdf)
  - [Speculate, then Collaborate: Fusing Knowledge of Language Models during Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25e/wang25e.pdf)
  - [PIPA: Preference Alignment as Prior-Informed Statistical Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cl/li25cl.pdf)
  - [KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dd/li25dd.pdf)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)
  - [Gumiho: A Hybrid Architecture to Prioritize Early Tokens in Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dg/li25dg.pdf)
  - [Critical Tokens Matter: Token-Level Contrastive Estimation Enhances LLM’s Reasoning Capability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25j/lin25j.pdf)
  - [SeedLoRA: A Fusion Approach to Efficient LLM Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25o/liu25o.pdf)
  - [AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aq/liu25aq.pdf)
  - [Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mahdavi25a/mahdavi25a.pdf)
  - [Discriminative Policy Optimization for Token-Level Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ca/chen25ca.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Fast Large Language Model Collaborative Decoding via Speculation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25c/fu25c.pdf)
  - [MARGE: Improving Math Reasoning with Guided Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25h/gao25h.pdf)
  - [Large Language Models to Diffusion Finetuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cetin25a/cetin25a.pdf)
  - [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aa/chen25aa.pdf)
  - [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [Discriminative Finetuning of Generative Large Language Models without Reward Models and Human Preference Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25d/guo25d.pdf)
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)
  - [Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf)
  - [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf)
  - [Latent Thought Models with Variational Bayes Inference-Time Computation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kong25c/kong25c.pdf)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
  - [polybasic Speculative Decoding Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25az/wang25az.pdf)
  - [Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bb/wang25bb.pdf)
  - [BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
  - [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf)
  - [Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25ae/zhu25ae.pdf)
  - [From Parameters to Performance: A Data-Driven Study on LLM Structure and Development](https://aclanthology.org/2025.emnlp-main.1325.pdf)
  - [Model Unlearning via Sparse Autoencoder Subspace Guided Projections](https://aclanthology.org/2025.emnlp-main.1348.pdf)
  - [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [Active Layer-Contrastive Decoding Reduces Hallucination in Large Language Model Generation](https://aclanthology.org/2025.emnlp-main.150.pdf)
  - [Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens](https://aclanthology.org/2025.emnlp-main.171.pdf)
  - [Can LLMs Explain Themselves Counterfactually?](https://aclanthology.org/2025.emnlp-main.396.pdf)
  - [UNCERTAINTY-LINE: Length-Invariant Estimation of Uncertainty for Large Language Models](https://aclanthology.org/2025.emnlp-main.400.pdf)
  - [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf)
  - [Superficial Self-Improved Reasoners Benefit from Model Merging](https://aclanthology.org/2025.emnlp-main.301.pdf)
  - [Feature Extraction and Steering for Enhanced Chain-of-Thought Reasoning in Language Models](https://aclanthology.org/2025.emnlp-main.552.pdf)
  - [G2: Guided Generation for Enhanced Output Diversity in LLMs](https://aclanthology.org/2025.emnlp-main.713.pdf)
  - [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.726.pdf)
  - [Expanding before Inferring: Enhancing Factuality in Large Language Models through Premature Layers Interpolation](https://aclanthology.org/2025.emnlp-main.645.pdf)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
  - [Graceful Forgetting in Generative Language Models](https://aclanthology.org/2025.emnlp-main.666.pdf)
  - [Direct Value Optimization: Improving Chain-of-Thought Reasoning in LLMs with Refined Values](https://aclanthology.org/2025.emnlp-main.668.pdf)
  - [CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs](https://aclanthology.org/2025.emnlp-main.704.pdf)
  - [HookMoE: A learnable performance compensation strategy of Mixture-of-Experts for LLM inference acceleration](https://aclanthology.org/2025.emnlp-main.1610.pdf)
  - [Orthogonal Finetuning Made Scalable](https://aclanthology.org/2025.emnlp-main.1627.pdf)
  - [Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.914.pdf)
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf)
  - [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1087.pdf)
  - [Compound AI Systems Optimization: A Survey of Methods, Challenges, and Future Directions](https://aclanthology.org/2025.emnlp-main.1463.pdf)
  - [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf)
  - [Do Large Language Models excel in Complex Logical Reasoning with Formal Language?](https://aclanthology.org/2025.emnlp-main.855.pdf)
  - [ThinkEdit: Interpretable Weight Editing to Mitigate Overly Short Thinking in Reasoning Models](https://aclanthology.org/2025.emnlp-main.861.pdf)
  - [Dovetail: A CPU/GPU Heterogeneous Speculative Decoding for LLM inference](https://aclanthology.org/2025.emnlp-main.879.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.236.pdf)
  - [Improving Reasoning Capabilities in Small Models through Mixture-of-layers Distillation with Stepwise Attention on Key Information](https://aclanthology.org/2025.emnlp-main.250.pdf)
  - [Reasoning under Uncertainty: Efficient LLM Inference via Unsupervised Confidence Dilution and Convergent Adaptive Sampling](https://aclanthology.org/2025.emnlp-main.1638.pdf)
  - [ThinkSLM: Towards Reasoning in Small Language Models](https://aclanthology.org/2025.emnlp-main.1659.pdf)
  - [No Need for Explanations: LLMs can implicitly learn from mistakes in-context](https://aclanthology.org/2025.emnlp-main.1686.pdf)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-Only LLMs](https://aclanthology.org/2025.emnlp-main.481.pdf)
  - [Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance](https://aclanthology.org/2025.emnlp-main.500.pdf)
  - [LaMDAgent: An Autonomous Framework for Post-Training Pipeline Optimization via LLM Agents](https://aclanthology.org/2025.emnlp-main.1529.pdf)
  - [Expectation Preference Optimization: Reliable Preference Estimation for Improving the Reasoning Capability of Large Language Models](https://aclanthology.org/2025.emnlp-main.1532.pdf)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1542.pdf)
  - [CoMAT: Chain of Mathematically Annotated Thought Improves Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1024.pdf)
  - [The Emperor's New Reasoning: Format Imitation Overshadows Genuine Mathematical Understanding in SFT](https://aclanthology.org/2025.emnlp-main.1067.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
  - [From Understanding to Generation: An Efficient Shortcut for Evaluating Language Models](https://aclanthology.org/2025.emnlp-main.1148.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
  - [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173.pdf)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)
  - [Firewall Routing: Blocking Leads to Better Hybrid Inference for LLMs](https://aclanthology.org/2025.emnlp-main.331.pdf)
  - [Empowering Math Problem Generation and Reasoning for Large Language Model via Synthetic Data based Continual Learning Framework](https://aclanthology.org/2025.emnlp-main.1223.pdf)
  - [Principled Personas: Defining and Measuring the Intended Effects of Persona Prompting on Task Performance](https://aclanthology.org/2025.emnlp-main.1364.pdf)
  - [Parrot: A Training Pipeline Enhances Both Program CoT and Natural Language CoT for Reasoning](https://aclanthology.org/2025.emnlp-main.1366.pdf)
- **MATH** (measurement instrument): *measured_by*, 109 papers
  > We evaluate DTV on three quantitative reasoning datasets: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021) and MultiArith (Roy & Roth, 2016).
  - [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf)
  - [MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/15425f2df99aa1ba52712c9a4afc8536-Paper-Conference.pdf)
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
  - [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c400474e8a36d0812fdee52739288b12-Paper-Conference.pdf)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
  - [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf)
  - [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)
  - [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf)
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
  - [OpenWebMath: An Open Dataset of High-Quality Mathematical Web Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf)
  - [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
  - [Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bc4f74e35bcfe8cfe43b0a860786d6a-Paper-Conference.pdf)
  - [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [VB-LoRA: Extreme Parameter Efficient Fine-Tuning with Vector Banks](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e0d38c676d5855bcfab7f6d29d20ad9-Paper-Conference.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Bridging The Gap between Low-rank and Orthogonal Adaptation via Householder Reflection Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf)
  - [Metacognitive Capabilities of LLMs: An Exploration in Mathematical Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/2318d75a06437eaa257737a5cf3ab83c-Paper-Conference.pdf)
  - [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf)
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
  - [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
  - [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf)
  - [Learning from Teaching Regularization: Generalizable Correlations Should be Easy to Imitate](https://proceedings.neurips.cc/paper_files/paper/2024/file/01ce1ae7f94d139e4917f9e4425a4f38-Paper-Conference.pdf)
  - [AutoPSV: Automated Process-Supervised Verifier](https://proceedings.neurips.cc/paper_files/paper/2024/file/9246aa822579d9b29a140ecdac36ad60-Paper-Conference.pdf)
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [Toward Self-Improvement of LLMs via Imagination, Searching, and Criticizing](https://proceedings.neurips.cc/paper_files/paper/2024/file/5e5853f35164e434015716a8c2a66543-Paper-Conference.pdf)
  - [SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Conformal Language Model Reasoning with Coherent Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/679fcceef65c3d855aa885bd024542c1-Paper-Conference.pdf)
  - [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/bea94fe9c5573e74294657f692069d89-Paper-Conference.pdf)
  - [3D-Properties: Identifying Challenges in DPO and Charting a Path Forward](https://proceedings.iclr.cc/paper_files/paper/2025/file/c080f9fb3658511bc4f063c5794ef706-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [B-STaR: Monitoring and Balancing Exploration and Exploitation in Self-Taught Reasoners](https://proceedings.iclr.cc/paper_files/paper/2025/file/c8db30c6f024a3f667232ed7ba5b6d47-Paper-Conference.pdf)
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
  - [WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c04aea54c2a60a632a47bd451cd2849-Paper-Conference.pdf)
  - [Balancing Act: Diversity and Consistency in Large Language Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5554e55d7a21e62d0d7a028ec0ea1c7-Paper-Conference.pdf)
  - [MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/abbbb25cddb2c2cd08714e6bfa2f0634-Paper-Conference.pdf)
  - [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
  - [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf)
  - [Automatic Curriculum Expert Iteration for Reliable LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9083c94382509473bdf5fc2672fc72b3-Paper-Conference.pdf)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [UGMathBench: A Diverse and Dynamic Benchmark for Undergraduate-Level Mathematical Reasoning with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c3af3531df85264decc31382cb319781-Paper-Conference.pdf)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [A transfer learning framework for weak to strong generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa47ffc7b2033fd32d8b8734686f6ff4-Paper-Conference.pdf)
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
  - [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf)
  - [S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.475.pdf)
  - [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf)
  - [Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning](https://aclanthology.org/2025.naacl-long.519.pdf)
  - [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf)
  - [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf)
  - [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf)
  - [Fusing Highly Specialized Language Models for Comprehensive Expertise](https://aclanthology.org/2025.acl-long.42.pdf)
  - [RATIONALYST: Pre-training Process-Supervision for Improving Reasoning](https://aclanthology.org/2025.acl-long.1288.pdf)
  - [From Informal to Formal – Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs](https://aclanthology.org/2025.acl-long.1310.pdf)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [ScaleBiO: Scalable Bilevel Optimization for LLM Data Reweighting](https://aclanthology.org/2025.acl-long.1543.pdf)
  - [How to Mitigate Overfitting in Weak-to-strong Generalization?](https://aclanthology.org/2025.acl-long.784.pdf)
  - [MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion](https://aclanthology.org/2025.acl-long.367.pdf)
  - [Unleashing LLM Reasoning Capability via Scalable Question Synthesis from Scratch](https://aclanthology.org/2025.acl-long.658.pdf)
  - [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yi25c/yi25c.pdf)
  - [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25g/su25g.pdf)
  - [Optimizing Language Models for Inference Time Objectives using Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25o/tang25o.pdf)
  - [PIPA: Preference Alignment as Prior-Informed Statistical Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cl/li25cl.pdf)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)
  - [SeedLoRA: A Fusion Approach to Efficient LLM Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25o/liu25o.pdf)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
  - [Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mahdavi25a/mahdavi25a.pdf)
  - [Discriminative Policy Optimization for Token-Level Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ca/chen25ca.pdf)
  - [MARGE: Improving Math Reasoning with Guided Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25h/gao25h.pdf)
  - [Large Language Models to Diffusion Finetuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cetin25a/cetin25a.pdf)
  - [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf)
  - [Discriminative Finetuning of Generative Large Language Models without Reward Models and Human Preference Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25d/guo25d.pdf)
  - [Measuring In-Context Computation Complexity via Hidden State Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/herrmann25a/herrmann25a.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25e/hou25e.pdf)
  - [What Do Learning Dynamics Reveal About Generalization in LLM Mathematical Reasoning?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kang25f/kang25f.pdf)
  - [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf)
  - [BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
  - [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment](https://aclanthology.org/2025.emnlp-main.406.pdf)
  - [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf)
  - [Superficial Self-Improved Reasoners Benefit from Model Merging](https://aclanthology.org/2025.emnlp-main.301.pdf)
  - [HookMoE: A learnable performance compensation strategy of Mixture-of-Experts for LLM inference acceleration](https://aclanthology.org/2025.emnlp-main.1610.pdf)
  - [Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.914.pdf)
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf)
  - [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1087.pdf)
  - [ThinkSLM: Towards Reasoning in Small Language Models](https://aclanthology.org/2025.emnlp-main.1659.pdf)
  - [Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning](https://aclanthology.org/2025.emnlp-main.1068.pdf)
  - [Enhancing Chain-of-Thought Reasoning via Neuron Activation Differential Analysis](https://aclanthology.org/2025.emnlp-main.817.pdf)
  - [Principled Personas: Defining and Measuring the Intended Effects of Persona Prompting on Task Performance](https://aclanthology.org/2025.emnlp-main.1364.pdf)
- **SVAMP** (measurement instrument): *measured_by*, 42 papers
  > We evaluated models on... SVAMP... ensuring a thorough assessment of the model’s mathematical reasoning aptitude. (Section 3.2)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
  - [Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL](https://proceedings.iclr.cc/paper_files/paper/2024/file/b84b9d1fe05c5e74d8f9466f063327a5-Paper-Conference.pdf)
  - [MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/15425f2df99aa1ba52712c9a4afc8536-Paper-Conference.pdf)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
  - [Reranking Laws for Language Generation: A Communication-Theoretic Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/c8b2f897e45770595656a79a9ad91e89-Paper-Conference.pdf)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
  - [Instance-adaptive Zero-shot Chain-of-Thought Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/e304e04a6f455dd82f8a85a0a3679493-Paper-Conference.pdf)
  - [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
  - [Localized Zeroth-Order Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cef1316eaef9bd99da46f63334dc031-Paper-Conference.pdf)
  - [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf)
  - [SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbc461518c59a2a8d64e70e2c38c4a0e-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf)
  - [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf)
  - [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf)
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)
  - [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.503.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
  - [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf)
  - [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf)
  - [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yi25c/yi25c.pdf)
  - [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cu/zhang25cu.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25ae/zhu25ae.pdf)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
  - [CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs](https://aclanthology.org/2025.emnlp-main.704.pdf)
  - [Improving Reasoning Capabilities in Small Models through Mixture-of-layers Distillation with Stepwise Attention on Key Information](https://aclanthology.org/2025.emnlp-main.250.pdf)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)
  - [Parrot: A Training Pipeline Enhances Both Program CoT and Natural Language CoT for Reasoning](https://aclanthology.org/2025.emnlp-main.1366.pdf)
- **AQuA-RAT** (measurement instrument): *measured_by*, 24 papers
  > For evaluation, we employ a range of benchmarks - GSM8K, MATH, MMLU-MATH, AGIEval-SAT-MATH, MathQA, AQuA - to assess varying levels of mathematical reasoning abilities, comparing all models using the same few-shot prompting with greedy decoding. (Section 4.2)
  - [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [Localized Zeroth-Order Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cef1316eaef9bd99da46f63334dc031-Paper-Conference.pdf)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
  - [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbc461518c59a2a8d64e70e2c38c4a0e-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf)
  - [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf)
  - [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf)
  - [Fusing Highly Specialized Language Models for Comprehensive Expertise](https://aclanthology.org/2025.acl-long.42.pdf)
  - [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.503.pdf)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
  - [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf)
  - [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cu/zhang25cu.pdf)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
  - [Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
  - [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf)
  - [No Need for Explanations: LLMs can implicitly learn from mistakes in-context](https://aclanthology.org/2025.emnlp-main.1686.pdf)
  - [CoMAT: Chain of Mathematically Annotated Thought Improves Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1024.pdf)
- **MATH-500** (measurement instrument): *measured_by*, 22 papers
  > We analyze the performance of fine-tuned models of various sizes given different inference FLOPs on mathematical reasoning benchmarks (e.g., GSM8K test set (Cobbe et al., 2021) and MATH500 test set (Hendrycks et al., 2021b; Lightman et al., 2024)).
  - [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf)
  - [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf)
  - [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
  - [YuLan-Mini: Pushing the Limits of Open Data-efficient Language Model](https://aclanthology.org/2025.acl-long.268.pdf)
  - [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf)
  - [AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aq/liu25aq.pdf)
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
  - [Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bb/wang25bb.pdf)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf)
  - [Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens](https://aclanthology.org/2025.emnlp-main.171.pdf)
  - [An Empirical Study of LLM Reasoning Ability Under Strict Output Length Constraint](https://aclanthology.org/2025.emnlp-main.389.pdf)
  - [Feature Extraction and Steering for Enhanced Chain-of-Thought Reasoning in Language Models](https://aclanthology.org/2025.emnlp-main.552.pdf)
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.683.pdf)
  - [Let's Reason Formally: Natural-Formal Hybrid Reasoning Enhances LLM's Math Capability](https://aclanthology.org/2025.emnlp-main.850.pdf)
  - [ThinkEdit: Interpretable Weight Editing to Mitigate Overly Short Thinking in Reasoning Models](https://aclanthology.org/2025.emnlp-main.861.pdf)
  - [CoMAT: Chain of Mathematically Annotated Thought Improves Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1024.pdf)
  - [The Emperor's New Reasoning: Format Imitation Overshadows Genuine Mathematical Understanding in SFT](https://aclanthology.org/2025.emnlp-main.1067.pdf)
  - [Learning Like Humans: Advancing LLM Reasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation](https://aclanthology.org/2025.emnlp-main.336.pdf)
  - [Agentic-R1: Distilled Dual-Strategy Reasoning](https://aclanthology.org/2025.emnlp-main.604.pdf)
- **ASDiv** (measurement instrument): *measured_by*, 17 papers
  > We evaluated models on... ASDIV... ensuring a thorough assessment of the model’s mathematical reasoning aptitude. (Section 3.2)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
  - [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
  - [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf)
  - [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf)
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
  - [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [Improving Reasoning Capabilities in Small Models through Mixture-of-layers Distillation with Stepwise Attention on Key Information](https://aclanthology.org/2025.emnlp-main.250.pdf)
  - [No Need for Explanations: LLMs can implicitly learn from mistakes in-context](https://aclanthology.org/2025.emnlp-main.1686.pdf)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)
- **MultiArith** (measurement instrument): *measured_by*, 14 papers
  > We evaluate DTV on three quantitative reasoning datasets: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021) and MultiArith (Roy & Roth, 2016).
  - [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf)
  - [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)
  - [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf)
  - [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbc461518c59a2a8d64e70e2c38c4a0e-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf)
  - [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf)
  - [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cu/zhang25cu.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf)
  - [CoMAT: Chain of Mathematically Annotated Thought Improves Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1024.pdf)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)
- **AIME 2024** (measurement instrument): *measured_by*, 13 papers
  > We evaluate our models on a set of common benchmarks that consists of GSM8K (1.3K examples), MATH (5K examples), AMC 2023 (40 examples), AIME 2024 (30 examples), and Omni-MATH (4.4K examples) (Omni-Math, 2024).
  - [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)
  - [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
  - [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models](https://aclanthology.org/2025.emnlp-main.287.pdf)
  - [RCScore: Quantifying Response Consistency in Large Language Models](https://aclanthology.org/2025.emnlp-main.290.pdf)
  - [AlphaOne: Reasoning Models Thinking Slow and Fast at Test Time](https://aclanthology.org/2025.emnlp-main.570.pdf)
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.683.pdf)
  - [Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning](https://aclanthology.org/2025.emnlp-main.1068.pdf)
  - [Learning Like Humans: Advancing LLM Reasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation](https://aclanthology.org/2025.emnlp-main.336.pdf)
  - [Sticker-TTS: Learn to Utilize Historical Experience with a Sticker-driven Test-Time Scaling Framework](https://aclanthology.org/2025.emnlp-main.621.pdf)
- **AMC 2023** (measurement instrument): *measured_by*, 12 papers
  > We evaluate our models on a set of common benchmarks that consists of GSM8K (1.3K examples), MATH (5K examples), AMC 2023 (40 examples), AIME 2024 (30 examples), and Omni-MATH (4.4K examples) (Omni-Math, 2024).
  - [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)
  - [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf)
  - [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
  - [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf)
  - [AlphaOne: Reasoning Models Thinking Slow and Fast at Test Time](https://aclanthology.org/2025.emnlp-main.570.pdf)
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.683.pdf)
  - [Steering LLM Reasoning Through Bias-Only Adaptation](https://aclanthology.org/2025.emnlp-main.467.pdf)
  - [Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning](https://aclanthology.org/2025.emnlp-main.1068.pdf)
  - [Learning Like Humans: Advancing LLM Reasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation](https://aclanthology.org/2025.emnlp-main.336.pdf)
  - [Agentic-R1: Distilled Dual-Strategy Reasoning](https://aclanthology.org/2025.emnlp-main.604.pdf)
- **MathQA** (measurement instrument): *measured_by*, 12 papers
  > For evaluation, we employ a range of benchmarks - GSM8K, MATH, MMLU-MATH, AGIEval-SAT-MATH, MathQA, AQuA - to assess varying levels of mathematical reasoning abilities, comparing all models using the same few-shot prompting with greedy decoding. (Section 4.2)
  - [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf)
  - [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf)
  - [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf)
  - [Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.236.pdf)
  - [ThinkSLM: Towards Reasoning in Small Language Models](https://aclanthology.org/2025.emnlp-main.1659.pdf)
  - [Parrot: A Training Pipeline Enhances Both Program CoT and Natural Language CoT for Reasoning](https://aclanthology.org/2025.emnlp-main.1366.pdf)
  - [NESTFUL: A Benchmark for Evaluating LLMs on Nested Sequences of API Calls](https://aclanthology.org/2025.emnlp-main.1702.pdf)
- **CollegeMath** (measurement instrument): *measured_by*, 11 papers
  > For mathematical reasoning, the performance is evaluated on the test set of MATH (Hendrycks et al., 2021b), GSM8K (Cobbe et al., 2021a), and College Math (Tang et al., 2024) by Accuracy. (Section 4.1)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf)
  - [Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning](https://aclanthology.org/2025.acl-long.417.pdf)
  - [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
  - [MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion](https://aclanthology.org/2025.acl-long.367.pdf)
  - [Unleashing LLM Reasoning Capability via Scalable Question Synthesis from Scratch](https://aclanthology.org/2025.acl-long.658.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [Logits-Based Finetuning](https://aclanthology.org/2025.emnlp-main.745.pdf)
  - [Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.236.pdf)
  - [The Emperor's New Reasoning: Format Imitation Overshadows Genuine Mathematical Understanding in SFT](https://aclanthology.org/2025.emnlp-main.1067.pdf)
  - [Empowering Math Problem Generation and Reasoning for Large Language Model via Synthetic Data based Continual Learning Framework](https://aclanthology.org/2025.emnlp-main.1223.pdf)
- **MathVista** (measurement instrument): *measured_by*, 10 papers
  > In this paper, we present MATHVISTA, a consolidated Mathematical reasoning benchmark in Visual contexts. (Section 1)
  - [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf)
  - [Evaluating Large Vision-and-Language Models on Children's Mathematical Olympiads](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc12fb3d4033ad72d33a51f1d0ab5d0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [What matters when building vision-language models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/78b248ea6f627431bba5029d92be8a3d-Paper-Conference.pdf)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
  - [VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.72.pdf)
- **OlympiadBench** (measurement instrument): *measured_by*, 9 papers
  > recent math specific competition and Olympiad-level benchmarking on Math Odyssey (Fang et al., 2024), OlymiadBench (He et al., 2024), and the American Invitational Mathematics Examination (AIME) & the American Mathematics Competitions (AMC) (Beeching et al., 2024; DeepSeek-AI et al., 2024; Reid et al., 2024) questions show that the state-of-the-art (SOTA), both generalist and specialist, LLMs continue to struggle with advanced math reasoning. (Section 1.1).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
  - [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
  - [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf)
  - [Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mahdavi25a/mahdavi25a.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf)
  - [Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.914.pdf)
  - [The Emperor's New Reasoning: Format Imitation Overshadows Genuine Mathematical Understanding in SFT](https://aclanthology.org/2025.emnlp-main.1067.pdf)
  - [Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning](https://aclanthology.org/2025.emnlp-main.1068.pdf)
- **MAWPS** (measurement instrument): *measured_by*, 8 papers
  > We evaluate our models on popular math reasoning benchmarks, namely GSM8K, MATH, GSM-Hard [24], SVAMP [28], TabMWP [29], ASDiv [30], and MAWPS [31]. (Section 3.2)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
- **AddSub** (measurement instrument): *measured_by*, 8 papers
  > We select eleven mathematical reasoning datasets... while the OOD datasets include GSM8K, SVAMP, AddSub, SingleEq, SingleOp, and MATH. (Section 2.2)
  - [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.503.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf)
  - [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
- **GSM-Hard** (measurement instrument): *measured_by*, 8 papers
  > We evaluated models on... GSM-Hard... ensuring a thorough assessment of the model’s mathematical reasoning aptitude. (Section 3.2)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
  - [Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks](https://proceedings.iclr.cc/paper_files/paper/2024/file/72679d76c80e079c70fe5977d21ed1e4-Paper-Conference.pdf)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yi25c/yi25c.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
  - [Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25ae/zhu25ae.pdf)
- **MGSM** (measurement instrument): *measured_by*, 7 papers
  > We experimented MindMerger with the latest multilingual mathematical reasoning MGSM [Shi et al., 2023] and MSVAMP [Chen et al., 2023] (Section 4.2)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
  - [Language Imbalance Driven Rewarding for Multilingual Self-improving](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cdee7247c410907b32fcbc12a605823-Paper-Conference.pdf)
  - [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf)
  - [Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f9a44cb707ede42a659ad85d940dd55-Paper-Conference.pdf)
  - [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf)
  - [P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs](https://aclanthology.org/2025.emnlp-main.242.pdf)
  - [When Life Gives You Samples: The Benefits of Scaling up Inference Compute for Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.1402.pdf)
- **Minerva Math** (measurement instrument): *measured_by*, 6 papers
  > Math: SVAMP (Patel et al., 2021), GSM8k (Cobbe et al., 2021), GSM-Hard (Gao et al., 2023), Hendrycks-MATH (Hendrycks et al., 2021), Minerva-MATH (Lewkowycz et al., 2022). (Section 5.1)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf)
  - [Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens](https://aclanthology.org/2025.emnlp-main.171.pdf)
  - [AlphaOne: Reasoning Models Thinking Slow and Fast at Test Time](https://aclanthology.org/2025.emnlp-main.570.pdf)
  - [HookMoE: A learnable performance compensation strategy of Mixture-of-Experts for LLM inference acceleration](https://aclanthology.org/2025.emnlp-main.1610.pdf)
  - [Learning Like Humans: Advancing LLM Reasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation](https://aclanthology.org/2025.emnlp-main.336.pdf)
- **SingleEq** (measurement instrument): *measured_by*, 6 papers
  > We select eleven mathematical reasoning datasets... while the OOD datasets include GSM8K, SVAMP, AddSub, SingleEq, SingleOp, and MATH. (Section 2.2)
  - [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Improving Reasoning Capabilities in Small Models through Mixture-of-layers Distillation with Stepwise Attention on Key Information](https://aclanthology.org/2025.emnlp-main.250.pdf)
- **TabMWP** (measurement instrument): *measured_by*, 6 papers
  > We evaluated models on... TabMWP... ensuring a thorough assessment of the model’s mathematical reasoning aptitude. (Section 3.2)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [LLaSA: Large Language and Structured Data Assistant](https://aclanthology.org/2025.naacl-long.97.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
- **Reasoning** (construct): *correlates*, 6 papers
  > We find that unsurprisingly, math, coding, and reasoning all correlate with one another.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2025/file/9c77f2ce42151b2c2e26d2cf47f99564-Paper-Conference.pdf)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
  - [CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs](https://aclanthology.org/2025.emnlp-main.704.pdf)
  - [Expectation Preference Optimization: Reliable Preference Estimation for Improving the Reasoning Capability of Large Language Models](https://aclanthology.org/2025.emnlp-main.1532.pdf)
- **Game of 24** (measurement instrument): *measured_by*, 5 papers
  > Besides, we include a challenging mathematical reasoning task, Game of 24 Yao et al. (2024), where the goal is to use four numbers and basic arithmetic operations (addition, subtraction, multiplication, and division) to obtain 24 in 1 equation. (Section 4)
  - [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf)
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
  - [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf)
  - [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf)
- **Omni-MATH** (measurement instrument): *measured_by*, 5 papers
  > We evaluate our models on a set of common benchmarks that consists of GSM8K (1.3K examples), MATH (5K examples), AMC 2023 (40 examples), AIME 2024 (30 examples), and Omni-MATH (4.4K examples) (Omni-Math, 2024).
  - [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/302ce0673c00aee2cf84bb43d0117553-Paper-Conference.pdf)
  - [Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mahdavi25a/mahdavi25a.pdf)
  - [T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25e/hou25e.pdf)
  - [Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.236.pdf)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1542.pdf)
- **AIME 2025** (measurement instrument): *measured_by*, 5 papers
  > In this section, we present a comprehensive evaluation of the proposed GRPO-LEAD framework on two mathematical benchmarks: AIME24 and AIME25. (Section 5)
  - [GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models](https://aclanthology.org/2025.emnlp-main.287.pdf)
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.683.pdf)
  - [Learning Like Humans: Advancing LLM Reasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation](https://aclanthology.org/2025.emnlp-main.336.pdf)
  - [Sticker-TTS: Learn to Utilize Historical Experience with a Sticker-driven Test-Time Scaling Framework](https://aclanthology.org/2025.emnlp-main.621.pdf)
  - [Agentic-R1: Distilled Dual-Strategy Reasoning](https://aclanthology.org/2025.emnlp-main.604.pdf)
- **AIME** (measurement instrument): *measured_by*, 3 papers
  > recent math specific competition and Olympiad-level benchmarking on Math Odyssey (Fang et al., 2024), OlymiadBench (He et al., 2024), and the American Invitational Mathematics Examination (AIME) & the American Mathematics Competitions (AMC) (Beeching et al., 2024; DeepSeek-AI et al., 2024; Reid et al., 2024) questions show that the state-of-the-art (SOTA), both generalist and specialist, LLMs continue to struggle with advanced math reasoning. (Section 1.1).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
  - [T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25e/hou25e.pdf)
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)
- **SAT-Math** (measurement instrument): *measured_by*, 3 papers
  > We evaluate the MathCoder2 models on five representative datasets: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b), SAT-Math (Azerbayev et al., 2024), OCW (Lewkowycz et al., 2022), and MMLU-Math (Hendrycks et al., 2021a). (Section 3.1)
  - [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/bea94fe9c5573e74294657f692069d89-Paper-Conference.pdf)
  - [Fusing Highly Specialized Language Models for Comprehensive Expertise](https://aclanthology.org/2025.acl-long.42.pdf)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
- **miniF2F** (measurement instrument): *measured_by*, 2 papers
  > “The miniF2F dataset is specifically curated for evaluating LLM abilities in autoformalization and mathematical reasoning.”
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
  - [Towards Advanced Mathematical Reasoning for LLMs via First-Order Logic Theorem Proving](https://aclanthology.org/2025.emnlp-main.628.pdf)
- **MathVerse** (measurement instrument): *measured_by*, 2 papers
  > Benchmarks such as MATH-V (Wang et al., 2024a) and MATHVERSE (Zhang et al., 2024e) demonstrate the current limitations of VLMs in handling challenging mathematical problems and understanding mathematical diagrams. (Section 1)
  - [DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/78b248ea6f627431bba5029d92be8a3d-Paper-Conference.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **SimulEq** (measurement instrument): *measured_by*, 2 papers
  > “We evaluate the MathCoder on five datasets, including two in-domain datasets: GSM8K (Cobbe et al., 2021) and MATH (Hendrycks et al., 2021); and three out-of-domain datasets: SVAMP (Patel et al., 2021), Mathematics (Saxton et al., 2019), and SimulEq (Kushman et al., 2014).”
  - [MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/15425f2df99aa1ba52712c9a4afc8536-Paper-Conference.pdf)
  - [SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf)
- **NumGLUE** (measurement instrument): *measured_by*, 2 papers
  > Specialized Domain 1: Mathematical Reasoning... Evaluation Datasets. We follow the framework established in [64] for a comprehensive assessment using several well-regarded datasets, including in-domain and out-of-domain datasets. For the in-domain datasets, we consider GSM8K [11], MATH [19], and NumGLUE [36].
  - [SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf)
  - [LaMDAgent: An Autonomous Framework for Post-Training Pipeline Optimization via LLM Agents](https://aclanthology.org/2025.emnlp-main.1529.pdf)
- **Mathematics Dataset** (measurement instrument): *measured_by*, 2 papers
  > Specialized Domain 1: Mathematical Reasoning... For the out-of-domain datasets, we consider SVAMP [38], Mathematics [13], SimulEq [25].
  - [SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf)
  - [AutoBencher: Towards Declarative Benchmark Construction](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb216114f3eaad22506fd1bc7bbff0ca-Paper-Conference.pdf)
- **GSM-Plus** (measurement instrument): *measured_by*, 2 papers
  > The model’s performance is evaluated on two grade school math benchmarks: GSM8k (Cobbe et al., 2021) and GSM-Plus (Li et al., 2024), which is an adversarial version of GSM8k. (Section 4.4)
  - [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
- **DynaMath** (measurement instrument): *measured_by*, 2 papers
  > To analyze cross-benchmark redundancy, we focus on the Math domain, specifically examining several popular mathematical benchmarks: MathVista (Lu et al., 2023), MathVision (Zhang et al., 2025), MathVerse (Wang et al., 2024a), and DynaMath (Zou et al., 2024).
  - [Redundancy Principles for MLLMs Benchmarks](https://aclanthology.org/2025.acl-long.612.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **CMATH** (measurement instrument): *measured_by*, 2 papers
  > Ape210K (Zhao et al., 2020) and CMATH (Wei et al., 2023a) are two popular Chinese benchmarks for elementary-school-level math reasoning tasks.
  - [Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf)
  - [Empowering Math Problem Generation and Reasoning for Large Language Model via Synthetic Data based Continual Learning Framework](https://aclanthology.org/2025.emnlp-main.1223.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > The evaluation scripts are based on lm-eval for commonsense and mathematical reasoning (Section 4.1).
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMStar** (measurement instrument): *measured_by*, 1 paper
  > The performance of LLaVA-Next-LLaMA3-8B model with merged task vectors across math-related Benchmarks: MathVista ..., MathVerse ..., MMStar ..., DynaMath ..., MathVision ... (Table 2)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **GaoKao** (measurement instrument): *measured_by*, 1 paper
  > Using evaluation scripts from Gou et al. (2023), we assess model accuracy through chain-of-thought reasoning under 0-shot settings, except for multiple-choice problems in GaoKao and CN Middle School 24 which use 5-shot settings. (Section 3.2)
  - [Empowering Math Problem Generation and Reasoning for Large Language Model via Synthetic Data based Continual Learning Framework](https://aclanthology.org/2025.emnlp-main.1223.pdf)
- **MMLU-STEM** (measurement instrument): *measured_by*, 1 paper
  > To evaluate performance, we assess the model on 9 mathematical reasoning benchmarks covering diverse domains, question formats (multiple-choice and open-ended), and difficulty levels (elementary to university): GSM8k (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b), GSM-Hard (Gao et al., 2022), SVAMP (Patel et al., 2021), ASDiv (Miao et al., 2020), MAWPS (Koncel-Kedziorski et al., 2016), TabMWP (TAB) (Lu et al., 2023), MathQA (MQA) (Amini et al., 2019), MMLU-STEM (Hendrycks et al., 2021a), and SAT (Azerbayev et al., 2024). (Section 4.1)
  - [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25a/shin25a.pdf)
- **MathVision** (measurement instrument): *measured_by*, 1 paper
  > The performance of LLaVA-Next-LLaMA3-8B model with merged task vectors across math-related Benchmarks: MathVista ..., MathVerse ..., MMStar ..., DynaMath ..., MathVision ... (Table 2)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on tasks selected from BIG-Bench Hard (BBH) [43], a collection of diverse tasks considered to be challenging to LLMs ... the tasks include numerical reasoning, commonsense problem-solving, logical deduction, linguistic manipulation, machine translation, and tabular reasoning, among others. (Section 3.1)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **MR-GSM8K** (measurement instrument): *measured_by*, 1 paper
  > MR-GSM8K and MR-Math focus solely on mathematical reasoning
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > MT-bench and Vicuna-bench are designed to test the models' competencies in various complex cognitive tasks, including mathematics, reasoning, complex format handling, and writing
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **Vicuna-Bench** (measurement instrument): *measured_by*, 1 paper
  > MT-bench and Vicuna-bench are designed to test the models' competencies in various complex cognitive tasks, including mathematics, reasoning, complex format handling, and writing
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **Geometry3K** (measurement instrument): *measured_by*, 1 paper
  > “To evaluate the effectiveness of SKETCHPAD, we use the problems from the Geometry3K dataset [32].”
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **TACT** (measurement instrument): *measured_by*, 1 paper
  > "TACT—Text And Calculations through Tables, a dataset crafted to evaluate LLMs’ reasoning and computational abilities using complex instructions."
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLU-Math** (measurement instrument): *measured_by*, 1 paper
  > Following [33], we select five mathematical reasoning datasets from MMLU [18] to demonstrate this
  - [Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf)
- **TRACE** (measurement instrument): *measured_by*, 1 paper
  > TRACE (Wang et al., 2023b) serves as a challenging continual instruction tuning benchmark comprising 8 diverse tasks, including domain-specific QA, code completion, mathematical reasoning (Section 2).
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Open LLM Leaderboard** (measurement instrument): *measured_by*, 1 paper
  > This evaluation suite measures LLM performance across six tasks: ... and math problem-solving (GSM8K (Cobbe et al., 2021)).
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **MathGAP** (measurement instrument): *measured_by*, 1 paper
  > In this paper, we present a data-generation framework for evaluating LLMs on problems with arbitrarily complex arithmetic proofs, called MathGAP. (ABSTRACT)
  - [MathGAP: Out-of-Distribution Evaluation on Problems with Arbitrarily Complex Proofs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9c2ab8d429044e0c35bcece2ff6d123-Paper-Conference.pdf)
- **R-GSM** (measurement instrument): *measured_by*, 1 paper
  > Math reasoning results of Qwen1.5 series on R-GSM subset.
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **LiveBench** (measurement instrument): *measured_by*, 1 paper
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **GSM-Symbolic** (measurement instrument): *measured_by*, 1 paper
  > GSM-Symbolic enables more controllable evaluations, providing key insights and more reliable metrics for measuring the reasoning capabilities of models. (Abstract)
  - [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf)
- **GSM-NoOp** (measurement instrument): *measured_by*, 1 paper
  > We introduce GSM-NoOp, a dataset designed to challenge the reasoning capabilities of language models. (Section 4.4)
  - [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf)
- **MathOdyssey** (measurement instrument): *measured_by*, 1 paper
  > recent math specific competition and Olympiad-level benchmarking on Math Odyssey (Fang et al., 2024), OlymiadBench (He et al., 2024), and the American Invitational Mathematics Examination (AIME) & the American Mathematics Competitions (AMC) (Beeching et al., 2024; DeepSeek-AI et al., 2024; Reid et al., 2024) questions show that the state-of-the-art (SOTA), both generalist and specialist, LLMs continue to struggle with advanced math reasoning. (Section 1.1).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
- **VoxEval** (measurement instrument): *measured_by*, 1 paper
  > and 3) pioneers the assessment of complex tasks like mathematical reasoning in spoken format. (Abstract)
  - [VoxEval: Benchmarking the Knowledge Understanding Capabilities of End-to-End Spoken Language Models](https://aclanthology.org/2025.acl-long.818.pdf)
- **TheoremQA** (measurement instrument): *measured_by*, 1 paper
  > For out-of-domain (OOD) evaluation, we use the CollegeMath (Tang et al., 2024), DeepMind-Mathematics (Saxton et al., 2019), OlympiadBench-Math (He et al., 2024), and TheoremQA (Chen et al., 2023) benchmarks (Section 4.1).
  - [MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion](https://aclanthology.org/2025.acl-long.367.pdf)
- **RewardBench** (measurement instrument): *measured_by*, 1 paper
  > RewardBench contains subsets that test RMs in targeted domains, including their coding ability, mathematical ability, and harmlessness. (Section 3.3)
  - [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://aclanthology.org/2025.emnlp-main.167.pdf)
- **PricingLogic** (measurement instrument): *measured_by*, 1 paper
  > Evaluations of a line of LLMs reveal a steep performance drop on the harder tier, exposing systematic failures in rule interpretation and arithmetic reasoning. (Abstract)
  - [PricingLogic: Evaluating LLMs Reasoning on Complex Tourism Pricing Tasks](https://aclanthology.org/2025.emnlp-main.393.pdf)
- **GSM8K-Aug** (measurement instrument): *measured_by*, 1 paper
  > we mainly fine-tune models on the complicated mathematical reasoning benchmark GSM8K-Aug (Deng et al., 2023) (Section 4.1)
  - [DART: Distilling Autoregressive Reasoning to Silent Thought](https://aclanthology.org/2025.emnlp-main.256.pdf)
- **CodeMixBench** (measurement instrument): *measured_by*, 1 paper
  > we introduce the CodeMixBench, a code-mixing evaluation benchmark including eight tasks–three for evaluating LLMs (knowledge reasoning, mathematical reasoning, and truthfulness) and five for traditional NLP tasks (LID, POS, NER, SA, and MT). (§1)
  - [CodeMixBench: Evaluating Code-Mixing Capabilities of LLMs Across 18 Languages](https://aclanthology.org/2025.emnlp-main.109.pdf)
- **IMPLIRET** (measurement instrument): *measured_by*, 1 paper
  > "IMPLIRET covers three reasoning categories: World Knowledge, Arithmetic, and Temporal."
  - [ImpliRet: Benchmarking the Implicit Fact Retrieval Challenge](https://aclanthology.org/2025.emnlp-main.1685.pdf)
- **MMLU-Redux** (measurement instrument): *measured_by*, 1 paper
  > We select a total of seven datasets, including... MMLU-Redux (Gema et al. 2024); focusing on various mathematics subjects... (Section 3)
  - [CoMAT: Chain of Mathematically Annotated Thought Improves Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1024.pdf)
- **MCBench** (measurement instrument): *measured_by*, 1 paper
  > MCBench evaluates three key capabilities of LLMs: ... • Mathematical Reasoning: Each step requires precise arithmetic operations.
  - [Metric Calculating Benchmark: Code-Verifiable Complicate Instruction Following Benchmark for Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf)
- **GaoKao 2023 En** (measurement instrument): *measured_by*, 1 paper
  > On advanced benchmarks such as Minerva Math, GaoKao 2023 En, and CollegeMath, our optimized models achieve 27.9%, 54.3%, and 39.5% respectively, approaching the performance of the best-performing models. (Section 4.1)
  - [Empowering Math Problem Generation and Reasoning for Large Language Model via Synthetic Data based Continual Learning Framework](https://aclanthology.org/2025.emnlp-main.1223.pdf)
- **ProofNet** (measurement instrument): *measured_by*, 1 paper
  > While contemporary LLMs attain competitive performance on established formal mathematical reasoning benchmarks such as miniF2F ... and ProofNet (formal undergraduate-level mathematics (Azerbayev et al., 2023))... (Section 1)
  - [Towards Advanced Mathematical Reasoning for LLMs via First-Order Logic Theorem Proving](https://aclanthology.org/2025.emnlp-main.628.pdf)
- **Arithmetic** (measurement instrument): *measured_by*, 1 paper
  > Arithmetic (Brown et al., 2020): a datasets evaluates the model’s fundamental mathematical reasoning abilities. (Section 4.1)
  - [S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.475.pdf)

### → Mathematical reasoning
- **Chain of thought** (behavioral indicator): *causes*, 7 papers
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [CoTFormer: A Chain of Thought Driven Architecture with Budget-Adaptive Computation Cost at Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf)
  - [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf)
  - [An Efficient and Precise Training Data Construction Framework for Process-supervised Reward Model in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.216.pdf)
  - [Can LLMs Help Uncover Insights about LLMs? A Large-Scale, Evolving Literature Analysis of Frontier LLMs](https://aclanthology.org/2025.acl-long.998.pdf)
  - [RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b77d5b896c321a29277524a98a50215-Paper-Conference.pdf)
  - [Understanding Chain-of-Thought in LLMs through Information Theory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ton25a/ton25a.pdf)
- **Expressive power** (construct): *causes*, 2 papers
  > the limited expressive capacity of LoRA, stemming from the low-rank constraint, has been recognized as a bottleneck, particularly in rigorous tasks like code generation and mathematical reasoning.
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
- **Coding ability** (construct): *causes*, 2 papers
  > Various studies (Azerbayev et al., 2024; Shao et al., 2024) have shown that training on code enhances the mathematical reasoning abilities of large language models (LLMs). (Section 1)
  - [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/bea94fe9c5573e74294657f692069d89-Paper-Conference.pdf)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Formal theorem proving** (behavioral indicator): *causes*, 2 papers
  > Lean provides a verifiable environment to explore theorem proving formally, which has been shown effective in improving mathematical reasoning (Xin et al., 2024; Ying et al., 2024b). As far as we know, we are the first public study to introduce formal mathematics data in pre-training, using a total amount of 0.2B lean-based synthesized data. (Section 4.1)
  - [YuLan-Mini: Pushing the Limits of Open Data-efficient Language Model](https://aclanthology.org/2025.acl-long.268.pdf)
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)
- **Backward reasoning** (behavioral indicator): *causes*, 1 paper
  > ...demonstrating the effectiveness of SV and FOBAR augmentation data in improving mathematical reasoning ability. (Section 4.3)
  - [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c400474e8a36d0812fdee52739288b12-Paper-Conference.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > our AlphaMath enhances Llama3’s mathematical reasoning capabilities without any annotations, yielding an average improvement of +20 points. (Section 4.6)
  - [AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf)
- **Visual understanding** (construct): *causes*, 1 paper
  > Despite the task being focused on mathematical reasoning, STIC enhanced the model’s response by improving its image comprehension capabilities. (Section 6)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Tool use** (behavioral indicator): *causes*, 1 paper
  > They utilize integrated natural language reasoning steps and Python code to improve performance on mathematical reasoning tasks. (Section 1)
  - [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/bea94fe9c5573e74294657f692069d89-Paper-Conference.pdf)
- **Computer science knowledge** (construct): *correlates*, 1 paper
  > we consider this evidence suggests a strong correlation between CS proficiency and skills in Math and Code. (Section 3.5)
  - [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct): *causes*, 1 paper
  > Chain of Thought (CoT) of multi-step benefits from the logical structure of the reasoning steps and task-specific actions, significantly enhancing the mathematical reasoning capabilities of large language models.
  - [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf)
- **System 2 thinking** (construct): *causes*, 1 paper
  > The continuously improved math reasoning capabilities via rStar-Math self-evolved deep thinking. (Table 4)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
- **Autoformalization ability** (construct): *correlates*, 1 paper
  > suggesting that an LLM with stronger mathematical reasoning capabilities is more effective in this task.
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)

### Associated with
- **Complex reasoning** (construct), 3 papers
  > Long-chain reasoning task (Wei et al., 2022; Xiong et al., 2024), such as commonsense reasoning and math reasoning, is one of the critical capabilities in large language models (LLMs) (Lai et al., 2024).
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
- **Memorization** (construct), 2 papers
  > Arithmetic reasoning provides a lens for this investigation, as it can be solved using various methods: learning known algorithms, developing novel approaches, or by memorizing vast quantities of input-output pairs. (Section 1)
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
  - [Exposing the Achilles' Heel: Evaluating LLMs Ability to Handle Mistakes in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.1313.pdf)
- **Table reasoning** (construct), 2 papers
  > Secondly, table reasoning tasks often require numerical reasoning, data preparation, or key cell identification.
  - [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Mathematical problem solving** (behavioral indicator), 1 paper
  > In the mathematical reasoning task, the weak models teach the strong model to respond to mathematical word problems. (Section 5)
  - [A transfer learning framework for weak to strong generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa47ffc7b2033fd32d8b8734686f6ff4-Paper-Conference.pdf)
- **Planning** (construct), 1 paper
  > we posit that the natural language mathematical CoT task is determined by two sub-tasks: step planning task and step calculation task for global logic planning and local mathematical calculation. (Section 4.2)
  - [Unlocking the Capabilities of Thought: A Reasoning Boundary Framework to Quantify and Optimize Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/62ab1c2cb4b03e717005479efb211841-Paper-Conference.pdf)
- **Data analysis** (behavioral indicator), 1 paper
  > the need for data analysis typically arises from specific application scenarios, and requires diverse reasoning skills including mathematical reasoning, logical reasoning, and strategic reasoning. (Abstract)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Problem solving** (behavioral indicator), 1 paper
  > Among these capabilities, mathematical ability serves as a fundamental measure of the problem-solving and complex reasoning skills of LLMs... (Section 1)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
- **Algorithmic reasoning** (construct), 1 paper
  > Arithmetic reasoning provides a lens for this investigation, as it can be solved using various methods: learning known algorithms, developing novel approaches, or by memorizing vast quantities of input-output pairs. (Section 1)
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
- **Optimization problem solving** (behavioral indicator), 1 paper
  > Solving realistic optimization (OPT) problems in application scenarios requires advanced and applied mathematics ability. (Section 1)
  - [OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3deb687c44d3687ace0729e5db3b4efd-Paper-Conference.pdf)
- **Analytical reasoning** (construct), 1 paper
  > This involves several reasoning types: numerical reasoning for interpreting data, temporal reasoning for time-related concepts, lexical reasoning for word meanings, domain-specific reasoning for specialized knowledge, and common-sense reasoning for inferences.
  - [TRANSIENTTABLES: Evaluating LLMs' Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Textual reasoning** (behavioral indicator), 1 paper
  > Textual reasoning ... struggles with quantitative reasoning.
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Error detection** (behavioral indicator), 1 paper
  > However, existing evaluations often focus on final accuracy, neglecting the critical aspect of reasoning capabilities. This work addresses that gap by evaluating LLMs’ abilities to detect and correct reasoning mistakes.
  - [Exposing the Achilles' Heel: Evaluating LLMs Ability to Handle Mistakes in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.1313.pdf)
- **Premise identification ability** (construct), 1 paper
  > “Mathematical problem solving requires a series of deductive reasoning steps, where each step is performed under a small set of premises.” (Section 1)
  - [Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mukherjee25a/mukherjee25a.pdf)
- **Rule-based reasoning** (construct), 1 paper
  > Large language models (LLMs) continue to face challenges in reliably solving reasoning tasks, particularly tasks that involve precise rule following, as often found in mathematical reasoning tasks.
  - [Improving Rule-based Reasoning in LLMs using Neurosymbolic Representations](https://aclanthology.org/2025.emnlp-main.1556.pdf)
- **Problem-solving ability** (construct), 1 paper
  > Mathematical reasoning has emerged as a critical benchmark to measure the advanced reasoning and problem-solving abilities of the Large Language Models (LLMs) (Section 1).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
- **Easy-to-hard generalization** (construct), 1 paper
  > "we select mathematical reasoning to evaluate easy-to-hard generalization ability"
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > mathematical reasoning with code (Section 4.1), where LMs must use reasoning and coding to answer mathematical questions. (Section 4)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
- **Integer addition** (behavioral indicator), 1 paper
  > “we focus on simple arithmetic test problems like addition”
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
- **Decision-making** (construct), 1 paper
  > Decision-making is a complex task requiring various abilities. Several common ones are evaluated across all games: ... (2) Arithmetic Reasoning...
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Logical reasoning** (construct), 1 paper
  > Mathematical reasoning tasks pose significant challenges for large language models (LLMs) because they require precise logical deduction and sequence analysis. (Abstract)
  - [Critical Tokens Matter: Token-Level Contrastive Estimation Enhances LLM’s Reasoning Capability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25j/lin25j.pdf)
- **Utility preservation** (construct), 1 paper
  > As a foundation model, f ′ is expected to retain abilities such as text and code generation, question answering, instruction-following, and basic mathematical reasoning.
  - [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf)
