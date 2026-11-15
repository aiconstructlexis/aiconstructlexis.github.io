# Localization ability
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Localization capability, Localization  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats localization ability as a latent model capacity for accurate spatial identification in visual content. The definitions largely agree on that core idea, with one framing it as identifying and specifying the position of target instances, and another as determining the spatial position and boundaries of objects within an image.

**Space of facets.** Papers use the near-synonymous labels localization capability and localization ability for the same kind of model property. The main difference in emphasis is whether the construct is described around target instances in visual content or around objects and their boundaries in images, and it is also discussed in connection with referring expression comprehension and open-ended object detection and segmentation.

**Space of measurement.** Papers link localization ability to one measurement instrument, MMLongBench-Doc, which is described as including single-page questions mainly to evaluate localization abilities, and to two behavioral indicators, Open-vocabulary object detection and Referring expression understanding. Another common operationalization is task accuracy under IoU-based criteria, including Acc0.5, Acc0.75, Acc0.9, and mean accuracy across IoU criteria, which matches the definitions' emphasis on locating targets and object boundaries.

**Links.** One paper claims a causal relationship from Fine-grained perception to localization ability, stating that sharper attention maps and more fine-grained features result in improved localization ability. Papers also describe localization ability as related to Referring expression understanding and to Open-vocabulary object detection, while no correlational links are reported.

## Sources

**Localization capability** (1 paper: [A Large-Scale Human-Centric Benchmark for Referring Expression Comprehension in the LMM Era](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f0cd0305f7741659304f5325f3bf6d-Paper-Datasets_and_Benchmarks_Track.pdf))
> The latent ability of a model to accurately identify and specify the position of target instances within visual content.

**Localization ability** (1 paper: [Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf))
> The model's latent capacity to accurately determine the spatial position and boundaries of objects within an image.

## Relationships

### Localization ability →
- **MMLongBench-Doc** (measurement instrument): *measured_by*, 1 paper
  > “(1) 494 single-page questions (with one evidence page) mainly to evaluate localization abilities”
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)

### → Localization ability
- **Fine-grained perception** (construct): *causes*, 1 paper
  > We visualize the attention maps from the penultimate layer of the CLIP visual encoder for several examples in Fig 2. The attention maps are generally similar w/wo alignment, as the regularization term prevents significant changes in the model’s weights. However, we still observe that the attention maps after alignment are sharper and highlight more fine-grained features. This indicates that the aligned model is better at capturing details from the input image, resulting in improved localization ability. (Section 4.2)
  - [Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25b/gong25b.pdf)

### Associated with
- **Referring expression understanding** (behavioral indicator), 1 paper
  > The REC task serves as a critical benchmark to evaluate the localization capabilities of these models. (Section 2)
  - [A Large-Scale Human-Centric Benchmark for Referring Expression Comprehension in the LMM Era](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f0cd0305f7741659304f5325f3bf6d-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Open-vocabulary object detection** (behavioral indicator), 1 paper
  > improving the localization capability, most works specifically focus on the downstream dense vision tasks such as open-vocabulary detection (Section 2)
  - [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf)
