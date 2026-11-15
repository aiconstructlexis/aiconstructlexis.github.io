# MixEval-Hard
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** MixEval Hard, MixEval-hard  

## State of the Field

**What it is.** Across definitions, MixEval-Hard is most commonly treated as the hard subset of MixEval. Papers describe it as a challenging or more challenging subset for difficult tasks or queries, and one definition says it was derived to better differentiate strong language models; a smaller formulation presents it more generally as a benchmark for challenging general-domain tasks.

**What it is claimed to measure.** Papers link MixEval-Hard to 1 construct and no behavioral indicators. The only linked construct is Reasoning: one paper uses MixEval-Hard among datasets spanning instruction-following, reasoning, mathematics, and coding, so in the recorded relationships it is reported as measuring reasoning rather than a wider spread of constructs.

**Space of uses.** The uses place it within broader evaluation suites. Papers use it alongside several other benchmarks, for example MT-Bench, AlpacaEval 2.0, Arena Hard Auto, and MixEval, and another paper treats it as one of several general-domain tasks. One paper also reports that this harder subset shows a higher correlation of 0.96 with Chatbot Arena Elo.

## Sources

**MixEval-hard** (2 papers: [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf), [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf))
> A challenging subset of the MixEval benchmark designed to test language models on more difficult tasks.

**MixEval-Hard** (1 paper: [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf))
> A more challenging subset of the MixEval benchmark designed to test the limits of LLM capabilities on difficult queries.

**MixEval Hard** (1 paper: [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf))
> A benchmark for evaluating model performance on challenging general domain tasks.

## Relationships

### → MixEval-Hard
- **Reasoning** (construct): *measured_by*, 1 paper
  > For our analysis, we look at seven datasets spanning instruction-following, reasoning, mathematics, and coding: MT-Bench (Zheng et al., 2023), AlpacaEval 2.0 (Li et al., 2023), Arena Hard Auto (Li et al., 2024b), MixEval (Ni et al., 2024), MixEval-Hard, MATH (Hendrycks et al., 2021), and CodeContests (Li et al., 2022). (Section 3.2)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
