# CelebA
**Type:** Measurement instrument  
**Supporting papers:** 8  

## State of the Field

**What it is.** Across papers, CelebA is most commonly described as a large-scale face or facial-attributes dataset, often said to contain over 200K celebrity images with 40 binary attribute annotations. Some authors narrow the setup to predicting 'Blond Hair' with 'Male' as the sensitive attribute, while others treat it as facial attribute recognition data or as source images for emotion-comparison examples. One paper also preprocesses CelebA by cropping, resizing, and flattening pixel values into space-separated numerical sentences for language-model inputs.

**What it is claimed to measure.** Recorded measurement claims are narrow. Papers link CelebA to one behavioral indicator, Image reconstruction, and link it to no constructs or other measurement instruments. In that usage, a paper evaluates reconstruction quality on CelebA and reports results on CelebA alongside LSUN-horse and LSUN-bedroom.

**Space of uses.** Papers position CelebA mainly as an evaluation dataset, with uses that include fairness evaluation, robustness testing under spurious correlations and distribution shifts, facial attribute recognition, early-exit diffusion image generation, and disentanglement, reconstruction, and attribute-scoring reliability. It also appears alongside other image datasets such as UTK, Waterbirds, CIFAR-10, and FER-2013. Some uses are indirect: one paper turns the images into numerical sentences for model inputs, and another gathers facial images from CelebA to build emotion-comparison examples.

**Concerns raised.** Where papers foreground issues around CelebA, they describe settings with spurious attribute correlations and distribution shifts. Fairness-oriented work also fixes a specific target and sensitive attribute, setting y to 'Blond Hair' and a to 'Male'.

## Sources

**CelebA** (7 papers: [Debiasing Attention Mechanism in Transformer without Demographics](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f5337a39b1f6d670aad9d32debc0e5d-Paper-Conference.pdf), [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf), [Zero-Shot Robustification of Zero-Shot Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/92ce40962b4098f7bf6eed33128fc606-Paper-Conference.pdf), [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf), [Fast yet Safe: Early-Exiting with Risk Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea5a63f7ddb82e58623693fd1f4933f7-Paper-Conference.pdf), [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf), [MLLM-CompBench: A Comparative Reasoning Benchmark for Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/32923dff09f75cf1974c145764a523e2-Paper-Datasets_and_Benchmarks_Track.pdf))
> The Celeb-A dataset, a large-scale face attributes dataset used here to evaluate fairness in predicting the 'Blond Hair' attribute with respect to the 'Male' sensitive attribute.

## Relationships

### → CelebA
- **Image reconstruction** (behavioral indicator): *measured_by*, 1 paper
  > As shown in Table 1, GEM surpasses baseline models in reconstruction quality on the datasets of CelebA, LSUN-horse, and LSUN-bedroom. (Section 4.2)
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
