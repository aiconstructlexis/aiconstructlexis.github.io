# LogiQA
**Type:** Measurement instrument  
**Supporting papers:** 45  
**Also known as:** Logiqa  

## State of the Field

**What it is.** Across papers, LogiQA is most commonly described as a machine reading comprehension or question answering benchmark for logical reasoning. Definitions usually present it as multiple-choice questions grounded in a passage or logical text, where models choose the correct option; one paper describes it as expert-written and aimed at human-level logical reasoning across deductive, inductive, and abductive inference, while others frame it as reading comprehension from logic puzzles or as NLI from premises to a conclusion. A smaller line of work places it under commonsense reasoning instead.

**What it is claimed to measure.** Papers link LogiQA to five constructs and one behavioral indicator. The prevailing use is to measure logical reasoning, with broader reasoning as another recurring framing; smaller lines of work use it to measure commonsense reasoning, generalization beyond the pretraining distribution, and question answering, and papers also link it to additional constructs. Overall, the measurement claims concentrate on logical reasoning but spread across several targets.

**Space of uses.** In use, papers often place LogiQA in broader benchmark suites for reasoning, reading comprehension, language understanding, and downstream evaluation. It appears alongside PIQA, WinoGrande, WSC, and GSM8K, and papers report it in zero-shot, 5-shot, and in-context learning evaluations. Papers also relate it to one other measurement instrument, MR-Ben, where a study says the benchmark's logic questions are drawn from LogiQA.

**Concerns raised.** One profiling paper argues that its measured content differs from its marketing: although LogiQA is marketed as a logical reasoning benchmark, it is reported to lean most on temporal reasoning, and deductive reasoning is said to contribute only modestly.

## Sources

**LogiQA** (13 papers: [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf), [Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.291.pdf), [Advancing MoE Efficiency: A Collaboration-Constrained Routing (C2R) Strategy for Better Expert Parallelism Design](https://aclanthology.org/2025.naacl-long.347.pdf), [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf), [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf), [Mixture of Hidden-Dimensions: Not All Hidden-States’ Dimensions are Needed in Transformer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bc/chen25bc.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf), [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf), [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf), [MemoryFormer : Minimize Transformer Computation by Removing Fully-Connected Layers](https://proceedings.neurips.cc/paper_files/paper/2024/file/24143e25a82f856aeed58b2f497d623b-Paper-Conference.pdf), [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf), [Stacking Your Transformers: A Closer Look at Model Growth for Efficient LLM Pre-Training](https://proceedings.neurips.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf), [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf))
> A dataset for logical reasoning, where models must choose the correct option for a question based on a given logical text passage.

**Logiqa** (1 paper: [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf))
> A benchmark dataset for evaluating commonsense reasoning capabilities in language models.

## Relationships

### → LogiQA
- **Logical reasoning** (construct): *measured_by*, 8 papers
  > "LogiQA [31] collects questions about natural language inference (NLI) and requires models to infer the conclusion based on provided premises."
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
  - [Logic-of-Thought: Injecting Logic into Contexts for Full Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.510.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
  - [Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance](https://aclanthology.org/2025.emnlp-main.500.pdf)
  - [A Graph-Theoretical Framework for Analyzing the Behavior of Causal Language Models](https://aclanthology.org/2025.emnlp-main.1014.pdf)
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
- **Reasoning** (construct): *measured_by*, 3 papers
  > We evaluate Spectra Suite models using eight distinct common-sense and reasoning benchmarks consisting of tasks from logical and reasoning questions to grounded and physical commonsense tasks: Arc Easy, Arc Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), HellaSWAG (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), PIQA (Bisk et al., 2019), LAMBADA (Paperno et al., 2016), LogiQA (Liu et al., 2021), all under zero-shot settings. (Section 5)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
  - [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > In the assessments of continued QA and text understanding, we report 0-shot accuracy for LogiQA [28], 32-shot BoolQ [29], and 0-shot LAMBADA [30]. (Section 5.1)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > Commonsense Reasoning: HellaSwag (Zellers et al., 2019), SIQA (Sap et al., 2019), Wino- Grande (Sakaguchi et al., 2021), Logiqa (Liu et al., 2020).
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **Temporal reasoning** (construct): *measured_by*, 1 paper
  > “LogiQA, marketed as a logical reasoning benchmark, in fact leans most on Temporal Reasoning and Commonsense Causal Reasoning”
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)

### Associated with
- **MR-Ben** (measurement instrument), 1 paper
  > For logic questions, we draw from LogiQA [40], which encompasses a broad spectrum of logical reasoning types, including categorical, conditional, disjunctive, and conjunctive reasoning. (Section 3.1).
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
