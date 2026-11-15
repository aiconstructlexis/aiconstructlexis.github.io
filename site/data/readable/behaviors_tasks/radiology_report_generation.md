# Radiology report generation
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Report generation  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is generating a descriptive, clinically relevant textual radiology report from a radiology image, often a chest X-ray. Definitions usually describe the report as detailing clinical observations or findings from the image, and one paper makes the expected output structure explicit by requiring "Findings" and "Impression" sections. A smaller variation broadens the input from a single medical image to one or more radiology images plus associated clinical context.

**Variants.** Most task instances focus on chest X-ray report generation. Papers vary the formulation by using a given radiology image or medical image, by allowing associated clinical context in addition to the image, and in one case by studying retrieval-based radiology report generation given only radiology images. Another naming variant is simply "report generation," where the task is framed as producing the "Findings" and "Impression" sections of a typical report.

**Space of elicitation and scores.** Papers link this behavior to two measurement instruments, MIMIC-CXR and GREEN. Radiology report generation is measured by MIMIC-CXR as a dataset for chest X-ray report generation, including use on a subset of the dataset, and by GREEN as a radiology report evaluation metric based on a single-answer reference-guided LLM-as-a-Judge mechanism.

**What it is taken as evidence of.** Only one construct is linked in the papers. The only linked construct is Factuality, and one paper treats Factuality as related to radiology report generation, noting that minute textual differences can drastically invert radiology report meaning and downstream prescribed treatments. Papers do not present additional construct links.

## Sources

**Radiology report generation** (3 papers: [RADAR: Enhancing Radiology Report Generation with Supplementary Knowledge Injection](https://aclanthology.org/2025.acl-long.1279.pdf), [Conformal Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf), [Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation](https://aclanthology.org/2025.naacl-long.28.pdf))
> The task of generating a descriptive, clinically relevant text report based on one or more radiology images and associated clinical context.

**Report generation** (1 paper: [VividMed: Vision Language Model with Versatile Visual Grounding for Medicine](https://aclanthology.org/2025.naacl-long.89.pdf))
> The task of generating a textual radiology report, typically including 'Findings' and 'Impression' sections, based on a medical image.

## Relationships

### Radiology report generation →
- **MIMIC-CXR** (measurement instrument): *measured_by*, 2 papers
  > In this section, we apply Conformal Alignment to chest X-ray report (CXR) generation. Following the pipeline in Figure 1, we apply our method to (a subset of) the MIMIC-CXR dataset [20]. (Section 5)
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
  - [Conformal Generative Modeling with Improved Sample Efficiency through Sequential Greedy Filtering](https://proceedings.iclr.cc/paper_files/paper/2025/file/c2a96d676ac2716615bf1ab7edd3f3d3-Paper-Conference.pdf)
- **GREEN** (measurement instrument): *measured_by*, 1 paper
  > GREEN is a state-of-the-art metric for radiology report evaluation, based on a single-answer reference-guided LLM-as-a-Judge mechanism. (Section 3.2)
  - [CheXalign: Preference fine-tuning in chest X-ray interpretation models without human feedback](https://aclanthology.org/2025.acl-long.1342.pdf)

### Associated with
- **Factuality** (construct), 1 paper
  > Factual correctness is especially critical in chest radiology domains, as minute textual differences can drastically invert radiology report meaning and downstream prescribed treatments
  - [Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation](https://aclanthology.org/2025.naacl-long.28.pdf)
