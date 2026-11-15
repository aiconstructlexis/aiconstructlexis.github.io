# Emotion understanding
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Emotion perception, Emotional recognition, Fine-grained emotion recognition, Nuanced emotion recognition, Emotional understanding  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats emotion understanding as a latent ability to perceive, identify, infer, or interpret emotional content from visual or multimodal evidence, including emotions, sentiment, affective tone, and sometimes the atmospheric quality of a scene. A smaller line of work defines it more narrowly as recognizing a person's emotion category or emotional expressions, while another broadens it to complex, coexisting, and nuanced states that go beyond basic or discrete categories. The main variation is in the target of inference, scene atmosphere versus human emotion, and in the expected output, label prediction versus natural-language description.

**Space of facets.** Papers organize the construct mainly by granularity. Some use nearby labels such as emotion perception and emotional recognition for identifying and interpreting cues from multimodal inputs and predicting an emotion label, while others introduce fine-grained or nuanced emotion recognition for subtle, compound, culturally specific, or arbitrary categories beyond basic taxonomies. One paper also relates it to a coarse-grained then fine-grained classification pipeline, and another explicitly describes emotion understanding as a more complex, high-level perceptual task.

**Space of measurement.** Operationalization is fairly concentrated: papers connect the construct to 5 measurement instruments and 1 behavioral indicator. The named instruments are EQ-Bench, MELD, MVSA-M, MVSA-S, and TumEmo; the recorded uses include evaluating emotional understanding with EQ-Bench, sentiment polarity classification with MVSA-S and MVSA-M, six-basic-emotion classification with TumEmo, and MELD results described as showing emotion perception and contextual understanding. This measurement space spans broad evaluation and narrower classification tasks, while several definitions emphasize nuanced, complex, or generative emotion understanding; the only linked behavioral indicator is emotion analysis, which one paper relates to a two-stage coarse- and fine-grained classification procedure.

**Links.** Outside measurement, papers only record related links. Emotion understanding is related to fine-grained visual understanding, with one paper stating that difficulty in perceiving fine-grained details is essential for understanding cognition and emotion, and it is also related to social bias through EQ-Bench-based findings of performance disparities across race, gender, and age group. A separate paper relates emotion analysis to emotion understanding through a setup that first performs coarse-grained emotion classification and then fine-grained classification.

## Sources

**Emotion understanding** (2 papers: [ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/28aad3b3b315d86910d7f4ee2867dfa4-Paper-Datasets_and_Benchmarks_Track.pdf), [AffectGPT: A New Dataset, Model, and Benchmark for Emotion Understanding with Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lian25a/lian25a.pdf))
> The ability to infer or form an opinion about the emotional or atmospheric qualities of a scene based on visual evidence.

**Emotional understanding** (2 papers: [II-Bench: An Image Implication Understanding Benchmark for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/52764eb83bf0a0bd32766ce5c01612e5-Paper-Datasets_and_Benchmarks_Track.pdf), [Can MLLMs Understand the Deep Implication Behind Chinese Images?](https://aclanthology.org/2025.acl-long.700.pdf))
> The ability to perceive and interpret the human emotions, sentiment, and affective tone conveyed by an image.

**Emotion perception** (2 papers: [Emotion-LLaMA: Multimodal Emotion Recognition and Reasoning with Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/c7f43ada17acc234f568dc66da527418-Paper-Conference.pdf), [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf))
> The latent ability to accurately identify and interpret emotional expressions from multimodal inputs.

**Emotional recognition** (1 paper: [Emotion-LLaMA: Multimodal Emotion Recognition and Reasoning with Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/c7f43ada17acc234f568dc66da527418-Paper-Conference.pdf))
> The latent ability to infer a person's emotion category from multimodal evidence such as facial expression, voice, and text.

**Fine-grained emotion recognition** (1 paper: [AffectGPT: A New Dataset, Model, and Benchmark for Emotion Understanding with Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lian25a/lian25a.pdf))
> The capacity to identify and generate detailed, nuanced emotional categories beyond basic emotions, reflecting the diversity and subtlety of human affective states.

**Nuanced emotion recognition** (1 paper: [OV-MER: Towards Open-Vocabulary Multimodal Emotion Recognition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lian25b/lian25b.pdf))
> The ability to detect and represent subtle, compound, or culturally specific emotional states that are not captured by basic emotion taxonomies.

## Relationships

### Emotion understanding →
- **EQ-Bench** (measurement instrument): *measured_by*, 1 paper
  > To evaluate LVLMs’ emotional understanding ability, we utilized EQ-Bench (Paech, 2023). (Section 3.3)
  - [Does the Emotional Understanding of LVLMs Vary Under High-Stress Environments and Across Different Demographic Attributes?](https://aclanthology.org/2025.acl-long.1130.pdf)
- **MVSA-S** (measurement instrument): *measured_by*, 1 paper
  > “Emotion: Following (Yang et al., 2023; Huang et al., 2024), we conduct experiments on 4 benchmark datasets. MVSA-S and MVSA-M (Niu et al., 2016) are datasets used for sentiment polarity classification (positive or negative), while TumEmo (Yang et al., 2021) is a multimodal dataset designed for classifying six basic emotions. Additionally, HFM (Liu et al., 2022) is a multimodal dataset focused on recognizing high-level implicit emotion of sarcasm.”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **MVSA-M** (measurement instrument): *measured_by*, 1 paper
  > “Emotion: Following (Yang et al., 2023; Huang et al., 2024), we conduct experiments on 4 benchmark datasets. MVSA-S and MVSA-M (Niu et al., 2016) are datasets used for sentiment polarity classification (positive or negative), while TumEmo (Yang et al., 2021) is a multimodal dataset designed for classifying six basic emotions. Additionally, HFM (Liu et al., 2022) is a multimodal dataset focused on recognizing high-level implicit emotion of sarcasm.”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **TumEmo** (measurement instrument): *measured_by*, 1 paper
  > “Emotion: Following (Yang et al., 2023; Huang et al., 2024), we conduct experiments on 4 benchmark datasets. MVSA-S and MVSA-M (Niu et al., 2016) are datasets used for sentiment polarity classification (positive or negative), while TumEmo (Yang et al., 2021) is a multimodal dataset designed for classifying six basic emotions. Additionally, HFM (Liu et al., 2022) is a multimodal dataset focused on recognizing high-level implicit emotion of sarcasm.”
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **MELD** (measurement instrument): *measured_by*, 1 paper
  > This shows its strong emotion perception and contextual understanding. (Section 4.2, referring to MELD results in Table 6)
  - [Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.1216.pdf)

### Associated with
- **Fine-grained visual understanding** (construct), 1 paper
  > While recent MLLMs show promising results in basic perception, they still struggle to perceive fine-grained details (Tong et al., 2024b), which is essential for understanding cognition and emotion.
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Emotion analysis** (behavioral indicator), 1 paper
  > In this paper, we propose Sharpening Emotion Perception in Multimodal Large Language Models (SEPM)... The first stage performs coarse-grained emotion classification, generating textual prompts for the next stage... The second stage then completes fine-grained emotion classification based on this enhanced input. (Section 1, 3.2)
  - [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf)
- **Social bias** (construct), 1 paper
  > an analysis of the models’ emotional understanding ability, using EQ-Bench-based metrics, revealed that... (2) performance disparities were confirmed across race, gender, and age group. (Abstract)
  - [Does the Emotional Understanding of LVLMs Vary Under High-Stress Environments and Across Different Demographic Attributes?](https://aclanthology.org/2025.acl-long.1130.pdf)
