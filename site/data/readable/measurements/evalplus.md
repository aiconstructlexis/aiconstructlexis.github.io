# EvalPlus
**Type:** Measurement instrument  
**Supporting papers:** 39  
**Also known as:** Evalplus, MBPP+  

## State of the Field

**What it is.** Across papers, the prevailing description is an augmented evaluation framework or suite for HumanEval and MBPP that adds more test cases for more rigorous assessment of Python code generation and functional correctness. Definitions regularly refer to its plus versions, HumanEval+ and MBPP+, and one paper notes that scores are reported both on HE and MBPP base test cases and on HE+ and MBPP+ plus test cases. A smaller line of work describes it more narrowly as the test set used to augment HumanEval, while some definitions focus specifically on MBPP+ as the extended MBPP portion covering human-written basic Python tasks.

**What it is claimed to measure.** Papers most commonly use EvalPlus to measure code generation, and that is the dominant role across the surveyed work. More broadly, papers link it to 3 behavioral indicators, Code generation, Code debugging, and Coding, and to 2 constructs, Inductive reasoning and Self-correction ability. The overall pattern is therefore concentrated on code generation, with smaller uses that report it as evaluating coding, code debugging, self-correction ability, or, through MBPP+, inductive reasoning.

**Space of uses.** In use, papers relate EvalPlus to 2 other measurement instruments, HumanEval and HumanEval+, usually by treating it as an improved version of HumanEval or as the evaluation used for HumanEval+. Quoted passages also show it being used to evaluate MBPP and MBPP+, to test the Python version of a HumanEval extension with the EvalPlus test set, and to appear alongside other code-generation benchmarks in comparative evaluation. Papers position it both as a main benchmark for assessing code generation capabilities and as an auxiliary test set used with existing benchmarks.

## Sources

**Evalplus** (1 paper: [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf))
> An evaluation framework used for rigorous assessment of code generation models, particularly for Python.

**EvalPlus** (3 papers: [Tree-of-Evolution: Tree-Structured Instruction Evolution for Code Generation in Large Language Models](https://aclanthology.org/2025.acl-long.14.pdf), [CursorCore: Assist Programming through Aligning Anything](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25f/jiang25f.pdf), [CodeArena: Evaluating and Aligning CodeLLMs on Human Preference](https://aclanthology.org/2025.emnlp-main.489.pdf))
> An augmented version of the HumanEval and MBPP benchmarks that significantly increases the number of test cases per problem to provide a more rigorous evaluation.

**MBPP+** (2 papers: [Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf), [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf))
> An extended version of the Mostly Basic Python Problems (MBPP) benchmark with additional test cases to improve evaluation robustness.

## Relationships

### → EvalPlus
- **Code generation** (behavioral indicator): *measured_by*, 11 papers
  > HumanEval [8] and MBPP [3] are the two most widely-used benchmarks for function-level code generation. We use their test augmented versions, i.e., HumanEval+ and MBPP+, with 80×/35× more test cases for rigorous evaluation [38]. (Section 3.1)
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
  - [Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf)
  - [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf)
  - [Personality-Guided Code Generation Using Large Language Models](https://aclanthology.org/2025.acl-long.54.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
  - [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [CodeArena: Evaluating and Aligning CodeLLMs on Human Preference](https://aclanthology.org/2025.emnlp-main.489.pdf)
- **Coding** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate models on 11 different benchmarks, covering skills such as ... coding (HumanEval+ [6, 32], MBPP+ [2, 32]) (Section 2.2).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **Code debugging** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate their static debug and self-refine capabilities on EvalPlus with five iterations.
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Self-correction ability** (construct): *measured_by*, 1 paper
  > We evaluate their static debug and self-refine capabilities on EvalPlus with five iterations.
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Inductive reasoning** (construct): *measured_by*, 1 paper
  > The abundance of test cases avails utilizing MBPP+ as an inductive reasoning dataset.
  - [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf)

### Associated with
- **HumanEval** (measurement instrument), 1 paper
  > Finally, we conduct a detailed evaluation (Sec. 3) against a range of state-of-the-art models known for their strong performance on the EvalPlus [48] benchmark (an improved version of HumanEval). (Introduction)
  - [IaC-Eval: A Code Generation Benchmark for Cloud Infrastructure-as-Code Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26b29298ae8acd94bd7e839688e329b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **HumanEval+** (measurement instrument), 1 paper
  > “The evaluation of HumanEval+ is conducted with EvalPlus (Liu et al., 2023a)”
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
