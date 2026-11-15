# Text-image alignment
**Type:** Construct  
**Supporting papers:** 6  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats text-image alignment as semantic correspondence between generated visual output and the input text: papers describe it as the degree to which an image matches a caption, narrative fragment, or prompt, and faithfully reflects its visual concepts, intended elements, and descriptive details. Some papers make this more specific by stressing visual consistency in narrative depictions, such as characters and settings, while another frames it as a multimodal capability, the joint interpretation of visual content and embedded text so meaning stays consistent across modalities.

**Space of facets.** Papers do not provide an explicit subtype taxonomy, but they use the term across several scopes. In narrower uses it concerns caption or prompt matching for generated images or other visual assets, while broader uses include consistency across story elements and alignment when textual elements are partially visible inside the image itself. No definition explicitly equates it with another construct or places it under a larger construct.

**Space of measurement.** Operationalization is narrow in the papers: it is linked to 2 measurement instruments, LLM-as-a-judge and Pick-a-Pic, and to 1 behavioral indicator, Boolean question answering. One paper uses MLLM-as-a-Judge with golden answers and an Analyze-then-Judge chain of thought to score generation quality, text-image alignment, and helpfulness, while another uses Pick-a-Pic as a benchmark for agreement with human judgments of alignment on images generated from complex text prompts. A related setup uses Boolean yes or no questions generated from text so a model can assess visual-textual alignment consistently.

**Links.** Beyond measurement links, no causal or correlational claims are reported, and no links to other constructs are reported. The only non-measurement link is a related relation involving Boolean question answering: one paper describes converting text into yes or no questions so the model can assess visual-textual alignment in a consistent manner.

## Sources

**Text-image alignment** (1 paper: [AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7641940c7dd9e5de58c20e39586eb64-Paper-Conference.pdf))
> The degree to which the generated image semantically corresponds to the input caption, reflecting accurate interpretation of visual concepts from text.

## Relationships

### Text-image alignment →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > Building on previous work (An et al., 2023; Liu et al., 2024d), we enhance the process by employing MLLM-as-a-Judge with golden answers and the "Analyze-then-Judge" Chain-of-Thought (CoT) (Wei et al., 2022). This allows for a more human-aligned evaluation, assessing generation quality, text-image alignment, and helpfulness to yield a comprehensive score.
  - [Interleaved Scene Graphs for Interleaved Text-and-Image Generation Assessment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e0ceee9751ae8b5c6603c029e4ca42-Paper-Conference.pdf)
- **Pick-a-Pic** (measurement instrument): *measured_by*, 1 paper
  > 2) Score agreement with human judgments of alignment for image-text alignment, using images generated from complex text prompts. We report results on five text-to-image evaluation benchmarks (DrawBench (Saharia et al., 2022), EditBench (Wang et al., 2023a), COCO-T2I (Lin et al., 2014), TIFA160 (Hu et al., 2023), Pick-a-Pic (Kirstain et al., 2023)).
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)

### Associated with
- **Boolean question answering** (behavioral indicator), 1 paper
  > "we use a function q(.) that converts a given text t into a question format, which enables the model to assess the visual-textual alignment in a consistent manner. Specifically, q(.) generates a yes/no question"
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)
