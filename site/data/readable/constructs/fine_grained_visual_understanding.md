# Fine-grained visual understanding
**Type:** Construct  
**Supporting papers:** 27  
**Also known as:** Perception of small visual details, Fine-grained recognition, Granular visual recognition, Detailed scene understanding, Fine-grained image comprehension, Confusing concept recognition, Fine-grained image understanding, Region-level comprehension, Fine-grained understanding, Finer-grained understanding, Fine-grained comprehension  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is a model ability to perceive and interpret detailed local visual information, especially small, pixel-level, point-level, or region-level content, rather than only high-level objects, scenes, or whole-image summaries. Most definitions keep the scope visual and focus on recognizing or understanding fine details, though narrower versions emphasize small objects, occluded details, text-like elements, confusing concepts, or subtle motion differences. A smaller line broadens the scope to preserving detailed visual information during multimodal question answering, integrating local details with broader context, or capturing subtle semantics in both vision and language.

**Space of facets.** Papers use many near-equivalent labels for overlapping ideas, including perception of small visual details, granular visual recognition, detailed scene understanding, fine-grained image comprehension, region-level comprehension, and fine-grained comprehension. The recurring facets are pixel or point-level detail, specific spatial regions, object attributes and relations, varying-sized text, confusing-concept discrimination, and frame-level action differencing. The consistent contrast is against global scene-level content or processing the image as a whole, although one paper extends the label to finer-grained understanding of both visual and linguistic patterns.

**Space of measurement.** Papers link it to 13 measurement instruments and 2 behavioral indicators. Operationalization is dominated by benchmark-style datasets: the most frequently linked instruments listed are ChartQA, DocVQA, TextVQA, GQA, and InfoVQA, and papers describe these evaluations as detail-sensitive, OCR-extensive, vision-centric, or scene-recognition tasks that require fine-grained visual information, smaller visual concepts, or reasoning across multiple areas of an image. This largely matches the definitions, because the instruments target local detail, text, confusing scenes, and multi-region understanding; the linked behavioral indicators are Image reconstruction and Sign language recognition.

**Links.** Beyond measurement, one paper claims a causal relationship from Image reconstruction to fine-grained visual understanding, stating that reconstruction helps models maintain low-level details and thereby enhances fine-grained comprehension. Related links are narrower: one paper reports that fine-grained visual understanding is related to Sign language recognition, because sign tasks demand fine-grained comprehension and context awareness, and another reports that Cognition and Emotion understanding are related to fine-grained visual understanding by noting that difficulty perceiving fine-grained details bears on those forms of understanding.

## Sources

**Fine-grained visual understanding** (4 papers: [KptLLM: Unveiling the Power of Large Language Model for Keypoint Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe692980c5d9732cf153ce27947653a7-Paper-Conference.pdf), [Video Action Differencing](https://proceedings.iclr.cc/paper_files/paper/2025/file/26f62bf3b74cda621831f550c6ee2dce-Paper-Conference.pdf), [MedRAX: Medical Reasoning Agent for Chest X-ray](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fallahpour25a/fallahpour25a.pdf), [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf))
> The ability to perceive and interpret small, pixel-level semantic details within an image, as opposed to only understanding high-level objects and scenes.

**Perception of small visual details** (1 paper: [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf))
> The ability to accurately identify and interpret fine-grained details or small objects within an image, a specific facet of visual perception.

**Granular visual recognition** (1 paper: [Feast Your Eyes: Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf))
> The latent ability of a model to perceive and identify small, occluded, or fine-grained details within an image.

**Detailed scene understanding** (1 paper: [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf))
> The model's ability to perceive and interpret fine-grained visual details within an image, such as small objects or intricate patterns.

**Fine-grained recognition** (1 paper: [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf))
> The latent ability to correctly identify small, irregular, or text-like visual elements in images.

**Fine-grained image comprehension** (1 paper: [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf))
> The model's ability to understand specific details, objects, and their attributes within an image at a level more detailed than a global summary.

**Confusing concept recognition** (1 paper: [Contrastive Visual Data Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25h/zhou25h.pdf))
> The latent ability of a model to distinguish between visually similar or commonly misrecognized concepts by leveraging fine-grained discriminative features.

**Fine-grained image understanding** (1 paper: [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf))
> The model's capacity to comprehend and reason about specific regions and objects within an image, beyond global image-level semantics.

**Region-level comprehension** (1 paper: [GeoPixel: Pixel Grounding Large Multimodal Model in Remote Sensing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shabbir25a/shabbir25a.pdf))
> The ability to understand and reason about specific spatial regions within an image, as opposed to only processing the image as a whole.

**Fine-grained understanding** (2 papers: [FineCLIP: Self-distilled Region-based CLIP for Better Fine-grained Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/3122aaa22b2fe83f9cead1a696f65ceb-Paper-Conference.pdf), [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf))
> The model's ability to comprehend and represent detailed local information within an image, such as object attributes and their relationships, as opposed to just global scene-level content.

**Finer-grained understanding** (1 paper: [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf))
> The ability to capture subtle differences and detailed semantic information in both visual and linguistic patterns.

**Fine-grained comprehension** (1 paper: [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf))
> The latent ability to preserve and use detailed visual information when answering multimodal questions.

## Relationships

### Fine-grained visual understanding →
- **TextVQA** (measurement instrument): *measured_by*, 2 papers
  > We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA, V∗, POPE, DocVQA)... (Sec. 6)
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **DocVQA** (measurement instrument): *measured_by*, 2 papers
  > We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA, V∗, POPE, DocVQA)... (Sec. 6)
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **ChartQA** (measurement instrument): *measured_by*, 2 papers
  > We evaluate our each variant of ROSS mainly on ... (ii) fine-grained comprehension: MMVP (Tong et al., 2024b) and ChartQA (Masry et al., 2022) (Section 5.1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 1 paper
  > Tasks that require fine-grained visual understanding and deep reasoning across multiple areas of the image naturally demand a higher number of visual tokens for optimal performance. ... This trend is evident in tasks such as VQAv2, GQA, VizWiz, MMBench, LLaVA-Bench, and MM-Vet.
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **GQA** (measurement instrument): *measured_by*, 1 paper
  > Tasks that require fine-grained visual understanding and deep reasoning across multiple areas of the image naturally demand a higher number of visual tokens for optimal performance. ... This trend is evident in tasks such as VQAv2, GQA, VizWiz, MMBench, LLaVA-Bench, and MM-Vet.
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **MMBench** (measurement instrument): *measured_by*, 1 paper
  > Tasks that require fine-grained visual understanding and deep reasoning across multiple areas of the image naturally demand a higher number of visual tokens for optimal performance. ... This trend is evident in tasks such as VQAv2, GQA, VizWiz, MMBench, LLaVA-Bench, and MM-Vet.
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **OCRBench** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **VizWiz** (measurement instrument): *measured_by*, 1 paper
  > Tasks that require fine-grained visual understanding and deep reasoning across multiple areas of the image naturally demand a higher number of visual tokens for optimal performance. ... This trend is evident in tasks such as VQAv2, GQA, VizWiz, MMBench, LLaVA-Bench, and MM-Vet.
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 1 paper
  > Tasks that require fine-grained visual understanding and deep reasoning across multiple areas of the image naturally demand a higher number of visual tokens for optimal performance. ... This trend is evident in tasks such as VQAv2, GQA, VizWiz, MMBench, LLaVA-Bench, and MM-Vet.
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **POPE** (measurement instrument): *measured_by*, 1 paper
  > We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA, V∗, POPE, DocVQA)... (Sec. 6)
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **MMVP** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our each variant of ROSS mainly on ... (ii) fine-grained comprehension: MMVP (Tong et al., 2024b) and ChartQA (Masry et al., 2022) (Section 5.1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **InfoVQA** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **SUN** (measurement instrument): *measured_by*, 1 paper
  > The SUN Dataset (Xiao et al., 2010) is a widely used large-scale scene recognition dataset that contains rich and confusing visual scenes. Correctly recognizing the scenes requires fine-grained visual reasoning and understanding of the scenes. (Section 5.1)
  - [Contrastive Visual Data Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25h/zhou25h.pdf)

### → Fine-grained visual understanding
- **Image reconstruction** (behavioral indicator): *causes*, 1 paper
  > This approach encourages LMMs to maintain low-level details, thereby enhancing their fine-grained comprehension abilities and reducing hallucinations. (Section 1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)

### Associated with
- **Sign language recognition** (behavioral indicator), 1 paper
  > All these tasks [ISLR, CSLR, and SLT] impose indispensable demands on the model’s fine-grained comprehension and context awareness capabilities. (Section 1)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
- **Cognition** (construct), 1 paper
  > While recent MLLMs show promising results in basic perception, they still struggle to perceive fine-grained details (Tong et al., 2024b), which is essential for understanding cognition and emotion.
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Emotion understanding** (construct), 1 paper
  > While recent MLLMs show promising results in basic perception, they still struggle to perceive fine-grained details (Tong et al., 2024b), which is essential for understanding cognition and emotion.
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
