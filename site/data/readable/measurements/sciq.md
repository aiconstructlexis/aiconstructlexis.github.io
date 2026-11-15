# SciQ
**Type:** Measurement instrument  
**Supporting papers:** 80  
**Also known as:** SCIQ  

## State of the Field

**What it is.** Across the surveyed papers, SciQ is most commonly described as a benchmark or dataset for scientific question answering built from multiple-choice science exam questions. Several definitions also call it a crowdsourced science-question dataset, and some add supporting paragraphs or annotated support. A smaller line of work describes its use more broadly, as reading comprehension, commonsense question answering, natural language understanding, or phrase-level and free-form question answering; one paper uses a LitCab test split, and another uses it for short responses.

**What it is claimed to measure.** Papers link SciQ to 6 constructs and 3 behavioral indicators. The prevailing usage is to measure Commonsense reasoning, with additional papers using it to measure General ability, Scientific knowledge, Scientific reasoning, Out-of-distribution generalization, and 1 other construct. At the behavioral level, it is used for Multiple-choice question answering most often, and also for Question answering and Open-ended question answering. One line of work explicitly says it measures scientific reasoning by challenging models to apply scientific concepts beyond mere fact recall.

**Space of uses.** In practice, papers usually place SciQ inside broader benchmark suites rather than using it alone, recurring alongside ARC variants, PIQA, WinoGrande, HellaSwag, and TriviaQA in reported evaluations. Only 1 other measurement instrument is directly related to it, lm-evaluation-harness, and papers report evaluating SciQ through that harness. Other uses treat it as a downstream benchmark, an out-of-distribution reasoning check, or a science-domain question-answering dataset for uncertainty, confidence estimation, and retrieval-augmented settings.

## Sources

**SciQ** (17 papers: [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf), [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf), [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf), [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf), [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.575.pdf), [From Evidence to Belief: A Bayesian Epistemology Approach to Language Models](https://aclanthology.org/2025.naacl-long.531.pdf), [Advancing MoE Efficiency: A Collaboration-Constrained Routing (C2R) Strategy for Better Expert Parallelism Design](https://aclanthology.org/2025.naacl-long.347.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf), [TrimLLM: Progressive Layer Dropping for Domain-Specific LLMs](https://aclanthology.org/2025.acl-long.33.pdf), [Mixture of Hidden-Dimensions: Not All Hidden-States’ Dimensions are Needed in Transformer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bc/chen25bc.pdf), [Too Consistent to Detect: A Study of Self-Consistent Errors in LLMs](https://aclanthology.org/2025.emnlp-main.238.pdf), [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf), [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf), [LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf), [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf), [Semantic Density: Uncertainty Quantification for Large Language Models through Confidence Measurement in Semantic Space](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26d4fbaf7dfa115f1d4b3f104e26bce-Paper-Conference.pdf), [Stacking Your Transformers: A Closer Look at Model Growth for Efficient LLM Pre-Training](https://proceedings.neurips.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf))
> A benchmark for scientific question answering, consisting of multiple-choice questions sourced from science exams.

**SCIQ** (1 paper: [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf))
> A benchmark dataset with about 13,000 multiple-choice science questions.

## Relationships

### → SciQ
- **Commonsense reasoning** (construct): *measured_by*, 7 papers
  > For common sense and reading comprehension tasks, we report 0-shot accuracy results for SciQ [22], PIQA [23], WinoGrande (Wino.) [24], ARC Easy(ARC-E.) [25], and HellaSwag (HellaS.) [26], alongside 25-shot accuracy for ARC Challenge (ARC-C.) [27]. (Section 5.1)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
  - [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf)
  - [Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 3 papers
  > The Science Questions (SciQ) dataset [73] consists of 13,679 crowdsourced multiple choice science exam questions ranging across physics, chemistry, biology, earth science, astronomy, and computer science. (Appendix E)
  - [LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf)
  - [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **Scientific reasoning** (construct): *measured_by*, 2 papers
  > SciQ measures scientific reasoning, challenging models to apply scientific concepts beyond mere fact recall. (Section 4.2)
  - [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > Following Tian et al. (2023), we use two question-answering datasets: (1) SciQ (Welbl et al., 2017) contains crowd-sourced science exam questions (Section 4.3).
  - [Calibrating Expressions of Certainty](https://proceedings.iclr.cc/paper_files/paper/2025/file/66b35d2e8d524706f39cc21f5337b002-Paper-Conference.pdf)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
- **Scientific knowledge** (construct): *measured_by*, 2 papers
  > SciQ (Welbl et al., 2017) for science-related abilities. (Section 3.1)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
- **General ability** (construct): *measured_by*, 2 papers
  > “These models are trained further and evaluated on downstream tasks: ... SciQ (Welbl et al., 2017)”
  - [STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including... SciQ... (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Open-ended question answering** (behavioral indicator): *measured_by*, 1 paper
  > We cover four open-ended quenstion-answering datasets: TriviaQA (Joshi et al., 2017), Sciq (Welbl et al., 2017), WikiQA (Yang et al., 2015), and NQ (Kwiatkowski et al., 2019). (Section 4.1)
  - [Influences on LLM Calibration: A Study of Response Agreement, Loss Functions, and Prompt Styles](https://aclanthology.org/2025.acl-long.188.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)

### Associated with
- **lm-evaluation-harness** (measurement instrument), 2 papers
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
