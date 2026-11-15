# IU-Xray
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across the surveyed work, IU-Xray is most commonly described as a dataset of chest X-ray images paired with associated medical or radiology reports, mainly used for evaluating medical report generation. Definitions largely converge on that image report format, while a smaller line of work broadens the description to a chest X-ray dataset used for both report generation and medical visual question answering.

**What it is claimed to measure.** Papers use IU-Xray to measure 2 behavioral indicators, and the linked claims are concentrated on behavioral indicators rather than constructs. The prevailing usage is Medical report generation: papers describe evaluating models on the report generation task with IU-Xray and refer to it as a report generation dataset. A smaller line of work also uses it to measure Medical visual question answering, including definitions that place IU-Xray among medical VQA datasets; no constructs are linked to it.

**Space of uses.** In practice, papers most often use IU-Xray alongside MIMIC-CXR for report generation evaluation; as one study puts it, "For medical report generation, we use MIMIC-CXR and IU-Xray" (Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning). Some papers also include it in broader multi-dataset evaluation suites for medical VQA, alongside datasets such as SLAKE, VQA-RAD, PathVQA, Harvard-FairVLMed, and other medical datasets, so it appears both in paired report generation setups and in mixed task evaluations.

## Sources

**IU-Xray** (3 papers: [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf), [Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://aclanthology.org/2025.acl-long.460.pdf), [Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](https://aclanthology.org/2025.emnlp-main.939.pdf))
> A dataset of chest X-ray images and associated reports used for evaluating medical report generation.

## Relationships

### → IU-Xray
- **Medical report generation** (behavioral indicator): *measured_by*, 5 papers
  > We utilize five medical vision-language datasets for medical VQA and report generation tasks, i.e., MIMIC-CXR (Johnson et al., 2019), IU-Xray (Demner-Fushman et al., 2016), Harvard-FairVLMed (Luo et al., 2024), PMC-OA (Lin et al., 2023a) (we only select the pathology part) and Quilt-1M (Ikezogwo et al., 2024).
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
  - [Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://aclanthology.org/2025.acl-long.460.pdf)
  - [MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25v/zhu25v.pdf)
  - [Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](https://aclanthology.org/2025.emnlp-main.939.pdf)
- **Medical visual question answering** (behavioral indicator): *measured_by*, 2 papers
  > We utilize five medical vision-language datasets for medical VQA and report generation tasks, i.e., MIMIC-CXR (Johnson et al., 2019), IU-Xray (Demner-Fushman et al., 2016), Harvard-FairVLMed (Luo et al., 2024), PMC-OA (Lin et al., 2023a) (we only select the pathology part) and Quilt-1M (Ikezogwo et al., 2024).
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
  - [Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://aclanthology.org/2025.acl-long.460.pdf)
