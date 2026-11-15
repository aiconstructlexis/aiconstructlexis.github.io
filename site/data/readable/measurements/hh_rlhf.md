# HH-RLHF
**Type:** Measurement instrument  
**Supporting papers:** 98  
**Also known as:** Anthropic-RLHF-HH, Anthropic/HH-RLHF, HH-RLHF*, hh-rlhf, Anthropic HH, ANTHROPIC HH, Anthropic-HH, HH-rlhf, Anthropic HH dataset, Anthropic harmless data, HH, Anthropic Helpfulness and Harmlessness (HH), Helpful & Harmless, Anthropic Helpfulness-Harmlessness dataset, Helpful-Harmless dataset, Anthropic HH (RLHF), Anthropic HHH, Anthropic Helpful and Harmless, HH dataset, Anthropic-HH dataset  

## State of the Field

**What it is.** Most commonly described as Anthropic's Helpful and Harmless preference dataset for human-assistant dialogue, it contains prompts or conversation histories with two candidate responses and a human-preferred choice, often framed as chosen-rejected pairs annotated for helpfulness and harmlessness. Papers variously describe it as multi-turn dialogues, human-AI conversation pairs, or single-step human-assistant interactions, and reported sizes include 161K training and 8.55K test pairs, approximately 170K dialogues or chosen-rejected pairs, and more than 160,000 preference comparisons. Several papers treat it as having separate helpfulness and harmlessness subsets or focus only on the helpfulness portion, and one paper defines a 150-instance HH-RLHF* subset for out-of-domain evaluation. Some papers instead describe Anthropic HHH with helpful, harmless, and honest comparisons, sometimes using it as a source of harmful prompts and responses.

**What it is claimed to measure.** Across papers, measurement claims converge most strongly on helpfulness and harmlessness, often with separate helpful and harmless splits. It is linked to 9 constructs and 1 behavioral indicator: beyond helpfulness and harmlessness, papers use it to measure alignment and human preference alignment, and the sole linked behavioral indicator is dialogue generation. The construct claims spread beyond these dominant uses to 5 other constructs.

**Space of uses.** The prevailing usage is as a headline benchmark and training or evaluation source for alignment methods, with some papers calling it a commonly adopted or widely used alignment dataset. No measurement instrument is linked to it, though papers often use it alongside SHP, UltraFeedback, AlpacaEval, SafeRLHF, and TL;DR. Authors use the full dataset, validation or test splits, or smaller subsets, sometimes converting multi-turn dialogues into single-turn format, sampling prompts for external reward-model and pairwise GPT-4 scoring, or using it as a source of prompts for other evaluations.

**Concerns raised.** Concerns appear in a smaller line of work that audits the dataset. One study reports annotation problems, stating that "over 40% of the answers in the sampled dataset is incorrect," and other descriptions note toxic content in the dataset and use it as a source of harmful prompts and responses.

## Sources

**hh-rlhf** (9 papers: [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf), [Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment](https://aclanthology.org/2025.naacl-long.472.pdf), [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf), [Diff-eRank: A Novel Rank-Based Metric for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/45cc967d7899616f51993b7b363d35b5-Paper-Conference.pdf), [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf), [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf), [Online Iterative Reinforcement Learning from Human Feedback with General Preference Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf), [Preference Learning Algorithms Do Not Learn Preference Rankings](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8ce770a6b25e603fbff4a37f9e31edc-Paper-Conference.pdf), [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf))
> The helpfulness and harmlessness dataset from Anthropic (Bai et al., 2022a), containing human preference comparisons between model responses, used here to analyze what behaviors are incentivized.

**Anthropic/HH-RLHF** (1 paper: [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf))
> Dataset of human-AI conversation pairs used to train and evaluate helpful and harmless behavior in language models, containing preference-labeled responses for alignment evaluation.

**HH-RLHF** (12 papers: [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf), [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf), [Compositional Preference Models for Aligning LMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/8fd10360ac9de462ffd36155d87ee999-Paper-Conference.pdf), [Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/092359ce5cf60a80e882378944bf1be4-Paper-Conference.pdf), [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf), [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf), [Constrained Decoding with Speculative Lookaheads](https://aclanthology.org/2025.naacl-long.239.pdf), [BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.443.pdf), [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf), [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf), [Reward-Shifted Speculative Sampling Is An Efficient Test-Time Weak-to-Strong Aligner](https://aclanthology.org/2025.emnlp-main.578.pdf), [Wait, that's not an option: LLMs Robustness with Incorrect Multiple-Choice Options](https://aclanthology.org/2025.acl-long.75.pdf))
> The Helpful and Harmless dataset from Anthropic, a benchmark for alignment that consists of prompts each with two responses, where one is preferred by human annotators based on helpfulness and harmlessness.

**HH-RLHF*** (1 paper: [Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf))
> A 150-instance subset of the HH-RLHF dataset used for out-of-domain evaluation to test the model's ability to generalize its preference scoring to unseen prompts.

**Anthropic-RLHF-HH** (1 paper: [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf))
> A large-scale dataset of human feedback on AI assistant responses, containing preference data for both helpful and harmless conversations.

**Anthropic-HH** (3 papers: [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf), [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf), [Understanding Impact of Human Feedback via Influence Functions](https://aclanthology.org/2025.acl-long.1333.pdf))
> A preference dataset for evaluating helpfulness and harmlessness, consisting of prompts with two model-generated continuations ranked by human labelers.

**Anthropic HH** (1 paper: [Regressing the Relative Future: Efficient Policy Optimization for Multi-turn RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/186094ef879dcbd5ef6879782916c309-Paper-Conference.pdf))
> The Anthropic Helpful and Harmless dataset, a collection of multi-turn dialogues used to train and evaluate models on their ability to be helpful while avoiding harmful responses.

**ANTHROPIC HH** (1 paper: [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf))
> The Anthropic Helpful and Harmless dataset, which contains pairs of multi-turn dialogues designed to evaluate a model's ability to be both helpful and safe.

**HH-rlhf** (1 paper: [3D-Properties: Identifying Challenges in DPO and Charting a Path Forward](https://proceedings.iclr.cc/paper_files/paper/2025/file/c080f9fb3658511bc4f063c5794ef706-Paper-Conference.pdf))
> A preference dataset used for training and evaluation in the comparison between DPO and reward-model training.

**Anthropic HH dataset** (2 papers: [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf), [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf))
> The test split of the Anthropic Helpful and Harmless (HH) dataset, used to evaluate model alignment by assessing responses in single-step human-assistant interactions.

**Anthropic HHH** (2 papers: [Failures to Find Transferable Image Jailbreaks Between Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e3daaeca6be8579573f69082b2dd58b-Paper-Conference.pdf), [Whose Boat Does it Float? Improving Personalization in Preference Tuning via Inferred User Personas](https://aclanthology.org/2025.acl-long.168.pdf))
> A dataset of human preference comparisons over helpful, harmless, and honest AI responses, used here as a source of harmful prompts and responses.

**Anthropic harmless data** (1 paper: [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf))
> A dataset of human-AI conversations used as a source of prompts for evaluating alignment on conversational tasks.

**HH** (1 paper: [Entropy-based Activation Function Optimization: A Method on Searching Better Activation Functions](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5cbee19280e1fd9d9dba8c1febf48bd-Paper-Conference.pdf))
> The Anthropic Helpful and Harmless dataset, a collection of human preference data comparing model responses to evaluate and align language models.

**Anthropic Helpfulness and Harmlessness (HH)** (1 paper: [Preference learning made easy: Everything should be understood through win rate](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bm/zhang25bm.pdf))
> A dataset of human preference comparisons between model responses, focused on the criteria of being helpful and harmless.

**Helpful & Harmless** (1 paper: [Right Now, Wrong Then: Non-Stationary Direct Preference Optimization under Preference Drift](https://raw.githubusercontent.com/mlresearch/v267/main/assets/son25a/son25a.pdf))
> A preference dataset used to construct non-stationary preference data for LLM fine-tuning experiments.

**Anthropic Helpfulness-Harmlessness dataset** (1 paper: [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf))
> A dataset containing conversations where human labelers compare two model responses based on helpfulness and harmlessness criteria.

**Helpful-Harmless dataset** (1 paper: [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf))
> A large-scale dataset of human preference labels used for training and evaluating models on helpfulness and harmlessness.

**Anthropic Helpful and Harmless** (1 paper: [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf))
> A benchmark dataset for evaluating the helpfulness and harmlessness of conversational agents, containing dialogues designed to elicit these qualities.

**HH dataset** (1 paper: [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf))
> Human preference dataset by Anthropic containing paired model responses annotated for helpfulness and harmlessness, used to train models via learning from human feedback.

**Anthropic-HH dataset** (1 paper: [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf))
> The Anthropic Helpful and Harmless dataset, containing human preference data for training models to be helpful and harmless in dialogue.

## Relationships

### → HH-RLHF
- **Helpfulness** (construct): *measured_by*, 28 papers
  > Human preference data: Anthropic-RLHF-HH dataset is used, which is a large-scale collection of human feedback on AI assistant responses, including both helpful and harmless data (Bai et al., 2022b). (Section 5)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
  - [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf)
  - [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf)
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
  - [Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ebfb4ec1926fc6409df3bcf7ce957e8-Paper-Conference.pdf)
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [On-the-fly Preference Alignment via Principle-Guided Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcd1d7a599f33c06f06615429793c69b-Paper-Conference.pdf)
  - [Learn Your Reference Model for Real Good Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf)
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
  - [Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/092359ce5cf60a80e882378944bf1be4-Paper-Conference.pdf)
  - [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf)
  - [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf)
  - [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf)
  - [Gradient-Adaptive Policy Optimization: Towards Multi-Objective Alignment of Large Language Models](https://aclanthology.org/2025.acl-long.549.pdf)
  - [DeAL: Decoding-time Alignment for Large Language Models](https://aclanthology.org/2025.acl-long.1274.pdf)
  - [Tokenized Bandit for LLM Decoding and Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25h/shin25h.pdf)
  - [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
  - [TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nuti25a/nuti25a.pdf)
  - [Reward-Shifted Speculative Sampling Is An Efficient Test-Time Weak-to-Strong Aligner](https://aclanthology.org/2025.emnlp-main.578.pdf)
- **Harmlessness** (construct): *measured_by*, 18 papers
  > The HH contains several subsplits, broadly for measuring ‘helpfulness’ and ‘harmlessness’ of a chatbot. (Section 4, Datasets)
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
  - [Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ebfb4ec1926fc6409df3bcf7ce957e8-Paper-Conference.pdf)
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [On-the-fly Preference Alignment via Principle-Guided Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcd1d7a599f33c06f06615429793c69b-Paper-Conference.pdf)
  - [Learn Your Reference Model for Real Good Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf)
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
  - [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf)
  - [Gradient-Adaptive Policy Optimization: Towards Multi-Objective Alignment of Large Language Models](https://aclanthology.org/2025.acl-long.549.pdf)
  - [DeAL: Decoding-time Alignment for Large Language Models](https://aclanthology.org/2025.acl-long.1274.pdf)
  - [Tokenized Bandit for LLM Decoding and Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25h/shin25h.pdf)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
  - [TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nuti25a/nuti25a.pdf)
- **Dialogue generation** (behavioral indicator): *measured_by*, 9 papers
  > We also evaluate on the validation split of the Anthropic’s Helpful and Harmless (HH) dataset (Ganguli et al., 2022; Bai et al., 2022a), where where each example comprises a pair of conversations between a human and a large language model, with one of the two conversations preferred by a human.
  - [Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
  - [MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ddab70bf41ffe5d423840644d3357f4-Paper-Conference.pdf)
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
  - [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf)
  - [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf)
  - [BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling](https://proceedings.neurips.cc/paper_files/paper/2024/file/056521a35eacd9d2127b66a7d3c499c5-Paper-Conference.pdf)
- **Alignment** (construct): *measured_by*, 3 papers
  > To evaluate the performance, we use the Anthropic HH-RLHF (Helpful and Harmless) dataset (Bai et al., 2022a), which is the most commonly used dataset for alignment. (Section 3.2)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)
  - [RLTHF: Targeted Human Feedback for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25c/xu25c.pdf)
- **Humor** (construct): *measured_by*, 2 papers
  > HH-RLHF [3]: a large-scale dataset ... We follow Yang et al. [35] and use open-sourced reward models on three objectives: "Harmless", "Helpful", and "Humor" to score the responses (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf)
- **Safety alignment** (construct): *measured_by*, 2 papers
  > To further evaluate the effectiveness of SimPER in safety alignment on Pythia-2.8B following (Rafailov et al., 2024), we use the Anthropic-HH dataset.
  - [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
  - [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)
- **Human preference alignment** (construct): *measured_by*, 2 papers
  > Comparison in terms of the trade-off between Alignment (accuracy) and Diversity (entropy) on the Anthropic HH dataset. (Table 1)
  - [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf)
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
- **Safety** (construct): *measured_by*, 1 paper
  > we applied our approach to HH-RLHF (Anthropic, 2022), a commonly used preference dataset for safety alignment. (Section 5.2)
  - [RuleAdapter: Dynamic Rules for training Safety Reward Models in RLHF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25o/li25o.pdf)
- **Reward overoptimization** (construct): *measured_by*, 1 paper
  > Additional plots illustrating similar over-optimization trends for Direct Alignment Algorithms on the Gemma2-2b model [61] and the Anthropic Helpfulness-Harmlessness dataset [5] are provided in Appendix F (Section 3)
  - [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf)
- **Memorization** (construct): *measured_by*, 1 paper
  > Finally, we explore RLHF memorization on different task domains by studying memorization on natural language datasets, LIMA (Zhou et al., 2024) and Anthropic HH (Bai et al., 2022). (Section 5.5)
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)
