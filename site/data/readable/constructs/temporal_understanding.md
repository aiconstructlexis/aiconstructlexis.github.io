# Temporal understanding
**Type:** Construct  
**Supporting papers:** 37  
**Also known as:** Time awareness, Temporal comprehension, Temporal awareness, Chronological awareness, Chronological understanding, Temporal modeling  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing centers on ordering and relating events over time, especially in videos: papers most commonly describe temporal understanding as comprehending chronological order, temporal relations, and event evolution, sometimes for long videos or long narratives. A smaller line of work broadens it beyond event order to duration and timing, with one definition noting that models may know frame order but not "how long the frames last," and other papers extend the idea to cross-modality coherence, time-evolving graph structure, dates and periodicity in time series, compressed temporal representations for forecasting, and factual knowledge that changes over time. The main variation is therefore one of scope, from video event sequencing to broader temporal information use in predictions, outputs, and knowledge tracking.

**Space of facets.** Papers break the construct down in several ways. Some treat it as a multi-facet notion covering camera states, scenes, actions, attributes, and their relationships and evolution over time, while benchmark descriptions also mention temporal aspects such as speed, direction, and attribute changes. Another recurring distinction is between temporal understanding and reasoning ability, where temporal understanding is framed as multimodal information comprehension and cross-modality coherence rather than complex reasoning and generation. Across the literature, neighboring labels, including time awareness, temporal comprehension, temporal awareness, chronological awareness or understanding, and temporal modeling, are used for closely related variants, with one strand singling out duration and timing beyond simple sequence order.

**Space of measurement.** Operationalization is benchmark-centered: papers link the construct to 4 measurement instruments and 3 behavioral indicators. The most frequently linked instrument is TempCompass, described as assessing temporal understanding across temporal aspects such as speed, direction, and attribute changes, or across five dimensions; the other linked instruments are MMBench-Video, a Something-Something V2 subset chosen because the action becomes indistinguishable when reversed in time, and the Video-ChatGPT benchmark, which includes a Temporal Understanding metric alongside other evaluation dimensions. These operationalizations align most directly with the video-centered definitions, because the linked instruments are all video benchmarks, while the linked behavioral indicators, temporal grounding, embodied question answering, and video object segmentation, connect the construct to tasks involving temporal coherence, ordering, dependencies, or temporally consistent outputs.

**Links.** Papers connect temporal understanding to nearby tasks and constructs mostly through related links, with one paper also claiming a causal relationship from temporal understanding to generalization, stating that strong spatial reasoning and temporal understanding capabilities allow vision language models to generalize to novel scenarios. Papers also report it as related to multimodal understanding, where temporal understanding issues are described as multimodal information comprehension and cross-modality coherence, and to aleatoric uncertainty awareness through a sub-category called temporal awareness. Additional related links connect it to temporal grounding, video object segmentation, and embodied question answering.

## Sources

**Temporal understanding** (4 papers: [Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf), [MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf), [TUNA: Comprehensive Fine-grained Temporal Understanding Evaluation on Dense Dynamic Videos](https://aclanthology.org/2025.acl-long.91.pdf), [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf))
> The ability to comprehend the chronological order and relationships of events and actions over time within a video.

**Time awareness** (1 paper: [Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf))
> The model's internal representation and understanding of the duration and timing of events within a video, beyond just the sequence of frames.

**Temporal comprehension** (2 papers: [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf), [LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/niu25e/niu25e.pdf))
> The ability to understand and process temporal dynamics and relations within video sequences.

**Temporal awareness** (2 papers: [DTGB: A Comprehensive Benchmark for Dynamic Text-Attributed Graphs](https://proceedings.neurips.cc/paper_files/paper/2024/file/a65d054a407f94c34ecfb598fb540a0d-Paper-Datasets_and_Benchmarks_Track.pdf), [EvolveBench: A Comprehensive Benchmark for Assessing Temporal Awareness in LLMs on Evolving Knowledge](https://aclanthology.org/2025.acl-long.788.pdf))
> The ability to account for time-evolving structure and events when making predictions or generating outputs.

**Chronological awareness** (1 paper: [AutoTimes: Autoregressive Time Series Forecasters via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf))
> The model's ability to understand and utilize temporal information, such as dates and periodicity, to inform its predictions and align multivariate data.

**Chronological understanding** (1 paper: [InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows](https://aclanthology.org/2025.emnlp-main.984.pdf))
> The ability to represent and sequence events in their correct temporal order across a long narrative.

**Temporal modeling** (1 paper: [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf))
> The capacity to represent and reason about temporal structure in long videos, especially when event duration and ordering matter.

## Relationships

### Temporal understanding →
- **TempCompass** (measurement instrument): *measured_by*, 3 papers
  > TempCompass [44] specifically assesses the nuanced performance of LVLMs across various temporal aspects, such as speed, direction, and attribute changes. (Section 5.1)
  - [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Video-ChatGPT benchmark** (measurement instrument): *measured_by*, 1 paper
  > ...and the newly proposed generative performance benchmark [51], include evaluation metrics such as Correctness of Information (CI), Detail Orientation (DO), Contextual Understanding (CU), Temporal Understanding (TU), and Consistency (CO). (Section 4.1)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **MMBench-Video** (measurement instrument): *measured_by*, 1 paper
  > inadequately assess models'temporal comprehension. To address these limitations, we introduce MMBench-Video
  - [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > state-of-the-art VLMs have exhibited strong spatial reasoning and temporal understanding capabilities across various vision tasks (Nag et al., 2022; Chen et al., 2024; Hong et al., 2023; Gao et al., 2024), allowing them to generalize to novel scenarios. (Section 1)
  - [Vision Language Models are In-Context Value Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/54854cf15a24fff9f5134a8641136fe4-Paper-Conference.pdf)
- **Something-Something V2** (measurement instrument): *measured_by*, 1 paper
  > ...we selected 12 classes a priori from SSv2, where the action is indistinguishable if reversed in time... to form a subset that can test the model’s ability in temporal understanding.
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)

### Associated with
- **Temporal grounding** (behavioral indicator), 2 papers
  > These limitations are particularly problematic for temporal understanding tasks that rely on maintaining temporal coherence across frames, such as highlight detection and temporal grounding.
  - [Language-Guided Temporal Token Pruning for Efficient VideoLLM Processing](https://aclanthology.org/2025.emnlp-main.451.pdf)
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
- **Video object segmentation** (behavioral indicator), 1 paper
  > VOS requires models to 1) on the input side, capture and comprehend the temporal dynamics present in the video; and 2) on the output side, predict temporally consistent segmentation masks across frames. (Section 1)
  - [One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf)
- **Multimodal understanding** (construct), 1 paper
  > Specifically, temporal understanding issues refer to multimodal information comprehension and cross-modality coherence, while reasoning issues involve complex reasoning and generation capabilities. (Section 5)
  - [MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf)
- **Aleatoric uncertainty awareness** (construct), 1 paper
  > “Similarly, we define 2 sub-categories under aleatoric uncertainty: • Temporal awareness means understanding that we may not always have access to all relevant data required to predict specific outcomes with absolute certainty, especially when it involves reasoning about time.”
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
- **Embodied question answering** (behavioral indicator), 1 paper
  > complex embodied tasks like Embodied Question Answering (EQA) where nuanced evaluation of agents’ spatial, temporal, and logical understanding is critical yet not considered by generic approaches. (Abstract)
  - [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf)
