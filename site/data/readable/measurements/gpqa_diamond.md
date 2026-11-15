# GPQA-Diamond
**Type:** Measurement instrument  
**Supporting papers:** 17  
**Also known as:** GPQADiamond, GPQA Diamond  

## State of the Field

**What it is.** Across the papers, GPQA-Diamond is most commonly described as a challenging expert-level science or STEM question answering benchmark for deep reasoning. Most definitions describe graduate-level or expert-level multiple-choice questions across biology, physics, and chemistry, and one definition specifies 198 questions. A smaller line of work frames GPQADiamond as a challenging subset of GPQA used to assess zero-shot generalization on an unseen task, and some definitions note pass@1 accuracy.

**What it is claimed to measure.** Papers link it to 2 constructs and no behavioral indicators. The prevailing usage is to measure Reasoning: papers describe evaluating models on reasoning benchmarks that include GPQA-Diamond, selecting it among mathematical and reasoning datasets, and measuring reasoning ability with accuracy on GPQA Diamond. A smaller line of work uses it to measure Generalization, specifically how well a transferring-then-finetuning approach generalizes to the unseen task GPQADiamond.

**Space of uses.** Papers do not explicitly relate it to other measurement instruments, but they often use it alongside AIME 2024 and MATH-500, and sometimes LiveCodeBench or GSM8K, in multi-benchmark evaluations. In those evaluations it is positioned as one of the challenging reasoning benchmarks or datasets, while one paper uses it as an additional unseen task for transfer-based evaluation. Some definitions also describe evaluation on GPQA Diamond with pass@1 accuracy.

## Sources

**GPQA-Diamond** (1 paper: [Thinking Out Loud: Do Reasoning Models Know When They're Right?](https://aclanthology.org/2025.emnlp-main.73.pdf))
> Scientific reasoning benchmark containing 198 graduate-level multiple-choice questions across biology, physics, and chemistry.

**GPQADiamond** (1 paper: [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf))
> Challenging subset of GPQA used to assess zero-shot generalization on unseen, expert-level reasoning tasks.

**GPQA Diamond** (3 papers: [Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation](https://aclanthology.org/2025.acl-long.1136.pdf), [LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf), [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf))
> Expert-level question answering benchmark in STEM fields requiring deep reasoning, evaluated using pass@1 accuracy.

## Relationships

### → GPQA-Diamond
- **Reasoning** (construct): *measured_by*, 5 papers
  > Reasoning Models, in which we perform SFT with Qwen-2.5 on s1K dataset (Muennighoff et al., 2025) and evaluated on GPQA Diamond (Rein et al., 2023) (Section 5.1).
  - [LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf)
  - [Enhancing Reasoning Abilities of Small LLMs with Cognitive Alignment](https://aclanthology.org/2025.emnlp-main.377.pdf)
  - [Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.931.pdf)
  - [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf)
  - [Accelerated Test-Time Scaling with Model-Free Speculative Sampling](https://aclanthology.org/2025.emnlp-main.1558.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > we use GSM8K and MATH500, along with an additional dataset to assess how well our transferring-then-finetuning approach generalizes to the unseen task GPQADiamond (Rein et al., 2024). (Section 5.1).
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
