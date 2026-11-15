# Diagram understanding ability
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Diagram understanding, Physical diagram understanding, Diagram comprehension  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage frames this as a latent ability to interpret structured information in diagrams, including their components, layout, and semantic meaning. A smaller line of work narrows it to a perceptual ability for diagrams representing physical systems, emphasizing correct interpretation of components, their properties, and their structural relationships. The main difference is scope and framing: broad diagram interpretation in most definitions, versus perception-focused understanding in a physical-science setting in a minority framing.

**Space of facets.** Papers use closely related labels, namely diagram understanding, diagram comprehension, and physical diagram understanding, with the last functioning as the more specific variant. One paper places physical diagram understanding inside a perception component of expert-level multi-modal reasoning, describing it as understanding the physical context in multi-modal input and handling diagrams with complex physical structures.

**Space of measurement.** The only linked operationalization uses 1 measurement instrument, the MMMU benchmark, and no behavioral indicators are linked. In that use, the benchmark evidence supports a claim that current general purpose MLLMs show poor perception abilities on diagrams related to physical sciences, such as circuit diagrams, so the recorded measurement targets benchmark performance on perception of physical-science diagrams.

## Sources

**Diagram understanding** (1 paper: [Sketch2Diagram: Generating Vector Diagrams from Hand-Drawn Sketches](https://proceedings.iclr.cc/paper_files/paper/2025/file/2567c95fd41459a98a73ba893775d22a-Paper-Conference.pdf))
> The latent ability of a model to comprehend the components, layout, and semantic meaning of a diagram from an image.

**Physical diagram understanding** (1 paper: [MAPS: Advancing Multi-Modal Reasoning in Expert-Level Physical Science](https://proceedings.iclr.cc/paper_files/paper/2025/file/e0422224da8dc076cab83709b9839b7b-Paper-Conference.pdf))
> The perceptual ability to correctly interpret the components, their properties, and their structural relationships within a diagram representing a physical system.

**Diagram comprehension** (1 paper: [Diagram-Driven Course Questions Generation](https://aclanthology.org/2025.emnlp-main.305.pdf))
> The latent ability to interpret and understand the structured information presented in diagrams.

## Relationships

### Diagram understanding ability →
- **MMMU** (measurement instrument): *measured_by*, 1 paper
  > Based on observations reported in the MMMU benchmark (Yue et al., 2023) and our empirical studies, we found that current general purpose MLLMs, including the most powerful ones such as GPT-4V and Claude-3.5, exhibit poor perception abilities in understanding diagrams related to physical sciences (e.g., circuit diagrams). (Section 2)
  - [MAPS: Advancing Multi-Modal Reasoning in Expert-Level Physical Science](https://proceedings.iclr.cc/paper_files/paper/2025/file/e0422224da8dc076cab83709b9839b7b-Paper-Conference.pdf)
