# Yelp
**Type:** Measurement instrument  
**Supporting papers:** 9  

## State of the Field

**What it is.** Across papers, the prevailing description is of a review dataset from the Yelp platform, derived from Yelp reviews and used in classification settings. Most definitions frame it for sentiment classification or sentiment analysis, while some specify business reviews, opinions about restaurants and local services, or short natural language casual reviews; one definition also describes it as a 5-way classification task.

**What it is claimed to measure.** Formally, papers link Yelp to 1 behavioral indicator and no constructs. The linked behavioral indicator is Text classification: one paper reports that Text classification is measured by Yelp, describing Yelp as one of two 5-way classification tasks; elsewhere, papers describe Yelp as used to evaluate sentiment classification, out-of-distribution sentiment analysis, downstream classifiers, synthetic-data utility, and text origin detection.

**Space of uses.** Papers often use Yelp alongside other datasets, including SST-5, SST2, Fine-Food, and OpenReview, as one component of broader evaluation suites. In those settings it is positioned as a sentiment benchmark, an out-of-distribution evaluation set, a source of seed samples and downstream classifier evaluation, a 5-way classification task for assessing synthetic data utility, and a short natural language dataset for text origin detection; no measurement instrument is formally linked to it.

## Sources

**Yelp** (5 papers: [LLMs vs Established Text Augmentation Techniques for Classification: When do the Benefits Outweight the Costs?](https://aclanthology.org/2025.naacl-long.526.pdf), [SALAD: Improving Robustness and Generalization through Contrastive Learning with Structure-Aware and LLM-Driven Augmented Data](https://aclanthology.org/2025.naacl-long.634.pdf), [Direct Prompt Optimization with Continuous Representations](https://aclanthology.org/2025.acl-long.133.pdf), [Synthesizing Privacy-Preserving Text Data via Finetuning *without* Finetuning Billion-Scale LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25g/tan25g.pdf), [Profiler: Black-box AI-generated Text Origin Detection via Context-aware Inference Pattern Analysis](https://aclanthology.org/2025.emnlp-main.1265.pdf))
> A dataset derived from Yelp reviews, used for sentiment classification tasks to source seed samples and evaluate downstream classifiers.

## Relationships

### → Yelp
- **Text classification** (behavioral indicator): *measured_by*, 1 paper
  > We conduct experiments on two classiﬁcation tasks: Yelp (Yelp, Inc.) and OpenReview (Xie et al., 2024), both of which are 5-way classiﬁcation... (Section 4.1.1)
  - [Synthesizing Privacy-Preserving Text Data via Finetuning *without* Finetuning Billion-Scale LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25g/tan25g.pdf)
