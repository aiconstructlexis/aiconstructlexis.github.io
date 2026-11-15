# Oxford Flowers-102
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** Flower-102, Flowers-102, Oxford Flowers, OxfordFlowers, Flowers102, Flowers  

## State of the Field

**What it is.** Across papers, the dominant framing is a flower image classification benchmark for fine-grained recognition. Definitions variously call it Flowers-102, Flower-102, Flowers102, Oxford Flowers, OxfordFlowers, or the Oxford 102 Flowers dataset, and some descriptions specify fine-grained classification of 102 different flower species or categories. Most papers describe it broadly as an image or visual classification dataset, while smaller lines of work describe it more specifically as a zero-shot classification benchmark, a few-shot learning dataset, a fine-grained visual recognition dataset, or a benchmark used to evaluate personalized and generalized performance across clients.

**What it is claimed to measure.** Papers link it to 2 behavioral indicators and no constructs. The prevailing use is to measure Image classification: papers report using Flowers102 among image classification benchmarks, to test downstream performance, or for zero-shot classification. A smaller line of work uses it to measure Fine-grained visual recognition, so the linked claims stay with behavioral indicators rather than constructs.

**Space of uses.** Papers usually place it inside broader benchmark suites rather than as a standalone protocol, alongside datasets such as Stanford Cars, CIFAR-100, Food101, and ImageNet, among others. It is also related to 1 other instrument, FGVC, with one paper stating that FGVC includes Oxford Flowers. Across these uses, authors position it as one of several visual or fine-grained classification datasets, and one paper uses it to investigate balancing personalization, generalization and privacy across clients.

## Sources

**Flowers-102** (1 paper: [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf))
> An image classification benchmark used for zero-shot classification.

**Flower-102** (1 paper: [Analyzing and Boosting the Power of Fine-Grained Visual Recognition for Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfa2f1555d46b553827af4e1557f3c9a-Paper-Conference.pdf))
> A fine-grained flower classification dataset used to evaluate FGVR performance.

**Oxford Flowers** (1 paper: [Weighted Multi-Prompt Learning with Description-free Large Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/284e7ef68bf3d8fa42abf45a39f29f5e-Paper-Conference.pdf))
> A dataset for fine-grained classification of flower species, used to evaluate few-shot learning performance.

**OxfordFlowers** (1 paper: [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf))
> A visual classification benchmark used to evaluate personalized and generalized performance across clients.

**Flowers102** (6 papers: [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf), [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf), [IPO: Interpretable Prompt Optimization for Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf), [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf), [Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf), [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf))
> Flowers102, a flower classification benchmark used to evaluate class descriptions for everyday visual categories.

**Flowers** (1 paper: [Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/27571b74d6cd650b8eb6cf1837953ae8-Paper-Conference.pdf))
> An object classification dataset, also known as the Oxford 102 Flowers dataset, designed for fine-grained image-based recognition of 102 different flower species.

## Relationships

### → Oxford Flowers-102
- **Image classification** (behavioral indicator): *measured_by*, 6 papers
  > We evaluate our method on 12 image recognition datasets. We use the ... Flowers102 (Nilsback & Zisserman, 2008)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
  - [IPO: Interpretable Prompt Optimization for Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **Fine-grained visual recognition** (behavioral indicator): *measured_by*, 1 paper
  > We conduct experiments on several popular FGVR datasets that include... Flower-102 (Nilsback & Zisserman, 2008) (Section 4.1).
  - [Analyzing and Boosting the Power of Fine-Grained Visual Recognition for Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfa2f1555d46b553827af4e1557f3c9a-Paper-Conference.pdf)

### Associated with
- **FGVC** (measurement instrument), 1 paper
  > FGVC includes five Fine-Grained Visual Classification datasets: ... Oxford Flowers (Nilsback & Zisserman, 2008)... (Section 5.1)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)
