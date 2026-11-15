# Amazon Polarity
**Type:** Measurement instrument  
**Supporting papers:** 7  
**Also known as:** Amazon, AmazonPolarity  

## State of the Field

**What it is.** The prevailing description treats Amazon Polarity, sometimes written as Amazon or AmazonPolarity, as a sentiment classification benchmark for product reviews and, more broadly, an NLP text classification dataset. Some papers instead describe "Amazon" differently: as a product co-purchasing network, where nodes are products and edges connect items frequently bought together, used for node classification in a text-attributed heterophilic graph, or as a temporal point process benchmark where the goal is to predict the timestamp and category of the next reviewed product among 16 categories.

**What it is claimed to measure.** In recorded relationships, papers link it to 1 behavioral indicator, Text classification, and to no constructs. The relationship is stated directionally as text classification being measured by Amazon Polarity, with the supporting use describing it as part of sentiment analysis, so the measurement claims converge on a single behavioral indicator rather than being spread across many targets.

**Space of uses.** Papers place it alongside other evaluation datasets rather than describe a separate protocol. It appears with SST-2 and Yelp in sentiment analysis evaluations, with BoolQ, SciQ, and CosmosQA as one of "four real-world NLP classification datasets," and in one debiasing study as a downstream check of whether debiasing preserves classification performance under semantic understanding tasks; no measurement instrument is formally linked to it.

## Sources

**Amazon** (4 papers: [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf), [Exploring the Potential of Large Language Models for Heterophilic Graphs](https://aclanthology.org/2025.naacl-long.269.pdf), [LAST SToP for Modeling Asynchronous Time Series](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25a/gupta25a.pdf))
> A benchmark dataset for text classification, specifically for sentiment analysis of product reviews.

**Amazon Polarity** (1 paper: [Relating Misfit to Gain in Weak-to-Strong Generalization Beyond the Squared Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mulgund25a/mulgund25a.pdf))
> A sentiment classification benchmark used here as an NLP classification dataset.

**AmazonPolarity** (1 paper: [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.208.pdf))
> AmazonPolarity is a sentiment-related benchmark used to check whether debiasing preserves downstream classification performance.

## Relationships

### → Amazon Polarity
- **Text classification** (behavioral indicator): *measured_by*, 1 paper
  > We study text classification using four datasets: sentiment analysis using SST-2 (Socher et al., 2013) and Amazon (Zhang et al., 2015)... (Section 4.1)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
