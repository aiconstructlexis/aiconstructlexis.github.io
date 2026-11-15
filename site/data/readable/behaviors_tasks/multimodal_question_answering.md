# Multimodal question answering
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Multi-modal question answering  

## State of the Field

**Space of definitions.** Most commonly, papers treat this behavior as answering questions over inputs from more than one modality, with examples spanning images, video, audio, depth, point clouds, and text. A recurring narrower formulation focuses on joint text-image understanding, while other papers specify natural language question answering over synchronized video, audio, and sensor streams, or over non-textual biomedical inputs such as a molecule SMILES string or a protein sequence. Papers also differ on what counts as a valid response: some use multiple-choice selection, some require a single word or short phrase, and some describe generating a natural language answer.

**Variants.** The most prevalent variant uses image and text together, and one paper explicitly describes visual QA as a typical form of multimodal QA. Smaller lines of work study procedural activity understanding from video plus a textual recipe, question answering over video, audio, embedded sensors, and natural language, question answering over image and profile text, and biomedical question answering where the context includes a molecule SMILES string or protein sequence.

**Space of elicitation and scores.** Only 1 measurement instrument is linked to this behavior, Visual7W. In the recorded evaluation use, it is a dataset of multimodal samples, each containing a multiple-choice question paired with a related image, so it operationalizes multimodal question answering through image-grounded multiple-choice QA. No other measurement instrument is linked.

**What it is taken as evidence of.** No construct is linked to this behavior in the surveyed papers, so they do not specify what broader construct it is taken to evidence.

## Sources

**Multimodal question answering** (6 papers: [LLMs Can Evolve Continually on Modality for $\mathbb{X}$-Modal Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/5942d10ae51b6bd07648e54df07ef9cd-Paper-Conference.pdf), [Protecting Privacy in Multimodal Large Language Models with MLLMU-Bench](https://aclanthology.org/2025.naacl-long.207.pdf), [JMMMU: A Japanese Massive Multi-discipline Multimodal Understanding Benchmark for Culture-aware Evaluation](https://aclanthology.org/2025.naacl-long.43.pdf), [ProMQA: Question Answering Dataset for Multimodal Procedural Activity Understanding](https://aclanthology.org/2025.naacl-long.579.pdf), [RAVEN: Query-Guided Representation Alignment for Question Answering over Audio, Video, Embedded Sensors, and Natural Language](https://aclanthology.org/2025.emnlp-main.96.pdf), [BioBridge: Bridging Biomedical Foundation Models via Knowledge Graphs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a5a9f5c15632e9f52c9c1ba4134f13c-Paper-Conference.pdf))
> Answering questions about inputs from different modalities such as image, video, audio, depth, and point cloud.

**Multi-modal question answering** (1 paper: [Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities](https://aclanthology.org/2025.emnlp-main.1249.pdf))
> The task of answering questions that require processing and integrating information from multiple data modalities, such as text and images.

## Relationships

### Multimodal question answering →
- **Visual7W** (measurement instrument): *measured_by*, 1 paper
  > For evaluation, Visual7W (Zhu et al., 2016) and VMCBench (Zhang et al., 2025b) datasets are employed, which both consist of multimodal samples each containing a multiple-choice question paired with a related image.
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)
