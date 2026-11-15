# LVIS
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across papers, LVIS is most commonly described as a large-vocabulary instance segmentation dataset or benchmark used for evaluation. Definitions repeatedly emphasize a long-tail version with annotations for over 1000 object categories, while one paper describes a commonly used zero-shot LVIS with 1,203 categories. Papers also refer to its validation dataset or validation sets, and some describe it as being used to evaluate object-level classification when a model is prompted with a visual region.

**What it is claimed to measure.** Papers use LVIS to measure 2 behavioral indicators, Instance segmentation and Open-vocabulary object detection, and no constructs are linked to it. These linked claims stay at the behavioral level, though some definitions also describe LVIS as assessing object-level classification performance, including referring classification scored with Semantic Similarity and Semantic Intersection over Union.

**Space of uses.** No other measurement instrument is linked to LVIS. Papers mainly position it as an evaluation benchmark: they report results on object detection, instance segmentation, and open-vocabulary recognition or segmentation, and in one usage they form 1,748 Referring Object Classification questions from the LVIS validation dataset, with 1,548 for test and 200 for validation; another quoted passage reports referring classification results on LVIS and PACO.

## Sources

**LVIS** (4 papers: [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf), [ControlMLLM: Training-Free Visual Prompt Learning for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4fd96b997454b5b02698595df70fccaf-Paper-Conference.pdf), [Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf), [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf))
> Large Vocabulary Instance Segmentation (LVIS) is a dataset used here to evaluate a model's object-level classification performance when prompted with a visual region.

## Relationships

### → LVIS
- **Instance segmentation** (behavioral indicator): *measured_by*, 1 paper
  > Experimental results on the long-tail instance segmentation dataset (LVIS) show that our method surpasses the previous open-ended method on the object detection task and can provide additional instance segmentation masks. (Abstract)
  - [Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf)
- **Open-vocabulary object detection** (behavioral indicator): *measured_by*, 1 paper
  > our model is evaluated on the commonly used zero-shot LVIS (Gupta et al., 2019) dataset, which contains 1,203 categories. (Section 4)
  - [Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf)
