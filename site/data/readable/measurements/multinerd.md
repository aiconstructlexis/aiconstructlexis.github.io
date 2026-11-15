# MultiNERD
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Most commonly, papers describe MultiNERD as a named entity recognition dataset, with one definition presenting it as a NER pre-training dataset based on Wikipedia and Wikinews, containing 164K instances in the English split and 17 label names, and used as a baseline for IE pre-training. A smaller line of work treats it as the named entity recognition dataset used to examine chain-of-thought prompting under few-shot open-set conditions, including seen and unseen classes.

**What it is claimed to measure.** Across the papers here, MultiNERD is not explicitly linked as measuring any construct or behavioral indicator. Instead, papers use it for task evaluation in named entity recognition and, in one case, for reporting seen-class and unseen-class F1 under few-shot open-set classification.

**Space of uses.** Papers position MultiNERD in two main ways: as a baseline dataset for IE pre-training, and as an evaluation dataset for reasoning-based prompting. In "Few-Shot Open-Set Classification via Reasoning-Aware Decomposition," it is the dataset on which chain-of-thought prompting is examined, and the paper reports that a method achieves the highest F1-score in 50/54 settings for seen classes and 47/54 for unseen classes; the papers do not explicitly relate it to other named measurement instruments.

## Sources

**MultiNERD** (2 papers: [Cuckoo: An IE Free Rider Hatched by Massive Nutrition in LLM's Nest](https://aclanthology.org/2025.acl-long.66.pdf), [Few-Shot Open-Set Classification via Reasoning-Aware Decomposition](https://aclanthology.org/2025.emnlp-main.699.pdf))
> A named entity recognition pre-training dataset based on Wikipedia and Wikinews, containing 164K English instances with 17 label names, used as a baseline for IE pre-training.
