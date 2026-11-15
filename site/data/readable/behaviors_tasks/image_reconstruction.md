# Image reconstruction
**Type:** Behavioral indicator  
**Supporting papers:** 8  

## State of the Field

**Space of definitions.** Across the surveyed papers, the prevailing usage is a fidelity-oriented task in which an image, or a compressed or latent form of it, is reconstructed so the output can be compared with the original. Most definitions describe encoding and decoding back to the original image, while some frame it as generating an output image that accurately matches a training example, recovering clean fine-grained tokens from noisy tokens, or re-rendering decomposed layers so they yield the original picture. One paper, Reconstructive Visual Instruction Tuning, also describes it as supervising visual outputs by reconstructing the input image. Success is usually expressed as fidelity to the original, through reconstruction quality, reconstruction loss, or a reconstruction error threshold.

**Variants.** Papers study several variants rather than a single fixed setup. These include reconstruction from compressed representations, from visual outputs or latent visual representations, from noisy tokens back to clean fine-grained tokens, from noise conditioned on visual and textual features, and by re-rendering decomposed layers while recovering occluded regions. One paper also instantiates the task as reconstructing images from Fashion-MNIST training data.

**Space of elicitation and scores.** Papers link the behavior to 3 measurement instruments: CUB-200-2011, CelebA, and MS-COCO, and papers report image reconstruction results on these datasets. Scoring is most commonly described through differences between generated and original images, including reconstruction quality tables, reconstruction loss, and a failure condition when reconstruction error exceeds a threshold. DS-VLM: Diffusion Supervision Vision Language Model states that it constructs reconstruction loss to measure the difference between the generated image and the original image.

**What it is taken as evidence of.** The linked construct targets are spread across 3 constructs, Fine-grained visual understanding, Multimodal understanding, and Representation quality, so the recorded relationships do not single out one prevailing construct. Instead, different papers claim causal relationships from image reconstruction to each of these constructs, describing the effects as enhancing fine-grained comprehension, enhancing multimodal comprehension, or enhancing visual feature quality. There is also 1 linked behavioral indicator, Hallucination, and one paper claims a causal relationship from image reconstruction to it, describing the effect as reducing hallucinations.

## Sources

**Image reconstruction** (5 papers: [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf), [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf), [A Simple Model of Inference Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/levi25a/levi25a.pdf), [DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf), [Decomposition of Graphic Design with Unified Multimodal Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25c/nie25c.pdf))
> The task of encoding an image into a compressed representation and then decoding it back to its original form to measure fidelity.

## Relationships

### Image reconstruction →
- **CelebA** (measurement instrument): *measured_by*, 1 paper
  > As shown in Table 1, GEM surpasses baseline models in reconstruction quality on the datasets of CelebA, LSUN-horse, and LSUN-bedroom. (Section 4.2)
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **CUB-200-2011** (measurement instrument): *measured_by*, 1 paper
  > Results of image reconstruction on TextCaps, CelebA-HQ, CUB-200, and MS-COCO. (Table 1)
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **MS-COCO** (measurement instrument): *measured_by*, 1 paper
  > Results of image reconstruction on TextCaps, CelebA-HQ, CUB-200, and MS-COCO. (Table 1)
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **Fine-grained visual understanding** (construct): *causes*, 1 paper
  > This approach encourages LMMs to maintain low-level details, thereby enhancing their fine-grained comprehension abilities and reducing hallucinations. (Section 1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > This approach encourages LMMs to maintain low-level details, thereby enhancing their fine-grained comprehension abilities and reducing hallucinations. (Section 1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Multimodal understanding** (construct): *causes*, 1 paper
  > In this way, LMMs are required to preserve every detail of input images, thereby enhancing multimodal comprehension capabilities and reducing hallucinations. (Figure 1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Representation quality** (construct): *causes*, 1 paper
  > This approach simultaneously preserves high-level semantic alignment through conventional text supervision while enhancing visual feature quality via pixel-level reconstruction constraints. (Abstract)
  - [DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf)
