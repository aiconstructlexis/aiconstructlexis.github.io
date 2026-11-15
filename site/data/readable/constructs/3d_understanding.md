# 3D understanding
**Type:** Construct  
**Supporting papers:** 9  
**Also known as:** 3D awareness, Object-level 3D awareness, 3D-related reasoning, 3D scene understanding, 3D scene representation  

## State of the Field

**Space of definitions.** Across the literature, the prevailing usage describes 3D understanding as a latent ability to infer, represent, ground, and reason about the three-dimensional structure of objects and scenes from 2D or RGB inputs. Definitions largely converge on geometry, layout, object properties, and spatial relations as the shared content. A smaller line of work uses nearby labels such as 3D awareness for accounting for depth during compositing, narrows the concept to object-level encoding of structure and viewpoint in internal representations, or emphasizes constructing and maintaining a metrically accurate scene model over time from egocentric visual inputs.

**Space of facets.** Papers systematize the concept mainly by level and function. Object-level formulations target whether representations encode discriminative information about 3D structure and viewpoint, scene-level formulations target reasoning about objects, attributes, and their spatial relationships in a 3D environment, and a temporal formulation centers on maintaining coherent 3D scene representations across frames. Related labels also separate representation from reasoning: some papers use 3D-related reasoning for reasoning about pose, distance, and spatial relationships using integrated 3D information, while broader terms such as 3D understanding or 3D awareness refer to the more general ability.

**Space of measurement.** Papers link the construct to 2 measurement instruments, ScanQA and SQA3D, and to 2 behavioral indicators, 3D question answering and motion planning, with no linked constructs. The explicitly linked measurements are benchmark evaluations: papers report 3D spatial understanding on the ScanQA validation set and use ScanQA and SQA3D to demonstrate improved overall 3D scene understanding and reasoning. These operationalizations emphasize scene understanding and reasoning, in line with the dominant definitions, while a narrower object-level usage is evaluated by linear probing frozen feature representations on a 3D viewpoint classification task.

**Links.** Beyond measurement, one paper claims a causal relationship from 3D understanding to motion planning, stating that higher-level 3D-aware tasks such as motion planning require a "fundamental and explicit" 3D understanding. One paper also reports that 3D question answering is related to 3D understanding, using 3D-QA as a representative example of 3D scene understanding tasks. No correlational links or construct-to-construct links are reported.

## Sources

**3D understanding** (2 papers: [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf), [Language-Image Models with 3D Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a829e299ebc1c1615ddb09e98fb6ce8-Paper-Conference.pdf))
> The model's ability to infer and represent the three-dimensional structure, layout, and properties of a scene and its objects from two-dimensional inputs.

**3D awareness** (1 paper: [$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf))
> The latent capacity to account for depth and three-dimensional geometry when placing or compositing objects into a scene.

**Object-level 3D awareness** (1 paper: [ImageNet3D: Towards General-Purpose Object-Level 3D Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae51515c1cfecf544963a527260f94e9-Paper-Datasets_and_Benchmarks_Track.pdf))
> The degree to which a model's internal representations encode discriminative information about the 3D structure and viewpoint of objects.

**3D-related reasoning** (1 paper: [ImageNet3D: Towards General-Purpose Object-Level 3D Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae51515c1cfecf544963a527260f94e9-Paper-Datasets_and_Benchmarks_Track.pdf))
> The cognitive ability of a model, particularly an LLM, to reason about object properties like pose, distance, and spatial relationships using integrated 3D information.

**3D scene understanding** (1 paper: [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf))
> The ability to comprehend and reason about the objects, their attributes, and their spatial relationships within a three-dimensional environment.

**3D scene representation** (1 paper: [Out of Sight, Not Out of Context? Egocentric Spatial Reasoning in VLMs Across Disjoint Frames](https://aclanthology.org/2025.emnlp-main.816.pdf))
> The internal construction and maintenance of a metrically accurate, three-dimensional model of a scene from egocentric visual inputs, enabling spatial inference across time.

## Relationships

### 3D understanding →
- **ScanQA** (measurement instrument): *measured_by*, 2 papers
  > on ScanQA and SQA3D, which do not require object referencing and grounding, we still achieve consistent performance enhancement, demonstrating improved overall 3D scene understanding and reasoning
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
- **Motion planning** (behavioral indicator): *causes*, 1 paper
  > ...higher-level 3D-aware tasks, such as articulating dynamic scene changes and motion planning, require a fundamental and explicit 3D understanding beyond current spatial VQA datasets. (Abstract)
  - [SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf)
- **SQA3D** (measurement instrument): *measured_by*, 1 paper
  > on ScanQA and SQA3D, which do not require object referencing and grounding, we still achieve consistent performance enhancement, demonstrating improved overall 3D scene understanding and reasoning
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)

### Associated with
- **3D question answering** (behavioral indicator), 1 paper
  > In this work, we explore how to harness their potential to address 3D scene understanding tasks, using 3D question answering (3D-QA) as a representative example. (Abstract)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
