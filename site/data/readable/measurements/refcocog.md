# RefCOCOg
**Type:** Measurement instrument  
**Supporting papers:** 30  
**Also known as:** refCOCOg  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats RefCOCOg as a benchmark or dataset for referring expression comprehension, visual grounding, and object localization from natural language descriptions. Definitions repeatedly emphasize longer or more descriptive referring expressions, sometimes with spatial relations, and some papers specify grounding a described region to a single bounding box. A smaller line of work describes refCOCOg as a version of the refCOCO series for referring expression segmentation, with natural language queries paired with object masks, while some papers also use it for referring expression generation and region-level captioning.

**What it is claimed to measure.** Papers link RefCOCOg to 1 construct and 4 behavioral indicators. The most common reported use is to measure Referring expression understanding, followed by Referring expression segmentation, Region captioning, and Referring expression generation, and it is also reported as measuring the construct Visual grounding. Overall, papers use it across several task framings rather than centering it on only one reported target.

**Space of uses.** Papers most commonly use RefCOCOg alongside RefCOCO and RefCOCO+, often presenting the three as standard, well-established, or renowned benchmarks. Some papers pair it with Visual Genome for region captioning, and some segmentation work uses it with refCLEF or Reaseg, including one description that constructs training data by combining the train split of refCOCOg with other referring segmentation datasets. One paper also reports evaluating zero-shot and few-shot settings on it.

## Sources

**RefCOCOg** (6 papers: [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf), [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf), [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf), [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf), [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf), [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf))
> Referring expression comprehension benchmark requiring models to localize an object in an image based on a natural language description, with longer expressions and spatial relations.

**refCOCOg** (3 papers: [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf), [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf), [RSVP: Reasoning Segmentation via Visual Prompting and Multi-modal Chain-of-Thought](https://aclanthology.org/2025.acl-long.715.pdf))
> A version of the refCOCO dataset for referring expression segmentation that contains longer, more descriptive phrases.

## Relationships

### → RefCOCOg
- **Referring expression understanding** (behavioral indicator): *measured_by*, 5 papers
  > RefCOCOg [67] Refer grounding on natural images. (Table A2)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
  - [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
- **Referring expression segmentation** (behavioral indicator): *measured_by*, 4 papers
  > Table 2 presents the results of referring image segmentation on three datasets: RefCOCO [40], RefCOCO+ [123] and RefCOCOg [68].
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
  - [Towards Semantic Equivalence of Tokenization in Multimodal LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/e95eb5206c867be843fbc14bbfe8c10e-Paper-Conference.pdf)
  - [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)
- **Region captioning** (behavioral indicator): *measured_by*, 3 papers
  > To assess the region-level caption ability, we also evaluate ASM on the Visual Genome (Krishna et al., 2017) and RefCOCOg (Mao et al., 2016).
  - [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf)
  - [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf)
  - [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf)
- **Visual grounding** (construct): *measured_by*, 3 papers
  > For visual grounding, we use RefCOCO, RefCCO+ and RefCOCOg [62]. (Section 4.1)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
  - [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
- **Referring expression generation** (behavioral indicator): *measured_by*, 1 paper
  > The RefCOCOg [33] dataset is a classical benchmark for referring expression generation, which contains 85,474 expressions for 54,822 objects in 26,711 images. (Section 4.1)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
