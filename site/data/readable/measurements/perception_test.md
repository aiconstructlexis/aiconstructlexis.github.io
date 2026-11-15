# Perception Test
**Type:** Measurement instrument  
**Supporting papers:** 11  
**Also known as:** PerceptionTest  

## State of the Field

**What it is.** Across these papers, Perception Test is most commonly described as a video perception or video understanding benchmark, often framed as a diagnostic for multimodal video models or MLLMs. Definitions recurrently say it assesses visual understanding over video sequences and fine-grained perception, and several also extend this to reasoning, logical inference, scene understanding, object tracking, and spatial awareness. Some authors narrow it to a video multiple-choice question answering dataset, while others describe an open-set benchmark with action-related questions or a diagnostic that covers skills such as memory, abstraction, physics, and semantics across video, audio, and text modalities.

**What it is claimed to measure.** Across the surveyed use, claims mostly converge on Video understanding: papers use Perception Test to measure that construct, and papers link it to 2 constructs in total and no behavioral indicators. One paper additionally reports that Perception Test is related to Reasoning, describing it as focused on skills and types of reasoning such as descriptive, explanatory, predictive, and counterfactual reasoning.

**Space of uses.** Most papers position Perception Test as one benchmark within broader evaluation suites rather than as a standalone protocol. It is commonly used alongside ActivityNet-QA, EgoSchema, MVBench, NExT-QA, and VideoMME, and some papers explicitly place it among multiple-choice video benchmarks. A smaller line of work uses an action-tagged subset of its questions, and another repurposes it as a source dataset for action localization and related task repurposing; papers do not describe it as linked to other measurement instruments.

## Sources

**PerceptionTest** (5 papers: [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf), [HAIC: Improving Human Action Understanding and Generation with Better Captions for Multi-modal Large Language Models](https://aclanthology.org/2025.acl-long.501.pdf), [MMInference: Accelerating Pre-filling for Long-Context Visual Language Models via Modality-Aware Permutation Sparse Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25aq/li25aq.pdf), [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf), [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf))
> A video perception benchmark used to assess visual understanding over video sequences.

**Perception Test** (5 papers: [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf), [Addressing Blind Guessing: Calibration of Selection Bias in Multiple-Choice Question Answering by Video Language Models](https://aclanthology.org/2025.acl-long.162.pdf), [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf), [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf), [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf))
> Perception Test (Patraucean et al., 2024) is a benchmark that focuses on the perception and reasoning skills of MLLMs.

## Relationships

### → Perception Test
- **Video understanding** (construct): *measured_by*, 2 papers
  > We evaluate our model on a comprehensive suite of video understanding benchmarks... as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (P˘atr˘aucean et al., 2023).
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)

### Associated with
- **Reasoning** (construct), 1 paper
  > The Perception test [45] focused on skills (memory, abstraction, physics, semantics) and types of reasoning (descriptive, explanatory, predictive, counterfactual) across video, audio, and text modalities. (Section 2)
  - [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf)
