# Video question answering
**Type:** Behavioral indicator  
**Supporting papers:** 65  
**Also known as:** Long-video question answering, Egocentric question answering, Temporal video reasoning  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing is answering a natural-language question from a given video, with the answer grounded in the video's content and often in its dynamic, visual, and temporal information. Most definitions treat success as producing a correct or accurate answer, often a textual one. Some papers frame the task as open-ended natural-language generation, while others use multiple-choice or instruction-following settings. One paper calls it a task that "requires understanding complex visual and temporal relationships within videos to answer questions accurately."

**Variants.** Papers study several variants. A common split is between closed-ended or multiple-choice VideoQA and open-ended, including long-form, answer generation, and one long-video line explicitly separating multiple-choice-based selection from text generation. Smaller strands examine long-video question answering, egocentric question answering on first-person videos, and temporal video reasoning, where questions concern relationships between actions over time such as sequence or frequency; one paper also says typical video-language tasks can be formulated as video question answering tasks.

**Space of elicitation and scores.** Papers measure it with 15 instruments. The most frequently linked are ActivityNet-QA, NExT-QA, MSVD-QA, MSRVTT-QA, and EgoSchema, followed by 10 other instruments. Most of these are VideoQA datasets or benchmarks, spanning open-ended, closed-ended, long-form, and long-video settings; one paper also scores freely generated answers with an LLM-as-a-judge that returns a True or False judgment from the question, correct answer, and model prediction.

**What it is taken as evidence of.** Papers connect it to 7 constructs rather than a single shared target construct. The most frequently linked are causal reasoning, multimodal understanding, reasoning, temporal reasoning, and spatial understanding. In the recorded relationships, video question answering is related to causal reasoning and temporal reasoning, and some long-video work says such benchmarks aim to measure causal and temporal reasoning abilities; it is also related to spatial understanding. Papers additionally claim causal relationships from multimodal understanding to video question answering and from reasoning to video question answering, while one paper claims a causal relationship from video question answering to reasoning, and 2 other constructs are linked only as related.

## Sources

**Video question answering** (9 papers: [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf), [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/32683193e1d0e7a5795b073acecb3549-Paper-Datasets_and_Benchmarks_Track.pdf), [Exploring the Design Space of Visual Context Representation in Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/24e2320097bdf179e2b2719c6df2f448-Paper-Conference.pdf), [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf), [Direct Preference Optimization of Video Large Multimodal Models from Language Model Reward](https://aclanthology.org/2025.naacl-long.30.pdf), [Sharper and Faster mean Better: Towards More Efficient Vision-Language Model for Hour-scale Long Video Understanding](https://aclanthology.org/2025.acl-long.222.pdf), [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf), [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf))
> Answering questions that require understanding of dynamic visual content from videos.

**Long-video question answering** (1 paper: [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf))
> Answering questions about long videos, typically by selecting among candidate answers or generating a textual response.

**Egocentric question answering** (1 paper: [MMEgo: Towards Building Egocentric Multimodal LLMs for Video QA](https://proceedings.iclr.cc/paper_files/paper/2025/file/b29a95e7d9f1e1a6dfc567b556733744-Paper-Conference.pdf))
> Answering questions about first-person videos using visual and textual evidence from the video content.

**Temporal video reasoning** (1 paper: [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf))
> A category of tasks requiring the model to answer questions that involve understanding the relationships between actions over time, such as their sequence or frequency.

## Relationships

### Video question answering →
- **NExT-QA** (measurement instrument): *measured_by*, 12 papers
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
- **ActivityNet-QA** (measurement instrument): *measured_by*, 12 papers
  > Additionally, we evaluate zero-shot performance on open-ended video question-answering benchmarks such as MSVD-QA [68], ActivityNet-QA [69], MSRVTT-QA [70]... (Section 4.1)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf)
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
  - [SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25s/zhang25s.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
  - [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf)
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf)
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
- **MSVD-QA** (measurement instrument): *measured_by*, 11 papers
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
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
- **MSRVTT-QA** (measurement instrument): *measured_by*, 10 papers
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
- **TGIF-QA** (measurement instrument): *measured_by*, 6 papers
  > ...as well as four video QA benchmarks: MVSD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2016), TGIF-QA (Jang et al., 2017), and ActivityNet-QA (Caba Heilbron et al., 2015). (Section 4.2)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
  - [SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25s/zhang25s.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
  - [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf)
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.28.pdf)
- **Video-MME** (measurement instrument): *measured_by*, 6 papers
  > To evaluate FRAME-VOYAGER, we plug it into two versions of the state-of-the-art Video-LLM named VILA (VILA-8B and VILA-40B, Lin et al. (2024b)) and conduct experiments on four widely-used Video Question Answering benchmarks, Video-MME (Fu et al., 2024a), MLVU (Zhou et al., 2024), NextQA (Xiao et al., 2021) and ActivityNet-QA (Yu et al., 2019). (Section 1)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
  - [Improving LLM Video Understanding with 16 Frames Per Second](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cg/li25cg.pdf)
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
  - [Language-Guided Temporal Token Pruning for Efficient VideoLLM Processing](https://aclanthology.org/2025.emnlp-main.451.pdf)
- **EgoSchema** (measurement instrument): *measured_by*, 6 papers
  > We use Egoschema (Mangalam et al., 2023) and VideoMME (Fu et al., 2024) to evaluate the long video capabilities of VideoChat-T.
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
  - [$∞$-Video: A Training-Free Approach to Long Video Understanding via Continuous-Time Memory Consolidation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/santos25a/santos25a.pdf)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
- **MLVU** (measurement instrument): *measured_by*, 3 papers
  > To evaluate FRAME-VOYAGER, we plug it into two versions of the state-of-the-art Video-LLM named VILA (VILA-8B and VILA-40B, Lin et al. (2024b)) and conduct experiments on four widely-used Video Question Answering benchmarks, Video-MME (Fu et al., 2024a), MLVU (Zhou et al., 2024), NextQA (Xiao et al., 2021) and ActivityNet-QA (Yu et al., 2019). (Section 1)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
  - [Static or Dynamic: Towards Query-Adaptive Token Selection for Video Question Answering](https://aclanthology.org/2025.emnlp-main.545.pdf)
- **STAR** (measurement instrument): *measured_by*, 3 papers
  > We evaluate ReasVQA on three popular benchmarks, and our results establish new state-of-the-art performance with significant improvements of +2.9 on NExT-QA, +7.3 on STAR, and +5.9 on IntentQA.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
  - [Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf)
- **Video-ChatGPT benchmark** (measurement instrument): *measured_by*, 2 papers
  > We test the trained model on the Video-ChatGPT test set [37] and the other three benchmarks (i.e., MSVD-QA [8], MSRVTT-QA [53], and ActivityNet-QA [6, 58]) where their training sets was not used to train Artemis. (Section 4.2).
  - [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **TempCompass** (measurement instrument): *measured_by*, 1 paper
  > To evaluate Video-STaR’s effect on general video question answering, we evaluated its effect on Video-LLaVA’s performance on TempCompass (Sec. 4.2).
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > Video question answering datasets to enhance TRACE’s reasoning capabilities.
  - [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > The second method involves models freely generating answers, which are then evaluated by GPT-4. Given the question, correct answer, and model’s prediction, GPT-4 returns a True or False judgment.
  - [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf)
- **LongVideoBench** (measurement instrument): *measured_by*, 1 paper
  > We also evaluate MVU on the LongVideoBench dataset which contains even longer videos (Section 5.1)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
- **MUSIC-AVQA** (measurement instrument): *measured_by*, 1 paper
  > "and two open-ended VideoQA datasets: MUSIC-AVQA (MUSC) (Li et al., 2022a) and MSVD (Chen & Dolan, 2011)"
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
- **MSVD** (measurement instrument): *measured_by*, 1 paper
  > "and two open-ended VideoQA datasets: MUSIC-AVQA (MUSC) (Li et al., 2022a) and MSVD (Chen & Dolan, 2011)"
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)

### → Video question answering
- **Multimodal understanding** (construct): *causes*, 2 papers
  > These models also exhibit strong multimodal understanding (Lin et al., 2023; Li et al., 2024; Zhang et al., 2023b), capable of answering questions about unseen content, thus opening up new avenues for improving VideoQA.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > In this work, we introduce ReasVQA (Reasoning-enhanced Video Question Answering), a novel approach that leverages reasoning processes generated by Multimodal Large Language Models (MLLMs) to improve the performance of VideoQA models.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)

### Associated with
- **Temporal reasoning** (construct), 2 papers
  > Wang et al. (2023b) and Ko et al. (2023) try to leverage LLaMA’s (Touvron et al., 2023) knowledge of temporal and causal reasoning to address the complexities of VideoQA.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
- **Causal reasoning** (construct), 2 papers
  > Wang et al. (2023b) and Ko et al. (2023) try to leverage LLaMA’s (Touvron et al., 2023) knowledge of temporal and causal reasoning to address the complexities of VideoQA.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
- **Video understanding** (construct), 1 paper
  > In the research context of Video-LLMs, typical video-language tasks such as video understanding, summarization, and reasoning can be formulated as video question answering tasks. (Section 3)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Video summarization** (behavioral indicator), 1 paper
  > In the research context of Video-LLMs, typical video-language tasks such as video understanding, summarization, and reasoning can be formulated as video question answering tasks. (Section 3)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Spatial understanding** (construct), 1 paper
  > We annotate 98 videos and provide 882 question-answer pairs that target three types of questions: ... 2) spatial Understanding about the position of items and their relation to other items...
  - [Evaluating Multimodal Language Models as Visual Assistants for Visually Impaired Users](https://aclanthology.org/2025.acl-long.1260.pdf)
- **Uncertainty handling** (construct), 1 paper
  > Adversarial questions, which cannot be answered based on the information provided in the video, help assess whether models hallucinate responses or can reliably acknowledge uncertainty—a critical safety feature for assistive technologies.
  - [Evaluating Multimodal Language Models as Visual Assistants for Visually Impaired Users](https://aclanthology.org/2025.acl-long.1260.pdf)
