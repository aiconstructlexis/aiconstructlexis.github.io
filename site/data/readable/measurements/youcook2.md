# YouCook2
**Type:** Measurement instrument  
**Supporting papers:** 3  
**Also known as:** Youcook2  

## State of the Field

**What it is.** Across the cited definitions, papers most commonly present YouCook2 as a dense video captioning dataset. Some describe it as an English prior benchmark for video-language evaluation, while others frame it as an instructional video dataset or, more generally, as a video dataset used to evaluate dense video captioning and temporal localization.

**What it is claimed to measure.** Papers link YouCook2 to 2 behavioral indicators, Dense video captioning and Video captioning, and to 1 construct, Video understanding. The prevailing use is captioning evaluation: papers use it to measure Dense video captioning and Video captioning, while one paper also reports it as measuring Video understanding.

**Space of uses.** In use, papers position YouCook2 as an evaluation dataset within broader benchmark suites, and no measurement instrument is linked to it. One study uses it together with ActivityNet Captions as evaluation datasets, and the same study also reports performance on Charades-STA and QVHighlights; another paper lists it among six benchmarks for video understanding.

**Concerns raised.** A concern raised in one paper is domain specificity, with the paper stating that datasets like YouCook2 "highlight domain specificity." No other concern is explicitly stated.

## Sources

**YouCook2** (2 papers: [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf), [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf))
> An English dense video captioning dataset referenced as a prior benchmark for video-language evaluation.

**Youcook2** (1 paper: [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf))
> A video dataset used here to evaluate dense video captioning and temporal localization performance.

## Relationships

### → YouCook2
- **Dense video captioning** (behavioral indicator): *measured_by*, 1 paper
  > we report the performance of models using the CIDEr metric for the dense video captioning task on the Youcook2 dataset
  - [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
- **Video understanding** (construct): *measured_by*, 1 paper
  > We evaluate our EMLoC on six challenging benchmarks: ... and YouCook2 for video understanding. (Section 4.1).
  - [Efficient Multi-modal Long Context Learning for Training-free Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25v/ma25v.pdf)
- **Video captioning** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate RACCOON on diverse video datasets across tasks, including video captioning (YouCook2 (Zhou et al., 2018a), VPLM)... (Section 4)
  - [RACCooN: Versatile Instructional Video Editing with Auto-Generated Narratives](https://aclanthology.org/2025.emnlp-main.1420.pdf)
