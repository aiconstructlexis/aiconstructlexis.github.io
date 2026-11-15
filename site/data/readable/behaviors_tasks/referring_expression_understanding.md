# Referring expression understanding
**Type:** Behavioral indicator  
**Supporting papers:** 31  
**Also known as:** Referring expression comprehension, Multi-object referring segmentation, Multi-target segmentation, Video grounding, Object grounding, Spatio-temporal object grounding, Phrase grounding, Referring expression grounding, Referential expression grounding  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is an image grounding task: the model must locate the object or region referred to by a natural language expression, usually by outputting a bounding box. Some authors describe the same behavior more broadly as linking text to the corresponding object or region, while a smaller line formulates it through segmentation, first generating a mask and then deriving the box. Where scoring is stated, predictions are compared with ground-truth boxes as accuracy or Acc@0.5, and one paper notes that a prediction is correct only if the IoU with the ground-truth box exceeds 0.5 (Text4Seg: Reimagining Image Segmentation as Text Generation).

**Variants.** Papers use several nearby labels and settings for this behavior. Most variants stay in images, under referring expression comprehension or phrase grounding, and some broaden the task to predicting boxes for one or more phrases or noun phrases within a caption; some versions also ask for multiple referred targets through multi-target segmentation. Other work extends the same localization behavior to object grounding in 3D scenes and to video grounding, including spatio-temporal outputs such as frame, x, y tuples or start and end frames with spatial coordinates.

**Space of elicitation and scores.** Seven measurement instruments are linked to this behavior in papers. Most often it is measured by RefCOCO, RefCOCOg, and RefCOCO+, with additional use of Flickr30k Entities and Talk2Car; two other linked instruments appear less often, including one that appears in a reported correlation rather than as a direct benchmark. Reported scores are typically given as accuracy or Acc@0.5 against reference boxes.

**What it is taken as evidence of.** Five constructs are linked to this behavior, and papers use several framings rather than a single one. The most common links treat it as related to visual grounding and to localization ability, and some papers also describe it as related to spatial reasoning and semantic reasoning when the task involves complex textual queries. Separately, a paper claims a causal relationship from referring expression understanding to scene understanding.

## Sources

**Referring expression comprehension** (3 papers: [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf), [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf), [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf))
> Identifying the referred object by generating a mask and deriving a bounding box that matches the language query.

**Multi-object referring segmentation** (1 paper: [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf))
> The observable task of generating instance segmentation masks for multiple referred objects in an image.

**Multi-target segmentation** (1 paper: [MMR: A Large-scale Benchmark Dataset for Multi-target and Multi-granularity Reasoning Segmentation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8661ab3440964c27794607f0ea73624-Paper-Conference.pdf))
> The observable behavior of simultaneously generating distinct segmentation masks for multiple target entities within a single image based on one instruction.

**Video grounding** (1 paper: [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf))
> The task of localizing a target object described by text within a video sequence of a 3D scene.

**Object grounding** (2 papers: [Multi-modal Situated Reasoning in 3D Scenes](https://proceedings.neurips.cc/paper_files/paper/2024/file/feaeec8ec2d3cb131fe18517ff14ec1f-Paper-Datasets_and_Benchmarks_Track.pdf), [ModalPrompt: Towards Efficient Multimodal Continual Instruction Tuning with Dual-Modality Guided Prompt](https://aclanthology.org/2025.emnlp-main.609.pdf))
> The task of localizing a specific 3D object in a scene based on a natural language description.

**Spatio-temporal object grounding** (1 paper: [TUMTraf VideoQA: Dataset and Benchmark for Unified Spatio-Temporal Video Understanding in Traffic Scenes](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25g/zhou25g.pdf))
> Predicting the precise spatio-temporal coordinates (frame, x, y) of a referred object in a video as a tuple output.

**Phrase grounding** (2 papers: [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf), [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf))
> The task of associating specific phrases or words in a text description with their corresponding regions or objects in an image.

**Referring expression grounding** (1 paper: [Follow the Flow: Fine-grained Flowchart Attribution with Neurosymbolic Agents](https://aclanthology.org/2025.emnlp-main.1144.pdf))
> The task of linking a textual description (referring expression) to the corresponding object or region in an image.

**Referential expression grounding** (1 paper: [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf))
> Locating the object in an image that corresponds to a given textual description.

## Relationships

### Referring expression understanding →
- **RefCOCO** (measurement instrument): *measured_by*, 7 papers
  > Initially, we demonstrate our models’ effectiveness in learning neural modules on two established benchmarks: GQA (Hudson & Manning, 2019), focusing on compositional visual question answering, and RefCOCO (Kazemzadeh et al., 2014), which assesses referring expression comprehension. (Section 4)
  - [GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
  - [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf)
- **RefCOCOg** (measurement instrument): *measured_by*, 5 papers
  > RefCOCOg [67] Refer grounding on natural images. (Table A2)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
  - [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
- **RefCOCO+** (measurement instrument): *measured_by*, 4 papers
  > RefCOCO+ [103] Refer grounding on natural images. (Table A2)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
- **Flickr30k Entities** (measurement instrument): *measured_by*, 1 paper
  > We evaluate phrase grounding task on Flickr30k Entities (Plummer et al., 2015) val and test splits. (Sec. 4.1.1).
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Talk2Car** (measurement instrument): *measured_by*, 1 paper
  > We also use the driving, non human-centric, Talk2Car (Deruyttere et al., 2019) REC dataset.
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **RefCOCO/g/+** (measurement instrument): *measured_by*, 1 paper
  > In Table 4, we compare CUBE-LLM to the state-of-the-arts in Referring Expression Comprehension (REC) benchmark on refCOCO/+/g (Yu et al., 2016) dataset. (Section 4.4)
  - [Language-Image Models with 3D Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a829e299ebc1c1615ddb09e98fb6ce8-Paper-Conference.pdf)
- **Scene understanding** (construct): *causes*, 1 paper
  > Object referencing and grounding are essential for advanced scene understanding.
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)

### Associated with
- **Visual grounding** (construct), 2 papers
  > For tasks that focus on visual grounding ability like REC [42], and REG [37], the model uses more DINO features to perceive region-level visual information. (Section 4.1)
  - [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf)
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Spatial reasoning** (construct), 1 paper
  > This work focuses on the challenging open-vocabulary detection task of Referring Expression Comprehension (REC) (Mao et al., 2016), which involves localizing an object in an image based on a complex textual query, requiring both spatial and semantic reasoning.
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **Semantic reasoning** (construct), 1 paper
  > This work focuses on the challenging open-vocabulary detection task of Referring Expression Comprehension (REC) (Mao et al., 2016), which involves localizing an object in an image based on a complex textual query, requiring both spatial and semantic reasoning.
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **Object detection** (behavioral indicator), 1 paper
  > It also differs from object detection (Girshick, 2015), which uses predefined categories instead of natural language expressions.
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **Localization ability** (construct), 1 paper
  > The REC task serves as a critical benchmark to evaluate the localization capabilities of these models. (Section 2)
  - [A Large-Scale Human-Centric Benchmark for Referring Expression Comprehension in the LMM Era](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f0cd0305f7741659304f5325f3bf6d-Paper-Datasets_and_Benchmarks_Track.pdf)
- **HellaSwag** (measurement instrument), 1 paper
  > “Further analysis shows a Pearson correlation of 0.88 between the LLM’s original performance on reasoning benchmarks, measured by the HellaSwag score (Zellers et al., 2019), and REC performance”
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
