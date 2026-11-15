# RefCOCO+
**Type:** Measurement instrument  
**Supporting papers:** 25  
**Also known as:** refCOCO+  

## State of the Field

**What it is.** Across the cited definitions, RefCOCO+ is most commonly described as a benchmark or dataset for referring expression tasks, usually paired with RefCOCO and RefCOCOg. The prevailing description treats it as similar to RefCOCO but with constraints that exclude spatial or location words, shifting descriptions toward appearance-based language; a smaller line of work describes it as an extension used for referring expression segmentation and as featuring more complex language. Papers also variously label it as a referring expression comprehension benchmark, a visual grounding benchmark, or a referring expression segmentation dataset.

**What it is claimed to measure.** Papers use RefCOCO+ to measure two behavioral indicators, Referring expression segmentation and Referring expression understanding, and one construct, Visual grounding. The recurring uses are to assess referring expression understanding or comprehension, referring expression segmentation, and visual grounding, so the measurement claims are spread across these tasks rather than concentrated on only one framing. Relationship evidence describes it as evaluating recognition ability on referring expression comprehension datasets, as assessing referring segmentation with the refCOCO series, and as measuring grounding capability in natural image scenarios.

**Space of uses.** The most common usage positions RefCOCO+ as one of a small set of standard or well-established benchmarks used alongside RefCOCO and RefCOCOg. Several papers present evaluation on this trio for visual grounding, referring expression comprehension or understanding, and referring segmentation; one paper also says it combines the train split of refCLEF, refCOCO, refCOCO+, and refCOCOg to construct a referring segmentation dataset. No other measurement instrument is linked to it through the recorded relationships.

## Sources

**RefCOCO+** (2 papers: [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf), [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf))
> Referring expression comprehension benchmark similar to RefCOCO but excluding spatial relations in annotations, focusing on appearance-based descriptions.

**refCOCO+** (2 papers: [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf), [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf))
> An extension of the refCOCO dataset for referring expression segmentation, featuring more complex language.

## Relationships

### → RefCOCO+
- **Referring expression segmentation** (behavioral indicator): *measured_by*, 4 papers
  > Table 2 presents the results of referring image segmentation on three datasets: RefCOCO [40], RefCOCO+ [123] and RefCOCOg [68].
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
  - [Towards Semantic Equivalence of Tokenization in Multimodal LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/e95eb5206c867be843fbc14bbfe8c10e-Paper-Conference.pdf)
  - [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf)
- **Referring expression understanding** (behavioral indicator): *measured_by*, 4 papers
  > RefCOCO+ [103] Refer grounding on natural images. (Table A2)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
- **Visual grounding** (construct): *measured_by*, 3 papers
  > For visual grounding, we use RefCOCO, RefCCO+ and RefCOCOg [62]. (Section 4.1)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
  - [CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf)
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
