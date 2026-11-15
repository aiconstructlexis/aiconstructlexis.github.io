# CIFAR-100
**Type:** Measurement instrument  
**Supporting papers:** 34  
**Also known as:** CIFAR100  

## State of the Field

**What it is.** Across papers, it is most commonly described as an image classification benchmark or dataset with 100 classes, often framed as 100 fine-grained object classes or categories. Some definitions add that it consists of 32x32 color images, and several papers explicitly contrast it with CIFAR-10 as a more challenging or more complex setting; papers also use both spellings, CIFAR-100 and CIFAR100.

**What it is claimed to measure.** The prevailing use is to measure Image classification, which is the only linked behavioral indicator and the one attached to most papers, covering finetuning, zero-shot classification, linear probing, transfer learning, and downstream performance. Papers also link it to 2 constructs, Generalization and Multimodal alignment: one paper evaluates the generalization of discrete prompts on CIFAR-100, and another reports alignment scores on CIFAR-100 to measure multimodal alignment. Overall, the measurement claims concentrate on image classification rather than spreading evenly across constructs.

**Space of uses.** Papers do not link it to other measurement instruments directly, but they commonly use it inside multi-benchmark evaluation suites, most often alongside CIFAR-10 and ImageNet or ImageNet-1K, with other recurring companions including CUB, Food101, and DTD. Within those suites, it is typically positioned as a standard benchmark for comparing methods in clustering, concept bottleneck models, prompt-based evaluation, pruning and compression, architecture search, and robustness or shift settings; as one study puts it, there is a "Correlation comparison ... on synthetic shifted datasets of CIFAR-100" (Energy-based Automated Model Evaluation).

## Sources

**CIFAR-100** (15 papers: [Bootstrapping Variational Information Pursuit with Large Language and Vision Models for Interpretable Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/8e12ba543adc673da5b89c9311fcf72c-Paper-Conference.pdf), [Energy-based Automated Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5ef1df239d6640a27dd6ed9a59f518c9-Paper-Conference.pdf), [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf), [Image Clustering Conditioned on Text Criteria](https://proceedings.iclr.cc/paper_files/paper/2024/file/05b69cc4c8ff6e24c5de1ecd27223d37-Paper-Conference.pdf), [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf), [MCNC: Manifold-Constrained Reparameterization for Neural Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f63d2963526bdd9ff1b8bcc2dc9905a-Paper-Conference.pdf), [Enhancing Interpretable Image Classification Through LLM Agents and Conditional Concept Bottleneck Models](https://aclanthology.org/2025.acl-long.600.pdf), [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf), [LM-Searcher: Cross-domain Neural Architecture Search with LLMs via Unified Numerical Encoding](https://aclanthology.org/2025.emnlp-main.478.pdf), [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf), [Beyond Accuracy: Ensuring Correct Predictions With Correct Rationales](https://proceedings.neurips.cc/paper_files/paper/2024/file/4bbeef01d9753fd5a29e9fd02d275698-Paper-Conference.pdf), [Learning from Teaching Regularization: Generalizable Correlations Should be Easy to Imitate](https://proceedings.neurips.cc/paper_files/paper/2024/file/01ce1ae7f94d139e4917f9e4425a4f38-Paper-Conference.pdf), [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf), [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf), [Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf))
> An image dataset with 100 object classes, used to evaluate the proposed text-conditioned clustering method in a more complex setting compared to classical methods.

**CIFAR100** (1 paper: [Dynamic Sparse Training of Diagonally Sparse Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tyagi25a/tyagi25a.pdf))
> An image classification dataset similar to CIFAR10 but with 100 fine-grained classes, presenting a more challenging vision task.

## Relationships

### → CIFAR-100
- **Image classification** (behavioral indicator): *measured_by*, 16 papers
  > We perform experiments on the image classification task... We use... CIFAR100... datasets for finetuning. (Section 3.4)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
  - [Learning from Teaching Regularization: Generalizable Correlations Should be Easy to Imitate](https://proceedings.neurips.cc/paper_files/paper/2024/file/01ce1ae7f94d139e4917f9e4425a4f38-Paper-Conference.pdf)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [MCNC: Manifold-Constrained Reparameterization for Neural Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f63d2963526bdd9ff1b8bcc2dc9905a-Paper-Conference.pdf)
  - [Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf)
  - [Entropy-based Activation Function Optimization: A Method on Searching Better Activation Functions](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5cbee19280e1fd9d9dba8c1febf48bd-Paper-Conference.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf)
  - [Dynamic Sparse Training of Diagonally Sparse Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tyagi25a/tyagi25a.pdf)
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)
  - [SAFE: Finding Sparse and Flat Minima to Improve Pruning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25s/lee25s.pdf)
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.563.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > In this section, we evaluate the generalization of discrete prompts generated by Greedy on CIFAR-10, CIFAR-100, ImageNet as well as domain generalization datasets fMoW (Christie et al., 2018) and OfficeHome (Venkateswara et al., 2017) (Section 5)
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **Multimodal alignment** (construct): *measured_by*, 1 paper
  > We start by reporting and comparing the alignment scores when using CLIP, SharedCLIP, and AlignCLIP models on the ... CIFAR-100 ... test datasets. (Section 4.2)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
