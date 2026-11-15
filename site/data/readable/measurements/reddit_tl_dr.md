# Reddit TL;DR
**Type:** Measurement instrument  
**Supporting papers:** 35  
**Also known as:** TL;DR dataset, Reddit TL;DR dataset, Reddit summarization dataset, TL;DR summarization, TL;DR comparison data, Reddit TL;DR Summarization, TL;DR, TLDR  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats Reddit TL;DR as a Reddit-based summarization dataset or benchmark, usually described as posts paired with short, human-written summaries. Some definitions add that a post may come with several short summaries judged by human evaluators for quality and informativeness, while others describe preference-labeled comparison data or multiple generated summaries with human preference data. A smaller line describes it more generally as a summarization benchmark of articles and summaries, but most descriptions specifically center Reddit posts, with papers also referring to train and test splits, a comparison-data variant, and a subset restricted to relationship-oriented subreddits.

**What it is claimed to measure.** Papers use it to measure 3 constructs and 2 behavioral indicators. The prevailing use is to measure Text summarization, and a smaller line of work uses it to measure Alignment; individual papers also use it to measure Abstractive summarization, Summary quality, and Out-of-distribution generalization. Taken together, these claims mostly converge on summarization, with additional use for Alignment, Summary quality, and Out-of-distribution generalization.

**Space of uses.** No other measurement instrument is linked to it. Papers usually position it as a benchmark for summarization experiments, and some explicitly use it as a main dataset in RLHF, preference optimization, or offline alignment settings; some also use it across supervised fine-tuning, reward modeling, RL, and test-set evaluation. More specialized uses include training reward models on the train split, domain-specific pre-training on TL;DR comparison pairs, judging win rate between a model summary and the ground-truth answer with GPT-4, and holding out relationship and relationship-advice subreddits for out-of-distribution evaluation.

## Sources

**TL;DR** (4 papers: [Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf), [Design Considerations in Offline Preference-based RL](https://raw.githubusercontent.com/mlresearch/v267/main/assets/agarwal25a/agarwal25a.pdf), [Intuitive Fine-Tuning: Towards Simplifying Alignment into a Single Process](https://aclanthology.org/2025.acl-long.6.pdf), [RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.252.pdf))
> A benchmark dataset used for evaluating the quality of text summarization.

**TL;DR dataset** (2 papers: [A Common Pitfall of Margin-based Language Model Alignment: Gradient Entanglement](https://proceedings.iclr.cc/paper_files/paper/2025/file/10272bfd0371ef960ec557ed6c866058-Paper-Conference.pdf), [Towards Cost-Effective Reward Guided Text Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rashid25a/rashid25a.pdf))
> A dataset consisting of Reddit posts and their summaries, used in this paper to evaluate the training dynamics of various preference optimization algorithms. The full name is 'Too Long; Didn't Read'.

**Reddit TL;DR** (4 papers: [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf), [The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25c/miao25c.pdf), [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf), [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf))
> A summarization dataset consisting of Reddit posts and several corresponding short summaries, which have been judged for quality and informativeness by human evaluators.

**Reddit TL;DR dataset** (2 papers: [Variational Best-of-N Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/402542c2341e5d2eadc1dd0891275901-Paper-Conference.pdf), [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf))
> A dataset consisting of Reddit posts and their human-written summaries (Stiennon et al., 2020), used for training and evaluating summarization models.

**Reddit summarization dataset** (1 paper: [InfAlign: Inference-aware language model alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balashankar25a/balashankar25a.pdf))
> A dataset also known as the TL;DR dataset, containing Reddit posts and their corresponding human-written summaries, used for training and evaluating text summarization models.

**TL;DR summarization** (1 paper: [Symmetric Reinforcement Learning Loss for Robust Learning on Diverse Tasks and Model Scales](https://raw.githubusercontent.com/mlresearch/v267/main/assets/byun25a/byun25a.pdf))
> Summarization task requiring models to generate concise summaries of Reddit posts, used here as an RLHF benchmark with a learned reward model.

**TL;DR comparison data** (1 paper: [GRAM: A Generative Foundation Reward Model for Reward Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ad/wang25ad.pdf))
> A dataset composed of summarization response pairs used for domain-specific pre-training of a reward model.

**Reddit TL;DR Summarization** (1 paper: [RoSTE: An Efficient Quantization-Aware Supervised Fine-Tuning Approach for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25n/wei25n.pdf))
> A summarization benchmark based on the Reddit TL;DR dataset used to evaluate fine-tuned LLMs on generating concise summaries of posts.

**TLDR** (2 papers: [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf), [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf))
> A dataset derived from Reddit for training and evaluating automatic text summarization models.

## Relationships

### → Reddit TL;DR
- **Text summarization** (behavioral indicator): *measured_by*, 22 papers
  > Summarization Task. SFT dataset: Reddit TL;DR dataset is used, comprising 123, 169 Reddit posts along with human-written summaries. (Section 5)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
  - [CPPO: Continual Learning for Reinforcement Learning with Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf)
  - [Privately Aligning Language Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/477b39bfb9db99f60914dbfed5f23eb2-Paper-Conference.pdf)
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
  - [Self-Improving Robust Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bc795afae289ed465a65a3b4b1f4eb7-Paper-Conference.pdf)
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
  - [Correcting the Mythos of KL-Regularization: Direct Alignment without Overoptimization via Chi-Squared Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e785d64baa2cde06c69d9b7a14636ef2-Paper-Conference.pdf)
  - [Learn Your Reference Model for Real Good Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf)
  - [Variational Best-of-N Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/402542c2341e5d2eadc1dd0891275901-Paper-Conference.pdf)
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
  - [LiPO: Listwise Preference Optimization through Learning-to-Rank](https://aclanthology.org/2025.naacl-long.121.pdf)
  - [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf)
  - [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf)
  - [Optimal Transport-Based Token Weighting scheme for Enhanced Preference Optimization](https://aclanthology.org/2025.acl-long.1035.pdf)
  - [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf)
  - [Towards Cost-Effective Reward Guided Text Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rashid25a/rashid25a.pdf)
  - [Design Considerations in Offline Preference-based RL](https://raw.githubusercontent.com/mlresearch/v267/main/assets/agarwal25a/agarwal25a.pdf)
  - [Symmetric Reinforcement Learning Loss for Robust Learning on Diverse Tasks and Model Scales](https://raw.githubusercontent.com/mlresearch/v267/main/assets/byun25a/byun25a.pdf)
  - [RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.252.pdf)
- **Alignment** (construct): *measured_by*, 4 papers
  > In the experiments, we simulate the soft preference labels with AI feedback from LLMs [4, 24] and show that soft preference labels and weighted geometric averaging achieve consistent improvement to the baselines on popular benchmarks for the alignment research literature, such as Reddit TL;DR [49]... (Section 1).
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
  - [RLTHF: Targeted Human Feedback for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25c/xu25c.pdf)
- **Summary quality** (construct): *measured_by*, 1 paper
  > for the summarization quality task, we use Reddit posts from TL;DR dataset (Stiennon et al., 2020) and train uncalibrated and calibrated reward models on the train split. (Section 5.1)
  - [InfAlign: Inference-aware language model alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balashankar25a/balashankar25a.pdf)
- **Abstractive summarization** (behavioral indicator): *measured_by*, 1 paper
  > “It contains user-generated posts paired with concise summaries, providing a challenging benchmark for abstractive summarization tasks.”
  - [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > To evaluate the generalization ability of the aligned models on out-of-distribution data, we fine-tune the models using only posts from the relationship and relationship advice subreddits of the Reddit TL;DR (Stiennon et al., 2020) dataset. (Section 6)
  - [Variational Best-of-N Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/402542c2341e5d2eadc1dd0891275901-Paper-Conference.pdf)
