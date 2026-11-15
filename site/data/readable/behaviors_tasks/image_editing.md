# Image editing
**Type:** Behavioral indicator  
**Supporting papers:** 20  
**Also known as:** Object creation, Object removal, Instruction-based image compositing, Identity-preserved inpainting, Identity transfer, Object replacement, Background replacement, Color alteration, Style alteration, Drag-based editing, Content dragging, Object moving, Instruction-based image editing  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats image editing as modifying an existing image in response to a natural-language instruction. Definitions largely agree on instruction-guided changes such as replacing, hiding, recoloring, adding, removing, or otherwise changing elements, and one paper also frames it as changing attributes or adding accessories; a smaller line explicitly describes instruction-based editing as following a natural-language command without regional masks or elaborate descriptions. Some papers narrow the task further with extra success conditions, such as plausibly filling the background after removing an object, preserving an object's visual identity while changing pose or view, or inserting a reference object into a background at a specified location and spatial relation.

**Variants.** Papers study several recurring variants, especially object removal, object replacement, background replacement, style alteration, and drag-based editing. Other papers introduce single-paper variants such as object creation, color alteration, content dragging, object moving, and reference-object editing setups that include compositing, identity-preserved inpainting, and identity transfer. These formulations differ in whether the edit is driven only by text or also by masks, drag points, or reference objects.

**Space of elicitation and scores.** Papers link image editing to 2 measurement instruments. The more common one is MagicBrush, used in several evaluations of image editing capability and described in one paper as challenging models with an editing query that demands "a series of complex edits to an image"; the other is an LLM-as-a-judge setup in which GPT-4V is asked whether the edited image contains the target object. Together, these instruments cover both dataset-based evaluation and judge-based scoring of whether the requested edit appears in the output.

**What it is taken as evidence of.** Papers do not converge on a single construct linked to image editing. The literature connects it to 3 constructs in different ways: one paper reports that generalization is related to image editing, while separate papers claim causal relationships from in-context learning to image editing and from interpretability and explainability to image editing. The causal claims are stated in task terms, with one paper saying editing can be performed successfully from examples rather than explicit instructions, and another saying that human-interpretable prompts make it easier for users to modify an image in the desired direction by making slight prompt edits.

## Sources

**Image editing** (4 papers: [GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf), [Kosmos-G: Generating Images in Context with Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b2fe1ee8d936ac08dd26f2ff58986c8f-Paper-Conference.pdf), [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf), [Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/12678c3948153f4bc391f51e2082bd6e-Paper-Conference.pdf))
> Modifying an image according to a natural-language instruction, such as replacing, hiding, or recoloring an object.

**Object creation** (1 paper: [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf))
> The task of adding a new object to an image based on a textual instruction.

**Object removal** (1 paper: [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf))
> The task of removing a specified object from an image and plausibly filling the background, guided by a textual instruction.

**Instruction-based image compositing** (1 paper: [$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf))
> The task of generating a composite image by integrating a reference object into a background image according to a natural language instruction that specifies the object's location and spatial relationship.

**Identity-preserved inpainting** (1 paper: [$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf))
> The task of modifying the pose or view of an object within an image while preserving its unique visual identity, often guided by a user-provided mask.

**Identity transfer** (1 paper: [$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf))
> The task of applying the visual identity of a reference object to a different target object already present in a background scene.

**Object replacement** (1 paper: [$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf))
> The task of substituting an existing object in a background image with a new reference object.

**Background replacement** (1 paper: [I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf))
> Changing the background of an image to match a target background described in the instruction.

**Color alteration** (1 paper: [I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf))
> The observable task of modifying the color of a specified object in an image based on a text instruction.

**Style alteration** (1 paper: [I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf))
> The observable task of changing the artistic or visual style of an entire image based on a text instruction.

**Drag-based editing** (1 paper: [Localize, Understand, Collaborate: Semantic-Aware Dragging via Intention Reasoner](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dd7c683eddc14f8cabcd6ce8d48cd41-Paper-Conference.pdf))
> Editing an image by moving specified handle points toward target points within an editable region.

**Content dragging** (1 paper: [Localize, Understand, Collaborate: Semantic-Aware Dragging via Intention Reasoner](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dd7c683eddc14f8cabcd6ce8d48cd41-Paper-Conference.pdf))
> The task of moving or deforming the content within a specified region of an image according to drag points.

**Object moving** (1 paper: [Localize, Understand, Collaborate: Semantic-Aware Dragging via Intention Reasoner](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dd7c683eddc14f8cabcd6ce8d48cd41-Paper-Conference.pdf))
> The task of relocating an entire object from a source position to a target position within an image.

**Instruction-based image editing** (1 paper: [Guiding Instruction-based Image Editing via Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f0e91b1314fa5eabf1d7ef6d1561ecec-Paper-Conference.pdf))
> The task of modifying an input image according to a natural language command that specifies the desired change, without requiring regional masks or elaborate descriptions.

## Relationships

### Image editing →
- **MagicBrush** (measurement instrument): *measured_by*, 3 papers
  > We use the MagicBrush dataset [129], which challenges models with an editing query that demands a series of complex edits to an image.
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
  - [Towards Semantic Equivalence of Tokenization in Multimodal LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/e95eb5206c867be843fbc14bbfe8c10e-Paper-Conference.pdf)
  - [Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > To evaluate this dimension, we inquire whether GPT-4V identifies the presence of the target object in the image. (Sec. 3.1.1)
  - [I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf)

### → Image editing
- **Interpretability and explainability** (construct): *causes*, 1 paper
  > When a prompt closely aligns with the image content and is interpretable by humans, it becomes easier for users to modify the image in the desired direction by making slight edits to the prompt. (Section 4.3)
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **In-context learning** (construct): *causes*, 1 paper
  > Notably, Orthus exhibits in-context learning capacity by performing image editing successfully when provided with examples rather than explicit instructions, which is not included in the training dataset. (Figure 3)
  - [Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kou25a/kou25a.pdf)

### Associated with
- **Generalization** (construct), 1 paper
  > To further demonstrate the generalization and applicability of ELM, we evaluate its ability to generate samples from novel classes and perform image editing tasks, with the results in Appendix A.2. (Section 4.4)
  - [Elucidating the design space of language models for image generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25w/liu25w.pdf)
