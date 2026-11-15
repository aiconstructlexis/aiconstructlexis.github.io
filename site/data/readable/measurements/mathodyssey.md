# MathOdyssey
**Type:** Measurement instrument  
**Supporting papers:** 3  
**Also known as:** Math Odyssey  

## State of the Field

**What it is.** Across the papers, the prevailing usage is as a benchmark for math reasoning, especially Olympiad-level mathematical reasoning. One definition describes it more specifically as a set of math problems of varying difficulty, including olympiad-level competition questions, and a quoted passage calls it "a popular benchmark for LLM math reasoning"; another paper refers to it more generally as an olympiad benchmark, and one study focuses on its olympiad-level competition problems.

**What it is claimed to measure.** Papers use MathOdyssey to measure one behavioral indicator, Mathematical problem solving, and two constructs, Generalization and Mathematical reasoning. In the linked claims, it is used as a held-out benchmark for Mathematical problem solving and Generalization, and it is also reported as evaluating Mathematical reasoning, so the measurement claims are spread across these targets rather than centered on a single construct.

**Space of uses.** Papers do not link it to another measurement instrument, though they use it alongside Hendrycks MATH and Functional Math. In those uses, it is positioned as an additional or challenging held-out benchmark, and elsewhere as one of multiple olympiad benchmarks in performance comparisons.

## Sources

**MathOdyssey** (1 paper: [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf))
> A benchmark of varying-difficulty math problems, including olympiad-level competition questions, used to evaluate mathematical reasoning.

**Math Odyssey** (1 paper: [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf))
> A benchmark used in the paper to evaluate Olympiad-level mathematical reasoning.

## Relationships

### → MathOdyssey
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > For math, we train and evaluate on Hendrycks MATH benchmark (Hendrycks et al., 2021), and additionally evaluate on two held-out math benchmarks: Functional MATH (Srivastava et al., 2024) and MathOdyssey (Fang et al., 2024).
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To further assess the generalization capabilities of our BoN aware fine-tuned models, we evaluate their performance on two challenging, held-out benchmarks: Functional Math (Srivastava et al., 2024) and MathOdyssey (Fang et al., 2024).
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > recent math specific competition and Olympiad-level benchmarking on Math Odyssey (Fang et al., 2024), OlymiadBench (He et al., 2024), and the American Invitational Mathematics Examination (AIME) & the American Mathematics Competitions (AMC) (Beeching et al., 2024; DeepSeek-AI et al., 2024; Reid et al., 2024) questions show that the state-of-the-art (SOTA), both generalist and specialist, LLMs continue to struggle with advanced math reasoning. (Section 1.1).
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
