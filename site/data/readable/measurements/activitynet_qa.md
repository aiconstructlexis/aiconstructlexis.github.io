# ActivityNet-QA
**Type:** Measurement instrument  
**Supporting papers:** 33  

## State of the Field

**What it is.** Across the surveyed work, ActivityNet-QA is most commonly described as an open-ended video question-answering benchmark or dataset built on ActivityNet videos. Definitions repeatedly frame it as covering complex web videos, longer activity videos, and complex human activities or events, with some papers emphasizing zero-shot video understanding evaluation and others describing it in terms of human activity understanding. One paper further states that it contains human-annotated QA pairs on 5,800 videos derived from ActivityNet and is designed for long-term spatiotemporal reasoning.

**What it is claimed to measure.** Papers link it to 2 constructs and 1 behavioral indicator. The prevailing usage is to measure video question answering: many papers evaluate zero-shot or open-ended VideoQA on ActivityNet-QA and refer to it directly as a video QA benchmark. A broader framing treats it as measuring video understanding, while a smaller line of work reports it as assessing spatiotemporal reasoning.

**Space of uses.** Papers usually position ActivityNet-QA as one item in broader evaluation suites, describing it as part of classical, widely used, or general video QA and video understanding benchmark collections. It appears in comparative evaluations, zero-shot video-QA settings, and comprehensive suites of video understanding benchmarks. No measurement instrument is linked to it.

## Sources

**ActivityNet-QA** (13 papers: [Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf), [VQAGuider: Guiding Multimodal Large Language Models to Answer Complex Video Questions](https://aclanthology.org/2025.acl-long.385.pdf), [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf), [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf), [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf), [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf), [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf), [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf), [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf), [Slot-VLM: Object-Event Slots for Video-Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf), [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf), [VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf), [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf))
> A video question-answering benchmark used for zero-shot video understanding evaluation.

## Relationships

### → ActivityNet-QA
- **Video question answering** (behavioral indicator): *measured_by*, 12 papers
  > Additionally, we evaluate zero-shot performance on open-ended video question-answering benchmarks such as MSVD-QA [68], ActivityNet-QA [69], MSRVTT-QA [70]... (Section 4.1)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf)
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
  - [SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25s/zhang25s.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
  - [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf)
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf)
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
- **Video understanding** (construct): *measured_by*, 5 papers
  > By scaling up the LLM to 34B, our model demonstrates a marked improvement in video understanding capabilities, achieving state-of-the-art performance on video evaluation benchmarks with accuracies of 77.4% on MSVD [68], 62.1% on MSR-VTT [70], and 55.8% on ActivityNet [69]. (Section 4.3)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **Spatiotemporal reasoning** (construct): *measured_by*, 1 paper
  > ActivityNet-QA (Yu et al., 2019) encompasses human-annotated QA pairs on 5,800 videos derived from the ActivityNet (Caba Heilbron et al., 2015) dataset. This benchmark is designed to assess the capabilities of VideoQA models in long-term spatiotemporal reasoning.
  - [Streaming Video Question-Answering with In-context Video KV-Cache Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/67a9b444cbcd647572c88194619f72d5-Paper-Conference.pdf)
