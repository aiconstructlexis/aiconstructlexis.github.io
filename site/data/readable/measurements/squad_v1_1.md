# SQuAD v1.1
**Type:** Measurement instrument  
**Supporting papers:** 94  
**Also known as:** SQuAD, SQuADv1.1, SQUAD, Squad, SQuAD v1, SQuAD 1.1  

## State of the Field

**What it is.** Across the surveyed work, the dominant framing is a reading comprehension benchmark for extractive question answering, where a model answers a question from a context passage or Wikipedia article by selecting a text span. Definitions usually refer to the Stanford Question Answering Dataset version 1.1, sometimes contrasted with v2.0, and one paper notes that v1.1 contains no unanswerable questions; a few papers describe it more broadly as an open-book question answering dataset or emphasize its context, question, answer format.

**What it is claimed to measure.** Papers use it to measure 8 behavioral indicators and 5 constructs. The most frequently linked behavioral indicators are question answering, machine reading comprehension, extractive question answering, open-domain question answering, and downstream task performance; papers also link it to additional behavioral indicators and to 5 constructs, so the reported scope is spread across multiple targets rather than one construct.

**Space of uses.** Most papers position it as one benchmark within broader evaluation suites rather than a standalone protocol, often alongside GLUE, CoQA, Natural Questions, TriviaQA, and HotpotQA. Several papers use it for fine-tuning and evaluation, sometimes reporting Exact Match and F1, while a smaller line repurposes it as reference or prompt data, uses few-shot variants, or applies it in detection settings.

## Sources

**SQuAD** (21 papers: [Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/45fc8e1c55df116b23488f3cdb2fc642-Paper-Conference.pdf), [Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf), [INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://proceedings.iclr.cc/paper_files/paper/2024/file/0d1986a61e30e5fa408c81216a616e20-Paper-Conference.pdf), [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf), [Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf), [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf), [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf), [Soft Language Prompts for Language Transfer](https://aclanthology.org/2025.naacl-long.517.pdf), [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [A Survey of Post-Training Scaling in Large Language Models](https://aclanthology.org/2025.acl-long.140.pdf), [Beyond Input Activations: Identifying Influential Latents by Gradient Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.87.pdf), [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf), [Fast yet Safe: Early-Exiting with Risk Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea5a63f7ddb82e58623693fd1f4933f7-Paper-Conference.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf), [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf))
> SQuAD (Stanford Question Answering Dataset) is an open-book question answering dataset used for evaluation.

**SQuADv1.1** (3 papers: [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf), [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf), [Masked Structural Growth for 2x Faster Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2024/file/a8320b6b9d95798dc286a867c44742a1-Paper-Conference.pdf))
> Stanford Question Answering Dataset version 1.1, a reading comprehension task where models identify answer spans in a passage given a question, used to evaluate question answering performance.

**SQuAD v1.1** (3 papers: [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf), [SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3504a4fa45685d668ce92797fbbf1895-Paper-Conference.pdf), [Plug-in and Fine-tuning: Bridging the Gap between Small Language Models and Large Language Models](https://aclanthology.org/2025.acl-long.271.pdf))
> The Stanford Question Answering Dataset v1.1 is a reading comprehension benchmark for extractive question answering.

**SQUAD** (1 paper: [GraphRouter: A Graph-based Router for LLM Selections](https://proceedings.iclr.cc/paper_files/paper/2025/file/41b6674c28a9b93ec8d22a53ca25bc3b-Paper-Conference.pdf))
> The Stanford Question Answering Dataset, a crowdsourced reading comprehension benchmark consisting of questions posed on a set of Wikipedia articles.

**Squad** (1 paper: [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf))
> The Stanford Question Answering Dataset (SQuAD) is a reading comprehension benchmark where the answer to every question is a segment of text from a corresponding Wikipedia article.

**SQuAD 1.1** (1 paper: [A Lens into Interpretable Transformer Mistakes via Semantic Dependency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25n/dong25n.pdf))
> The Stanford Question Answering Dataset (version 1.1), a reading comprehension benchmark where answers are text spans extracted from a given Wikipedia article.

**SQuAD v1** (1 paper: [Cooperative or Competitive? Understanding the Interaction between Attention Heads From A Game Theory Perspective](https://aclanthology.org/2025.acl-long.688.pdf))
> The Stanford Question Answering Dataset (SQuAD) v1 is a reading comprehension benchmark where the answer to every question is a span of text from a given Wikipedia article.

## Relationships

### → SQuAD v1.1
- **Question answering** (behavioral indicator): *measured_by*, 19 papers
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
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 4 papers
  > Reading Comprehension (RC): SQuAD-3-shots [50], BoolQ-0-shot [12], and CoQA-0-shot [51].
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa27ac7aca4e462da1439b43ceebc04c-Paper-Conference.pdf)
  - [GraphRouter: A Graph-based Router for LLM Selections](https://proceedings.iclr.cc/paper_files/paper/2025/file/41b6674c28a9b93ec8d22a53ca25bc3b-Paper-Conference.pdf)
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)
- **Extractive question answering** (behavioral indicator): *measured_by*, 3 papers
  > (b) extractive question answering (SQuAD (Rajpurkar et al., 2016), CoQA (Reddy et al., 2019)) (Section 4.2)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
- **Open-domain question answering** (behavioral indicator): *measured_by*, 2 papers
  > We use the open domain question answering datasets WebQuestion (Berant et al., 2013), NaturalQA (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017) and SQuAD (Rajpurkar, 2016), as well as the complex multi-hop question answering datasets HotpotQA (Ho et al., 2020a) and 2WikiMultiHopQA (Ho et al., 2020b). (Section 4.2)
  - [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf)
  - [A Theory for Token-Level Harmonization in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a461bdff86cc07e976bb6c518810398-Paper-Conference.pdf)
- **Continual learning** (construct): *measured_by*, 1 paper
  > Continual Fine-Tuning: (a) SQuAD (Rajpurkar et al., 2016) paired with HotpotQA... (Section 4.1)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **Factual recall** (behavioral indicator): *measured_by*, 1 paper
  > To evaluate the fact recall ability of the adapted model, we use two question answering (QA) datasets, SQuAD (Rajpurkar et al., 2016) and StreamingQA (Liska et al., 2022)... (Section 4.1)
  - [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf)
- **Downstream task performance** (behavioral indicator): *measured_by*, 1 paper
  > “In Table 6, we list the performance on downstream tasks of GLUE and SAQuAD according to LIGO(Wang et al., 2023).”
  - [LOIRE: LifelOng learning on Incremental data via pre-trained language model gRowth Efficiently](https://proceedings.iclr.cc/paper_files/paper/2025/file/03945380ca5af0dc80782d8e0b72a8d7-Paper-Conference.pdf)
- **Knowledge retention** (construct): *measured_by*, 1 paper
  > To evaluate the ability of M+ to recall long-term knowledge, we follow the experimental setup in MemoryLLM (Wang et al., 2024a) on datasets SQuAD and NaturalQA (Section 4.3.1).
  - [M+: Extending MemoryLLM with Scalable Long-Term Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25au/wang25au.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > Experimental results across four datasets—Dragonball, SQUAD, NFCORPUS, and SCI-DOCS demonstrate that SAKI-RAG achieves better recall and precision compared to other RAG frameworks in long-document retrieval scenarios (Abstract).
  - [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **Factual question answering** (behavioral indicator): *measured_by*, 1 paper
  > the SQUAD, NFCORPUS, and SCI-DOCS datasets consist of factual questions involving single entities (Section 4.1).
  - [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **World knowledge** (construct): *measured_by*, 1 paper
  > "general knowledge (TriviaQA [29] and SQuAD [62])"
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
- **Natural language understanding** (construct): *measured_by*, 1 paper
  > ...language understanding (HellaSwag (Zellers et al., 2019), BoolQ (Clark et al., 2019), OpenbookQA (Mihaylov et al., 2018), SQuAD (Rajpurkar et al., 2016), MMLU (Hendrycks et al., 2021), MMLU-Pro (Wang et al., 2024), GPQA(Rein et al., 2023)) (Section 3).
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **Associative recall ability** (construct): *measured_by*, 1 paper
  > “Recall” represents the average performance across FDA, SWDE, and SQuAD. (Table 7)
  - [Scaling up the State Size of RNN LLMs for Long-Context Scenarios](https://aclanthology.org/2025.acl-long.564.pdf)
