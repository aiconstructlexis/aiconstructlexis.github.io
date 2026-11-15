# IMDb
**Type:** Measurement instrument  
**Supporting papers:** 45  
**Also known as:** IMDB, Imdb, IMDB dataset, IMDb dataset  

## State of the Field

**What it is.** Across the surveyed papers, the prevailing usage is as a movie-review sentiment benchmark: definitions most often describe IMDb as a large, binary sentiment classification dataset of movie reviews with positive and negative labels. Some papers make the format more specific, describing a corpus of 50,000 or 50K highly polar reviews, while one definition says it contains movie reviews and ratings and is also used in recommendation system research. A smaller line of work uses it as a controlled-generation testbed for generating positive movie reviews, and one paper treats it as an out-of-distribution target-domain sentiment benchmark.

**What it is claimed to measure.** Papers link it to three behavioral indicators and three constructs. The linked behavioral-indicator uses are sentiment analysis, controlled sentiment generation, and text classification; the quoted passages describe IMDb as supporting binary polarity classification, semantic analysis of user sentiment, and positive-sentiment movie review generation. Beyond those uses, papers also report it as measuring general ability, generalization, and out-of-distribution generalization, so the measurement claims extend across several evaluation targets rather than a single one.

**Space of uses.** Papers commonly place it inside broader evaluation suites, alongside other classification benchmarks such as SST-2, MNLI, AG News, BoolQ, and SuperGLUE, and one definition places it in an expanded dataset pool for cascade evaluation. Other papers use it as a target task under domain shift or as a downstream evaluation task after continued pretraining and finetuning. In controlled-generation work it is positioned as a testbed for sentiment alignment, and one study reports using a subset of 1000 samples separately for positive and negative control; no measurement instrument is directly linked to it.

## Sources

**IMDb** (8 papers: [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf), [Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf), [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf), [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.416.pdf), [Explicit Preference Optimization: No Need for an Implicit Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25l/hu25l.pdf), [Achieving Domain-Independent Certified Robustness via Knowledge Continuity](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cc11cda2a2679e8af5c6317aed0af8-Paper-Conference.pdf), [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf), [UQE: A Query Engine for Unstructured Databases](https://proceedings.neurips.cc/paper_files/paper/2024/file/34b3a40ec9752c1ae48fe85fef8fe8dc-Paper-Conference.pdf))
> A sentiment classification benchmark included in the expanded dataset pool for cascade evaluation.

**IMDB** (7 papers: [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf), [Vanishing Gradients in Reinforcement Finetuning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b09bb02b90584e2be94ff3ae09289bc-Paper-Conference.pdf), [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf), [Logit Separability-Driven Samples and Multiple Class-Related Words Selection for Advancing In-Context Learning](https://aclanthology.org/2025.naacl-long.343.pdf), [LLM The Genius Paradox: A Linguistic and Math Expert's Struggle with Simple Word-based Counting Problems](https://aclanthology.org/2025.naacl-long.172.pdf), [Direct Prompt Optimization with Continuous Representations](https://aclanthology.org/2025.acl-long.133.pdf), [CondenseLM: LLMs-driven Text Dataset Condensation via Reward Matching](https://aclanthology.org/2025.emnlp-main.65.pdf))
> A sentiment-related dataset from GRUE used in the paper's reinforcement finetuning experiments.

**Imdb** (1 paper: [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf))
> A dataset of movie reviews and ratings, widely used for sentiment analysis and recommendation system research.

**IMDb dataset** (1 paper: [Privately Aligning Language Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/477b39bfb9db99f60914dbfed5f23eb2-Paper-Conference.pdf))
> Sentiment classification benchmark used to evaluate controlled generation of positive movie reviews, serving as a testbed for alignment without human-in-the-loop.

**IMDB dataset** (1 paper: [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf))
> A large movie review dataset used for evaluating controlled text generation, particularly sentiment alignment in generated reviews.

## Relationships

### → IMDb
- **Sentiment analysis** (behavioral indicator): *measured_by*, 11 papers
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
- **Text classification** (behavioral indicator): *measured_by*, 4 papers
  > Table 1: Overview of the tasks, datasets... Task Text Classification Dataset IMDB
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
  - [EMO: Embedding Model Distillation via Intra-Model Relation and Optimal Transport Alignments](https://aclanthology.org/2025.emnlp-main.385.pdf)
  - [CondenseLM: LLMs-driven Text Dataset Condensation via Reward Matching](https://aclanthology.org/2025.emnlp-main.65.pdf)
  - [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486.pdf)
- **Controlled sentiment generation** (behavioral indicator): *measured_by*, 4 papers
  > For controlled sentiment generation task, we employ the IMDB dataset (Maas et al., 2011), which is a large movie review dataset. (Section 4)
  - [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf)
  - [Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.497.pdf)
  - [MPO: An Efficient Post-Processing Framework for Mixing Diverse Preference Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25af/wang25af.pdf)
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > We investigate the generalization performance of a host of approximate Bayesian methods... we train a CNN-LSTM model... on the IMDB (Maas et al., 2011)...
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > To test this hypothesis [about generalizability], we conducted an experiment ... under conditions of domain shift. For this experiment, we used three text classification datasets. Specifically, we used IMDB, CR (Ding et al., 2008), and Tweet for sentiment classification. (Section 4.4)
  - [Plug-in and Fine-tuning: Bridging the Gap between Small Language Models and Large Language Models](https://aclanthology.org/2025.acl-long.271.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > To evaluate LLMs’ general capabilities, we select several widely used benchmark, i.e., HellaSwag (Zellers et al., 2019), Race (Lai et al., 2017), MMLU (Hendrycks et al., 2021), GPQA (Rein et al., 2024), OpenBookQA (Mihaylov et al., 2018), BoolQ (Clark et al., 2019), AG News (Zhang et al., 2015), IMDB (Maas et al., 2011), and Perplexity (Chen et al., 1998). (Section 4.1)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
