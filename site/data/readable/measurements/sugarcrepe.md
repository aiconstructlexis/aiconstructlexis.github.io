# SugarCrepe
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Across the papers, SugarCrepe is most commonly described as a large-scale benchmark for evaluating the compositional reasoning capabilities of vision-language models, specifically through swaps, replacements, and additions of objects, attributes, and relations. Another description presents it as a compositionality benchmark with fine-grained attribute and semantic relationship distinctions, evaluated primarily with a single image and a caption choice.

**What it is claimed to measure.** Papers use SugarCrepe to measure 2 constructs, and no behavioral indicators are linked to it. The prevailing use is to measure compositional reasoning, with TripletCLIP describing analysis of models' compositional understanding on SugarCrepe, while some work also reports it as measuring relation understanding by evaluating the ability to understand and represent relationships between objects within an image.

**Space of uses.** Papers typically position SugarCrepe as a challenging benchmark for model evaluation, and no measurement instrument is linked to it. In reported uses, authors mainly evaluate models on it as a composition benchmark, and COCO-Tree notes that, because only a single image is provided, the task is simplified to Text Score.

## Sources

**SugarCrepe** (2 papers: [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf), [COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.135.pdf))
> A large-scale benchmark designed to systematically evaluate the compositional reasoning capabilities of vision-language models by testing their ability to handle swaps, replacements, and additions of objects, attributes, and relations.

## Relationships

### → SugarCrepe
- **Compositional reasoning** (construct): *measured_by*, 1 paper
  > We comprehensively analyze the compositional understanding of models on the SugarCrepe benchmark, as detailed in Table 4. (Section 4.2)
  - [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
- **Relation understanding** (construct): *measured_by*, 1 paper
  > We include relational benchmarks, such as Visual Genome [Yuksekgonul et al., 2023], Winoground [Thrush et al., 2022a], and SugarCrepe [Hsieh et al., 2024] designed to evaluate the models’ ability to understand and represent relationships between objects within an image... (Section 3.2)
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
