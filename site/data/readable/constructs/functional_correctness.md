# Functional correctness
**Type:** Construct  
**Supporting papers:** 15  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats functional correctness as whether a generated artifact does what it is intended to do under a specification or user request, typically by passing relevant test cases or functional verification. Most formulations are about generated code, smart contracts, programs, or API calls, while a smaller formulation extends it to an LLM output that correctly solves the intended problem as verified by an external solver. Papers also separate it from syntactic validity, with one quoted passage noting that better-formed outputs do not by themselves guarantee functional correctness.

**Space of facets.** Papers do not introduce named subtypes, but they recurrently position the construct against nearby evaluation dimensions. The clearest contrast is with syntactic correctness, and some work evaluates it alongside design quality or alongside API hallucination as a distinct target; in benchmark descriptions, test-based checking is also described as execution correctness. No linked constructs are reported as superordinate, equivalent, or contrasting constructs beyond these pairings.

**Space of measurement.** Operationalization is dominated by benchmark-based testing. Papers link it to 5 measurement instruments and 2 behavioral indicators; the instruments named most often are HumanEval, APPS, CodeContests, HumanEval+, and MBPP. HumanEval and MBPP use Pass or passRatio@k, where a task is solved if the solution passes all test cases, APPS and CodeContests use private test cases to check execution correctness, and other quoted passages show Pass@k and Compile@k, AST sub-tree matching for API calls, and solver-based equivalence checks, all of which directly test whether outputs satisfy the intended function.

**Links.** In the papers, the non-measurement links are causal claims from the two linked behavioral indicators. One paper claims a causal relationship from catastrophic forgetting to functional correctness, stating that direct SFT may lead to catastrophic forgetting that diminishes the ability to generate functionally correct code. Another paper claims a causal relationship from code editing to functional correctness, reporting higher functional correctness together with stronger editing performance and robustness; no correlational or undirected related links are reported.

## Sources

**Functional correctness** (3 papers: [SolEval: Benchmarking Large Language Models for Repository-level Solidity Smart Contract Generation](https://aclanthology.org/2025.emnlp-main.218.pdf), [CraftRTL: High-quality Synthetic Data Generation for Verilog Code Models with Correct-by-Construction Non-Textual Representations and Targeted Code Repair](https://proceedings.iclr.cc/paper_files/paper/2025/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf), [CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf))
> The degree to which a generated smart contract behaves as intended according to its specification and passes all relevant test cases.

## Relationships

### Functional correctness →
- **HumanEval** (measurement instrument): *measured_by*, 3 papers
  > HumanEval assesses the functional correctness of synthesized code derived from docstrings. (Section 4.2)
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Black-Box Adversarial Attacks on LLM-Based Code Completion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jenko25a/jenko25a.pdf)
  - [SolEval: Benchmarking Large Language Models for Repository-level Solidity Smart Contract Generation](https://aclanthology.org/2025.emnlp-main.218.pdf)
- **MBPP** (measurement instrument): *measured_by*, 1 paper
  > Both HumanEval and MBPP harness the metric Pass to measure the Code LLMs’ functional correctness, where a task is considered solved if the given solution passes all test cases, and the total fraction of solved tasks is reported as P ass = Nsolved/Ntotal [25]. (Section 4.2)
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
- **APPS** (measurement instrument): *measured_by*, 1 paper
  > Generated codes are evaluated against (private) test cases to check the execution correctness (Hendrycks et al., 2021; Chen et al., 2021; Li et al., 2022) (Section 3.1).
  - [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf)
- **CodeContests** (measurement instrument): *measured_by*, 1 paper
  > Generated codes are evaluated against (private) test cases to check the execution correctness (Hendrycks et al., 2021; Chen et al., 2021; Li et al., 2022) (Section 3.1).
  - [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf)
- **HumanEval+** (measurement instrument): *measured_by*, 1 paper
  > As shown in Table 3, we observe that almost all LLMs achieve better efficiency and higher correctness after being fine-tuned with . Take HumanEvalPlus as an example... (Section 4.1)
  - [EffiCoder: Enhancing Code Generation in Large Language Models through Efficiency-Aware Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25as/huang25as.pdf)

### → Functional correctness
- **Catastrophic forgetting** (behavioral indicator): *causes*, 1 paper
  > This suggests that direct SFT may lead to catastrophic forgetting in vanilla models, diminishing their ability to generate functionally correct code. (Section 4.5)
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Code editing** (behavioral indicator): *causes*, 1 paper
  > EDITLORD outperforms the state-of-the-art by an average of 22.7% in editing performance and 58.1% in robustness while achieving 20.2% higher functional correctness across critical software engineering and security applications, LM models, and editing modes. (Abstract)
  - [EditLord: Learning Code Transformation Rules for Code Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25al/li25al.pdf)
