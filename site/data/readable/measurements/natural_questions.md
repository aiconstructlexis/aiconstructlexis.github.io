# Natural Questions
**Type:** Measurement instrument  
**Supporting papers:** 166  
**Also known as:** NQ, NQ-Open, NaturalQuestion, NaturalQuestions, NQ dataset, Nature Questions, NaturalQuestions (NQ-Open), NQ Open, Natural Questions (NQ), NATURAL QUESTIONS (NQ), NaturalQA, NaturalQuestions-Open  

## State of the Field

**What it is.** Across the papers, Natural Questions is most commonly treated as a question answering benchmark built from real user Google Search queries, usually paired with Wikipedia answers or passages. The dominant framing is open-domain, knowledge-intensive, and often single-hop, though some authors instead describe it as closed-book, fact-recall, world-knowledge, or retrieval evaluation. Papers also refer to an open-domain variant, NQ-Open or NaturalQuestions-Open, and to versions with short and long answers, golden and distractor passages, or retrieved documents with the gold document placed at different positions; some studies evaluate it in 0-, 3-, 5-, or 32-shot form, or use subsets such as 10,000 queries and the 3,610-pair NQ-Open validation set.

**What it is claimed to measure.** Papers link Natural Questions to 9 constructs and 9 behavioral indicators. The prevailing use is to measure question answering, especially open-domain question answering, and some work also uses it for text generation. Construct claims are less concentrated on a single target: world knowledge is the most recurrent framing, editing locality is another recurring use, and papers also attach the benchmark to several other constructs.

**Space of uses.** In use, papers usually place it beside other QA benchmarks, most often TriviaQA, WebQuestions, and HotpotQA, as one of several representative datasets for RAG, retrieval, or factual QA. It is related to 2 other measurement instruments, BEIR and HELMET, and papers also use it more indirectly as an out-of-domain or control benchmark, or as a source of prompt, training, or locality questions.

## Sources

**Natural Questions** (30 papers: [INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://proceedings.iclr.cc/paper_files/paper/2024/file/0d1986a61e30e5fa408c81216a616e20-Paper-Conference.pdf), [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation](https://proceedings.iclr.cc/paper_files/paper/2024/file/bda88ed2892f5e61c9a9bf215c566913-Paper-Conference.pdf), [SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/428ceef2cd8a53add7213e04d1746479-Paper-Conference.pdf), [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf), [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf), [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf), [Are LLM-Judges Robust to Expressions of Uncertainty? Investigating the effect of Epistemic Markers on LLM-based Evaluation](https://aclanthology.org/2025.naacl-long.452.pdf), [Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective](https://aclanthology.org/2025.naacl-long.151.pdf), [Teaching Models to Balance Resisting and Accepting Persuasion](https://aclanthology.org/2025.naacl-long.412.pdf), [PA-RAG: RAG Alignment via Multi-Perspective Preference Optimization](https://aclanthology.org/2025.naacl-long.459.pdf), [CartesianMoE: Boosting Knowledge Sharing among Experts via Cartesian Product Routing in Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.505.pdf), [RAG LLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.281.pdf), [Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.275.pdf), [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf), [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf), [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf), [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf), [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf), [IQA-EVAL: Automatic Evaluation of Human-Model Interactive Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a23b26eaaefd187973658f5001f4fe-Paper-Conference.pdf), [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf), [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf), [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf), [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf), [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf), [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf), [Semantic Density: Uncertainty Quantification for Large Language Models through Confidence Measurement in Semantic Space](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26d4fbaf7dfa115f1d4b3f104e26bce-Paper-Conference.pdf), [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf), [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf))
> Natural Questions (NQ) is a closed-book question answering dataset derived from real user queries, used for evaluation.

**NaturalQA** (5 papers: [Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf), [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf), [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf), [M+: Extending MemoryLLM with Scalable Long-Term Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25au/wang25au.pdf), [InfoGain-RAG: Boosting Retrieval-Augmented Generation through Document Information Gain-based Reranking and Filtering](https://aclanthology.org/2025.emnlp-main.365.pdf))
> A question answering benchmark included in the expanded evaluation set.

**NQ** (10 papers: [Making Retrieval-Augmented Language Models Robust to Irrelevant Context](https://proceedings.iclr.cc/paper_files/paper/2024/file/8011b23e1dc3f57e1b6211ccad498919-Paper-Conference.pdf), [Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce806d8b4bf38cd92d483e5a0490d983-Paper-Conference.pdf), [Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/639a9a172c044fbb64175b5fad42e9a5-Paper-Conference.pdf), [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf), [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf), [Hierarchical Document Refinement for Long-context Retrieval-augmented Generation](https://aclanthology.org/2025.acl-long.176.pdf), [LLM Alignment as Retriever Optimization: An Information Retrieval Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25k/jin25k.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf), [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf), [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf))
> Natural Questions benchmark, a real-world question answering dataset requiring retrieval and comprehension of factual information, evaluated in a 32-shot setting.

**NQ-Open** (5 papers: [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf), [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf), [Demystifying Domain-adaptive Post-training for Financial LLMs](https://aclanthology.org/2025.emnlp-main.1579.pdf), [Hallucination Detection in LLMs Using Spectral Features of Attention Maps](https://aclanthology.org/2025.emnlp-main.1239.pdf), [The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs](https://aclanthology.org/2025.emnlp-main.1761.pdf))
> An open-domain question-answering benchmark derived from the Natural Questions dataset, where questions are real user queries to a search engine.

**NaturalQuestions** (5 papers: [Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/26d3c9a66836ded8f34a944f2bfe868e-Paper-Conference.pdf), [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf), [Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models](https://aclanthology.org/2025.acl-long.533.pdf), [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf), [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf))
> A question-answering dataset derived from real user queries to the Google search engine, cited as an example of a world knowledge benchmark.

**NaturalQuestion** (3 papers: [Determine-Then-Ensemble: Necessity of Top-k Union for Large Language Model Ensembling](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbb10d319d44f8c3b4720873e4177c65-Paper-Conference.pdf), [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf), [HFT: Half Fine-Tuning for Large Language Models](https://aclanthology.org/2025.acl-long.626.pdf))
> A question-answering corpus of queries issued to the Google search engine.

**NQ dataset** (1 paper: [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf))
> A dataset used to source text questions for evaluating locality in knowledge editing.

**Nature Questions** (1 paper: [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf))
> A question answering dataset used to evaluate QA behavior under dynamic input streams.

**NaturalQuestions (NQ-Open)** (1 paper: [Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/97e2df4bb8b2f1913657344a693166a2-Paper-Conference.pdf))
> A question answering dataset of Google search queries with annotated answers from Wikipedia and multiple annotators.

**NQ Open** (1 paper: [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf))
> Open-domain version of the Natural Questions dataset, used for evaluating question answering and hallucination detection in realistic settings.

**Natural Questions (NQ)** (1 paper: [Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf))
> A question answering dataset used to evaluate RAG system performance by varying the number of retrieved passages.

**NATURAL QUESTIONS (NQ)** (1 paper: [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf))
> A question answering dataset consisting of real user questions posed to Google search and corresponding answers found in Wikipedia articles.

**NaturalQuestions-Open** (2 papers: [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf), [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf))
> A dataset subset used for MDQA experiments to evaluate context awareness across various contextual positions.

## Relationships

### → Natural Questions
- **Question answering** (behavioral indicator): *measured_by*, 19 papers
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
- **Open-domain question answering** (behavioral indicator): *measured_by*, 10 papers
  > We evaluate BTR on five knowledge-rich NLP tasks, including three open-domain question-answering tasks (NaturalQuestions (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017), and WebQA (Berant et al., 2013)) (Section 2).
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
  - [Block-Attention for Efficient Prefilling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
  - [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf)
  - [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf)
  - [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf)
  - [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf)
  - [Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://aclanthology.org/2025.acl-long.770.pdf)
  - [InfoGain-RAG: Boosting Retrieval-Augmented Generation through Document Information Gain-based Reranking and Filtering](https://aclanthology.org/2025.emnlp-main.365.pdf)
  - [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1371.pdf)
- **World knowledge** (construct): *measured_by*, 5 papers
  > World Knowledge (5-shot): NaturalQuestions (NQ, Kwiatkowski et al. (2019))... (Section 4.2).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 3 papers
  > We have conducted additional experiments on more realistic open-ended generations datasets, Hot-PotQA [57], Natural Question (NQ) [23], TriviaQA [21]. (Appendix D)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
- **Factuality** (construct): *measured_by*, 2 papers
  > "factual QA accuracy (exact match on NaturalQuestions and F1 score on TriviaQA)"
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [PruneCD: Contrasting Pruned Self Model to Improve Decoding Factuality](https://aclanthology.org/2025.emnlp-main.1651.pdf)
- **Editing locality** (construct): *measured_by*, 2 papers
  > The unrelated tuples (xu i , yu i )m i=1 are sampled from Natural Questions (NQ; Kwiatkowski et al., 2019). (Section 5).
  - [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf)
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)
- **Factual recall** (behavioral indicator): *measured_by*, 2 papers
  > (f) fact recall (WebQuestions (Berant et al., 2013), Natural Questions (Kwiatkowski et al., 2019)) (Section 4.2)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Open-ended question answering** (behavioral indicator): *measured_by*, 2 papers
  > Specifically, we consider the open-ended QA task, where the model is prompted to generate the answer in a declarative form given a question. To validate our method and its theoretical guarantee on controlling FDR-E, we create a dataset on textual entailment using the Natural Questions (NQ) dataset [17] for each GLM. (Section A.3.2).
  - [Selective Generation for Controllable Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a6815122f533193a022cbc41786c1cc-Paper-Conference.pdf)
  - [Influences on LLM Calibration: A Study of Response Agreement, Loss Functions, and Prompt Styles](https://aclanthology.org/2025.acl-long.188.pdf)
- **Factual question answering** (behavioral indicator): *measured_by*, 2 papers
  > Our evaluations cover factual question answering (NaturalQuestions (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017)) (Section 4.2).
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **Generalization** (construct): *measured_by*, 2 papers
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Factual knowledge** (construct): *measured_by*, 2 papers
  > For factual knowledge, we use PopQA (Mallen et al., 2023), TriviaQA (Joshi et al., 2017), and Natural Questions (NQ) (Kwiatkowski et al., 2019). (Section 5)
  - [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf)
  - [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > We conduct main experiments on Natural Questions (NQ) [21] and TriviaQA [18] datasets, both of which are widely used retrieval benchmarks... We use passage-level Hits@{1, 5} and Mean Reciprocal Rank (MRR)@5 as evaluation metrics.
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Knowledge-based question answering** (behavioral indicator): *measured_by*, 1 paper
  > “Datastore scaling brings major improvements to knowledge-intensive question answering tasks such as NQ and TQA”
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Knowledge conflict resolution** (construct): *measured_by*, 1 paper
  > We benchmark the current LLM’s ability to perform situated faithful reasoning on several question-answering tasks, including FreshQA (Vu et al., 2023), NaturalQA (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017), PopQA (Mallen et al., 2023).
  - [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf)
- **Hallucination resistance** (construct): *measured_by*, 1 paper
  > Gekhman et al. (2024) shows that finetuning on factual information encourages hallucinations, something that we verify observing the significant degradation on TriviaQA and NQ-Open, which are knowledge-based benchmarks.
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
- **Knowledge retention** (construct): *measured_by*, 1 paper
  > To evaluate the ability of M+ to recall long-term knowledge, we follow the experimental setup in MemoryLLM (Wang et al., 2024a) on datasets SQuAD and NaturalQA (Section 4.3.1).
  - [M+: Extending MemoryLLM with Scalable Long-Term Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25au/wang25au.pdf)
- **Memorization** (construct): *measured_by*, 1 paper
  > “Simple QA primarily evaluates the ability to recall and retrieve factual knowledge accurately.” and “we randomly collect 1, 000 queries from the NaturalQuestions (NQ) dataset”
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **Single-hop question answering** (behavioral indicator): *measured_by*, 1 paper
  > “Natural Questions (NQ; Kwiatkowski et al., 2019), Single-hop QA”
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)

### Associated with
- **HELMET** (measurement instrument), 1 paper
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **BEIR** (measurement instrument), 1 paper
  > “nine public datasets in the BEIR benchmark (Thakur et al., 2021), including ... NQ (Kwiatkowski et al., 2019)”
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
