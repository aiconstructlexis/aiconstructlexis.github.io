# Weibo21
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across papers, Weibo21 is commonly described as a Chinese benchmark drawn from the Weibo platform for fake news or rumor detection. One description presents it as a Chinese-language fake news detection dataset, while another frames it as a Chinese multi-domain rumor detection dataset covering 9 domains, with each news item containing news content and several comments.

**What it is claimed to measure.** Across papers, Weibo21 is used to measure one behavioral indicator, Misinformation detection, and it is not linked to any constructs. This usage converges on a single target: papers evaluate misinformation detection with Weibo21, and several descriptions place that evaluation within fake news detection tasks.

**Space of uses.** Papers use Weibo21 alongside GossipCop, AMTCele, Pheme, and LLM-mis in experimental evaluations. In these accounts it is positioned as one of the benchmark datasets in the test setup, for example as the Chinese dataset paired with GossipCop, or as one of the public datasets used in experiments on cross-domain misinformation detection and rumor detection.

## Sources

**Weibo21** (2 papers: [Generate First, Then Sample: Enhancing Fake News Detection with LLM-Augmented Reinforced Sampling](https://aclanthology.org/2025.acl-long.1182.pdf), [A Multi-Agent Framework with Automated Decision Rule Optimization for Cross-Domain Misinformation Detection](https://aclanthology.org/2025.emnlp-main.291.pdf))
> A Chinese-language benchmark dataset for fake news detection, sourced from the Weibo social media platform.

## Relationships

### → Weibo21
- **Misinformation detection** (behavioral indicator): *measured_by*, 2 papers
  > We conduct experiments on three public datasets, including human-written Pheme (Buntain and Golbeck, 2017), Weibo21 (Nan et al., 2021), and the LLM-generated LLM-mis (Chen and Shu, 2022). (Section 4.1)
  - [LLM-based Rumor Detection via Influence Guided Sample Selection and Game-based Perspective Analysis](https://aclanthology.org/2025.acl-long.1378.pdf)
  - [A Symbolic Adversarial Learning Framework for Evolving Fake News Generation and Detection](https://aclanthology.org/2025.emnlp-main.619.pdf)
