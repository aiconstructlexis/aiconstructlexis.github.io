# Helpfulness
**Type:** Construct  
**Supporting papers:** 180  
**Also known as:** Perceived helpfulness, Usefulness  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats helpfulness as the quality, or latent tendency, of a model response to be useful, relevant, informative, supportive, or satisfying for a user’s query, instruction, or needs. Many definitions alternate between describing it as a property of outputs and as a model ability, disposition, or capacity, but they largely converge on assistance that meets user goals, sometimes explicitly through instruction following or direct task completion. Smaller lines define it more narrowly as completing the basic task in an instruction, serving as a direct answer, or fully understanding user intent, while a few domain-specific papers recast it as culturally aware support, advice shaped by personal or majority preferences, or tutor guidance that is constructive and appropriately toned without giving away the full answer. A minority framing shifts the reference point to the user, defining perceived helpfulness as how effectively users feel the model supported their needs and goals, and some authors use usefulness as a near-synonym for meeting user requirements or retaining task performance.

**Space of facets.** Papers most often organize helpfulness as one objective in multi-objective alignment, usually alongside harmlessness, and also with honesty, truthfulness, factuality, safety, empathy, and sensitivity. Some work places it inside broader preference schemes such as HHH, while other work merges labels, for example helpfulness with instruction following, or embeds it in a utility constraint that also includes language, supportiveness, consistency, and factuality. The term is not used in a single way: some papers treat helpfulness and usefulness almost interchangeably, whereas others distinguish ordinary helpfulness from perceived helpfulness, culturally aware helpfulness, subjective advice helpfulness, or pedagogical helpfulness.

**Space of measurement.** Operationally, papers link helpfulness to 33 measurement instruments and 4 behavioral indicators. The most common instruments are HH-RLHF, LLM-as-a-judge, MT-Bench, AlpacaEval 2.0, and human evaluation: preference datasets such as HH-RLHF operationalize it through crowdworker choices between responses, judge models rate responses for helpfulness alongside criteria like relevance, accuracy, and insightfulness, MT-Bench and AlpacaEval 2.0 treat it as performance on multi-turn or general-domain prompts, and human raters compare responses or score their usefulness or helpfulness on rating scales. The linked behavioral indicators center on generating helpful answers, following instructions, and refusal-related behavior. These measurements often match the dominant definition of useful assistance, but some papers operationalize helpfulness as instruction following, average task accuracy on general benchmarks, averaged normalized benchmark scores, or not-overrefusal rates.

**Links.** Harmlessness is the most recurrent linked construct: several papers report that harmlessness correlates with helpfulness, and many others describe the pair as related or competing objectives, often using the language of trade-off or tension. Several papers claim a causal relationship from alignment to helpfulness, and from safety alignment to helpfulness, while one paper claims a causal relationship from safety reasoning to helpfulness. Papers also claim causal relationships from refusal to helpfulness and from overrefusal to helpfulness, with the quoted evidence describing refusals as rendering responses unhelpful or less helpful. Beyond that, helpfulness is reported to correlate with factuality, coherence, complexity, and verbosity, and is related to human preference alignment, safety, humor, empathy, instruction following, and helpful response generation.

## Sources

**Helpfulness** (22 papers: [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf), [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf), [Navigating the Cultural Kaleidoscope: A Hitchhiker's Guide to Sensitivity in Large Language Models](https://aclanthology.org/2025.naacl-long.388.pdf), [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf), [Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque](https://aclanthology.org/2025.naacl-long.629.pdf), [From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.346.pdf), [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf), [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf), [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf), [Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment](https://aclanthology.org/2025.naacl-long.472.pdf), [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf), [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf), [Protecting Privacy in Multimodal Large Language Models with MLLMU-Bench](https://aclanthology.org/2025.naacl-long.207.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf), [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf), [AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.333.pdf), [PRACTIQ: A Practical Conversational Text-to-SQL dataset with Ambiguous and Unanswerable Queries](https://aclanthology.org/2025.naacl-long.13.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [Wait, that's not an option: LLMs Robustness with Incorrect Multiple-Choice Options](https://aclanthology.org/2025.acl-long.75.pdf), [InfAlign: Inference-aware language model alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balashankar25a/balashankar25a.pdf), [From Problem-Solving to Teaching Problem-Solving: Aligning LLMs with Pedagogy using Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.15.pdf))
> The quality of an AI assistant's responses in being useful, relevant, and satisfying to a user's query or instruction.

**Perceived helpfulness** (1 paper: [Personality Matters: User Traits Predict LLM Preferences in Multi-Turn Collaborative Tasks](https://aclanthology.org/2025.emnlp-main.71.pdf))
> The extent to which a user feels an LLM effectively supports their specific needs and goals during a collaborative interaction.

**Usefulness** (6 papers: [Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf), [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf), [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf), [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf), [Sightation Counts: Leveraging Sighted User Feedback in Building a BLV-aligned Dataset of Diagram Descriptions](https://aclanthology.org/2025.acl-long.1338.pdf), [TrojanStego: Your Language Model Can Secretly Be A Steganographic Privacy Leaking Agent](https://aclanthology.org/2025.emnlp-main.1386.pdf))
> The degree to which a model's output effectively meets a user's requirements and performs well on general language processing tasks, often considered in a trade-off with safety.

## Relationships

### Helpfulness →
- **HH-RLHF** (measurement instrument): *measured_by*, 28 papers
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
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 19 papers
  > the three rounds of Safe RLHF significantly improved the Elo scores in both helpfulness and harmlessness, as evaluated by both GPT-4 and human evaluators.
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
  - [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf)
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
  - [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf)
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [LLaMA-Omni: Seamless Speech Interaction with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf)
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
  - [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf)
  - [AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.333.pdf)
  - [From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.346.pdf)
  - [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf)
  - [Data to Defense: The Role of Curation in Aligning Large Language Models Against Safety Compromise](https://aclanthology.org/2025.emnlp-main.647.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 7 papers
  > Following HelpSteer [12], we use MT Bench [31] to measure helpfulness, TruthfulQA MC2 [36] to measure correctness, and the mean number of characters in MT Bench responses to measure verbosity.
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Backtracking Improves Generation Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/65beb73449888fabcf601b3a3ef4b3a7-Paper-Conference.pdf)
  - [Can a Large Language Model be a Gaslighter?](https://proceedings.iclr.cc/paper_files/paper/2025/file/0769598fdeb4f23ee86fec1bc0777f44-Paper-Conference.pdf)
  - [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf)
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
  - [AGD: Adversarial Game Defense Against Jailbreak Attacks in Large Language Models](https://aclanthology.org/2025.acl-long.851.pdf)
  - [CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/min25b/min25b.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 6 papers
  > We ask human evaluators to determine which response is more useful, harmless, and of higher quality. (Section 5)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
  - [IQA-EVAL: Automatic Evaluation of Human-Model Interactive Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a23b26eaaefd187973658f5001f4fe-Paper-Conference.pdf)
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.333.pdf)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 6 papers
  > In addition, we also use AlpacaEval 2.0 Length Controlled [37] and Arena Hard [38] as secondary measures of helpfulness, following [33, 39].
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
  - [HelpSteer3: Human-Annotated Feedback and Edit Data to Empower Inference-Time Scaling in Open-Ended General-Domain Tasks](https://aclanthology.org/2025.acl-long.1246.pdf)
  - [AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs](https://aclanthology.org/2025.acl-long.990.pdf)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **PKU-SafeRLHF** (measurement instrument): *measured_by*, 5 papers
  > PKU-SafeRLHF provides both paired helpfulness preference rankings and binary safety labels.
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
  - [Gradient-Adaptive Policy Optimization: Towards Multi-Objective Alignment of Large Language Models](https://aclanthology.org/2025.acl-long.549.pdf)
  - [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf)
  - [RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.252.pdf)
  - [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf)
- **UltraFeedback** (measurement instrument): *measured_by*, 3 papers
  > UltraFeedback [7]: a multi-aspect alignment dataset with 64K prompts with preferences obtained from GPT-4, including "Instruction following", "Honest", "Truthful", and "Helpful" objectives (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [DPO Meets PPO: Reinforced Token Optimization for RLHF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25b/zhong25b.pdf)
  - [Textual Aesthetics in Large Language Models](https://aclanthology.org/2025.emnlp-main.696.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 3 papers
  > training set is GSM8K (grade school math) and helpfulness is test accuracy on GSM8K. (Section 2)
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
  - [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 3 papers
  > For models tuned on benign data, we also tested helpfulness on AlpacaEval [29]. (Section 5, Response to RQ2)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [Improving Factuality with Explicit Working Memory](https://aclanthology.org/2025.acl-long.548.pdf)
  - [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 3 papers
  > In addition, we also use AlpacaEval 2.0 Length Controlled [37] and Arena Hard [38] as secondary measures of helpfulness, following [33, 39].
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
  - [HelpSteer3: Human-Annotated Feedback and Edit Data to Empower Inference-Time Scaling in Open-Ended General-Domain Tasks](https://aclanthology.org/2025.acl-long.1246.pdf)
- **Alpaca instruction dataset** (measurement instrument): *measured_by*, 3 papers
  > To evaluate helpfulness, we assessed the quality of responses generated on the Alpaca dataset (Taori et al., 2023)...
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [Data to Defense: The Role of Curation in Aligning Large Language Models Against Safety Compromise](https://aclanthology.org/2025.emnlp-main.647.pdf)
  - [Too Helpful, Too Harmless, Too Honest or Just Right?](https://aclanthology.org/2025.emnlp-main.1510.pdf)
- **HelpSteer** (measurement instrument): *measured_by*, 3 papers
  > For HelpSteer, we use https://huggingface.co/Haoxiang-Wang/ RewardModel-Mistral-7B-for-DPA-v1 for all attributes of rewards, including helpfulness, correctness, coherence, complexity and verbosity.
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
  - [Balancing the Budget: Understanding Trade-offs Between Supervised and Preference-Based Finetuning](https://aclanthology.org/2025.acl-long.1248.pdf)
- **BeaverTails** (measurement instrument): *measured_by*, 3 papers
  > BeaverTails dataset... assessing the harmlessness and helpfulness of the models.
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf)
- **PKU-SafeRLHF-10K** (measurement instrument): *measured_by*, 2 papers
  > the PKU-SafeRLHF-10K dataset (Ji et al., 2023; Dai et al., 2024), which contains human-labeled preference data on the helpfulness and harmlessness of prompt-response pairs (Section 6.4)
  - [A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2025/file/084cf2b3d73abafa1705336a0e9ebb1c-Paper-Conference.pdf)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 2 papers
  > we also leverage MMMU (Yue et al., 2024) and LLaVA-Bench (Liu et al., 2024b) to assess the model’s reasoning ability and helpfulness level. (Section 3.3.1)
  - [Protecting Privacy in Multimodal Large Language Models with MLLMU-Bench](https://aclanthology.org/2025.naacl-long.207.pdf)
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)
- **Just-Eval** (measurement instrument): *measured_by*, 2 papers
  > Just-Eval evaluates LLMs’ outputs based on helpfulness, clarity, factuality, depth, and engagement.
  - [AGD: Adversarial Game Defense Against Jailbreak Attacks in Large Language Models](https://aclanthology.org/2025.acl-long.851.pdf)
  - [Speculative Safety-Aware Decoding](https://aclanthology.org/2025.emnlp-main.648.pdf)
- **ArmoRM** (measurement instrument): *measured_by*, 1 paper
  > Since ArmoRM is a multi-objective model that not only gives a scalar reward value but also predicts human-interpretable fine-grained attributes, we first select 5 attributes (namely complexity, instruction following, honesty, helpfulness, and intelligence depth) that have the highest average coefficients on the UltraFeedback data. (Section 6.2)
  - [Reward-Augmented Data Enhances Direct Preference Alignment of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25az/zhang25az.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > We also assess the helpfulness of the targeted LLMs... To do this, we select 500 examples from three sources: ...MMLU (knowledge tests)... (Section 4.1)
  - [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf)
- **GPT-4 Head-to-head Comparison** (measurement instrument): *measured_by*, 1 paper
  > For the helpfulness and outlining tasks we collect just one set of labels for overall helpfulness (Help) and outline quality (Qual) respectively... We additionally query GPT-4 for binary judgments on 1000 examples. (Sec. 4)
  - [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bd09a559a8c8e230697107b0f353d39-Paper-Conference.pdf)
- **XNLI** (measurement instrument): *measured_by*, 1 paper
  > For the assessment of usefulness, we sample 30 examples in English and each language overlapping with MultiJail from XNLI (Conneau et al., 2018) and X-CSQA (Lin et al., 2021)... We calculate the average accuracy on both datasets to represent usefulness. (Section 4.3)
  - [Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf)
- **X-CSQA** (measurement instrument): *measured_by*, 1 paper
  > For the assessment of usefulness, we sample 30 examples in English and each language overlapping with MultiJail from XNLI (Conneau et al., 2018) and X-CSQA (Lin et al., 2021)... We calculate the average accuracy on both datasets to represent usefulness. (Section 4.3)
  - [Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf)
- **AlpacaFarm** (measurement instrument): *measured_by*, 1 paper
  > The first is the test set from AlpacaFarm (Dubois et al., 2023), which contains 805 instructions for assessing helpfulness. (Sec. 5.1)
  - [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > ...we select TruthfulQA (Lin et al., 2022) and SafetyBench (Zhang et al., 2023) as the evaluation datasets, which measure helpfulness and safety, respectively. (Section 4.1)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
- **Verbosity** (construct): *correlates*, 1 paper
  > Finally, response length is slightly positively correlated with helpfulness (Pearson’s R=0.0845), consistent with the correlation between verbosity and helpfulness (Pearson’s R=0.0600).
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > we evaluate the impact of safety heads ablation on helpfulness. We use lm-eval (Gao et al., 2024) to assess model performance after ablating safety heads of Llama-2-7b-chat on zero-shot tasks... (Section 5.3)
  - [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf)
- **MME** (measurement instrument): *measured_by*, 1 paper
  > “For multimodal helpfulness benchmarks, we use MMBench (Liu et al., 2023d), MME (Fu et al., 2024), and SEEDBench (Li et al., 2023a).”
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **PandaLM** (measurement instrument): *measured_by*, 1 paper
  > Specifically, we use PandaLM (Wang et al., 2023b, 2024) to evaluate the helpfulness of various models. (Section 4.1)
  - [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > TRIVIAQA (Joshi et al., 2017): Assesses the model’s question-answering capability. ... Helpfulness: evaluated as the averaged normalized scores across all general performance benchmarks we considered. (Section 5.1)
  - [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > HELLASWAG (Zellers et al., 2019): Measures how well the model can generate the most natural continuation from four candidate sentences following a given sentence fragment. ... Helpfulness: evaluated as the averaged normalized scores across all general performance benchmarks we considered. (Section 5.1)
  - [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf)
- **IFEval** (measurement instrument): *measured_by*, 1 paper
  > Our experiments focus on Helpfulness (Alpaca Eval 2.0 (Dubois et al., 2024) and IFEval (Zhou et al., 2023)), Harmlessness (Toxigen (Hartvigsen et al., 2022)), and Coding (MBPP (Austin et al., 2021), HumanEval (Chen et al., 2021)). (Section 4)
  - [AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs](https://aclanthology.org/2025.acl-long.990.pdf)
- **Databricks Dolly-15k** (measurement instrument): *measured_by*, 1 paper
  > to assess whether LLMs retain usefulness after fine-tuning, we select 15k general-domain samples equally from Alpaca (Taori et al., 2023), BeaverTails, and Dolly (Conover et al., 2023). (Section 5.1)
  - [Data to Defense: The Role of Curation in Aligning Large Language Models Against Safety Compromise](https://aclanthology.org/2025.emnlp-main.647.pdf)
- **MORBENCH** (measurement instrument): *measured_by*, 1 paper
  > We have explored the safety decision boundaries of various LLMs and construct the MORBENCH evaluation set to facilitate robust assessment of model safety and helpfulness across multiple languages. (Abstract)
  - [Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary](https://aclanthology.org/2025.emnlp-main.1065.pdf)
- **PLLuM-Align** (measurement instrument): *measured_by*, 1 paper
  > For scalar multi-attribute rating, annotators evaluated each response on a 5-point Likert scale across seven criteria: i) truthfulness, (ii) linguistic correctness, (iii) safety, (iv) fairness, (v) conciseness, (vi) coherence & reasoning, as well as vii) helpfulness & instruction-following.
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)
- **AUTO-J** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the model’s responses, we enlist the assistance of both AUTO-J (Li et al., 2023a) and GPT-4 (i.e., gpt-4-0613; OpenAI (2023a)), which provide ratings on a scale of 1 to 10. (Section 4.6)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **Safety reasoning** (construct): *causes*, 1 paper
  > Moreover, benefiting from the decomposed problem-solving in reasoning, STAIR mitigates safety-performance trade-offs and gets improvements in multiple dimensions, including helpfulness, truthfulness, robustness, and privacy awareness. (Section 1)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)

### → Helpfulness
- **Harmlessness** (construct): *correlates*, 14 papers
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
- **Alignment** (construct): *causes*, 5 papers
  > Extensive efforts have been made before model release to align their behavior with human values, with the primary goal of ensuring their helpfulness and harmlessness. (ABSTRACT)
  - [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf)
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
  - [BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling](https://proceedings.neurips.cc/paper_files/paper/2024/file/056521a35eacd9d2127b66a7d3c499c5-Paper-Conference.pdf)
  - [Nudging: Inference-time Alignment of LLMs via Guided Decoding](https://aclanthology.org/2025.acl-long.623.pdf)
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)
- **Safety alignment** (construct): *causes*, 4 papers
  > Via this channel, an LLM learns how to react to human instruction in a harmless and helpful way, as demonstrated in the alignment dataset. (Section 1)
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
  - [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **Refusal** (behavioral indicator): *causes*, 3 papers
  > ...a model that refuses to answer, while technically considered harmless, renders the response quite unhelpful [16].
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
- **Overrefusal** (behavioral indicator): *causes*, 3 papers
  > increased model over-rejection, resulting in diminished helpfulness
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)
  - [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf)
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
- **Coherence** (construct): *correlates*, 1 paper
  > In Table 2, we observe that coherence is a much weaker predictor of helpfulness in HelpSteer2 (Pearson’s R=0.4979) compared to HelpSteer (Pearson’s R=0.6348).
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Factuality** (construct): *correlates*, 1 paper
  > Conversely, correctness has become a stronger predictor of helpfulness in HelpSteer2 (Pearson’s R=0.9430) than in HelpSteer (Pearson’s R=0.8525).
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Complexity** (construct): *correlates*, 1 paper
  > Additionally, the Pearson’s R values for both complexity (0.2361 to 0.1805) and verbosity (0.2555 to 0.0600) have decreased, indicating that annotators are less influenced by the complexity and verbosity of responses when assessing overall helpfulness in HelpSteer2.
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Human preference alignment** (construct), 6 papers
  > Alignment is critical for a helpful and harmless language model (Ouyang et al., 2022; Bai et al., 2022).
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Instruction following** (behavioral indicator), 3 papers
  > LMMs must be helpful (e.g., ... follow user instructions)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Helpful response generation** (behavioral indicator), 3 papers
  > “We evaluate RLCD through both human and automatic evaluations on three tasks, aiming to improve the ability of LLaMA-7B ... to generate ... helpful outputs” (Introduction).
  - [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bd09a559a8c8e230697107b0f353d39-Paper-Conference.pdf)
  - [Controllable Safety Alignment: Inference-Time Adaptation to Diverse Safety Requirements](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9fa03d8b6b0564580337c985ad10a04-Paper-Conference.pdf)
  - [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf)
- **Safety** (construct), 2 papers
  > α is a hyperparameter to adjust the balance between safety and usefulness.
  - [Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats](https://proceedings.iclr.cc/paper_files/paper/2025/file/699c5a2bb87a8aa32c4ad541d9997361-Paper-Conference.pdf)
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **Humor** (construct), 2 papers
  > In practice, human preferences are multi-dimensional and we often need to align LLMs to balance multiple, sometimes conflicting, preference dimensions such as helpfulness, harmlessness, and humor (Section 2. Related Work)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
- **Empathy** (construct), 1 paper
  > Wang and Torres (2022) collected helpful and unhelpful advice from Reddit and analyzed that the main factor is ‘empathy’, consistent with our findings in Figure 4. (Section 2)
  - [AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.333.pdf)
