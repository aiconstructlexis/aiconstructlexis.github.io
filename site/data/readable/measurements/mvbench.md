# MVBench
**Type:** Measurement instrument  
**Supporting papers:** 32  

## State of the Field

**What it is.** Across papers, the prevailing description is a video or video-language understanding benchmark centered on temporal sensitivity. Definitions often say it covers nine core temporal tasks with 20 subtasks, and that each task cannot be solved from a single frame; some authors instead describe it as a reorganized benchmark containing 20 video understanding tasks, or as a multi-choice QA benchmark with 4,000 QA pairs derived from 11 public video benchmarks. A smaller line of work highlights specific subsets, especially action-related subtasks such as Action Antonym, Action Count, Action Sequence, Action Prediction, Action Localization, Fine-grained Action, and Unexpected Action.

**What it is claimed to measure.** Papers link MVBench to 3 constructs and 1 behavioral indicator. The dominant use is to measure video understanding, with several papers treating it as one of the general benchmarks for that construct; a recurring second use is to measure temporal reasoning, with papers describing it as concentrating on temporal reasoning skills or video temporal reasoning. A smaller usage treats it as measuring multi-image reasoning, and a single paper uses it to measure the behavioral indicator Action localization.

**Space of uses.** Most commonly, papers use MVBench alongside other video benchmarks, especially VideoMME, and also with EgoSchema, MLVU, LongVideoBench, and TempCompass. They usually position it as a general video understanding or temporal benchmark within broader evaluation suites, sometimes explicitly as a short-video benchmark contrasted with long-video settings. Some papers also use it for narrower checks, such as action-focused comparisons, five-task in-depth analysis, generalizability tests, or zero-shot transfer evaluation.

**Concerns raised.** Only a few papers raise scope concerns. One paper describes MVBench as predominantly human-centric, saying the main agents are humans and objects and that animal data accounts for only 1%, while another contrasts it with text-dominant multimodal document understanding and describes it instead as focused on vision-dominant video understanding.

## Sources

**MVBench** (10 papers: [TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/16ba99f25a235f1100a4014d71d34ad8-Paper-Conference.pdf), [HAIC: Improving Human Action Understanding and Generation with Better Captions for Multi-modal Large Language Models](https://aclanthology.org/2025.acl-long.501.pdf), [Understanding Complexity in VideoQA via Visual Program Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eyzaguirre25a/eyzaguirre25a.pdf), [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf), [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf), [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf), [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf), [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf), [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf), [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf))
> A benchmark for visual temporal reasoning that defines nine core temporal tasks with 20 subtasks, designed to be unsolvable using a single frame.

## Relationships

### → MVBench
- **Video understanding** (construct): *measured_by*, 10 papers
  > MVBench [36] is designed to challenge LVLMs with video tasks that cannot be effectively resolved by single-frame reliance, featuring 4,000 QA pairs derived from 11 public video benchmarks. (Section 5.1)
  - [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
  - [MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2c3c86679300047c740c9900f19ddac-Paper-Conference.pdf)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
  - [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf)
  - [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf)
- **Temporal reasoning** (construct): *measured_by*, 2 papers
  > Results across tasks, including general video understanding (Video-MME), video temporal reasoning (MVBench, TempCompass), and long video understanding (MLVU, LongVideoBench, EgoSchema). (Table 2)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
  - [A Culturally-diverse Multilingual Multimodal Video Benchmark & Model](https://aclanthology.org/2025.emnlp-main.1012.pdf)
- **Action localization** (behavioral indicator): *measured_by*, 1 paper
  > MVBench [29] is a recent video-language understanding benchmark that covers 20 challenging video tasks... TOPA Surprisingly excels in the Action Localization (AL) task
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **Multi-image reasoning** (construct): *measured_by*, 1 paper
  > First, we select five multi-image benchmarks: MMMU (Yue et al., 2024), BLINK (Fu et al., 2024), Mantis (Jiang et al., 2024), NLVR2 (Suhr et al., 2018), and MVBench (Li et al., 2024c). (Section 4.1)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)
