# Spatiotemporal reasoning
**Type:** Construct  
**Supporting papers:** 13  
**Also known as:** Spatial-temporal awareness, Spatial-temporal understanding, Spatiotemporal dynamics understanding, Spatial-temporal orientation awareness, Spatial-temporal knowledge, Spatio-temporal reasoning, Spatial-temporal reasoning, Fine-grained spatio-temporal reasoning  

## State of the Field

**Space of definitions.** The prevailing usage treats spatiotemporal reasoning as an ability to reason about spatial relationships or layout together with temporal change, dynamics, or order, often in video content. Several definitions keep the scope narrow, focusing on relations between objects and their changes over time in videos or across frames, including movement, positioning, directional changes, and temporal extents. A smaller line of work broadens it to multimodal interpretation across images, videos, and 3D scenes, to using a model's own movement history to inform actions, or to building and updating a mental model of a dynamically changing environment.

**Space of facets.** Across papers, recurring facets are spatial layout or relationships, movement and orientation, temporal structure or order, and temporal properties or constraints. Authors use nearby labels, including spatial-temporal awareness, spatial-temporal understanding, spatial-temporal orientation awareness, spatial-temporal knowledge, and spatiotemporal dynamics understanding, for closely related capabilities. One paper isolates a fine-grained subtype centered on precise inferences about object locations, movements, and temporal extents across frames, and another explicitly contrasts spatiotemporal reasoning with mere visual-fact retrieval.

**Space of measurement.** Operationalization is concentrated in 3 linked measurement instruments, all benchmarks: ActivityNet-QA, MM-ID, and NExT-QA. Papers use these to assess long-term spatiotemporal reasoning in VideoQA, spatial and temporal comprehension in multimodal video understanding, and video reasoning rather than mere visual-fact retrieval. The construct is also linked to 2 behavioral indicators, Action prediction and Robotic manipulation, but through causal claims rather than direct measurement links, so measurement in these papers is benchmark-based and video-centered even though some definitions extend to robotics, 3D scenes, and changing environments.

**Links.** Beyond measurement, one paper claims a causal relationship from spatiotemporal reasoning to Action prediction, describing spatial-temporal awareness as facilitated for action prediction by encoding state-action trajectories visually. The same paper claims a causal relationship from spatiotemporal reasoning to Robotic manipulation, hypothesizing that providing the needed spatial and temporal relations supports improving manipulation tasks. The linked non-measurement claims are limited to these causal relations.

## Sources

**Spatial-temporal awareness** (1 paper: [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf))
> The model's ability to understand and utilize its history of movements and the spatial relationships evolving over time to inform its actions.

**Spatial-temporal understanding** (1 paper: [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf))
> The latent multimodal competence to interpret visual content across both spatial detail and temporal structure, including images, videos, and 3D scenes.

**Spatiotemporal reasoning** (2 papers: [Streaming Video Question-Answering with In-context Video KV-Cache Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/67a9b444cbcd647572c88194619f72d5-Paper-Conference.pdf), [Evaluating Spatiotemporal Consistency in Automatically Generated Sewing Instructions](https://aclanthology.org/2025.emnlp-main.934.pdf))
> The ability to reason about the spatial relationships between objects and their changes over time within a video.

**Spatiotemporal dynamics understanding** (1 paper: [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf))
> The ability to comprehend and model the interplay of spatial relationships and their changes over time within a video.

**Spatial-temporal orientation awareness** (1 paper: [LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25j/shen25j.pdf))
> The ability to perceive and reason about the movement, positioning, and directional changes of objects across both space and time in a video sequence.

**Spatial-temporal knowledge** (1 paper: [VisEscape: A Benchmark for Evaluating Exploration-driven Decision-making in Virtual Escape Rooms](https://aclanthology.org/2025.emnlp-main.810.pdf))
> The latent ability to construct and update a mental model of the environment that integrates spatial layout and dynamic state changes over time.

**Spatio-temporal reasoning** (1 paper: [MapEval: A Map-Based Evaluation of Geo-Spatial Reasoning in Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dihan25a/dihan25a.pdf))
> The ability to reason about entities and events considering both their spatial locations and their temporal properties or constraints.

**Spatial-temporal reasoning** (1 paper: [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf))
> The latent ability to understand and make inferences based on the spatial layout and temporal dynamics present in video content.

**Fine-grained spatio-temporal reasoning** (1 paper: [TUMTraf VideoQA: Dataset and Benchmark for Unified Spatio-Temporal Video Understanding in Traffic Scenes](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25g/zhou25g.pdf))
> The capacity to make precise inferences about object locations, movements, and temporal extents across video frames.

## Relationships

### Spatiotemporal reasoning →
- **ActivityNet-QA** (measurement instrument): *measured_by*, 1 paper
  > ActivityNet-QA (Yu et al., 2019) encompasses human-annotated QA pairs on 5,800 videos derived from the ActivityNet (Caba Heilbron et al., 2015) dataset. This benchmark is designed to assess the capabilities of VideoQA models in long-term spatiotemporal reasoning.
  - [Streaming Video Question-Answering with In-context Video KV-Cache Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/67a9b444cbcd647572c88194619f72d5-Paper-Conference.pdf)
- **MM-ID** (measurement instrument): *measured_by*, 1 paper
  > Spatial and temporal comprehension are equally important for multimodal video understanding. Here, we evaluate Video-UTR’s performance in these two areas using the latest benchmark, MM-ID, in a zero-shot setting. (Section 4.4)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
- **Action prediction** (behavioral indicator): *causes*, 1 paper
  > we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models’ spatial-temporal awareness for action prediction by encoding state-action trajectories visually. (ABSTRACT)
  - [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf)
- **Robotic manipulation** (behavioral indicator): *causes*, 1 paper
  > We hypothesize that this will effectively provide spatial and temporal relations necessary for improving manipulation tasks (Wen et al., 2023; Yuan et al., 2024). (1 INTRODUCTION)
  - [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf)
- **NExT-QA** (measurement instrument): *measured_by*, 1 paper
  > "We focus on the NExT-QA (Xiao et al., 2021) benchmark for its size, variety of human-annotated questions, and its focus on spatio-temporal reasoning in videos over mere visual-fact retrieval"
  - [Understanding Complexity in VideoQA via Visual Program Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eyzaguirre25a/eyzaguirre25a.pdf)
