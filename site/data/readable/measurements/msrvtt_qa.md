# MSRVTT-QA
**Type:** Measurement instrument  
**Supporting papers:** 29  
**Also known as:** MSRVTTQA, MSR-VTT-QA, MSRVT-QA  

## State of the Field

**What it is.** Across papers, the prevailing description is a video question answering benchmark based on or derived from the MSR-VTT dataset, also expanded in some definitions as Microsoft Research Video to Text. Definitions differ mainly in label and emphasis: some call it a benchmark, others a dataset or benchmark dataset, and several specify that it is open-ended, testing comprehension of video content through associated questions or answers about video clips. One description also notes that MSRVTT-QA, together with MSVD-QA, is derived from video retrieval datasets.

**What it is claimed to measure.** Measurement claims are concentrated rather than spread across many targets. Papers link it to 1 behavioral indicator, Video question answering, and this is the dominant usage: relationship evidence describes MSRVTT-QA as a benchmark for open-ended or zero-shot video question answering. Papers also link it to 1 construct, Video understanding, typically when placing it inside broader video understanding benchmark suites.

**Space of uses.** No paper directly links it to another measurement instrument, but papers usually use it alongside other video QA benchmarks, most often MSVD-QA and ActivityNet-QA, and often TGIF-QA; a few also mention NextQA or the Video-ChatGPT test set. The recurring positioning is as one benchmark within a broader evaluation suite, with several quoted passages describing open-ended or zero-shot VideoQA evaluation and one describing MSRVTT-QA among classical video QA datasets.

## Sources

**MSRVTT-QA** (13 papers: [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf), [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf), [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf), [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf), [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf), [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf), [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf), [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf), [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf), [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf), [Slot-VLM: Object-Event Slots for Video-Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf), [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf), [VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf))
> A video question answering benchmark derived from the MSR-VTT dataset.

**MSRVTTQA** (2 papers: [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf))
> Video question answering benchmark based on MSRVTT, testing comprehension of video content with associated questions.

**MSR-VTT-QA** (1 paper: [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf))
> Video question answering benchmark based on the MSR-VTT dataset, assessing model performance on diverse video content with open-ended questions.

**MSRVT-QA** (1 paper: [CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eb/wang25eb.pdf))
> A benchmark for video question answering based on the MSR-VTT (Microsoft Research Video to Text) dataset.

## Relationships

### → MSRVTT-QA
- **Video question answering** (behavioral indicator): *measured_by*, 10 papers
  > We evaluate Emu on a broad range of vision-language tasks including ... video question answering (MSRVTTQA (Xu et al., 2017), MSVDQA (Xu et al., 2017), NextQA (Xiao et al., 2021))... (Section 5)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
  - [SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25s/zhang25s.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
  - [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf)
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf)
- **Video understanding** (construct): *measured_by*, 3 papers
  > By scaling up the LLM to 34B, our model demonstrates a marked improvement in video understanding capabilities, achieving state-of-the-art performance on video evaluation benchmarks with accuracies of 77.4% on MSVD [68], 62.1% on MSR-VTT [70], and 55.8% on ActivityNet [69]. (Section 4.3)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf)
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
