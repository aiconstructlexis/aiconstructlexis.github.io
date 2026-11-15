# Visual relation identification
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Inter-relationship analysis, Interaction relation understanding, Relationship identification, Object interaction analysis  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this behavior as identifying or describing relationships among visual entities: "connections, interactions, or spatial dynamics" between specified objects or regions, or interactions between objects in an image. A smaller line of work narrows it to dynamic interactions in traffic scenes, including an ego vehicle's reaction to other traffic elements, while another formulation asks models to identify which properties change or stay the same across paired images in a visual analogy. In these formulations, the output is an analysis or identification of the relation, such as analyzing the relationship between marked regions or naming changed and unchanged properties.

**Variants.** Papers use several nearby names for the behavior, including inter-relationship analysis, object interaction analysis, interaction relation understanding, and relationship identification. The main settings are marked regions or arbitrarily shaped ROIs inside an image, traffic scenes with multiple agents, and cross-image analogy tasks. Some variants emphasize spatial dynamics with surrounding entities and backgrounds, while others emphasize extracting relationships between the first and second images.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior in the papers. The excerpts instead show prompt-based elicitation, for example asking a model to analyze the relationship between marked regions or to identify changed and unchanged properties across images, but they do not specify a distinct scoring instrument.

**What it is taken as evidence of.** No construct is linked to this behavior in the papers. The descriptions treat it as a task or capability description and do not state that it is evidence of any broader construct.

## Sources

**Inter-relationship analysis** (1 paper: [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf))
> The ability to identify and describe the connections, interactions, or spatial dynamics between multiple specified objects or regions within an image.

**Interaction relation understanding** (1 paper: [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf))
> The task of reasoning about the dynamic interactions between different agents in a traffic scene, such as an ego vehicle's reaction to others.

**Relationship identification** (1 paper: [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf))
> Identifying which properties stay the same or change between images in a visual analogy.

**Object interaction analysis** (1 paper: [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf))
> Describing the relationships and interactions between objects in an image.
