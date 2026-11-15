# CrowS-Pairs
**Type:** Measurement instrument  
**Supporting papers:** 27  
**Also known as:** Crows-Pairs, CrowsPairs  

## State of the Field

**What it is.** Across the surveyed work, CrowS-Pairs is most commonly described as a crowdsourced dataset or benchmark of sentence pairs that contrast stereotypical with anti-stereotypical, or less stereotypical, formulations, often as minimal pairs differing in a demographic-group or social-group reference. Papers describe the task in slightly different ways: models may be asked which sentence is more likely, which is more natural or reasonable, or be checked for whether they assign higher probability to the biased variant. Most descriptions place it in English or U.S. English and focused on stereotypes tied to historically disadvantaged groups, while some papers discuss multilingual adaptations or translations, including French, Dutch, German, Spanish, and Catalan, as well as multilingual and Spanish-subset versions.

**What it is claimed to measure.** Papers link CrowS-Pairs to 3 constructs and no behavioral indicators. The prevailing measurement claim is social bias: papers say it evaluates social bias, includes sentences with social biases, or checks a model's propensity to generate biased outputs. A smaller but recurring line of work uses it to measure stereotyping, and one paper places it among safety and toxicity benchmarks, so its reported use spreads across Social bias, Stereotyping, and Toxicity rather than converging on only one construct.

**Space of uses.** Papers usually position CrowS-Pairs as one component in broader evaluation suites or as a comparison point for other bias benchmarks. It appears alongside StereoSet, TruthfulQA, BBQ-style benchmarks, WinoGender, and DecodingTrust, and some studies use it to validate methods or compare closed-ended against open-ended fairness evaluation. Other work extracts stereotype prompts from it or correlates new audit rankings against it.

**Concerns raised.** A few papers note limits in how the benchmark is structured or what it covers. One description says that, because it is crowd-sourced, it does not explicitly identify concept or identity terms, and another reports limited overlap between its examples and CrowS-Pairs.

## Sources

**CrowS-Pairs** (20 papers: [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf), [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf), [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf), [Towards Reward Fairness in RLHF: From a Resource Allocation Perspective](https://aclanthology.org/2025.acl-long.163.pdf), [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf), [BTC-SAM: Leveraging LLMs for Generation of Bias Test Cases for Sentiment Analysis Models](https://aclanthology.org/2025.emnlp-main.763.pdf), [Blind Men and the Elephant: Diverse Perspectives on Gender Stereotypes in Benchmark Datasets](https://aclanthology.org/2025.emnlp-main.1162.pdf), [Debiasing Multilingual LLMs in Cross-lingual Latent Space](https://aclanthology.org/2025.emnlp-main.1149.pdf), [F²Bench: An Open-ended Fairness Evaluation Benchmark for LLMs with Factuality Considerations](https://aclanthology.org/2025.emnlp-main.105.pdf), [HESEIA: A community-based dataset for evaluating social biases in large language models, co-designed in real school settings in Latin America](https://aclanthology.org/2025.emnlp-main.1275.pdf), [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models](https://aclanthology.org/2025.emnlp-main.774.pdf), [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.208.pdf), [Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLM Collaboration](https://aclanthology.org/2025.emnlp-main.1221.pdf), [Social Bias in Multilingual Language Models: A Survey](https://aclanthology.org/2025.emnlp-main.1416.pdf), [TFDP: Token-Efficient Disparity Audits for Autoregressive LLMs via Single-Token Masked Evaluation](https://aclanthology.org/2025.emnlp-main.1250.pdf), [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf), [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf), [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf), [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf), [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf))
> Dataset for measuring the presence of stereotypical biases in language models by comparing model preferences between stereotypical and anti-stereotypical sentence pairs.

**Crows-Pairs** (1 paper: [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf))
> A dataset for measuring stereotypical biases in U.S. English language models by comparing sentences with stereotypical and anti-stereotypical associations.

**CrowsPairs** (2 papers: [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf), [La Leaderboard: A Large Language Model Leaderboard for Spanish Varieties and Languages of Spain and Latin America](https://aclanthology.org/2025.acl-long.1561.pdf))
> A benchmark for measuring stereotypical biases in language models by presenting pairs of sentences, one more stereotypical than the other, and testing which the model prefers.

## Relationships

### → CrowS-Pairs
- **Social bias** (construct): *measured_by*, 8 papers
  > Probability-based bias evaluations such as CrowS-Pairs [22] and tasks in the BIG-bench benchmarking suite [48] compare the probabilities of stereotype-related tokens conditional on the presence of identity-related tokens. (Section 2.2)
  - [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf)
  - [Towards Reward Fairness in RLHF: From a Resource Allocation Perspective](https://aclanthology.org/2025.acl-long.163.pdf)
  - [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.208.pdf)
  - [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models](https://aclanthology.org/2025.emnlp-main.774.pdf)
  - [Debiasing Multilingual LLMs in Cross-lingual Latent Space](https://aclanthology.org/2025.emnlp-main.1149.pdf)
  - [TFDP: Token-Efficient Disparity Audits for Autoregressive LLMs via Single-Token Masked Evaluation](https://aclanthology.org/2025.emnlp-main.1250.pdf)
- **Stereotyping** (construct): *measured_by*, 3 papers
  > CrowS-Pairs (Nangia et al., 2020) assesses stereotypes associated with historically disadvantaged groups.
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
  - [Blind Men and the Elephant: Diverse Perspectives on Gender Stereotypes in Benchmark Datasets](https://aclanthology.org/2025.emnlp-main.1162.pdf)
  - [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
- **Toxicity** (construct): *measured_by*, 1 paper
  > We evaluate the Spectra suite across various safety and toxicity benchmarks of TruthfulQA (Lin et al., 2021), Big Bench BBQ Lite (Parrish et al., 2022) and CrowsPairs (Nangia et al., 2020). (Section 5)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
