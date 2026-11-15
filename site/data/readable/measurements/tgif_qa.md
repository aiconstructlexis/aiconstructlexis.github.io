# TGIF-QA
**Type:** Measurement instrument  
**Supporting papers:** 10  

## State of the Field

**What it is.** Across papers, the dominant framing is a video question answering benchmark built from the TGIF, or Tumblr GIF, dataset, with animated GIFs as the video source. Definitions commonly describe it as targeting short video clips or sequences and assessing temporal, causal, or spatio-temporal reasoning, and one recurring description highlights tasks such as repetition counting and state transition recognition. A smaller line of work describes it more broadly as a visual question answering dataset, and one paper uses it as a source of evaluation data for count and reasoning tasks.

**What it is claimed to measure.** Papers link TGIF-QA to 1 behavioral indicator and 1 construct. The prevailing usage is to measure Video question answering: papers describe it as one of the common, open-ended, or zero-shot VideoQA benchmarks. A smaller usage treats it as measuring Video understanding, with one paper placing it in a broader suite of video understanding benchmarks. Overall, the measurement claims are concentrated on these two targets rather than spread across many constructs or behavioral indicators.

**Space of uses.** Across papers, TGIF-QA is usually used as one item in a larger evaluation suite rather than on its own. It is commonly listed alongside MSVD-QA, MSRVTT-QA, and ActivityNet-QA for open-ended, common, or zero-shot VideoQA evaluation, and some papers also place it with MVSD-QA or use it as evaluation data together with NExT-QA for count and reasoning tasks. No measurement instrument is linked to it through an explicit relationship.

## Sources

**TGIF-QA** (5 papers: [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf), [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf), [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf), [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf), [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf))
> A video question answering benchmark based on the Tumblr GIF (TGIF) dataset, focusing on tasks like repetition counting and state transition recognition.

## Relationships

### → TGIF-QA
- **Video question answering** (behavioral indicator): *measured_by*, 6 papers
  > ...as well as four video QA benchmarks: MVSD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2016), TGIF-QA (Jang et al., 2017), and ActivityNet-QA (Caba Heilbron et al., 2015). (Section 4.2)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
  - [SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25s/zhang25s.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
  - [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf)
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf)
- **Video understanding** (construct): *measured_by*, 1 paper
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019)...
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
