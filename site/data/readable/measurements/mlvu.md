# MLVU
**Type:** Measurement instrument  
**Supporting papers:** 19  

## State of the Field

**What it is.** Across papers, the prevailing usage treats MLVU as a long-video or long-form video understanding benchmark for multimodal models. Definitions often add that it is multi-task or oriented to question answering, with videos described as ranging from 3 minutes to 2 hours; some papers specify a test set of over 500 QA pairs and multiple-choice accuracy, and one paper instead highlights an average video duration of 15.5 minutes. Other descriptions emphasize long-context comprehension, extended temporal reasoning, or complex scene dynamics, but the common framing remains a benchmark for understanding long videos.

**What it is claimed to measure.** Papers link MLVU to 3 constructs and 2 behavioral indicators. The dominant claim is that papers use it to measure long video understanding; other papers report it as measuring video understanding and, in a smaller line of work, temporal reasoning across diverse domains. Among behavioral indicators, it is used for video question answering, and one paper points to MLVU subtasks for counting.

**Space of uses.** Papers often use MLVU alongside other video benchmarks, especially VideoMME, LongVideoBench, and EgoSchema, and also with MVBench and NextQA. It is regularly positioned as one of several widely used or mainstream benchmarks for comprehensive long-video evaluation, though some papers use it more specifically for multi-task question answering or pair it with Video-MME for long-form assessment. Reported results are typically given as accuracy on MLVU, consistent with descriptions of multiple-choice evaluation.

## Sources

**MLVU** (10 papers: [Exploring the Design Space of Visual Context Representation in Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/24e2320097bdf179e2b2719c6df2f448-Paper-Conference.pdf), [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf), [InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows](https://aclanthology.org/2025.emnlp-main.984.pdf), [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf), [ProLongVid: A Simple but Strong Baseline for Long-context Video Instruction Tuning](https://aclanthology.org/2025.emnlp-main.1570.pdf), [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf), [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf), [ViPE: Visual Perception in Parameter Space for Efficient Video-Language Understanding](https://aclanthology.org/2025.emnlp-main.897.pdf), [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf), [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf))
> A long-video understanding benchmark used to evaluate multiple-choice performance on video understanding tasks.

## Relationships

### → MLVU
- **Long video understanding** (construct): *measured_by*, 8 papers
  > VideoMME (Fu et al., 2024) (1 min ∼1 hour) and MLVU (Zhou et al., 2024) (3 mins ∼2 hours) are long video benchmarks for assessing long video understanding ability. (Section 4.2)
  - [LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25j/shen25j.pdf)
  - [VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf)
  - [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
  - [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf)
  - [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf)
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **Video question answering** (behavioral indicator): *measured_by*, 3 papers
  > To evaluate FRAME-VOYAGER, we plug it into two versions of the state-of-the-art Video-LLM named VILA (VILA-8B and VILA-40B, Lin et al. (2024b)) and conduct experiments on four widely-used Video Question Answering benchmarks, Video-MME (Fu et al., 2024a), MLVU (Zhou et al., 2024), NextQA (Xiao et al., 2021) and ActivityNet-QA (Yu et al., 2019). (Section 1)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
- **Video understanding** (construct): *measured_by*, 2 papers
  > We also evaluate the performance of mPLUG-Owl3 on video and multi-image benchmarks (including NextQA (Xiao et al., 2021), MVBench (Li et al., 2023c) VideoMME (Fu et al., 2024a), LongVideoBench (Wu et al., 2024) and MLVU (Zhou et al., 2024)), as it is capable of processing multiple images with an interleaved format.
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **Temporal reasoning** (construct): *measured_by*, 1 paper
  > "For a comprehensive assessment of long-form video understanding capabilities, we choose two challenging benchmarks: MLVU (Zhou et al., 2024) and Video-MME (Fu et al., 2024). These benchmarks are specifically designed to test temporal reasoning across diverse domains."
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Counting** (behavioral indicator): *measured_by*, 1 paper
  > "the results of each subtask in MLVU (Zhou et al., 2024) show significant performance improvements when using cross-modal queries, particularly for frame-retrieval tasks such as counting and needle detection."
  - [LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25j/shen25j.pdf)
