# Temporal grounding
**Type:** Behavioral indicator  
**Supporting papers:** 8  
**Also known as:** Moment localization, Temporal video grounding, Clue retrieval, Episodic memory, Moment retrieval  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is localizing a moment, span, segment, or timestamps in a video that match a question, answer event, supporting evidence, or a natural-language query. Most definitions converge on finding the video evidence needed for a question, often described as selecting the related clips or localizing the answer event span; some formulations make the required output more explicit by asking for start and end timestamps or the intervals of clues that can accurately answer the question. A smaller strand casts the same behavior as grounding a textual description to a video segment, and one egocentric formulation asks models to find the visual event that can answer the question.

**Variants.** Papers use several near-synonymous task names, most commonly moment localization, temporal video grounding, clue retrieval, episodic memory, and moment retrieval. The common setting is video, but the prompts vary: some studies use question answering over answer-supporting evidence, some use query sentences or textual descriptions, and some focus on egocentric scenarios. A smaller line of work extends the label beyond video, describing temporal grounding as retrieving or extracting the relevant set of tables needed to answer a question, that is, retrieval over temporal information.

**Space of elicitation and scores.** Papers measure it with two linked instruments, Charades-STA and QVHighlights, both used as benchmarks for locating described activities or relevant moments from text or user queries. Charades-STA is used for moment retrieval and temporal grounding evaluations that report recall at IoU thresholds of 0.5 and 0.7, while QVHighlights is used for temporal video grounding and for identifying relevant moments and highlights. More generally, grounding tasks are also scored with retrieval and overlap measures such as R@N and IoU=M.

**What it is taken as evidence of.** Papers link temporal grounding to five constructs, rather than to a single shared construct. Some papers treat it as related to temporal understanding, fine-grained video understanding, and temporal reasoning, including a formulation that places temporal grounding as one dimension within temporal reasoning. Other papers claim a causal relationship from temporal grounding to temporal grounding ability and to long video understanding.

## Sources

**Moment localization** (1 paper: [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/32683193e1d0e7a5795b073acecb3549-Paper-Datasets_and_Benchmarks_Track.pdf))
> Predicting the temporal span in a video that corresponds to the answer event or relevant evidence for a question.

**Temporal grounding** (2 papers: [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf), [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf))
> Identifying the video segments or timestamps that correspond to the evidence needed for a question.

**Temporal video grounding** (1 paper: [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/32683193e1d0e7a5795b073acecb3549-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of localizing a specific moment or time span in a video that corresponds to a given natural language text query.

**Clue retrieval** (1 paper: [CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/70fa5df8e3300dc30bf19bee44a56155-Paper-Conference.pdf))
> The observable action of identifying and outputting specific time intervals within a video that support an answer.

**Episodic memory** (1 paper: [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf))
> Localizing the video moment that contains the evidence needed to answer an egocentric question.

**Moment retrieval** (1 paper: [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf))
> The task of identifying the start and end timestamps of a video segment that corresponds to a given natural language query.

## Relationships

### Temporal grounding →
- **Charades-STA** (measurement instrument): *measured_by*, 3 papers
  > We utilize test set of Charades-STA (Gao et al., 2017) for the moment retrieval task and report the recall at IOU thresholds of 0.5 and 0.7.
  - [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
  - [Language-Guided Temporal Token Pruning for Efficient VideoLLM Processing](https://aclanthology.org/2025.emnlp-main.451.pdf)
- **QVHighlights** (measurement instrument): *measured_by*, 3 papers
  > Task [TVG] Temporal Video Grounding Source QVHighlights [44] (Table 4)
  - [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/32683193e1d0e7a5795b073acecb3549-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **Temporal grounding ability** (construct): *causes*, 2 papers
  > We present a novel training strategy specifically designed to enhance the temporal localization abilities of Vid-LLMs... we fine-tune our Vid-LLM in the second stage on dense video captioning and temporal grounding tasks.
  - [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf)
  - [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
- **Long video understanding** (construct): *causes*, 1 paper
  > We argue long video understanding could be assisted by explicitly performing temporal grounding, as grounding supervision enables MLLM to establish the detailed correspondance between the visual segments and fine-grained semantics.
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)

### Associated with
- **Temporal understanding** (construct), 2 papers
  > These limitations are particularly problematic for temporal understanding tasks that rely on maintaining temporal coherence across frames, such as highlight detection and temporal grounding.
  - [Language-Guided Temporal Token Pruning for Efficient VideoLLM Processing](https://aclanthology.org/2025.emnlp-main.451.pdf)
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
- **Fine-grained video understanding** (construct), 1 paper
  > Comprehending videos in fine-grained aspects requires precisely locating and understanding specific events within a video. It is roughly divided by previous works [10] into temporal grounding [2, 7] and dense video captioning [13, 31] tasks.
  - [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf)
- **Temporal reasoning** (construct), 1 paper
  > Temporal reasoning encompasses several key aspects. Based on recent Video LLM benchmarks (Fu et al., 2024; Wu et al., 2024), we focus on four critical dimensions: ... and (4) Temporal Grounding: identifying the temporal location of specific elements in a video. (Section 2.2)
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator), 1 paper
  > Temporal Grounding. Accurately identify and retrieve/extract the relevant set of tables necessary to answer the question. This can be regarded as retrieval over temporal information.
  - [TRANSIENTTABLES: Evaluating LLMs' Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.332.pdf)
