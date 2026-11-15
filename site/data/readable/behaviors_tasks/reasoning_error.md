# Reasoning error
**Type:** Behavioral indicator  
**Supporting papers:** 9  
**Also known as:** Reasoning Errors, Flawed reasoning, Making systematic errors  

## State of the Field

**Space of definitions.** Across definitions, papers most commonly describe reasoning error as a failure to apply the logical steps needed to solve a problem, including inferential mistakes, missing critical steps, and incorrect or misapplied reasoning. Some formulations are task-specific: audio work describes cases where the model correctly perceives the audio but still fails at the necessary complex reasoning, while math-focused papers describe flawed solution paths with logical fallacies or misapplication of mathematical principles. A smaller framing treats it as systematic, predictable mistakes in the reasoning process that lead to incorrect answers.

**Variants.** Papers study this behavior in multimodal mathematical reasoning, audio understanding and reasoning, undergraduate-level mathematical reasoning, and grade-school math. The most common names are reasoning error and reasoning errors, though some authors use flawed reasoning or making systematic errors. One multimodal math study, Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset, describes it as the most prevalent cause of errors.

**Space of elicitation and scores.** Papers measure it with one instrument, Manual error analysis. One paper describes this as in-depth human analysis of model error cases that identifies reasoning error as one of the common error types.

**What it is taken as evidence of.** The only construct link claimed in papers is to Reasoning, and it is described as related rather than causal or correlational. The supporting language frames reasoning error as cases where models can correctly perceive audio but still fail to apply the necessary complex reasoning. Beyond that construct link, one paper also relates Hallucination to reasoning error, saying hallucinations can extend to faulty or incomplete reasoning.

## Sources

**Reasoning error** (2 papers: [Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad0edc7d5fa1a783f063646968b7315b-Paper-Datasets_and_Benchmarks_Track.pdf), [Are Multimodal LLMs Robust Against Adversarial Perturbations? RoMMath: A Systematic Evaluation on Multimodal Math Reasoning](https://aclanthology.org/2025.naacl-long.582.pdf))
> An observable failure mode where the model does not apply logical steps correctly or makes inferential mistakes.

**Reasoning Errors** (2 papers: [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf), [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf))
> Observable failures where the model correctly perceives audio but fails to apply the necessary complex reasoning to derive the answer.

**Flawed reasoning** (1 paper: [UGMathBench: A Diverse and Dynamic Benchmark for Undergraduate-Level Mathematical Reasoning with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c3af3531df85264decc31382cb319781-Paper-Conference.pdf))
> An observable error where the model's generated solution path contains logical fallacies, incorrect steps, or misapplication of mathematical principles.

**Making systematic errors** (1 paper: [Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3064f7a0ca2328ecb41a3aef6177d68-Paper-Conference.pdf))
> An observable failure mode where the model consistently produces incorrect answers that can be traced to specific, predictable flaws in its reasoning process.

## Relationships

### Reasoning error →
- **Manual error analysis** (measurement instrument): *measured_by*, 1 paper
  > we conduct an in-depth human analysis of the error cases made by GPT-4o, Qwen2-VL-7B, and Llama 3.2-Vision 11B... Through in-depth analysis, we have identified the following ﬁve common error types that current MLLMs are likely to make: (1) Reasoning Error... (Section 4)
  - [Are Multimodal LLMs Robust Against Adversarial Perturbations? RoMMath: A Systematic Evaluation on Multimodal Math Reasoning](https://aclanthology.org/2025.naacl-long.582.pdf)

### Associated with
- **Reasoning** (construct), 1 paper
  > “Reasoning Errors ... account for a significant portion of mistakes... suggesting that even when models correctly perceive the audio, they often fail to apply the necessary complex reasoning.”
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator), 1 paper
  > hallucinations are not limited to factual inaccuracies; they can also extend to faulty or incomplete reasoning, a significant concern for multi-step reasoning-based tasks (Creswell et al., 2022). (Section 2)
  - [Automatic Curriculum Expert Iteration for Reliable LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9083c94382509473bdf5fc2672fc72b3-Paper-Conference.pdf)
