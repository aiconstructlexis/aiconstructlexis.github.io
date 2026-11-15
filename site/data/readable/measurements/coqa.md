# CoQA
**Type:** Measurement instrument  
**Supporting papers:** 28  
**Also known as:** COQA  

## State of the Field

**What it is.** Most papers treat CoQA as a conversational question answering dataset or benchmark for dialogue-based evaluation. The prevailing description is passage-based conversational comprehension: papers say it requires understanding a text passage and answering a series of interconnected questions in conversation, and one description adds that it requires coreference and pragmatic reasoning. Descriptions differ on access conditions, with several papers calling it open-book, one calling it a closed-book reading comprehension dataset, and some referring to specific subsets such as the development split or coqa-dev-v1.0.

**What it is claimed to measure.** Papers link CoQA to 4 behavioral indicators and 1 construct. The dominant measurement claim is conversational question answering, and papers also use it to measure machine reading comprehension, question answering, and extractive question answering. These measurement claims spread across several task labels rather than one label only, while a smaller line of work reports it as measuring the construct Reasoning, including evaluation framed as commonsense and math reasoning on CoQA with exact match accuracy.

**Space of uses.** Papers usually include CoQA within broader evaluation suites rather than as a standalone check. Across the surveyed uses, it appears alongside SQuAD, GSM8K, TruthfulQA, TriviaQA, and QASPER, with reported settings such as zero-shot inference, evaluation on validation or development splits, and scoring with F1 or exact match. It is also related to 1 other measurement instrument, lm-evaluation-harness, which one paper uses to conduct zero-shot inference on GSM8K and COQA.

## Sources

**CoQA** (14 papers: [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf), [INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://proceedings.iclr.cc/paper_files/paper/2024/file/0d1986a61e30e5fa408c81216a616e20-Paper-Conference.pdf), [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf), [Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/725f5e8036cc08adeba4a7c3bcbc6f2c-Paper-Conference.pdf), [Cool-Fusion: Fuse Large Language Models without Training](https://aclanthology.org/2025.acl-long.521.pdf), [MAC-Tuning: LLM Multi-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.35.pdf), [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf), [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf), [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf), [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf), [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf), [On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf), [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf), [Semantic Density: Uncertainty Quantification for Large Language Models through Confidence Measurement in Semantic Space](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26d4fbaf7dfa115f1d4b3f104e26bce-Paper-Conference.pdf))
> CoQA (Conversational Question Answering) is an open-book conversational question answering dataset used for evaluation.

**COQA** (1 paper: [HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf))
> The Conversational Question Answering benchmark, a dataset designed to evaluate dialogue-based question-answering systems.

## Relationships

### → CoQA
- **Conversational question answering** (behavioral indicator): *measured_by*, 3 papers
  > We use a relation extraction dataset ZSRE (Meng et al., 2022a) and a conversational question answering dataset CoQA (Reddy et al., 2019) to represent unrelated tasks
  - [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [Persona-Augmented Benchmarking: Evaluating LLMs Across Diverse Writing Styles](https://aclanthology.org/2025.emnlp-main.1155.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > we performed experiments on three datasets that cover a broad range of question answering settings. To be concrete, we use ... the almost 8,000 open-book questions in the development split of CoQA (Reddy et al., 2019) (Section 6).
  - [Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)
  - [MAC-Tuning: LLM Multi-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.35.pdf)
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 2 papers
  > Reading Comprehension (RC): SQuAD-3-shots [50], BoolQ-0-shot [12], and CoQA-0-shot [51].
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
- **Extractive question answering** (behavioral indicator): *measured_by*, 1 paper
  > (b) extractive question answering (SQuAD (Rajpurkar et al., 2016), CoQA (Reddy et al., 2019)) (Section 4.2)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > For standard contexts, we utilize generation tasks from LM-Eval (Gao et al., 2021), assessing model performance across commonsense and math reasoning on CoQA (Exact Match (EM) Accuracy) (Reddy et al., 2019)... (Section 5.1)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)

### Associated with
- **lm-evaluation-harness** (measurement instrument), 1 paper
  > We use the LM-Eval framework to conduct zero-shot inference on GSM8K and COQA.
  - [HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf)
