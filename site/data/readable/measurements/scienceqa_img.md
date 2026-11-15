# ScienceQA-IMG
**Type:** Measurement instrument  
**Supporting papers:** 9  
**Also known as:** SciQA-IMG, SQA-I, SQAI  

## State of the Field

**What it is.** Across papers, the prevailing usage treats ScienceQA-IMG, also written as SciQA-IMG, SQAI, or SQA-I, as a multimodal science question answering benchmark with image or visual context. Most descriptions say it contains image-based questions and evaluates reasoning over visual and textual context in science-related problems, while one definition presents SQA-I more specifically as the image-based subset of the ScienceQA benchmark.

**What it is claimed to measure.** Papers use it to measure two constructs and no behavioral indicators: Language bias and Visual understanding. One paper reports zero-shot performance on ScienceQA-IMG and says a model outperforms others by "successfully alleviating language bias," while another uses it when reporting "superior image understanding capabilities"; the reported uses are therefore split across those two constructs rather than centered on a single named target.

**Space of uses.** Papers often position it as one member of broader evaluation suites: quoted passages describe evaluating models across eight vision-language tasks, 11 mainstream benchmarks, or widely-adopted VLM benchmarks that include ScienceQA-IMG. In these descriptions it appears alongside MMMU, MathVista, and AI2D, and one paper reports accuracy for SciQA-IMG across five resolutions and selects it as a reference task for low-resolution needs.

## Sources

**ScienceQA-IMG** (4 papers: [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf), [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf), [Unified Generative and Discriminative Training for Multi-modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/29416b66c2149872b9d1415a3fd2c5e0-Paper-Conference.pdf), [Unveiling Encoder-Free Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5e2217482fa75556f1970be809acd3f8-Paper-Conference.pdf))
> A multimodal science question answering benchmark that includes questions with visual context from images.

**SciQA-IMG** (1 paper: [Task-Aware Resolution Optimization for Visual Large Language Models](https://aclanthology.org/2025.emnlp-main.795.pdf))
> Science Question Answering dataset with image-based questions assessing scientific reasoning from visual content.

**SQA-I** (1 paper: [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf))
> The image-based subset of the ScienceQA benchmark, which involves multimodal reasoning for science question answering.

**SQAI** (1 paper: [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf))
> A science question answering benchmark used to evaluate multimodal reasoning on science-related questions.

## Relationships

### → ScienceQA-IMG
- **Language bias** (construct): *measured_by*, 1 paper
  > Zero-shot performance of different VLMs on ScienceQA-IMG dataset in different split. MMICL outperforms other VLMs by successfully alleviating language bias. (Table 5)
  - [MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf)
- **Visual understanding** (construct): *measured_by*, 1 paper
  > TinyGroundingGPT-3B demonstrates superior image understanding capabilities on the VQAv2, GQA, SQA, and POPE benchmarks
  - [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf)
