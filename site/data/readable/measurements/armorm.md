# ArmoRM
**Type:** Measurement instrument  
**Supporting papers:** 16  
**Also known as:** ArmoRM-Llama3-8B-v0.1, ArmoRM-8B, ArmoRM-Llama3-8B  

## State of the Field

**What it is.** Across papers, the prevailing usage is as a reward model and automated judge for LLM responses. Most descriptions present it as a multi-dimension or multi-objective model, while some papers refer to specific 8B Llama3 variants, including ArmoRM-8B, ArmoRM-Llama3-8B, and ArmoRM-Llama3-8B-v0.1 or v0.13. Definitions and quoted passages place these variants in several roles: evaluating alignment from various perspectives, scoring model outputs, filtering synthetic preference data, creating preference pairs, and assigning ground-truth quality labels or acting as a proxy judge.

**What it is claimed to measure.** Papers link ArmoRM to two constructs and two behavioral indicators overall. The most common reported measurement claim is that it measures text generation quality, while smaller lines of work use it to measure helpfulness and instruction following, sometimes by selecting its instruction-following dimension as the main evaluation metric. It is also related to preference ranking, with papers employing it to score and rank responses, so its reported use covers a small set of different evaluation targets rather than a single one.

**Space of uses.** Most commonly, papers position ArmoRM as an automated evaluator, external judge, or proxy model for response assessment. It appears both as a main metric, for example when authors select its instruction-following dimension, and as a scorer for ranking multiple responses, filtering synthetic preference data, creating preference pairs when gold labels are absent, calculating win rate on ListUltraFeedback, and assigning ground-truth labels. Some studies use it alongside other reward models, including PairRM, Skywork-Reward-Llama-3.1-8B, and Skywork-Reward-Gemma-2-27B.

## Sources

**ArmoRM-Llama3-8B-v0.1** (1 paper: [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf))
> ArmoRM-Llama3-8B-v0.1, a scoring model used for filtering synthetic preference data in the Llama3 setting.

**ArmoRM-8B** (1 paper: [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf))
> An 8-billion parameter reward model used as an automated evaluator, specifically leveraging its instruction-following dimension to score model outputs.

**ArmoRM** (3 papers: [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf), [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf), [Permutative Preference Alignment from Listwise Ranking of Human Judgments](https://aclanthology.org/2025.emnlp-main.17.pdf))
> A state-of-the-art multi-dimension reward model used as an automated judge to evaluate the alignment of LLM responses from various perspectives.

**ArmoRM-Llama3-8B** (1 paper: [Self-Consistency Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/prasad25a/prasad25a.pdf))
> A specific, publicly-available reward model used as an external judge to score model-generated responses and create preference pairs for baseline training.

## Relationships

### → ArmoRM
- **Text generation quality** (construct): *measured_by*, 2 papers
  > we assess response quality using reward models... we employ three state-of-the-art reward models from RewardBench (Lambert et al., 2024): ArmoRM-Llama3-8B-v0.1 (Wang et al., 2024a), Skywork-Reward-Llama-3.1-8B (Liu and Zeng, 2024), and Skywork-Reward-Gemma-2-27B (Liu and Zeng, 2024). (Section 4.2)
  - [Stronger Models are Not Always Stronger Teachers for Instruction Tuning](https://aclanthology.org/2025.naacl-long.224.pdf)
  - [BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ding25d/ding25d.pdf)
- **Helpfulness** (construct): *measured_by*, 1 paper
  > Since ArmoRM is a multi-objective model that not only gives a scalar reward value but also predicts human-interpretable fine-grained attributes, we first select 5 attributes (namely complexity, instruction following, honesty, helpfulness, and intelligence depth) that have the highest average coefficients on the UltraFeedback data. (Section 6.2)
  - [Reward-Augmented Data Enhances Direct Preference Alignment of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25az/zhang25az.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > To address this issue, we selected the instruction-following dimension from ArmoRM-8B (Wang et al., 2024a) as the main evaluation metric for our experiment. (Section 4.1)
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)

### Associated with
- **Preference ranking** (behavioral indicator), 1 paper
  > “ArmoRM-Llama-3-8B-v0.1 (Wang et al., 2024a) is then employed as the reward model to score and rank these responses.”
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
