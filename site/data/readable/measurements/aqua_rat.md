# AQuA-RAT
**Type:** Measurement instrument  
**Supporting papers:** 60  
**Also known as:** AQUA, AQuA, AQUA-RAT, AquaRAT  

## State of the Field

**What it is.** Across papers, the dominant framing treats AQuA-RAT, often written AQuA or AQUA-RAT, as a dataset or benchmark of algebraic word problems in multiple-choice format. Many definitions add rationales and multi-step reasoning, and one study describes it as containing approximately 100,000 algebraic word problems, each with a rationale leading to one of five answer options, while others characterize it more broadly as algebraic and quantitative reasoning or as reasoning over quantitative and qualitative relationships. Papers also differ slightly in presentation, with one calling it a 4-option multiple-choice benchmark and another a five-option one, and with difficulty described both as relatively simple and as harder math word problems.

**What it is claimed to measure.** The prevailing usage is as a measure of Mathematical reasoning: papers say it is used to assess varying levels of mathematical reasoning abilities, mathematical reasoning capacity, and arithmetic reasoning. Papers link it to 3 constructs and 1 behavioral indicator overall, with claims concentrated on Mathematical reasoning; a smaller line of work uses it to measure Mathematical problem solving, and single papers also report it as measuring Chain-of-thought reasoning, because the problems require bottom-up composition and multi-step reasoning, and Symbolic reasoning, describing it as involving multiple-choice symbolic reasoning with expressions not explicitly defined in the query. Across papers, the measurement claims therefore center on Mathematical reasoning, with the other links appearing as narrower uses.

**Space of uses.** Papers usually place AQuA-RAT inside broader evaluation suites rather than use it alone, most often alongside GSM8K and also beside SVAMP, MultiArith, MATH, and FinQA. Some studies position it as an auxiliary transfer check, for example evaluating instructions optimized on GSM8K on AQuA and MultiArith, while others use it as a zero-shot chain-of-thought or few-shot numerical reasoning benchmark. It also appears as an unseen-task evaluation and as a test-set benchmark for adapted or fine-tuned models.

## Sources

**AQuA** (9 papers: [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf), [Large Language Models as Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/3339f19c5fcee3ad74502947a32be9e6-Paper-Conference.pdf), [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf), [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf), [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf), [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf), [Fine-Tuning on Diverse Reasoning Chains Drives Within-Inference CoT Refinement in LLMs](https://aclanthology.org/2025.acl-long.191.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf), [AnyMAC: Cascading Flexible Multi-Agent Collaboration via Next-Agent Prediction](https://aclanthology.org/2025.emnlp-main.584.pdf))
> Dataset of algebraic word problems with multiple-choice answers, used to test transferability of optimized prompts across math reasoning tasks.

**AQUA** (1 paper: [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf))
> Multiple-choice math word problem dataset requiring reasoning over quantitative and qualitative relationships.

**AQUA-RAT** (5 papers: [Towards Effective and Efficient Continual Pre-training of Large Language Models](https://aclanthology.org/2025.acl-long.289.pdf), [ACING: Actor-Critic for Instruction Learning in Black-Box LLMs](https://aclanthology.org/2025.emnlp-main.965.pdf), [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf), [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1236.pdf), [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1750.pdf))
> A dataset of algebraic word problems with rationales, requiring multi-step reasoning.

**AQuA-RAT** (1 paper: [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf))
> A dataset of algebraic word problems requiring rationales for their solutions, used to test arithmetic reasoning.

**AquaRAT** (1 paper: [Sample Efficient Demonstration Selection for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/purohit25a/purohit25a.pdf))
> A benchmark of algebraic and quantitative reasoning questions used here to evaluate numerical reasoning with few-shot demonstrations.

## Relationships

### → AQuA-RAT
- **Mathematical reasoning** (construct): *measured_by*, 24 papers
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
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 3 papers
  > AQuA (Ling et al., 2017) is designed for algebraic question-answering tasks and includes a variety of multiple-choice math word problems.
  - [Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4006ff54a7bbda74c09bad6f7586f5b-Paper-Conference.pdf)
  - [Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf)
  - [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf)
- **Chain-of-thought reasoning** (construct): *measured_by*, 1 paper
  > Two mathematical datasets are considered: (4) GSM8k (Cobbe et al., 2021) and (5) AQuA (Ling et al., 2017), since they require comprehensive understanding of complex problems and powerful abilities like bottom-up composition and multi-step reasoning. (Section 4.1)
  - [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf)
- **Symbolic reasoning** (construct): *measured_by*, 1 paper
  > AQuA involves multiple-choice symbolic reasoning with expressions not explicitly defined in the query. (Section 4)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)
