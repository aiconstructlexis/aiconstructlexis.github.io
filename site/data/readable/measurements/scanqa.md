# ScanQA
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across papers, ScanQA is most commonly described as a benchmark dataset for question answering in 3D scenes, with questions grounded in objects within ScanNet scans. Some definitions present it more specifically as a 3D visual question answering dataset focused on spatial relationships and object properties, while another describes a challenging indoor 3D VQA dataset with over 41,000 question-answer pairs. A smaller line of description treats it as a multi-modal 3D scene dataset for spatial scene understanding, and one quoted passage says it is centered on ScanNet and pioneered human annotations and template-based generation.

**What it is claimed to measure.** Papers use ScanQA to measure 3 constructs and 2 behavioral indicators. The prevailing construct-level use is for 3D understanding, with additional papers reporting it as measuring 3D perception and vision-language reasoning; at the behavioral-indicator level, it is linked to 3D question answering and visual question answering. One paper explicitly says evaluations on ScanQA and SQA3D do not require object referencing and grounding while being used to demonstrate overall 3D scene understanding and reasoning, so the measurement claims span several nearby 3D understanding and question-answering targets rather than a single construct.

**Space of uses.** In use, ScanQA is often paired with SQA3D for 3D or visual question answering, and some papers place it alongside Scan2Cap as a general scene understanding task. Other work includes it in broader 3D evaluation suites with 3D-LLM tasks, nuScenes VQA, and ALFRED. Papers variously position it as a general scene understanding task, a classic validation set for 3D spatial understanding, and one of two challenging indoor 3D VQA datasets.

## Sources

**ScanQA** (4 papers: [SPARTUN3D: Situated Spatial Understanding of 3D World in Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/b633e7052970b8f5aa1a69164d99e9e8-Paper-Conference.pdf), [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf), [Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8c67fc501a50977947c5bebbc39ca8f6-Paper-Conference.pdf), [MMScan: A Multi-Modal 3D Scene Dataset with Hierarchical Grounded Language Annotations](https://proceedings.neurips.cc/paper_files/paper/2024/file/5aed0d900297bd5593afc14ff452d4a8-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark dataset for question answering in 3D scenes, where questions are grounded in objects within scans from the ScanNet dataset.

## Relationships

### → ScanQA
- **3D understanding** (construct): *measured_by*, 2 papers
  > on ScanQA and SQA3D, which do not require object referencing and grounding, we still achieve consistent performance enhancement, demonstrating improved overall 3D scene understanding and reasoning
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
- **Vision-language reasoning** (construct): *measured_by*, 1 paper
  > Evaluation of vision-language reasoning on ScanQA [5] and SQA3D [55] datasets.
  - [Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8c67fc501a50977947c5bebbc39ca8f6-Paper-Conference.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > ...and both ScanQA [2] and SQA3D [38] for visual question answering.
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
- **3D perception** (construct): *measured_by*, 1 paper
  > For 3D evaluation, we select ScanQA (3), two tasks from 3D-LLM (16), i.e., 3D-assisted Dialogue and Task Decomposition, and also curate two new test set from nuScenes VQA (6) and ALFRED (48).
  - [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf)
- **3D question answering** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate the proposed cdViews on two widely used benchmarks of 3D-QA: ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). (Section 1)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
