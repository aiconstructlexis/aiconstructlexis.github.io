# LiveCodeBench
**Type:** Measurement instrument  
**Supporting papers:** 45  
**Also known as:** LiveCodeBench-v1.0  

## State of the Field

**What it is.** Across papers, LiveCodeBench is most commonly described as a contamination-free benchmark for code generation built from recent competitive programming problems, often from LeetCode, AtCoder, and Codeforces, with date-based segregation to avoid contamination. Some definitions broaden it to a holistic evaluation of models for code, highlight real-world execution-based evaluation, or describe a dynamic collection process that continuously adds new human-authored problems. Papers also mention variants or subsets, including LiveCodeBench-v1.0, an "easy" subset, and the code execution task LCB-Exec; descriptions of scale differ, ranging from over 711 problems to 400 recent Python algorithm challenges or over 300 contest questions.

**What it is claimed to measure.** The prevailing usage is to measure code generation: papers repeatedly use LiveCodeBench to assess coding capability or function generation, and it is linked to 4 constructs and 3 behavioral indicators. Smaller lines of work use it to measure code debugging through a self-repair scenario, code output prediction through LCB-Exec, test generation ability through test output prediction, abductive code reasoning, coding ability, and reasoning. Overall, the reported measurement claims spread across several code-related capabilities, though code generation is the dominant framing.

**Space of uses.** Papers commonly use it as one of the main code generation benchmarks in multi-benchmark evaluations, often alongside HumanEval+ and MBPP+, and execution-focused work pairs its LCB-Exec task with CRUXEval. At the instrument level, papers link it to 2 other instruments: Chatbot Arena is reported to correlate with LiveCodeBench, and JudgeBench is related to it through a coding-category selection. Some papers also position it as one task within broader evaluation suites rather than as a stand-alone check.

**Concerns raised.** A recurring concern in how papers present LiveCodeBench is data contamination. Definitions repeatedly emphasize contamination-free evaluation, careful segregation by date, and continuous collection of new human-authored problems to maintain freshness and reduce contamination risk.

## Sources

**LiveCodeBench** (8 papers: [Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf), [Tree-of-Evolution: Tree-Structured Instruction Evolution for Code Generation in Large Language Models](https://aclanthology.org/2025.acl-long.14.pdf), [DyCodeEval: Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Under Data Contamination](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ba/chen25ba.pdf), [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf), [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf), [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf), [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf), [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf))
> A benchmark for code generation consisting of competitive programming problems, with careful segregation by date to avoid data contamination issues in evaluation.

**LiveCodeBench-v1.0** (1 paper: [Dynamic Parallel Tree Search for Efficient LLM Reasoning](https://aclanthology.org/2025.acl-long.550.pdf))
> Code generation benchmark designed to evaluate LLMs on programming tasks across difficulty levels, with an 'easy' subset used for efficiency and accuracy comparisons.

## Relationships

### → LiveCodeBench
- **Code generation** (behavioral indicator): *measured_by*, 13 papers
  > LiveCodeBench [21] is a benchmark for contamination-free evaluation. ... we focus on the code generation task for assessing LLM function generation. (Section 3.1)
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf)
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
  - [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
  - [AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aq/liu25aq.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [Alignment with Fill-In-the-Middle for Enhancing Code Generation](https://aclanthology.org/2025.emnlp-main.419.pdf)
  - [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf)
  - [AlphaOne: Reasoning Models Thinking Slow and Fast at Test Time](https://aclanthology.org/2025.emnlp-main.570.pdf)
  - [Process-Supervised Reinforcement Learning for Code Generation](https://aclanthology.org/2025.emnlp-main.719.pdf)
- **Code output prediction** (behavioral indicator): *measured_by*, 1 paper
  > "For execution reasoning, we employ CRUXEval [37] and the code execution task in LiveCodeBench (LCB-Exec for short) [18]."
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Abductive code reasoning** (construct): *measured_by*, 1 paper
  > Deductive code and abductive code reasoning can be regarded as opposite processes; therefore, we selected two identical and representative datasets, CRUXEval (Gu et al., 2024) and LiveCodeBench (Jain et al., 2024), as benchmarks to validate these two capabilities.
  - [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf)
- **Code debugging** (behavioral indicator): *measured_by*, 1 paper
  > "we evaluate the execution-feedback-based multi-turn coding using the self-repair scenario"
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **Test generation ability** (construct): *measured_by*, 1 paper
  > "introduce the test output prediction scenario to evaluate the models’ test generation capabilities"
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **Chatbot Arena** (measurement instrument): *correlates*, 1 paper
  > Even then, our results are well correlated with findings from human evaluations like Chatbot-Arena
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **Coding ability** (construct): *measured_by*, 1 paper
  > “Coding: code generation questions from recent Leetcode and AtCoder questions (via LiveCodeBench (Jain et al., 2024))”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > Extensive evaluations across multiple models and reasoning tasks (AIME-2024, GPQA-Diamond, and LiveCodeBench) demonstrate that STAND reduces inference latency by 60-65% compared to standard autoregressive decoding while maintaining accuracy. (Abstract)
  - [Accelerated Test-Time Scaling with Model-Free Speculative Sampling](https://aclanthology.org/2025.emnlp-main.1558.pdf)

### Associated with
- **JudgeBench** (measurement instrument), 1 paper
  > LiveCodeBench is a contamination-free dataset for coding tasks, containing over 300 challenging questions sourced from coding contests like LeetCode, AtCoder, and Codeforces. We select this dataset for the Coding category. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
