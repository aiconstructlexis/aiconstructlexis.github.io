# Action localization
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Temporal action localization, Accident temporal localization  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats action localization as finding when a specified action occurs in a video by marking its temporal extent, usually with start and end times. Most definitions describe detecting and localizing temporal segments that contain a given action, and some explicitly extend this to finding all matching segments in a long or untrimmed video. A narrower variant applies the same formulation to traffic accidents, where success is identifying the precise start and end timestamps of the accident event within a clip.

**Variants.** Papers most commonly use the names Action Localization and Temporal Action Localization. The settings vary across animal-centric videos, longer untrimmed videos, and traffic accident clips, with examples phrased as locating where an action such as "flying" occurs or finding all segments for a named action in a long video. A smaller line of work specializes this as accident temporal localization, and one paper also describes it as accident duration.

**Space of elicitation and scores.** Only one measurement instrument is linked to this behavior, MVBench. One paper reports that action localization is measured by MVBench, which it describes as a video-language understanding benchmark covering multiple challenging video tasks, including an Action Localization task.

**What it is taken as evidence of.** No construct is linked to action localization in the reported relationships, so the papers do not specify a broader construct that this behavior is taken to indicate.

## Sources

**Action localization** (1 paper: [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf))
> Identifying when a specified action occurs within a video timeline.

**Temporal action localization** (2 papers: [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf), [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf))
> The task of detecting and localizing all temporal segments in a video that contain a specific, given action.

**Accident temporal localization** (1 paper: [TAU-106K: A New Dataset for Comprehensive Understanding of Traffic Accident](https://proceedings.iclr.cc/paper_files/paper/2025/file/b33ad9d46ab2a23b6783d954121d26e3-Paper-Conference.pdf))
> The task of identifying the precise start and end timestamps of a traffic accident event within a video clip.

## Relationships

### Action localization →
- **MVBench** (measurement instrument): *measured_by*, 1 paper
  > MVBench [29] is a recent video-language understanding benchmark that covers 20 challenging video tasks... TOPA Surprisingly excels in the Action Localization (AL) task
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
