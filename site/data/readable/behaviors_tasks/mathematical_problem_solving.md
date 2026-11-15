# Mathematical problem solving
**Type:** Behavioral indicator  
**Supporting papers:** 652  
**Also known as:** Math word problem solving, Arithmetic problem solving, Math problem solving, Mathematical Problem Solving, Mathematical question answering, Algebraic question answering, Polynomial root-finding, Solving nonlinear ordinary differential equations, Visual math problem solving, Symbolic expression generation, Problem solving, Mathematical word problem solving, Symbolic equation solving, Visual equation solving, Free-response math problem solving, Mathematical reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is solving a mathematical or math word problem and returning a correct final answer, usually numerical but sometimes symbolic. Most definitions pair this with multi-step reasoning or calculation, and some quoted passages describe producing step-by-step solutions or a valid reasoning path before the final answer. A smaller line of work broadens the expected output beyond a single answer to mathematically correct expressions, equation solutions, or formal formulations.

**Variants.** Most papers study natural-language word problems and arithmetic reasoning, often at grade-school level, though some extend to harder benchmark questions. Recurring variants include arithmetic-only tasks, algebraic multiple-choice question answering, symbolic expression generation, and tool-using settings that solve the problem by invoking arithmetic or code. Smaller strands cover visual math from diagrams, graphs, or image-rendered equations, translation of operations-research descriptions into variables, constraints, and objectives, and specialized applied-math tasks such as polynomial root-finding and approximate nonlinear ODE solving.

**Space of elicitation and scores.** Papers link this behavior to 32 measurement instruments. The most frequently linked are GSM8K and MATH, followed by MATH-500, SVAMP, and AIME 2024. These instruments are mostly benchmark datasets or evaluation suites for math word problems, competition-style problems, or broader math reasoning, and scoring commonly uses final-answer correctness, with some papers instead reporting solve rate, extracted-answer accuracy, or F1.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects. It is linked to 6 constructs: papers report that mathematical problem solving is related to Reasoning; other papers report that Chain-of-thought reasoning and Logical reasoning are related to mathematical problem solving; further papers report that mathematical problem solving is related to Mathematical reasoning and State tracking ability. The remaining linked construct appears in a causal claim to mathematical problem solving, and papers also connect this behavior to causal claims from 3 behavioral indicators.

## Sources

**Mathematical problem solving** (11 papers: [AlphaMath Almost Zero: Process Supervision without Process](https://proceedings.neurips.cc/paper_files/paper/2024/file/30dfe47a3ccbee68cffa0c19ccb1bc00-Paper-Conference.pdf), [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf), [Intuitive Fine-Tuning: Towards Simplifying Alignment into a Single Process](https://aclanthology.org/2025.acl-long.6.pdf), [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf), [Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e1a87dbb7e954b8d9d6c91f6db771eb-Paper-Conference.pdf), [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf), [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf), [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf), [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf), [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf), [CogLM: Tracking Cognitive Development of Large Language Models](https://aclanthology.org/2025.naacl-long.4.pdf))
> The observable task of receiving a mathematical problem as input and producing a final numerical or symbolic answer as output.

**Math word problem solving** (4 papers: [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf), [Reasoning with Latent Thoughts: On the Power of Looped Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/2676109d49d1eb26d6bc584a8f556305-Paper-Conference.pdf), [Exposing the Achilles' Heel: Evaluating LLMs Ability to Handle Mistakes in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.1313.pdf), [Predicate-Guided Generation for Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.462.pdf))
> Solving arithmetic word problems and producing the correct numeric answer.

**Arithmetic problem solving** (9 papers: [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf), [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf), [Through the Valley: Path to Effective Long CoT Training for Small Language Models](https://aclanthology.org/2025.emnlp-main.251.pdf), [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf), [BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf), [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf), [DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf))
> Solving numerical word problems or arithmetic questions posed in benchmark format.

**Math problem solving** (3 papers: [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf), [Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/98711dea460bdefe0e651ca23ec98ba2-Paper-Conference.pdf), [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf))
> Solving arithmetic or word problems and producing the numerical answer, often with intermediate calculation steps.

**Mathematical Problem Solving** (1 paper: [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf))
> The observable task of solving geometric or mathematical problems presented in visual contexts.

**Mathematical question answering** (1 paper: [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf))
> Solving math word problems or math questions in a benchmark setting.

**Algebraic question answering** (1 paper: [Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4006ff54a7bbda74c09bad6f7586f5b-Paper-Conference.pdf))
> The task of answering multiple-choice questions based on algebraic word problems.

**Polynomial root-finding** (1 paper: [HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf))
> The task of finding approximate roots for high-order polynomial equations, particularly in different regimes of a small parameter.

**Solving nonlinear ordinary differential equations** (1 paper: [HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf))
> The task of finding approximate analytical solutions for nonlinear ordinary differential equations (ODEs) in different regimes, such as for small and large values of the independent variable.

**Visual math problem solving** (1 paper: [MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine](https://proceedings.iclr.cc/paper_files/paper/2025/file/db36dcad6baee298a34ffca324b84b09-Paper-Conference.pdf))
> Solving mathematics questions that require interpreting diagrams or graphs and producing the correct answer.

**Symbolic expression generation** (1 paper: [CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf))
> The task of generating a correct symbolic mathematical expression as a solution to a word problem with symbolic variables.

**Problem solving** (1 paper: [MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities of LLM Tutors](https://aclanthology.org/2025.emnlp-main.11.pdf))
> Generating a correct numerical answer to a math word problem using chain-of-thought reasoning.

**Mathematical word problem solving** (1 paper: [NESTFUL: A Benchmark for Evaluating LLMs on Nested Sequences of API Calls](https://aclanthology.org/2025.emnlp-main.1702.pdf))
> Solving a natural-language math problem by invoking arithmetic or other math tools and returning the correct numeric answer.

**Symbolic equation solving** (1 paper: [Can Vision-Language Models Solve Visual Math Equations?](https://aclanthology.org/2025.emnlp-main.547.pdf))
> Solving linear equations when the equations are rendered as text in the image.

**Visual equation solving** (1 paper: [Can Vision-Language Models Solve Visual Math Equations?](https://aclanthology.org/2025.emnlp-main.547.pdf))
> Solving linear equations presented as images with icon-based variables and visually repeated coefficients.

**Mathematical reasoning** (5 papers: [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf), [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf), [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf), [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.502.pdf), [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf))
> The observable solving of mathematical problems requiring logical deduction, calculation, or symbolic manipulation.

## Relationships

### Mathematical problem solving →
- **GSM8K** (measurement instrument): *measured_by*, 82 papers
  > We evaluate on the popular GSM8K dataset with grade school math questions (Cobbe et al., 2021). (Section 6)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
  - [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf)
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
  - [Coevolving with the Other You: Fine-Tuning LLM with Sequential Cooperative Multi-Agent Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c2b1c8f7d317719a9ce32dd7386ba35-Paper-Conference.pdf)
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
  - [On Giant's Shoulders: Effortless Weak to Strong by Dynamic Logits Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/34ec1286b2ccd4794c5ca4ad078b7150-Paper-Conference.pdf)
  - [Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf)
  - [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf)
  - [On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf)
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
  - [AutoPSV: Automated Process-Supervised Verifier](https://proceedings.neurips.cc/paper_files/paper/2024/file/9246aa822579d9b29a140ecdac36ad60-Paper-Conference.pdf)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
  - [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf)
  - [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf)
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c04aea54c2a60a632a47bd451cd2849-Paper-Conference.pdf)
  - [Step-by-Step Reasoning for Math Problems via Twisted Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4d92f656cc99f60fe1bfc98386aee34-Paper-Conference.pdf)
  - [Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa27ac7aca4e462da1439b43ceebc04c-Paper-Conference.pdf)
  - [Token-Supervised Value Models for Enhancing Mathematical Problem-Solving Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0801fccb1d705a9e6747e138d9a0056a-Paper-Conference.pdf)
  - [Asynchronous RLHF: Faster and More Efficient Off-Policy RL for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b99315234cc95e6ef281f9155b68832-Paper-Conference.pdf)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
  - [Determine-Then-Ensemble: Necessity of Top-k Union for Large Language Model Ensembling](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbb10d319d44f8c3b4720873e4177c65-Paper-Conference.pdf)
  - [Iterative Nash Policy Optimization: Aligning LLMs with General Preferences via No-Regret Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/4eef032250ac525903063cd760cb0480-Paper-Conference.pdf)
  - [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf)
  - [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf)
  - [Beyond Surface Structure: A Causal Assessment of LLMs' Comprehension ability](https://proceedings.iclr.cc/paper_files/paper/2025/file/88139fdcc82fc597090620d77b023282-Paper-Conference.pdf)
  - [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf)
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
  - [Building Math Agents with Multi-Turn Iterative Preference Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/40eff1670d6b08bb1bda48b0c5f30110-Paper-Conference.pdf)
  - [GraphRouter: A Graph-based Router for LLM Selections](https://proceedings.iclr.cc/paper_files/paper/2025/file/41b6674c28a9b93ec8d22a53ca25bc3b-Paper-Conference.pdf)
  - [Can Textual Gradient Work in Federated Learning?](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a25185fe1b0d46241de7738ea320710-Paper-Conference.pdf)
  - [Leveraging Submodule Linearity Enhances Task Arithmetic Performance in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c983bf84ddbf8c71b2fd19a9d48186b-Paper-Conference.pdf)
  - [Iterative Label Refinement Matters More than Preference Optimization under Weak Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/240225294cdd2c9b692c2519d3278a08-Paper-Conference.pdf)
  - [Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf)
  - [DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf)
  - [Mini-batch Coresets for Memory-efficient Language Model Training on Data Mixtures](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd141278c2cf38ae1e4aee909451fb61-Paper-Conference.pdf)
  - [Dynamic Data Mixing Maximizes Instruction Tuning for Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.80.pdf)
  - [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.584.pdf)
  - [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf)
  - [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf)
  - [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf)
  - [Exploring Safety-Utility Trade-Offs in Personalized Language Models](https://aclanthology.org/2025.naacl-long.565.pdf)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [Refining Salience-Aware Sparse Fine-Tuning Strategies for Language Models](https://aclanthology.org/2025.acl-long.1541.pdf)
  - [TESS 2: A Large-Scale Generalist Diffusion Language Model](https://aclanthology.org/2025.acl-long.1029.pdf)
  - [Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks](https://aclanthology.org/2025.acl-long.317.pdf)
  - [Adapt Once, Thrive with Updates: Transferable Parameter-Efficient Fine-Tuning on Evolving Base Models](https://aclanthology.org/2025.acl-long.719.pdf)
  - [IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory](https://aclanthology.org/2025.acl-long.761.pdf)
  - [LongRecipe: Recipe for Efficient Long Context Generalization in Large Language Models](https://aclanthology.org/2025.acl-long.581.pdf)
  - [ImPart: Importance-Aware Delta-Sparsification for Improved Model Compression and Merging in LLMs](https://aclanthology.org/2025.acl-long.921.pdf)
  - [The Jailbreak Tax: How Useful are Your Jailbreak Outputs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nikolic25a/nikolic25a.pdf)
  - [Self-Consistency Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/prasad25a/prasad25a.pdf)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
  - [Radio: Rate–Distortion Optimization for Large Language Model Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/young25b/young25b.pdf)
  - [Flow of Reasoning: Training LLMs for Divergent Reasoning with Minimal Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25k/yu25k.pdf)
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
  - [Regress, Don’t Guess: A Regression-like Loss on Number Tokens for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zausinger25a/zausinger25a.pdf)
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
  - [SeedLoRA: A Fusion Approach to Efficient LLM Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25o/liu25o.pdf)
  - [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf)
  - [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf)
  - [Make LoRA Great Again: Boosting LoRA with Adaptive Singular Values and Mixture-of-Experts Optimization Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25g/fan25g.pdf)
  - [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)
  - [GaussMark: A Practical Approach for Structural Watermarking of Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/block25a/block25a.pdf)
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
  - [Accelerating Large Language Model Reasoning via Speculative Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25di/wang25di.pdf)
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
  - [Hyperband-based Bayesian Optimization for Black-box Prompt Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schneider25b/schneider25b.pdf)
  - [TokenSkip: Controllable Chain-of-Thought Compression in LLMs](https://aclanthology.org/2025.emnlp-main.165.pdf)
  - [AdaptThink: Reasoning Models Can Learn When to Think](https://aclanthology.org/2025.emnlp-main.184.pdf)
  - [ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning](https://aclanthology.org/2025.emnlp-main.405.pdf)
  - [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf)
  - [Mixture-of-Clustered-Experts: Advancing Expert Specialization and Generalization in Instruction Tuning](https://aclanthology.org/2025.emnlp-main.718.pdf)
  - [Can LLMs Reason Abstractly Over Math Word Problems Without CoT? Disentangling Abstract Formulation From Arithmetic Computation](https://aclanthology.org/2025.emnlp-main.723.pdf)
  - [Logits-Based Finetuning](https://aclanthology.org/2025.emnlp-main.745.pdf)
- **MATH** (measurement instrument): *measured_by*, 43 papers
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
- **MATH-500** (measurement instrument): *measured_by*, 8 papers
  > This evaluation includes benchmarks in: ... 3) Specific math domain tasks like MATH500 (Lightman et al., 2023). (Section 4.3)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf)
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
  - [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf)
  - [AdaptThink: Reasoning Models Can Learn When to Think](https://aclanthology.org/2025.emnlp-main.184.pdf)
  - [ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning](https://aclanthology.org/2025.emnlp-main.405.pdf)
  - [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf)
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)
- **SVAMP** (measurement instrument): *measured_by*, 7 papers
  > To test the performance of OccamLlama on more general mathematical problem solving tasks, we evaluate our method and baselines on the following six benchmarks: AddSub [41], GSM8K [42], MultiArith [33], MATH401 [8], Single Eq [43], and SVAMP [44].
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf)
  - [Can LLMs Reason Abstractly Over Math Word Problems Without CoT? Disentangling Abstract Formulation From Arithmetic Computation](https://aclanthology.org/2025.emnlp-main.723.pdf)
- **AIME 2024** (measurement instrument): *measured_by*, 6 papers
  > These include MATH (Hendrycks et al., 2021b), GSM8K (Cobbe et al., 2021), GSM-Hard (Gao et al., 2023), AIME-2024 for math domains (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
  - [AdaptThink: Reasoning Models Can Learn When to Think](https://aclanthology.org/2025.emnlp-main.184.pdf)
  - [ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning](https://aclanthology.org/2025.emnlp-main.405.pdf)
  - [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf)
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
- **AQuA-RAT** (measurement instrument): *measured_by*, 3 papers
  > AQuA (Ling et al., 2017) is designed for algebraic question-answering tasks and includes a variety of multiple-choice math word problems.
  - [Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4006ff54a7bbda74c09bad6f7586f5b-Paper-Conference.pdf)
  - [Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf)
  - [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf)
- **ASDiv** (measurement instrument): *measured_by*, 3 papers
  > ...GSM-Plus [18], MATH, TheoremQA [6], SVAMP [28], and ASDiv [22] for math. (Section 5.2)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf)
- **TheoremQA** (measurement instrument): *measured_by*, 3 papers
  > We applied MACM to two datasets, SciBench [16] and TheoremQA [5], which claim their difficulty surpasses the middle school level of the MATH dataset, reaching the Undergraduate Level. (Section 4.3)
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 3 papers
  > "MT-bench and Vicuna-bench are designed to test the models’ competencies in various complex cognitive tasks, including mathematics, reasoning, complex format handling, and writing through both multi-turn and single-turn dialogues."
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
  - [FuseChat: Knowledge Fusion of Chat Models](https://aclanthology.org/2025.emnlp-main.1096.pdf)
- **Game of 24** (measurement instrument): *measured_by*, 3 papers
  > The task is that given four cards drawn from a deck of poker, use basic arithmetic operations to combine the card values to reach 24.
  - [Learning to Search from Demonstration Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdf80d651420b47da80f789f2631b1b5-Paper-Conference.pdf)
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **MathQA** (measurement instrument): *measured_by*, 3 papers
  > For mathematic QA tasks (MathQA and GSM8K)... (Section 3.1)
  - [DIVE into MoE: Diversity-Enhanced Reconstruction of Large Language Models from Dense into Mixture-of-Experts](https://aclanthology.org/2025.acl-long.951.pdf)
  - [Mixture-of-Clustered-Experts: Advancing Expert Specialization and Generalization in Instruction Tuning](https://aclanthology.org/2025.emnlp-main.718.pdf)
  - [RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning](https://aclanthology.org/2025.emnlp-main.1630.pdf)
- **GSM-Plus** (measurement instrument): *measured_by*, 2 papers
  > ...GSM-Plus [18], MATH, TheoremQA [6], SVAMP [28], and ASDiv [22] for math. (Section 5.2)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 2 papers
  > Table 3: NAMMs evaluation on InfiniteBench. Model/Task name ... Math
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
- **AMC 2023** (measurement instrument): *measured_by*, 2 papers
  > (2) Math benchmarks include MATH500 (Lightman et al., 2024), AMC2023, and AIME2024. (Section 4.1)
  - [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf)
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)
- **MMLU-Math** (measurement instrument): *measured_by*, 1 paper
  > We evaluate GPT4-Code using CSV on three datasets: MATH (Hendrycks et al., 2021), GSM8K (Cobbe et al., 2021), and MMLU-Math (Hendrycks et al., 2020).
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Math Hard** (measurement instrument): *measured_by*, 1 paper
  > However, progress remains slower in the Math Hard, where scores are consistently lower. This suggests that while MPO iterations are becoming more robust overall, further optimization is needed for specialized tasks like complex mathematical reasoning. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **AIME** (measurement instrument): *measured_by*, 1 paper
  > "Other benchmarks relevant to today’s frontier models include AIME with 15 competition math problems"
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
- **AddSub** (measurement instrument): *measured_by*, 1 paper
  > To test the performance of OccamLlama on more general mathematical problem solving tasks, we evaluate our method and baselines on the following six benchmarks: AddSub [41], GSM8K [42], MultiArith [33], MATH401 [8], Single Eq [43], and SVAMP [44].
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
- **MultiArith** (measurement instrument): *measured_by*, 1 paper
  > To test the performance of OccamLlama on more general mathematical problem solving tasks, we evaluate our method and baselines on the following six benchmarks: AddSub [41], GSM8K [42], MultiArith [33], MATH401 [8], Single Eq [43], and SVAMP [44].
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
- **SingleEq** (measurement instrument): *measured_by*, 1 paper
  > To test the performance of OccamLlama on more general mathematical problem solving tasks, we evaluate our method and baselines on the following six benchmarks: AddSub [41], GSM8K [42], MultiArith [33], MATH401 [8], Single Eq [43], and SVAMP [44].
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)
- **SciBench** (measurement instrument): *measured_by*, 1 paper
  > We applied MACM to two datasets, SciBench [16] and TheoremQA [5], which claim their difficulty surpasses the middle school level of the MATH dataset, reaching the Undergraduate Level. (Section 4.3)
  - [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf)
- **Vicuna-Bench** (measurement instrument): *measured_by*, 1 paper
  > MT-bench and Vicuna-bench are designed to test the models' competencies in various complex cognitive tasks, including mathematics, reasoning, complex format handling, and writing
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **MAWPS** (measurement instrument): *measured_by*, 1 paper
  > Second, GSM8K [9], MaWPS [33] are about math problem solving. (Section 4.1)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **Functional MATH** (measurement instrument): *measured_by*, 1 paper
  > For math, we train and evaluate on Hendrycks MATH benchmark (Hendrycks et al., 2021), and additionally evaluate on two held-out math benchmarks: Functional MATH (Srivastava et al., 2024) and MathOdyssey (Fang et al., 2024).
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
- **MathOdyssey** (measurement instrument): *measured_by*, 1 paper
  > For math, we train and evaluate on Hendrycks MATH benchmark (Hendrycks et al., 2021), and additionally evaluate on two held-out math benchmarks: Functional MATH (Srivastava et al., 2024) and MathOdyssey (Fang et al., 2024).
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
- **Chatbot Arena** (measurement instrument): *measured_by*, 1 paper
  > "The most popular one is the Chatbot Arena ... which contains over one million user queries and evaluates models in various tasks such as code, math, and multilingual understanding"
  - [Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf)
- **MGSM** (measurement instrument): *measured_by*, 1 paper
  > Multilingual math word problems: We use MGSM (Shi et al., 2022) that translates GSM8K (Cobbe et al., 2021) to 10 languages. (Section 4.1)
  - [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf)
- **GSM-Hard** (measurement instrument): *measured_by*, 1 paper
  > These include MATH (Hendrycks et al., 2021b), GSM8K (Cobbe et al., 2021), GSM-Hard (Gao et al., 2023), AIME-2024 for math domains (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **GSM-Symbolic** (measurement instrument): *measured_by*, 1 paper
  > We evaluate CRANE on GSM-Symbolic (Mirzadeh et al., 2024), a dataset consisting of math word problems designed to assess LLMs’ mathematical reasoning skills... the LLMs are tasked with generating correct symbolic expression solutions.
  - [CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf)
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > we task the LIMS method with enabling a model to behave with chain-of-thought generation when a math problem is sensed, following “math(x) →chain of thought(x)”. (Section 4.1)
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
- **Minerva Math** (measurement instrument): *measured_by*, 1 paper
  > Performance is evaluated on MATH500 (Lightman et al., 2023), Minerva Math (Lewkowycz et al., 2022), OlympiadBench (He et al., 2024), College Math (Tang et al., 2024) 3, AIME24, and AMC23 (Section 4.1).
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)
- **OlympiadBench** (measurement instrument): *measured_by*, 1 paper
  > Performance is evaluated on MATH500 (Lightman et al., 2023), Minerva Math (Lewkowycz et al., 2022), OlympiadBench (He et al., 2024), College Math (Tang et al., 2024) 3, AIME24, and AMC23 (Section 4.1).
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)
- **CollegeMath** (measurement instrument): *measured_by*, 1 paper
  > Performance is evaluated on MATH500 (Lightman et al., 2023), Minerva Math (Lewkowycz et al., 2022), OlympiadBench (He et al., 2024), College Math (Tang et al., 2024) 3, AIME24, and AMC23 (Section 4.1).
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)

### → Mathematical problem solving
- **Chain of thought** (behavioral indicator): *causes*, 5 papers
  > The seminal work of chain-of-thought (CoT) (Wei et al., 2022) is an excellent example of how enriching reasoning details, by decomposing reasoning traces into steps, improves its problem-solving capability (Section 1).
  - [Think Smarter not Harder: Adaptive Reasoning with Inference Aware Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25s/yu25s.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
  - [Enhancing Chain-of-Thought Reasoning via Neuron Activation Differential Analysis](https://aclanthology.org/2025.emnlp-main.817.pdf)
  - [Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/c239bac713017b0b2257b7622bf8aab3-Paper-Conference.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > GPT4-Code’s robust performance in solving math problems derives not only from its ability to generate accurate step-by-step code, but also from its self-debugging mechanism.
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > math and code problems are formatted as instructions, enhancing instruction following capabilities enables LLMs to better address these tasks. (Section 4)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
- **Symbolic reasoning** (construct): *causes*, 1 paper
  > Finally, as equation complexity increases, symbolic reasoning itself becomes a limiting factor.
  - [Can Vision-Language Models Solve Visual Math Equations?](https://aclanthology.org/2025.emnlp-main.547.pdf)

### Associated with
- **Reasoning** (construct), 6 papers
  > pipelines that reason about math word problems (Abstract)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
  - [VinePPO: Refining Credit Assignment in RL Training of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kazemnejad25a/kazemnejad25a.pdf)
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
  - [Enhancing Efficiency and Exploration in Reinforcement Learning for LLMs](https://aclanthology.org/2025.emnlp-main.75.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > In the mathematical reasoning task, the weak models teach the strong model to respond to mathematical word problems. (Section 5)
  - [A transfer learning framework for weak to strong generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa47ffc7b2033fd32d8b8734686f6ff4-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct), 1 paper
  > However, their performance in multi-step reasoning tasks, such as solving complex mathematical or coding problems, remains notably constrained (Section 1).
  - [Step-by-Step Reasoning for Math Problems via Twisted Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4d92f656cc99f60fe1bfc98386aee34-Paper-Conference.pdf)
- **Logical reasoning** (construct), 1 paper
  > math tasks challenge logical reasoning;
  - [GuideBench: Benchmarking Domain-Oriented Guideline Following for LLM Agents](https://aclanthology.org/2025.acl-long.557.pdf)
- **State tracking ability** (construct), 1 paper
  > models (especially DeltaNet) with extended eigenvalue range will perform better on language modeling tasks linked to state-tracking such as coding or mathematics
  - [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf)
