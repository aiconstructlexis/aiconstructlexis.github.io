# SIQA
**Type:** Measurement instrument  
**Supporting papers:** 94  
**Also known as:** SOCIALIQA, Social IQA, Social IQa, SocialIQA, Social-IQa, Social-I-QA  

## State of the Field

**What it is.** Across papers, SIQA is most commonly described as a benchmark or dataset for multiple-choice question answering about social situations or interactions. Papers variously call it SocialIQA, Social IQA, Social Interaction QA, or Social-I-QA, and they usually describe it as testing social commonsense reasoning, including understanding people's actions, feelings, social implications or consequences, likely outcomes, human motivations, and reactions. Some papers frame it more broadly as a downstream task benchmark or a socio-emotional-skills evaluation item, and a smaller line adapts or re-annotates it, either using it to construct situational questions for another benchmark or using a version with Likert-scale answer plausibility ratings.

**What it is claimed to measure.** Papers use SIQA to measure 8 constructs and 1 behavioral indicator. The prevailing usage is to measure commonsense reasoning, often as one of several commonsense reasoning tasks; smaller lines of work report it as evaluating question answering, general ability, social and emotional intelligence, and social reasoning, with additional papers linking it to other constructs. Overall, the measurement claims center on commonsense reasoning but extend across multiple other framings.

**Space of uses.** Most papers position SIQA as one benchmark within broader evaluation suites, commonly alongside HellaSwag, PIQA, WinoGrande, and ARC, plus other commonsense benchmarks. Some papers use it as a downstream fine-tuning or question-answering task, a held-out out-of-domain check, or part of a socio-emotional evaluation subset. Papers explicitly link it to 1 other measurement instrument, OLMES, where it appears in a multiple-choice question answering suite.

**Concerns raised.** Concern-focused uses appear in work on data contamination and forgetting, where papers include Social-I-QA in evaluations of benchmark overfitting. Another paper uses a re-annotated version with Likert-scale ratings for each answer option to assess label plausibility and variation.

## Sources

**SocialIQA** (4 papers: [Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/725f5e8036cc08adeba4a7c3bcbc6f2c-Paper-Conference.pdf), [BIG5-CHAT: Shaping LLM Personalities Through Training on Human-Grounded Data](https://aclanthology.org/2025.acl-long.999.pdf), [Emergent Response Planning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25p/dong25p.pdf), [Playpen: An Environment for Exploring Learning From Dialogue Game Feedback](https://aclanthology.org/2025.emnlp-main.1517.pdf))
> A benchmark dataset used to evaluate the downstream task performance of large language models.

**SOCIALIQA** (1 paper: [Neuron based Personality Trait Induction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d399b67fa017f0f7670102c88507720c-Paper-Conference.pdf))
> A multiple-choice question answering benchmark for social commonsense reasoning, used in this paper as a basis for constructing evaluation questions for PERSONALITYBENCH.

**Social IQA** (8 papers: [RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf), [Nemotron-CC: Transforming Common Crawl into a Refined Long-Horizon Pretraining Dataset](https://aclanthology.org/2025.acl-long.123.pdf), [Demystifying Domain-adaptive Post-training for Financial LLMs](https://aclanthology.org/2025.emnlp-main.1579.pdf), [From Language to Cognition: How LLMs Outgrow the Human Language Network](https://aclanthology.org/2025.emnlp-main.1237.pdf), [Stimulate the Critical Thinking of LLMs via Debiasing Discussion](https://aclanthology.org/2025.emnlp-main.579.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf), [Threading the Needle: Reweaving Chain-of-Thought Reasoning to Explain Human Label Variation](https://aclanthology.org/2025.emnlp-main.1682.pdf), [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf))
> A benchmark for commonsense reasoning that involves choosing the most likely answer to questions about social situations.

**SIQA** (17 papers: [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf), [SLIM: Let LLM Learn More and Forget Less with Soft LoRA and Identity Mixture](https://aclanthology.org/2025.naacl-long.246.pdf), [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf), [Sparser Mixture-of-Adapters with Cross-Layer Generalization](https://aclanthology.org/2025.naacl-long.201.pdf), [Efficient Pretraining Data Selection for Language Models via Multi-Actor Collaboration](https://aclanthology.org/2025.acl-long.466.pdf), [HD-PiSSA: High-Rank Distributed Orthogonal Adaptation](https://aclanthology.org/2025.emnlp-main.330.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf), [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf), [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf), [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf), [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf), [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf), [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf), [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf), [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf), [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf), [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf))
> The Social Interaction QA (SIQA) benchmark, which tests commonsense reasoning about social situations through multiple-choice questions.

**Social IQa** (2 papers: [Divergences between Language Models and Human Brains](https://proceedings.neurips.cc/paper_files/paper/2024/file/f96839fc751b67492e17e70f5c9730e4-Paper-Conference.pdf), [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf))
> A multiple-choice dataset of questions about people’s feelings and social implications, used here for fine-tuning on social/emotional content.

**Social-I-QA** (1 paper: [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf))
> Commonsense reasoning benchmark involving social interactions, used to assess model performance under contamination and forgetting conditions.

## Relationships

### → SIQA
- **Commonsense reasoning** (construct): *measured_by*, 24 papers
  > Commonsense Reasoning (0-shot): HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019)... (Section 4.2).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [Unleashing the Power of Task-Specific Directions in Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c3d101702194a5a345d81cdee4fe966f-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/abbbb25cddb2c2cd08714e6bfa2f0634-Paper-Conference.pdf)
  - [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf)
  - [Efficient Learning with Sine-Activated Low-Rank Matrices](https://proceedings.iclr.cc/paper_files/paper/2025/file/112d8e0c7563de6e3408b49a09b4d8a3-Paper-Conference.pdf)
  - [ComLoRA: A Competitive Learning Approach for Enhancing LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/e993102e60e4484686f0bafe7ba8b8f2-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
  - [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf)
  - [DenseLoRA: Dense Low-Rank Adaptation of Large Language Models](https://aclanthology.org/2025.acl-long.503.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [Tracing and Dissecting How LLMs Recall Factual Knowledge for Real World Questions](https://aclanthology.org/2025.acl-long.1133.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf)
  - [An Orthogonal High-Rank Adaptation for Large Language Models](https://aclanthology.org/2025.emnlp-main.951.pdf)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-Only LLMs](https://aclanthology.org/2025.emnlp-main.481.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 3 papers
  > OLMo-30M models trained on various pre-training token budgets are fine-tuned on downstream tasks using fixed hyperparameters: math (GSM8k), code (Starcoder-Python), and QA (SIQA). (Figure 4)
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **General ability** (construct): *measured_by*, 2 papers
  > Ultimately, we select the following benchmarks as our downstream tasks: Social IQA (Sap et al., 2019), HellaSwag (Zellers et al., 2019), PiQA (Bisk et al., 2020), OpenBookQA (Mihaylov et al., 2018), Lambada (Paperno et al., 2016), SciQ (Welbl et al., 2017), ARC Easy (Clark et al., 2018), COPA (Sarlin et al., 2020), RACE (Lai et al., 2017), LogiQA (Liu et al., 2020), QQP (Wang et al., 2018), WinoGrande (Sakaguchi et al., 2021), and MultiRC (Khashabi et al., 2018). (Section 5)
  - [RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **Social and emotional intelligence** (construct): *measured_by*, 2 papers
  > We study social and emotional intelligence using the Social IQa dataset [Sap et al., 2019]. (Section 5.1)
  - [Divergences between Language Models and Human Brains](https://proceedings.neurips.cc/paper_files/paper/2024/file/f96839fc751b67492e17e70f5c9730e4-Paper-Conference.pdf)
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
- **Social reasoning** (construct): *measured_by*, 2 papers
  > SIQA (Sap et al., 2019) and PIQA (Bisk et al., 2020) looks for social and physical reasoning, respectively. (Section 4.1)
  - [NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/db6461eaf0eaeaad1d9c4a70e4818cbd-Paper-Conference.pdf)
  - [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > For reasoning abilities, we use ARC-Easy, ARC-Challenge [42], SIQA [43], PIQA [44], WinoGrande [45], and QUAC [46] (all 0-shot).
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **Benchmark overfitting** (construct): *measured_by*, 1 paper
  > We evaluate the impact of data contamination using a mix of seven different benchmarks: ARC-Easy (Clark et al., 2018), Social-I-QA (Sap et al., 2019), WinoGrande (Sakaguchi et al., 2021), PiQA (Bisk et al., 2020), BoolQ (Clark et al., 2019), MMLU (Hendrycks et al., 2021), and HellaSwag (Zellers et al., 2019). (Section 3.2)
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **Functional linguistic competence** (construct): *measured_by*, 1 paper
  > To assess this, we use six benchmarks covering... social reasoning (SOCIAL IQA (Sap et al., 2019)) (Section 3.3)
  - [From Language to Cognition: How LLMs Outgrow the Human Language Network](https://aclanthology.org/2025.emnlp-main.1237.pdf)
- **Social intelligence** (construct): *measured_by*, 1 paper
  > We evaluated these models on six different benchmarks ... including PIQA (Bisk et al., 2020), hellaswag (Zellers et al., 2019), BoolQ (Clark et al., 2019), ARC (Clark et al., 2018), winogrande (Sakaguchi et al., 2021) and SIQA (Sap et al., 2019). These tasks examine models’ language understanding, logical reasoning, knowledge utilization, and social awareness capabilities.
  - [HMoE: Heterogeneous Mixture of Experts for Language Modeling](https://aclanthology.org/2025.emnlp-main.1115.pdf)

### Associated with
- **OLMES** (measurement instrument), 1 paper
  > "We use the OLMES suite of 10 multiple choice question answering benchmarks (Gu et al., 2024): ... SocialIQA (Sap et al., 2019), OpenBookQA ..."
  - [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf)
