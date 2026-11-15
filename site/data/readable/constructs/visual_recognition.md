# Visual recognition
**Type:** Construct  
**Supporting papers:** 11  
**Also known as:** Novel concept recognition, Object existence determination  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing framing treats visual recognition as a model ability to identify visual content in an image, usually objects, text, landmarks, and other elements, and sometimes to describe their relationships. One paper explicitly frames it as a latent ability that comes before solving a task, while another describes visual recognition prompts as those requiring simple descriptions of visual elements. A smaller line of work narrows the scope to novel concept recognition, meaning identifying and understanding concepts not seen in pre-training, or to object existence determination, meaning correctly judging whether a specified object is present or absent.

**Space of facets.** Papers organize the construct as a recognition-side capability rather than an understanding-side one: one paper presents multi-modal models as having visual recognition, for example grounding, alongside visual understanding. Within that framing, object detection and referring expression segmentation are treated as related recognition abilities. The term also appears as a prompt category, where visual recognition prompts are those that require simple descriptions of visual elements, and another paper contrasts recognition with visual perception, which it says goes further by interpreting and contextualizing those elements.

**Space of measurement.** Papers link visual recognition to two measurement instruments, both benchmarks: AMBER and FGVC. Operationalizations in the quoted passages are concrete recognition tasks, including visual recognition accuracy for recognizing four cards from an input image, recognizing different landmarks from visual observation, and prompts that require simple descriptions of visual elements; papers also link it to two behavioral indicators, object detection and referring expression segmentation. These measures mostly align with the broad definitions because they test identifying visual elements, but the concrete tasks narrow that broad idea to settings such as fine-grained classification, landmark identification, and short descriptive prompts.

**Links.** Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding claims a causal relationship from visual recognition to visual understanding, stating that recognition can benefit understanding tasks because recognition results are compositions for understanding. The same paper relates visual recognition to visual grounding, object detection, and referring expression segmentation, and Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs relates it to visual perception, described there as going beyond basic recognition by interpreting and contextualizing visual elements within a broader scene.

## Sources

**Visual recognition** (3 papers: [WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf), [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chu25c/chu25c.pdf), [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf))
> The general ability to identify and classify objects, text, and other elements within an image.

**Novel concept recognition** (1 paper: [Contrastive Visual Data Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25h/zhou25h.pdf))
> The ability of a model to correctly identify and understand visual concepts it has not encountered during its pre-training.

**Object existence determination** (1 paper: [Evaluating and Mitigating Object Hallucination in Large Vision-Language Models: Can They Still See Removed Objects?](https://aclanthology.org/2025.naacl-long.349.pdf))
> The model's latent capability to correctly identify whether a specified object is present or absent in a given image.

## Relationships

### Visual recognition →
- **Visual understanding** (construct): *causes*, 1 paper
  > visual recognition is potential to benefit all understanding tasks as recognition results are important compositions for understanding. (Section 1)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **AMBER** (measurement instrument): *measured_by*, 1 paper
  > The models are tested across seven benchmarks: AMBER (visual recognition)... (Section 3)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **FGVC** (measurement instrument): *measured_by*, 1 paper
  > We evaluate WeGeFT on the VTAB-1k benchmark (Zhai et al., 2019) and the fine-grained visual classification (FGVC) benchmark...
  - [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf)

### Associated with
- **Visual grounding** (construct), 1 paper
  > A mainstream of Multi-modal Large Language Models (MLLMs) have two essential functions, i.e., visual recognition (e.g., grounding) and understanding (e.g., visual question answering). (Abstract)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Object detection** (behavioral indicator), 1 paper
  > Prior MLLMs [1, 2, 21] solve traditional visual recognition tasks (e.g., object detection, instance segmentation) in a sequential generation paradigm. (Section 3.1)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Referring expression segmentation** (behavioral indicator), 1 paper
  > In addition to detection, Octopus is potential to acquire a broader range of recognition abilities, taking advantage of the versatility of the DETR mechanism. Hereby, we endow Octopus with the referring segmentation ability by modifying its object queries into “mask” queries... (Appendix B)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Visual perception** (construct), 1 paper
  > Visual Perception (VP) extends beyond VR by interpreting and contextualizing these elements within the broader scene (Fu et al., 2024), essential for tasks requiring more than basic recognition. (Section 3)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
