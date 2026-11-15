# Harmlessness
**Type:** Construct  
**Supporting papers:** 164  
**Also known as:** Harmfulness, Harm  

## State of the Field

**Space of definitions.** Most definitions treat harmlessness as a latent safety-oriented tendency or property of a model, or of its responses, to avoid generating unsafe, harmful, unethical, toxic, offensive, or dangerous content, often even under harmful or adversarial prompts. Across papers, the reference standard is broad but similar: responses should not violate ethical, legal, or social norms, and should avoid content such as illegal advice, discrimination, misinformation, hate, self-harm, or dangerous activities. Smaller strands state the construct in the inverse as harmfulness, the disposition to generate ethically problematic or privacy-revealing content, and one paper narrows harm to eating-disorder-related promotion, so the main differences are inverse wording, model versus response focus, and scope.

**Space of facets.** Most commonly, papers place harmlessness inside broader alignment bundles, especially with helpfulness and often honesty, sometimes under the labels 3H or HHH, and sometimes as one objective in multi-objective alignment alongside humor or other user-alignment skills. Several papers explicitly separate it from helpfulness by evaluating them on independent axes and noting that an answer can be helpful but unsafe. Some work treats harmlessness as close to safety, even using the terms interchangeably, while dataset-focused and auditing papers describe it as spanning multiple dimensions or considerations and note that its interpretation can be vague.

**Space of measurement.** Operationalization is broad: papers link harmlessness to 28 measurement instruments and 4 behavioral indicators. The most common instruments are HH-RLHF, LLM-as-a-judge, PKU-SafeRLHF, AdvBench, and Human evaluation. In practice, this means preference datasets with helpfulness and harmlessness annotations or subsplits, LLM judges that score responses on scales or compare response pairs for harmlessness and related criteria, human pairwise judgments of which response is more harmless, and harmful-query benchmarks that are often paired with safety classifiers or attack success rate. The behavioral indicators center on harmful content generation, harmful-request refusal, refusal, and safe response generation, so papers often operationalize harmlessness through whether models avoid harmful outputs, though some measures focus more specifically on toxicity or classifier-detected harmfulness.

**Links.** Among linked constructs, papers most often connect harmlessness to helpfulness: many describe the pair as competing objectives, a trade-off, or a negative correlation, and one study reports negative correlations on two alignment datasets. Harmlessness is also related to human preference alignment, and several papers claim a causal relationship from safety alignment to harmlessness, while a smaller set claims a causal relationship from alignment to harmlessness. A few papers further relate it to humor. Beyond these, papers connect it to several other constructs and to 4 behavioral indicators tied to refusal and harmful or safe output generation.

## Sources

**Harmlessness** (39 papers: [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf), [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf), [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf), [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf), [Constrained Decoding with Speculative Lookaheads](https://aclanthology.org/2025.naacl-long.239.pdf), [Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment](https://aclanthology.org/2025.naacl-long.472.pdf), [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf), [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf), [FiNE: Filtering and Improving Noisy Data Elaborately with Large Language Models](https://aclanthology.org/2025.naacl-long.437.pdf), [AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.333.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [The TIP of the Iceberg: Revealing a Hidden Class of Task-in-Prompt Adversarial Attacks on LLMs](https://aclanthology.org/2025.acl-long.334.pdf), [InfAlign: Inference-aware language model alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balashankar25a/balashankar25a.pdf), [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://aclanthology.org/2025.emnlp-main.167.pdf), [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf), [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf), [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf), [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf), [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf), [Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf), [Distributional Preference Learning: Understanding and Accounting for Hidden Context in RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/7423902b5534e2b267438c85444a54b1-Paper-Conference.pdf), [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf), [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf), [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf), [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf), [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf), [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf), [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf), [Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL](https://proceedings.iclr.cc/paper_files/paper/2024/file/b84b9d1fe05c5e74d8f9466f063327a5-Paper-Conference.pdf), [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf), [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bd09a559a8c8e230697107b0f353d39-Paper-Conference.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf), [Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/9178ece87f0a5d6558f49f43ec1e8a1a-Paper-Conference.pdf), [Training Socially Aligned Language Models on Simulated Social Interactions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d763b4a2dde0ae7b77498516ce9f439e-Paper-Conference.pdf), [Universal Jailbreak Backdoors from Poisoned Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/d1e63f4027efc7c44bfc253eafc15a58-Paper-Conference.pdf), [Unmasking and Improving Data Credibility: A Study with Datasets for Training Harmless Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c3837ae3d17a91b08bf5cc19280e7fd2-Paper-Conference.pdf))
> The degree to which a model avoids producing unsafe or harmful responses when given potentially malicious multimodal inputs.

**Harmfulness** (3 papers: [SoftMatcha: A Soft and Fast Pattern Matcher for Billion-Scale Corpus Searches](https://proceedings.iclr.cc/paper_files/paper/2025/file/159511050630689045bf5593e74b13cc-Paper-Conference.pdf), [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf), [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf))
> The latent disposition of a model to generate ethically problematic content, such as private information or information that could facilitate dangerous activities.

**Harm** (1 paper: [Improving and Assessing the Fidelity of Large Language Models Alignment to Online Communities](https://aclanthology.org/2025.naacl-long.5.pdf))
> The extent to which language promotes or glorifies unhealthy dieting, body objectification, or other harmful eating-disorder-related content.

## Relationships

### Harmlessness →
- **HH-RLHF** (measurement instrument): *measured_by*, 18 papers
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
- **Helpfulness** (construct): *correlates*, 14 papers
  > We find that the performance on the two alignment objectives is negatively correlated, with the Spearman’s correlation coefficient being ρ = −0.51 for HH-RLHF (Bai et al., 2022) and ρ = −0.61 for SafeRLHF (Ji et al., 2023) (p < 0.01). (Section 1)
  - [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf)
  - [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf)
  - [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf)
  - [Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/9178ece87f0a5d6558f49f43ec1e8a1a-Paper-Conference.pdf)
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
  - [L3Ms — Lagrange Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/92d3d2a9801211ca3693ccb2faa1316f-Paper-Conference.pdf)
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
  - [AGD: Adversarial Game Defense Against Jailbreak Attacks in Large Language Models](https://aclanthology.org/2025.acl-long.851.pdf)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
  - [Preference Learning for AI Alignment: a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kobalczyk25a/kobalczyk25a.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 12 papers
  > the three rounds of Safe RLHF significantly improved the Elo scores in both helpfulness and harmlessness, as evaluated by both GPT-4 and human evaluators.
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
  - [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf)
  - [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf)
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
  - [AGD: Adversarial Game Defense Against Jailbreak Attacks in Large Language Models](https://aclanthology.org/2025.acl-long.851.pdf)
  - [Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf)
- **PKU-SafeRLHF** (measurement instrument): *measured_by*, 8 papers
  > Harmful evaluation on PKU-SafeRLHF. (Figure 3a)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
  - [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf)
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
  - [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf)
  - [Gradient-Adaptive Policy Optimization: Towards Multi-Objective Alignment of Large Language Models](https://aclanthology.org/2025.acl-long.549.pdf)
  - [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf)
  - [RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.252.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 4 papers
  > We ask human evaluators to determine which response is more useful, harmless, and of higher quality. (Section 5)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
  - [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf)
  - [Accelerating Unbiased LLM Evaluation via Synthetic Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25v/zhou25v.pdf)
- **AdvBench** (measurement instrument): *measured_by*, 4 papers
  > "we red-team LLaMA2-7B-chat using three attack levels and evaluated on Advbench [10]."
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
  - [Ambiguity Awareness Optimization: Towards Semantic Disambiguation for Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.460.pdf)
- **BeaverTails** (measurement instrument): *measured_by*, 3 papers
  > BeaverTails dataset... assessing the harmlessness and helpfulness of the models.
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Too Helpful, Too Harmless, Too Honest or Just Right?](https://aclanthology.org/2025.emnlp-main.1510.pdf)
- **PKU-SafeRLHF-10K** (measurement instrument): *measured_by*, 3 papers
  > the PKU-SafeRLHF-10K dataset (Ji et al., 2023; Dai et al., 2024), which contains human-labeled preference data on the helpfulness and harmlessness of prompt-response pairs (Section 6.4)
  - [A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2025/file/084cf2b3d73abafa1705336a0e9ebb1c-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
- **StrongREJECT** (measurement instrument): *measured_by*, 3 papers
  > while quantifying response harmfulness using STRONG REJECT scores (Souly et al., 2024).
  - [The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25f/pan25f.pdf)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
  - [Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility](https://aclanthology.org/2025.emnlp-main.669.pdf)
- **HarmBench** (measurement instrument): *measured_by*, 2 papers
  > We evaluate the harmfulness of the model using HarmBench [40], a standardized framework that includes harmful behaviors and a wide range of both black box and white box attacks. (Section 4.1)
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
  - [Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment](https://aclanthology.org/2025.emnlp-main.406.pdf)
- **BeaverTails-Evaluation** (measurement instrument): *measured_by*, 2 papers
  > To further explore how increased honesty impacts harmlessness, we utilize the 700 test prompts from BeaverTails-Evaluation10 (Ji et al., 2023b) that can potentially elicit harmful responses... (Appendix D.8)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
  - [SDD: Self-Degraded Defense against Malicious Fine-tuning](https://aclanthology.org/2025.acl-long.1412.pdf)
- **JailbreakBench** (measurement instrument): *measured_by*, 2 papers
  > For harmlessness evaluation, we generated responses from the aligned LLM on a mixed dataset of AdvBench (Zou et al., 2023) and JailbreakBench (Chao et al., 2024)...
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [Ambiguity Awareness Optimization: Towards Semantic Disambiguation for Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.460.pdf)
- **Llama Guard** (measurement instrument): *measured_by*, 2 papers
  > For harmlessness evaluation, we ... used Llama-Guard (Inan et al., 2023) to determine the safety of the responses...
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [Ambiguity Awareness Optimization: Towards Semantic Disambiguation for Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.460.pdf)
- **HEx-PHI** (measurement instrument): *measured_by*, 2 papers
  > To assess the defense performance when a naive attacker directly inputs harmful queries to the language model, we utilize two harmful query benchmark datasets: Advbench (Zou et al., 2023) and HEx-PHI (Qi et al., 2024). (Section 4.1)
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
  - [Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment](https://aclanthology.org/2025.emnlp-main.406.pdf)
- **HarmBench classifier** (measurement instrument): *measured_by*, 2 papers
  > We report percentage of harmless responses based on the safety classifier HarmBench-Llama2-13B-Chat (Mazeika et al., 2024).
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **OpenAI Moderation API** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the toxicity and harmfulness of the fine-tuning examples by prompting strategy we use OpenAI’s Moderation API. (Section 3.1)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Perspective API** (measurement instrument): *measured_by*, 1 paper
  > For harmlessness, we follow (Li et al., 2024b) and utilize metrics Expected Maximum Toxicity (EMT) and Toxicity Probability (TP) from the Perspective API to examine the harmful content (Section 4.1).
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)
- **Anthropic Red Team** (measurement instrument): *measured_by*, 1 paper
  > The Anthropic Red-Team (Ganguli et al., 2022) dataset contains ∼40k instances. Each instance has a multi-round conversation between humans and the AI assistant, and a 5-level score showing the harmfulness of the conversation (Section 5.1).
  - [Unmasking and Improving Data Credibility: A Study with Datasets for Training Harmless Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c3837ae3d17a91b08bf5cc19280e7fd2-Paper-Conference.pdf)
- **GPT-4 Head-to-head Comparison** (measurement instrument): *measured_by*, 1 paper
  > we measure both harmlessness (Harm) and helpfulness (Help) for the harmlessness task... We additionally query GPT-4 for binary judgments on 1000 examples. (Sec. 4)
  - [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bd09a559a8c8e230697107b0f353d39-Paper-Conference.pdf)
- **Honesty** (construct): *correlates*, 1 paper
  > MiniGPT-v2 exhibits strong safety across several dimensions but underperforms on Truthfulness, suggesting a potential trade-off between honesty and harmlessness.
  - [MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d9dcd4ebef57f1839d871fe7d891e91-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmful instructions** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the safety of the fine-tuned models, we follow previous work by analyzing their performance on two evaluation datasets of harmful queries: Harmful Instructions (HarmI) (Zou et al., 2023) and Harmful Questions (HarmQ) (Bai et al., 2022a). (Section 3.1)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Llama Guard 3** (measurement instrument): *measured_by*, 1 paper
  > For evaluating if a generated response is harmless, we use an off-the-shelf LLM, Llama-Guard-3-8B (Llama Team, 2024), which is fine-tuned for content safety classification task to assess the safety of the generated text (Section 4.3).
  - [Constrained Decoding with Speculative Lookaheads](https://aclanthology.org/2025.naacl-long.239.pdf)
- **GCG** (measurement instrument): *measured_by*, 1 paper
  > Table 1 presents a benchmark comparison, displaying harmfulness scores and ASR (attack success rates, shown in brackets) for various defense methods... under several benchmark attacks, including GCG (Section 4.2).
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
- **PAIR** (measurement instrument): *measured_by*, 1 paper
  > Table 1 presents a benchmark comparison, displaying harmfulness scores and ASR (attack success rates, shown in brackets) for various defense methods... under several benchmark attacks, including PAIR (Section 4.2).
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
- **DeepInception** (measurement instrument): *measured_by*, 1 paper
  > Table 1 presents a benchmark comparison, displaying harmfulness scores and ASR (attack success rates, shown in brackets) for various defense methods... under several benchmark attacks, including DeepInception (Section 4.2).
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
- **Harmful content generation** (behavioral indicator): *causes*, 1 paper
  > Taking the concept of harmfulness as an example, L-Cross Modulation effectively steer LLMs to generate harmful content in 90% of outputs on test set, compared with 0% harmful content in the original responses;
  - [Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts](https://aclanthology.org/2025.acl-long.185.pdf)
- **ToxiGen** (measurement instrument): *measured_by*, 1 paper
  > Our experiments focus on Helpfulness (Alpaca Eval 2.0 (Dubois et al., 2024) and IFEval (Zhou et al., 2023)), Harmlessness (Toxigen (Hartvigsen et al., 2022)), and Coding (MBPP (Austin et al., 2021), HumanEval (Chen et al., 2021)). (Section 4)
  - [AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs](https://aclanthology.org/2025.acl-long.990.pdf)
- **AgentHarm** (measurement instrument): *measured_by*, 1 paper
  > AgentHarm (Andriushchenko et al., 2024b) is a benchmark proposed for measuring such harmfulness in LLM agents based on Inspect AI (UK AI Safety Institute, 2024).
  - [UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cl/zhang25cl.pdf)
- **XSTest** (measurement instrument): *measured_by*, 1 paper
  > For harmlessness, models are required to provide clear refusals to harmful queries... We test the models on StrongReject (Souly et al., 2024), XsTest (Röttger et al., 2024)... (Section 3.1)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **WildChat** (measurement instrument): *measured_by*, 1 paper
  > For harmlessness, models are required to provide clear refusals to harmful queries... We test the models on ... highly toxic prompts from WildChat (Zhao et al., 2024)... (Section 3.1)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **RealToxicityPrompts** (measurement instrument): *measured_by*, 1 paper
  > For harmlessness, we follow (Li et al., 2024b) and utilize metrics ... to examine the harmful content generated on RealToxicityPrompts (Gehman et al., 2020). (Section 4.1).
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)

### → Harmlessness
- **Safety alignment** (construct): *causes*, 4 papers
  > Specifically, harmless is achieved by safety alignment that empowers the LLM with safety guardrails so that the model can refuse harmful instructions.
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **Alignment** (construct): *causes*, 2 papers
  > Extensive efforts have been made before model release to align their behavior with human values, with the primary goal of ensuring their helpfulness and harmlessness. (ABSTRACT)
  - [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf)
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Actionability** (construct): *causes*, 1 paper
  > Through human evaluation, we determine actionability and informativeness as key attributes in inducing harm when the jailbroken response is followed by individuals without specialized knowledge. (Section 1)
  - [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf)
- **Informativeness** (construct): *causes*, 1 paper
  > Through human evaluation, we determine actionability and informativeness as key attributes in inducing harm when the jailbroken response is followed by individuals without specialized knowledge. (Section 1)
  - [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf)

### Associated with
- **Human preference alignment** (construct), 8 papers
  > Alignment is critical for a helpful and harmless language model (Ouyang et al., 2022; Bai et al., 2022).
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [HPS: Hard Preference Sampling for Human Preference Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25c/zou25c.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Safety** (construct), 2 papers
  > safety assesses harmlessness (Section 4.1).
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
  - [A Simple Yet Effective Method for Non-Refusing Context Relevant Fine-grained Safety Steering in LLMs](https://aclanthology.org/2025.emnlp-main.1781.pdf)
- **Humor** (construct), 2 papers
  > In practice, human preferences are multi-dimensional and we often need to align LLMs to balance multiple, sometimes conflicting, preference dimensions such as helpfulness, harmlessness, and humor (Section 2. Related Work)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
- **Safe response generation** (behavioral indicator), 1 paper
  > “We evaluate RLCD through both human and automatic evaluations on three tasks, aiming to improve the ability of LLaMA-7B ... to generate harmless outputs” (Introduction).
  - [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bd09a559a8c8e230697107b0f353d39-Paper-Conference.pdf)
- **Refusal** (behavioral indicator), 1 paper
  > ...a model that refuses to answer, while technically considered harmless, renders the response quite unhelpful [16].
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
- **Harmful request refusal** (behavioral indicator), 1 paper
  > The first two responses demonstrate the model’s ability to avoid providing assistance on unethical actions... (Figure 4).
  - [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf)
