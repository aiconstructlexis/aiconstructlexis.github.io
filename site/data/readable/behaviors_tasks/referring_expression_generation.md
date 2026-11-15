# Referring expression generation
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Multimodal referring  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage treats referring expression generation as producing a descriptive textual expression for a specified object or bounded region in an image, usually supplied as a bounding box. Papers agree that the output should accurately, and in some formulations unambiguously, refer to that content; a smaller line of work also describes it as the latent ability to understand a visual reference and then generate the description.

**Variants.** A recurring variant names the task multimodal referring, with the same basic setup of understanding image regions or objects that users specify through bounding boxes or location tokens and generating the associated text. Papers also connect it to two other behavioral indicators in nearby grounding settings: referring expression segmentation is described as the dual task of REG, and one paper claims a causal relationship from referring expression generation to Entity grounding by incorporating descriptive textual clues into that task.

**Space of elicitation and scores.** Papers link it to one measurement instrument, RefCOCOg, described as a classical benchmark for referring expression generation. This operationalizes the behavior through image objects or regions paired with referring expressions; no other instrument is linked.

**What it is taken as evidence of.** Among constructs, papers link it to two constructs, Grounding and Visual grounding, rather than using a single uniform construct link. One paper claims a causal relationship from Grounding to referring expression generation, stating that adding grounding data improves referring performance, while another reports that referring expression generation is related to Visual grounding as part of grounding data for interactive visual grounding capabilities.

## Sources

**Referring expression generation** (2 papers: [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf), [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf))
> The task of generating a descriptive textual expression that accurately refers to a specific, bounded region within an image.

**Multimodal referring** (1 paper: [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf))
> The latent ability of a model to understand a visual reference, such as a bounding box, and generate an appropriate textual description for the specified object or region.

## Relationships

### Referring expression generation →
- **RefCOCOg** (measurement instrument): *measured_by*, 1 paper
  > The RefCOCOg [33] dataset is a classical benchmark for referring expression generation, which contains 85,474 expressions for 54,822 objects in 26,711 images. (Section 4.1)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
- **Entity grounding** (behavioral indicator): *causes*, 1 paper
  > we are the first to incorporate referring expression generation into the entity grounding task, enhancing its process by providing descriptive textual clues. (Section 1)
  - [ISR: Self-Refining Referring Expressions for Entity Grounding](https://aclanthology.org/2025.acl-long.1483.pdf)

### → Referring expression generation
- **Grounding** (construct): *causes*, 1 paper
  > “Particularly, when adding grounding data into training, the referring performance gets improved, and vice versa.”
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)

### Associated with
- **Referring expression segmentation** (behavioral indicator), 1 paper
  > To eliminate unsuitable candidate outputs, we leverage the dual task of REG: Referring expression segmentation (RES) [37, 48], which aims to segment a target object mask from the entire image given a sentence describing the object. (Section 1)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
- **Visual grounding** (construct), 1 paper
  > In order to endow our model with consistent, interactive visual grounding capabilities, we collect a high-quality dataset covering 4 types of grounding data: ... (2) Referring Expression Generation (REG)... (Section 2.3)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
