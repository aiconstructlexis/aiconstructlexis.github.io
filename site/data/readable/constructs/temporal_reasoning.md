# Temporal reasoning
**Type:** Construct  
**Supporting papers:** 60  
**Also known as:** Temporal awareness, Temporal semantics, Chronological reasoning, Reverse event inference, Clock-time computation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats temporal reasoning as a broad ability to understand and reason about events over time, especially their order, duration, evolution, relative timing, and whether an event could occur at the right time. Definitions often extend this to timelines, changes in entity attributes over time, and applying time-related constraints or instructions in text, video, tables, navigation, and future-event plausibility judgments. A smaller line of work uses narrower labels for adjoining phenomena, including temporal awareness, temporal semantics, chronological reasoning, reverse event inference, and clock-time computation. The main variation is whether authors present a broad latent ability or an observable task, such as temporal sequences or explicit time calculations.

**Space of facets.** Several papers split the construct into subskills rather than treat it as unitary. One paper explicitly separates the semantics and logic of time from temporal arithmetic, and one benchmark further groups temporal questions into time-time, time-event, and event-event relations. In video-oriented work, papers also treat referring and grounding as part of the space, while some papers use narrower labels, such as temporal awareness, chronological reasoning, or clock-time computation, to isolate only one slice of the broader term.

**Space of measurement.** Operationalization is dominated by benchmarks and QA datasets: papers link temporal reasoning to 17 measurement instruments and 4 behavioral indicators. The most frequently linked instruments are LongMemEval, MVBench, TOMATO, TempCompass, and TempReason, with 12 other instruments also used; together, these cast the construct as long-context memory tasks, video temporal understanding, human-annotated multiple-choice visual temporal tasks, and QA over time-time, time-event, and event-event relations. These measurements mostly mirror the prevailing definitions around event order, timelines, and time-based relations, though some papers narrow the target to specific observable tasks such as temporal sequences or clock-time calculation.

**Links.** Only a few directional claims are recorded, and no correlational link is reported. One paper claims a causal relationship from temporal referring expression to temporal reasoning, and another claims a causal relationship from temporal reasoning to video understanding. More often, papers describe temporal reasoning as related to video question answering, temporal grounding, and analytical reasoning, with 7 other related constructs or behaviors also mentioned.

## Sources

**Temporal reasoning** (13 papers: [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf), [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf), [ViLMA: A Zero-Shot Benchmark for Linguistic and Temporal Grounding in Video-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b176e960edbb8afe77f77f9039d2738a-Paper-Conference.pdf), [Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf), [From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf), [GroundCocoa: A Benchmark for Evaluating Compositional & Conditional Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.420.pdf), [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf), [Follow the Beaten Path: The Role of Route Patterns on Vision-Language Navigation Agents Generalization Abilities](https://aclanthology.org/2025.naacl-long.406.pdf), [TRANSIENTTABLES: Evaluating LLMs' Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.332.pdf), [Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.243.pdf), [Real-time Factuality Assessment from Adversarial Feedback](https://aclanthology.org/2025.acl-long.81.pdf), [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf), [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf))
> The ability to reason about when events occurred and whether a person had the relevant opportunity at the right time.

**Temporal awareness** (2 papers: [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf), [FOUNDER: Grounding Foundation Models in World Models for Open-Ended Embodied Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ee/wang25ee.pdf))
> The ability to reason about and consistently apply instructions related to time, such as recurring events at specific intervals.

**Temporal semantics** (1 paper: [Test of Time: A Benchmark for Evaluating LLMs on Temporal Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb7295a8bc613b375726659c2ecd6f14-Paper-Conference.pdf))
> The ability to interpret the logic and meaning of temporal relations among events or entities without relying on memorized facts.

**Chronological reasoning** (1 paper: [M+: Extending MemoryLLM with Scalable Long-Term Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25au/wang25au.pdf))
> The ability to recall and reason about the temporal order of events described in a long narrative.

**Reverse event inference** (1 paper: [GLIMPSE: Do Large Vision-Language Models Truly Think With Videos or Just Glimpse at Them?](https://aclanthology.org/2025.emnlp-main.1415.pdf))
> The ability to determine the correct sequence of events or actions by reconstructing the event flow from partial information.

**Clock-time computation** (1 paper: [TCP: a Benchmark for Temporal Constraint-Based Planning](https://aclanthology.org/2025.emnlp-main.1142.pdf))
> The observable task of performing calculations involving clock times, such as determining durations or end times.

## Relationships

### Temporal reasoning →
- **LongMemEval** (measurement instrument): *measured_by*, 2 papers
  > We introduce LONGMEMEVAL, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. (Abstract)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **TempCompass** (measurement instrument): *measured_by*, 2 papers
  > To establish a connection between textual temporal reasoning ability and video comprehension, we adopt the fine-grained temporal understanding benchmark, TempCompass (Liu et al., 2024b) (Multiple-Choice subset), diagnosing multi-facet basic video temporal understanding abilities. (Section 4.1)
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
- **TempReason** (measurement instrument): *measured_by*, 2 papers
  > We demonstrate that fine-tuning and test-time scaling using TISER achieves state-of-the-art temporal reasoning performance on multiple benchmarks, including TGQA (Xiong et al., 2024), TempReason (Tan et al., 2023), and TimeQA (Chen et al., 2021) (Section 1).
  - [Learning to Reason Over Time: Timeline Self-Reflection for Improved Temporal Reasoning in Language Models](https://aclanthology.org/2025.acl-long.1358.pdf)
  - [Temporal Referential Consistency: Do LLMs Favor Sequences Over Absolute Time References?](https://aclanthology.org/2025.emnlp-main.889.pdf)
- **TimeQA** (measurement instrument): *measured_by*, 2 papers
  > We demonstrate that fine-tuning and test-time scaling using TISER achieves state-of-the-art temporal reasoning performance on multiple benchmarks, including TGQA (Xiong et al., 2024), TempReason (Tan et al., 2023), and TimeQA (Chen et al., 2021) (Section 1).
  - [Learning to Reason Over Time: Timeline Self-Reflection for Improved Temporal Reasoning in Language Models](https://aclanthology.org/2025.acl-long.1358.pdf)
  - [Will It Still Be True Tomorrow? Multilingual Evergreen Question Classification to Improve Trustworthy QA](https://aclanthology.org/2025.emnlp-main.434.pdf)
- **MVBench** (measurement instrument): *measured_by*, 2 papers
  > Results across tasks, including general video understanding (Video-MME), video temporal reasoning (MVBench, TempCompass), and long video understanding (MLVU, LongVideoBench, EgoSchema). (Table 2)
  - [VRoPE: Rotary Position Embedding for Video Large Language Models](https://aclanthology.org/2025.emnlp-main.731.pdf)
  - [A Culturally-diverse Multilingual Multimodal Video Benchmark & Model](https://aclanthology.org/2025.emnlp-main.1012.pdf)
- **TOMATO** (measurement instrument): *measured_by*, 2 papers
  > "we test our models on two recent benchmarks with complementary temporal characteristics: TOMATO (Shangguan et al., 2024) and Vinoground (Zhang et al., 2024a)."
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
  - [TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/16ba99f25a235f1100a4014d71d34ad8-Paper-Conference.pdf)
- **BIG-bench** (measurement instrument): *measured_by*, 1 paper
  > "We further evaluate on various reasoning tasks in BIG-Bench (Srivastava et al., 2022; Suzgun et al., 2022): word sorting, logical deduction five objects, temporal sequences, reasoning about colored objects, and formal fallacies."
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **MMBench-Video** (measurement instrument): *measured_by*, 1 paper
  > The benchmark is meticulously crafted to probe the models’ temporal reasoning skills, with all questions human-annotated according to a carefully constructed ability taxonomy. (Abstract)
  - [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf)
- **bAbI** (measurement instrument): *measured_by*, 1 paper
  > "the reasoning skills they assess, including spatial and temporal reasoning, deduction, and coreference resolution"
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **EgoSchema** (measurement instrument): *measured_by*, 1 paper
  > Results on EgoSchema (accuracy), a long-form video benchmark (∼3 minutes) for first-person view temporal reasoning. (Table 5).
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
- **Video understanding** (construct): *causes*, 1 paper
  > These results validate that enhanced textual temporal reasoning in LLM backbones effectively transfers to holistic video understanding. (Section 4.2)
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **MLVU** (measurement instrument): *measured_by*, 1 paper
  > "For a comprehensive assessment of long-form video understanding capabilities, we choose two challenging benchmarks: MLVU (Zhou et al., 2024) and Video-MME (Fu et al., 2024). These benchmarks are specifically designed to test temporal reasoning across diverse domains."
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Video-MME** (measurement instrument): *measured_by*, 1 paper
  > "For a comprehensive assessment of long-form video understanding capabilities, we choose two challenging benchmarks: MLVU (Zhou et al., 2024) and Video-MME (Fu et al., 2024). These benchmarks are specifically designed to test temporal reasoning across diverse domains."
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **NExT-QA** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on three popular VideoQA datasets: NExT-QA, STAR, and IntentQA (Xiao et al., 2021; Wu et al., 2021; Li et al., 2023a), which demand both causal and temporal reasoning abilities.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
- **STAR** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on three popular VideoQA datasets: NExT-QA, STAR, and IntentQA (Xiao et al., 2021; Wu et al., 2021; Li et al., 2023a), which demand both causal and temporal reasoning abilities.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
- **IMPLIRET** (measurement instrument): *measured_by*, 1 paper
  > "IMPLIRET covers three reasoning categories: World Knowledge, Arithmetic, and Temporal."
  - [ImpliRet: Benchmarking the Implicit Fact Retrieval Challenge](https://aclanthology.org/2025.emnlp-main.1685.pdf)
- **ComplexTempQA** (measurement instrument): *measured_by*, 1 paper
  > Additionally, each question is accompanied by detailed metadata, including specific time scopes, allowing for comprehensive evaluation of temporal reasoning abilities of large language models.
  - [ComplexTempQA: A 100m Dataset for Complex Temporal Question Answering](https://aclanthology.org/2025.emnlp-main.463.pdf)
- **LogiQA** (measurement instrument): *measured_by*, 1 paper
  > “LogiQA, marketed as a logical reasoning benchmark, in fact leans most on Temporal Reasoning and Commonsense Causal Reasoning”
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)

### → Temporal reasoning
- **Temporal referring expression** (behavioral indicator): *causes*, 1 paper
  > To enable the model to temporally localize change, we include tasks instructing the model to identify the specific image(s) in which a given change occurred. (Section 3.1.2).
  - [TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac3af725ae398b6184faae0828bdbd6c-Paper-Conference.pdf)

### Associated with
- **Video question answering** (behavioral indicator), 2 papers
  > Wang et al. (2023b) and Ko et al. (2023) try to leverage LLaMA’s (Touvron et al., 2023) knowledge of temporal and causal reasoning to address the complexities of VideoQA.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
- **Fine-grained video understanding** (construct), 1 paper
  > Moreover, fine-grained video understanding demands a deep comprehension of how objects change and interact over time, particularly at a detailed level. This complexity necessitates temporal reasoning tasks to effectively analyze these dynamics.
  - [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf)
- **Visual reasoning** (construct), 1 paper
  > Our task suite encompasses a comprehensive set of perceptual and cognitive tasks, including summarization, perception (recall, tracking), visual reasoning (spatial, temporal, predictive, causal, counterfactual), and navigation (room-to-room, object retrieval) tasks. (Section 2.1)
  - [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Temporal arithmetic** (construct), 1 paper
  > Our benchmark, Test of Time, ToT, is centered around the observation that temporal reasoning often involves two primary skills: 1) understanding the semantics and logic of time, and 2) the ability to carry out temporal arithmetic.
  - [Test of Time: A Benchmark for Evaluating LLMs on Temporal Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb7295a8bc613b375726659c2ecd6f14-Paper-Conference.pdf)
- **Factual retention** (construct), 1 paper
  > For factual retention, we further divide this category into four finer sub-categories: (1) Visual Perception (OCR, Spatial Reasoning), (2) Audio Perception, (3) Full Video Understanding (i.e., tasks that require information across several parts of the video), and (4) Temporal Reasoning (i.e., tasks that require understanding the video with respect to time).
  - [VideoWebArena: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf)
- **Temporal referring** (behavioral indicator), 1 paper
  > Temporal reasoning encompasses several key aspects. Based on recent Video LLM benchmarks (Fu et al., 2024; Wu et al., 2024), we focus on four critical dimensions: ... (3) Temporal Referring: formulating questions based on specific temporal positions within a video (Section 2.2)
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Temporal grounding** (behavioral indicator), 1 paper
  > Temporal reasoning encompasses several key aspects. Based on recent Video LLM benchmarks (Fu et al., 2024; Wu et al., 2024), we focus on four critical dimensions: ... and (4) Temporal Grounding: identifying the temporal location of specific elements in a video. (Section 2.2)
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Analytical reasoning** (construct), 1 paper
  > This involves several reasoning types: numerical reasoning for interpreting data, temporal reasoning for time-related concepts, lexical reasoning for word meanings, domain-specific reasoning for specialized knowledge, and common-sense reasoning for inferences.
  - [TRANSIENTTABLES: Evaluating LLMs' Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Planning** (construct), 1 paper
  > "While these efforts highlight the relevance of temporal reasoning in planning"
  - [TCP: a Benchmark for Temporal Constraint-Based Planning](https://aclanthology.org/2025.emnlp-main.1142.pdf)
- **Table reasoning** (construct), 1 paper
  > Third, we note a marked increase in arithmetic and temporal reasoning capabilities. The model becomes more adept at performing arithmetic calculations over table entries and reasoning over temporal sequences, both of which are crucial for table reasoning tasks. (Section 4.6)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
