# Emotion (dair-ai)
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** Emotion  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats Emotion (Saravia et al., 2018) as a text classification dataset or benchmark for fine-grained emotion classification. One definition specifies six classes, joy, sadness, anger, fear, love, and surprise, and one study describes these as six "nuanced" classes in a more complex evaluation. Another definition also presents it as a six-category emotion benchmark but lists anger, disgust, fear, joy, sadness, and surprise, so papers do not describe the label set identically.

**What it is claimed to measure.** Most papers use it to measure Text classification, describing Emotion among "Text Classification datasets" and text classification benchmark suites. A smaller line of work uses it to measure Sentiment analysis, with one paper describing it as text data labeled with various emotions and suitable for sentiment analysis tasks. Papers link it to 2 behavioral indicators, Text classification and Sentiment analysis, and to no constructs.

**Space of uses.** Papers often place it inside multi-dataset evaluation suites. In those setups it appears alongside other text classification datasets such as CoLA, AG News, Stanford Sentiment Treebank, DBPEDIA-14, and IMDb, and one study describes it as part of a "more complex evaluation" for fine-grained sentiment classification.

## Sources

**Emotion** (1 paper: [LLaMAs Have Feelings Too: Unveiling Sentiment and Emotion Representations in LLaMA Models Through Probing](https://aclanthology.org/2025.acl-long.306.pdf))
> A dataset for fine-grained emotion classification, categorizing text into six classes: joy, sadness, anger, fear, love, and surprise.

## Relationships

### → Emotion (dair-ai)
- **Text classification** (behavioral indicator): *measured_by*, 4 papers
  > Following Zhang et al. (2023b), we evaluate on a series of Text Classification datasets: CoLA (2 labels) (Warstadt et al., 2019), Emotion (6 labels) (Saravia et al., 2018)... (Section 3.1)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
  - [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486.pdf)
  - [SliceMoE: Routing Embedding Slices Instead of Tokens for Fine-Grained and Balanced Transformer Scaling](https://aclanthology.org/2025.emnlp-main.807.pdf)
- **Sentiment analysis** (behavioral indicator): *measured_by*, 1 paper
  > Emotion (Kosti et al., 2019) with text data labeled with various emotions, suitable for sentiment analysis tasks (Section 5.2)
  - [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf)
