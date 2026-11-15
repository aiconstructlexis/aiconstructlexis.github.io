# Recommendation
**Type:** Behavioral indicator  
**Supporting papers:** 8  
**Also known as:** User intention capture, Collaborative filtering, Top-K item generation, Recommendation generation, Item recommendation, Top-k recommendation  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats recommendation as predicting or generating items for a user from profile information, historical interactions, or user-item interaction behaviors. Most definitions describe the output as a list, often a ranked or top-k list, of items or item IDs that are relevant, most likely to be preferred, or that best match the user's preferences. As described in Language Representations Can be What Recommenders Need: Findings and Potentials, collaborative filtering "aims to select item i that best matches user u's preferences based on binary interaction behaviors," while other papers phrase the task as generating recommendations directly with an LLM.

**Variants.** Papers study several variants under this label. Common named versions include collaborative filtering, top-K item generation, item recommendation, top-k recommendation, and user intention capture; these differ in whether they predict the next liked item, generate K distinct token sequences by beam search, or refine outputs by combining historical interests with language-based intention queries. A smaller line of work places the task in multi-modal or graph-based settings, estimating preferences from an interaction graph together with item descriptions and images.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers operationalize the behavior directly through the task output: generating a recommendation list, predicting relevant item IDs, or producing K distinct token sequences as top-K items, often through beam search.

**What it is taken as evidence of.** Rather than mapping it to one construct, papers link recommendation to 3 constructs. One paper reports that Fairness is related to Recommendation, and that Recommendation is related to Social bias, describing implications for fairness, bias, and whether recommender systems work for everyone. Another paper claims a causal relationship from Memorization to Recommendation, stating that better memorization "leads to improvements in various recommendation tasks."

## Sources

**Collaborative filtering** (1 paper: [Language Representations Can be What Recommenders Need: Findings and Potentials](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4bab1843c8d5a69f5abfd0824593493-Paper-Conference.pdf))
> The task of predicting a user's interest in an item based on the collective preferences and behaviors of many users, typically represented in a user-item interaction matrix.

**User intention capture** (1 paper: [Language Representations Can be What Recommenders Need: Findings and Potentials](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4bab1843c8d5a69f5abfd0824593493-Paper-Conference.pdf))
> Refining recommendations by combining user historical interests with language-based intention queries.

**Top-K item generation** (1 paper: [Efficient Inference for Large Language Model-based Generative Recommendation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4bf5c3245fd92a4554a16af9803b757-Paper-Conference.pdf))
> The observable behavior of producing K distinct token sequences, representing a list of recommended items, typically via beam search.

**Recommendation generation** (1 paper: [Logit Space Constrained Fine-Tuning for Mitigating Hallucinations in LLM-Based Recommender Systems](https://aclanthology.org/2025.emnlp-main.1491.pdf))
> The observable task of producing a list of recommended items for a user based on their profile and historical interactions.

**Item recommendation** (1 paper: [Towards Unified Multi-Modal Personalization: Large Vision-Language Models for Generative Recommendation and Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/297a7a54da76d95f02b04d957a53c7ba-Paper-Conference.pdf))
> The observable task of predicting and generating a list of relevant item IDs that a user is likely to be interested in based on their interaction history.

**Top-k recommendation** (1 paper: [A Multi-modal Large Language Model with Graph-of-Thought for Effective Recommendation](https://aclanthology.org/2025.naacl-long.76.pdf))
> Generating a ranked list of k items most likely to be preferred by a user based on historical interactions and item features.

## Relationships

### → Recommendation
- **Memorization** (construct): *causes*, 1 paper
  > The experiments show that META ID improves memorization and diversity score, which leads to improvements in various recommendation tasks. (Section 1)
  - [Improving LLMs for Recommendation with Out-Of-Vocabulary Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ar/huang25ar.pdf)

### Associated with
- **Fairness** (construct), 1 paper
  > Clearly, this has important implications for fairness, bias, and whether recommender systems work for everyone. (Section 4).
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Social bias** (construct), 1 paper
  > Clearly, this has important implications for fairness, bias, and whether recommender systems work for everyone. (Section 4).
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
