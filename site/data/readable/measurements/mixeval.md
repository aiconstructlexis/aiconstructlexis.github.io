# MixEval
**Type:** Measurement instrument  
**Supporting papers:** 10  

## State of the Field

**What it is.** Across the papers, MixEval is most commonly described as a hybrid benchmark for language models that combines 18 ground-truth-based tasks. Some definitions broaden this to a benchmark across a diverse mix of tasks and domains, and one paper frames it as an efficient, gold-standard evaluation paradigm built by strategically mixing off-the-shelf benchmarks after matching real-world user queries mined from the web to similar queries from existing ground-truth benchmarks; another reports a 0.96 correlation to human preferences.

**What it is claimed to measure.** Papers use MixEval to measure four constructs and one behavioral indicator. The linked constructs are alignment, conversational ability, general ability, and reasoning, and the linked behavioral indicator is classification, so the recorded measurement claims are spread across several targets rather than centered on one; the papers describe it as evaluating alignment effectiveness, general capabilities, and generalist chat capabilities.

**Space of uses.** In practice, papers often use MixEval alongside other evaluations rather than alone. It appears with Open LLM Leaderboard v2 for benchmark evaluation, with MT-Bench and AlpacaEval2 for generalist chat capabilities using GPT-4o-mini as the judge LLM, and with ARC-Challenge, MMLU-Pro, and several other benchmarks in broader analyses.

## Sources

**MixEval** (3 papers: [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf), [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf), [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf))
> A hybrid evaluation benchmark for language models that combines 18 ground-truth-based tasks.

## Relationships

### → MixEval
- **General ability** (construct): *measured_by*, 1 paper
  > To evaluate the general capabilities of the self-play fine-tuned models, we employ MixEval (Ni et al., 2024) and Open LLM Leaderboard v2 (Fourrier et al., 2024) for benchmark evaluation. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **Alignment** (construct): *measured_by*, 1 paper
  > "We evaluate alignment effectiveness using three benchmarks: (1) MixEval ..."
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > For our analysis, we look at seven datasets spanning instruction-following, reasoning, mathematics, and coding: MT-Bench (Zheng et al., 2023), AlpacaEval 2.0 (Li et al., 2023), Arena Hard Auto (Li et al., 2024b), MixEval (Ni et al., 2024), MixEval-Hard, MATH (Hendrycks et al., 2021), and CodeContests (Li et al., 2022). (Section 3.2)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Classification** (behavioral indicator): *measured_by*, 1 paper
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **Conversational ability** (construct): *measured_by*, 1 paper
  > For generalist chat capabilities, we use MixEval, AlpacaEval2, and MTBench with GPT-4o-mini as the judge LLM (Ni et al., 2024; Dubois et al., 2024; Zheng et al., 2023). (Section 3.1)
  - [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf)
