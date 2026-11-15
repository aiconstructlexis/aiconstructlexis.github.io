# QNLI
**Type:** Measurement instrument  
**Supporting papers:** 35  

## State of the Field

**What it is.** Across the surveyed work, QNLI is most commonly described as a question-answering natural language inference benchmark or dataset, often said to be derived from SQuAD. The prevailing formulation is an entailment-style, usually binary, classification task over question-sentence pairs, though some papers describe question-paragraph pairs instead, where the model determines whether the context sentence contains the answer to the question. A smaller set of definitions frames the same setup as question answering cast as textual entailment.

**What it is claimed to measure.** Papers link QNLI to 2 constructs and 3 behavioral indicators, and the dominant claim is that it measures natural language inference. Smaller lines of work also report it as measuring question answering and text classification, while only a few papers treat it as measuring natural language understanding or reasoning. Overall, the reported measurement claims center on natural language inference, with a smaller set of broader or alternative framings.

**Space of uses.** The only linked instrument is GLUE, to which QNLI is related, and many papers position it as one task within GLUE evaluations. In practice, papers use it alongside MNLI, RTE, SST-2, MRPC, and QQP, and they commonly report it in broader evaluations of fine-tuning, pruning, compression, and in-context learning settings. Several descriptions present QNLI through accuracy tables or zero-shot and few-shot results rather than as a standalone protocol.

**Concerns raised.** A specific concern appears in prompt-based evaluation: one paper reports that an ICL template with the content-free token "Question: N/A, Sentence: N/A, Answer:" biases QNLI predictions toward "entailment".

## Sources

**QNLI** (23 papers: [Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/45fc8e1c55df116b23488f3cdb2fc642-Paper-Conference.pdf), [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf), [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf), [Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce806d8b4bf38cd92d483e5a0490d983-Paper-Conference.pdf), [ReLoRA: High-Rank Training Through Low-Rank Updates](https://proceedings.iclr.cc/paper_files/paper/2024/file/d6fdc308a3b0f017f16059e5888f3346-Paper-Conference.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [Improving Language Model Distillation through Hidden State Matching](https://proceedings.iclr.cc/paper_files/paper/2025/file/2fb462e23667ad5e6471a4e9af8e4774-Paper-Conference.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf), [Making Language Models Robust Against Negation](https://aclanthology.org/2025.naacl-long.413.pdf), [D.Va: Validate Your Demonstration First Before You Use It](https://aclanthology.org/2025.acl-long.129.pdf), [Beyond Zero Initialization: Investigating the Impact of Non-Zero Initialization on LoRA Fine-Tuning Dynamics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bm/li25bm.pdf), [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf), [FISTAPruner: Layer-wise Post-training Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.1498.pdf), [MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines](https://aclanthology.org/2025.emnlp-main.1022.pdf), [NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1769.pdf), [Surprise Calibration for Better In-Context Learning](https://aclanthology.org/2025.emnlp-main.1175.pdf), [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf), [Topic Coverage-based Demonstration Retrieval for In-Context Learning](https://aclanthology.org/2025.emnlp-main.1007.pdf), [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf), [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf), [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf))
> A question-answering natural language inference benchmark used to evaluate entailment classification for question-sentence pairs.

## Relationships

### → QNLI
- **Natural language inference** (behavioral indicator): *measured_by*, 7 papers
  > “Natural Language Inference (MNLI, RTE, QNLI)”
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
  - [Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b79416c0dc4b09feaa169ed5cdd63d4-Paper-Conference.pdf)
  - [Topic Coverage-based Demonstration Retrieval for In-Context Learning](https://aclanthology.org/2025.emnlp-main.1007.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
- **Natural language understanding** (construct): *measured_by*, 1 paper
  > The experiments involved 4 NLU benchmarks: RTE (Wang et al., 2019), COLA (Wang et al., 2019), 20NG (Lang, 1995) and QNLI (Wang et al., 2019) (Section 4).
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > For inference ability, we choose six datasets including Hellaswag [48], PIQA [1], WinoGrande [32], QNLI [31], MNLI [44], and WikiText2 [28] for evaluation.
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text classification** (behavioral indicator): *measured_by*, 1 paper
  > QNLI: This is a dataset containing sentence pairs for binary classification (entailment/not entailment). (Section 5)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > ...and QNLI for question answering (Wang et al., 2018). (Section 4.1)
  - [NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1769.pdf)

### Associated with
- **GLUE** (measurement instrument), 3 papers
  > We first evaluate the language understanding tasks from the GLUE benchmark(Wang et al., 2018) including MNLI, SST2, QNLI and QQP using the RoBERTa model.
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
