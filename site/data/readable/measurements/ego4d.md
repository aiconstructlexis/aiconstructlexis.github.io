# Ego4D
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across the surveyed work, Ego4D is most commonly described as a large-scale egocentric video dataset. Definitions emphasize everyday activities, and one paper adds that it has dense annotations for various aspects of the videos. Papers often discuss it as source material for derived benchmarks: HourVideo is curated from Ego4D, with 500 videos covering 77 daily life scenarios, and another line of work recasts Ego4D into an offline procedural mistake detection format for Ego4D-PMD using individually annotated video frames.

**What it is claimed to measure.** Across the papers, Ego4D is linked to 1 construct and no behavioral indicators. The measurement claims center on Egocentric video understanding: one paper reports that Ego4D offers human-annotated videos and labels for certain egocentric video understanding tasks, particularly episodic memory.

**Space of uses.** No other measurement instrument is linked to it. Instead, papers mainly position Ego4D as a source dataset from which other evaluations are built or reformatted, including curation for HourVideo and recasting into an offline mistake detection setting for Ego4D-PMD.

## Sources

**Ego4D** (2 papers: [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf), [Transparent and Coherent Procedural Mistake Detection](https://aclanthology.org/2025.emnlp-main.706.pdf))
> A large-scale dataset of egocentric videos from which the videos for the HourVideo benchmark were curated.

## Relationships

### → Ego4D
- **Egocentric video understanding** (construct): *measured_by*, 1 paper
  > While Ego4D (Grauman et al., 2022) offers valuable human-annotated videos and labels for certain egocentric video understanding tasks, particularly episodic memory (which assesses a model’s ability to retain visual details in such videos)... (Section 1)
  - [MMEgo: Towards Building Egocentric Multimodal LLMs for Video QA](https://proceedings.iclr.cc/paper_files/paper/2025/file/b29a95e7d9f1e1a6dfc567b556733744-Paper-Conference.pdf)
