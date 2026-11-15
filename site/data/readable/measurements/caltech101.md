# Caltech101
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** Caltech-101  

## State of the Field

**What it is.** Most definitions describe Caltech101 as an image or object classification dataset or benchmark with 101 object categories, used for visual recognition evaluation. Papers also place it in broader evaluation setups, for example among nine benchmark datasets for image classification and in an 11-dataset image-classification suite, and one paper reports 4,331 test images from 101 classes.

**What it is claimed to measure.** Across reported links, papers use it to measure one behavioral indicator and two constructs. The recurring claim is that it measures image classification, while a smaller line of work reports that it is used to measure personalization and generalization, so the recorded uses extend beyond a single construct.

**Space of uses.** Papers commonly include it as one dataset within larger image-classification suites rather than presenting it on its own. It appears alongside datasets such as ImageNet, StanfordCars, Flowers102, CUB, and OxfordPets, with several other classification datasets also used, and papers position it in zero-shot and linear-probe evaluations as well as in multi-dataset studies of personalization and generalization.

## Sources

**Caltech101** (4 papers: [Weighted Multi-Prompt Learning with Description-free Large Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/284e7ef68bf3d8fa42abf45a39f29f5e-Paper-Conference.pdf), [Beyond Accuracy: Ensuring Correct Predictions With Correct Rationales](https://proceedings.neurips.cc/paper_files/paper/2024/file/4bbeef01d9753fd5a29e9fd02d275698-Paper-Conference.pdf), [IPO: Interpretable Prompt Optimization for Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf), [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf))
> An object classification dataset containing 101 categories used for visual recognition evaluation.

**Caltech-101** (1 paper: [Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf))
> An image dataset of 101 object categories used for evaluation.

## Relationships

### → Caltech101
- **Image classification** (behavioral indicator): *measured_by*, 2 papers
  > We evaluated the aforementioned models on four widely-used image classification benchmarks: ImageNet (shortened as , same below) [11], Flowers102 ( ) [35], StanfordCars ( ) [21], and Caltech101 ( ) [13] (Section 2.2)
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Personalization** (construct): *measured_by*, 1 paper
  > We select four visual classification datasets to investigate the task of balancing personalization, generalization and privacy: Caltech101 (Fei-Fei et al., 2004) (Section 4.1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > We select four visual classification datasets to investigate the task of balancing personalization, generalization and privacy: Caltech101 (Fei-Fei et al., 2004) (Section 4.1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
