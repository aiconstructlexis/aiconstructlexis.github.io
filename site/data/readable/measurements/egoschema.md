# EgoSchema
**Type:** Measurement instrument  
**Supporting papers:** 31  
**Also known as:** Egoschema, Ego-Schema  

## State of the Field

**What it is.** Across papers, EgoSchema is most commonly treated as a benchmark, often called a benchmark dataset, for long-form or long video question answering on egocentric videos. Some descriptions frame it more broadly as a benchmark for very long-form or long-context video-language understanding, but the recurring details are multiple-choice questions over egocentric videos, often described as over 5K videos or 5000 questions and as three-minute videos or videos with an average length of 3 minutes. Some papers further specify evaluation slices such as a 500-question subset, the full test split, or a 5031-video test set.

**What it is claimed to measure.** Papers link EgoSchema to 4 constructs and 1 behavioral indicator. The prevailing measurement claims are that it measures video understanding and long video understanding, and papers also use it to measure egocentric video understanding, temporal reasoning, and the behavioral indicator video question answering. Overall, papers use it across several targets rather than tying it to only one.

**Space of uses.** Papers do not describe EgoSchema through direct instrument-to-instrument relationship claims. Instead, they usually deploy it as one item in broader benchmark suites, often alongside VideoMME and NExT-QA, and also with MLVU, LongVideoBench, and MovieChat-1K. In practice, authors report top-1 accuracy, zero-shot results on the full test split, or results on a 500-question subset.

## Sources

**EgoSchema** (9 papers: [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf), [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf), [MovieCORE: COgnitive REasoning in Movies](https://aclanthology.org/2025.emnlp-main.66.pdf), [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf), [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf), [Slot-VLM: Object-Event Slots for Video-Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf), [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf), [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf), [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf))
> A benchmark dataset for long-form video question answering, designed to measure causal and temporal reasoning abilities in egocentric videos.

**Egoschema** (1 paper: [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf))
> A benchmark for evaluating long video question answering capabilities, particularly focusing on egocentric videos.

**Ego-Schema** (1 paper: [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf))
> A Video Question-Answering benchmark focused on long-form, egocentric video understanding.

## Relationships

### → EgoSchema
- **Video question answering** (behavioral indicator): *measured_by*, 6 papers
  > We use Egoschema (Mangalam et al., 2023) and VideoMME (Fu et al., 2024) to evaluate the long video capabilities of VideoChat-T.
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
  - [$∞$-Video: A Training-Free Approach to Long Video Understanding via Continuous-Time Memory Consolidation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/santos25a/santos25a.pdf)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
- **Video understanding** (construct): *measured_by*, 4 papers
  > “and (b) multi-choice video question answering benchmarks: NExT-QA (Xiao et al., 2021), IntentQA (Li et al., 2023b), and EgoSchema (Mangalam et al., 2024).”
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
  - [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf)
- **Long video understanding** (construct): *measured_by*, 4 papers
  > EgoSchema [51] contains over 5K three-minute videos with multiple-choice questions. Each question has a long temporal certificate, requiring more than 100 seconds within a video to produce a correct answer. (Section 4.1)
  - [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf)
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
  - [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
- **Temporal reasoning** (construct): *measured_by*, 1 paper
  > Results on EgoSchema (accuracy), a long-form video benchmark (∼3 minutes) for first-person view temporal reasoning. (Table 5).
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
- **Egocentric video understanding** (construct): *measured_by*, 1 paper
  > prior work on egocentric video-language benchmarks include QaEgo4D (B¨armann & Waibel, 2022) and EgoSchema (Mangalam et al., 2023). (Section 4)
  - [MMEgo: Towards Building Egocentric Multimodal LLMs for Video QA](https://proceedings.iclr.cc/paper_files/paper/2025/file/b29a95e7d9f1e1a6dfc567b556733744-Paper-Conference.pdf)
