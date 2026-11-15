# MSVD
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Across the papers, MSVD is most commonly framed as a video understanding benchmark, including for assessing short video comprehension and for evaluating multimodal video question answering or captioning performance. A smaller framing describes it as a benchmark dataset for video captioning: one paper specifies that it contains 1,970 open-domain videos collected from a commercial video search engine, with about 41 human-annotated captions for each video.

**What it is claimed to measure.** Papers link MSVD to 1 construct and 2 behavioral indicators. The construct-level claim is that video understanding is measured by MSVD, while the behavioral indicators are video question answering, where it is listed as an open-ended VideoQA dataset, and cross-modal retrieval, where it appears as one of the retrieval benchmarks. These claims spread across a small set of evaluation targets rather than only one task framing.

**Space of uses.** In use, papers often place MSVD alongside other benchmarks in evaluation suites. It appears with MSR-VTT in video captioning experiments, with MUSIC-AVQA in open-ended VideoQA evaluation, and with MSR-VTT, LSMDC, and DiDeMo in cross-modal retrieval benchmarking. No measurement instrument is linked to it in the papers' reported relationships.

## Sources

**MSVD** (3 papers: [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf), [Stop Looking for “Important Tokens” in Multimodal Language Models: Duplication Matters More](https://aclanthology.org/2025.emnlp-main.505.pdf), [Learnability Matters: Active Learning for Video Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/43069caa6776eac8bca4bfd74d4a476d-Paper-Conference.pdf))
> A video understanding benchmark used here to assess short video comprehension.

## Relationships

### → MSVD
- **Video understanding** (construct): *measured_by*, 1 paper
  > “To assess DART’s capabilities in video understanding, we integrate it with Video-LLaVA ... achieving a notable 4.0 score on MSVD”
  - [Stop Looking for “Important Tokens” in Multimodal Language Models: Duplication Matters More](https://aclanthology.org/2025.emnlp-main.505.pdf)
- **Video question answering** (behavioral indicator): *measured_by*, 1 paper
  > "and two open-ended VideoQA datasets: MUSIC-AVQA (MUSC) (Li et al., 2022a) and MSVD (Chen & Dolan, 2011)"
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
- **Cross-modal retrieval** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate X-CoT on four benchmarks: MSR-VTT (Xu et al., 2016), MSVD (Chen and Dolan, 2011), LSMDC (Rohrbach et al., 2015), and DiDeMo (Anne Hendricks et al., 2017).
  - [X-CoT: Explainable Text-to-Video Retrieval via LLM-based Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.1588.pdf)
