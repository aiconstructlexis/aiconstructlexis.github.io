# Object recognition
**Type:** Behavioral indicator  
**Supporting papers:** 28  
**Also known as:** Object presence detection, Object identification, Structure identification, Object existence determination, Object name generation, Entity recognition  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as identifying or naming objects present in an image. Definitions often phrase it as identifying specific objects, identifying and naming objects, or correctly naming an everyday object; some formulations narrow the task to deciding whether a specified object is present or absent, while others extend it to identifying visible people and environmental features, anatomical structures in medical scans, or objects in video frames. Success criteria also vary across papers: some use correct object names, some ask whether an object exists, and some include localization, for example bounding boxes or approximate coordinates.

**Variants.** Papers study several named variants, including object presence detection, object existence determination, object identification, structure identification, object name generation, and entity recognition. The settings range from everyday images and per-sample object questions, to video tasks where the aim is to identify caption-mentioned objects in frames or localize them on keyframes, to biomedical scans for anatomy naming. A smaller strand frames the behavior as open-ended detection, where the model "detects objects and generates their category names in a free-form manner" (Open-Det: An Efficient Learning Framework for Open-Ended Detection).

**Space of elicitation and scores.** Papers link this behavior to 2 measurement instruments, CUB-200-2011 and ImageNet-1k. They are used as benchmark-style resources for object identification or image recognition, with CUB-200-2011 described as focused on bird species and ImageNet-1k as a benchmark for evaluating image recognition models. Other papers elicit it with category questions, caption-conditioned identification, free-form naming, and entity listing; one study scores recognition as the ratio of recognized entities to annotated entities.

**What it is taken as evidence of.** Papers connect this behavior to 2 constructs, Grounding and Visual perception. One paper, Look, Remember and Reason: Grounded Reasoning in Videos with Language Models, claims a causal relationship from object recognition to Grounding, saying the model is grounded by introducing surrogate tasks including object recognition; another reports that object recognition is related to Visual perception, describing perception MLLMs as using skills like object recognition and OCR. The recorded relationships therefore connect it to both Grounding and Visual perception.

## Sources

**Object recognition** (5 papers: [WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf), [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf), [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf), [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf), [MLLM-Bench: Evaluating Multimodal LLMs with Per-sample Criteria](https://aclanthology.org/2025.naacl-long.256.pdf))
> Identifying specific objects present in the image.

**Object presence detection** (1 paper: [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf))
> The task of determining whether a specific object exists within an image.

**Object identification** (2 papers: [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf), [ViLMA: A Zero-Shot Benchmark for Linguistic and Temporal Grounding in Video-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b176e960edbb8afe77f77f9039d2738a-Paper-Conference.pdf))
> The task of correctly naming an everyday object depicted in an image.

**Structure identification** (1 paper: [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf))
> The specific task of identifying and naming anatomical structures, such as organs, within a specified region of a medical scan.

**Object existence determination** (1 paper: [Evaluating and Mitigating Object Hallucination in Large Vision-Language Models: Can They Still See Removed Objects?](https://aclanthology.org/2025.naacl-long.349.pdf))
> The model's latent capability to correctly identify whether a specified object is present or absent in a given image.

**Object name generation** (1 paper: [Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf))
> The model produces free-form textual names for detected objects without relying on a fixed vocabulary.

**Entity recognition** (1 paper: [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.324.pdf))
> Identifying and naming visible objects, people, and environmental features in an image.

## Relationships

### Object recognition →
- **Grounding** (construct): *causes*, 1 paper
  > Our multi-modal LRR model is grounded to relevant low-level visual information in the scene by stochastically introducing low-level surrogate tasks during training, including object recognition, re-identification, and tracking (Section 1).
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **CUB-200-2011** (measurement instrument): *measured_by*, 1 paper
  > Caltech’s CUB Dataset on Birds [82] is a well-known resource for evaluating algorithms on the task of object identification, specifically focused on bird species. (Section 4.3)
  - [Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/27571b74d6cd650b8eb6cf1837953ae8-Paper-Conference.pdf)
- **ImageNet-1k** (measurement instrument): *measured_by*, 1 paper
  > "ImageNet, often considered a cornerstone in the field of computer vision, has been widely used as a benchmark to evaluate the performance of image recognition models."
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Visual perception** (construct), 1 paper
  > Perception MLLMs retrieve information from multimodal inputs, using skills like object recognition and OCR. (Table 3).
  - [MLLM-Bench: Evaluating Multimodal LLMs with Per-sample Criteria](https://aclanthology.org/2025.naacl-long.256.pdf)
