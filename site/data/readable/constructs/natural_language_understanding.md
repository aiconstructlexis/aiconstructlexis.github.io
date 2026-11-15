# Natural language understanding
**Type:** Construct  
**Supporting papers:** 306  
**Also known as:** Language understanding, Natural Language Understanding, Language comprehension, Natural language comprehension, Linguistic understanding, General language understanding, Text comprehension, Input comprehension, Text-level understanding, Text understanding  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats natural language understanding as a latent model ability or capacity to comprehend, interpret, and process human language or text across tasks. Many definitions stay broad, covering sentence meaning, context, nuance, intent, instructions, and semantic content, while narrower formulations tie it to specific settings such as interpreting puzzle rules, open-ended user commands, natural-language questions for formal conversion, tabular queries, or problem descriptions for optimization. A recurring disagreement is whether it is a latent property of the model or an observable performance profile: some papers define it directly as performance on classification, inference, similarity, acceptability, question answering, or related task families rather than as an internal capacity.

**Space of facets.** Most papers use neighboring labels almost interchangeably, especially language understanding, language comprehension, linguistic understanding, text understanding, and text comprehension. A smaller line of work carves out narrower facets, including input comprehension, correct interpretation before generation, text-level understanding of natural-language descriptions in neural architecture search, and entity tracking as a facet of language comprehension; another paper distinguishes culture-agnostic language understanding from cultural understanding. Papers also sometimes nest task families under the construct, with natural language inference presented as a popular way to evaluate it, and with broader variants such as general language understanding extending it to reasoning, comprehension, and knowledge recall.

**Space of measurement.** Operationalization is overwhelmingly benchmark-based. Papers link natural language understanding to 35 measurement instruments and 11 behavioral indicators, most often GLUE, MMLU, HellaSwag, ARC-Challenge, and OpenBookQA, with 30 other instruments covering further benchmark suites, task datasets, and evaluation frameworks. These measurements make the construct concrete as performance on sentence classification, textual entailment or inference, paraphrase and semantic similarity, acceptability judgment, multiple-choice question answering, reading or passage comprehension, multilingual comprehension, and text-based embodied tasks; several papers explicitly state that GLUE tests NLU ability, MMLU assesses breadth and depth of language understanding across subjects, and HellaSwag measures the ability to understand language. This often narrows broad definitions of latent comprehension into observable scores on task collections, though some operationalizations stay closer to instruction or passage comprehension.

**Links.** Papers link it to 11 behavioral indicators and 3 constructs. Causal claims are sparse: one paper claims causal relationships from natural language understanding to paraphrastic robustness, harmful content detection, and jailbreak prompt generation, and another claims a causal relationship from question-answer pair generation to natural language understanding. Other papers report that it is related to reasoning, with the remaining related links spanning nine other behaviors and tasks; no correlational link is reported.

## Sources

**Natural language understanding** (24 papers: [Fast-ELECTRA for Efficient Pre-training](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e5f58d98523298cba093f658cfdf2d6-Paper-Conference.pdf), [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf), [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf), [Large Language Models as Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/3339f19c5fcee3ad74502947a32be9e6-Paper-Conference.pdf), [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf), [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf), [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf), [ESPACE: Dimensionality Reduction of Activations for Model Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6591cc41be737e9ba4cc487ac8082d-Paper-Conference.pdf), [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf), [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf), [Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque](https://aclanthology.org/2025.naacl-long.629.pdf), [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf), [Lost in Inference: Rediscovering the Role of Natural Language Inference for Large Language Models](https://aclanthology.org/2025.naacl-long.466.pdf), [Language Models are Crossword Solvers](https://aclanthology.org/2025.naacl-long.104.pdf), [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf), [Diversify-verify-adapt: Efficient and Robust Retrieval-Augmented Ambiguous Question Answering](https://aclanthology.org/2025.naacl-long.56.pdf), [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf), [Investigating the (De)Composition Capabilities of Large Language Models in Natural-to-Formal Language Conversion](https://aclanthology.org/2025.naacl-long.87.pdf), [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf), [BelarusianGLUE: Towards a Natural Language Understanding Benchmark for Belarusian](https://aclanthology.org/2025.acl-long.25.pdf), [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf), [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf))
> The ability of a model to comprehend and interpret human language across a range of tasks.

**Language understanding** (16 papers: [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf), [TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf), [Towards Quantifying Commonsense Reasoning with Mechanistic Insights](https://aclanthology.org/2025.naacl-long.487.pdf), [SANDWiCH: Semantical Analysis of Neighbours for Disambiguating Words in Context ad Hoc](https://aclanthology.org/2025.naacl-long.358.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models](https://aclanthology.org/2025.naacl-long.139.pdf), [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf), [On the Analysis and Distillation of Emergent Outlier Properties in Pre-trained Language Models](https://aclanthology.org/2025.naacl-long.430.pdf), [AlgoPuzzleVQA: Diagnosing Multimodal Reasoning Challenges of Language Models with Algorithmic Multimodal Puzzles](https://aclanthology.org/2025.naacl-long.486.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf), [JMMMU: A Japanese Massive Multi-discipline Multimodal Understanding Benchmark for Culture-aware Evaluation](https://aclanthology.org/2025.naacl-long.43.pdf), [Bayelemabaga: Creating Resources for Bambara NLP](https://aclanthology.org/2025.naacl-long.602.pdf), [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf), [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf), [Fusing Highly Specialized Language Models for Comprehensive Expertise](https://aclanthology.org/2025.acl-long.42.pdf), [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abnar25a/abnar25a.pdf))
> The general capability of a model to comprehend and process textual information, which is a prerequisite for interpreting puzzle rules and states.

**Natural Language Understanding** (1 paper: [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf))
> The latent capacity to comprehend and interpret natural language text and instructions.

**Language comprehension** (2 papers: [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50e9ad960ae78b741a6b4fea533f2eaf-Paper-Conference.pdf), [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.322.pdf))
> The fundamental ability to process and interpret the meaning of written or spoken language.

**Natural language comprehension** (1 paper: [EditRoom: LLM-parameterized Graph Diffusion for Composable 3D Room Layout Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/d807e7678ba3afd3a904f4af52819e77-Paper-Conference.pdf))
> The ability to interpret open-ended user commands and convert them into actionable internal representations for downstream execution.

**Linguistic understanding** (2 papers: [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf), [CrafText Benchmark: Advancing Instruction Following in Complex Multimodal Open-Ended World](https://aclanthology.org/2025.acl-long.1267.pdf))
> The model's ability to comprehend and interpret the meaning, intent, and nuances of natural language questions and contexts.

**General language understanding** (1 paper: [Nemotron-CC: Transforming Common Crawl into a Refined Long-Horizon Pretraining Dataset](https://aclanthology.org/2025.acl-long.123.pdf))
> The latent ability of a language model to comprehend and perform well across a diverse range of natural language tasks involving reasoning, comprehension, and knowledge recall.

**Text understanding** (3 papers: [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://proceedings.iclr.cc/paper_files/paper/2024/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf), [Improving Clustering with Positive Pairs Generated from LLM-Driven Labels](https://aclanthology.org/2025.emnlp-main.613.pdf), [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf))
> The model's ability to comprehend the meaning, context, and nuances of written language.

**Text comprehension** (2 papers: [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf), [Basic Reading Distillation](https://aclanthology.org/2025.acl-long.1472.pdf))
> The ability to process textual information, understand its meaning, and extract relevant details to answer questions or perform tasks.

**Input comprehension** (1 paper: [From Input Perception to Predictive Insight: Modeling Model Blind Spots Before They Become Errors](https://aclanthology.org/2025.emnlp-main.1740.pdf))
> The latent ability of a language model to correctly interpret the meaning of an input sequence, particularly in context-sensitive or non-literal constructions, prior to generating any output.

**Text-level understanding** (1 paper: [RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ji25a/ji25a.pdf))
> The latent ability of the LLM to comprehend and reason about neural architecture search tasks through natural language descriptions of search spaces, network construction, and evaluation methods.

## Relationships

### Natural language understanding →
- **GLUE** (measurement instrument): *measured_by*, 42 papers
  > We compare our approach with LoRA and other parameter-efficient adaptation methods on the natural language understanding (GLUE) and natural language generation (E2E) benchmarks... (Section 1)
  - [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf)
  - [Fast-ELECTRA for Efficient Pre-training](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e5f58d98523298cba093f658cfdf2d6-Paper-Conference.pdf)
  - [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf)
  - [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf)
  - [A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf)
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
  - [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf)
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
  - [VB-LoRA: Extreme Parameter Efficient Fine-Tuning with Vector Banks](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e0d38c676d5855bcfab7f6d29d20ad9-Paper-Conference.pdf)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [Bridging The Gap between Low-rank and Orthogonal Adaptation via Householder Reflection Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf)
  - [Unveiling LoRA Intrinsic Ranks via Salience Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9f00cb7dd5fbdc2175d55e2fdf1b05-Paper-Conference.pdf)
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
  - [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf)
  - [LoQT: Low-Rank Adapters for Quantized Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0c6bc641a56bebee9d985b937307367-Paper-Conference.pdf)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [FouRA: Fourier Low-Rank Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/83960718b4d12f799985206f1b1cf00f-Paper-Conference.pdf)
  - [Decoupling Angles and Strength in Low-rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3379ce104189b72d5f7baaa03ae81329-Paper-Conference.pdf)
  - [Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf)
  - [Efficient Learning with Sine-Activated Low-Rank Matrices](https://proceedings.iclr.cc/paper_files/paper/2025/file/112d8e0c7563de6e3408b49a09b4d8a3-Paper-Conference.pdf)
  - [Selective Aggregation for Low-Rank Adaptation in Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53a37f820d5be5930415d964f4a0187-Paper-Conference.pdf)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
  - [LoCA: Location-Aware Cosine Adaptation for Parameter-Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/d63d7d489a9338afff53d17410ea2c10-Paper-Conference.pdf)
  - [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf)
  - [Quantum-PEFT: Ultra parameter-efficient fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e52bbb99690d1e05c7ef7b4c8b3569a-Paper-Conference.pdf)
  - [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [The LLM Language Network: A Neuroscientific Approach for Identifying Causally Task-Relevant Units](https://aclanthology.org/2025.naacl-long.544.pdf)
  - [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf)
  - [LoRA-One: One-Step Full Gradient Could Suffice for Fine-Tuning Large Language Models, Provably and Efficiently](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ax/zhang25ax.pdf)
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)
  - [LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf)
  - [Make LoRA Great Again: Boosting LoRA with Adaptive Singular Values and Mixture-of-Experts Optimization Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25g/fan25g.pdf)
  - [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf)
  - [Beyond Zero Initialization: Investigating the Impact of Non-Zero Initialization on LoRA Fine-Tuning Dynamics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bm/li25bm.pdf)
  - [Scalable Model Merging with Progressive Layer-wise Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25r/xu25r.pdf)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf)
  - [NeuroAda: Activating Each Neuron's Potential for Parameter-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.555.pdf)
  - [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf)
- **MMLU** (measurement instrument): *measured_by*, 19 papers
  > To demonstrate the effectiveness of SPA in the natural language understanding domain, we evaluate its performance on several diverse tasks, including Big-Bench Hard (BBH) (Suzgun et al., 2022), GPQA (Rein et al., 2023), MMLU (Hendrycks et al., 2020), and WinoGrande (Sakaguchi et al., 2019).
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
  - [Understanding In-Context Learning from Repetitions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d88f6f81e1aaf606776ffdd06fdf24ef-Paper-Conference.pdf)
  - [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
  - [TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nuti25a/nuti25a.pdf)
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)
  - [Direct Density Ratio Optimization: A Statistically Consistent Approach to Aligning Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/higuchi25a/higuchi25a.pdf)
  - [What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-Only LLMs](https://aclanthology.org/2025.emnlp-main.481.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 9 papers
  > A diverse set of benchmarks containing Piqa (Bisk et al., 2019), ARC-c, ARC-e (Clark et al., 2018), Hellaswag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021) and Winogrande (Sakaguchi et al., 2019), which collectively evaluate the language comprehension and reasoning faculties of LLMs. (Section 5.1)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [ALLaM: Large Language Models for Arabic and English](https://proceedings.iclr.cc/paper_files/paper/2025/file/54c15a3033686e7999aecd2740c5a7c4-Paper-Conference.pdf)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
  - [HMoE: Heterogeneous Mixture of Experts for Language Modeling](https://aclanthology.org/2025.emnlp-main.1115.pdf)
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [fMRI predictors based on language models of increasing complexity recover brain left lateralization](https://proceedings.neurips.cc/paper_files/paper/2024/file/e28e19d00b23fe0265f433fa05a96b06-Paper-Conference.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
  - [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 6 papers
  > A diverse set of benchmarks containing Piqa (Bisk et al., 2019), ARC-c, ARC-e (Clark et al., 2018), Hellaswag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021) and Winogrande (Sakaguchi et al., 2019), which collectively evaluate the language comprehension and reasoning faculties of LLMs. (Section 5.1)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 6 papers
  > To evaluate multitask performance, we test on several NLP benchmarks, including MMLU (Hendrycks et al., 2020), MMLU-Pro (Wang et al., 2024), ARC-Easy, ARC-Challenge (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018), SWAG (Zellers et al., 2018), and CommonsenseQA (Talmor et al., 2018). These benchmarks consist of multiple-choice questions, assessing various aspects of the model's natural language understanding.
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
  - [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
  - [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 5 papers
  > These benchmarks consist of multiple-choice questions, assessing various aspects of the model's natural language understanding. For MMLU and MMLU-Pro, we use macro accuracy...
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf)
  - [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.727.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 5 papers
  > To demonstrate the effectiveness of SPA in the natural language understanding domain, we evaluate its performance on several diverse tasks, including Big-Bench Hard (BBH) (Suzgun et al., 2022), GPQA (Rein et al., 2023), MMLU (Hendrycks et al., 2020), and WinoGrande (Sakaguchi et al., 2019).
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 4 papers
  > A diverse set of benchmarks containing Piqa (Bisk et al., 2019), ARC-c, ARC-e (Clark et al., 2018), Hellaswag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021) and Winogrande (Sakaguchi et al., 2019), which collectively evaluate the language comprehension and reasoning faculties of LLMs. (Section 5.1)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 4 papers
  > BBH tasks cover a diverse range of reasoning problems spanning the following 4 categories according to their authors: 1) Algorithmic and Multi-Step Arithmetic Reasoning, 2) Natural Language Understanding, 3) Use of World Knowledge, and 4) Multilingual Knowledge and Reasoning.
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 4 papers
  > A diverse set of benchmarks containing Piqa (Bisk et al., 2019), ARC-c, ARC-e (Clark et al., 2018), Hellaswag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021) and Winogrande (Sakaguchi et al., 2019), which collectively evaluate the language comprehension and reasoning faculties of LLMs. (Section 5.1)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
  - [HMoE: Heterogeneous Mixture of Experts for Language Modeling](https://aclanthology.org/2025.emnlp-main.1115.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 4 papers
  > ...language understanding (HellaSwag (Zellers et al., 2019), BoolQ (Clark et al., 2019), OpenbookQA (Mihaylov et al., 2018), SQuAD (Rajpurkar et al., 2016), MMLU (Hendrycks et al., 2021), MMLU-Pro (Wang et al., 2024), GPQA(Rein et al., 2023)) (Section 3).
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
  - [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf)
  - [HMoE: Heterogeneous Mixture of Experts for Language Modeling](https://aclanthology.org/2025.emnlp-main.1115.pdf)
- **CoLA** (measurement instrument): *measured_by*, 4 papers
  > In the realm of NLU, we utilized the CoLA (Warstadt et al., 2019), RTE (Poliak, 2020), MNLI (Williams et al., 2018), MRPC (Dolan & Brockett, 2005) datasets from GLUE benchmark (Wang et al., 2018) to evaluate the performance of UniCoTT (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
  - [HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
  - [LoRA-One: One-Step Full Gradient Could Suffice for Fine-Tuning Large Language Models, Provably and Efficiently](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ax/zhang25ax.pdf)
- **SuperGLUE** (measurement instrument): *measured_by*, 3 papers
  > We assess the effectiveness of MPDistil using two natural language understanding benchmarks, SuperGLUE (Wang et al., 2019) and GLUE (Wang et al., 2018), encompassing 15 NLU tasks. (Section 1)
  - [A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf)
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.563.pdf)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 3 papers
  > exceeding the performance of AR models in text quality and on the LAMBADA natural language understanding benchmark.
  - [Beyond Autoregression: Fast LLMs via Self-Distillation Through Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f93c3e9b557980d93016671acd94bd2-Paper-Conference.pdf)
  - [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **RTE** (measurement instrument): *measured_by*, 2 papers
  > In the realm of NLU, we utilized the CoLA (Warstadt et al., 2019), RTE (Poliak, 2020), MNLI (Williams et al., 2018), MRPC (Dolan & Brockett, 2005) datasets from GLUE benchmark (Wang et al., 2018) to evaluate the performance of UniCoTT (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 2 papers
  > The results show no significant losses of general ability like natural language understanding after aligning with the embodied environment... Table 2: Zero-shot performance on Language Model Evaluation Harness [56]
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **GPQA** (measurement instrument): *measured_by*, 2 papers
  > To demonstrate the effectiveness of SPA in the natural language understanding domain, we evaluate its performance on several diverse tasks, including Big-Bench Hard (BBH) (Suzgun et al., 2022), GPQA (Rein et al., 2023), MMLU (Hendrycks et al., 2020), and WinoGrande (Sakaguchi et al., 2019).
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **HumanEval** (measurement instrument): *measured_by*, 2 papers
  > HumanEval [6] is a dataset for evaluating code generation ability, containing 164 manually crafted programming problems covering aspects such as language understanding, reasoning, algorithms, and simple mathematics.
  - [Parameter Competition Balancing for Model Merging](https://proceedings.neurips.cc/paper_files/paper/2024/file/99fc8bc48b917c301a80cb74d91c0c06-Paper-Conference.pdf)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
- **Lambada-OpenAI** (measurement instrument): *measured_by*, 2 papers
  > Language Understanding (LU): Lambada-OpenAI [44], Hellaswag-0-shot [65], Winograd-3-shots [30], and WinoGrande-5-shots [54].
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abnar25a/abnar25a.pdf)
- **MNLI** (measurement instrument): *measured_by*, 1 paper
  > In the realm of NLU, we utilized the CoLA (Warstadt et al., 2019), RTE (Poliak, 2020), MNLI (Williams et al., 2018), MRPC (Dolan & Brockett, 2005) datasets from GLUE benchmark (Wang et al., 2018) to evaluate the performance of UniCoTT (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **MRPC** (measurement instrument): *measured_by*, 1 paper
  > In the realm of NLU, we utilized the CoLA (Warstadt et al., 2019), RTE (Poliak, 2020), MNLI (Williams et al., 2018), MRPC (Dolan & Brockett, 2005) datasets from GLUE benchmark (Wang et al., 2018) to evaluate the performance of UniCoTT (Section 4.1).
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **QNLI** (measurement instrument): *measured_by*, 1 paper
  > The experiments involved 4 NLU benchmarks: RTE (Wang et al., 2019), COLA (Wang et al., 2019), 20NG (Lang, 1995) and QNLI (Wang et al., 2019) (Section 4).
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **GLUE-X** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on both zero-shot and few-shot settings of natural language understanding and question answering (QA). SuperContext is validated on a comprehensive OOD benchmarks GLUE-X (Yang et al., 2022), and a QA dataset, SQuAD 2.0 (Rajpurkar et al., 2018). (Section 2)
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
- **SWAG** (measurement instrument): *measured_by*, 1 paper
  > To evaluate multitask performance, we test on several NLP benchmarks, including MMLU (Hendrycks et al., 2020), MMLU-Pro (Wang et al., 2024), ARC-Easy, ARC-Challenge (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018), SWAG (Zellers et al., 2018), and CommonsenseQA (Talmor et al., 2018). These benchmarks consist of multiple-choice questions, assessing various aspects of the model's natural language understanding.
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 1 paper
  > To evaluate multitask performance, we test on several NLP benchmarks, including MMLU (Hendrycks et al., 2020), MMLU-Pro (Wang et al., 2024), ARC-Easy, ARC-Challenge (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018), SWAG (Zellers et al., 2018), and CommonsenseQA (Talmor et al., 2018). These benchmarks consist of multiple-choice questions, assessing various aspects of the model's natural language understanding.
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **LiveBench** (measurement instrument): *measured_by*, 1 paper
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **20 Newsgroups** (measurement instrument): *measured_by*, 1 paper
  > The experiments involved 4 NLU benchmarks: RTE (Wang et al., 2019), COLA (Wang et al., 2019), 20NG (Lang, 1995) and QNLI (Wang et al., 2019) (Section 4).
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **MLQA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our methods on unlearning math-solving, Python-coding, and comprehension skills across seven different languages with GSM8K, MBPP, and MLQA datasets respectively. (Section 6)
  - [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.322.pdf)
- **ALFWorld** (measurement instrument): *measured_by*, 1 paper
  > ALFWorld (Shridhar et al., 2020) provides a text-based household task environment that for natural language understanding and embodied reasoning. (Section 5.1)
  - [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf)
- **Paraphrastic robustness** (construct): *causes*, 1 paper
  > Althought this is expected for paraphrastic robustnes as LLMs are known for their language understanding capabilities, it is somewhat surprising to see that the LLM helps even for novel behaviors...
  - [Large Language Models as Generalizable Policies for Embodied Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/8f9461d11e8ce9b0b28b21bfc645d74e-Paper-Conference.pdf)
- **TACT** (measurement instrument): *measured_by*, 1 paper
  > The resulting TACT instances consist of the original text, the written instruction, and a gold answer, all requiring advanced text comprehension and reasoning (illustrated in Figure 1). (Section 1)
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmful content detection** (behavioral indicator): *causes*, 1 paper
  > text comprehension plays a more crucial role than image understanding in the detection of harmful memes.
  - [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf)
- **RACE** (measurement instrument): *measured_by*, 1 paper
  > Different datasets including... language understanding and knowledge such as... Race-Middle, Race-High [60]... are comprehensively evaluated. (Section 4)
  - [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf)
- **Belebele** (measurement instrument): *measured_by*, 1 paper
  > After numerous SFT runs on these “generic” multi-task datasets, the three checkpoints for each language are primarily selected based off their performance on the target language splits on BELEBELE (Bandarkar et al., 2024) and FLORES (NLLB et al., 2022). These simple tasks, reading comprehension and translation, are strong indicators of basic language understanding and generation capabilities. (Section 3.1)
  - [Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f9a44cb707ede42a659ad85d940dd55-Paper-Conference.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 1 paper
  > ...language understanding (HellaSwag (Zellers et al., 2019), BoolQ (Clark et al., 2019), OpenbookQA (Mihaylov et al., 2018), SQuAD (Rajpurkar et al., 2016), MMLU (Hendrycks et al., 2021), MMLU-Pro (Wang et al., 2024), GPQA(Rein et al., 2023)) (Section 3).
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > Additionally, we employ comprehensive benchmarks for different tasks, including MTBench (Zheng et al., 2023) to compare their language understanding and reasoning capabilities across different quantizations. (Section 3.1)
  - [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf)
- **Jailbreak prompt generation** (behavioral indicator): *causes*, 1 paper
  > we can fine-tune an existing language model, turning it into a robust jailbreak prompt generator by leveraging LLMs’ advanced language understanding and generation abilities. (INTRODUCITON)
  - [One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf)
- **TweetEval** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on two multi-task benchmarks, TweetEval and AffectEval for language understanding. (Section 1)
  - [Impartial Multi-task Representation Learning via Variance-invariant Probabilistic Decoding](https://aclanthology.org/2025.acl-long.975.pdf)

### → Natural language understanding
- **Question-answer pair generation** (behavioral indicator): *causes*, 1 paper
  > Moreover, both objectives [rationale and QA] enhance the model’s language understanding, which we found to be important especially for the query split. (Section 4.3).
  - [Web-Scale Visual Entity Recognition: An LLM-Driven Data Approach](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d158f054ff0cb83397367234899db07-Paper-Conference.pdf)

### Associated with
- **Text-to-SQL** (behavioral indicator), 1 paper
  > Text-to-SQL generation provides an ideal middle ground, as SQL’s formal structure makes it more tractable than general language generation while still requiring natural language understanding. (Section 1)
  - [TinySQL: A Progressive Text-to-SQL Dataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1489.pdf)
- **Knowledge graph question answering** (behavioral indicator), 1 paper
  > KGQA poses challenges to existing approaches, as it requires a deep understanding of natural language questions and the ability to perform complex reasoning over KGs. (Section 1)
  - [D-RAG: Differentiable Retrieval-Augmented Generation for Knowledge Graph Question Answering](https://aclanthology.org/2025.emnlp-main.1793.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > For actions that require natural language understanding, such as composing a text message or querying a search engine, a VLM is invoked to generate the necessary text.
  - [Lightweight Neural App Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/b81266057eb3d96469940d1860a41ad2-Paper-Conference.pdf)
- **Word puzzle solving** (behavioral indicator), 1 paper
  > “Language Comprehension: Connections word puzzles, a typo-fixing task, and a movie synopsis unscrambling task”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Chronological ordering** (behavioral indicator), 1 paper
  > “Language Comprehension: Connections word puzzles, a typo-fixing task, and a movie synopsis unscrambling task”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Reasoning** (construct), 1 paper
  > recent studies indicate that the language understanding offered by these models remains limited and far from human-like performance, particularly in grasping the contextual meanings of words—an essential aspect of reasoning. (Abstract)
  - [SANDWiCH: Semantical Analysis of Neighbours for Disambiguating Words in Context ad Hoc](https://aclanthology.org/2025.naacl-long.358.pdf)
- **Table reasoning** (construct), 1 paper
  > Tabular reasoning involves interpreting natural language queries about tabular data, which presents a unique challenge of combining language understanding with structured data analysis.
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Textual reasoning** (behavioral indicator), 1 paper
  > Textual reasoning excels in natural language understanding
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Natural language inference** (behavioral indicator), 1 paper
  > In the recent past, a popular way of evaluating natural language understanding (NLU), was to consider a model’s ability to perform natural language inference (NLI) tasks. (Abstract)
  - [Lost in Inference: Rediscovering the Role of Natural Language Inference for Large Language Models](https://aclanthology.org/2025.naacl-long.466.pdf)
- **Ranking** (behavioral indicator), 1 paper
  > Passage reranking aims to assign fine-grained relevance scores to candidate passages – typically retrieved by a first-stage retriever (Robertson et al., 1994; Karpukhin et al., 2020) – by harnessing the language understanding capabilities of large language models (LLMs) (Section 1).
  - [Multi-view-guided Passage Reranking with Large Language Models](https://aclanthology.org/2025.emnlp-main.1459.pdf)
