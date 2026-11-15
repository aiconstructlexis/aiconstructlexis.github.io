# Video-MME
**Type:** Measurement instrument  
**Supporting papers:** 46  
**Also known as:** VideoMME  

## State of the Field

**What it is.** Across papers, Video-MME, often written VideoMME, is most commonly treated as a multimodal benchmark for video understanding and video-language models, frequently described as a multiple-choice or video question answering benchmark. Several papers also frame it as a long-video benchmark, with videos described as spanning 11 seconds to 1 hour or 1 minute to 1 hour, sometimes split into short, medium, and long groups or reported in a long subset such as VideoMME-L; individual definitions mention 900 videos and 2,700 QA pairs, 6 visual domains and 30 subfields, and reporting with or without subtitles. A smaller set of definitions gives it broader task coverage, including captioning, question answering, and retrieval with subtitles, while others emphasize perception, cognition, reasoning, temporal understanding, temporal ordering, event reasoning, and modality alignment.

**What it is claimed to measure.** Papers link Video-MME to 3 constructs and 1 behavioral indicator. The prevailing use is to measure long video understanding, and many papers also use it to measure video understanding; papers also report it as measuring video question answering, often in long-form or comprehensive settings. A smaller line of work uses it to measure temporal reasoning, with one paper describing Video-MME and MLVU as benchmarks designed to test temporal reasoning across diverse domains, so the measurement claims center on closely related video understanding capacities rather than a broader range of targets.

**Space of uses.** Most papers use Video-MME inside multi-benchmark evaluation suites, often alongside MLVU, EgoSchema, MVBench, LongVideoBench, and NextQA, and position it either as a general video understanding benchmark or as the long-form part of an evaluation setup. Some papers use it for ablations, report results separately for duration groups or subtitle settings, or use top models from the benchmark for further evaluation. One paper also describes it as the first comprehensive benchmark for evaluating multimodal large language models on video analysis.

## Sources

**Video-MME** (6 papers: [Video Action Differencing](https://proceedings.iclr.cc/paper_files/paper/2025/file/26f62bf3b74cda621831f550c6ee2dce-Paper-Conference.pdf), [Addressing Blind Guessing: Calibration of Selection Bias in Multiple-Choice Question Answering by Video Language Models](https://aclanthology.org/2025.acl-long.162.pdf), [LV-XAttn: Distributed Cross-Attention for Long Visual Inputs in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25c/chang25c.pdf), [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf), [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf), [VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf))
> A video understanding benchmark used to identify and select top-performing large multimodal models for evaluation.

**VideoMME** (10 papers: [MMInference: Accelerating Pre-filling for Long-Context Visual Language Models via Modality-Aware Permutation Sparse Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25aq/li25aq.pdf), [Language-Guided Temporal Token Pruning for Efficient VideoLLM Processing](https://aclanthology.org/2025.emnlp-main.451.pdf), [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf), [Out of Sight, Not Out of Context? Egocentric Spatial Reasoning in VLMs Across Disjoint Frames](https://aclanthology.org/2025.emnlp-main.816.pdf), [ProLongVid: A Simple but Strong Baseline for Long-context Video Instruction Tuning](https://aclanthology.org/2025.emnlp-main.1570.pdf), [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf), [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf), [ViPE: Visual Perception in Parameter Space for Efficient Video-Language Understanding](https://aclanthology.org/2025.emnlp-main.897.pdf), [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf), [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf))
> Multimodal evaluation benchmark for video models covering captioning, question answering, and retrieval tasks with subtitles.

## Relationships

### → Video-MME
- **Long video understanding** (construct): *measured_by*, 8 papers
  > Table 4 shows long video evaluations on the Video-MME (Fu et al., 2024) benchmark, demonstrating our model as the best performing model among its size class. (Section 4.3.1)
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
  - [LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25j/shen25j.pdf)
  - [VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf)
  - [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf)
  - [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf)
  - [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf)
- **Video understanding** (construct): *measured_by*, 6 papers
  > For video understanding, we focused on three general benchmarks: MVBench (Li et al., 2024c), TempCompass (Liu et al., 2024c), and VideoMME (Fu et al., 2024)... (Section 4.2)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ag/xu25ag.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
- **Video question answering** (behavioral indicator): *measured_by*, 6 papers
  > To evaluate FRAME-VOYAGER, we plug it into two versions of the state-of-the-art Video-LLM named VILA (VILA-8B and VILA-40B, Lin et al. (2024b)) and conduct experiments on four widely-used Video Question Answering benchmarks, Video-MME (Fu et al., 2024a), MLVU (Zhou et al., 2024), NextQA (Xiao et al., 2021) and ActivityNet-QA (Yu et al., 2019). (Section 1)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
  - [Improving LLM Video Understanding with 16 Frames Per Second](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cg/li25cg.pdf)
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
  - [Language-Guided Temporal Token Pruning for Efficient VideoLLM Processing](https://aclanthology.org/2025.emnlp-main.451.pdf)
- **Temporal reasoning** (construct): *measured_by*, 1 paper
  > "For a comprehensive assessment of long-form video understanding capabilities, we choose two challenging benchmarks: MLVU (Zhou et al., 2024) and Video-MME (Fu et al., 2024). These benchmarks are specifically designed to test temporal reasoning across diverse domains."
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
