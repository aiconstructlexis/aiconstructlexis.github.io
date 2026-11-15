# AG News
**Type:** Measurement instrument  
**Supporting papers:** 60  
**Also known as:** AG-News, AGNews, AGNEWS, AGnews, AgNews, AG's News, AG News Corpus, AG’s News  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats AG News as a benchmark or corpus for news topic classification, usually described as news articles assigned to four classes or categories. Many definitions specify the categories as World, Sports, Business, and Sci/Tech, while some describe the material more generally as short news articles from diverse domains or as a collection drawn from more than 2000 sources. A smaller line of work refers to AG News Title and Description, AGT and AGD, as title and description subsets used for semantic classification and retrieval.

**What it is claimed to measure.** Measurement claims are dominated by text classification: papers use AG News to measure 3 behavioral indicators in total, with text classification the prevailing one, downstream task performance another recurring use, and one other behavioral indicator appearing less often. It is also used to measure 5 constructs, with zero-shot generalization the most recurrent named construct, while papers also use it for adversarial robustness, calibration, and 2 other constructs. Some papers make the task explicit as categorizing a news article into one of the 4 categories, World, Sports, Business, and Sci/Tech.

**Space of uses.** Papers position AG News in several roles rather than a single fixed protocol. It is often used alongside other benchmarks, especially SST-2, and also with IMDB, DBpedia, and StrategyQA, and papers variously treat it as a primary classification benchmark, a user fine-tuning task, an in-context learning benchmark, an out-of-domain or unseen dataset for zero-shot evaluation, and a testbed for backdoor attacks, defenses, and confidence elicitation. No measurement instrument is linked to it.

## Sources

**AG-News** (2 papers: [Out-of-Distribution Detection by Leveraging Between-Layer Transformation Smoothness](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a2f65c9d2313b71005e600bd23393fe-Paper-Conference.pdf), [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf))
> A topic classification dataset (AGN) constructed from news articles, categorized into four classes.

**AG News** (8 papers: [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf), [In-Context Learning Learns Label Relationships but Is Not Conventional Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/0db404e9cc9d282be6dfe8538352408c-Paper-Conference.pdf), [SetCSE: Set Operations using Contrastive Learning of Sentence Embeddings](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed863220bf8b6ae698e26d66e86fb97d-Paper-Conference.pdf), [LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect](https://proceedings.neurips.cc/paper_files/paper/2024/file/064f6bcd7d3c72fb187bfca35ba2bfd4-Paper-Conference.pdf), [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf), [LLMs vs Established Text Augmentation Techniques for Classification: When do the Benefits Outweight the Costs?](https://aclanthology.org/2025.naacl-long.526.pdf), [Vulnerability-Aware Alignment: Mitigating Uneven Forgetting in Harmful Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25w/chen25w.pdf), [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf))
> The AG News dataset, a benchmark for topic classification of news articles into four categories.

**AGNews** (7 papers: [Revisiting In-context Learning Inference Circuit in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/22d4f952efa13970f0b1ffb22170d416-Paper-Conference.pdf), [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.416.pdf), [Logit Separability-Driven Samples and Multiple Class-Related Words Selection for Advancing In-Context Learning](https://aclanthology.org/2025.naacl-long.343.pdf), [Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25x/he25x.pdf), [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf), [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf), [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf))
> The AG News dataset, a topic classification benchmark with four categories of news articles.

**AGNEWS** (1 paper: [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf))
> The AG News (AGNEWS) corpus is a benchmark dataset for topic classification of news articles, used here as a user fine-tuning task.

**AGnews** (1 paper: [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf))
> A news topic classification benchmark used to evaluate text classification and generation settings in the paper.

**AgNews** (1 paper: [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf))
> A topic classification benchmark used in the paper's in-context learning and instruction-tuning analysis.

**AG's News** (1 paper: [Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf))
> A topic classification benchmark used to evaluate model behavior on news-topic categorization.

**AG News Corpus** (1 paper: [Active Few-Shot Learning for Text Classification](https://aclanthology.org/2025.naacl-long.340.pdf))
> News topic classification benchmark containing news articles across four categories, used to assess few-shot performance on balanced multi-class text classification.

**AG’s News** (1 paper: [ICLShield: Exploring and Mitigating In-Context Learning Backdoor Attacks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ren25b/ren25b.pdf))
> Text classification dataset used to evaluate news topic classification under backdoor attacks and defenses.

## Relationships

### → AG News
- **Text classification** (behavioral indicator): *measured_by*, 19 papers
  > SST-2 (Socher et al., 2013) and AGNews (Zhang et al., 2015) are text classification tasks with different class numbers
  - [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
  - [LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect](https://proceedings.neurips.cc/paper_files/paper/2024/file/064f6bcd7d3c72fb187bfca35ba2bfd4-Paper-Conference.pdf)
  - [Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
  - [Can Generative AI Solve Your In-Context Learning Problem? A Martingale Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/d90268f01ef06a55630b0588227adf4f-Paper-Conference.pdf)
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
  - [Data-adaptive Differentially Private Prompt Synthesis for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96d00450ed65531ffe2996daed487536-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
  - [LSSF: Safety Alignment for Large Language Models through Low-Rank Safety Subspace Fusion](https://aclanthology.org/2025.acl-long.1479.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [Plausible Token Amplification for Improving Accuracy of Differentially Private In-Context Learning Based on Implicit Bayesian Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yamasaki25a/yamasaki25a.pdf)
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
  - [Continuous-Time Attention: PDE-Guided Mechanisms for Long-Sequence Transformers](https://aclanthology.org/2025.emnlp-main.1097.pdf)
  - [CondenseLM: LLMs-driven Text Dataset Condensation via Reward Matching](https://aclanthology.org/2025.emnlp-main.65.pdf)
  - [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486.pdf)
  - [SliceMoE: Routing Embedding Slices Instead of Tokens for Fine-Grained and Balanced Transformer Scaling](https://aclanthology.org/2025.emnlp-main.807.pdf)
- **Zero-shot generalization** (construct): *measured_by*, 2 papers
  > We also evaluate the ability of BD3-LMs to generalize to unseen datasets in a zero-shot setting... We evaluate the likelihood of models trained with OWT on datasets... AG News... (Section 6.1)
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **Downstream task performance** (behavioral indicator): *measured_by*, 2 papers
  > “For fine-tuning task, we consider SST2(Socher et al., 2013), AGNEWS(Zhang et al., 2015), GSM8K(Cobbe et al., 2021) and AlpacaEval (Li et al., 2023a) as the user fine-tuning task.”
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **Language modeling ability** (construct): *measured_by*, 1 paper
  > We use 6 English textual corpora from 5 different domains for comprehensive evaluation... (5) AG News (Zhang et al., 2015) is a collection of news articles from diverse domains (Section 4.1.1)
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **News categorization** (behavioral indicator): *measured_by*, 1 paper
  > instruction: Categorize the news article into one of the 4 categories: World,Sports,Business,Sci/Tech. (Appendix B.1)
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
- **Adversarial robustness** (construct): *measured_by*, 1 paper
  > We conducted our confidence elicitation attacks on Meta-Llama-3-8B-Instruct (Touvron et al., 2023) and Mistral-7B-Instruct-v0.2 (Jiang et al., 2023) while performing classification on two common datasets to evaluate adversarial robustness: SST-2, AG-News and one modern dataset: StrategyQA (Geva et al., 2021). (Section 4)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **Calibration** (construct): *measured_by*, 1 paper
  > We first demonstrate that LLama3 is well-calibrated for the SST2, AG-News, and StrategyQA tasks, as illustrated in Table 1 and Figure 3. (Section 5.1)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > To evaluate LLMs’ general capabilities, we select several widely used benchmark, i.e., HellaSwag (Zellers et al., 2019), Race (Lai et al., 2017), MMLU (Hendrycks et al., 2021), GPQA (Rein et al., 2024), OpenBookQA (Mihaylov et al., 2018), BoolQ (Clark et al., 2019), AG News (Zhang et al., 2015), IMDB (Maas et al., 2011), and Perplexity (Chen et al., 1998). (Section 4.1)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
