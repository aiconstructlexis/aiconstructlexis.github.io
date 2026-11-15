# UltraFeedback Binarized
**Type:** Measurement instrument  
**Supporting papers:** 3  
**Also known as:** UF-B  

## State of the Field

**What it is.** Most descriptions treat UltraFeedback Binarized, also written UF-B or UFB, as a widely used dataset for preference alignment or preference fine-tuning, organized as binarized or paired preference data for dialogue tasks. A more specific description says it is built from GPT-4 scored UltraFeedback completions, where the highest-scoring completion is labeled "chosen" and another, in one account a random completion, is labeled "rejected".

**What it is claimed to measure.** Papers do not explicitly say that UltraFeedback Binarized measures any construct or behavioral indicator. The descriptions instead frame it as a dataset for preference alignment or preference fine-tuning, and as a resource used to train and evaluate alignment methods.

**Space of uses.** Across the surveyed work, it is commonly used as an evaluation and fine-tuning dataset for alignment methods. Papers place it alongside Alpaca Comparison and TL;DR in multi-dataset experiments, and one line of work specifically groups it with Alpaca Comparison as one of two dialogue datasets; another states, "For fine-tuning on the UltraFeedback Binarized dataset, we use two families of models."

## Sources

**UF-B** (1 paper: [Direct Density Ratio Optimization: A Statistically Consistent Approach to Aligning Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/higuchi25a/higuchi25a.pdf))
> UltraFeedback-Binarized (UF-B), a paired preference dataset derived from GPT-4 scored completions, where the highest-scoring response is labeled as chosen and another as rejected.

**UltraFeedback Binarized** (2 papers: [ROPO: Robust Preference Optimization for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25d/liang25d.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf))
> A widely-used dataset for preference alignment consisting of binarized preference pairs for dialogue tasks.
