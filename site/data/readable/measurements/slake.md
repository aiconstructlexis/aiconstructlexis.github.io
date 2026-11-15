# SLAKE
**Type:** Measurement instrument  
**Supporting papers:** 13  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats SLAKE as a medical visual question answering benchmark or dataset built from image and question-answer pairs. Several definitions further describe it as semantically labeled and knowledge-enhanced, and some add radiology images, physician annotation, region-level annotations of organs and diseases, or multiple imaging modalities such as CT and MRI across different pathologies and modalities. A smaller set of descriptions specifies versions and question formats: some papers describe English and Chinese versions, one evaluation keeps only the English portion with 641 images and 7,033 question-answer pairs, and others note open and closed questions or Yes/No and single-word answers.

**What it is claimed to measure.** In these papers, SLAKE is linked to 2 behavioral indicators and no constructs. The prevailing claim is that it measures Medical visual question answering, and a smaller but closely aligned usage treats it as measuring Visual question answering; overall, the reported links stay within VQA rather than spreading across other outcomes.

**Space of uses.** Papers most often position SLAKE as one benchmark within a bundle of medical VQA evaluations rather than as a standalone protocol. It is frequently used alongside VQA-RAD, and often with PathVQA, PMC-VQA, IU-Xray, or OmniMedVQA; some papers benchmark models on SLAKE to assess efficacy or report zero-shot performance on it. No measurement instrument is linked to it.

## Sources

**SLAKE** (8 papers: [MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf), [Guiding Medical Vision-Language Models with Diverse Visual Prompts: Framework Design and Comprehensive Exploration of Prompt Variations](https://aclanthology.org/2025.naacl-long.587.pdf), [VividMed: Vision Language Model with Versatile Visual Grounding for Medicine](https://aclanthology.org/2025.naacl-long.89.pdf), [Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://aclanthology.org/2025.acl-long.460.pdf), [HealthGPT: A Medical Large Vision-Language Model for Unifying Comprehension and Generation via Heterogeneous Knowledge Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25n/lin25n.pdf), [Biomedical Visual Instruction Tuning with Clinician Preference Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec33ab89b5986605cd7c331396e7e5c-Paper-Datasets_and_Benchmarks_Track.pdf), [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf), [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf))
> A benchmark dataset for Visual Question Answering (VQA) in the medical domain, containing questions and answers for images across various pathologies and modalities.

## Relationships

### → SLAKE
- **Medical visual question answering** (behavioral indicator): *measured_by*, 7 papers
  > This experiment is conducted on popular medical VQA benchmarks VQA-RAD and SLAKE. (Section 4.5)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
  - [MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)
  - [Guiding Medical Vision-Language Models with Diverse Visual Prompts: Framework Design and Comprehensive Exploration of Prompt Variations](https://aclanthology.org/2025.naacl-long.587.pdf)
  - [Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://aclanthology.org/2025.acl-long.460.pdf)
  - [HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models](https://aclanthology.org/2025.acl-long.679.pdf)
  - [MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25v/zhu25v.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > We adopt three widely used VQA datasets for evaluation: ... (ii) SLAKE (Liu et al., 2021): A bilingual (English and Chinese) medical VQA dataset. (Section 4.2)
  - [VividMed: Vision Language Model with Versatile Visual Grounding for Medicine](https://aclanthology.org/2025.naacl-long.89.pdf)
