# MATH
**Type:** Measurement instrument  
**Supporting papers:** 342  
**Also known as:** Math, Mathmeticas, Hendrycks-MATH, Hendrycks MATH, MATH dataset  

## State of the Field

**What it is.** Across papers, the prevailing usage treats MATH as a benchmark dataset of challenging competition-level or high school mathematics problems for evaluating advanced mathematical reasoning. Definitions commonly describe problems drawn from competitions such as AMC 10, AMC 12, and AIME, often spanning seven subjects and domains such as algebra, geometry, and number theory; some papers add that it contains 12,500 problems in informal language with step-by-step solutions and boxed answers, and one paper notes a 5,000-problem evaluation split. A smaller line of work further describes internal difficulty levels from 1 to 5 and uses variants such as an algebra subset of 881 problems, MATH-Algebra-Easy, a multiple-choice version, and the MATH-500 test subset.

**What it is claimed to measure.** Papers link MATH to 13 constructs and 1 behavioral indicator. The dominant framing is that it measures mathematical reasoning; a recurring secondary use is mathematical problem solving, and broader work also treats it as measuring reasoning, complex reasoning, and general ability. The remaining links are more dispersed across 9 other constructs, so reported uses spread across many targets even though mathematical reasoning is the prevailing one.

**Space of uses.** Papers typically include it as one of the main evaluation benchmarks for math or reasoning, most commonly alongside GSM8K and other math datasets. Some studies use fixed-shot evaluation, train and test directly on it, or repurpose it for multi-turn evaluation, while others restrict evaluation to specific slices such as the algebra subset or MATH-500. Related-instrument links also connect it to PutnamBench and lm-evaluation-harness.

**Concerns raised.** Only a smaller line of work raises explicit concerns. One paper analyzes memorization by separating "hits" and non-hits based on 30-gram overlap between a MATH problem or solution and training data, and another contrasts PutnamBench with informal benchmarks such as MATH because its own target output has never been produced, "hence avoiding direct contamination".

## Sources

**MATH** (36 papers: [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf), [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf), [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf), [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf), [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf), [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf), [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf), [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf), [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf), [MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b063829b922fdeb4fa3472dd3471ff43-Paper-Conference.pdf), [MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a0d3ae989a382ce6e50312bc35bf7e1-Paper-Conference.pdf), [MUSTARD: Mastering Uniform Synthesis of Theorem and Proof Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e118ba9ee76c20df728b42a35fb4704-Paper-Conference.pdf), [MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/15425f2df99aa1ba52712c9a4afc8536-Paper-Conference.pdf), [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c400474e8a36d0812fdee52739288b12-Paper-Conference.pdf), [OpenWebMath: An Open Dataset of High-Quality Mathematical Web Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf), [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf), [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fa1edbc195336e29893cdae0939e495f-Paper-Conference.pdf), [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [Token-Supervised Value Models for Enhancing Mathematical Problem-Solving Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0801fccb1d705a9e6747e138d9a0056a-Paper-Conference.pdf), [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf), [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf), [The LLM Language Network: A Neuroscientific Approach for Identifying Causally Task-Relevant Units](https://aclanthology.org/2025.naacl-long.544.pdf), [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf), [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf), [Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning](https://aclanthology.org/2025.naacl-long.519.pdf), [Guiding Through Complexity: What Makes Good Supervision for Hard Reasoning Tasks?](https://aclanthology.org/2025.naacl-long.550.pdf), [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf), [S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.475.pdf), [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf), [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf), [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf), [Fusing Highly Specialized Language Models for Comprehensive Expertise](https://aclanthology.org/2025.acl-long.42.pdf), [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf))
> A dataset of challenging high school mathematical competition problems from sources like AMC 10, AMC 12, and AIME, used to evaluate advanced mathematical reasoning.

**Math** (2 papers: [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf), [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf))
> A mathematical problem-solving benchmark used to evaluate math performance after fine-tuning.

**Mathmeticas** (1 paper: [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf))
> A benchmark for evaluating mathematical reasoning by testing models on problems from the MATH dataset.

**Hendrycks-MATH** (1 paper: [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf))
> Hendrycks-MATH is a mathematical reasoning benchmark covering competition-style math problems.

**Hendrycks MATH** (1 paper: [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf))
> A benchmark dataset consisting of challenging mathematics problems used to evaluate mathematical reasoning capabilities.

**MATH dataset** (2 papers: [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf), [Can LLMs Learn by Teaching for Better Reasoning? A Preliminary Study](https://proceedings.neurips.cc/paper_files/paper/2024/file/8340b085045cf13f1f0b6c2c4cc0a89c-Paper-Conference.pdf))
> A dataset used to evaluate mathematical problem solving capabilities, specifically for comparing template quality.

## Relationships

### → MATH
- **Mathematical reasoning** (construct): *measured_by*, 109 papers
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
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 43 papers
  > We evaluate GPT4-Code using CSV on three datasets: MATH (Hendrycks et al., 2021), GSM8K (Cobbe et al., 2021), and MMLU-Math (Hendrycks et al., 2020).
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
  - [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf)
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
  - [Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
  - [AutoPSV: Automated Process-Supervised Verifier](https://proceedings.neurips.cc/paper_files/paper/2024/file/9246aa822579d9b29a140ecdac36ad60-Paper-Conference.pdf)
  - [ReMI: A Dataset for Reasoning with Multiple Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ea56c0baacac9f7764257a43a93c90a-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
  - [WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c04aea54c2a60a632a47bd451cd2849-Paper-Conference.pdf)
  - [DataEnvGym: Data Generation Agents in Teacher Environments with Student Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/846d3ef94d8c1a833a62cff05569c851-Paper-Conference.pdf)
  - [VibeCheck: Discover and Quantify Qualitative Differences in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/acbfe708197ff78ad04cc1beb1710979-Paper-Conference.pdf)
  - [Token-Supervised Value Models for Enhancing Mathematical Problem-Solving Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0801fccb1d705a9e6747e138d9a0056a-Paper-Conference.pdf)
  - [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf)
  - [Training Language Models to Self-Correct via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf)
  - [Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate](https://proceedings.iclr.cc/paper_files/paper/2025/file/3de667dab3b3d812583abc0a786139a0-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [Building Math Agents with Multi-Turn Iterative Preference Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/40eff1670d6b08bb1bda48b0c5f30110-Paper-Conference.pdf)
  - [Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf)
  - [Adapt Once, Thrive with Updates: Transferable Parameter-Efficient Fine-Tuning on Evolving Base Models](https://aclanthology.org/2025.acl-long.719.pdf)
  - [IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory](https://aclanthology.org/2025.acl-long.761.pdf)
  - [The Jailbreak Tax: How Useful are Your Jailbreak Outputs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nikolic25a/nikolic25a.pdf)
  - [Self-Consistency Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/prasad25a/prasad25a.pdf)
  - [How Do Large Language Monkeys Get Their Power (Laws)?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schaeffer25a/schaeffer25a.pdf)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
  - [Free Process Rewards without Process Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25c/yuan25c.pdf)
  - [Optimizing Language Models for Inference Time Objectives using Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25o/tang25o.pdf)
  - [SeedLoRA: A Fusion Approach to Efficient LLM Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25o/liu25o.pdf)
  - [Optimizing Temperature for Language Models with Multi-Sample Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25f/du25f.pdf)
  - [A Simple Model of Inference Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/levi25a/levi25a.pdf)
  - [Accelerating Large Language Model Reasoning via Speculative Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25di/wang25di.pdf)
  - [BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf)
  - [PIPA: Preference Alignment as Prior-Informed Statistical Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cl/li25cl.pdf)
  - [Co-Eval: Augmenting LLM-based Evaluation with Machine Metrics](https://aclanthology.org/2025.emnlp-main.1307.pdf)
  - [Direct Value Optimization: Improving Chain-of-Thought Reasoning in LLMs with Refined Values](https://aclanthology.org/2025.emnlp-main.668.pdf)
- **Reasoning** (construct): *measured_by*, 13 papers
  > We test SELF-DISCOVER on 25 challenging reasoning tasks including Big Bench-Hard (BBH) (Suzgun et al., 2022), Thinking for Doing (T4D) (Zhou et al., 2023) and MATH (Hendrycks et al., 2021). (Section 1)
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
  - [Quantifying Generalization Complexity for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1a65614bf80c4168acc2b6f05f0950c-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf)
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
  - [The Jailbreak Tax: How Useful are Your Jailbreak Outputs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nikolic25a/nikolic25a.pdf)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
  - [Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25a/zhao25a.pdf)
  - [ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1453.pdf)
- **Complex reasoning** (construct): *measured_by*, 3 papers
  > Experiments are further carried out on the mathematical competition benchmark, MATH (Hendrycks et al., 2021b), achieving a +6.0 improvement with GPT-4, indicating that FUNCODER can also generalize to complex reasoning. (Introduction)
  - [Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bc4f74e35bcfe8cfe43b0a860786d6a-Paper-Conference.pdf)
  - [Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4006ff54a7bbda74c09bad6f7586f5b-Paper-Conference.pdf)
  - [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf)
- **General ability** (construct): *measured_by*, 2 papers
  > We evaluated the general capabilities of the models on benchmarks related to general-domain chat (MT-Bench [83] and Alpaca-Eval [37]), general MCQs (MMLU [34] and GPQA [54]), and mathematical tasks (MATH [22] and GSM8k [12]). (Section 4.1)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Mix-CPT: A Domain Adaptation Framework via Decoupling Knowledge Learning and Format Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc721384c26c0bdff3ec31a7de31d8d5-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **Short-context ability** (construct): *measured_by*, 1 paper
  > We select 8 short-context tasks commonly used for evaluating the general capabilities of models. These include... and MATH... (Section 4.1)
  - [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf)
- **Autoformalization ability** (construct): *measured_by*, 1 paper
  > “Our extensive experiments on the MATH and miniF2F datasets demonstrate that our approach significantly enhances autoformalization accuracy”
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
- **Contextual understanding** (construct): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Chain-of-thought reasoning** (construct): *measured_by*, 1 paper
  > challenging multi-step reasoning tasks such as MATH (Hendrycks et al., 2021) (Section 1)
  - [QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.240.pdf)
- **Coherence** (construct): *measured_by*, 1 paper
  > preserving coherence, as measured by accuracy on the GSM8K, MATH, HumanEval and MMLU-Pro datasets.
  - [Group-Aware Reinforcement Learning for Output Diversity in Large Language Models](https://aclanthology.org/2025.emnlp-main.1649.pdf)
- **Cross-domain generalization** (construct): *measured_by*, 1 paper
  > We find that fine-tuning generalizes perfectly across domains for MATH, which is not very surprising given the near-perfect generalization from few samples to the full distribution in Figure 3. (Section 5.2)
  - [Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf)
- **Easy-to-hard generalization** (construct): *measured_by*, 1 paper
  > We evaluate these verifiers on the GSM8K test set as well as their easy-to-hard generalization on much harder MATH dataset (Hendrycks et al., 2021) (Section 4)
  - [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf)

### Associated with
- **Memorization** (construct), 1 paper
  > Table 7: LLEMMA-34b’s accuracy on hits (a 30-gram overlap between a problem or solution and a training sequence) and non-hits by MATH difficulty level. (Table 7)
  - [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf)
- **PutnamBench** (measurement instrument), 1 paper
  > Our benchmark is unique compared to informal benchmarks such as MATH (Hendrycks et al., 2021) and GSM8K (Cobbe et al., 2021) in the sense that the target output has never been produced, hence avoiding direct contamination.
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MATH-500** (measurement instrument), 1 paper
  > For evaluation, we use the MATH500 subset of the test set (Lightman et al., 2023). (Section 2.2)
  - [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.727.pdf)
- **lm-evaluation-harness** (measurement instrument), 1 paper
  > “We perform evaluations using lm-evaluation-harness ... For both GSM8k and MATH, we use 5-shot examples”
  - [Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning](https://aclanthology.org/2025.naacl-long.519.pdf)
