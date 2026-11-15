# MSVD-QA
**Type:** Measurement instrument  
**Supporting papers:** 31  
**Also known as:** MSVDQA, MVSD-QA  

## State of the Field

**What it is.** Across the papers, MSVD-QA is most commonly treated as a video question-answering benchmark, often described as open-ended and frequently used for zero-shot evaluation. Definitions repeatedly tie it to the Microsoft Video Description dataset or the Microsoft Research Video Description Corpus, and the name also appears as MSVDQA and, in one formulation, MVSD-QA. Some descriptions add that it assesses understanding of video content through natural-language answers to video-based questions, sometimes over short video clips, and one paper notes that MSVD-QA is derived from video retrieval datasets.

**What it is claimed to measure.** Papers link MSVD-QA to 1 construct and 2 behavioral indicators. The prevailing usage is to measure Video question answering, with many papers explicitly calling it a video QA, open-ended VideoQA, or zero-shot video question answering benchmark. A smaller line of work reports it as measuring Video understanding by placing it among video understanding benchmarks, and a minority framing uses it for Visual question answering. These claims concentrate most strongly on Video question answering rather than spreading evenly across targets.

**Space of uses.** In practice, papers usually use MSVD-QA as part of broader benchmark suites rather than on its own. It is most often evaluated alongside MSRVTT-QA and ActivityNet-QA, often with TGIF-QA, and less often with NextQA or the Video-ChatGPT test set. Papers commonly position it as a standard or classical benchmark for open-ended or zero-shot video evaluation, including comparisons within comprehensive video understanding suites.

## Sources

**MSVD-QA** (12 papers: [Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf), [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf), [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf), [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf), [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf), [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf), [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf), [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf), [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf), [Slot-VLM: Object-Event Slots for Video-Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf), [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf), [VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf))
> A video question-answering benchmark used for zero-shot video understanding evaluation.

**MSVDQA** (2 papers: [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf))
> MSVD-QA benchmark used to assess answering questions about video content.

**MVSD-QA** (1 paper: [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf))
> A video question answering benchmark based on the Microsoft Video Description Corpus.

## Relationships

### → MSVD-QA
- **Video question answering** (behavioral indicator): *measured_by*, 11 papers
  > We evaluate Emu on a broad range of vision-language tasks including ... video question answering (MSRVTTQA (Xu et al., 2017), MSVDQA (Xu et al., 2017), NextQA (Xiao et al., 2021))... (Section 5)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
  - [SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25s/zhang25s.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
  - [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf)
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf)
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
- **Video understanding** (construct): *measured_by*, 4 papers
  > By scaling up the LLM to 34B, our model demonstrates a marked improvement in video understanding capabilities, achieving state-of-the-art performance on video evaluation benchmarks with accuracies of 77.4% on MSVD [68], 62.1% on MSR-VTT [70], and 55.8% on ActivityNet [69]. (Section 4.3)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > Visual Question Answering (VQA): We evaluate the performance of visual question answering on the following benchmark datasets:... We also use MSVD-QA
  - [Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf)
