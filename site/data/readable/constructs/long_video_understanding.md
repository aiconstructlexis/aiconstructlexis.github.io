# Long video understanding
**Type:** Construct  
**Supporting papers:** 16  
**Also known as:** Long video comprehension, Long-video understanding, Long-range video understanding  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats long video understanding as a model ability to process, comprehend, and reason about extended video sequences, especially their content and temporal dynamics. Most descriptions stay close to this framing, with some broadening it to include plot, relationships, retrieval and synthesis across long time spans, or integration of information over long durations. A smaller framing casts it more as a task setting, namely handling videos much longer than short clips, sometimes through segmenting them into shorter clips and summarizing them.

**Space of facets.** Papers usually position the construct as a facet of broader multi-modal or video understanding, and one paper directly relates it to long-context understanding. Terminology overlaps heavily: some authors use long video comprehension or long-range video understanding for what is otherwise defined in very similar terms. A narrower strand highlights target-centric understanding of long videos as a challenge within this broader space.

**Space of measurement.** Operationalization is benchmark-based: papers link the construct to 7 measurement instruments and 1 behavioral indicator, with MLVU, Video-MME, LongVideoBench, EgoSchema, and InfiniBench appearing most often, plus 2 other benchmarks. These instruments are used for long-form evaluation of comprehension, reasoning, question answering, or retrieval over extended videos, and papers explicitly describe MLVU and Video-MME as suitable for assessing long video understanding ability or long-context comprehension. The only linked behavioral indicator is temporal grounding, but it is introduced elsewhere as assisting the construct rather than measuring it directly.

**Links.** Outside measurement, papers record 1 related construct link and 1 causal link from a behavioral indicator. One paper reports that long video understanding is related to long-context understanding, noting that long-context capability is especially relevant to it. Another paper claims a causal relationship from temporal grounding to long video understanding, arguing that explicitly performing temporal grounding could assist it by establishing detailed correspondence between visual segments and fine-grained semantics.

## Sources

**Long video understanding** (2 papers: [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf), [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf))
> A specific facet of multi-modal understanding focused on the model's ability to comprehend and reason about the content and temporal dynamics of extended video sequences.

**Long video comprehension** (1 paper: [Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf))
> The capacity to understand and reason over extended video sequences, including plot, relationships, and temporal dynamics.

**Long-video understanding** (1 paper: [$∞$-Video: A Training-Free Approach to Long Video Understanding via Continuous-Time Memory Consolidation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/santos25a/santos25a.pdf))
> The ability of a model to process, comprehend, and reason about video content that extends beyond a short time frame, often requiring the integration of information over long durations.

**Long-range video understanding** (1 paper: [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf))
> Comprehending and reasoning over extended video sequences.

## Relationships

### Long video understanding →
- **Video-MME** (measurement instrument): *measured_by*, 8 papers
  > Table 4 shows long video evaluations on the Video-MME (Fu et al., 2024) benchmark, demonstrating our model as the best performing model among its size class. (Section 4.3.1)
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
  - [LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25j/shen25j.pdf)
  - [VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf)
  - [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf)
  - [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf)
  - [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf)
- **MLVU** (measurement instrument): *measured_by*, 8 papers
  > VideoMME (Fu et al., 2024) (1 min ∼1 hour) and MLVU (Zhou et al., 2024) (3 mins ∼2 hours) are long video benchmarks for assessing long video understanding ability. (Section 4.2)
  - [LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25j/shen25j.pdf)
  - [VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf)
  - [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
  - [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf)
  - [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf)
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **LongVideoBench** (measurement instrument): *measured_by*, 5 papers
  > For long video understanding, we use LongVideoBench (Wu et al., 2024a) (8 seconds to 1 hour), MLVU (Zhou et al., 2024) (3 minutes to 2 hours), and Video-MME (Fu et al., 2024) (11 seconds to 60 minutes). (Section 5.1)
  - [VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
  - [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf)
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **EgoSchema** (measurement instrument): *measured_by*, 4 papers
  > EgoSchema [51] contains over 5K three-minute videos with multiple-choice questions. Each question has a long temporal certificate, requiring more than 100 seconds within a video to produce a correct answer. (Section 4.1)
  - [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf)
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
  - [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
- **NExT-QA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our model on long video QA datasets... Among them, Next-QA [79], Next-GQA [80] and VideoChatGPT [50] encompass minute-long videos with thousands of frames. (Section 4.1)
  - [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf)
- **MMBench-Video** (measurement instrument): *measured_by*, 1 paper
  > In addition, we rigorously assess the performance of our Video-UTR on the recently introduced and exceptionally demanding long-range video understanding benchmark, MVBench-Video. (Section 4.4)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
- **InfiniBench** (measurement instrument): *measured_by*, 1 paper
  > we introduce InfiniBench, a comprehensive benchmark designed to evaluate the capabilities of models in long video understanding rigorously.
  - [InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows](https://aclanthology.org/2025.emnlp-main.984.pdf)

### → Long video understanding
- **Temporal grounding** (behavioral indicator): *causes*, 1 paper
  > We argue long video understanding could be assisted by explicitly performing temporal grounding, as grounding supervision enables MLLM to establish the detailed correspondance between the visual segments and fine-grained semantics.
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)

### Associated with
- **Long-context understanding** (construct), 1 paper
  > Long-context capability is critical for multi-modal foundation models, especially for long video understanding. (ABSTRACT)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
