# Truthfulness
**Type:** Construct  
**Supporting papers:** 18  
**Also known as:** Response truthfulness, Skill-specific truthfulness  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage treats truthfulness as output-level factual accuracy: models are expected to produce statements aligned with reality and avoid false, misleading, hallucinated, or unsupported content, often especially on questions built around common misconceptions. Many papers phrase it as a latent tendency or propensity of the model, while others describe it as the degree to which responses adhere to real-world facts. Smaller lines of work narrow it to specific settings, such as response truthfulness in RAG, defined as the correctness of generated claims themselves, or to social interaction, where it means accurately conveying information received from the surrounding environment. A smaller line of work also treats it as an internal, skill-specific encoding rather than a universal property, arguing that models encode multiple distinct notions of truth.

**Space of facets.** When papers decompose the construct, several distinctions appear. One RAG paper separates response truthfulness from attribution groundedness, with the former about claim correctness and the latter about citation correctness, while another paper argues truthfulness is multifaceted and skill-specific rather than universal. Across papers, truthfulness is also described through adjacent terms such as correctness, factual accuracy, factual consistency, and avoidance of hallucinations or misinformation. In neighboring constructs, papers contrast it with honesty, where honesty is stating what the model believes and truthfulness is stating what is objectively true, and they place it inside broader trustworthiness frameworks, sometimes alongside robustness and other evaluation dimensions.

**Space of measurement.** Operationalization is benchmark-heavy: truthfulness is linked to 11 measurement instruments and 3 behavioral indicators. The most common instrument is TruthfulQA, used to test whether models identify true claims or avoid reproducing falsehoods, including adversarial questions about misconceptions, and in some papers MC1 variants are reported; the next most common is LLM-as-a-judge, where GPT-4 or a learned judge scores truthfulness, sometimes together with informativeness, from model responses given questions and gold labels. Papers also use the Open LLM Leaderboard, AraEval, and CodeMixBench, alongside several other instruments such as human ratings and other domain or language specific suites. These measurements mainly score output-level factual correctness, falsehood reproduction, or whether a model responds truthfully rather than misleadingly, so they match the dominant output-focused definitions more directly than the smaller internal, skill-specific framing.

**Links.** Truthfulness is linked to 10 constructs and 3 behavioral indicators. Papers most often connect it to human preference alignment, informativeness, sycophancy, and hallucination, with several also locating it inside broader trustworthiness frameworks. Several papers claim a causal relationship from human preference alignment to truthfulness, but the reported direction differs, from generating more truthful outputs to truthfulness decreasing by 25%; papers also claim a causal relationship from hallucination to truthfulness, describing hallucinations or misleading content as leading to lack of truthfulness. It is further reported as related to informativeness and sycophancy, with truthful answers sometimes less informative and agreeable outputs occurring at the expense of truthfulness. Other papers claim additional causal links from alignment-oriented or uncertainty-oriented approaches, and one paper claims a causal relationship from truthfulness to a utility trade-off; no paper reports a correlational link.

## Sources

**Truthfulness** (12 papers: [LLäMmlein: Transparent, Compact and Competitive German-Only Language Models from Scratch](https://aclanthology.org/2025.acl-long.111.pdf), [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf), [MiniLLM: Knowledge Distillation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/8ac015d409635f196f9e3e9dcfb9a94e-Paper-Conference.pdf), [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf), [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf), [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf), [Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf), [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf), [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf), [Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.44.pdf), [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf))
> The degree to which the model avoids generating false or misleading information, particularly when faced with questions designed to elicit misconceptions.

**Response truthfulness** (1 paper: [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf))
> A quality of an LLM's generated claims in a RAG context, specifically focusing on the correctness of the claims themselves.

**Skill-specific truthfulness** (1 paper: [LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations](https://proceedings.iclr.cc/paper_files/paper/2025/file/a712d461e57201efe35d429a6f1731c1-Paper-Conference.pdf))
> The property that a model's internal encoding of truthfulness is not universal, but rather multifaceted and dependent on the specific cognitive skill required by a task, such as factual retrieval or common-sense reasoning.

## Relationships

### Truthfulness →
- **TruthfulQA** (measurement instrument): *measured_by*, 48 papers
  > The dataset evaluates a model’s ability to not generate false answers learnt from imitation learning on text. (Section 3)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf)
  - [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf)
  - [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
  - [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf)
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf)
  - [LACIE: Listener-Aware Finetuning for Calibration in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8eaf3bcdc105423a972ed90eb07217-Paper-Conference.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [Exploiting LLM Quantization](https://proceedings.neurips.cc/paper_files/paper/2024/file/496720b3c860111b95ac8634349dcc88-Paper-Conference.pdf)
  - [On Giant's Shoulders: Effortless Weak to Strong by Dynamic Logits Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/34ec1286b2ccd4794c5ca4ad078b7150-Paper-Conference.pdf)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
  - [A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Towards Scalable Exact Machine Unlearning Using Parameter-Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/d33b741600f100b31256c70a46f66ec9-Paper-Conference.pdf)
  - [Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
  - [Iterative Nash Policy Optimization: Aligning LLMs with General Preferences via No-Regret Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/4eef032250ac525903063cd760cb0480-Paper-Conference.pdf)
  - [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf)
  - [Catastrophic Failure of LLM Unlearning via Quantization](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba79fb5c4fe70050752f20c90c5f07ca-Paper-Conference.pdf)
  - [Causally Motivated Sycophancy Mitigation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a52b0d191b619477cc798d544f4f0e4b-Paper-Conference.pdf)
  - [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf)
  - [Probe-Free Low-Rank Activation Intervention](https://aclanthology.org/2025.naacl-long.143.pdf)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf)
  - [SPRI: Aligning Large Language Models with Context-Situated Principles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhan25a/zhan25a.pdf)
  - [Tokenized Bandit for LLM Decoding and Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25h/shin25h.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
  - [Direct Density Ratio Optimization: A Statistically Consistent Approach to Aligning Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/higuchi25a/higuchi25a.pdf)
  - [MoH: Multi-Head Attention as Mixture-of-Head Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25l/jin25l.pdf)
  - [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf)
  - [What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf)
  - [Model Unlearning via Sparse Autoencoder Subspace Guided Projections](https://aclanthology.org/2025.emnlp-main.1348.pdf)
  - [SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.112.pdf)
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)
  - [Simple Yet Effective: An Information-Theoretic Approach to Multi-LLM Uncertainty Quantification](https://aclanthology.org/2025.emnlp-main.1551.pdf)
  - [DSVD: Dynamic Self-Verify Decoding for Faithful Generation in Large Language Models](https://aclanthology.org/2025.emnlp-main.1050.pdf)
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 3 papers
  > We prompt GPT-4 to evaluate the informativeness (Info) and truthfulness (True) of model responses given the question and the gold labels. (Section 6).
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Open LLM Leaderboard** (measurement instrument): *measured_by*, 2 papers
  > These benchmarks give us a glimpse into model knowledge, reasoning, and truthfulness. (Section 4)
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **UltraFeedback** (measurement instrument): *measured_by*, 1 paper
  > UltraFeedback [7]: a multi-aspect alignment dataset with 64K prompts with preferences obtained from GPT-4, including "Instruction following", "Honest", "Truthful", and "Helpful" objectives (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **Utility preservation** (construct): *causes*, 1 paper
  > Additionally, increase in truthfulness negatively impacts utility (-15%). (Section 1)
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf)
- **Human annotation study** (measurement instrument): *measured_by*, 1 paper
  > For each episode, three graduate students annotate the AI agent’s truthfulness using both fine-grained (distinguishing between Concealment and Equivocation) and coarse-grained (using the Partial Lie category) metrics. (Section 4.2)
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > We perform a manual evaluation of 400 responses for truthfulness and informativeness, with 100 questions and three responses from four models... (Section 3.2.1)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
- **SimpleQA** (measurement instrument): *measured_by*, 1 paper
  > We take SimpleQA (Wei et al., 2024b) for truthfulness... (Section 3.1)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **FINTRUST** (measurement instrument): *measured_by*, 1 paper
  > we curate 15, 680 instances to evaluate LLM trustworthiness in the financial domain. We ... incorporate seven core dimensions: Truthfulness, Safety, Fairness, Robustness, Privacy, Transparency, and Knowledge Discovery. (Section 2)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **CodeMixBench** (measurement instrument): *measured_by*, 1 paper
  > we introduce the CodeMixBench, a code-mixing evaluation benchmark including eight tasks–three for evaluating LLMs (knowledge reasoning, mathematical reasoning, and truthfulness) and five for traditional NLP tasks (LID, POS, NER, SA, and MT). (§1)
  - [CodeMixBench: Evaluating Code-Mixing Capabilities of LLMs Across 18 Languages](https://aclanthology.org/2025.emnlp-main.109.pdf)
- **AraEval** (measurement instrument): *measured_by*, 1 paper
  > In this paper, we present AraEval, a pioneering and comprehensive evaluation suite speciﬁcally developed to assess the advanced knowledge, reasoning, truthfulness, and instruction-following capabilities of foundation models in the Arabic context. (Abstract)
  - [AraEval: An Arabic Multi-Task Evaluation Suite for Large Language Models](https://aclanthology.org/2025.emnlp-main.1679.pdf)
- **PLLuM-Align** (measurement instrument): *measured_by*, 1 paper
  > For scalar multi-attribute rating, annotators evaluated each response on a 5-point Likert scale across seven criteria: i) truthfulness, (ii) linguistic correctness, (iii) safety, (iv) fairness, (v) conciseness, (vi) coherence & reasoning, as well as vii) helpfulness & instruction-following.
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)

### → Truthfulness
- **Hallucination** (behavioral indicator): *causes*, 4 papers
  > LLMs are prone to hallucinations [53] and misunderstandings of text, especially in specific technical domains, that can lead to a lack of truthfulness from the model [35].
  - [CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence](https://proceedings.neurips.cc/paper_files/paper/2024/file/5acd3c628aa1819fbf07c39ef73e7285-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d9dcd4ebef57f1839d871fe7d891e91-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Human preference alignment** (construct): *causes*, 2 papers
  > the effects on other trustworthiness aspects are negative: ... truthfulness decreases by 25%... (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > Reinforcement Learning from Human Feedback (RLHF) is a technique that can be used to align an agent — such as a Large Language Model (LLM) — to human preferences and lead to more truthful, more helpful, less harmful and more preferred outputs [29]. (Introduction)
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
- **Uncertainty quantification** (construct): *causes*, 1 paper
  > Uncertainty quantification (UQ) is a prominent approach for eliciting truthful answers from large language models (LLMs).
  - [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf)

### Associated with
- **Trustworthiness** (construct), 2 papers
  > Specifically, we divide model trustworthiness into robustness and truthfulness.
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Informativeness** (construct), 2 papers
  > This finding highlights the critical importance of assessing informativeness metrics specifically for non-instruction-tuned models, as failing to do so may result in misleadingly high truthfulness scores. (Section 5)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Sycophancy** (construct), 2 papers
  > Sycophancy causes models to produce answers that cater to user expectations rather than providing truthful responses. (Abstract)
  - [Self-Augmented Preference Alignment for Sycophancy Reduction in LLMs](https://aclanthology.org/2025.emnlp-main.625.pdf)
  - [Causally Motivated Sycophancy Mitigation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a52b0d191b619477cc798d544f4f0e4b-Paper-Conference.pdf)
- **Honesty** (construct), 1 paper
  > According to Evans et al. (2021); Park et al. (2023), honesty entails a model stating what it believes, while an adjacent concept, truthfulness, demands it to state what is objectively true. (Section 5.1)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **Robustness** (construct), 1 paper
  > Truthfulness involves a dual consideration of hallucination and robustness. (Section 2.1)
  - [MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d9dcd4ebef57f1839d871fe7d891e91-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Abstention** (behavioral indicator), 1 paper
  > It evaluates whether models can provide factually accurate responses, or appropriately abstain when uncertain. (Section 2.1)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **Open-ended question answering** (behavioral indicator), 1 paper
  > We examine CRITIC across diverse tasks: free-form question answering concentrates on truthfulness related to open-ended general factual knowledge (Section 4)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Controllability** (construct), 1 paper
  > GPT-4o shows a 40% increase in truthfulness when prompted, and this pattern is observed across most models, with the stronger models exhibiting more pronounced shifts toward truthfulness. (Section 5.3)
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf)
