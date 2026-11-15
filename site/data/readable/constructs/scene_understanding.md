# Scene understanding
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Visual scene comprehension, Scene-level visual perception  

## State of the Field

**Space of definitions.** Across the surveyed papers, the prevailing usage treats scene understanding as an ability to interpret a visual environment at the scene level: perceiving the environment, identifying objects or components, and understanding their relationships, layout, and overall meaning. A recurring formulation adds semantic, spatial, and motion attributes and says the goal is a comprehensive understanding, while another application-focused wording narrows it to interpreting environmental layout and visual context well enough to support navigation decisions. A smaller variant presents it as scene-level visual perception, emphasizing whole-image content and description rather than selective identification of critical objects.

**Space of facets.** Papers break the construct down by what is being understood: objects or components, their relationships, and broader scene meaning, with one definition explicitly naming semantic, spatial, and motion attributes. The naming is not fully uniform, and closely similar abilities are also labeled visual scene comprehension and scene-level visual perception. The clearest difference in wording is scope, with some descriptions centering whole-image content and others centering critical objects that matter for downstream decisions.

**Space of measurement.** Operationally, papers link scene understanding to 1 measurement instrument and 2 behavioral indicators. The only linked instrument is MuirBench, which evaluates whether models can understand a scene comprised of multiple views from multiple surveillance images, so the recorded measurement casts the construct as multi-view scene understanding. Beyond direct measurement, the linked behavioral indicators are Action selection and Referring expression understanding, but those appear through causal claims rather than as standalone tests. The operationalization overlaps with definitions centered on scene-level understanding and relationships, while the measurement evidence does not explicitly cover every definitional facet mentioned in definitions, such as motion attributes or selective focus on critical objects.

**Links.** The recorded non-measurement links are causal rather than correlational or generic relatedness. One paper claims a causal relationship from Scene understanding to Action selection, stating that selectively identifying critical objects simplifies the description of the surrounding environment and reduces the load on decision-making processes. Another paper claims a causal relationship from Referring expression understanding to Scene understanding, with object referencing and grounding described as essential for advanced scene understanding.

## Sources

**Scene understanding** (2 papers: [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf), [Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology](https://proceedings.iclr.cc/paper_files/paper/2025/file/15ce8e7afe5ee95bad56e3b9be28d3d1-Paper-Conference.pdf))
> The cognitive ability to perceive a visual environment, selectively identify critical objects, and interpret their semantic, spatial, and motion attributes to form a comprehensive understanding.

**Visual scene comprehension** (1 paper: [Dysca: A Dynamic and Scalable Benchmark for Evaluating Perception Ability of LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2372bb107ef0ba85e47c6a2dc7dafda-Paper-Conference.pdf))
> The ability to understand and interpret the components, relationships, and overall meaning of a visual scene.

**Scene-level visual perception** (1 paper: [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf))
> The ability to understand and describe whole-image content at the scene level.

## Relationships

### Scene understanding →
- **Action selection** (behavioral indicator): *causes*, 1 paper
  > the scene understanding module in LeapAD is designed to selectively identify critical objects, simplifying the description of the surrounding environment and reducing the load on decision-making processes. (Section 3.2)
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **MuirBench** (measurement instrument): *measured_by*, 1 paper
  > [SCENE UNDERSTANDING] aims to evaluate the ability of models to understand a scene comprised of multiple views from multiple surveillance images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)

### → Scene understanding
- **Referring expression understanding** (behavioral indicator): *causes*, 1 paper
  > Object referencing and grounding are essential for advanced scene understanding.
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
