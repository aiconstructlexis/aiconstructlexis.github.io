# PRM800K
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Most commonly, papers describe PRM800K as a dataset for mathematical reasoning with step-by-step, human or manually annotated process-level feedback. The descriptions vary in emphasis: some present mathematical or MATH problems with step-by-step solutions labeled for correctness, some describe each reasoning step as positive, negative, or neutral, and one paper describes 80,000 incorrect stepwise student solutions from MATH, with 2,077 test examples marked at the first error step. A smaller usage note refers to the easy, level 1-3 portion of the dataset.

**What it is claimed to measure.** Across these papers, PRM800K is described through its annotations on reasoning steps, but it is not linked to any named construct or behavioral indicator through explicit measurement claims. No constructs and no behavioral indicators are linked to it.

**Space of uses.** The prevailing usage is as a training or benchmark resource for process-supervised or step-level modeling in math reasoning. Papers describe training a step-level PRM on PRM800K, training policy and reward models on its easy portion, and using it as a benchmark dataset for labeled MATH solutions; one study also pairs training on PRM800K with evaluation on the MATH dataset. No other measurement instrument is linked to it.

## Sources

**PRM800K** (4 papers: [Discriminative Policy Optimization for Token-Level Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ca/chen25ca.pdf), [LLMs cannot spot math errors, even when allowed to peek into the solution](https://aclanthology.org/2025.emnlp-main.553.pdf), [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf), [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf))
> A dataset containing manually annotated step-by-step feedback on mathematical reasoning problems, used for training process-supervised reward models.
