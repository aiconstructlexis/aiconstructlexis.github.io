# Open-vocabulary object detection
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Open-ended object detection, Open-vocabulary detection  

## State of the Field

**Space of definitions.** Across papers, the prevailing framing is detecting and locating objects in images when the category set is not fixed in advance. Definitions differ on the inference setup: some describe categories not seen during training and use textual descriptions or an arbitrary open set of category names provided as text at inference time, while a smaller line of work uses open-ended object detection for discovering unseen objects without any object categories as inputs, with success described as predicting the object categories and locations themselves.

**Variants.** The main variants in naming are open-vocabulary object detection, open-vocabulary detection, and open-ended object detection. All are image-based, but papers distinguish text-conditioned versions, where category names or descriptions are supplied at inference, from a more open-ended version with no predefined categories, and one evaluation is explicitly described as zero-shot.

**Space of elicitation and scores.** Papers link this behavior to two measurement instruments, both datasets: LVIS and Visual Genome. LVIS is used as a zero-shot evaluation dataset, and Visual Genome appears in an open-ended object detection evaluation.

**What it is taken as evidence of.** Papers only link it to one construct, Localization ability, and that connection is framed as related rather than as direct evidence. One paper says that work on improving localization capability focuses on downstream dense vision tasks such as open-vocabulary detection, and no other construct linkage is reported.

## Sources

**Open-vocabulary object detection** (1 paper: [FineCLIP: Self-distilled Region-based CLIP for Better Fine-grained Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/3122aaa22b2fe83f9cead1a696f65ceb-Paper-Conference.pdf))
> Detecting objects in an image belonging to categories not seen during training, using textual descriptions.

**Open-ended object detection** (1 paper: [Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf))
> The task of identifying and locating objects in an image without being provided with a predefined set of object categories during inference.

**Open-vocabulary detection** (1 paper: [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf))
> The task of detecting objects in an image from an arbitrary, open set of category names provided as text at inference time.

## Relationships

### Open-vocabulary object detection →
- **Visual Genome** (measurement instrument): *measured_by*, 1 paper
  > Open-Ended Object Detection on the Visual Genome dataset. (Figure 6)
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)
- **LVIS** (measurement instrument): *measured_by*, 1 paper
  > our model is evaluated on the commonly used zero-shot LVIS (Gupta et al., 2019) dataset, which contains 1,203 categories. (Section 4)
  - [Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf)

### Associated with
- **Localization ability** (construct), 1 paper
  > improving the localization capability, most works specifically focus on the downstream dense vision tasks such as open-vocabulary detection (Section 2)
  - [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf)
