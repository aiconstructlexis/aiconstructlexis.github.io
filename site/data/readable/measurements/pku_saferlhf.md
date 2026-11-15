# PKU-SafeRLHF
**Type:** Measurement instrument  
**Supporting papers:** 22  
**Also known as:** PKU SafeRLHF, SafeRLHF, Safe-RLHF  

## State of the Field

**What it is.** Most commonly, papers treat PKU-SafeRLHF, also written SafeRLHF or Safe-RLHF, as a human-annotated preference dataset or public benchmark for safety alignment. Definitions usually describe prompt or instruction-response comparisons with paired responses and labels for helpfulness and harmlessness or safety, and some papers further describe safe and unsafe response pairs, conversation comparisons, and safety-focused coverage such as insults, immorality, crime, emotional harm, and privacy. A smaller line emphasizes it as a harmful-query or red-teaming test set for out-of-distribution evaluation, and papers describe its overall scale differently.

**What it is claimed to measure.** Across papers, the dominant use is to measure harmlessness and helpfulness: papers link it to five constructs and no behavioral indicators, with harmlessness and helpfulness appearing most often. Smaller lines of work use it to measure generalization or safety, and one paper relates PKU-SafeRLHF to safety alignment rather than treating it as a direct measure. Overall, the measurement claims are concentrated on harmlessness and helpfulness rather than evenly spread across the linked constructs.

**Space of uses.** Papers usually use it in training as well as evaluation, including alignment tuning, reward-model training, harmful-query or red-teaming evaluation, and benchmark test sets for generative judges. No measurement instrument is linked to it, though papers often place it alongside HH-RLHF, BigBench-HHH, UltraChat, CNN Dailymail, and Iterative-Prompt in broader experimental setups. Some also describe fixed train-test splits, comparisons against gold reward or reference models, or multi-objective settings that maximize helpfulness while imposing a harmlessness threshold.

## Sources

**PKU-SafeRLHF** (6 papers: [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf), [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf), [Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf), [Gradient-Adaptive Policy Optimization: Towards Multi-Objective Alignment of Large Language Models](https://aclanthology.org/2025.acl-long.549.pdf), [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf), [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf))
> A dataset used for out-of-distribution evaluation of model performance on harmful queries.

**PKU SafeRLHF** (1 paper: [Unmasking and Improving Data Credibility: A Study with Datasets for Training Harmless Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c3837ae3d17a91b08bf5cc19280e7fd2-Paper-Conference.pdf))
> A dataset of over 300k instances with prompt-response pairs and safety labels, derived from human preferences, used for reinforcement learning with human feedback in safety alignment.

**SafeRLHF** (3 papers: [BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.443.pdf), [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf), [RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.252.pdf))
> Human-annotated pairwise preference dataset that independently ranks responses for helpfulness and harmlessness, used for alignment tuning and evaluation.

**Safe-RLHF** (1 paper: [The Crucial Role of Samplers in Online Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/62133b95efaa6f10a5395eb10ca087cd-Paper-Conference.pdf))
> A dataset used for LM alignment experiments in which trained models are evaluated against a gold reward model and a reference model.

## Relationships

### → PKU-SafeRLHF
- **Harmlessness** (construct): *measured_by*, 8 papers
  > Harmful evaluation on PKU-SafeRLHF. (Figure 3a)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
  - [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf)
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
  - [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf)
  - [Gradient-Adaptive Policy Optimization: Towards Multi-Objective Alignment of Large Language Models](https://aclanthology.org/2025.acl-long.549.pdf)
  - [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf)
  - [RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.252.pdf)
- **Helpfulness** (construct): *measured_by*, 5 papers
  > PKU-SafeRLHF provides both paired helpfulness preference rankings and binary safety labels.
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
  - [Gradient-Adaptive Policy Optimization: Towards Multi-Objective Alignment of Large Language Models](https://aclanthology.org/2025.acl-long.549.pdf)
  - [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf)
  - [RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.252.pdf)
  - [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > In this section, we will evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU), Reward3, UltraFeedback(UltraF), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
- **Safety** (construct): *measured_by*, 1 paper
  > We evaluate model safety on the PKU-SafeRLHF and BigBench-HHH datasets. (Section 4.1)
  - [Governance in Motion: Co-evolution of Constitutions and AI models for Scalable Safety](https://aclanthology.org/2025.emnlp-main.869.pdf)

### Associated with
- **Safety alignment** (construct), 1 paper
  > Using the large-scale annotation data, we further train severity-sensitive moderation for the risk control of LLMs and safety-centric RLHF algorithms for the safety alignment of LLMs. (Abstract)
  - [PKU-SafeRLHF: Towards Multi-Level Safety Alignment for LLMs with Human Preference](https://aclanthology.org/2025.acl-long.1544.pdf)
