# Super-NaturalInstructions
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** SuperNI, Super-Natural Instructions, SuperNI Benchmark, Super NI, S-NI  

## State of the Field

**What it is.** Most papers describe Super-NaturalInstructions as a large instruction-following benchmark or collection of diverse NLP tasks with expert-written or human-written instructions, usually covering both classification and generation formats. Definitions commonly describe it as having over 1600 tasks or 1,616 tasks, while a smaller line of work uses SuperNI Benchmark for a continual learning setup of 15 tasks spanning dialogue generation, information extraction, question answering, summarization, and sentiment analysis. One paper also uses a subset of 53 tasks, described as 19 multiple-choice and 34 classification tasks, and separately tests formatting generation against 100+ tasks from the benchmark.

**What it is claimed to measure.** Across papers, it is linked to 4 constructs and 3 behavioral indicators. Among the named targets, instruction following, task generalization, and text generation recur most often: papers use it to measure instruction following, report it as evaluating cross-task or unseen-task generalization, and use it for text generation benchmarks. Smaller uses treat it as measuring text classification, continual learning, multi-task ability, and translation ability, so the measurement claims are spread across several targets rather than concentrated on only one.

**Space of uses.** No other measurement instrument is linked to it by papers. Papers usually position it as an evaluation benchmark: they use it as one of several instruction-following datasets, as one of two continual learning benchmarks, or as the source for building continual instruction tuning task sequences. It is also described as being used to assess cross-task generation and conflict after fine-tuning language models, and separate work uses subsets with diverse formats and instructions or tests grammar generation against formatting from 100+ tasks.

## Sources

**SuperNI** (1 paper: [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf))
> A collection of NLP tasks with expert-written instructions used to build continual instruction tuning task sequences and evaluate cross-task generation and conflict.

**Super-Natural Instructions** (2 papers: [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf), [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf))
> A large and diverse benchmark dataset containing over 1600 NLP tasks, designed to evaluate the general instruction-following capabilities of language models across both classification and generation formats.

**SuperNI Benchmark** (1 paper: [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf))
> A comprehensive continual learning benchmark consisting of 15 NLP tasks across categories such as dialogue generation, information extraction, question answering, summarization, and sentiment analysis, used to evaluate general CL performance.

**Super NI** (1 paper: [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf))
> Super Natural Instructions, a benchmark consisting of 1,616 diverse NLP tasks with expert-written instructions to evaluate instruction-following capabilities.

**Super-NaturalInstructions** (1 paper: [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf))
> A large benchmark dataset consisting of diverse natural language processing tasks, each with human-written instructions and prompt formats, used here for evaluation.

**S-NI** (1 paper: [Adversarial Moment-Matching Distillation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbae8efcc23a0cb6d15a20f245514020-Paper-Conference.pdf))
> An instruction-following evaluation dataset used to assess performance on Super-NaturalInstructions prompts.

## Relationships

### → Super-NaturalInstructions
- **Instruction following** (behavioral indicator): *measured_by*, 2 papers
  > This set of tasks evaluates a model’s capability in adhering to instructions. ... Our chosen benchmark for this category is the Super Natural Instructions (Super NI) (Wang et al., 2022)... (Section 4.1)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
- **Task generalization** (construct): *measured_by*, 2 papers
  > We evaluate TAGI on the Super-Natural Instructions (SNI) [37] and P3 [30] datasets. Experimental results demonstrate its ability to effectively generate adapters for unseen tasks, surpassing meta-trained models... (Section 1 Introduction).
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
  - [Automatic Expert Discovery in LLM Upcycling via Sparse Interpolated Mixture-of-Experts](https://aclanthology.org/2025.acl-long.816.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 2 papers
  > The Super-Natural instruction dataset (Wang et al., 2022) contains a collection of 1600+ NLP tasks, including both classiﬁcation and generation tasks.
  - [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf)
  - [AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning](https://aclanthology.org/2025.emnlp-main.678.pdf)
- **Multi-task ability** (construct): *measured_by*, 1 paper
  > “we conducted experiments on two publicly available multitasking benchmarks: SuperGLUE (Wang et al., 2019) and Super Natural-Instructions (Super NI) (Wang et al., 2022).”
  - [Customizable Combination of Parameter-Efficient Modules for Multi-Task Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a692a24dbc744fca340b9ba33bc6522-Paper-Conference.pdf)
- **Translation ability** (construct): *measured_by*, 1 paper
  > We evaluate Llama3 (8B-Instruct) on English-Spanish and English-French translations from SuperNI.
  - [An Auditing Test to Detect Behavioral Shift in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7af140f516c9f57050f7359bf53bc8f0-Paper-Conference.pdf)
- **Text classification** (behavioral indicator): *measured_by*, 1 paper
  > The Super-Natural instruction dataset (Wang et al., 2022) contains a collection of 1600+ NLP tasks, including both classiﬁcation and generation tasks.
  - [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf)
- **Continual learning** (construct): *measured_by*, 1 paper
  > We conducted experiments on two CL benchmarks, including SuperNI Benchmark (Wang et al., 2022a) and Long Sequence Benchmark (Razdaibiedina et al., 2023). (Section 4.1).
  - [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf)
