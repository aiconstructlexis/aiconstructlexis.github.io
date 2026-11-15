# Multiple-choice question answering
**Type:** Behavioral indicator  
**Supporting papers:** 306  
**Also known as:** Multi-choice question answering, Multiple-choice answering, Single-choice question answering, Multiple-selection question answering, Multiple Choice Question, Answer selection, Multiple-choice classification, Multiple-choice reasoning, Multiple-choice examination, Fixed-choice question answering  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing is selecting the correct answer from a fixed set of options for a question, most often a single option in a discrete format such as A/B/C/D. Success is usually matching a predefined correct answer, and many papers ask the model to output only the option symbol or index, though some accept the choice value itself, a label such as Yes, No, or Not Sure Enough, or treat the answer as valid even when the format is wrong. A smaller line casts the behavior as classification over option tokens or answer strings, often by selecting the candidate with the highest predicted likelihood or conditional log probability.

**Variants.** Papers use nearby names such as multi-choice question answering, multiple-choice answering, single-choice question answering, fixed-choice question answering, answer selection, multiple-choice classification, and multiple-choice reasoning. The prevailing variant still has one correct option, often among four choices, but papers also study settings with two to ten options, multiple correct answers, abstention as a fifth option, or multiple-selection across instruction chains. The task appears in many domains and modalities, including commonsense and science exams, medical and clinical cases, finance and culture, code and API invocation, survey questions, long-context reading, images and videos, speech inputs, spatial relations, and procedural next-step prediction.

**Space of elicitation and scores.** Papers measure this behavior with 46 linked instruments. The most recurrent are MMLU, ARC-Challenge, CommonsenseQA, ARC, and HellaSwag, followed by other academic, commonsense, factuality, multilingual, long-context, medical, and multimodal benchmarks. These instruments are usually benchmark datasets or evaluation suites, and scoring is most commonly reported as accuracy on the selected option, often by comparing the chosen answer to ground truth or by taking the option with the highest likelihood, though some papers also mention exact match, softmax-normalized option scores, and constrained decoding to valid options.

**What it is taken as evidence of.** When papers connect this behavior to broader constructs, the most common links are to Commonsense reasoning, Positional bias, Calibration, Emergent abilities, and Medical knowledge, across 7 linked constructs overall. The usage is not unified around one construct: papers usually report it as related to these constructs rather than as a single agreed indicator, for example using MCQ settings for commonsense or low-level medical knowledge tasks, or discussing how option choice interacts with bias, calibration, and claims about emergent abilities.

## Sources

**Multiple-choice question answering** (56 papers: [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf), [AutoCast++: Enhancing World Event Prediction with Zero-shot Ranking-based Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/93f01c8d9b355d7bbe3f353b44ccde66-Paper-Conference.pdf), [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf), [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf), [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf), [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf), [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf), [Group Preference Optimization: Few-Shot Alignment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/ffd4f5a2ea6b93e9bf5af9264d568cf2-Paper-Conference.pdf), [Knowledge Fusion of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4fd5cfd2e31bebbccfa5ffa354c04bdc-Paper-Conference.pdf), [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf), [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf), [Measuring Vision-Language STEM Skills of Neural Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a3a661eb3308d0bb686f6a4bac521032-Paper-Conference.pdf), [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf), [Predicting Emergent Abilities with Infinite Resolution Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e6d14709eae0cbc49a1d19d87fb8b21-Paper-Conference.pdf), [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf), [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf), [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf), [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf), [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf), [Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf), [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf), [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf), [Towards Quantifying Commonsense Reasoning with Mechanistic Insights](https://aclanthology.org/2025.naacl-long.487.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [Soft Prompting for Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.204.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf), [Few-shot Personalization of LLMs with Mis-aligned Responses](https://aclanthology.org/2025.naacl-long.598.pdf), [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf), [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf), [PerCul: A Story-Driven Cultural Evaluation of LLMs in Persian](https://aclanthology.org/2025.naacl-long.631.pdf), [CFinBench: A Comprehensive Chinese Financial Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.40.pdf), [Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.182.pdf), [Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations](https://aclanthology.org/2025.naacl-long.162.pdf), [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf), [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318.pdf), [LLMs Are Biased Towards Output Formats! Systematically Evaluating and Mitigating Output Format Bias of LLMs](https://aclanthology.org/2025.naacl-long.15.pdf), [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf), [CBT-Bench: Evaluating Large Language Models on Assisting Cognitive Behavior Therapy](https://aclanthology.org/2025.naacl-long.196.pdf), [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf), [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf), [MILU: A Multi-task Indic Language Understanding Benchmark](https://aclanthology.org/2025.naacl-long.507.pdf), [WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines](https://aclanthology.org/2025.naacl-long.167.pdf), [KMMLU: Measuring Massive Multitask Language Understanding in Korean](https://aclanthology.org/2025.naacl-long.206.pdf), [ITALIC: An Italian Culture-Aware Natural Language Benchmark](https://aclanthology.org/2025.naacl-long.68.pdf), [S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.475.pdf), [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.247.pdf), [LLMs Are Not Intelligent Thinkers: Introducing Mathematical Topic Tree Benchmark for Comprehensive Evaluation of LLMs](https://aclanthology.org/2025.naacl-long.161.pdf), [How Can We Diagnose and Treat Bias in Large Language Models for Clinical Decision-Making?](https://aclanthology.org/2025.naacl-long.114.pdf), [Improving Model Evaluation using SMART Filtering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.235.pdf), [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf), [CogLM: Tracking Cognitive Development of Large Language Models](https://aclanthology.org/2025.naacl-long.4.pdf), [Option Symbol Matters: Investigating and Mitigating Multiple-Choice Option Symbol Bias of Large Language Models](https://aclanthology.org/2025.naacl-long.95.pdf), [Can Multimodal Large Language Models Understand Spatial Relations?](https://aclanthology.org/2025.acl-long.31.pdf), [Impossible Videos](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25a/bai25a.pdf), [Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?](https://aclanthology.org/2025.emnlp-main.7.pdf), [Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf))
> The observable task of selecting the correct answer from a set of discrete options (e.g., A/B/C/D) in response to a given question.

**Multi-choice question answering** (7 papers: [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf), [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf), [QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models](https://aclanthology.org/2025.emnlp-main.271.pdf), [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf), [SpeechIQ: Speech-Agentic Intelligence Quotient Across Cognitive Levels in Voice Understanding by Large Language Models](https://aclanthology.org/2025.acl-long.1466.pdf), [Warmup Generations: A Task-Agnostic Approach for Guiding Sequence-to-Sequence Learning with Unsupervised Initial State Generation](https://aclanthology.org/2025.acl-long.434.pdf), [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf))
> The task of selecting the single correct option from a set of four choices in response to a question about a given grid, code, or programming concept.

**Multiple-choice answering** (4 papers: [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf), [Quantized but Deceptive? A Multi-Dimensional Truthfulness Evaluation of Quantized LLMs](https://aclanthology.org/2025.emnlp-main.1548.pdf), [MeteoRA: Multiple-tasks Embedded LoRA for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8951bbdcf234132bcce680825e7cb354-Paper-Conference.pdf), [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.183.pdf))
> Selecting the correct option from a set of choices based on provided context and question.

**Single-choice question answering** (1 paper: [Can Large Language Models Be Good Language Teachers?](https://aclanthology.org/2025.emnlp-main.1222.pdf))
> The observable task of selecting the single correct option from a list of choices in response to a question, often within a structured format.

**Multiple-selection question answering** (1 paper: [LoCt-Instruct: An Automatic Pipeline for Constructing Datasets of Logical Continuous Instructions](https://aclanthology.org/2025.emnlp-main.1734.pdf))
> Selecting all correct responses from a set of options for each sub-question in a multi-step instruction chain, where distractors increase complexity and test robustness.

**Multiple Choice Question** (1 paper: [CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25t/wang25t.pdf))
> A benchmark task in which the model selects the correct API invocation from four candidate invocations with one correct option and three distractors.

**Answer selection** (1 paper: [When LLMs Meet Cunning Texts: A Fallacy Understanding Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbfbf1a9adbcc29783475d2767f218e8-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of choosing the single correct explanation from a set of four provided candidate options in response to a given cunning text.

**Multiple-choice classification** (1 paper: [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf))
> The observable task of selecting the correct token or option from a set of candidates (e.g., A/B/C/D) given an input sequence.

**Multiple-choice reasoning** (2 papers: [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf), [RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ji25a/ji25a.pdf))
> The task of selecting the correct answer from a set of options for questions that require reasoning, often in a scientific or academic context.

**Multiple-choice examination** (1 paper: [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf))
> Selecting the correct answer from a set of options in a structured exam format across diverse domains.

**Fixed-choice question answering** (1 paper: [Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf))
> Selecting the correct answer from a given set of options in response to a question about a visual input.

## Relationships

### Multiple-choice question answering →
- **MMLU** (measurement instrument): *measured_by*, 34 papers
  > In the multiple-choice based datasets (ARC, RACE, HHH, MMLU), we consider the following approaches: (Section 3)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
  - [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf)
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
  - [Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf)
  - [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf)
  - [Embedding Trajectory for Out-of-Distribution Detection in Mathematical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b734e95f0788a030a69caa987516186-Paper-Conference.pdf)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
  - [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf)
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
  - [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
  - [On Bits and Bandits: Quantifying the Regret-Information Trade-off](https://proceedings.iclr.cc/paper_files/paper/2025/file/5efaaa07eb25eb4ab3e8754890f476bc-Paper-Conference.pdf)
  - [Task-Adaptive Pretrained Language Models via Clustered-Importance Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/688006b3d1df8be5bb2a2a31a407180c-Paper-Conference.pdf)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
  - [Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf)
  - [Limits to scalable evaluation at the frontier: LLM as judge won’t beat twice the data](https://proceedings.iclr.cc/paper_files/paper/2025/file/4264ee4376776907c0b87ed70b959585-Paper-Conference.pdf)
  - [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)
  - [LLMs Are Biased Towards Output Formats! Systematically Evaluating and Mitigating Output Format Bias of LLMs](https://aclanthology.org/2025.naacl-long.15.pdf)
  - [Option Symbol Matters: Investigating and Mitigating Multiple-Choice Option Symbol Bias of Large Language Models](https://aclanthology.org/2025.naacl-long.95.pdf)
  - [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.183.pdf)
  - [Improving Model Evaluation using SMART Filtering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.235.pdf)
  - [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf)
  - [DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation](https://aclanthology.org/2025.acl-long.358.pdf)
  - [RoToR: Towards More Reliable Responses for Order-Invariant Inputs](https://aclanthology.org/2025.acl-long.918.pdf)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)
  - [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chiang25a/chiang25a.pdf)
  - [On Zero-Initialized Attention: Optimal Prompt and Gating Factor Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diep25a/diep25a.pdf)
  - [Learning Safety Constraints for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25b/chen25b.pdf)
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
  - [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf)
  - [AdaptThink: Reasoning Models Can Learn When to Think](https://aclanthology.org/2025.emnlp-main.184.pdf)
  - [Towards Optimal Evaluation Efficiency for Large Language Models](https://aclanthology.org/2025.emnlp-main.716.pdf)
  - [Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements](https://aclanthology.org/2025.emnlp-main.1362.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 8 papers
  > We conduct experiments on MMLU (Hendrycks et al., 2020), ARC-Challenge (Clark et al., 2018), and CommonsenseQA (CSQA) (Talmor et al., 2019), which are all MCQ benchmarks widely used for LLM evaluation.
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
  - [Value-Incentivized Preference Optimization: A Unified Approach to Online and Offline RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2d80dc5b407e16b258abe3056402372-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation](https://aclanthology.org/2025.acl-long.358.pdf)
  - [Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?](https://aclanthology.org/2025.acl-long.722.pdf)
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
  - [Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.1474.pdf)
  - [Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements](https://aclanthology.org/2025.emnlp-main.1362.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 7 papers
  > We conduct experiments on MMLU (Hendrycks et al., 2020), ARC-Challenge (Clark et al., 2018), and CommonsenseQA (CSQA) (Talmor et al., 2019), which are all MCQ benchmarks widely used for LLM evaluation.
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
  - [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf)
  - [Taming Overconfidence in LLMs: Reward Calibration in RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/29fb6e1456b3d8b57ede5c45aa2c6537-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [Improving Model Evaluation using SMART Filtering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.235.pdf)
  - [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf)
- **ARC** (measurement instrument): *measured_by*, 5 papers
  > For MCQ answering, we use AI2 Reasoning Challenge (Clark et al., 2018, ARC), Massive Multitask Language Understanding (Hendrycks et al., 2021, MMLU), and Reward Bench Reasoning (Lambert et al., 2024, RWDB-R). (Section 4)
  - [Task-Adaptive Pretrained Language Models via Clustered-Importance Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/688006b3d1df8be5bb2a2a31a407180c-Paper-Conference.pdf)
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
  - [Improving Model Evaluation using SMART Filtering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.235.pdf)
  - [On Zero-Initialized Attention: Optimal Prompt and Gating Factor Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diep25a/diep25a.pdf)
  - [Hyperband-based Bayesian Optimization for Black-box Prompt Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schneider25b/schneider25b.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 4 papers
  > We experiment on two challenging real-world multiple-choice datasets from LLM benchmarks: HellaSwag (Zellers et al., 2019) and MMLU (Hendrycks et al., 2021). (Section 3.2).
  - [Answer, Assemble, Ace: Understanding How LMs Answer Multiple Choice Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c248154176c08147e82c0b30961604f7-Paper-Conference.pdf)
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
  - [On Zero-Initialized Attention: Optimal Prompt and Gating Factor Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diep25a/diep25a.pdf)
  - [Towards Optimal Evaluation Efficiency for Large Language Models](https://aclanthology.org/2025.emnlp-main.716.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 4 papers
  > “The MMLU-Pro dataset, while enhancing the complexity of MMLU by incorporating more challenging, reasoning-focused questions, remains constrained by the limitations of the multiple-choice format.”
  - [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad236edc564f3e3156e1b2feafb99a24-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf)
  - [Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf)
  - [DyePack: Provably Flagging Test Set Contamination in LLMs Using Backdoors](https://aclanthology.org/2025.emnlp-main.776.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 4 papers
  > For multiple-choice question tasks, we use the TruthfulQA [29] and FACTOR (Wiki) [33] datasets to assess the LLMs’ factuality (Section 3.1)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)
  - [On Zero-Initialized Attention: Optimal Prompt and Gating Factor Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diep25a/diep25a.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 3 papers
  > “The multiple-choice tasks include: ... open book question answering (OpenBookQA; Mihaylov et al. 2018)”
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?](https://aclanthology.org/2025.acl-long.722.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 3 papers
  > "We also re-examined data collected during the Pythia training runs [5] on the SciQ [73], PIQA [8], WinoGrande [60], and ARC Easy [18] datasets. Each of these consist of a wide range of questions with multiple-choice answers"
  - [LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf)
  - [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 3 papers
  > World Knowledge: MMLU [28] (5-shot), BBH [29] (3-shot), with the assessment based on the accuracy of multiple-choice answers. (Section 3.1).
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
  - [LLMs Are Biased Towards Output Formats! Systematically Evaluating and Mitigating Output Format Bias of LLMs](https://aclanthology.org/2025.naacl-long.15.pdf)
  - [DyePack: Provably Flagging Test Set Contamination in LLMs Using Backdoors](https://aclanthology.org/2025.emnlp-main.776.pdf)
- **SciQ** (measurement instrument): *measured_by*, 3 papers
  > The Science Questions (SciQ) dataset [73] consists of 13,679 crowdsourced multiple choice science exam questions ranging across physics, chemistry, biology, earth science, astronomy, and computer science. (Appendix E)
  - [LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf)
  - [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 3 papers
  > We evaluate all models on three tasks in this benchmark: summarization (En.Sum), long-book question answering (En.QA), and multi-choice question-answering (En.MC).
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
  - [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 2 papers
  > "We also re-examined data collected during the Pythia training runs [5] on the SciQ [73], PIQA [8], WinoGrande [60], and ARC Easy [18] datasets. Each of these consist of a wide range of questions with multiple-choice answers"
  - [LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 2 papers
  > We evaluate the pretrained models on language model tasks and multiple-choice tasks from LM evaluation Harness (Gao et al., 2023). (Section 5.3)
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
  - [MILU: A Multi-task Indic Language Understanding Benchmark](https://aclanthology.org/2025.naacl-long.507.pdf)
- **MedQA** (measurement instrument): *measured_by*, 2 papers
  > We also use MedQA, a collection of multiple-choice questions from the professional medical board exams (Jin et al., 2020).
  - [Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf)
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)
- **QuALITY** (measurement instrument): *measured_by*, 2 papers
  > Closed-ended tasks primarily focus on the capacity for understanding and reasoning within long contexts, including tasks like multiple-choice questions from QuALITY [5]... (Section 4.2).
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
  - [Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models](https://aclanthology.org/2025.emnlp-main.1656.pdf)
- **PIQA** (measurement instrument): *measured_by*, 2 papers
  > The Physical Interaction Question Answering (PIQA) dataset [8] contains a total of 21k (across different subsets) multiple choice questions probing reasoning about basic physical commonsense knowledge. (Appendix E)
  - [LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf)
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 2 papers
  > For the multiple-choice tasks, we use datasets: COPA (Gordon et al., 2012), StoryCloze (Mostafazadeh et al., 2016), NLI (Bowman et al., 2015), MMLU (Hendrycks et al., 2021), SST2 (Socher et al., 2013), SST5 (Socher et al., 2013), BoolQ (Clark et al., 2019), and Winogrande (Sakaguchi et al., 2020)... (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
  - [Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?](https://aclanthology.org/2025.acl-long.722.pdf)
- **MedMCQA** (measurement instrument): *measured_by*, 2 papers
  > Experiment results on the multiple-choice questions benchmarks in six languages range from different data ratios... MedMCQA
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)
  - [DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation](https://aclanthology.org/2025.acl-long.358.pdf)
- **GPQA** (measurement instrument): *measured_by*, 2 papers
  > To assess the impact of DRAG on retrieval-augmented multiple-choice question answering (MCQA), we conduct extensive experiments across four benchmark datasets: ARC-C, MedMCQA, GPQA, and MMLU
  - [DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation](https://aclanthology.org/2025.acl-long.358.pdf)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
- **WMDP** (measurement instrument): *measured_by*, 2 papers
  > We use the multiple-choice question-answering Weapons of Mass Destruction Proxy (WMDP) and Massive Multitask Language Understanding (MMLU) benchmarks. (Section 3.1. Benchmarks).
  - [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf)
  - [The Jailbreak Tax: How Useful are Your Jailbreak Outputs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nikolic25a/nikolic25a.pdf)
- **Belebele** (measurement instrument): *measured_by*, 1 paper
  > For multiple choice QA, we use Belebele (Bandarkar et al., 2024) and Multilingual MMLU (Hendrycks et al., 2021; Lai et al., 2023, MMMLU) with five shot prompting. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **EHRNoteQA** (measurement instrument): *measured_by*, 1 paper
  > We offer EHRNoteQA in two formats: open-ended and multi-choice question answering, and propose a reliable evaluation method for each. (Abstract)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **SEED-Bench** (measurement instrument): *measured_by*, 1 paper
  > “SEED-Bench [36] consists of 19k multiple choice questions with human annotations”
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **MMBench** (measurement instrument): *measured_by*, 1 paper
  > “we further evaluate our trained model over six benchmarks that examines LVLMs general perception capability, including SEED-Bench [36], ScienceQA [49], GQA [28], Vizwiz [22], MMBench [48] and MMStar [8] which evaluates LVLMs perception capability with multiple choice questions.”
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **CVQA** (measurement instrument): *measured_by*, 1 paper
  > “Each question was accompanied by one correct answer and three distractors that were reasonably plausible, yet incorrect, thus forming a multiple-choice format.”
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
- **COPA** (measurement instrument): *measured_by*, 1 paper
  > For the multiple-choice tasks, we use datasets: COPA (Gordon et al., 2012), StoryCloze (Mostafazadeh et al., 2016), NLI (Bowman et al., 2015), MMLU (Hendrycks et al., 2021), SST2 (Socher et al., 2013), SST5 (Socher et al., 2013), BoolQ (Clark et al., 2019), and Winogrande (Sakaguchi et al., 2020)... (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **StoryCloze** (measurement instrument): *measured_by*, 1 paper
  > For the multiple-choice tasks, we use datasets: COPA (Gordon et al., 2012), StoryCloze (Mostafazadeh et al., 2016), NLI (Bowman et al., 2015), MMLU (Hendrycks et al., 2021), SST2 (Socher et al., 2013), SST5 (Socher et al., 2013), BoolQ (Clark et al., 2019), and Winogrande (Sakaguchi et al., 2020)... (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **SST-2** (measurement instrument): *measured_by*, 1 paper
  > For the multiple-choice tasks, we use datasets: COPA (Gordon et al., 2012), StoryCloze (Mostafazadeh et al., 2016), NLI (Bowman et al., 2015), MMLU (Hendrycks et al., 2021), SST2 (Socher et al., 2013), SST5 (Socher et al., 2013), BoolQ (Clark et al., 2019), and Winogrande (Sakaguchi et al., 2020)... (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **SST-5** (measurement instrument): *measured_by*, 1 paper
  > For the multiple-choice tasks, we use datasets: COPA (Gordon et al., 2012), StoryCloze (Mostafazadeh et al., 2016), NLI (Bowman et al., 2015), MMLU (Hendrycks et al., 2021), SST2 (Socher et al., 2013), SST5 (Socher et al., 2013), BoolQ (Clark et al., 2019), and Winogrande (Sakaguchi et al., 2020)... (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **INCLUDE** (measurement instrument): *measured_by*, 1 paper
  > INCLUDE is a dataset of 197,243 MCQA pairs from 1,926 examinations across 44 languages and 15 scripts.
  - [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf)
- **MMMLU** (measurement instrument): *measured_by*, 1 paper
  > For multiple choice QA, we use Belebele (Bandarkar et al., 2024) and Multilingual MMLU (Hendrycks et al., 2021; Lai et al., 2023, MMMLU) with five shot prompting. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **MME-RealWorld** (measurement instrument): *measured_by*, 1 paper
  > For each question, we manually construct four options, with one being the correct answer... We try to use the model's default prompt for multiple-choice questions...
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **RACE** (measurement instrument): *measured_by*, 1 paper
  > “The multiple-choice tasks include: ... reading comprehension (RACE; Lai et al. 2017)”
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
- **JAMA Clinical Challenge** (measurement instrument): *measured_by*, 1 paper
  > Both datasets are structured as multiple-choice question-answering tasks, accompanied by expert-written explanations. (Abstract)
  - [Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.182.pdf)
- **Medbullets** (measurement instrument): *measured_by*, 1 paper
  > Both datasets are structured as multiple-choice question-answering tasks, accompanied by expert-written explanations. (Abstract)
  - [Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.182.pdf)
- **LogiQA 2.0** (measurement instrument): *measured_by*, 1 paper
  > LogiQA2 (Liu et al., 2023) for logical reasoning multi-choice QA;
  - [Warmup Generations: A Task-Agnostic Approach for Guiding Sequence-to-Sequence Learning with Unsupervised Initial State Generation](https://aclanthology.org/2025.acl-long.434.pdf)
- **OLMES** (measurement instrument): *measured_by*, 1 paper
  > We use the OLMES suite of 10 multiple choice question answering benchmarks (Gu et al., 2024)... (Section 2.4)
  - [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf)
- **Open LLM Leaderboard** (measurement instrument): *measured_by*, 1 paper
  > We started from two LLM leaderboards: (1) HuggingFace’s Open LLM Leaderboard 21; and (2) Stanford’s Holistic Evaluation of Language Models (Helm) (Liang et al., 2023). Both use questions from the Massive Multitask Language Understanding (MMLU) question-answering dataset (Hendrycks et al., 2020), with multiple choice questions and labeled correct answers. (Section 3.1).
  - [Correlated Errors in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25e/kim25e.pdf)
- **HELM** (measurement instrument): *measured_by*, 1 paper
  > We started from two LLM leaderboards: (1) HuggingFace’s Open LLM Leaderboard 21; and (2) Stanford’s Holistic Evaluation of Language Models (Helm) (Liang et al., 2023). Both use questions from the Massive Multitask Language Understanding (MMLU) question-answering dataset (Hendrycks et al., 2020), with multiple choice questions and labeled correct answers. (Section 3.1).
  - [Correlated Errors in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25e/kim25e.pdf)
- **C-Eval** (measurement instrument): *measured_by*, 1 paper
  > For multi-choice QA, we choose eight subjects from CEVAL (Huang et al., 2023), covering compulsory courses from middle school to university in China. (Section 4.2)
  - [AQuilt: Weaving Logic and Self-Inspection into Low-Cost, High-Relevance Data Synthesis for Specialist LLMs](https://aclanthology.org/2025.emnlp-main.293.pdf)
- **MMMU** (measurement instrument): *measured_by*, 1 paper
  > “For both multiple-choice answers in MMMU and open responses in VL-ICL”
  - [Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning](https://aclanthology.org/2025.emnlp-main.97.pdf)
- **SinhalaMMLU** (measurement instrument): *measured_by*, 1 paper
  > To address this, we introduce SinhalaMMLU, the first multiple-choice question answering benchmark designed specifically for Sinhala, a low-resource language. (Abstract)
  - [SinhalaMMLU: A Comprehensive Benchmark for Evaluating Multitask Language Understanding in Sinhala](https://aclanthology.org/2025.emnlp-main.1673.pdf)
- **NOVA-63** (measurement instrument): *measured_by*, 1 paper
  > “a general multiple-choice benchmark containing 89,107 native questions across 14 languages and 63 academic secondary disciplines”
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.364.pdf)
- **EDUADAPT** (measurement instrument): *measured_by*, 1 paper
  > To bridge this gap, we developed EDUADAPT, a benchmark of nearly 48k QA pairs (comprising both multiple-choice and open-ended question-answers) for Grades 1-12 across nine educational subjects, following the K-12 framework. (Section 1)
  - [EduAdapt: A Question Answer Benchmark Dataset for Evaluating Grade-Level Adaptability in LLMs](https://aclanthology.org/2025.emnlp-main.1736.pdf)
- **SNLI** (measurement instrument): *measured_by*, 1 paper
  > For the multiple-choice tasks, we use datasets: COPA (Gordon et al., 2012), StoryCloze (Mostafazadeh et al., 2016), NLI (Bowman et al., 2015), MMLU (Hendrycks et al., 2021), SST2 (Socher et al., 2013), SST5 (Socher et al., 2013), BoolQ (Clark et al., 2019), and Winogrande (Sakaguchi et al., 2020)... (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)

### → Multiple-choice question answering
- **Explanation generation** (behavioral indicator): *correlates*, 1 paper
  > models that exhibit superior performance in the Answer Selection task tend to generate more plausible explanations. (Section 3.2)
  - [When LLMs Meet Cunning Texts: A Fallacy Understanding Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbfbf1a9adbcc29783475d2767f218e8-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Commonsense reasoning** (construct), 2 papers
  > we used the PEFT library (Mangrulkar et al., 2022) for fine-tuning LlaMA2-7B on common-sense reasoning tasks (multiple choice or True/False classification). (Section 5)
  - [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf)
  - [zFLoRA: Zero-Latency Fused Low-Rank Adapters](https://aclanthology.org/2025.emnlp-main.1086.pdf)
- **Positional bias** (construct), 2 papers
  > Pezeshkpour et al., 2023 identify inherent ‘positional bias’ in the MCQ setting, where LLMs prefer to select options in specific positions as answers (Section 2)
  - [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf)
  - [Positional Overload: Positional Debiasing and Context Window Extension for Large Language Models using Set Encoding](https://aclanthology.org/2025.acl-long.197.pdf)
- **Reasoning** (construct), 1 paper
  > The multiple-choice benchmarks we chose is challenging enough in itself and requires strong reasoning ability from the model; (Section 4.1)
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **Emergent abilities** (construct), 1 paper
  > Schaeffer et al. (2024a) finds that emergent abilities mainly happen on string-match and multiple-choice tasks (Schaeffer et al., 2024a), for which traditional performance measures exhibit strong discontinuity. (Sec. 1)
  - [U-shaped and Inverted-U Scaling behind Emergent Abilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f696200311b445af686c3ebd87ade1d7-Paper-Conference.pdf)
- **Action selection** (behavioral indicator), 1 paper
  > Large language models (LLMs) (Touvron et al., 2023; Databricks, 2024; Abdin et al., 2024) have demonstrated remarkable capabilities in various decision-making tasks, including multi-choice question answering and tool usage (Section 1)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)
- **Medical knowledge** (construct), 1 paper
  > For Low-Level tasks (f1), we adopt multiple-choice questions (MCQs) as simple knowledge recalling tasks for Low-Level, where the model is required to recognize the correct answer from multiple candidate options (see the left part of Figure 2). (Section 3.3)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
- **Selection bias** (construct), 1 paper
  > One such underexplored phenomenon is selection bias in MCQA. Unlike open-ended VQA formats, MCQA requires models to select one option among predefined choices (e.g., A/B/C/D), introducing the possibility of preference for certain option positions or tokens. (Introduction)
  - [Benchmarking and Mitigating MCQA Selection Bias of Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1703.pdf)
- **Fine-grained visual recognition** (behavioral indicator), 1 paper
  > we leverage the test sets as resources for annotated data and frame FGVR as a multiple-choice task
  - [Analyzing and Boosting the Power of Fine-Grained Visual Recognition for Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfa2f1555d46b553827af4e1557f3c9a-Paper-Conference.pdf)
- **Calibration** (construct), 1 paper
  > The calibration error of an LLM is typically evaluated on a multiple-choice question and its corresponding correct answer, which can be formalized as an input-label pair (x, y)... (Section 3)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
