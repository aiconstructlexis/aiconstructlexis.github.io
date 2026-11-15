# AudioCaps
**Type:** Measurement instrument  
**Supporting papers:** 14  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats AudioCaps as an audio captioning benchmark or dataset of AudioSet clips paired with human-written captions or natural-language descriptions. Some definitions add that the captions are in English, and one specifies one or two captions per clip. A smaller line of work also describes it as being used for audio retrieval, semantic retrieval, or question answering, and a few papers refer to AudioCapsZS, AudioCaps-QA, or an AC evaluation set.

**What it is claimed to measure.** Papers use AudioCaps to measure 3 behavioral indicators and no constructs. The dominant use is for Audio captioning: papers evaluate generated captions on AudioCaps, sometimes on its test set, and report conventional captioning metrics such as CIDEr. More occasionally, papers report it as measuring Cross-modal retrieval through semantic retrieval on AudioCaps, and Text-to-audio generation through evaluation on the AC evaluation set, so the measurement claims extend beyond captioning but remain centered on it.

**Space of uses.** In practice, papers most often use AudioCaps alongside Clotho or Clotho v2, and some also report it together with MusicCaps or Clotho-AQA. They commonly position it as a major, foundational, or commonly used benchmark for audio captioning, and in one case as part of audio-retrieval benchmarking. No measurement instrument is linked to it.

**Concerns raised.** A concern appears in one paper, which remarks that it is easy for audio-language models to perform well on AudioCaps and Clotho.

## Sources

**AudioCaps** (8 papers: [CompA: Addressing the Gap in Compositional Reasoning in Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/43c18853329c7504996b255252b6cb1f-Paper-Conference.pdf), [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf), [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf), [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf), [Merge then Realign: Simple and Effective Modality-Incremental Continual Learning for Multimodal LLMs](https://aclanthology.org/2025.emnlp-main.665.pdf), [An eye for an ear: zero-shot audio description leveraging an image captioner with audio-visual token distribution matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/4426af45e987692abf1b80108951ff8a-Paper-Conference.pdf), [LLMs Can Evolve Continually on Modality for $\mathbb{X}$-Modal Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/5942d10ae51b6bd07648e54df07ef9cd-Paper-Conference.pdf), [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf))
> A benchmark dataset used for evaluating audio-retrieval and captioning tasks, containing audio clips from AudioSet with human-written captions.

## Relationships

### → AudioCaps
- **Audio captioning** (behavioral indicator): *measured_by*, 6 papers
  > evaluate LTU on the test set of two major audio captioning benchmarks Clotho v2 (Drossos et al., 2020) and AudioCaps (Kim et al., 2019) (Section 5.1)
  - [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf)
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
  - [An eye for an ear: zero-shot audio description leveraging an image captioner with audio-visual token distribution matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/4426af45e987692abf1b80108951ff8a-Paper-Conference.pdf)
  - [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf)
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
  - [Enhancing Speech Large Language Models with Prompt-Aware Mixture of Audio Encoders](https://aclanthology.org/2025.emnlp-main.974.pdf)
- **Cross-modal retrieval** (behavioral indicator): *measured_by*, 1 paper
  > “Table 3: Semantic retrieval (R@1, R@5, and R@10) for CLAP and ELSA calculated over the original (non-spatial) versions of Clotho and AudioCaps.”
  - [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf)
- **Text-to-audio generation** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate our model on the AC evaluation set, following the protocol in AudioLDM and using its evaluation toolkit10. (Section 5)
  - [Generative Audio Language Modeling with Continuous-valued Tokens and Masked Next-Token Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25n/yang25n.pdf)
