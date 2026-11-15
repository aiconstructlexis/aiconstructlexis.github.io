# Temporal grounding ability
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Temporal grounding, Video temporal grounding, Temporal localization, Referring  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this construct as mapping language to a precise segment of video time. Papers describe associating a textual query or question with the relevant time segment in a video, precisely identifying timestamps of specific events from a textual query or instruction, or understanding time information in user inputs so the model can identify which part of a video is being referred to. A smaller framing narrows it to temporal localization of relevant sub-action frames and their alignment across videos, so the main variation is between general event localization within a video and cross-video sub-action localization.

**Space of facets.** Papers most commonly use closely related labels for nearby formulations: temporal grounding and video temporal grounding name the query-to-time-span version, while referring names the user-time-reference version. Another line uses temporal localization for a narrower case centered on finding the sub-action frames where differences occur and aligning those frames between videos. The labels therefore differ mainly in whether the target is an event timestamp, a referred video segment, or sub-action frames aligned across videos.

**Space of measurement.** No measurement instrument is linked to it, so no benchmark, human evaluation, LLM-as-a-judge, probe, or analysis instrument is recorded. Papers link it to two behavioral indicators, temporal grounding and dense video captioning, and no construct link is recorded. These links are not measured_by relations: temporal grounding mirrors the dominant query-to-time-segment definitions, while dense video captioning appears only as a related downstream task rather than a direct measure.

**Links.** The recorded links focus on temporal grounding and dense video captioning. One paper claims a causal relationship from temporal grounding to temporal grounding ability, describing fine-tuning on temporal grounding tasks as enhancing temporal localization abilities, while another paper treats video temporal grounding as related to the construct. Dense video captioning is related to temporal grounding ability in one paper, which presents it as a downstream task built on video temporal grounding. No correlational link is reported.

## Sources

**Temporal grounding** (1 paper: [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf))
> The ability to accurately associate a textual query or question with the specific time segment in a video where the relevant event occurs.

**Video temporal grounding** (1 paper: [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf))
> The model's ability to precisely identify and localize the timestamps of specific events within a video based on a textual query or instruction.

**Temporal localization** (1 paper: [Video Action Differencing](https://proceedings.iclr.cc/paper_files/paper/2025/file/26f62bf3b74cda621831f550c6ee2dce-Paper-Conference.pdf))
> The ability to identify the specific sub-action frames where a relevant difference occurs and align those frames across videos.

**Referring** (1 paper: [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to comprehend time information from user inputs and identify which part of a video the user is referring to.

## Relationships

### → Temporal grounding ability
- **Temporal grounding** (behavioral indicator): *causes*, 2 papers
  > We present a novel training strategy specifically designed to enhance the temporal localization abilities of Vid-LLMs... we fine-tune our Vid-LLM in the second stage on dense video captioning and temporal grounding tasks.
  - [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf)
  - [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)

### Associated with
- **Dense video captioning** (behavioral indicator), 1 paper
  > Video Temporal Grounding (VTG) is an important ability for video understanding models (Lin et al., 2023b), and has becoming the base of a series of downstream tasks like moment retrieval (Fabian Caba Heilbron & Niebles, 2015; Gao et al., 2017; Oncescu et al., 2021), dense video caption (Zhou et al., 2018; Tang et al., 2019), video highlight detection (Lei et al.; Liu et al., 2022), and video summarization (Song et al., 2015; Gygli et al., 2014).
  - [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
