# CIFAR-10
**Type:** Measurement instrument  
**Supporting papers:** 43  
**Also known as:** CIFAR10  

## State of the Field

**What it is.** Across papers, the dominant framing is a standard or benchmark image classification dataset, most often described as 60,000 32x32 color images in 10 classes. Some definitions compress this to a 10-class object recognition or small-image classification benchmark, while a few papers describe it more situationally, for example as a testbed for clustering comparisons, automated accuracy prediction under synthetic and natural shifts, dirty-sample detection under poisoned or noisy samples, or zero-shot adversarial robustness.

**What it is claimed to measure.** Papers link it to 1 behavioral indicator and 3 constructs. The prevailing use is to measure Image classification, with studies using it for finetuning, zero-shot classification, linear probing, and downstream performance evaluation. One paper each also uses it to measure Generalization, Label noise robustness, and Multimodal alignment, so the measurement claims are centered on image classification rather than distributed evenly across several constructs.

**Space of uses.** Most papers position it as one benchmark within broader image-evaluation suites, often alongside CIFAR-100 and ImageNet, and also with STL-10, CUB, and Places365. It appears in training, fine-tuning, transfer learning, and evaluation setups, including ResNet and ViT experiments, and some papers use it more specifically to compare clustering methods, to study shifted-data accuracy prediction, or to test dirty-sample detection.

## Sources

**CIFAR-10** (16 papers: [Bootstrapping Variational Information Pursuit with Large Language and Vision Models for Interpretable Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/8e12ba543adc673da5b89c9311fcf72c-Paper-Conference.pdf), [Energy-based Automated Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5ef1df239d6640a27dd6ed9a59f518c9-Paper-Conference.pdf), [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf), [Image Clustering Conditioned on Text Criteria](https://proceedings.iclr.cc/paper_files/paper/2024/file/05b69cc4c8ff6e24c5de1ecd27223d37-Paper-Conference.pdf), [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf), [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf), [VDC: Versatile Data Cleanser based on Visual-Linguistic Inconsistency by Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/518046d86bbc41a0707727c38301ad8e-Paper-Conference.pdf), [dEBORA: Efficient Bilevel Optimization-based low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f0c4f3d83c58df58380af3b0729354c-Paper-Conference.pdf), [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf), [LM-Searcher: Cross-domain Neural Architecture Search with LLMs via Unified Numerical Encoding](https://aclanthology.org/2025.emnlp-main.478.pdf), [Beyond Accuracy: Ensuring Correct Predictions With Correct Rationales](https://proceedings.neurips.cc/paper_files/paper/2024/file/4bbeef01d9753fd5a29e9fd02d275698-Paper-Conference.pdf), [Optimistic Verifiable Training by Controlling Hardware Nondeterminism](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad885a9caafff30ee9cafdf0ee42fda2-Paper-Conference.pdf), [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf), [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf), [Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf), [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf))
> A standard image dataset with 10 object classes, used to compare the proposed text-conditioned clustering method against classical clustering algorithms.

**CIFAR10** (2 papers: [Quantum-PEFT: Ultra parameter-efficient fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e52bbb99690d1e05c7ef7b4c8b3569a-Paper-Conference.pdf), [Dynamic Sparse Training of Diagonally Sparse Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tyagi25a/tyagi25a.pdf))
> A dataset of 60,000 32x32 color images in 10 classes, used for image classification tasks.

## Relationships

### → CIFAR-10
- **Image classification** (behavioral indicator): *measured_by*, 17 papers
  > We perform experiments on the image classification task... We use CIFAR10... datasets for finetuning. (Section 3.4)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
  - [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [MCNC: Manifold-Constrained Reparameterization for Neural Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f63d2963526bdd9ff1b8bcc2dc9905a-Paper-Conference.pdf)
  - [Quantum-PEFT: Ultra parameter-efficient fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e52bbb99690d1e05c7ef7b4c8b3569a-Paper-Conference.pdf)
  - [Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
  - [Entropy-based Activation Function Optimization: A Method on Searching Better Activation Functions](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5cbee19280e1fd9d9dba8c1febf48bd-Paper-Conference.pdf)
  - [On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf)
  - [Dynamic Sparse Training of Diagonally Sparse Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tyagi25a/tyagi25a.pdf)
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)
  - [SAFE: Finding Sparse and Flat Minima to Improve Pruning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25s/lee25s.pdf)
- **Label noise robustness** (construct): *measured_by*, 1 paper
  > For this experiment, we use CIFAR10 and randomly flip p percentage of the labels in the dataset—we vary p in {10%, 30%, 50%}.
  - [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > In this section, we evaluate the generalization of discrete prompts generated by Greedy on CIFAR-10, CIFAR-100, ImageNet as well as domain generalization datasets fMoW (Christie et al., 2018) and OfficeHome (Venkateswara et al., 2017) (Section 5)
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **Multimodal alignment** (construct): *measured_by*, 1 paper
  > We start by reporting and comparing the alignment scores when using CLIP, SharedCLIP, and AlignCLIP models on the ... CIFAR-10 test datasets. (Section 4.2)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
