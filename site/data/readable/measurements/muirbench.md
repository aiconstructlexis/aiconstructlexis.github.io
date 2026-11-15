# MuirBench
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** MUIRBENCH  

## State of the Field

**What it is.** Papers most commonly describe MuirBench as a multi-image, multimodal benchmark for evaluating understanding or reasoning across multiple images. The definitions converge on its focus on integrating information from diverse visual inputs and assessing image relationships, and one paper introduces it as a "comprehensive benchmark" for multi-image understanding; the documented task areas include counting, diagram understanding, image-text matching, scene understanding, and visual retrieval.

**What it is claimed to measure.** Across the linked uses, papers use MuirBench to measure 2 constructs and 4 behavioral indicators, rather than tying it to a single target. The construct-level claims center on multi-image reasoning and scene understanding, and the behavioral indicators are counting, cross-modal retrieval, diagram understanding, and information retrieval; the task descriptions say these cover counting specific objects across multiple images, understanding diagrams, matching text and visual content, understanding scenes from multiple surveillance images, and retrieving images that contain the same building.

**Space of uses.** No other measurement instrument is linked to MuirBench. Papers use it as an evaluation benchmark for reporting and comparing model performance on multi-image understanding, for example by giving a model's score on MuirBench and noting a remaining performance gap relative to another model.

**Concerns raised.** The main concern raised in the descriptions is scope: one paper states that MuirBench "does not consider spatial relationships between objects in multiple images," and the definition likewise says it does not cover spatial relationships.

## Sources

**MUIRBENCH** (1 paper: [MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf))
> A multi-image evaluation benchmark that assesses various image relationships but does not cover spatial relationships.

**MuirBench** (1 paper: [MAmmoTH-VL: Eliciting Multimodal Reasoning with Instruction Tuning at Scale](https://aclanthology.org/2025.acl-long.680.pdf))
> Multimodal benchmark evaluating reasoning across multiple images, testing a model's ability to integrate information from diverse visual inputs.

## Relationships

### → MuirBench
- **Multi-image reasoning** (construct): *measured_by*, 1 paper
  > we introduce MUIRBENCH (MULTI-IMAGE UNDERSTANDING BENCHMARK), a comprehensive benchmark designed to rigorously assess and evaluate multi-image understanding by multimodal LLMs. (Section 2)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Counting** (behavioral indicator): *measured_by*, 1 paper
  > [COUNTING] aims to evaluate the ability of models to count the number of specific objects across multiple images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Diagram understanding** (behavioral indicator): *measured_by*, 1 paper
  > [DIAGRAM UNDERSTANDING] aims to evaluate the ability of models to understand information conveyed in diagram images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Cross-modal retrieval** (behavioral indicator): *measured_by*, 1 paper
  > [IMAGE-TEXT MATCHING] aims to evaluate the ability of models to understand the meaning of a text snippet and match it with the corresponding visual content or vice versa. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Scene understanding** (construct): *measured_by*, 1 paper
  > [SCENE UNDERSTANDING] aims to evaluate the ability of models to understand a scene comprised of multiple views from multiple surveillance images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > [VISUAL RETRIEVAL] aims to evaluate the ability of models to retrieval images that contain the same building. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
