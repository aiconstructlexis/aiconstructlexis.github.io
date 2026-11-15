# Video understanding
**Type:** Construct  
**Supporting papers:** 51  
**Also known as:** Video comprehension, Video understanding and reasoning, Long-form video understanding, Long-form video-language understanding, Explanation  

## State of the Field

**Space of definitions.** Across the literature, the prevailing usage treats video understanding as a model ability to comprehend and interpret video content, usually including events, context, actions, and temporal dynamics, and sometimes also spatial or semantic information. Most definitions frame it as a latent capability of the model, but some papers use a more behavioral framing, describing it as processing videos to answer questions, generate descriptions or responses, or otherwise demonstrate comprehension; one definition makes this explicit as the observable ability to answer questions about scene changes, object interactions, and event sequences. A smaller line of work uses nearby labels such as video comprehension, while some authors broaden the label to video understanding and reasoning or video-language understanding, so the main variation is whether the construct is treated as a latent ability or as task-demonstrated performance, and whether reasoning is included inside it.

**Space of facets.** Papers also use the nearby label video comprehension for the same general capability, and some explicitly widen the label to video understanding and reasoning or to video-language understanding. The clearest subtype is long-form video understanding, or long-form video-language understanding, which is described as focusing on extended videos and on integrating information over many minutes, sometimes over hour-long spans. A narrower facet appears as explanation, defined as inferring and articulating the logic, purpose, or mechanism behind what is happening in a video.

**Space of measurement.** Papers link video understanding to 19 measurement instruments and 2 behavioral indicators. Operationalization is almost entirely benchmark-based: the most frequently linked instruments are MVBench, Video-MME, ActivityNet-QA, EgoSchema, and MSVD-QA, within a broader set of 19 instruments that also includes long-video, multiple-choice, and open-ended video QA benchmarks. Some papers make the procedure explicit by using open-ended video question answering benchmarks evaluated by GPT-3.5, while others describe benchmarks as covering challenging video tasks or comprehensive video analysis. These operationalizations largely match definitions that tie video understanding to answering questions, generating descriptions, and handling temporal and spatial content, although several definitions are broader than any single benchmark task. The 2 linked behavioral indicators are video detailed captioning and video question answering.

**Links.** Beyond measurement, papers link video understanding to 2 constructs and 2 behavioral indicators. One paper claims a causal relationship from temporal reasoning to video understanding, stating that enhanced textual temporal reasoning transfers to holistic video understanding, and one paper claims a causal relationship from reasoning to video understanding, describing reasoning processes as enhancing video understanding. Separately, video detailed captioning is related to video understanding, and video question answering is related to video understanding; one paper states that typical video-language tasks such as video understanding, summarization, and reasoning can be formulated as video question answering tasks.

## Sources

**Video understanding** (6 papers: [Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf), [TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/16ba99f25a235f1100a4014d71d34ad8-Paper-Conference.pdf), [Evaluating Multimodal Large Language Models on Video Captioning via Monte Carlo Tree Search](https://aclanthology.org/2025.acl-long.323.pdf), [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf), [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.98.pdf), [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/50623630a2372839c078474efa6c0cb8-Paper-Conference.pdf))
> The ability of a model to comprehend and interpret the content, context, and events within a video.

**Video comprehension** (2 papers: [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf), [SpecVLM: Enhancing Speculative Decoding of Video LLMs via Verifier-Guided Token Pruning](https://aclanthology.org/2025.emnlp-main.366.pdf))
> The general capability of a model to understand and interpret the content of a video.

**Video understanding and reasoning** (1 paper: [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf))
> Interpreting and drawing conclusions from dynamic visual sequences, such as videos, involving perception, comprehension, and adaptation.

**Long-form video understanding** (1 paper: [Streaming Video Question-Answering with In-context Video KV-Cache Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/67a9b444cbcd647572c88194619f72d5-Paper-Conference.pdf))
> A specific facet of video understanding focused on comprehending videos of extended duration, often requiring the integration of information over many minutes.

**Long-form video-language understanding** (1 paper: [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf))
> The comprehensive ability to process, comprehend, and reason about visual and linguistic information presented in videos spanning long durations, typically an hour or more.

**Explanation** (1 paper: [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf))
> The ability to infer and articulate the underlying logic, purpose, or mechanism behind what is happening in a video.

## Relationships

### Video understanding →
- **MVBench** (measurement instrument): *measured_by*, 10 papers
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
- **Video-MME** (measurement instrument): *measured_by*, 6 papers
  > For video understanding, we focused on three general benchmarks: MVBench (Li et al., 2024c), TempCompass (Liu et al., 2024c), and VideoMME (Fu et al., 2024)... (Section 4.2)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ag/xu25ag.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
- **ActivityNet-QA** (measurement instrument): *measured_by*, 5 papers
  > By scaling up the LLM to 34B, our model demonstrates a marked improvement in video understanding capabilities, achieving state-of-the-art performance on video evaluation benchmarks with accuracies of 77.4% on MSVD [68], 62.1% on MSR-VTT [70], and 55.8% on ActivityNet [69]. (Section 4.3)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **EgoSchema** (measurement instrument): *measured_by*, 4 papers
  > “and (b) multi-choice video question answering benchmarks: NExT-QA (Xiao et al., 2021), IntentQA (Li et al., 2023b), and EgoSchema (Mangalam et al., 2024).”
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://aclanthology.org/2025.emnlp-main.174.pdf)
  - [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://aclanthology.org/2025.emnlp-main.954.pdf)
- **MSVD-QA** (measurement instrument): *measured_by*, 4 papers
  > By scaling up the LLM to 34B, our model demonstrates a marked improvement in video understanding capabilities, achieving state-of-the-art performance on video evaluation benchmarks with accuracies of 77.4% on MSVD [68], 62.1% on MSR-VTT [70], and 55.8% on ActivityNet [69]. (Section 4.3)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **LongVideoBench** (measurement instrument): *measured_by*, 3 papers
  > We also evaluate the performance of mPLUG-Owl3 on video and multi-image benchmarks (including NextQA (Xiao et al., 2021), MVBench (Li et al., 2023c) VideoMME (Fu et al., 2024a), LongVideoBench (Wu et al., 2024) and MLVU (Zhou et al., 2024)), as it is capable of processing multiple images with an interleaved format.
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **MSRVTT-QA** (measurement instrument): *measured_by*, 3 papers
  > By scaling up the LLM to 34B, our model demonstrates a marked improvement in video understanding capabilities, achieving state-of-the-art performance on video evaluation benchmarks with accuracies of 77.4% on MSVD [68], 62.1% on MSR-VTT [70], and 55.8% on ActivityNet [69]. (Section 4.3)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
  - [Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf)
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **NExT-QA** (measurement instrument): *measured_by*, 3 papers
  > We also evaluate the performance of mPLUG-Owl3 on video and multi-image benchmarks (including NextQA (Xiao et al., 2021), MVBench (Li et al., 2023c) VideoMME (Fu et al., 2024a), LongVideoBench (Wu et al., 2024) and MLVU (Zhou et al., 2024)), as it is capable of processing multiple images with an interleaved format.
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **MLVU** (measurement instrument): *measured_by*, 2 papers
  > We also evaluate the performance of mPLUG-Owl3 on video and multi-image benchmarks (including NextQA (Xiao et al., 2021), MVBench (Li et al., 2023c) VideoMME (Fu et al., 2024a), LongVideoBench (Wu et al., 2024) and MLVU (Zhou et al., 2024)), as it is capable of processing multiple images with an interleaved format.
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **TempCompass** (measurement instrument): *measured_by*, 2 papers
  > we conduct comprehensive evaluations of the model across three multi-modal video benchmarks. VideoBench [52]... MVBench [36]... TempCompass [44]
  - [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
- **Perception Test** (measurement instrument): *measured_by*, 2 papers
  > We evaluate our model on a comprehensive suite of video understanding benchmarks... as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (P˘atr˘aucean et al., 2023).
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **MSVD** (measurement instrument): *measured_by*, 1 paper
  > “To assess DART’s capabilities in video understanding, we integrate it with Video-LLaVA ... achieving a notable 4.0 score on MSVD”
  - [Stop Looking for “Important Tokens” in Multimodal Language Models: Duplication Matters More](https://aclanthology.org/2025.emnlp-main.505.pdf)
- **TGIF** (measurement instrument): *measured_by*, 1 paper
  > “To assess DART’s capabilities in video understanding, we integrate it with Video-LLaVA ... achieving ... 46.3% accuracy on TGIF”
  - [Stop Looking for “Important Tokens” in Multimodal Language Models: Duplication Matters More](https://aclanthology.org/2025.emnlp-main.505.pdf)
- **MMBench-Video** (measurement instrument): *measured_by*, 1 paper
  > To address these problems, we develop a new VideoQA benchmark, MMBench-Video, to evaluate the effectiveness of LVLMs in video understanding. (Section 1)
  - [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf)
- **YouCook2** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our EMLoC on six challenging benchmarks: ... and YouCook2 for video understanding. (Section 4.1).
  - [Efficient Multi-modal Long Context Learning for Training-free Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25v/ma25v.pdf)
- **TGIF-QA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019)...
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **TVQA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our model on a comprehensive suite of video understanding benchmarks... as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (P˘atr˘aucean et al., 2023).
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **Event-Bench** (measurement instrument): *measured_by*, 1 paper
  > Table 3: Performance comparisons on 9 video benchmarks, including ActivityNet-QA (Yu et al., 2019), EgoSchema (Mangalam et al., 2023), EventBench (Du et al., 2024), LongVideoBench (Wu et al., 2024), PerceptionTest (Patraucean et al., 2023), MVBench (Li et al., 2024b), NExT-QA (Xiao et al., 2021), VNBench (Zhao et al., 2024), and VideoMME (Fu et al., 2024a). (Table 3)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **VNBench** (measurement instrument): *measured_by*, 1 paper
  > Table 3: Performance comparisons on 9 video benchmarks, including ActivityNet-QA (Yu et al., 2019), EgoSchema (Mangalam et al., 2023), EventBench (Du et al., 2024), LongVideoBench (Wu et al., 2024), PerceptionTest (Patraucean et al., 2023), MVBench (Li et al., 2024b), NExT-QA (Xiao et al., 2021), VNBench (Zhao et al., 2024), and VideoMME (Fu et al., 2024a). (Table 3)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)

### → Video understanding
- **Temporal reasoning** (construct): *causes*, 1 paper
  > These results validate that enhanced textual temporal reasoning in LLM backbones effectively transfers to holistic video understanding. (Section 4.2)
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > The results above demonstrate the effectiveness of our approach, particularly in leveraging reasoning processes to enhance video understanding.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)

### Associated with
- **Video detailed captioning** (behavioral indicator), 1 paper
  > Video detailed captioning is a key task which aims to generate comprehensive and coherent textual descriptions of video content, benefiting both video understanding and generation. (Abstract)
  - [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)
- **Video question answering** (behavioral indicator), 1 paper
  > In the research context of Video-LLMs, typical video-language tasks such as video understanding, summarization, and reasoning can be formulated as video question answering tasks. (Section 3)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
