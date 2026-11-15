# SQA3D
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across definitions, SQA3D is most commonly described as a situated 3D dataset or benchmark for situated question answering in 3D scenes. Papers variously call it human-annotated, multi-modal, and a dataset for situated understanding in real-world scenes, and one definition adds that it contains over 33,000 question-answer pairs for evaluating vision-language reasoning. Several descriptions emphasize questions posed from an embodied agent's perspective or under imaginative situations, and one paper says it emphasizes the role of "situation" in the scene context.

**What it is claimed to measure.** Papers use SQA3D to measure 3D question answering and situated question answering, and they also report it as measuring 3D understanding and vision-language reasoning. Across linked concepts, claims are spread across 3 constructs and 2 behavioral indicators rather than converging on one target. Separately, one paper says SQA3D is related to spatial reasoning, citing question types that include object identification, spatial relationships, scene-level understanding, and general reasoning.

**Space of uses.** In use, papers commonly evaluate SQA3D alongside ScanQA, describing the pair as indoor 3D VQA, visual question answering, or vision-language reasoning benchmarks, while one paper pairs it with Spartun3D as the two situated understanding datasets. One usage description formats the task as "<Situation> <Question>" with answers restricted to a phrase or single word, and another reports evaluation with exact match accuracy and EM-R. Papers therefore use it as a benchmark or dataset in 3D scene understanding and reasoning evaluations.

## Sources

**SQA3D** (5 papers: [SPARTUN3D: Situated Spatial Understanding of 3D World in Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/b633e7052970b8f5aa1a69164d99e9e8-Paper-Conference.pdf), [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf), [Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8c67fc501a50977947c5bebbc39ca8f6-Paper-Conference.pdf), [MMScan: A Multi-Modal 3D Scene Dataset with Hierarchical Grounded Language Annotations](https://proceedings.neurips.cc/paper_files/paper/2024/file/5aed0d900297bd5593afc14ff452d4a8-Paper-Datasets_and_Benchmarks_Track.pdf), [Multi-modal Situated Reasoning in 3D Scenes](https://proceedings.neurips.cc/paper_files/paper/2024/file/feaeec8ec2d3cb131fe18517ff14ec1f-Paper-Datasets_and_Benchmarks_Track.pdf))
> A human-annotated situated 3D dataset used for evaluating situated question answering capabilities.

## Relationships

### → SQA3D
- **Vision-language reasoning** (construct): *measured_by*, 1 paper
  > Evaluation of vision-language reasoning on ScanQA [5] and SQA3D [55] datasets.
  - [Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8c67fc501a50977947c5bebbc39ca8f6-Paper-Conference.pdf)
- **Situated question answering** (behavioral indicator): *measured_by*, 1 paper
  > Situated Question Answering (SQA3D): User: <Situation> <Question> The answer should be a phrase or a single word. (Table 12)
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
- **3D understanding** (construct): *measured_by*, 1 paper
  > on ScanQA and SQA3D, which do not require object referencing and grounding, we still achieve consistent performance enhancement, demonstrating improved overall 3D scene understanding and reasoning
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
- **3D question answering** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate the proposed cdViews on two widely used benchmarks of 3D-QA: ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). (Section 1)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)

### Associated with
- **Spatial reasoning** (construct), 1 paper
  > It encompasses a diverse range of question types, including object identification, spatial relationships, scene-level understanding, and general reasoning. (Section 5)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
