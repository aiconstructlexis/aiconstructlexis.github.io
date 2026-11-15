# Error detection
**Type:** Behavioral indicator  
**Supporting papers:** 23  
**Also known as:** Accounting bug detection, Error awareness, Stepwise error detection, Discrimination, Mistake detection, Error identification  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats error detection as identifying whether some reasoning step, response, utterance, text, video, or other artifact contains an error, usually through a direct judgment such as error versus no error, correct versus wrong, or 'ok' versus 'not ok.' Several papers narrow this to reasoning processes, asking a model to examine a specified solution step or chain of thought and determine whether it is correct, while others apply the same idea to dialogue turns, molecular descriptions, generated responses, or agent actions. A smaller line of work makes the output more fine-grained, either determining which error is associated with the last utterance in dialogue or mapping a step to categories such as mathematically erroneous, logically inconsistent, or accumulation error, and some authors describe this as a latent ability to recognize mistakes rather than only as an observed task.

**Variants.** Papers study the behavior in several settings and under several names. The most visible variants are mathematical reasoning versions, including stepwise error detection, mistake detection, and error identification; dialogue settings, where the model determines the error tied to the last agent utterance, including unseen error types; chemistry and code settings, including chemical error detection in molecular descriptions and accounting bug detection in smart contracts; and multimodal settings such as error awareness in AIGC or natural videos and diagnosis of students' hand-drawn math errors. Another recurring formulation applies it to generated text by assigning each sentence a binary faithfulness label.

**Space of elicitation and scores.** Papers measure error detection with two instruments, MMLU-Redux and MOLERR2FIX, and both are described as benchmarks. MMLU-Redux is presented as usable for automatic error detection in NLP datasets, while MOLERR2FIX is explicitly designed to evaluate detection and recovery from chemical errors in molecular descriptions. Outside those named instruments, elicitation is usually by direct judgments, most often binary ones, such as Yes or No for video errors, correct or incorrect for a specified solution step, correct or wrong for a model response, 'ok' or 'not ok' for question quality, or a binary faithfulness label for each generated sentence; a smaller line of work scores reasoning steps against a predefined error taxonomy.

**What it is taken as evidence of.** Papers relate error detection to two constructs, error recovery and mathematical reasoning, and both construct links are framed as related links. One paper places it alongside evaluations of reasoning capabilities that go beyond final accuracy, and another relates it to routing incorrect actions to a reflector for error recovery. Papers also position it around other behaviors: one paper claims a causal relationship from error detection to self-reflection, another claims a causal relationship from error detection to self-correction, and another claims a causal relationship from backtracking to error detection.

## Sources

**Error detection** (5 papers: [Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf), [Towards Automated Error Discovery: A Study in Conversational AI](https://aclanthology.org/2025.emnlp-main.1.pdf), [Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mukherjee25a/mukherjee25a.pdf), [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf), [MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.498.pdf))
> The observable process of an agent identifying mistakes or failures in its own or another agent's reasoning or actions.

**Accounting bug detection** (1 paper: [Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1d8400fec75f683c4d823f5836a81bb-Paper-Conference.pdf))
> Identifying smart-contract statements or code regions that violate domain-specific financial-model constraints.

**Error awareness** (1 paper: [VF-Eval: Evaluating Multimodal LLMs for Generating Feedback on AIGC Videos](https://aclanthology.org/2025.acl-long.1027.pdf))
> The observable task of identifying the presence of general errors in a given video, typically evaluated with binary (Yes/No) questions.

**Stepwise error detection** (1 paper: [Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bb/wang25bb.pdf))
> The observable task of examining a specified step within a given solution to a problem and determining whether that step is correct or incorrect.

**Discrimination** (1 paper: [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf))
> The latent ability of a model to identify and analyze potential mistakes, errors, or harmful elements within a given response.

**Mistake detection** (1 paper: [Exposing the Achilles' Heel: Evaluating LLMs Ability to Handle Mistakes in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.1313.pdf))
> The latent ability to identify incorrect or flawed reasoning steps within a chain of thought, even when the final answer may appear plausible.

**Error identification** (1 paper: [Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mukherjee25a/mukherjee25a.pdf))
> The observable classification of reasoning steps as correct, mathematically erroneous, logically inconsistent, or suffering from accumulation errors.

## Relationships

### Error detection →
- **MMLU-Redux** (measurement instrument): *measured_by*, 1 paper
  > "MMLU-Redux can also be used as a strong benchmark for automatic error detection in NLP datasets"
  - [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > The results show that CDG training significantly improves error detection in reasoning, particularly on the more challenging MATH500 dataset, enhancing the model’s self-reflection ability. (Section 4.2)
  - [Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bb/wang25bb.pdf)
- **MOLERR2FIX** (measurement instrument): *measured_by*, 1 paper
  > We propose MOLERR2FIX, the first benchmark explicitly designed to evaluate LLMs’ ability to detect and recover from chemical errors in molecular descriptions. (Section 1)
  - [MolErr2Fix: Benchmarking LLM Trustworthiness in Chemistry via Modular Error Detection, Localization, Explanation, and Correction](https://aclanthology.org/2025.emnlp-main.977.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > Without accurate error identifications, self-correction becomes more challenging. (Section 1)
  - [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf)

### → Error detection
- **Backtracking** (behavioral indicator): *causes*, 1 paper
  > BacktrackAgent explicitly incorporates a backtracking mechanism to observe the outcomes of action executions, allowing it to detect and recover from error states effectively. (Section 2)
  - [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://aclanthology.org/2025.emnlp-main.212.pdf)

### Associated with
- **Mathematical reasoning** (construct), 1 paper
  > However, existing evaluations often focus on final accuracy, neglecting the critical aspect of reasoning capabilities. This work addresses that gap by evaluating LLMs’ abilities to detect and correct reasoning mistakes.
  - [Exposing the Achilles' Heel: Evaluating LLMs Ability to Handle Mistakes in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.1313.pdf)
- **Error recovery** (construct), 1 paper
  > If both the Verifier and the Judger confirm that ai t is correct, the agent considers it the final action at time-step t and proceeds to time-step t+1. Otherwise, the agent goes to the Reflector for error recovery. (Section 3.2)
  - [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://aclanthology.org/2025.emnlp-main.212.pdf)
