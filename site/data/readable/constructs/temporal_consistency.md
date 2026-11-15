# Temporal consistency
**Type:** Construct  
**Supporting papers:** 7  
**Also known as:** Temporal coherence  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats temporal consistency, often also called temporal coherence, as coherence or stability over time, most commonly in videos across frames. The broadest definitions describe generated video as maintaining "smooth, logically continuous progression across frames without flicker or discontinuities" or preserving the logical flow of events and objects across frames, while narrower video-focused definitions restrict it to stable, coherent segmentation masks for an object across consecutive frames or to stable main subject and background elements over time. A smaller line of work uses temporal coherence for text, defining it as the logical and chronological flow of ideas across sentences and as a latent property reflected in time-ordered representations.

**Space of facets.** Papers organize the concept mainly by what must remain stable over time: whole-video progression, events and objects across frames, segmentation masks, or, in one text-focused usage, ideas across sentences. The terminology is not fully settled, because "temporal coherence" and "temporal consistency" are both used for cross-frame continuity in generated video, and "temporal coherence" is also used for document coherence, so the same name covers both output-level continuity and a latent textual property. Some formulations also narrow the video case to particular facets, such as consistency of the main subject and background.

**Space of measurement.** No measurement instrument is formally linked to this construct, and only one behavioral indicator is linked, Video object segmentation. In practice, papers still operationalize it with named scores and evaluation dimensions: CHScore is described as assessing whether generated videos maintain logical progression and continuity, Flow-score is cited for temporal consistency, one "Consistency" dimension checks whether the main subject and background stay stable over time, and one text-focused paper describes BBScoreV2 as capturing temporal structure and assessing document coherence. These operationalizations mostly track the definitions, but they span several targets, from whole-video continuity to segmentation stability and textual flow.

**Links.** The only explicit relationship reported is that temporal consistency is related to Video object segmentation. One paper describes video object segmentation as requiring models to capture temporal dynamics in the input video and to predict temporally consistent segmentation masks across frames on the output side. No causal claims, correlations, or links to other constructs are reported.

## Sources

**Temporal coherence** (2 papers: [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf), [BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation](https://aclanthology.org/2025.emnlp-main.151.pdf))
> The extent to which a generated video maintains smooth, logically continuous progression across frames without flicker or discontinuities.

**Temporal consistency** (2 papers: [One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf), [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf))
> The quality of producing segmentation masks for an object that are stable and coherent across consecutive video frames.

## Relationships

### Associated with
- **Video object segmentation** (behavioral indicator), 1 paper
  > VOS requires models to 1) on the input side, capture and comprehend the temporal dynamics present in the video; and 2) on the output side, predict temporally consistent segmentation masks across frames. (Section 1)
  - [One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf)
