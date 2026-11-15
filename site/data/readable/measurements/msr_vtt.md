# MSR-VTT
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** MSRVTT  

## State of the Field

**What it is.** Most papers describe MSR-VTT as a large video description or video captioning benchmark used for video-language evaluation. Definitions variously frame it as an English video captioning dataset, a text-to-video retrieval benchmark with 10,000 video clips and associated natural language descriptions, and a benchmark for short video understanding; one source also notes 10K open-domain videos, while another refers to a test set of 2,990 videos that are 10 to 30 seconds long. A smaller line of work treats it as the large unannotated dataset in active-learning experiments.

**What it is claimed to measure.** Across the surveyed work, the dominant use is to measure behavioral indicators rather than constructs: papers link it to 3 behavioral indicators and no constructs. Most commonly, papers use it to measure video captioning, while smaller lines of work use it to measure video generation and cross-modal retrieval. These reported uses stay at the level of behavioral indicators.

**Space of uses.** Papers often use MSR-VTT alongside other video-language benchmarks, most often MSVD, and also VATEX, LSMDC, DiDeMo, and UCF-101. It is positioned both as a benchmark for evaluating zero-shot captioning, text-to-video retrieval, and text-to-video generation, and in one active-learning setup as the large unannotated dataset contrasted with a small annotated MSVD set.

## Sources

**MSR-VTT** (7 papers: [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf), [X-CoT: Explainable Text-to-Video Retrieval via LLM-based Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.1588.pdf), [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf), [Learnability Matters: Active Learning for Video Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/43069caa6776eac8bca4bfd74d4a476d-Paper-Conference.pdf), [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf), [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf), [Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf))
> An English video captioning dataset referenced as a prior benchmark for video-language evaluation.

**MSRVTT** (1 paper: [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf))
> A video understanding benchmark used here to assess short video comprehension.

## Relationships

### → MSR-VTT
- **Video captioning** (behavioral indicator): *measured_by*, 3 papers
  > We further perform zero-shot video captioning on MSR-VTT [75] and VATEX [62]. (Section 4.3)
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
  - [Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf)
- **Video generation** (behavioral indicator): *measured_by*, 2 papers
  > "We also evaluate LVD on common datasets such as UCF-101 (Soomro et al., 2012) and MSR-VTT (Xu et al., 2016)"
  - [LLM-grounded Video Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d9f8b5abc8e0926539ecbb492af7b2f1-Paper-Conference.pdf)
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Cross-modal retrieval** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate X-CoT on four benchmarks: MSR-VTT (Xu et al., 2016), MSVD (Chen and Dolan, 2011), LSMDC (Rohrbach et al., 2015), and DiDeMo (Anne Hendricks et al., 2017).
  - [X-CoT: Explainable Text-to-Video Retrieval via LLM-based Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.1588.pdf)
