# Commonsense reasoning benchmark
**Type:** Measurement instrument  
**Supporting papers:** 7  
**Also known as:** Commonsense Reasoning benchmark, Commonsense Benchmark, Commonsense reasoning benchmarks, Commonsense Reasoning Tasks  

## State of the Field

**What it is.** Across papers, the prevailing description is a composite commonsense evaluation suite built from eight tasks or datasets. Definitions usually list BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, and other ARC/OBQA components, and describe either aggregated training with individual test evaluation or a suite for commonsense question answering and inference. A smaller difference is whether ARC is split into ARC-e and ARC-c or referred to more broadly as ARC, and one definition frames the suite as covering factual, physical, social, and scientific inference.

**What it is claimed to measure.** Its measurement claims are focused: papers link it to one construct, Commonsense reasoning, and one behavioral indicator, Catastrophic forgetting. The prevailing usage is to measure commonsense reasoning, with papers reporting evaluation on the benchmark or on its constituent tasks for that purpose. A smaller usage treats performance on the commonsense reasoning QA task after instruction-following training as measuring catastrophic forgetting, described as assessing knowledge forgetting.

**Space of uses.** Papers commonly use it as a composite benchmark rather than as a standalone single dataset, and it is linked to one other measurement instrument, BoolQ, as a related component of the suite. Several descriptions present a setup in which training sets from the component datasets are aggregated, sometimes using a predefined split, and testing is done on the individual tasks. In a less common pairing, results on this benchmark are reported alongside zero-shot MMLU.

## Sources

**Commonsense Reasoning benchmark** (1 paper: [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf))
> A collection of eight sub-tasks (BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-e, ARC-c, OBQA) used to evaluate language models on reasoning about everyday situations, with combined training and individual test evaluation.

**Commonsense Benchmark** (1 paper: [From Weight-Based to State-Based Fine-Tuning: Further Memory Reduction on LoRA with Parallel Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25au/zhang25au.pdf))
> A composite evaluation suite assessing model performance on multiple tasks requiring commonsense reasoning, including BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-e, ARC-c, and OBQA.

**Commonsense reasoning benchmarks** (1 paper: [FouRA: Fourier Low-Rank Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/83960718b4d12f799985206f1b1cf00f-Paper-Conference.pdf))
> A collection of benchmark tasks used to evaluate commonsense question answering and inference, including BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC, and OBQA.

**Commonsense Reasoning Tasks** (1 paper: [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf))
> A collection of eight commonsense reasoning datasets used for evaluating a model's ability in factual, physical, social, and scientific inference.

## Relationships

### → Commonsense reasoning benchmark
- **Commonsense reasoning** (construct): *measured_by*, 5 papers
  > “We also evaluate on Commonsense Reasoning benchmarks BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC and OBQA.”
  - [FouRA: Fourier Low-Rank Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/83960718b4d12f799985206f1b1cf00f-Paper-Conference.pdf)
  - [Segment-Based Attention Masking for GPTs](https://aclanthology.org/2025.acl-long.947.pdf)
  - [BSLoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25k/zhou25k.pdf)
  - [Sketch to Adapt: Fine-Tunable Sketches for Efficient LLM Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bs/zhang25bs.pdf)
  - [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator): *measured_by*, 1 paper
  > we also evaluate on the commonsense reasoning QA task after training on the instruction-following datasets to assess knowledge forgetting. (Section 5.1)
  - [Weights-Rotated Preference Optimization for Large Language Models](https://aclanthology.org/2025.emnlp-main.1329.pdf)

### Associated with
- **BoolQ** (measurement instrument), 1 paper
  > Our benchmark contains eight commonsense reasoning datasets, including BoolQ [Clark et al., 2019], PIQA [Bisk et al., 2020], SIQA [Sap et al., 2019], HellaSwag [Zellers et al., 2019], WinoGrande [Sakaguchi et al., 2021], ARC-e, ARC-c [Clark et al., 2018], and OBQA [Mihaylov et al., 2018]. (Section 4.2)
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)
