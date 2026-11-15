# QVHighlights
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Most descriptions treat QVHighlights as an evaluation benchmark for highlight detection, or more broadly for detecting moments and highlights in videos from natural language queries. In that usage, models are asked to identify highlight moments and their saliency scores for a given query. A smaller line of work treats it as a video dataset for QA creation, describing YouTube videos with sparsely annotated captions or events and event pairs; one paper says it features over 10,000 videos across various themes.

**What it is claimed to measure.** Across papers, the measurement claims converge on Temporal grounding. QVHighlights is linked to one behavioral indicator, Temporal grounding, and no constructs, and papers report using it for the video grounding task and for identifying relevant moments and highlights in response to user queries.

**Space of uses.** Papers commonly position QVHighlights as an evaluation benchmark rather than as an auxiliary check. It is used for experiments on video grounding and temporal localization, appears alongside Charades-STA in zero-shot temporal localization reporting, and is selected with ActivityNet for QA data creation. One definition also says it is used as a source for grounding, highlight detection, and temporal event matching.

**Concerns raised.** One paper notes a sparsity issue: captions or events in QVHighlights are sparsely annotated, so related events are found from an initial pivotal event.

## Sources

**QVHighlights** (3 papers: [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf), [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf), [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/32683193e1d0e7a5795b073acecb3549-Paper-Datasets_and_Benchmarks_Track.pdf))
> An evaluation benchmark for the highlight detection task, requiring a model to identify all highlight moments and their saliency scores for a given query.

## Relationships

### → QVHighlights
- **Temporal grounding** (behavioral indicator): *measured_by*, 3 papers
  > Task [TVG] Temporal Video Grounding Source QVHighlights [44] (Table 4)
  - [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/32683193e1d0e7a5795b073acecb3549-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
