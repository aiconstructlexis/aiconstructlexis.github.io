# Sentiment analysis
**Type:** Behavioral indicator  
**Supporting papers:** 135  
**Also known as:** Sentiment classification, Binary sentiment classification, Sentiment label generation, Emotional valence scoring, Embodied emotion recognition, Opinion polarity classification  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing treats sentiment analysis as a text classification task over text inputs, usually asking a model to assign sentiment polarity or tone labels such as positive and negative, and often also neutral. Papers describe success as returning the appropriate label for a sentence, review, tweet, or other text, and one prompt-based formulation asks the model to "return the sentiment of the review." A smaller line of work broadens this beyond fixed-label classification, including finer-grained sentiment scales, generated label text, and continuous emotional valence scores.

**Variants.** Variants are most often distinguished by label granularity and domain. Papers study binary sentiment classification of reviews and sentences most often, but also positive, negative, neutral setups, five-way sentiment, document-level and sentence-level classification, and opinion polarity classification; domain-specific versions include financial sentiment, code-mixed text, Persian text, and Belarusian sentiment-labeled sentences. A smaller line of work treats related tasks as emotional valence scoring for crisis conversations, where models "assign numerical emotional valence scores," or as embodied emotion recognition, where a first-person video is classified for its overall positive or negative emotional tendency.

**Space of elicitation and scores.** Papers measure this behavior with nine measurement instruments. The most frequently linked are SST-2 and IMDb, followed by GLUE, Financial PhraseBank, and SST-5, with four other instruments also used. These are mostly benchmark datasets for sentiment polarity classification, with GLUE appearing as a broader evaluation suite; where papers state the scoring explicitly, classification variants are commonly reported with accuracy or top-1 accuracy, while the valence-scoring variant predicts numerical scores.

**What it is taken as evidence of.** Only one linked construct appears in the papers, compositional generalization. The relationship is a related claim rather than a measured_by, correlational, or causal one: one paper uses sentiment classification as a phrase-level structure task to assess aspects of compositional generalization. Beyond that, the papers do not provide an alternative construct framing.

## Sources

**Sentiment analysis** (17 papers: [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf), [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf), [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf), [Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf), [Matina: A Large-Scale 73B Token Persian Text Corpus](https://aclanthology.org/2025.naacl-long.462.pdf), [CompAct: Compressed Activations for Memory-Efficient LLM Training](https://aclanthology.org/2025.naacl-long.71.pdf), [EmojiPrompt: Generative Prompt Obfuscation for Privacy-Preserving Communication with Cloud-based LLMs](https://aclanthology.org/2025.naacl-long.614.pdf), [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.122.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf), [LLM The Genius Paradox: A Linguistic and Math Expert's Struggle with Simple Word-based Counting Problems](https://aclanthology.org/2025.naacl-long.172.pdf), [BelarusianGLUE: Towards a Natural Language Understanding Benchmark for Belarusian](https://aclanthology.org/2025.acl-long.25.pdf), [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf), [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.24.pdf), [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf))
> The task of classifying the sentiment or tone of a given piece of text as positive, negative, or neutral.

**Sentiment classification** (7 papers: [Achieving Domain-Independent Certified Robustness via Knowledge Continuity](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cc11cda2a2679e8af5c6317aed0af8-Paper-Conference.pdf), [Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf), [UniICL: An Efficient ICL Framework Unifying Compression, Selection, and Generation](https://aclanthology.org/2025.acl-long.24.pdf), [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf), [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [SMAB: MAB based word Sensitivity Estimation Framework and its Applications in Adversarial Text Generation](https://aclanthology.org/2025.naacl-long.463.pdf))
> The task of determining the sentimental tone (e.g., positive, negative) expressed in a piece of text.

**Binary sentiment classification** (1 paper: [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf))
> The task of classifying text into one of two sentiment categories, such as positive or negative.

**Sentiment label generation** (1 paper: [Power doesn't reside in size: A Low Parameter Hybrid Language Model (HLM) for Sentiment Analysis in Code-mixed data](https://aclanthology.org/2025.emnlp-main.749.pdf))
> The task of producing the text of a sentiment label (e.g., "Positive") as a generative output rather than selecting from a fixed set of classes.

**Emotional valence scoring** (1 paper: [Assessing effective de-escalation of crisis conversations using transformer-based models and trend statistics](https://aclanthology.org/2025.emnlp-main.1512.pdf))
> Assigning a continuous numerical score to a text input that represents its emotional valence, typically on a scale from negative to positive.

**Embodied emotion recognition** (1 paper: [$E^3$: Exploring Embodied Emotion Through A Large-Scale Egocentric Video Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/d611d5c0251d9680f869c5d2c46c6fcd-Paper-Datasets_and_Benchmarks_Track.pdf))
> A classification task to predict the overall positive or negative emotional tendency of a first-person view video.

**Opinion polarity classification** (1 paper: [Active Few-Shot Learning for Text Classification](https://aclanthology.org/2025.naacl-long.340.pdf))
> The specific text classification task of determining whether an expressed opinion is positive, negative, or neutral.

## Relationships

### Sentiment analysis →
- **SST-2** (measurement instrument): *measured_by*, 27 papers
  > “Sentiment Analysis (SST-2)”
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
  - [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf)
  - [DP-OPT: Make Large Language Model Your Privacy-Preserving Prompt Engineer](https://proceedings.iclr.cc/paper_files/paper/2024/file/fffe5a7804c40465ef2432386850c2c7-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
  - [Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf)
  - [Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf)
  - [Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
  - [Can Generative AI Solve Your In-Context Learning Problem? A Martingale Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/d90268f01ef06a55630b0588227adf4f-Paper-Conference.pdf)
  - [Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b79416c0dc4b09feaa169ed5cdd63d4-Paper-Conference.pdf)
  - [Soft Prompting for Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.204.pdf)
  - [Enhancing Language Model Hypernetworks with Restart: A Study on Optimization](https://aclanthology.org/2025.naacl-long.397.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [LLaMAs Have Feelings Too: Unveiling Sentiment and Emotion Representations in LLaMA Models Through Probing](https://aclanthology.org/2025.acl-long.306.pdf)
  - [Pretraining Context Compressor for Large Language Models with Embedding-Based Memory](https://aclanthology.org/2025.acl-long.1394.pdf)
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
  - [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf)
  - [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf)
  - [Continuous-Time Attention: PDE-Guided Mechanisms for Long-Sequence Transformers](https://aclanthology.org/2025.emnlp-main.1097.pdf)
  - [Linear-Time Demonstration Selection for In-Context Learning via Gradient Estimation](https://aclanthology.org/2025.emnlp-main.832.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
  - [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173.pdf)
  - [Disentangled Information Bottleneck for Adversarial Text Defense](https://aclanthology.org/2025.emnlp-main.1183.pdf)
  - [NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1769.pdf)
  - [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf)
- **IMDb** (measurement instrument): *measured_by*, 11 papers
  > we run all of our experiments on the IMDB dataset [48] (a sentiment classification task) using a host of language models from different model families (encoder, decoder, encoder-decoder). (Section 5)
  - [Achieving Domain-Independent Certified Robustness via Knowledge Continuity](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cc11cda2a2679e8af5c6317aed0af8-Paper-Conference.pdf)
  - [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf)
  - [Release the Powers of Prompt Tuning: Cross-Modality Prompt Transfer](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ae9589ff1a691d09ef0528e4e309b2f-Paper-Conference.pdf)
  - [Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b79416c0dc4b09feaa169ed5cdd63d4-Paper-Conference.pdf)
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
  - [Towards Robust Alignment of Language Models: Distributionally Robustifying Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/294fd30f8cbb89ce328d5a01fef47fb4-Paper-Conference.pdf)
  - [LLaMAs Have Feelings Too: Unveiling Sentiment and Emotion Representations in LLaMA Models Through Probing](https://aclanthology.org/2025.acl-long.306.pdf)
  - [Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf)
  - [Continuous-Time Attention: PDE-Guided Mechanisms for Long-Sequence Transformers](https://aclanthology.org/2025.emnlp-main.1097.pdf)
  - [Disentangled Information Bottleneck for Adversarial Text Defense](https://aclanthology.org/2025.emnlp-main.1183.pdf)
- **GLUE** (measurement instrument): *measured_by*, 4 papers
  > We finetune the pretrained RoBERTa-base model (Liu et al., 2019) on the GLUE benchmark, a widely used suite for evaluating NLP models across various tasks, including sentiment analysis and question answering (Wang et al., 2019). (Section 4.2)
  - [CompAct: Compressed Activations for Memory-Efficient LLM Training](https://aclanthology.org/2025.naacl-long.71.pdf)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
  - [A Memory Efficient Randomized Subspace Optimization Method for Training Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cj/chen25cj.pdf)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf)
- **SST-5** (measurement instrument): *measured_by*, 3 papers
  > SST-5 [40] Sentiment Analysis (Table 1)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf)
  - [Graceful Forgetting in Generative Language Models](https://aclanthology.org/2025.emnlp-main.666.pdf)
- **Financial PhraseBank** (measurement instrument): *measured_by*, 3 papers
  > Sentiment analysis focuses on extracting sentiment information (positive, negative, or neutral) from financial texts, using three datasets: the Financial Phrase Bank (FPB) (Malo et al., 2014), FiQA-SA (Maia et al., 2018), and TSA (Cortis et al., 2017).
  - [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
- **Rotten Tomatoes** (measurement instrument): *measured_by*, 2 papers
  > Our experiments utilize three benchmark datasets for sentiment classification: IMDB (Maas et al., 2011), SST-2 (Socher et al., 2013), and Rotten Tomatoes (Pang and Lee, 2005), all of which contain movie reviews for binary polarity tasks (e.g., positive or negative sentiment). (Section 3)
  - [LLaMAs Have Feelings Too: Unveiling Sentiment and Emotion Representations in LLaMA Models Through Probing](https://aclanthology.org/2025.acl-long.306.pdf)
  - [Disentangled Information Bottleneck for Adversarial Text Defense](https://aclanthology.org/2025.emnlp-main.1183.pdf)
- **FiQA-SA** (measurement instrument): *measured_by*, 2 papers
  > Sentiment analysis focuses on extracting sentiment information (positive, negative, or neutral) from financial texts, using three datasets: the Financial Phrase Bank (FPB) (Malo et al., 2014), FiQA-SA (Maia et al., 2018), and TSA (Cortis et al., 2017).
  - [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf)
- **Emotion (dair-ai)** (measurement instrument): *measured_by*, 1 paper
  > Emotion (Kosti et al., 2019) with text data labeled with various emotions, suitable for sentiment analysis tasks (Section 5.2)
  - [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf)
- **CR** (measurement instrument): *measured_by*, 1 paper
  > For sentiment classification, we use the Poem Sentiment, SST-2, and CR datasets. (Section 5.1)
  - [Linear-Time Demonstration Selection for In-Context Learning via Gradient Estimation](https://aclanthology.org/2025.emnlp-main.832.pdf)

### Associated with
- **Compositional generalization** (construct), 1 paper
  > Two tasks that assess different aspects of compositional generalisation are used in the paper: Inverse Dictionary Modelling (IDM) for word-level composition and Sentiment Classification (SC) for phrase-level structure. (Section 4.1)
  - [CARMA: Enhanced Compositionality in LLMs via Advanced Regularisation and Mutual Information Alignment](https://aclanthology.org/2025.emnlp-main.822.pdf)
