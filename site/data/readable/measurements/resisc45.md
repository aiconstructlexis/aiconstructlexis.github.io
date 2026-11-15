# RESISC45
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** The prevailing description treats RESISC45 as a publicly available remote-sensing image or land-scene classification benchmark with 45 classes. Definitions describe it as a benchmark for Remote Sensing Image Scene Classification and as a land use dataset involving land scene classification over 45 classes. A smaller variation in wording presents it more generally as a vision benchmark, and one evaluation setup frames the task as selecting a class from a provided list.

**What it is claimed to measure.** Across papers, its measurement role is narrowly focused: it is linked to 1 behavioral indicator, Image classification, and to no constructs. Papers use RESISC45 to measure image classification, with evidence phrased as reporting performance on image classification benchmarks that include Resisc-45 and as part of evaluations spanning multiple classification domains. The claims therefore converge on a single behavioral indicator rather than being spread across multiple constructs or behaviors.

**Space of uses.** No measurement instrument is linked to it. Papers usually position RESISC45 as one component of broader benchmark suites, for example alongside CIFAR-100, Food101, Flowers102, StanfordCars, and DTD, and one paper explicitly places it among four vision-task benchmarks. In another usage pattern, it appears in fine-tuning and multimodal evaluation setups where the model is asked to choose a class for the image.

## Sources

**RESISC45** (3 papers: [Tiny Budgets, Big Gains: Parameter Placement Strategy in Parameter Super-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.321.pdf), [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf), [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf))
> The RESISC45 dataset is a publicly available benchmark for Remote Sensing Image Scene Classification (RESISC), containing 45 scene classes.

## Relationships

### → RESISC45
- **Image classification** (behavioral indicator): *measured_by*, 3 papers
  > Performance on image classification benchmarks – CIFAR-100 (C100), Food101 (F101), Flowers102 (F102), and Resisc-45 (R45). (Table 4)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
