# Multi-image visual question answering
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Multi-image question answering  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as answering a user's or textual question from information distributed across multiple provided images, often by reasoning over their content and, in some definitions, their relationships. Most definitions say only that the images are multiple, while one benchmark specifies questions involving 2 to 20 images. A smaller variation makes the output explicit as a textual answer.

**Variants.** Papers use several nearby names, including multi-image question answering, multi-image visual question answering, multi-image VQA, and MIQA. Most descriptions present it simply as question answering over a set of images, though one line of work places it in multi-turn dialogue and combines multi-image Q&A with Q&A for each individual image, so dialogues can mix single-image and multi-image questions. Another paper describes complex MIQA scenarios that involve retrieval and reasoning.

**Space of elicitation and scores.** Papers link this behavior to two measurement instruments, most often Mantis-Eval and also MMMU. In evaluation use, papers report that it is measured by Mantis-Eval, described as containing "all multi-image questions" and used to probe models' multi-image reasoning abilities, and by MMMU, described as containing both single-image and multi-image questions.

**What it is taken as evidence of.** Papers do not link this behavior to any construct.

## Sources

**Multi-image question answering** (2 papers: [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf))
> Answering a user's question based on the content and relationships of two or more provided images.

**Multi-image visual question answering** (1 paper: [JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/734abb86d3caa949f44da8a093717f61-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of answering a question by reasoning over the content of multiple provided images.

## Relationships

### Multi-image visual question answering →
- **Mantis-Eval** (measurement instrument): *measured_by*, 2 papers
  > We additionally evaluate models on ... Mantis-Eval [Jiang et al., 2024](all multi-image questions) to probe a model’s multi-image reasoning abilities... (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/734abb86d3caa949f44da8a093717f61-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMMU** (measurement instrument): *measured_by*, 1 paper
  > We additionally evaluate models on MMMU [Yue et al., 2024](containing both single and multi-image questions)... (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
