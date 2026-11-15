# Human preference alignment
**Type:** Construct  
**Supporting papers:** 131  
**Also known as:** Alignment with human preferences, General alignment, User Alignment, Preference alignment, Human-predictor alignment, Human value alignment, Human alignment, Human-AI alignment, Value alignment, Alignment with physician preferences, Alignment with human preference, Preference following  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats human preference alignment as the degree to which an LLM's outputs or behaviors conform to human preferences, judgments, values, intentions, or desired objectives. Many definitions anchor those preferences in qualities such as helpfulness, harmlessness, honesty, truthfulness, coherence, appropriateness, safety, or broadly desirable assistant behavior, and several papers describe the construct as something learned from preference data, reward models, RLHF, DPO, or related optimization. A smaller line narrows the reference standard to user expectations such as conciseness and readability, to physician note preferences, to multimodal interactions, or to human or model-derived preferences rather than human preferences alone. Only a few definitions shift from a latent property to an explicitly observable tendency, such as producing higher-ranked responses, or to a continuous scalar objective over parameter space.

**Space of facets.** A recurring way of organizing the construct is through HHH or 3H style components: helpfulness, honesty, and harmlessness, sometimes with a broader general criterion. Nearby labels are used across papers for closely overlapping ideas, including general alignment, human alignment, human value alignment, value alignment, and human-AI alignment, while user alignment is used for a narrower skill set covering conciseness, readability, and safety. The naming is therefore broad: some papers specialize the target to open-ended ranking, multimodal interaction, physician note quality, or demographic-group preferences. One paper also separates the latent construct from the observable notion of preference following, defined as producing responses that rank better with reward models or human evaluators.

**Space of measurement.** Papers link human preference alignment to 10 measurement instruments and 3 behavioral indicators. The most commonly linked instruments are AlpacaEval 2.0, Arena-Hard, Chatbot Arena, AlpacaEval, and MT-Bench. Operationally, papers use benchmark scores and preference comparisons over model outputs: AlpacaEval 2.0 is described as approximately evaluating human preference for instruction following, Arena-Hard as a challenging benchmark aligned with Chatbot Arena rankings, and Chatbot Arena as pairwise battles where users vote for a preferred response; other studies score best-of-n samples with human evaluators or LLM-as-a-judge systems. These operationalizations mostly target preferred outputs and instruction-following behavior, matching the dominant definitions, while other linked instruments extend to human preference studies, alignment datasets, and multimodal benchmarks.

**Links.** Related links most often connect human preference alignment with Harmlessness, Helpfulness, and Honesty, often through HHH or 3H formulations. Several papers claim a causal relationship from Instruction following and Mode-seeking behavior to Human preference alignment, and another paper claims a reverse causal relationship from Human preference alignment to Instruction following. Additional papers also claim causal relationships from Human preference alignment to other linked constructs and indicators, alongside further related links to the remaining linked constructs and indicators. No correlational link is reported.

## Sources

**Alignment with human preferences** (12 papers: [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf), [CPPO: Continual Learning for Reinforcement Learning with Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf), [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf), [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf), [Privately Aligning Language Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/477b39bfb9db99f60914dbfed5f23eb2-Paper-Conference.pdf), [Statistical Rejection Sampling Improves Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/efea6d3821a7ccae74e58892162164c0-Paper-Conference.pdf), [Multi-turn Reinforcement Learning with Preference Human Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/d77a7b289361abff82bdd2fb537ae152-Paper-Conference.pdf), [SELF-EVOLVED REWARD LEARNING FOR LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/26f5a4e26c13d1e0a47f46790c999361-Paper-Conference.pdf), [Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque](https://aclanthology.org/2025.naacl-long.629.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.51.pdf), [Direct Density Ratio Optimization: A Statistically Consistent Approach to Aligning Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/higuchi25a/higuchi25a.pdf))
> The degree to which a model's outputs reflect the qualities preferred by humans, such as being helpful and harmless, learned implicitly through training on preference data rather than explicit instruction.

**Human preference alignment** (8 papers: [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf), [Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf), [Compositional Preference Models for Aligning LMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/8fd10360ac9de462ffd36155d87ee999-Paper-Conference.pdf), [WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf), [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf), [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf), [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf), [BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ding25d/ding25d.pdf))
> The degree to which a large language model's behaviors and outputs conform to human values and intentions.

**General alignment** (1 paper: [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf))
> The extent to which an LLM's outputs conform to human intentions and broadly desirable assistant behavior across tasks.

**User Alignment** (1 paper: [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf))
> The ability to empathize with the user and align responses to their intentions, preferences, and expectations in terms of conciseness, readability, and safety.

**Preference alignment** (5 papers: [SaulLM-54B & SaulLM-141B: Scaling Up Domain Adaptation for the Legal Domain](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea3f85a33f9ba072058e3df233cf6cca-Paper-Conference.pdf), [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf), [LiPO: Listwise Preference Optimization through Learning-to-Rank](https://aclanthology.org/2025.naacl-long.121.pdf), [Cheems: A Practical Guidance for Building and Evaluating Chinese Reward Models from Scratch](https://aclanthology.org/2025.acl-long.737.pdf), [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf))
> The degree to which model outputs conform to human or model-derived preferences for desirable responses.

**Human-predictor alignment** (1 paper: [Eliciting Human Preferences with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9867d5a22653ce98b02595061e40f12-Paper-Conference.pdf))
> The degree to which a model's behavior and predictions correspond to a human user's desired behavior and true preferences.

**Human value alignment** (1 paper: [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf))
> The process of adjusting an AI system's behavior to be consistent with specified human values and preferences.

**Human alignment** (3 papers: [Seeing Eye to AI: Human Alignment via Gaze-Based Response Rewards for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4165875c8140617b8c165e18c342ccbb-Paper-Conference.pdf), [Single Ground Truth Is Not Enough: Adding Flexibility to Aspect-Based Sentiment Analysis Evaluation](https://aclanthology.org/2025.naacl-long.603.pdf), [Discriminative Finetuning of Generative Large Language Models without Reward Models and Human Preference Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25d/guo25d.pdf))
> The degree to which a large language model's outputs and behaviors conform to human expectations, values, and intentions.

**Human-AI alignment** (1 paper: [Position: Beyond Assistance – Reimagining LLMs as Ethical and Adaptive Co-Creators in Mental Health Care](https://raw.githubusercontent.com/mlresearch/v267/main/assets/badawi25a/badawi25a.pdf))
> The degree to which an LLM's outputs and behavior remain aligned with human expertise, therapeutic goals, and human-centered care norms.

**Value alignment** (7 papers: [Large Language Models as Automated Aligners for benchmarking Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf), [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf), [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf), [SafetyQuizzer: Timely and Dynamic Evaluation on the Safety of LLMs](https://aclanthology.org/2025.naacl-long.85.pdf), [One fish, two fish, but not the whole sea: Alignment reduces language models' conceptual diversity](https://aclanthology.org/2025.naacl-long.561.pdf), [Internal Value Alignment in Large Language Models through Controlled Value Vector Activation](https://aclanthology.org/2025.acl-long.1326.pdf), [Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf))
> The tendency of a model's responses to conform to high-level human quality guidelines such as being helpful, honest, and harmless.

**Alignment with physician preferences** (1 paper: [Process-Supervised Reward Models for Verifying Clinical Note Generation: A Scalable Approach Guided by Domain Expertise](https://aclanthology.org/2025.emnlp-main.967.pdf))
> The degree to which a model's outputs match the subjective preferences of physicians regarding clinical note quality, beyond mere factual correctness.

**Alignment with human preference** (1 paper: [Energy-Based Preference Model Offers Better Offline Alignment than the Bradley-Terry Preference Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25i/hong25i.pdf))
> The degree to which a language model's outputs conform to human judgments of quality, desirability, or correctness, as inferred from preference data.

**Preference following** (1 paper: [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf))
> The observable tendency of a model to produce responses that are rated higher by a reward model or human evaluators, reflecting alignment with desired behaviors.

## Relationships

### Human preference alignment →
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 7 papers
  > AlpacaEval 2.0 approximately evaluates human preference for instruction following. (Section 5.1)
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
  - [Bootstrapping Language Models with DPO Implicit Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4de96b9169aa869cc102afe31055e8-Paper-Conference.pdf)
  - [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
  - [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.51.pdf)
  - [KABB: Knowledge-Aware Bayesian Bandits for Dynamic Expert Coordination in Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aa/zhang25aa.pdf)
  - [Energy-Based Preference Model Offers Better Offline Alignment than the Bradley-Terry Preference Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25i/hong25i.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 4 papers
  > Arena-Hard is a more challenging benchmark that closely aligns with the human preference ranking from Chatbot Arena
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
  - [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
  - [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Chatbot Arena** (measurement instrument): *measured_by*, 4 papers
  > The resulting dynamic benchmarks, i.e., MixEval and MixEval-Hard, exhibit significant correlations (0.93 and 0.96) with real-world user preference leaderboard (i.e., Chatbot Arena) and showcase high impartiality and efficiency.
  - [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf)
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
  - [Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf)
  - [Improving Your Model Ranking on Chatbot Arena by Vote Rigging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/min25a/min25a.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 3 papers
  > For assessing human preferences, recent studies have focused on building crowdsourced battle platforms with human ratings as the primary evaluation metric. Typical platforms include Chatbot Arena (Zheng et al., 2023), MT-Bench (Zheng et al., 2023), and AlpacaEval (Li et al., 2023b). (Section 1)
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
  - [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf)
  - [EcoLoRA: Communication-Efficient Federated Fine-Tuning of Large Language Models](https://aclanthology.org/2025.emnlp-main.1046.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 3 papers
  > For assessing human preferences, recent studies have focused on building crowdsourced battle platforms with human ratings as the primary evaluation metric. Typical platforms include Chatbot Arena (Zheng et al., 2023), MT-Bench (Zheng et al., 2023), and AlpacaEval (Li et al., 2023b). (Section 1)
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
  - [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf)
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)
- **Human preference evaluation** (measurement instrument): *measured_by*, 2 papers
  > “Then, we conduct a human preference study.”
  - [Multimodal Large Language Models Make Text-to-Image Generative Models Align Better](https://proceedings.neurips.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
  - [ALLaM: Large Language Models for Arabic and English](https://proceedings.iclr.cc/paper_files/paper/2025/file/54c15a3033686e7999aecd2740c5a7c4-Paper-Conference.pdf)
- **HH-RLHF** (measurement instrument): *measured_by*, 2 papers
  > Comparison in terms of the trade-off between Alignment (accuracy) and Diversity (entropy) on the Anthropic HH dataset. (Table 1)
  - [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf)
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
- **Truthfulness** (construct): *causes*, 2 papers
  > the effects on other trustworthiness aspects are negative: ... truthfulness decreases by 25%... (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **Readability** (construct): *causes*, 2 papers
  > By aligning the LLM with the aggregated client preference, we can improve the professionalism and readability of LLM’s generated content. (Section 1)
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > for the VA task, we evaluate using MT-bench (Zheng et al., 2023) and MMLU (Hendrycks et al., 2020) (Section 4.1)
  - [EcoLoRA: Communication-Efficient Federated Fine-Tuning of Large Language Models](https://aclanthology.org/2025.emnlp-main.1046.pdf)
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > their magical ability to follow myriad user instructions – the driving force behind their mass adoption – has been attributed to instruction fine-tuning and learning from human feedback. (Section 1)
  - [Privately Aligning Language Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/477b39bfb9db99f60914dbfed5f23eb2-Paper-Conference.pdf)
- **Moral reasoning** (construct): *causes*, 1 paper
  > RLHF applied to a general-purpose preference dataset leads to a substantial average improvement of 31% on the machine ethics benchmark. (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Stereotyping** (construct): *causes*, 1 paper
  > the effects on other trustworthiness aspects are negative: stereotypical bias increases by 150%... (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **OASST1** (measurement instrument): *measured_by*, 1 paper
  > OASST1 is a human-generated, human-annotated, assistant-style conversation, created through global crowdsourcing and widely used for human alignment tasks (K¨opf et al., 2023; Dettmers et al., 2023; Wu et al., 2024b).
  - [Seeing Eye to AI: Human Alignment via Gaze-Based Response Rewards for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4165875c8140617b8c165e18c342ccbb-Paper-Conference.pdf)
- **WildVision** (measurement instrument): *measured_by*, 1 paper
  > human-preference alignment benchmarks: MM-AlignBench, WildVision (Lu et al., 2024), and MIA-Bench (Qian et al., 2024). (Section 6.1)
  - [OmniAlign-V: Towards Enhanced Alignment of MLLMs with Human Preference](https://aclanthology.org/2025.acl-long.906.pdf)

### → Human preference alignment
- **Instruction following** (behavioral indicator): *causes*, 2 papers
  > the model's ability to follow instructions inherently leads to better alignment with general preferences such as helpfulness and safety
  - [On-the-fly Preference Alignment via Principle-Guided Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcd1d7a599f33c06f06615429793c69b-Paper-Conference.pdf)
  - [OmniAlign-V: Towards Enhanced Alignment of MLLMs with Human Preference](https://aclanthology.org/2025.acl-long.906.pdf)
- **Mode-seeking behavior** (construct): *causes*, 2 papers
  > SimPER implicitly exhibits mode-seeking behavior, leading to strong alignment performance.
  - [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)

### Associated with
- **Harmlessness** (construct), 8 papers
  > Alignment is critical for a helpful and harmless language model (Ouyang et al., 2022; Bai et al., 2022).
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [HPS: Hard Preference Sampling for Human Preference Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25c/zou25c.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Helpfulness** (construct), 6 papers
  > Alignment is critical for a helpful and harmless language model (Ouyang et al., 2022; Bai et al., 2022).
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Honesty** (construct), 2 papers
  > Additionally, we found SALMON capable to emphasize the distinct aspects of the alignment with respect to being Helpful, Honest, and Harmless) (HHH) (Askell et al., 2021) by customizing its preference principles.
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Conciseness** (construct), 1 paper
  > We define 4 primary abilities which are divided into 12 fine-grained skills for comprehensive language model evaluation: ... and User Alignment (Conciseness, Readability, Harmlessness). (Section 1)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Refusal** (behavioral indicator), 1 paper
  > “The ideal models are supposed to refuse to answer questions that violate human values and meanwhile provide appropriate justifications for rejection.”
  - [Large Language Models as Automated Aligners for benchmarking Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf)
- **Verbosity bias** (construct), 1 paper
  > Despite its advantages, DPO suffers from a length bias problem, which is caused by the unbalanced length preference due to the non-uniform length distribution of chosen and rejected responses. (Section 1)
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **Trustworthiness** (construct), 1 paper
  > Our results demonstrate that RLHF on human preferences doesn’t automatically guarantee trustworthiness, and reverse effects are often observed. (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Reasoning** (construct), 1 paper
  > With the bidirectional negative feedback, our proposed BNF can naturally prevent the model from over-fitting to preference data, striking a better balance between human values and reasoning ability while minimizing the alignment tax.
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Knowledge retention** (construct), 1 paper
  > This seeks a good trade-off between policy learning and knowledge retention. Our experimental results show that CPPO outperforms strong Continuous learning (CL) baselines when it comes to consistently aligning with human preferences. (Abstract)
  - [CPPO: Continual Learning for Reinforcement Learning with Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > given π∗aligned with human preference, it can both empower response generation, as well as work with its reference model (amateur) to enhance the scoring of HPA for candidate responses. (Section 1)
  - [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf)
