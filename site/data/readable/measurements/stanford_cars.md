# Stanford Cars
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** Stanford-Cars, Cars, StanfordCars  

## State of the Field

**What it is.** Across papers, Stanford Cars is most commonly described as a fine-grained image classification benchmark or dataset for car models. Several definitions specify that it contains 196 classes or categories of cars, and some frame it as assessing fine-grained visual discrimination, while a smaller framing presents it more generally as an image classification benchmark used to test downstream performance. Papers also place it within broader image recognition and fine-grained visual classification benchmark suites.

**What it is claimed to measure.** In the recorded relationships, papers use Stanford Cars to measure the behavioral indicator Image classification. It is linked to 1 behavioral indicator and no constructs, so the recorded measurement use centers on a single target rather than being spread across multiple constructs. The relationship evidence describes this use in image recognition, zero-shot classification, downstream performance, and broader classification-domain evaluations.

**Space of uses.** Usage is usually as one dataset among several benchmarks, rather than as a standalone protocol. Quoted passages place it in zero-shot and linear-probe image classification, downstream performance testing, and fine-tuning of pretrained models, and the only linked instrument is FGVC, to which one paper relates it as one of the datasets in a fine-grained visual classification benchmark.

## Sources

**Stanford Cars** (3 papers: [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf), [Weighted Multi-Prompt Learning with Description-free Large Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/284e7ef68bf3d8fa42abf45a39f29f5e-Paper-Conference.pdf), [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf))
> Stanford Cars, a car model classification benchmark used to assess fine-grained visual discrimination.

**Stanford-Cars** (1 paper: [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf))
> Stanford-Cars is an image classification benchmark used here to test downstream performance of DeiT-B.

**Cars** (1 paper: [Portable Reward Tuning: Towards Reusable Fine-Tuning across Different Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chijiwa25a/chijiwa25a.pdf))
> The Stanford Cars dataset, a benchmark for fine-grained image classification consisting of 196 classes of cars.

**StanfordCars** (4 papers: [Beyond Accuracy: Ensuring Correct Predictions With Correct Rationales](https://proceedings.neurips.cc/paper_files/paper/2024/file/4bbeef01d9753fd5a29e9fd02d275698-Paper-Conference.pdf), [IPO: Interpretable Prompt Optimization for Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf), [Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf), [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf))
> A fine-grained image classification dataset containing images of 196 classes of cars.

## Relationships

### → Stanford Cars
- **Image classification** (behavioral indicator): *measured_by*, 4 papers
  > We evaluate our method on 12 image recognition datasets. We use the ... Stanford Cars (Krause et al., 2013)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)

### Associated with
- **FGVC** (measurement instrument), 1 paper
  > FGVC includes five Fine-Grained Visual Classification datasets: ... Stanford Cars (Gebru et al., 2017). (Section 5.1)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)
