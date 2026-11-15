# Video captioning
**Type:** Behavioral indicator  
**Supporting papers:** 29  
**Also known as:** Video scripting, Clip summarization, Video description generation, Audio description generation, Video narration, Caption generation, Video description  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats video captioning as generating a textual or natural-language description of a video's content or events. Most definitions stay broad, covering whole videos or video segments, while some sharpen the target to captions that accurately and comprehensively summarize the video, closely resemble human-written captions, or are refined using video-text similarity feedback.

**Variants.** Most papers keep the generic captioning framing, but a smaller line of work studies narrower variants. These include video scripting, with structured scene details such as a title, content, shot type, and camera movement; clip summarization for a time-stamped clip inside a longer video; audio description generation as accessibility-oriented narration of key visual elements; video narration as real-time descriptive text for a video stream; and video description generation focused on anomalous events. Some papers also shift from whole-video outputs to segment-level descriptions or emphasize especially detailed descriptions of subjects, environment, motion, camera parameters, and style.

**Space of elicitation and scores.** Papers link video captioning to 5 measurement instruments. MSR-VTT is the most commonly linked, used for zero-shot captioning or to evaluate captioning ability; the other linked instruments are LLM-as-a-judge, where GPT-4 scores caption generation results, MM-ID, which includes captioning as one of four competency levels, VATEX for zero-shot video captioning, and YouCook2 in task-based evaluation. Across these links, papers measure the task with named evaluation resources and one judge-based scoring setup.

**What it is taken as evidence of.** No construct is linked to video captioning in the relationships reported by papers. Papers therefore do not explicitly specify a construct that this behavior is evidence of.

## Sources

**Video captioning** (6 papers: [Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf), [Exploring the Design Space of Visual Context Representation in Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/24e2320097bdf179e2b2719c6df2f448-Paper-Conference.pdf), [Direct Preference Optimization of Video Large Multimodal Models from Language Model Reward](https://aclanthology.org/2025.naacl-long.30.pdf), [MEDA: Dynamic KV Cache Allocation for Efficient Multimodal Long-Context Inference](https://aclanthology.org/2025.naacl-long.125.pdf), [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf), [VC4VG: Optimizing Video Captions for Text-to-Video Generation](https://aclanthology.org/2025.emnlp-main.59.pdf))
> The task of generating a textual description of the content of a video.

**Video scripting** (1 paper: [Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf))
> Describing a video scene with structured details such as title, content, shot type, and camera movement.

**Clip summarization** (1 paper: [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of generating a summary caption for a specific time-stamped clip within a longer video, potentially by reusing pre-computed differential captions.

**Video description generation** (1 paper: [HAWK: Learning to Understand Open-World Video Anomalies](https://proceedings.neurips.cc/paper_files/paper/2024/file/fca83589e85cb061631b7ebc5db5d6bd-Paper-Conference.pdf))
> The task of generating a natural language text that describes the content of a video, with a specific focus on anomalous events.

**Audio description generation** (1 paper: [CALVIN: Improved Contextual Video Captioning via Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a922b7121007768f78f770c404415375-Paper-Conference.pdf))
> The task of generating a verbal narration of the key visual elements in a video, intended to make content accessible to visually impaired individuals.

**Video narration** (1 paper: [VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf))
> The task of generating real-time, descriptive text that narrates the events occurring in a video stream.

**Caption generation** (1 paper: [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf))
> The observable task of producing text descriptions that summarize or detail the content of video segments.

**Video description** (1 paper: [Is Your Video Language Model a Reliable Judge?](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc4f891373d19087d1ddda33e81e00e4-Paper-Conference.pdf))
> Generating a textual description of the content of a video.

## Relationships

### Video captioning →
- **MSR-VTT** (measurement instrument): *measured_by*, 3 papers
  > We further perform zero-shot video captioning on MSR-VTT [75] and VATEX [62]. (Section 4.3)
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
  - [Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf)
- **VATEX** (measurement instrument): *measured_by*, 1 paper
  > We further perform zero-shot video captioning on MSR-VTT [75] and VATEX [62]. (Section 4.3)
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **MM-ID** (measurement instrument): *measured_by*, 1 paper
  > "MM-ID dissects LVLMs’ competency across four progressively complex levels: matching, location, question-answering, and captioning."
  - [IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/82dcb6da1b408d59d15f68afdebf1489-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > "For question-answering and caption generation tasks... GPT-4 is used to score the results."
  - [IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/82dcb6da1b408d59d15f68afdebf1489-Paper-Conference.pdf)
- **YouCook2** (measurement instrument): *measured_by*, 1 paper
  > We evaluate RACCOON on diverse video datasets across tasks, including video captioning (YouCook2 (Zhou et al., 2018a), VPLM)... (Section 4)
  - [RACCooN: Versatile Instructional Video Editing with Auto-Generated Narratives](https://aclanthology.org/2025.emnlp-main.1420.pdf)
