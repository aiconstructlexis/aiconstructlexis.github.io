# Question answering
**Type:** Behavioral indicator  
**Supporting papers:** 322  
**Also known as:** Question Answering, Benchmark Question Answering, Text-based question answering, Tideo question answering, Natural language question answering  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats question answering as producing or selecting an answer to a natural-language question, usually with correctness as the success criterion. Most papers frame the answer as grounded either in a provided passage, document set, retrieved evidence, tables or knowledge graphs, or in the model's internal or general knowledge, though a smaller line places the task in adversarial or knowledge-conflict settings. Output formats vary from direct short answers and open-ended responses to multiple-choice, yes/no, and span-based answers; in some passage-based settings, papers specify answers as Yes/No/Don't Know, a span in the question, or a span in the passage. Some papers also require a rationale alongside the answer, and correctness is judged against a gold or reference answer.

**Variants.** Papers study many variants, most commonly passage- or document-grounded QA, open-domain QA, and multi-hop or long-context QA where answers may require combining evidence across documents, retrieved passages, or multiple tables. Other named variants include contextual, entity, extractive, benchmark, closed-book, and open-book QA, as well as reformulations of dialogue state tracking or entity identification as question answering. A smaller line extends the task to structured data, text-only and Tideo video representations, images, game states, video, speech, audio, and music, and to specialized domains such as mental health, medicine, science, law, finance, IT operations, and community-specific Reddit responses.

**Space of elicitation and scores.** Papers measure question answering with 72 linked instruments, mostly benchmark datasets and evaluation suites. The most frequently linked are Natural Questions, SQuAD v1.1, HotpotQA, TriviaQA, and MMLU; the wider instrument pool also covers passage-based, multi-hop, long-context, multilingual, domain-specific, and instruction-following QA benchmarks. A smaller line uses scoring tools such as LLM-as-a-judge or lm-evaluation-harness, where responses are compared with reference answers or assigned correctness labels.

**What it is taken as evidence of.** Question answering is linked to 14 constructs, and papers spread those links across several constructs rather than centering on one. The most recurrent recorded links say that Question answering is related to Reasoning and Completeness, and papers also relate it to In-context learning. Directional claims are rarer: one paper claims a causal relationship from Question answering to GUI understanding, while another claims a causal relationship from Knowledge conflict resolution to Question answering.

## Sources

**Question answering** (92 papers: [Enhancing Language Model Hypernetworks with Restart: A Study on Optimization](https://aclanthology.org/2025.naacl-long.397.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf), [THREAD: Thinking Deeper with Recursive Spawning](https://aclanthology.org/2025.naacl-long.427.pdf), [GuideLLM: Exploring LLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.287.pdf), [Dynamic Uncertainty Ranking: Enhancing Retrieval-Augmented In-Context Learning for Long-Tail Knowledge in LLMs](https://aclanthology.org/2025.naacl-long.453.pdf), [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.444.pdf), [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf), [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.387.pdf), [Are LLM-Judges Robust to Expressions of Uncertainty? Investigating the effect of Epistemic Markers on LLM-based Evaluation](https://aclanthology.org/2025.naacl-long.452.pdf), [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.575.pdf), [LLaSA: Large Language and Structured Data Assistant](https://aclanthology.org/2025.naacl-long.97.pdf), [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf), [CharacterBox: Evaluating the Role-Playing Capabilities of LLMs in Text-Based Virtual Worlds](https://aclanthology.org/2025.naacl-long.323.pdf), [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf), [Knowledge Graph-Guided Retrieval Augmented Generation](https://aclanthology.org/2025.naacl-long.449.pdf), [Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective](https://aclanthology.org/2025.naacl-long.151.pdf), [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf), [From Evidence to Belief: A Bayesian Epistemology Approach to Language Models](https://aclanthology.org/2025.naacl-long.531.pdf), [Balancing Forget Quality and Model Utility: A Reverse KL-Divergence Knowledge Distillation Approach for Better Unlearning in LLMs](https://aclanthology.org/2025.naacl-long.60.pdf), [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf), [COVE: COntext and VEracity prediction for out-of-context images](https://aclanthology.org/2025.naacl-long.102.pdf), [ComPO: Community Preferences for Language Model Personalization](https://aclanthology.org/2025.naacl-long.419.pdf), [Analyzing and Improving Coherence of Large Language Models in Question Answering](https://aclanthology.org/2025.naacl-long.588.pdf), [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf), [RAP: A Metric for Balancing Repetition and Performance in Open-Source Large Language Models](https://aclanthology.org/2025.naacl-long.69.pdf), [CompAct: Compressed Activations for Memory-Efficient LLM Training](https://aclanthology.org/2025.naacl-long.71.pdf), [Pointwise Mutual Information as a Performance Gauge for Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.78.pdf), [PA-RAG: RAG Alignment via Multi-Perspective Preference Optimization](https://aclanthology.org/2025.naacl-long.459.pdf), [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf), [SLIM: Let LLM Learn More and Forget Less with Soft LoRA and Identity Mixture](https://aclanthology.org/2025.naacl-long.246.pdf), [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.122.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf), [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf), [Soft Language Prompts for Language Transfer](https://aclanthology.org/2025.naacl-long.517.pdf), [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf), [Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models](https://aclanthology.org/2025.naacl-long.632.pdf), [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf), [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.538.pdf), [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf), [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf), [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.601.pdf), [TRANSIENTTABLES: Evaluating LLMs' Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.332.pdf), [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf), [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf), [Making Language Models Robust Against Negation](https://aclanthology.org/2025.naacl-long.413.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [Is your benchmark truly adversarial? AdvScore: Evaluating Human-Grounded Adversarialness](https://aclanthology.org/2025.naacl-long.27.pdf), [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf), [Unlearning as multi-task optimization: A normalized gradient difference approach with an adaptive learning rate](https://aclanthology.org/2025.naacl-long.563.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [TrimLLM: Progressive Layer Dropping for Domain-Specific LLMs](https://aclanthology.org/2025.acl-long.33.pdf), [Soup-of-Experts: Pretraining Specialist Models via Parameters Averaging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ablin25a/ablin25a.pdf), [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf), [ESPACE: Dimensionality Reduction of Activations for Model Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6591cc41be737e9ba4cc487ac8082d-Paper-Conference.pdf), [Differential Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/00b67df24009747e8bbed4c2c6f9c825-Paper-Conference.pdf), [Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/45fc8e1c55df116b23488f3cdb2fc642-Paper-Conference.pdf), [Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf), [Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://proceedings.iclr.cc/paper_files/paper/2024/file/99261adc8a6356b38bcf999bba9a26dc-Paper-Conference.pdf), [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf), [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf), [Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/6733cf15e10e2cd1d59af033c3bb8507-Paper-Conference.pdf), [DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/e352b765e625934ce86919995e2371aa-Paper-Conference.pdf), [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf), [How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions](https://proceedings.iclr.cc/paper_files/paper/2024/file/efe79ae16496a0f5b57287873de072d1-Paper-Conference.pdf), [INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://proceedings.iclr.cc/paper_files/paper/2024/file/0d1986a61e30e5fa408c81216a616e20-Paper-Conference.pdf), [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf), [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf), [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf), [LQ-LoRA: Low-rank plus Quantized Matrix Decomposition for Efficient Language Model Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/d97a16cb83d74195b76e0bf1e85bf072-Paper-Conference.pdf), [Large Language Models as Automated Aligners for benchmarking Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf), [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf), [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf), [MEND: Meta Demonstration Distillation for Efficient and Effective In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ce1cbededb4b0d6202847ac1b484ee8-Paper-Conference.pdf), [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf), [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf), [OWL: A Large Language Model for IT Operations](https://proceedings.iclr.cc/paper_files/paper/2024/file/6581ff85ba0ca663513d5f65b25f6631-Paper-Conference.pdf), [On the Humanity of Conversational AI: Evaluating the Psychological Portrayal of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/c48dcd605cfb17d5b4f94ce106a915f7-Paper-Conference.pdf), [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/be3b0d51a2b86cb4ffe50f13480217e0-Paper-Conference.pdf), [QLLM: Accurate and Efficient Low-Bitwidth Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/437bc4ccafd3fc6d4289bd10940be42b-Paper-Conference.pdf), [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf), [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf), [Representation Deficiency in Masked Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfde7fb279709eff53faa074b45840d8-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf), [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf), [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf), [SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/428ceef2cd8a53add7213e04d1746479-Paper-Conference.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [Tailoring Self-Rationalizers with Multi-Reward Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf), [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf), [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf))
> Producing answers to natural language questions, evaluated in both standard and adversarial settings.

**Question Answering** (1 paper: [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf))
> The model providing answers to questions across various subjects as part of knowledge benchmarks.

**Benchmark Question Answering** (1 paper: [EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf))
> Solving specific tasks on standardized public benchmarks to demonstrate model capabilities.

**Text-based question answering** (1 paper: [VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.72.pdf))
> Generating answers to questions using only textual input and reasoning, without reliance on visual information.

**Tideo question answering** (1 paper: [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf))
> A pre-alignment task where the model answers a question based on the content of a "textual video" (Tideo).

**Natural language question answering** (1 paper: [Semantic-Eval : A Semantic Comprehension Evaluation Framework for Large Language Models Generation without Training](https://aclanthology.org/2025.acl-long.477.pdf))
> The task of generating answers to open-ended questions in natural language, particularly in specialized domains like mental health or medicine.

## Relationships

### Question answering →
- **SQuAD v1.1** (measurement instrument): *measured_by*, 19 papers
  > In QA, we evaluate the performance of the proposed PEFT method on SQuADv1.1 (Rajpurkar et al., 2016) and SQuADv2.0 (Rajpurkar et al., 2018). (Section 4)
  - [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf)
  - [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf)
  - [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf)
  - [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
  - [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25x/yang25x.pdf)
  - [A Lens into Interpretable Transformer Mistakes via Semantic Dependency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25n/dong25n.pdf)
  - [Contrastive Private Data Synthesis via Weighted Multi-PLM Fusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25d/zou25d.pdf)
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf)
  - [Beyond Input Activations: Identifying Influential Latents by Gradient Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.87.pdf)
  - [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf)
  - [HydraOpt: Navigating the Efficiency-Performance Trade-off of Adapter Merging](https://aclanthology.org/2025.emnlp-main.1365.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 19 papers
  > we first fine-tune Llama 2-7B-chat on TruthfulQA and then evaluate 0-shot on three out-of-domain question-answering benchmarks: TriviaQA [18], Natural Questions [20, NQ], and MMLU [14]. (Section 6).
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf)
  - [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf)
  - [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf)
  - [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf)
  - [Pointwise Mutual Information as a Performance Gauge for Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.78.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
  - [RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf)
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf)
  - [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf)
  - [How Do Large Vision-Language Models See Text in Image? Unveiling the Distinctive Role of OCR Heads](https://aclanthology.org/2025.emnlp-main.1032.pdf)
  - [PathwiseRAG: Multi-Dimensional Exploration and Integration Framework](https://aclanthology.org/2025.emnlp-main.1167.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
  - [Hallucination Detection in LLMs Using Spectral Features of Attention Maps](https://aclanthology.org/2025.emnlp-main.1239.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 15 papers
  > In this section, we implement and evaluate Conformal Alignment in question-answering tasks, where we consider a conversational question answering dataset TriviaQA [21] and a closed-book reading comprehension dataset CoQA [39]. (Section 4)
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [On Giant's Shoulders: Effortless Weak to Strong by Dynamic Logits Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/34ec1286b2ccd4794c5ca4ad078b7150-Paper-Conference.pdf)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
  - [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf)
  - [Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf)
  - [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
  - [Hallucination Detection in LLMs Using Spectral Features of Attention Maps](https://aclanthology.org/2025.emnlp-main.1239.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 15 papers
  > “HotPotQA provides a more challenging open-ended question answering task with long answers containing many tokens.”
  - [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
  - [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
  - [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf)
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf)
  - [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf)
  - [How Do Large Vision-Language Models See Text in Image? Unveiling the Distinctive Role of OCR Heads](https://aclanthology.org/2025.emnlp-main.1032.pdf)
  - [PathwiseRAG: Multi-Dimensional Exploration and Integration Framework](https://aclanthology.org/2025.emnlp-main.1167.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
- **MMLU** (measurement instrument): *measured_by*, 10 papers
  > we first fine-tune Llama 2-7B-chat on TruthfulQA and then evaluate 0-shot on three out-of-domain question-answering benchmarks: TriviaQA [18], Natural Questions [20, NQ], and MMLU [14]. (Section 6).
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [The Unreasonable Ineffectiveness of the Deeper Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbabc2f70de2dd09f491a8715ec3e80f-Paper-Conference.pdf)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
  - [UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4800e97411c7f199b2895425f2933a5-Paper-Conference.pdf)
  - [Neutral residues: revisiting adapters for model extension](https://raw.githubusercontent.com/mlresearch/v267/main/assets/talla25a/talla25a.pdf)
  - [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf)
  - [GRU: Mitigating the Trade-off between Unlearning and Retention for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25de/wang25de.pdf)
  - [Forget What You Know about LLMs Evaluations - LLMs are Like a Chameleon](https://aclanthology.org/2025.emnlp-main.1098.pdf)
  - [Train It and Forget It: Merge Lists are Unnecessary for BPE Inference in Language Models](https://aclanthology.org/2025.emnlp-main.1775.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 9 papers
  > In the assessments of continued QA and text understanding, we report 0-shot accuracy for LogiQA [28], 32-shot BoolQ [29], and 0-shot LAMBADA [30]. (Section 5.1)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [The Unreasonable Ineffectiveness of the Deeper Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbabc2f70de2dd09f491a8715ec3e80f-Paper-Conference.pdf)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
  - [HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf)
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
  - [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf)
  - [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
- **ARC** (measurement instrument): *measured_by*, 9 papers
  > To evaluate the efficacy of ACC-Collab we make use of 5 standard benchmark tasks: ... ARC Chollet (2019) ∼7k multiple-choice reasoning-based questions. (Section 5)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
  - [Forward Knows Efficient Backward Path: Saliency-Guided Memory-Efficient Fine-tuning of Large Language Models](https://aclanthology.org/2025.acl-long.459.pdf)
  - [Optimizing Pre-Training Data Mixtures with Mixtures of Data Expert Models](https://aclanthology.org/2025.acl-long.1564.pdf)
  - [Radio: Rate–Distortion Optimization for Large Language Model Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/young25b/young25b.pdf)
  - [EcoLoRA: Communication-Efficient Federated Fine-Tuning of Large Language Models](https://aclanthology.org/2025.emnlp-main.1046.pdf)
  - [Train It and Forget It: Merge Lists are Unnecessary for BPE Inference in Language Models](https://aclanthology.org/2025.emnlp-main.1775.pdf)
  - [MemoryFormer : Minimize Transformer Computation by Removing Fully-Connected Layers](https://proceedings.neurips.cc/paper_files/paper/2024/file/24143e25a82f856aeed58b2f497d623b-Paper-Conference.pdf)
  - [Stacking Your Transformers: A Closer Look at Model Growth for Efficient LLM Pre-Training](https://proceedings.neurips.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf)
  - [Mixture of Tokens: Continuous MoE through Cross-Example Aggregation](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc427eb348789b190e3ea050cceff8a3-Paper-Conference.pdf)
- **Qasper** (measurement instrument): *measured_by*, 6 papers
  > Qasper (QASP) (Dasigi et al., 2021) is a question answering dataset over NLP papers filtered from the Semantic Scholar Open Research Corpus (S2ORC) (Lo et al., 2020).
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [Cost-efficient Collaboration between On-device and Cloud Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/narayan25a/narayan25a.pdf)
- **NarrativeQA** (measurement instrument): *measured_by*, 5 papers
  > NarrativeQA (NQA) (Koˇciský et al., 2018) is an established question answering dataset over entire books from Project Gutenberg3 and movie scripts from a list of websites.
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b0a8df568ec496a717566a7f8158aaa-Paper-Conference.pdf)
- **LongBench** (measurement instrument): *measured_by*, 5 papers
  > This benchmark encompasses a broad range of tasks, such as question-answering, summarization, and code completion, where the evaluation length ranges from 5k to 15k. (Section 4.3)
  - [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [FocusLLM: Precise Understanding of Long Context by Dynamic Condensing](https://aclanthology.org/2025.acl-long.1500.pdf)
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf)
- **QuALITY** (measurement instrument): *measured_by*, 5 papers
  > QuALITY (QLTY) (Pang et al., 2022) is a question answering dataset over stories and articles collected from several resources, such as Project Gutenberg and the Open American National Corpus4.
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Language Models Learn to Mislead Humans via RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a5a60573637f329b04d1beda4cd404-Paper-Conference.pdf)
  - [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 4 papers
  > In question answering, we adopt the test splits of ECQA (Aggarwal et al., 2021), QASC (Khot et al., 2020), OpenbookQA (Mihaylov et al., 2018), and StrategyQA (Geva et al., 2021) for evaluation. (Section 4)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [Optimizing Pre-Training Data Mixtures with Mixtures of Data Expert Models](https://aclanthology.org/2025.acl-long.1564.pdf)
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)
  - [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 4 papers
  > TruthfulQA encompasses multiple-choice questions, with only one option being the best answer. (Section 4.1)
  - [On the Humanity of Conversational AI: Evaluating the Psychological Portrayal of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/c48dcd605cfb17d5b4f94ce106a915f7-Paper-Conference.pdf)
  - [Calibrating Expressions of Certainty](https://proceedings.iclr.cc/paper_files/paper/2025/file/66b35d2e8d524706f39cc21f5337b002-Paper-Conference.pdf)
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)
  - [Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)
- **ZsRE** (measurement instrument): *measured_by*, 4 papers
  > For GPT-2, T5-XL, and GPT-J, we use the zero-shot Relation Extraction (zsRE) question answering dataset (Levy et al., 2017) with the identical train/val splits with De Cao et al. (2021); Mitchell et al. (2022) (Section 5).
  - [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)
  - [Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.733.pdf)
- **MedMCQA** (measurement instrument): *measured_by*, 4 papers
  > We evaluate our agent on three complex QA tasks: ProductQA, MedMCQA and HotPotQA.
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
  - [RECALL: REpresentation-aligned Catastrophic-forgetting ALLeviation via Hierarchical Model Merging](https://aclanthology.org/2025.emnlp-main.829.pdf)
  - [Topic Coverage-based Demonstration Retrieval for In-Context Learning](https://aclanthology.org/2025.emnlp-main.1007.pdf)
- **2WikiMultiHopQA** (measurement instrument): *measured_by*, 4 papers
  > Question Answering For this task, we consider the following datasets: 2WikiMultiHopQA [27], StrategyQA [28], MuSiQue [29], and HotpotQA [30] (Section 4.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
  - [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
- **WikiQA** (measurement instrument): *measured_by*, 4 papers
  > For question answering, we employ two famous benchmarks: SQuAD (Rajpurkar et al., 2016) and WikiQA (Yang et al., 2015). (Section 3)
  - [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf)
  - [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **QASC** (measurement instrument): *measured_by*, 4 papers
  > In question answering, we adopt the test splits of ECQA (Aggarwal et al., 2021), QASC (Khot et al., 2020), OpenbookQA (Mihaylov et al., 2018), and StrategyQA (Geva et al., 2021) for evaluation. (Section 4)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **SQuAD 2.0** (measurement instrument): *measured_by*, 3 papers
  > SuperContext is validated on a comprehensive OOD benchmarks GLUE-X (Yang et al., 2022), and a QA dataset, SQuAD 2.0 (Rajpurkar et al., 2018). (Section 2)
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [RECALL: REpresentation-aligned Catastrophic-forgetting ALLeviation via Hierarchical Model Merging](https://aclanthology.org/2025.emnlp-main.829.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 3 papers
  > Question Answering For this task, we consider the following datasets: 2WikiMultiHopQA [27], StrategyQA [28], MuSiQue [29], and HotpotQA [30] (Section 4.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 3 papers
  > CommonsenseQA [63] is to test models’ ability to answer questions using only the parameterized knowledge instead of the context knowledge. (Appendix E.2)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 3 papers
  > Question Answering. For questions about workflow demonstrations, the model generates a natural language answer, assessing its understanding of workflow semantics. We use GPT-4 to compare the generated answer to a reference answer for evaluation. (Section 4.2)
  - [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf)
- **SIQA** (measurement instrument): *measured_by*, 3 papers
  > OLMo-30M models trained on various pre-training token budgets are fine-tuned on downstream tasks using fixed hyperparameters: math (GSM8k), code (Starcoder-Python), and QA (SIQA). (Figure 4)
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **MuSiQue** (measurement instrument): *measured_by*, 3 papers
  > Question Answering For this task, we consider the following datasets: 2WikiMultiHopQA [27], StrategyQA [28], MuSiQue [29], and HotpotQA [30] (Section 4.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
  - [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 3 papers
  > "The datasets in ∞-Bench cover diverse tasks including question answering, summarization, context retrieval, and mathematic computing."
  - [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
- **Alpaca instruction dataset** (measurement instrument): *measured_by*, 3 papers
  > The ﬁrst task is Q&A and summarization, including Alpaca [68] and SAMSum [22], and perplexity (PPL) is used to measure their performance. (Section 4.1)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
  - [Permute-and-Flip: An optimally stable and watermarkable decoder for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/50be7e77b9c883144940be925b608acc-Paper-Conference.pdf)
  - [GraphRouter: A Graph-based Router for LLM Selections](https://proceedings.iclr.cc/paper_files/paper/2025/file/41b6674c28a9b93ec8d22a53ca25bc3b-Paper-Conference.pdf)
- **PopQA** (measurement instrument): *measured_by*, 2 papers
  > We adapt our approach to question answering as described at the end of Section 5. We focus on 1.5K randomly sampled questions from PopQA. (Section 6.3)
  - [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
- **CoQA** (measurement instrument): *measured_by*, 2 papers
  > we performed experiments on three datasets that cover a broad range of question answering settings. To be concrete, we use ... the almost 8,000 open-book questions in the development split of CoQA (Reddy et al., 2019) (Section 6).
  - [Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)
  - [MAC-Tuning: LLM Multi-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.35.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 2 papers
  > Second, we consider standard academic benchmarks used to evaluate large language models, such as question answering or Cloze-style problems. We use the following datasets: ARC challenge (Clark et al., 2018)...
  - [Neutral residues: revisiting adapters for model extension](https://raw.githubusercontent.com/mlresearch/v267/main/assets/talla25a/talla25a.pdf)
  - [PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation](https://aclanthology.org/2025.emnlp-main.747.pdf)
- **RULER** (measurement instrument): *measured_by*, 2 papers
  > Figure 5 illustrates the trade-off between two representative KV sparsification algorithms, SnapKV and PQCache, and their respective theoretical speedups on three distinct Ruler tasks: needle in a haystack with passkeys 3 (niah-multikeys-3), common word extraction (cwe), and question answering 1 (qa-1). (Section 4.4)
  - [MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/13f972adf12bdf886583d48cd528002f-Paper-Conference.pdf)
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
- **ZeroSCROLLS** (measurement instrument): *measured_by*, 2 papers
  > "ZeroSCROLLS benchmark ... contains ten diverse natural language tasks that require understanding long input contexts, including summarization, question answering"
  - [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf)
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
- **MedQA** (measurement instrument): *measured_by*, 2 papers
  > ...while MedQA-USMLE [34] acts as a domain-specific QA benchmark. (Section 4.1)
  - [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
  - [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 2 papers
  > Our method is benchmarked across a diverse range of question answering and generation datasets [24, 25, 26, 27, 28, 29, 30, 31] using the lm-eval-harness [32]. (Section 2)
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
  - [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf)
- **Bamboogle** (measurement instrument): *measured_by*, 2 papers
  > For QA, we conduct experiments on three widely used datasets: Bamboogle [17], WikiMultiHopQA [52], and HotpotQA [53]. (Section 5.1)
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
  - [Inference Scaling for Long-Context Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b57471758783450408f5c9b70257d15b-Paper-Conference.pdf)
- **DROP** (measurement instrument): *measured_by*, 2 papers
  > We also evaluate question answering on SQuAD [70], NQ [46], TriviaQA [40], and Drop [20], where models must ground their answers in in-context documents. (Section 4.1.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf)
- **GPQA** (measurement instrument): *measured_by*, 2 papers
  > question-answering [GPQA, 51] (Introduction).
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f74d79573d71078848973009d0e99bdb-Paper-Conference.pdf)
- **SciQ** (measurement instrument): *measured_by*, 2 papers
  > Following Tian et al. (2023), we use two question-answering datasets: (1) SciQ (Welbl et al., 2017) contains crowd-sourced science exam questions (Section 4.3).
  - [Calibrating Expressions of Certainty](https://proceedings.iclr.cc/paper_files/paper/2025/file/66b35d2e8d524706f39cc21f5337b002-Paper-Conference.pdf)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 2 papers
  > Question Answering. For ScienceQA (Lu et al., 2022b), we gather text-only samples to form a train and test set with 6,508 and 2,224 samples. (Section 4.1).
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)
- **LoCoMo** (measurement instrument): *measured_by*, 2 papers
  > Table 1: Performance comparison on LOCOMO and Long-MT-Bench+. (The table shows QA Performance metrics for these datasets.)
  - [SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf)
  - [MemInsight: Autonomous Memory Augmentation for LLM Agents](https://aclanthology.org/2025.emnlp-main.1683.pdf)
- **GLUE** (measurement instrument): *measured_by*, 2 papers
  > We finetune the pretrained RoBERTa-base model (Liu et al., 2019) on the GLUE benchmark, a widely used suite for evaluating NLP models across various tasks, including sentiment analysis and question answering (Wang et al., 2019). (Section 4.2)
  - [CompAct: Compressed Activations for Memory-Efficient LLM Training](https://aclanthology.org/2025.naacl-long.71.pdf)
  - [A Memory Efficient Randomized Subspace Optimization Method for Training Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cj/chen25cj.pdf)
- **TyDi QA** (measurement instrument): *measured_by*, 1 paper
  > TydiQA [7] Multilingual QA (Table 1)
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 1 paper
  > We conduct a comparative evaluation of PPC-GPT on QA datasets. Specifically, we include... ARC-E... (Section 5.1)
  - [PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation](https://aclanthology.org/2025.emnlp-main.747.pdf)
- **BioASQ** (measurement instrument): *measured_by*, 1 paper
  > We evaluate RAG performance across three datasets spanning different reasoning complexities and domain-specificity... BioASQ (Task 11B) (Krithara et al., 2023): PubMed-based biomedical QA for specialized domains. (Section 3.3)
  - [RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > “We test on the test splits of ... GSM8K (Cobbe et al., 2021), ARC (Clark et al., 2018), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2019), and WinoGrande (Sakaguchi et al., 2021) for question-answering tasks.”
  - [Radio: Rate–Distortion Optimization for Large Language Model Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/young25b/young25b.pdf)
- **BBQ** (measurement instrument): *measured_by*, 1 paper
  > For question answering, we use the BBQ dataset (Parrish et al., 2021), where unambiguous contexts serve as the knowledge base, and target groups are the classes to be predicted. (Section 5.1)
  - [Your RAG is Unfair: Exposing Fairness Vulnerabilities in Retrieval-Augmented Generation via Backdoor Attacks](https://aclanthology.org/2025.emnlp-main.804.pdf)
- **ELI5** (measurement instrument): *measured_by*, 1 paper
  > We run experiments on two question- answering datasets, namely NQ-Open and ELI5. (Section 3.1)
  - [Pointwise Mutual Information as a Performance Gauge for Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.78.pdf)
- **ArXivQA** (measurement instrument): *measured_by*, 1 paper
  > Three question-answering (QA) benchmarks: HotpotQA [53], ArxivQA [22], ToolQA [67], where the task is to provide natural language answers to the questions. (Section 5).
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **ToolQA** (measurement instrument): *measured_by*, 1 paper
  > Three question-answering (QA) benchmarks: HotpotQA [53], ArxivQA [22], ToolQA [67], where the task is to provide natural language answers to the questions. (Section 5).
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **LogiQA** (measurement instrument): *measured_by*, 1 paper
  > In the assessments of continued QA and text understanding, we report 0-shot accuracy for LogiQA [28], 32-shot BoolQ [29], and 0-shot LAMBADA [30]. (Section 5.1)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **NewsQA** (measurement instrument): *measured_by*, 1 paper
  > “For the news articles domain, we use the NewsQA dataset (Trischler et al., 2017), which consists of CNN articles paired with questions and answers derived from those articles.”
  - [Evaluating Copyright Takedown Methods for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/faed4276b52ef762879db4142655c699-Paper-Datasets_and_Benchmarks_Track.pdf)
- **SHP** (measurement instrument): *measured_by*, 1 paper
  > “Question-Answering (QA). We reconstruct the public dataset SHP, which comprises numerous questions from Reddit posts and their corresponding user answers.”
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 1 paper
  > For question answering, we use AlpacaEval 2.0 (Li et al., 2023b; Dubois et al., 2024a;b) to assess model performance on 805 instructions. (Section 7.1)
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
- **MMHal-Bench** (measurement instrument): *measured_by*, 1 paper
  > MMHal-Bench (MMHal) (Sun et al., 2023) is a question-answering benchmark that covers 8 question categories and 12 object topics. (Sec. 5.1)
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **ECQA** (measurement instrument): *measured_by*, 1 paper
  > In question answering, we adopt the test splits of ECQA (Aggarwal et al., 2021), QASC (Khot et al., 2020), OpenbookQA (Mihaylov et al., 2018), and StrategyQA (Geva et al., 2021) for evaluation. (Section 4)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the efficacy of ACC-Collab we make use of 5 standard benchmark tasks: ... BBH Suzgun et al. (2022) ∼5k mixed-type questions (Section 5)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
- **SST-2** (measurement instrument): *measured_by*, 1 paper
  > For question answering tasks, we utilize BoolQ (from SuperGLUE) and SST-2 (from GLUE) (Section 4).
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
- **HelpSteer** (measurement instrument): *measured_by*, 1 paper
  > "HelpSteer (Wang et al., 2023) is a QA dataset aimed at evaluating the model’s capability to follow instructions across five dimensions"
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)
- **UltraChat** (measurement instrument): *measured_by*, 1 paper
  > From UltraFeedback, we selected two high-quality QA datasets: Truthful QA (Lin et al., 2021), which includes 811 testing problems, and UltraChat (Ding et al., 2023)... (Section 4.1)
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 1 paper
  > We primarily evaluate all the models using two recent proposed instruction-following QA benchmarks: Arena-Hard (Li et al., 2024) and Wild-Bench(Lin et al., 2024).
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > We primarily evaluate all the models using two recent proposed instruction-following QA benchmarks: Arena-Hard (Li et al., 2024) and Wild-Bench(Lin et al., 2024).
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **XQuAD** (measurement instrument): *measured_by*, 1 paper
  > For NLU tasks, we test on the ... question-answering dataset XQuAD (Artetxe et al., 2020). (Section 4.1).
  - [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf)
- **NQ-Swap** (measurement instrument): *measured_by*, 1 paper
  > We demonstrate ADACAD’s effectiveness on a diverse range of tasks, covering question-answering (QA) and summarization, with six QA datasets (Natural Question (NQ; Kwiatkowski et al., 2019), NQ-SWAP (Longpre et al., 2021), TriviaQA (Joshi et al., 2017), PopQA (Mallen et al., 2023), HotpotQA (Yang et al., 2018), TabMWP (Lu et al., 2023)) (Section 1).
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
- **IIRC** (measurement instrument): *measured_by*, 1 paper
  > We measure all the methods on four different QA datasets, including multi-hop Wikipedia reasoning datasets: ... (2) IIRC (Ferguson et al., 2020)... (Section 4.1)
  - [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
- **RGB** (measurement instrument): *measured_by*, 1 paper
  > Open-source RAG datasets: RGB (Chen et al., 2024) and KNOT (Liu et al., 2024) are two general-domain QA datasets designed to evaluate LLMs’ ability to effectively utilize retrieved information while withstanding various imperfections in the retrieval process. (Section 5.1)
  - [Parenting: Optimizing Knowledge Selection of Retrieval-Augmented Language Models with Parameter Decoupling and Tailored Tuning](https://aclanthology.org/2025.acl-long.571.pdf)
- **ParaRel** (measurement instrument): *measured_by*, 1 paper
  > Question-Answering: Given a question, the model directly predicts its answer. We include ParaRel (Elazar et al., 2021) and HotpotQA (Yang et al., 2018). (Section 5.1)
  - [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf)
- **PrOntoQA** (measurement instrument): *measured_by*, 1 paper
  > "The first dataset, PrOntoQA ... consists of question-answering examples"
  - [An Analysis for Reasoning Bias of Language Models with Small Initialization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yao25g/yao25g.pdf)
- **MLQA** (measurement instrument): *measured_by*, 1 paper
  > MLQA (Lewis et al., 2019): A question-answering benchmark with context passages, questions, and answers.
  - [Transplant Then Regenerate: A New Paradigm for Text Data Augmentation](https://aclanthology.org/2025.emnlp-main.702.pdf)
- **CosmosQA** (measurement instrument): *measured_by*, 1 paper
  > These datasets encompass diverse tasks, covering three Question Answering datasets: Huang et al.’s (2019) Cosmos QA, Sap et al.’s (2019) Social IQA, and Rogers et al.’s (2020) QuAIL; (Section 5.2)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **CWQ** (measurement instrument): *measured_by*, 1 paper
  > “PathwiseRAG is evaluated on five challenging question-answering benchmarks spanning different reasoning complexities. ... ComplexWebQuestions ...”
  - [PathwiseRAG: Multi-Dimensional Exploration and Integration Framework](https://aclanthology.org/2025.emnlp-main.1167.pdf)
- **QNLI** (measurement instrument): *measured_by*, 1 paper
  > ...and QNLI for question answering (Wang et al., 2018). (Section 4.1)
  - [NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1769.pdf)
- **GUI understanding** (construct): *causes*, 1 paper
  > both QA and Caption samples enhance performance in GUI understanding and OCR-related benchmarks
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **FiQA-SA** (measurement instrument): *measured_by*, 1 paper
  > We conduct a comparative evaluation of PPC-GPT on QA datasets. Specifically, we include... FiQA-SA... (Section 5.1)
  - [PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation](https://aclanthology.org/2025.emnlp-main.747.pdf)

### → Question answering
- **Self-correction** (behavioral indicator): *causes*, 2 papers
  > PoG (Chen et al., 2024a) integrates reflection and self-correction mechanisms to adaptively explore the reasoning paths over KG via an LLM agent, and then augments the LLM in complex reasoning and question answering based on the retrieved knowledge paths. (Section 3.2.3)
  - [Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities](https://aclanthology.org/2025.emnlp-main.1249.pdf)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Coreference resolution** (behavioral indicator): *causes*, 1 paper
  > highlighting the effectiveness of leveraging coreference resolution to bridge context gaps in question answering. (Abstract)
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **Knowledge conflict resolution** (construct): *causes*, 1 paper
  > MICRO-ACT consistently achieves significant increase in QA accuracy over state-of-the-art baselines across all 5 datasets and 3 conflict types, especially in temporal and semantic types where all baselines fail significantly. (Abstract)
  - [Micro-Act: Mitigate Knowledge Conflict in Question Answering via Actionable Self-Reasoning](https://aclanthology.org/2025.acl-long.909.pdf)

### Associated with
- **Reasoning** (construct), 2 papers
  > Our two Knowledge Transfer tasks – Question Answering and Demo Validation – assess whether a model can perform higher-level reasoning about the properties and correctness of a workflow. (Section 4.2)
  - [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Relevance** (construct), 1 paper
  > question-answering systems can have attributes of relevance, verbosity, and completeness [52].
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **Verbosity** (construct), 1 paper
  > question-answering systems can have attributes of relevance, verbosity, and completeness [52].
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **Completeness** (construct), 1 paper
  > question-answering systems can have attributes of relevance, verbosity, and completeness [52].
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **Multi-hop reasoning** (construct), 1 paper
  > ...we conduct experiments using Llama2-70B [2], GPT-3.5 [1], and GPT-4 [3] on various contextually aware multi-hop reasoning tasks, including claim verification [12], question answering [13], and reading comprehension [14] (Section 1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **World knowledge** (construct), 1 paper
  > the QA ability to maintain pre-trained world knowledge (Section 1).
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
- **Ranking** (behavioral indicator), 1 paper
  > To leverage the instruction following abilities in modern LLMs, we formulate the re-ranking task into either question answering (QA) or information extraction (IE) tasks, which are more commonly seen by LLMs. (Section 3.1)
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **Entity disambiguation** (behavioral indicator), 1 paper
  > Entity Identification. This function acts as a question-answering module that extracts a specific entity. (Section 3.2)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
- **Dialogue state tracking** (behavioral indicator), 1 paper
  > Our approach includes reformulating DST as a question-answering task for less capable models and employing self-refining prompts for more adaptable ones.
  - [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.387.pdf)
- **In-context learning** (construct), 1 paper
  > For question-answering (QA) tasks, in-context learning (ICL) enables language models (LMs) to generate responses without modifying their parameters by leveraging examples provided in the input. (Abstract)
  - [Federated In-Context Learning: Iterative Refinement for Improved Answer Quality](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25db/wang25db.pdf)
- **Knowledge manipulation** (construct), 1 paper
  > We adopt question-answer style probes (QA) to assess the ability of the unlearned model to utilize knowledge in practical applications. (Section 3.3.1)
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hallucination** (behavioral indicator), 1 paper
  > However, we also observed that autoregressive large language models like GPT-4o-mini tend to hallucinate responses... in answering questions within the privacy policy context.
  - [Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf)
- **RAGTruth** (measurement instrument), 1 paper
  > RAGTruth is the first high-quality, manually annotated RAG hallucination dataset. The data includes three RAG task types: Question Answering (QA), Data-to-Text Writing, and News Summarization.
  - [ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability](https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf)
- **Knowledge retention** (construct), 1 paper
  > Retention can be measured by querying θn with questions related to each xi for i ∈{1, . . . , n −1}. (Section 3.1)
  - [Self-Updatable Large Language Models by Integrating Context into Model Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b0c4fc1bd52329279c51ad2ddec9ace-Paper-Conference.pdf)
- **Knowledge memorization** (construct), 1 paper
  > We measure a model f’s memorization of knowledge from the forget set Dforget as follows: for each example x ∈Dforget associated with a question-answer pair (q, a), we gather the model’s answer to the question q, denoted f(q). (Section 3.1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Task generalization** (construct), 1 paper
  > AQuilt achieves better task generalization by incorporating Chinese data and defining more flexible task types. Specifically, AQuilt assigns the task type as closed/open-book QA and uses task requirements as question prefixes. (Section 4.3)
  - [AQuilt: Weaving Logic and Self-Inspection into Low-Cost, High-Relevance Data Synthesis for Specialist LLMs](https://aclanthology.org/2025.emnlp-main.293.pdf)
- **Long-context understanding** (construct), 1 paper
  > ...achieving substantial progress on tasks such as summarization and question answering that emphasize the effective utilization and understanding of long inputs.
  - [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf)
