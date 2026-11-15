# Medical report generation
**Type:** Behavioral indicator  
**Supporting papers:** 7  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage is a generation task in which a model produces a detailed, structured or descriptive clinical report from a provided medical image or scan. Most papers define the report by its account of findings in the image, while one paper broadens the inputs to imaging data or contextual inputs and spells out the report content as findings, location, severity, and comparisons.

**Variants.** The naming is mostly report generation or medical report generation, with one paper phrasing the outputs specifically as radiology reports. Papers usually study image-based settings, and some work narrows further to English chest X-ray report generation on MIMIC-CXR and IU-Xray.

**Space of elicitation and scores.** It is measured by 2 instruments, IU-Xray and MIMIC-CXR. Papers use both as report generation datasets, and some descriptions call them chest X-ray datasets; no other instrument is linked.

**What it is taken as evidence of.** Only 1 construct is linked, Versatility. That link is stated as related: one paper says that performance on report generation, together with visual question answering and medical image classification, showcases versatility, and no other construct link is present.

## Sources

**Medical report generation** (5 papers: [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf), [ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment](https://aclanthology.org/2025.emnlp-main.598.pdf), [Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://aclanthology.org/2025.acl-long.460.pdf), [HealthGPT: A Medical Large Vision-Language Model for Unifying Comprehension and Generation via Heterogeneous Knowledge Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25n/lin25n.pdf), [MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25v/zhu25v.pdf))
> The task of generating a detailed, structured textual report describing the findings in a provided medical scan.

## Relationships

### Medical report generation →
- **MIMIC-CXR** (measurement instrument): *measured_by*, 5 papers
  > We utilize five medical vision-language datasets for medical VQA and report generation tasks, i.e., MIMIC-CXR (Johnson et al., 2019), IU-Xray (Demner-Fushman et al., 2016), Harvard-FairVLMed (Luo et al., 2024), PMC-OA (Lin et al., 2023a) (we only select the pathology part) and Quilt-1M (Ikezogwo et al., 2024).
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
  - [Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://aclanthology.org/2025.acl-long.460.pdf)
  - [MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25v/zhu25v.pdf)
  - [Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](https://aclanthology.org/2025.emnlp-main.939.pdf)
- **IU-Xray** (measurement instrument): *measured_by*, 5 papers
  > We utilize five medical vision-language datasets for medical VQA and report generation tasks, i.e., MIMIC-CXR (Johnson et al., 2019), IU-Xray (Demner-Fushman et al., 2016), Harvard-FairVLMed (Luo et al., 2024), PMC-OA (Lin et al., 2023a) (we only select the pathology part) and Quilt-1M (Ikezogwo et al., 2024).
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
  - [Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://aclanthology.org/2025.acl-long.460.pdf)
  - [MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25v/zhu25v.pdf)
  - [Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](https://aclanthology.org/2025.emnlp-main.939.pdf)

### Associated with
- **Versatility** (construct), 1 paper
  > Our MedRegA not only enables three region-centric tasks, but also achieves the best performance for visual question answering, report generation and medical image classification over 8 modalities, showcasing significant versatility. (Abstract)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
