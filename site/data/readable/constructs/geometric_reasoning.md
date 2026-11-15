# Geometric reasoning
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Geometric comprehension, Geometric understanding, Geometric ability, Geometric structure understanding, Geometry reasoning, Geometric problem solving, Geometric relationship identification  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats geometric reasoning as a latent ability to understand information in geometric diagrams, symbols, and text, and then carry out multi-step, often symbolic or logical inference to solve a problem. Several definitions add spatial relationships, theorems, and spatial comprehension to this framing, and some descriptions emphasize understanding basic geometric elements and their relationships as part of the challenge. A smaller line of work narrows the concept to subskills such as geometric structure understanding or geometric relationship identification, while another definition shifts from latent ability to the observable task of geometric problem solving, receiving a diagram plus text and producing an answer, often step by step.

**Space of facets.** Papers use several nearby labels for overlapping parts of this space, including geometric reasoning, geometry reasoning, geometric understanding, and geometric ability. Within that broader capability, they single out geometric comprehension of points, lines, angles, and their properties, geometric structure understanding, and geometric relationship identification, the step of identifying explicit or implicit relations such as parallel, perpendicular, or intersecting from text. One paper presents geometric relationship identification as a minimal module for evaluating understanding of geometric structures, and another places geometry reasoning as one of seven mathematical reasoning types, while geometric problem solving is used for the observable end task rather than the latent capability itself.

**Space of measurement.** Papers link geometric reasoning to 4 measurement instruments and 1 behavioral indicator. The recorded instruments are GeoQA and MathVista most often, with Geometry3K and GEOS also used through MathVista-GPS multiple-choice sub-tasks, so operationalization is mainly dataset-based evaluation on geometry problem solving test sets and sub-tasks. These measures line up most directly with definitions that emphasize multi-step problem solving and inference, while the narrower formulations around basic element comprehension or relationship identification are described separately; the only linked behavioral indicator, Hallucination, appears in a causal claim rather than as a measure.

**Links.** Beyond measurement, one paper claims a causal relationship from Hallucination to geometric reasoning, stating that severe hallucination on geometric figures hinders abilities on solving geometric problems. One paper also reports related links from Abstract reasoning to geometric reasoning and from Spatial reasoning to geometric reasoning, describing geometric ability in terms of advanced spatial comprehension and abstract thinking. No correlational link is recorded.

## Sources

**Geometric reasoning** (2 papers: [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf), [Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.38.pdf))
> The ability to perform multi-step, symbolic inference based on geometric figures and textual problem descriptions to arrive at a solution.

**Geometric comprehension** (1 paper: [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf))
> The ability to accurately perceive and understand basic geometric elements (like points, lines, angles), their properties, and their spatial relationships within a diagram.

**Geometric understanding** (1 paper: [GeoX: Geometric Problem Solving Through Unified Formalized Vision-Language Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/2722a0ccf6acfe3d144fdbb0dedd80b5-Paper-Conference.pdf))
> The ability to comprehend and interpret information from geometric diagrams, symbols, and textual descriptions.

**Geometric ability** (1 paper: [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf))
> The cognitive capacity to perform tasks involving spatial reasoning and a deep understanding of geometric diagrams and structures.

**Geometric structure understanding** (1 paper: [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf))
> The latent ability of a model to accurately comprehend and interpret the components and relationships within a geometric figure described textually.

**Geometry reasoning** (1 paper: [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf))
> The ability to understand and reason about geometric shapes, relationships, and properties, including the use of theorems and spatial configurations.

**Geometric problem solving** (1 paper: [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf))
> The observable task of receiving a geometric problem, which includes a diagram and text, and producing a final answer, often with a step-by-step solution.

**Geometric relationship identification** (1 paper: [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf))
> The specific cognitive skill of correctly identifying explicit or implicit geometric relationships between elements like points, lines, and shapes from a textual description.

## Relationships

### Geometric reasoning →
- **GeoQA** (measurement instrument): *measured_by*, 2 papers
  > We evaluate G-LLaVA on the geometry problems solving (GPS) task (testmini split) of MathVista (Lu et al., 2023) and test set of GeoQA. (Section 5.1)
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
  - [Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.38.pdf)
- **MathVista** (measurement instrument): *measured_by*, 2 papers
  > "We evaluate G-LLaVA on the geometry problems solving (GPS) task (testmini split) of MathVista"
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
  - [Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.38.pdf)
- **Geometry3K** (measurement instrument): *measured_by*, 1 paper
  > "Additionally, we show the results of sub-tasks on MathVista-GPS multiple-choice questions for easier evaluation in Table 15, which includes GeoQA+, UniGeo, Geometry3K, and GEOS."
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **GEOS** (measurement instrument): *measured_by*, 1 paper
  > "Additionally, we show the results of sub-tasks on MathVista-GPS multiple-choice questions for easier evaluation in Table 15, which includes GeoQA+, UniGeo, Geometry3K, and GEOS."
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)

### → Geometric reasoning
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > State-of-the-art MLLMs suffer severe hallucination on geometric figures, which greatly hinders their abilities on solving geometric problems. (Figure 1)
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)

### Associated with
- **Abstract reasoning** (construct), 1 paper
  > Geometric ability is a significant challenge for large language models (LLMs) due to the need for advanced spatial comprehension and abstract thinking.
  - [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf)
- **Spatial reasoning** (construct), 1 paper
  > "Geometric ability is a significant challenge for large language models (LLMs) due to the need for advanced spatial comprehension and abstract thinking."
  - [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf)
