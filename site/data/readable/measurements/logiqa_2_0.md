# LogiQA 2.0
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** LogiQA 2, LogiQA2  

## State of the Field

**What it is.** Across definitions, the prevailing usage treats LogiQA 2.0, often written as LogiQA2 or LogiQA 2, as a benchmark or dataset for logical reasoning and logical question answering. Papers describe it as requiring logical reasoning over text, and some specify a multiple-choice format, including "logical reasoning multi-choice QA" and multiple-choice questions derived from professional exams that require deductive reasoning. A smaller strand presents it as an improved version of LogiQA for machine reading comprehension, and one quoted passage describes LogiQA2 as a revision and re-annotation of LogiQA.

**What it is claimed to measure.** Papers link it to 5 constructs and 1 behavioral indicator. The most common claim is that it measures Logical reasoning; other papers use it to measure Commonsense reasoning, Executive function, Generalization, and Reasoning, and one paper uses it for the behavioral indicator Multiple-choice question answering. Overall, its reported measurement role is spread across several reasoning-related constructs rather than confined to a single framing.

**Space of uses.** Across papers, it is usually one component of broader evaluation suites rather than a standalone check. It is related to lm-evaluation-harness in one zero-shot downstream setup, and other papers place it in 5-shot evaluations, 0-shot reporting, an executive-skills subset, or multi-benchmark comparisons alongside StrategyQA, GSM8K, WinoGrande, CLadder, and SciQ.

## Sources

**LogiQA2** (4 papers: [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf), [Warmup Generations: A Task-Agnostic Approach for Guiding Sequence-to-Sequence Learning with Unsupervised Initial State Generation](https://aclanthology.org/2025.acl-long.434.pdf), [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf), [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf))
> A benchmark for logical question answering, requiring models to perform logical reasoning over text.

**LogiQA 2** (1 paper: [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf))
> A logical reasoning benchmark used in a 5-shot evaluation setting.

**LogiQA 2.0** (2 papers: [RiOT: Efficient Prompt Refinement with Residual Optimization Tree](https://aclanthology.org/2025.acl-long.1086.pdf), [Playpen: An Environment for Exploring Learning From Dialogue Game Feedback](https://aclanthology.org/2025.emnlp-main.1517.pdf))
> LogiQA 2.0 is a benchmark dataset designed to evaluate a model's logical reasoning capabilities.

## Relationships

### → LogiQA 2.0
- **Logical reasoning** (construct): *measured_by*, 2 papers
  > LogiQA2 [Liu et al., 2023] is a revision and re-annotation of LogiQA [Liu et al., 2021], a logical reasoning reading comprehension dataset. (Appendix C.1)
  - [Self-playing Adversarial Language Game Enhances LLM Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4be7e9867ef163563f4a5e90cec478f-Paper-Conference.pdf)
  - [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including... LogiQA 2... (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > LogiQA2 (Liu et al., 2023) for logical reasoning multi-choice QA;
  - [Warmup Generations: A Task-Agnostic Approach for Guiding Sequence-to-Sequence Learning with Unsupervised Initial State Generation](https://aclanthology.org/2025.acl-long.434.pdf)
- **Executive function** (construct): *measured_by*, 1 paper
  > Executive includes LogiQA 2.0, CLadder, and WinoGrande (Table 2).
  - [Playpen: An Environment for Exploring Learning From Dialogue Game Feedback](https://aclanthology.org/2025.emnlp-main.1517.pdf)

### Associated with
- **lm-evaluation-harness** (measurement instrument), 1 paper
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
