# Multimodal generation
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Multi-modal generation  

## State of the Field

**Space of definitions.** In the papers, the behavior is described as predicting missing modalities from available modal information and their interconnections. The recurring example is generating an image from a text caption, so the task is framed around recovering a missing modality given the others.

**Variants.** The recorded usage includes a broader missing-modality formulation and a narrower node-level setting. In the narrower setting, the goal is to predict missing images based on textual captions, while the broader label multi-modal generation covers cases such as image-from-caption generation.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior. Papers describe it directly as a task of predicting missing modalities, rather than through a separately named benchmark or scoring instrument.

**What it is taken as evidence of.** Only one construct is linked to this behavior, multimodal understanding. That link is not framed as an indicator relation: one paper claims a causal relationship from multimodal understanding to multimodal generation, stating that incorporating multimodal understanding data enhances comprehension of object details such as color and quantity, thereby improving generation capability.

## Sources

**Multi-modal generation** (1 paper: [Graph World Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25p/feng25p.pdf))
> Predicting missing modalities, such as generating an image from a text caption, given available modal information and their interconnections.

## Relationships

### → Multimodal generation
- **Multimodal understanding** (construct): *causes*, 1 paper
  > incorporating multimodal understanding data enhances the model’s comprehension of object details, including attributes such as color and quantity, thereby improving its generation capability. (Section 5.2.2)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
