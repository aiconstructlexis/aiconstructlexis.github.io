# NExT-QA
**Type:** Measurement instrument  
**Supporting papers:** 29  
**Also known as:** Next-QA, NExTQA, NextQA  

## State of the Field

**What it is.** Across the papers, the prevailing usage is as a video question answering benchmark, often described as multiple choice, for evaluating causal and temporal reasoning over video events. Several definitions add that it targets everyday activities, natural videos, or explanations of temporal actions, and some descriptions also mention descriptive question types; one paper additionally names a subset, NExT-GQA, with timestamp annotations to locate the answer moment. Papers describe its video scope somewhat differently: some call it a long-form or minute-long video dataset with thousands of multiple-choice questions, while others describe it as measuring temporal dynamics over short clips or focusing on short videos.

**What it is claimed to measure.** Papers link it to one behavioral indicator, Video question answering, and to seven constructs. The dominant measurement claim is that papers use NExT-QA to measure video question answering, while construct-level uses are spread across long video understanding and video understanding, followed by causal reasoning, compositional reasoning, reasoning, spatiotemporal reasoning, and temporal reasoning. The recorded relationship language is consistent with this use: papers report that it measures these task areas or abilities, with recurring descriptions that it demands both causal and temporal reasoning and, in one account, emphasizes spatio-temporal reasoning over mere visual-fact retrieval.

**Space of uses.** Papers commonly use it as one item in broader benchmark suites, alongside other video question answering or video-understanding instruments such as EgoSchema, Video-MME, STAR, ActivityNet-QA, and MSRVTT-QA, among others. Some studies make it a focal benchmark, for example by reporting dedicated NExT-QA result tables or by saying they "focus on the NExT-QA benchmark" for its human-annotated questions and spatio-temporal emphasis, while another paper reuses it as an evaluation data source for count and reasoning tasks.

## Sources

**NExT-QA** (9 papers: [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf), [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf), [Addressing Blind Guessing: Calibration of Selection Bias in Multiple-Choice Question Answering by Video Language Models](https://aclanthology.org/2025.acl-long.162.pdf), [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf), [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf), [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf), [Slot-VLM: Object-Event Slots for Video-Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf), [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf), [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf))
> NExT-QA is a video question answering benchmark used to evaluate long-video understanding, including causal and temporal reasoning.

**Next-QA** (1 paper: [Direct Preference Optimization of Video Large Multimodal Models from Language Model Reward](https://aclanthology.org/2025.naacl-long.30.pdf))
> Video question answering benchmark requiring causal and temporal reasoning to answer questions about video events.

**NExTQA** (2 papers: [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf))
> Temporal reasoning benchmark for video question answering, requiring models to understand causal and temporal dynamics in videos.

**NextQA** (1 paper: [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf))
> A video question answering benchmark that focuses on short videos and assesses causal and temporal reasoning.

## Relationships

### → NExT-QA
- **Video question answering** (behavioral indicator): *measured_by*, 12 papers
  > We evaluate Emu on a broad range of vision-language tasks including ... video question answering (MSRVTTQA (Xu et al., 2017), MSVDQA (Xu et al., 2017), NextQA (Xiao et al., 2021))... (Section 5)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
  - [CREMA: Generalizable and Efficient Video-Language Reasoning via Multimodal Modular Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9079234614422c036c5a92bb8ec04c4-Paper-Conference.pdf)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
  - [Direct Preference Optimization of Video Large Multimodal Models from Language Model Reward](https://aclanthology.org/2025.naacl-long.30.pdf)
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
  - [Efficiently Serving Large Multimodal Models Using EPD Disaggregation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/singh25d/singh25d.pdf)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
  - [Improving LLM Video Understanding with 16 Frames Per Second](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cg/li25cg.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
  - [Understanding Complexity in VideoQA via Visual Program Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eyzaguirre25a/eyzaguirre25a.pdf)
- **Video understanding** (construct): *measured_by*, 3 papers
  > We also evaluate the performance of mPLUG-Owl3 on video and multi-image benchmarks (including NextQA (Xiao et al., 2021), MVBench (Li et al., 2023c) VideoMME (Fu et al., 2024a), LongVideoBench (Wu et al., 2024) and MLVU (Zhou et al., 2024)), as it is capable of processing multiple images with an interleaved format.
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **Long video understanding** (construct): *measured_by*, 1 paper
  > We evaluate our model on long video QA datasets... Among them, Next-QA [79], Next-GQA [80] and VideoChatGPT [50] encompass minute-long videos with thousands of frames. (Section 4.1)
  - [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf)
- **Causal reasoning** (construct): *measured_by*, 1 paper
  > We conduct experiments on three popular VideoQA datasets: NExT-QA, STAR, and IntentQA (Xiao et al., 2021; Wu et al., 2021; Li et al., 2023a), which demand both causal and temporal reasoning abilities.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
- **Temporal reasoning** (construct): *measured_by*, 1 paper
  > We conduct experiments on three popular VideoQA datasets: NExT-QA, STAR, and IntentQA (Xiao et al., 2021; Wu et al., 2021; Li et al., 2023a), which demand both causal and temporal reasoning abilities.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > "video-SALMONN-o1 is also evaluated on Video-MME ... and NExT-QA ... benchmarks with challenging reasoning questions"
  - [video-SALMONN-o1: Reasoning-enhanced Audio-visual Large Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25x/sun25x.pdf)
- **Spatiotemporal reasoning** (construct): *measured_by*, 1 paper
  > "We focus on the NExT-QA (Xiao et al., 2021) benchmark for its size, variety of human-annotated questions, and its focus on spatio-temporal reasoning in videos over mere visual-fact retrieval"
  - [Understanding Complexity in VideoQA via Visual Program Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eyzaguirre25a/eyzaguirre25a.pdf)
- **Compositional reasoning** (construct): *measured_by*, 1 paper
  > We evaluate on general video understanding benchmarks: ... NeXTQA (Xiao et al., 2021) (compositional reasoning)
  - [VideoPASTA: 7K Preference Pairs That Matter for Video-LLM Alignment](https://aclanthology.org/2025.emnlp-main.1647.pdf)
