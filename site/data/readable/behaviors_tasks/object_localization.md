# Object localization
**Type:** Behavioral indicator  
**Supporting papers:** 20  
**Also known as:** Building localization, Defect localization, Instance localization, Text localization, Positioning, Bounding box prediction, Element identification, GUI element localization  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats object localization as finding where one or more objects are and returning a spatial output, most often a bounding box. Several definitions make the output explicit as box coordinates, and one video-oriented account describes the box as a 4-tuple of upper-left and lower-right corners. Smaller variants ask for approximate coordinates, the exact location of a defect, or permit masks alongside boxes, and some settings restrict the task to a single object while others target multiple objects or a referred region named in text.

**Variants.** Papers use nearby labels such as bounding box prediction, building localization, instance localization, defect localization, and text localization. The settings range from still images to video frames, and from generic scenes to earth-observation images, reference-image-based instance finding, and GUI tasks that ask the model to locate a piece of text or select the queried element. A smaller related line links object localization to reasoning segmentation, noting that that setup only allows single-object localization.

**Space of elicitation and scores.** Papers link object localization to 2 measurement instruments, MM-ID and RefCOCO. MM-ID is described as evaluating competency across four progressively complex levels, including location, while RefCOCO is cited among benchmarks involving spatial understanding and fine-grained features.

**What it is taken as evidence of.** Papers relate object localization to 2 constructs rather than to a single recurring construct. One line of work relates it to spatial reasoning, saying that spatial object localization helps models learn spatial reasoning, while another relates it to visual grounding through a grounding module that predicts bounding box annotations for precise visual focus.

## Sources

**Object localization** (6 papers: [GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf), [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf), [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf), [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf), [Multimodal Language Models See Better When They Look Shallower](https://aclanthology.org/2025.emnlp-main.339.pdf), [MLLM-Bench: Evaluating Multimodal LLMs with Per-sample Criteria](https://aclanthology.org/2025.naacl-long.256.pdf))
> The task of identifying the position of one or more objects within an image, typically by outputting bounding boxes.

**Building localization** (1 paper: [TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac3af725ae398b6184faae0828bdbd6c-Paper-Conference.pdf))
> Predicting bounding boxes for buildings visible in an earth-observation image region.

**Bounding box prediction** (2 papers: [Feast Your Eyes: Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf), [Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf))
> Producing coordinate boxes that localize a referred region in an image.

**Defect localization** (1 paper: [MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d91ffbe9c126765755ff52d36b715683-Paper-Conference.pdf))
> The observable task of identifying the spatial position of a defect within an image, typically expressed through textual description.

**Instance localization** (1 paper: [IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/82dcb6da1b408d59d15f68afdebf1489-Paper-Conference.pdf))
> The observable task of identifying and providing the bounding box coordinates for a specific instance within a test image, based on a provided reference image of that instance.

**Text localization** (1 paper: [Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf))
> The task of finding the location (i.e., bounding box) of a piece of text specified in a query.

**Positioning** (1 paper: [Multimodal Language Models See Better When They Look Shallower](https://aclanthology.org/2025.emnlp-main.339.pdf))
> The observable task of determining the spatial location or arrangement of objects in an image.

**Element identification** (1 paper: [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf))
> The action of correctly selecting or pointing to a specific GUI element based on a textual description or query.

## Relationships

### Object localization →
- **RefCOCO** (measurement instrument): *measured_by*, 1 paper
  > Benchmarks that involve spatial understanding and fine-grained features include object localization (RefCOCO, OCID-Ref; Kazemzadeh et al. 2014; Wang et al. 2021)... (Section 5)
  - [Locality Alignment Improves Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce6326ac4794bb04d5eb16f597446baf-Paper-Conference.pdf)
- **MM-ID** (measurement instrument): *measured_by*, 1 paper
  > "MM-ID dissects LVLMs’ competency across four progressively complex levels: matching, location, question-answering, and captioning."
  - [IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/82dcb6da1b408d59d15f68afdebf1489-Paper-Conference.pdf)

### Associated with
- **Reasoning segmentation** (behavioral indicator), 1 paper
  > RS has reasoning ability, but only allows single object localization. (Figure 2)
  - [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf)
- **Visual grounding** (construct), 1 paper
  > a grounding module (Gaze) provides precise visual focus by predicting bounding box annotations. (Section 1)
  - [Taking Notes Brings Focus? Towards Multi-Turn Multimodal Dialogue Learning](https://aclanthology.org/2025.emnlp-main.1690.pdf)
- **Spatial reasoning** (construct), 1 paper
  > spatial object localization (2,361 samples), which helps models learn spatial reasoning (Section 3)
  - [SilVar: Speech-Driven Multimodal Model for Reasoning Visual Question Answering and Object Localization](https://aclanthology.org/2025.emnlp-main.589.pdf)
