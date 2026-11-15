# Commonsense170K
**Type:** Measurement instrument  
**Supporting papers:** 21  
**Also known as:** COMMONSENSE170K, Common-sense170K, CSR-170k, Commonsense-170K, CSR170K, Commonsense170k  

## State of the Field

**What it is.** Across papers, the prevailing description is a large-scale commonsense reasoning dataset for supervised fine-tuning, usually presented as a mixture or combination of eight datasets or subtasks. Definitions variously call it a training dataset, a benchmark, or a language evaluation suite, and several specify components such as BoolQ, PIQA, SIQA, HellaSwag, Wino or WinoGrande, ARC-Easy or ARC-Challenge, and OpenBookQA or OBQA. One paper also describes it as "a comprehensive collection of commonsense reasoning questions" with 170020 training samples and 400 validation samples.

**What it is claimed to measure.** Papers link it to 1 construct, Commonsense reasoning, and to no behavioral indicators, so the reported measurement claims concentrate on a single construct. The dominant wording is that Commonsense reasoning is measured by Commonsense170K, while some papers frame the connection more loosely by describing fine-tuning or evaluation on a combined dataset of eight commonsense reasoning tasks.

**Space of uses.** Most papers use it as the resource on which models are fine-tuned for commonsense reasoning, often before evaluation on downstream tasks or benchmarks, and some explicitly say it is used for both training and evaluation. Papers repeatedly describe first fine-tuning a model on Commonsense170K and then testing on downstream tasks, and no other measurement instrument is linked to it.

## Sources

**COMMONSENSE170K** (1 paper: [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf))
> A training dataset of commonsense reasoning questions used to fine-tune a single model before evaluation on downstream commonsense benchmarks.

**Commonsense170K** (4 papers: [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf), [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf), [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf))
> A large-scale dataset for supervised fine-tuning focused on commonsense reasoning tasks.

**Common-sense170K** (1 paper: [DoMIX: An Efficient Framework for Exploiting Domain Knowledge in Fine-Tuning](https://aclanthology.org/2025.acl-long.710.pdf))
> A large training dataset for commonsense reasoning, constructed from eight different subtasks, used for fine-tuning models.

**CSR-170k** (1 paper: [SAN: Hypothesizing Long-Term Synaptic Development and Neural Engram Mechanism in Scalable Model’s Parameter-Efficient Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25e/dai25e.pdf))
> Commonsense Reasoning 170k, a language evaluation suite containing multiple commonsense reasoning datasets used to assess LLM performance on commonsense question answering tasks.

**Commonsense-170K** (1 paper: [LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf))
> Dataset used for fine-tuning and evaluating commonsense reasoning across multiple tasks such as BoolQ, PIQA, SIQA, HellaSwag, Wino, ARC-e, ARC-c, and OBQA.

**CSR170K** (1 paper: [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf))
> A composite benchmark for commonsense reasoning, comprising eight different datasets including BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-Easy, ARC-Challenge, and OpenbookQA.

## Relationships

### → Commonsense170K
- **Commonsense reasoning** (construct): *measured_by*, 7 papers
  > Specifically, we leverage Commonsense170K (Hu et al., 2023), which is a combination of eight commonsense reasoning datasets... for both training and evaluation. (Section 5)
  - [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf)
  - [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf)
  - [Sketch to Adapt: Fine-Tunable Sketches for Efficient LLM Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bs/zhang25bs.pdf)
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf)
  - [NeuroAda: Activating Each Neuron's Potential for Parameter-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.555.pdf)
