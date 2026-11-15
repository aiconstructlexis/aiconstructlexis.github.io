# ActivityNet
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across the papers here, ActivityNet is most commonly treated as a large-scale video dataset or benchmark for activity or human activity understanding. Some descriptions emphasize diverse web videos, while others use it as a source of time-aligned captions and denser event pairs for temporal reasoning question creation. It also appears as the basis for an activity generation task in InterleavedBench and as a benchmark for evaluating video-based multimodal models.

**What it is claimed to measure.** Papers use ActivityNet to measure two behavioral indicators, Action recognition and Natural language planning, and it is not linked to any construct. The reported measurement claims are limited to those two indicators: one paper evaluates action recognition on ActivityNet, and another uses activity generation from ActivityNet for natural language planning.

**Space of uses.** Papers position it both as a standalone benchmark and as a source dataset inside other evaluations. It is used alongside Something-Something V2, UCF-101, YouCook2, DAVIS, and QVHighlights, and appears in action recognition evaluation, conditional video generation, video understanding, and QA data creation from captions and event pairs. No measurement instrument is linked to it.

## Sources

**ActivityNet** (4 papers: [Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf), [RACCooN: Versatile Instructional Video Editing with Auto-Generated Narratives](https://aclanthology.org/2025.emnlp-main.1420.pdf), [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/32683193e1d0e7a5795b073acecb3549-Paper-Datasets_and_Benchmarks_Track.pdf), [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf))
> A dataset for activity understanding, used as a basis for the activity generation task in the InterleavedBench evaluation benchmark.

## Relationships

### → ActivityNet
- **Natural language planning** (behavioral indicator): *measured_by*, 1 paper
  > activity generation from ActivityNet (Krishna et al., 2017) (Section 6.1).
  - [Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf)
- **Action recognition** (behavioral indicator): *measured_by*, 1 paper
  > For the action recognition task, we incorporate two baselines: Adaframe (Wu et al., 2019) and MGSampler (Zhi et al., 2021), and evaluate them alongside VILAMP on three benchmarks: ActivityNet (Caba Heilbron et al., 2015), Something-Something V2 (Sth-V2) (Goyal et al., 2017), and UCF-101 (Soomro et al., 2012). (Section 5.4)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
