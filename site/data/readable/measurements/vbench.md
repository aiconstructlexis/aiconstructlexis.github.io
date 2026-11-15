# VBench
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across the papers, VBench is usually presented as a benchmark leaderboard, or more broadly a comprehensive benchmark suite, for text-to-video and video generative models. Definitions describe it as evaluating and ranking model performance across quality and semantic dimensions, and one paper reports average scores over 16 metrics drawn from those two dimensions. Some papers also treat it as a source of evaluation content, describing 946 GPT-augmented text prompts from VBench for generating videos.

**What it is claimed to measure.** Papers use VBench to measure video generation, and this is the only behavioral indicator linked to it; no constructs are linked to it. The claims therefore converge on a single target rather than spreading across many different outcomes. In the recorded evidence, papers describe using VBench to evaluate visual generation capability for video generation, while the definitions frame that evaluation through quality and semantic dimensions.

**Space of uses.** The prevailing use is as a comparison and ranking benchmark: papers report evaluating models with it, comparing results on its leaderboard, and citing outcomes such as topping the leaderboard. A smaller line of use treats it as an input source for evaluation, with one paper leveraging 946 GPT-augmented text prompts from VBench to generate videos. No other measurement instrument is linked to it.

## Sources

**VBench** (2 papers: [Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bm/chen25bm.pdf), [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark leaderboard used to evaluate and rank the performance of text-to-video generation models across multiple quality and semantic dimensions.

## Relationships

### → VBench
- **Video generation** (behavioral indicator): *measured_by*, 3 papers
  > To evaluate the visual generation capability, we use... VBench (Huang et al., 2024) for video generation. (Section 4.1)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
  - [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ag/xu25ag.pdf)
  - [Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bm/chen25bm.pdf)
