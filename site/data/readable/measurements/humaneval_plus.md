# HumanEval+
**Type:** Measurement instrument  
**Supporting papers:** 36  
**Also known as:** HumanEvalPlus, HumanEval Plus, Humaneval+  

## State of the Field

**What it is.** Across these papers, HumanEval+ is most commonly described as an extended or improved version of HumanEval for code generation, with stronger or more comprehensive unit tests for more rigorous evaluation of functional correctness. Definitions vary in the details they foreground: some describe handwritten Python programming questions with comprehensive, ground-truth unit tests, while others describe function-level problems with docstrings, code headers, and input-output examples, or 164 hand-crafted programming problems with function signatures, docstrings, and unit tests. One description adds that the extension scales the number of test cases by 80x.

**What it is claimed to measure.** Papers link HumanEval+ to three constructs and two behavioral indicators. The prevailing use is to measure code generation, often framed as evaluating whether models generate functionally correct code; smaller lines of work use it to measure coding, algorithmic reasoning, coding ability, and functional correctness. Overall, these claims are spread across several closely related targets rather than centered on a single construct.

**Space of uses.** Papers usually position HumanEval+ as a standard or widely used benchmark, often as a test set within multi-benchmark evaluations for code generation. It is commonly used alongside MBPP+, and it also appears with LiveCodeBench, HumanEval, CoderEval, and APPS, plus other benchmarks that appear less often. One paper also relates it to EvalPlus, stating that the evaluation of HumanEval+ is conducted with EvalPlus. Some papers use it as a general benchmark, another uses it to check whether models fine-tuned for code editing retain code generation ability, and one study selects 142 of its 164 problems.

## Sources

**HumanEvalPlus** (1 paper: [Beyond Sequences: Two-dimensional Representation and Dependency Encoding for Code Generation](https://aclanthology.org/2025.acl-long.308.pdf))
> An enhanced version of the HumanEval benchmark that includes more comprehensive and rigorous unit tests to better assess the functional correctness of generated code.

**HumanEval Plus** (1 paper: [Dynamic Scaling of Unit Tests for Code Reward Modeling](https://aclanthology.org/2025.acl-long.343.pdf))
> A benchmark for evaluating code generation, derived from HumanEval, consisting of handwritten Python programming questions with comprehensive, ground-truth unit tests.

**HumanEval+** (2 papers: [How efficient is LLM-generated code? A rigorous & high-standard benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf), [CodeSCM: Causal Analysis for Multi-Modal Code Generation](https://aclanthology.org/2025.naacl-long.345.pdf))
> An extension of the HumanEval benchmark that provides stronger test cases to more rigorously evaluate the functional correctness of generated code.

**Humaneval+** (1 paper: [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf))
> A benchmark for evaluating code generation, which extends the original Humaneval benchmark by significantly increasing the number of test cases.

## Relationships

### → HumanEval+
- **Code generation** (behavioral indicator): *measured_by*, 10 papers
  > HumanEval [8] and MBPP [3] are the two most widely-used benchmarks for function-level code generation. We use their test augmented versions, i.e., HumanEval+ and MBPP+, with 80×/35× more test cases for rigorous evaluation [38]. (Section 3.1)
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
  - [Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf)
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
  - [CodeSCM: Causal Analysis for Multi-Modal Code Generation](https://aclanthology.org/2025.naacl-long.345.pdf)
  - [Personality-Guided Code Generation Using Large Language Models](https://aclanthology.org/2025.acl-long.54.pdf)
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
  - [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.727.pdf)
- **Coding** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate models on 11 different benchmarks, covering skills such as ... coding (HumanEval+ [6, 32], MBPP+ [2, 32]) (Section 2.2).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **Coding ability** (construct): *measured_by*, 1 paper
  > Table 8: Performance of various LLMs on HumanEval, HumanEval+, MBPP, and MBPP+ benchmarks... The fine-tuned LLMs maintain their coding capabilities.
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
- **Algorithmic reasoning** (construct): *measured_by*, 1 paper
  > Our experiments demonstrate that RaLU significantly outperforms existing baselines in mathematical reasoning (GSM8K, MATH) and algorithmic reasoning (HumanEval+, MBPP+), underscoring its potential to advance LLM reasoning and programming by offering enhanced accuracy and interpretability. (Abstract)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)
- **Functional correctness** (construct): *measured_by*, 1 paper
  > As shown in Table 3, we observe that almost all LLMs achieve better efficiency and higher correctness after being fine-tuned with . Take HumanEvalPlus as an example... (Section 4.1)
  - [EffiCoder: Enhancing Code Generation in Large Language Models through Efficiency-Aware Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25as/huang25as.pdf)

### Associated with
- **EvalPlus** (measurement instrument), 1 paper
  > “The evaluation of HumanEval+ is conducted with EvalPlus (Liu et al., 2023a)”
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
