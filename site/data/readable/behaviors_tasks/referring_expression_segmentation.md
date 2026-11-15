# Referring expression segmentation
**Type:** Behavioral indicator  
**Supporting papers:** 16  
**Also known as:** Referring segmentation, Referring image segmentation, Referring object part segmentation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is a pixel-level task where a model receives a natural language description or referring expression and must output a segmentation mask for the specific object, object instance, or region it names. Most definitions are consistent on the success criterion: the output is a mask that covers the described target, as one paper phrases it, "segment a target object mask from the entire image given a sentence describing the object" (Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation). A smaller formulation instead describes a pre-training task on 3D objects, predicting a binary mask for a named component given a referring expression and an object point cloud.

**Variants.** Papers use several near-equivalent names, most commonly referring expression segmentation, and also referring segmentation and referring image segmentation. The common setting is 2D images, but some work studies remote sensing images, including prompts such as "Could you provide a segmentation mask for {referring expression} in this image?" and decoding a <SEG> token into the mask (GeoPixel: Pixel Grounding Large Multimodal Model in Remote Sensing). A narrower variant is referring object part segmentation, which targets components of 3D objects rather than whole image regions, and one paper also relates the task to referring expression generation as its dual.

**Space of elicitation and scores.** Papers link this behavior to 4 measurement instruments in total. The prevailing instruments are dataset and benchmark resources, especially RefCOCO, RefCOCO+, and RefCOCOg, which are often grouped as the refCOCO series for assessing referring segmentation performance; one paper additionally reports evaluating RefCOCO with cIoU. A further linked instrument is gRefCOCO, but papers relate it to the task rather than recording it as a direct measured_by instrument.

**What it is taken as evidence of.** The recorded construct links do not present a single agreed construct that this behavior evidences. Instead, papers relate it to 3 constructs: multimodal alignment, visual grounding, and visual recognition. The emphasis differs across papers, with one discussing the task in terms of learning visual-linguistic alignment, another placing it among visual grounding tasks, and another presenting referring segmentation ability as part of broader recognition abilities.

## Sources

**Referring expression segmentation** (2 papers: [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf), [GeoPixel: Pixel Grounding Large Multimodal Model in Remote Sensing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shabbir25a/shabbir25a.pdf))
> The task of segmenting the specific object or region in an image that is described by a given natural language expression.

**Referring segmentation** (1 paper: [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf))
> The task of segmenting an object in an image based on a natural language description.

**Referring image segmentation** (1 paper: [Visual-O1: Understanding Ambiguous Instructions via Multi-modal Multi-turn Chain-of-thoughts Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3769fddee1b20552d2490c4ff18b136-Paper-Conference.pdf))
> The task of segmenting a specific object or region in an image based on a natural language description.

**Referring object part segmentation** (1 paper: [3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds](https://proceedings.iclr.cc/paper_files/paper/2025/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf))
> The pre-training task of predicting a binary mask for a specific component of a 3D object, given a referring expression that names the component.

## Relationships

### Referring expression segmentation →
- **RefCOCO** (measurement instrument): *measured_by*, 5 papers
  > Table 2 presents the results of referring image segmentation on three datasets: RefCOCO [40], RefCOCO+ [123] and RefCOCOg [68].
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
  - [MMR: A Large-scale Benchmark Dataset for Multi-target and Multi-granularity Reasoning Segmentation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8661ab3440964c27794607f0ea73624-Paper-Conference.pdf)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
  - [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)
- **RefCOCO+** (measurement instrument): *measured_by*, 4 papers
  > Table 2 presents the results of referring image segmentation on three datasets: RefCOCO [40], RefCOCO+ [123] and RefCOCOg [68].
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
  - [Towards Semantic Equivalence of Tokenization in Multimodal LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/e95eb5206c867be843fbc14bbfe8c10e-Paper-Conference.pdf)
  - [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)
- **RefCOCOg** (measurement instrument): *measured_by*, 4 papers
  > Table 2 presents the results of referring image segmentation on three datasets: RefCOCO [40], RefCOCO+ [123] and RefCOCOg [68].
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
  - [Towards Semantic Equivalence of Tokenization in Multimodal LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/e95eb5206c867be843fbc14bbfe8c10e-Paper-Conference.pdf)
  - [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)

### Associated with
- **Referring expression generation** (behavioral indicator), 1 paper
  > To eliminate unsuitable candidate outputs, we leverage the dual task of REG: Referring expression segmentation (RES) [37, 48], which aims to segment a target object mask from the entire image given a sentence describing the object. (Section 1)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
- **Multimodal alignment** (construct), 1 paper
  > Despite remarkable progress, most existing RIS works [7, 58, 27, 26, 21, 5] rely heavily on pixel-level ground-truth masks to learn visual-linguistic alignment. (Section 1)
  - [Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf)
- **Visual recognition** (construct), 1 paper
  > In addition to detection, Octopus is potential to acquire a broader range of recognition abilities, taking advantage of the versatility of the DETR mechanism. Hereby, we endow Octopus with the referring segmentation ability by modifying its object queries into “mask” queries... (Appendix B)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Visual grounding** (construct), 1 paper
  > flexible switching between referring expression segmentation, open-vocabulary segmentation, and other visual grounding tasks. (Section 1)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
- **gRefCOCO** (measurement instrument), 1 paper
  > “we construct a generalized referring expression segmentation dataset with 419k samples using the train split of grefCOCO (Liu et al., 2023a).”
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
