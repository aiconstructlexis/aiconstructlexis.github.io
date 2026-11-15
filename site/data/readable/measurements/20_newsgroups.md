# 20 Newsgroups
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** 20NG, 20NewsGroups  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats 20 Newsgroups, also written 20NG or 20NewsGroups, as a dataset of newsgroup posts for document understanding and text classification. Definitions describe it as containing approximately 20,000 documents partitioned across 20 different newsgroups, and as a benchmark used to evaluate model performance and robustness in federated learning settings. A smaller usage repurposes it to define an in-domain task from its computer science categories and an out-of-domain set from the remaining categories.

**What it is claimed to measure.** In the recorded relationships, papers use it to measure one construct, Natural language understanding, and one behavioral indicator, Text classification. One paper includes 20NG among "4 NLU benchmarks," while another uses 20 Newsgroups as the proxy dataset for a topic classification task under the Text classification label. The linked measurement claims therefore span these two framings rather than a broader set of constructs or indicators.

**Space of uses.** Papers typically use it alongside other evaluation datasets rather than on its own. In federated fine-tuning work it appears with BANKING77 for comparisons under different data heterogeneity settings, and in one NLU setup it is grouped with RTE, COLA, and QNLI. Another usage takes articles from the computer science categories for training and treats the other categories as an out-of-domain set.

## Sources

**20NG** (1 paper: [Shh, don't say that! Domain Certification in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/27befed4547edcb4bdeacef9472cadee-Paper-Conference.pdf))
> The 20 Newsgroups dataset, used here to define the in-domain task of computer science news generation and the out-of-domain set from its other categories.

**20 Newsgroups** (1 paper: [Towards Robust and Efficient Federated Low-Rank Adaptation with Heterogeneous Clients](https://aclanthology.org/2025.acl-long.19.pdf))
> A dataset for text classification based on newsgroup posts, used to evaluate model performance and robustness in federated learning scenarios.

**20NewsGroups** (1 paper: [Forward Knows Efficient Backward Path: Saliency-Guided Memory-Efficient Fine-tuning of Large Language Models](https://aclanthology.org/2025.acl-long.459.pdf))
> A dataset for document understanding and classification, consisting of approximately 20,000 newsgroup documents partitioned across 20 different newsgroups.

## Relationships

### → 20 Newsgroups
- **Text classification** (behavioral indicator): *measured_by*, 1 paper
  > When conducting domain shift poisoning pre-training, we utilize the IMDB (Maas et al., 2011), Twitter (Founta et al., 2018), and 20 Newsgroups (Lang, 1995) as the proxy dataset for sentiment analysis, toxicity detection, and topic classification task, respectively (Section 5.1).
  - [Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
- **Natural language understanding** (construct): *measured_by*, 1 paper
  > The experiments involved 4 NLU benchmarks: RTE (Wang et al., 2019), COLA (Wang et al., 2019), 20NG (Lang, 1995) and QNLI (Wang et al., 2019) (Section 4).
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
