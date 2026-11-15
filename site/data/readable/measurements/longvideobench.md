# LongVideoBench
**Type:** Measurement instrument  
**Supporting papers:** 18  
**Also known as:** LongVideo-Bench  

## State of the Field

**What it is.** Across papers, LongVideoBench is most commonly described as a benchmark or dataset for long video understanding, often framed as long video question answering. Some papers narrow this further to referred reasoning on long frame inputs or to long-context interleaved video-language understanding: one description says it features "video-language interleaved inputs up to an hour long," with 3,763 web-collected videos and subtitles, plus 6,678 human-annotated multiple-choice questions in 17 fine-grained categories.

**What it is claimed to measure.** Across linked relationships, papers use it to measure 3 constructs and 1 behavioral indicator. The prevailing usage is to measure long video understanding, with additional use for video understanding and long-context multimodal understanding; one behavioral link treats it as measuring video question answering. Several task descriptions further characterize that measurement as targeting referred reasoning, long-form evaluation, or long-term multimodal understanding.

**Space of uses.** Papers usually deploy it as one benchmark within a broader evaluation suite rather than in isolation. It appears alongside MLVU, VideoMME, EgoSchema, MVBench, and TempCompass, and papers position it within comparative evaluations across video benchmarks, long-form evaluation, and zero-shot transfer settings. No measurement instrument is linked to it.

**Concerns raised.** Papers describe LongVideoBench as stressing memory and temporal coherence, sustained attention and context retention, and long-range temporal and contextual reasoning. One paper also says it presents a challenge of retrieving and reasoning over long video inputs.

## Sources

**LongVideoBench** (10 papers: [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf), [Sharper and Faster mean Better: Towards More Efficient Vision-Language Model for Hour-scale Long Video Understanding](https://aclanthology.org/2025.acl-long.222.pdf), [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf), [ProLongVid: A Simple but Strong Baseline for Long-context Video Instruction Tuning](https://aclanthology.org/2025.emnlp-main.1570.pdf), [SpecVLM: Enhancing Speculative Decoding of Video LLMs via Verifier-Guided Token Pruning](https://aclanthology.org/2025.emnlp-main.366.pdf), [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf), [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf), [Video-RTS: Rethinking Reinforcement Learning and Test-Time Scaling for Efficient and Enhanced Video Reasoning](https://aclanthology.org/2025.emnlp-main.1428.pdf), [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf), [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf))
> A dataset containing very long videos used to evaluate video question answering models.

**LongVideo-Bench** (1 paper: [Exploring the Design Space of Visual Context Representation in Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/24e2320097bdf179e2b2719c6df2f448-Paper-Conference.pdf))
> A benchmark dataset used to evaluate model performance on long video understanding tasks.

## Relationships

### → LongVideoBench
- **Long video understanding** (construct): *measured_by*, 5 papers
  > For long video understanding, we use LongVideoBench (Wu et al., 2024a) (8 seconds to 1 hour), MLVU (Zhou et al., 2024) (3 minutes to 2 hours), and Video-MME (Fu et al., 2024) (11 seconds to 60 minutes). (Section 5.1)
  - [VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
  - [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf)
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **Video understanding** (construct): *measured_by*, 3 papers
  > We also evaluate the performance of mPLUG-Owl3 on video and multi-image benchmarks (including NextQA (Xiao et al., 2021), MVBench (Li et al., 2023c) VideoMME (Fu et al., 2024a), LongVideoBench (Wu et al., 2024) and MLVU (Zhou et al., 2024)), as it is capable of processing multiple images with an interleaved format.
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **Long-context multimodal understanding** (construct): *measured_by*, 1 paper
  > To mitigate this gap, we introduce LONGVIDEOBENCH, a question-answering benchmark that features video-language interleaved inputs up to an hour long. Our benchmark includes 3,763 varying-length web-collected videos with their subtitles across diverse themes, designed to comprehensively evaluate LMMs on long-term multimodal understanding. (Abstract)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Video question answering** (behavioral indicator): *measured_by*, 1 paper
  > We also evaluate MVU on the LongVideoBench dataset which contains even longer videos (Section 5.1)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
