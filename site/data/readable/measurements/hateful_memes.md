# Hateful Memes
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** HATEFUL MEMES, FHM, HatefulMemes  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats Hateful Memes, also written HATEFUL MEMES, HatefulMemes, or FHM, as a multimodal meme benchmark or dataset built around meme images and their text captions. Papers describe it as classifying whether an image-text combination is hateful, whether a meme "describes hateful intentions," or whether it contains harmful content; some also note that it requires reasoning beyond simple unimodal signals and describe it as a challenge released by Meta or Facebook.

**What it is claimed to measure.** Papers link this instrument to no constructs and to two behavioral indicators, hate speech detection and harmful content detection. The reported measurement claims use both framings: some papers describe it as evaluating multimodal hate speech detection, while others use it to test whether a model can distinguish toxic from non-toxic images or detect harmful meme content.

**Space of uses.** No measurement instrument is linked to it. Papers instead use it as an evaluation dataset for multimodal systems, sometimes alongside other public meme datasets, including HarM and MAMI, and sometimes as a specific-mapping task where the model is asked to determine whether a meme with its caption contains harmful content and output "yes" or "no". Other papers place it inside broader evaluation setups where models output predictions for hate speech detection in HATEFUL MEMES.

## Sources

**HATEFUL MEMES** (1 paper: [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf))
> A multimodal meme classification benchmark used to determine whether an image-text combination is hateful.

**HatefulMemes** (2 papers: [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf), [TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.39.pdf))
> A dataset for detecting hate speech in multimodal memes, requiring reasoning beyond simple unimodal signals.

**FHM** (1 paper: [MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection](https://aclanthology.org/2025.acl-long.46.pdf))
> The Facebook Hateful Memes (FHM) dataset, a benchmark released as part of a challenge to evaluate multimodal harmful meme detection in hate speech.

## Relationships

### → Hateful Memes
- **Hate speech detection** (behavioral indicator): *measured_by*, 2 papers
  > Multimodal fusion takes in the image, text, and a description of the task, and then outputs a prediction, which can include... hate speech detection in HATEFUL MEMES... (Section 2.2).
  - [HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MemeIntel: Explainable Detection of Propagandistic and Hateful Memes](https://aclanthology.org/2025.emnlp-main.1539.pdf)
- **Harmful content detection** (behavioral indicator): *measured_by*, 2 papers
  > We use three publicly available meme datasets for evaluation: (1) HarM (Pramanick et al., 2021a), (2) FHM (Kiela et al., 2020), and (3) MAMI (Fersini et al., 2022). (Section 4.1)
  - [MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection](https://aclanthology.org/2025.acl-long.46.pdf)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
