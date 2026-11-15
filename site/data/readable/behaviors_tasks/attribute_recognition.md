# Attribute recognition
**Type:** Behavioral indicator  
**Supporting papers:** 13  
**Also known as:** Attribute identification, Fine-grained object property discernment, Attribute classification, Object attribute detection  

## State of the Field

**Space of definitions.** Most definitions treat it as identifying visual properties of objects in an image, most often color and other descriptive features. Several definitions extend the scope to material, texture, shape, state, length, or position, and one formulation emphasizes fine-grained discernment of subtle properties described in a caption. Some papers operationalize it through generated natural language responses or detailed feature descriptions.

**Variants.** Papers use nearby names such as attribute identification, attribute classification, object attribute detection, and fine-grained object property discernment. The variants span a TDIUC question category, open-ended classification over common adjective concepts like color, material, and length, fine-grained property discernment for open-vocabulary detection, and detailed feature description of animals to support recognition. Color is the most recurrent attribute, with some work isolating an attribute-level color subset, while another line includes position alongside color.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument, MMHal-Bench. It is described as a benchmark for evaluating LVLMs beyond object hallucination, with question types that include object attributes, so it measures attribute recognition as one benchmarked task. No other measurement instrument is explicitly linked to it.

**What it is taken as evidence of.** Papers do not link attribute recognition to any construct. Separately, one paper reports it as related to Hallucination, placing attribute recognition among the tasks covered within hallucination scenarios.

## Sources

**Attribute recognition** (3 papers: [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf), [Task Me Anything](https://proceedings.neurips.cc/paper_files/paper/2024/file/237ffa9a473eff1c66d085dba7f813ba-Paper-Datasets_and_Benchmarks_Track.pdf), [MLLM-Bench: Evaluating Multimodal LLMs with Per-sample Criteria](https://aclanthology.org/2025.naacl-long.256.pdf))
> Identifying visual attributes such as position and color from an image.

**Attribute identification** (1 paper: [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf))
> The task of identifying specific properties or characteristics of objects within an image.

**Fine-grained object property discernment** (1 paper: [Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf))
> The observable ability to distinguish subtle properties of objects, such as their specific color, material, or texture, as described in a caption.

**Attribute classification** (1 paper: [Open-ended VQA benchmarking of Vision-Language models by exploiting Classification datasets and their semantic hierarchy](https://proceedings.iclr.cc/paper_files/paper/2024/file/cb1c4782f159b55380b4584671c4fd88-Paper-Conference.pdf))
> Detecting descriptive properties such as color, material, or length of an object in an image through generated natural language responses.

**Object attribute detection** (1 paper: [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf))
> Identifying the properties or attributes (e.g., color, texture) of objects in an image.

## Relationships

### Attribute recognition →
- **MMHal-Bench** (measurement instrument): *measured_by*, 1 paper
  > "MMHAL-Bench (Sun et al., 2023): This benchmark evaluates LVLMs beyond object hallucination and contains eight question types: object attributes, adversarial objects, comparisons, counting, spatial relations, environment, holistic description, and others."
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
