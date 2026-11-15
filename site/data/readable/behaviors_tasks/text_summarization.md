# Text summarization
**Type:** Behavioral indicator  
**Supporting papers:** 323  
**Also known as:** Summarization, Summary generation, Document description, Text abbreviation, Spotlight generation, Paper reading, Document summarization, Document Summarization  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is the production of a concise, coherent shorter text from a longer source, usually a document, article, post, or conversation, while preserving the main or salient content. Some definitions make this explicit as extractive or abstractive summarization, and several papers add quality criteria such as coverage, accuracy, coherence, overall quality, faithfulness, or factuality. A smaller group broadens the target from a standard summary to a title, a one-sentence or bullet-point summary, or a structured description of a document's attributes.

**Variants.** Most work studies document or article summarization, including news and long documents, but dialogue summarization is also recurring, and papers also cover multi-document and query-based meeting summarization. Multilingual settings appear as well, with summaries generated across several languages, and some tasks fix the output form to one sentence, a TL;DR, or key points in bullets. A smaller line of work uses nearby labels such as summary generation, document summarization, document description, text abbreviation, spotlight generation, and paper reading, and extends the behavior to domains like government reports, academic papers and abstracts, sensor data, and multi-agent conversations that are condensed into an insight or final description.

**Space of elicitation and scores.** Papers measure this behavior with 24 instruments. The most frequently linked are CNN/DailyMail, XSum, Reddit TL;DR, LongBench, and SAMSum, showing a mix of article summarization datasets, preference-style Reddit summarization, dialogue summarization, and long-context benchmarks. Scoring is often reference-based, including ROUGE-style evaluation and comparison against human-written summaries, while some papers also use human ratings of coverage, accuracy, coherence, and overall quality, or pairwise win-rate judgments with judge-based evaluators.

**What it is taken as evidence of.** Papers connect text summarization to 7 constructs rather than centering it on one shared construct. The most recurrent construct link is a recorded causal relationship from Long-context understanding to Text summarization, with papers saying longer contexts or improved long-context processing are used in tasks like document summarization. Adaptability, In-context learning, Instruction following ability, and Language modeling ability are reported as related to it, and other construct links appear as well, so papers do not use one agreed construct label for what summarization reflects.

## Sources

**Summarization** (37 papers: [Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf), [Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf), [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf), [CPPO: Continual Learning for Reinforcement Learning with Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf), [Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf), [Curiosity-driven Red-teaming for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/56ed2bd15b66f709cd81cb1aaa0496b9-Paper-Conference.pdf), [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf), [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf), [Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing](https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf), [HyperAttention: Long-context Attention in Near-Linear Time](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5aa940590399350401c57cdf52ce78-Paper-Conference.pdf), [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf), [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf), [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf), [Privately Aligning Language Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/477b39bfb9db99f60914dbfed5f23eb2-Paper-Conference.pdf), [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [Statistical Rejection Sampling Improves Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/efea6d3821a7ccae74e58892162164c0-Paper-Conference.pdf), [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf), [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf), [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf), [Asynchronous RLHF: Faster and More Efficient Off-Policy RL for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b99315234cc95e6ef281f9155b68832-Paper-Conference.pdf), [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf), [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf), [Matina: A Large-Scale 73B Token Persian Text Corpus](https://aclanthology.org/2025.naacl-long.462.pdf), [Amphista: Bi-directional Multi-head Decoding for Accelerating LLM Inference](https://aclanthology.org/2025.naacl-long.450.pdf), [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf), [LiPO: Listwise Preference Optimization through Learning-to-Rank](https://aclanthology.org/2025.naacl-long.121.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models](https://aclanthology.org/2025.naacl-long.632.pdf), [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf), [Beemo: Benchmark of Expert-edited Machine-generated Outputs](https://aclanthology.org/2025.naacl-long.357.pdf), [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf), [The Power of Many: Multi-Agent Multimodal Models for Cultural Image Captioning](https://aclanthology.org/2025.naacl-long.152.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [Design Considerations in Offline Preference-based RL](https://raw.githubusercontent.com/mlresearch/v267/main/assets/agarwal25a/agarwal25a.pdf), [SensorLLM: Aligning Large Language Models with Motion Sensors for Human Activity Recognition](https://aclanthology.org/2025.emnlp-main.19.pdf))
> The task of creating a concise and coherent version of a longer source text.

**Summary generation** (3 papers: [Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf), [zFLoRA: Zero-Latency Fused Low-Rank Adapters](https://aclanthology.org/2025.emnlp-main.1086.pdf), [PlagBench: Exploring the Duality of Large Language Models in Plagiarism Generation and Detection](https://aclanthology.org/2025.naacl-long.384.pdf))
> Producing condensed versions of input texts, evaluated for both quality and faithfulness in the summarization task.

**Document description** (1 paper: [Synthesizing Privacy-Preserving Text Data via Finetuning *without* Finetuning Billion-Scale LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25g/tan25g.pdf))
> The task of generating a structured or unstructured summary of a document's key attributes, such as its type, keywords, and tone.

**Text abbreviation** (1 paper: [SmartBench: Is Your LLM Truly a Good Chinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.194.pdf))
> The task of shortening a given text while preserving its core meaning.

**Spotlight generation** (1 paper: [Introducing Spotlight: A Novel Approach for Generating Captivating Key Information from Documents](https://aclanthology.org/2025.emnlp-main.1796.pdf))
> Producing a concise, self-contained narrative that highlights the most engaging and insightful elements of a document to encourage deeper reader exploration.

**Text summarization** (20 papers: [AutoCast++: Enhancing World Event Prediction with Zero-shot Ranking-based Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/93f01c8d9b355d7bbe3f353b44ccde66-Paper-Conference.pdf), [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf), [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf), [Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf), [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf), [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf), [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf), [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf), [Unbiased Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c5b00c5bdcc6fe35907dbcca03d27652-Paper-Conference.pdf), [Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf), [Differential Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/00b67df24009747e8bbed4c2c6f9c825-Paper-Conference.pdf), [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf), [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf), [In-Context Learning with Long-Context Models: An In-Depth Exploration](https://aclanthology.org/2025.naacl-long.605.pdf), [Learning to Summarize from LLM-generated Feedback](https://aclanthology.org/2025.naacl-long.38.pdf), [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf), [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.601.pdf), [UniICL: An Efficient ICL Framework Unifying Compression, Selection, and Generation](https://aclanthology.org/2025.acl-long.24.pdf), [Core Context Aware Transformers for Long Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cg/chen25cg.pdf), [SmartBench: Is Your LLM Truly a Good Chinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.194.pdf))
> Producing a concise summary of a longer input text, evaluated using models fine-tuned on the CNN/Daily Mail dataset.

**Paper reading** (1 paper: [ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf))
> Aggregating information from papers to form a researcher profile or condensed understanding of research materials.

**Document summarization** (4 papers: [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf), [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf), [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf), [A Training-Free Length Extrapolation Approach for LLMs: Greedy Attention Logit Interpolation](https://aclanthology.org/2025.emnlp-main.443.pdf))
> The task of generating a concise summary of one or more long documents.

**Document Summarization** (1 paper: [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf))
> Comprehending the substance and context of a given document and producing a succinct and cohesive summary.

## Relationships

### Text summarization →
- **CNN/DailyMail** (measurement instrument): *measured_by*, 39 papers
  > Summarization on CNN Dailymail. (Figure 3b)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
  - [Unbiased Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c5b00c5bdcc6fe35907dbcca03d27652-Paper-Conference.pdf)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
  - [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf)
  - [Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf)
  - [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf)
  - [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [On Giant's Shoulders: Effortless Weak to Strong by Dynamic Logits Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/34ec1286b2ccd4794c5ca4ad078b7150-Paper-Conference.pdf)
  - [Unveiling LoRA Intrinsic Ranks via Salience Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9f00cb7dd5fbdc2175d55e2fdf1b05-Paper-Conference.pdf)
  - [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
  - [VibeCheck: Discover and Quantify Qualitative Differences in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/acbfe708197ff78ad04cc1beb1710979-Paper-Conference.pdf)
  - [Towards Optimal Multi-draft Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0907335ecf28faf15be54485dbcbe70e-Paper-Conference.pdf)
  - [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf)
  - [Distributed Speculative Inference (DSI): Speculation Parallelism for Provably Faster Lossless Language Model Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/b36554b97da741b1c48c9de05c73993e-Paper-Conference.pdf)
  - [MeteoRA: Multiple-tasks Embedded LoRA for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8951bbdcf234132bcce680825e7cb354-Paper-Conference.pdf)
  - [SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b0a8df568ec496a717566a7f8158aaa-Paper-Conference.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
  - [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.601.pdf)
  - [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf)
  - [Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models](https://aclanthology.org/2025.naacl-long.632.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [Multi-Level Explanations for Generative Language Models](https://aclanthology.org/2025.acl-long.1553.pdf)
  - [MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.240.pdf)
  - [Segment-Based Attention Masking for GPTs](https://aclanthology.org/2025.acl-long.947.pdf)
  - [Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nagarajan25a/nagarajan25a.pdf)
  - [Resolving Lexical Bias in Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rizwan25a/rizwan25a.pdf)
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
  - [Gumiho: A Hybrid Architecture to Prioritize Early Tokens in Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dg/li25dg.pdf)
  - [BiMark: Unbiased Multilayer Watermarking for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25u/feng25u.pdf)
  - [Fast Large Language Model Collaborative Decoding via Speculation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25c/fu25c.pdf)
  - [polybasic Speculative Decoding Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25az/wang25az.pdf)
  - [LowRA: Accurate and Efficient LoRA Fine-Tuning of LLMs under 2 Bits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ak/zhou25ak.pdf)
  - [FLRC: Fine-grained Low-Rank Compressor for Efficient LLM Inference](https://aclanthology.org/2025.emnlp-main.755.pdf)
  - [Orthogonal Finetuning Made Scalable](https://aclanthology.org/2025.emnlp-main.1627.pdf)
  - [Paired by the Teacher: Turning Unpaired Data into High-Fidelity Pairs for Low-Resource Text Generation](https://aclanthology.org/2025.emnlp-main.1030.pdf)
  - [ZERA: Zero-init Instruction Evolving Refinement Agent – From Zero Instructions to Structured Prompts via Principle-based Optimization](https://aclanthology.org/2025.emnlp-main.1190.pdf)
- **XSum** (measurement instrument): *measured_by*, 34 papers
  > We use 61.5% test set data for XSUM (Narayan et al., 2018), 17.6% for CNN/DM (Nallapati et al., 2016), and 4.0% for MEDIASUM (Zhu et al., 2021). (Section 4.2).
  - [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf)
  - [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf)
  - [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf)
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
  - [Unveiling LoRA Intrinsic Ranks via Salience Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9f00cb7dd5fbdc2175d55e2fdf1b05-Paper-Conference.pdf)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
  - [Self-Improving Robust Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bc795afae289ed465a65a3b4b1f4eb7-Paper-Conference.pdf)
  - [SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b0a8df568ec496a717566a7f8158aaa-Paper-Conference.pdf)
  - [Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf)
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [Beyond Text Compression: Evaluating Tokenizers Across Scales](https://aclanthology.org/2025.acl-long.1546.pdf)
  - [Multi-Level Explanations for Generative Language Models](https://aclanthology.org/2025.acl-long.1553.pdf)
  - [Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](https://aclanthology.org/2025.acl-long.210.pdf)
  - [A Systematic Study of Compositional Syntactic Transformer Language Models](https://aclanthology.org/2025.acl-long.350.pdf)
  - [Segment-Based Attention Masking for GPTs](https://aclanthology.org/2025.acl-long.947.pdf)
  - [Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nagarajan25a/nagarajan25a.pdf)
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
  - [On Teacher Hacking in Language Model Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tiapkin25a/tiapkin25a.pdf)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
  - [Can RLHF be More Efficient with Imperfect Reward Models? A Policy Coverage Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25o/huang25o.pdf)
  - [LowRA: Accurate and Efficient LoRA Fine-Tuning of LLMs under 2 Bits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ak/zhou25ak.pdf)
  - [Mask-Enhanced Autoregressive Prediction: Pay Less Attention to Learn More](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuang25b/zhuang25b.pdf)
  - [Orthogonal Finetuning Made Scalable](https://aclanthology.org/2025.emnlp-main.1627.pdf)
  - [Paired by the Teacher: Turning Unpaired Data into High-Fidelity Pairs for Low-Resource Text Generation](https://aclanthology.org/2025.emnlp-main.1030.pdf)
- **Reddit TL;DR** (measurement instrument): *measured_by*, 22 papers
  > Summarization Task. SFT dataset: Reddit TL;DR dataset is used, comprising 123, 169 Reddit posts along with human-written summaries. (Section 5)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
  - [CPPO: Continual Learning for Reinforcement Learning with Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf)
  - [Privately Aligning Language Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/477b39bfb9db99f60914dbfed5f23eb2-Paper-Conference.pdf)
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
  - [Self-Improving Robust Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bc795afae289ed465a65a3b4b1f4eb7-Paper-Conference.pdf)
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
  - [Correcting the Mythos of KL-Regularization: Direct Alignment without Overoptimization via Chi-Squared Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e785d64baa2cde06c69d9b7a14636ef2-Paper-Conference.pdf)
  - [Learn Your Reference Model for Real Good Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf)
  - [Variational Best-of-N Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/402542c2341e5d2eadc1dd0891275901-Paper-Conference.pdf)
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
  - [LiPO: Listwise Preference Optimization through Learning-to-Rank](https://aclanthology.org/2025.naacl-long.121.pdf)
  - [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf)
  - [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf)
  - [Optimal Transport-Based Token Weighting scheme for Enhanced Preference Optimization](https://aclanthology.org/2025.acl-long.1035.pdf)
  - [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf)
  - [Towards Cost-Effective Reward Guided Text Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rashid25a/rashid25a.pdf)
  - [Design Considerations in Offline Preference-based RL](https://raw.githubusercontent.com/mlresearch/v267/main/assets/agarwal25a/agarwal25a.pdf)
  - [Symmetric Reinforcement Learning Loss for Robust Learning on Diverse Tasks and Model Scales](https://raw.githubusercontent.com/mlresearch/v267/main/assets/byun25a/byun25a.pdf)
  - [RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.252.pdf)
- **LongBench** (measurement instrument): *measured_by*, 21 papers
  > This benchmark encompasses a broad range of tasks, such as question-answering, summarization, and code completion, where the evaluation length ranges from 5k to 15k. (Section 4.3)
  - [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
  - [Long Context Compression with Activation Beacon](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc797c61eb18f7b3ce9a74af0ef0d876-Paper-Conference.pdf)
  - [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [ThinK: Thinner Key Cache by Query-Driven Pruning](https://proceedings.iclr.cc/paper_files/paper/2025/file/8edb116d5b288b6a9bba4c16ab647702-Paper-Conference.pdf)
  - [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf)
  - [Forgetting Transformer: Softmax Attention with a Forget Gate](https://proceedings.iclr.cc/paper_files/paper/2025/file/add3d389197ad2267f660ad060ef61f4-Paper-Conference.pdf)
  - [FocusLLM: Precise Understanding of Long Context by Dynamic Condensing](https://aclanthology.org/2025.acl-long.1500.pdf)
  - [MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560.pdf)
  - [DAC: A Dynamic Attention-aware Approach for Task-Agnostic Prompt Compression](https://aclanthology.org/2025.acl-long.952.pdf)
  - [ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25b/sun25b.pdf)
  - [CommVQ: Commutative Vector Quantization for KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25du/li25du.pdf)
  - [HashAttention: Semantic Sparsity for Faster Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/desai25a/desai25a.pdf)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
  - [GSM-$∞$: How Do your LLMs Behave over Infinitely Increasing Reasoning Complexity and Context Length?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25m/zhou25m.pdf)
  - [GATEAU: Selecting Influential Samples for Long Context Alignment](https://aclanthology.org/2025.emnlp-main.375.pdf)
- **SAMSum** (measurement instrument): *measured_by*, 13 papers
  > As an early application for Hedgehog on larger models, we convert Llama-2 7B (Touvron et al., 2023) before finetuning with low-rank adapters (LoRA) (Hu et al., 2021) on SAMSum summarization (Gliwa et al., 2019).
  - [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
  - [Adversarial Moment-Matching Distillation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbae8efcc23a0cb6d15a20f245514020-Paper-Conference.pdf)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
  - [Efficient Many-Shot In-Context Learning with Dynamic Block-Sparse Attention](https://aclanthology.org/2025.acl-long.1542.pdf)
  - [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf)
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
  - [ACING: Actor-Critic for Instruction Learning in Black-Box LLMs](https://aclanthology.org/2025.emnlp-main.965.pdf)
  - [HydraOpt: Navigating the Efficiency-Performance Trade-off of Adapter Merging](https://aclanthology.org/2025.emnlp-main.1365.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 7 papers
  > "The datasets in ∞-Bench cover diverse tasks including question answering, summarization, context retrieval, and mathematic computing."
  - [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [SCOPE: Optimizing Key-Value Cache Compression in Long-context Generation](https://aclanthology.org/2025.acl-long.529.pdf)
  - [CommVQ: Commutative Vector Quantization for KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25du/li25du.pdf)
  - [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf)
- **MultiNews** (measurement instrument): *measured_by*, 5 papers
  > We investigate the drafts produced by this 1.5B blockwise parallel LM on ... ﬁve summarization tasks: XSUM [32], MultiNews [12], SAMSum [14], NewsRoom [15] and CNN/DailyMail [17]. (Section 4)
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)
  - [Mask-Enhanced Autoregressive Prediction: Pay Less Attention to Learn More](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuang25b/zhuang25b.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
- **XLSum** (measurement instrument): *measured_by*, 5 papers
  > We select the text summarization task with the XLSum (Hasan et al., 2021) dataset as the reference task to evaluate multilingual performance as it requires the model to comprehend the input text and generate a coherent fragment. (Section 2.3)
  - [How do Large Language Models Handle Multilingualism?](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bd359b32ab8b2a6bbafa1ed2856cf40-Paper-Conference.pdf)
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
  - [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf)
  - [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf)
- **GovReport** (measurement instrument): *measured_by*, 4 papers
  > GovReport [25] is a generic summarization dataset containing long reports published by the U.S. Government Accountability Office (Section 4.1).
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
  - [Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query](https://aclanthology.org/2025.emnlp-main.1732.pdf)
- **DialogSum** (measurement instrument): *measured_by*, 3 papers
  > For the decoding stage evaluation, we conduct experiments on two summarization benchmarks: DialogSum (Chen et al., 2021) and CNN/DM (Hermann et al., 2015) (Section 4.1).
  - [FLRC: Fine-grained Low-Rank Compressor for Efficient LLM Inference](https://aclanthology.org/2025.emnlp-main.755.pdf)
  - [Efficient Compositional Multi-tasking for On-device Large Language Models](https://aclanthology.org/2025.emnlp-main.1429.pdf)
  - [Speculative Streaming: Efficient and Scalable Speculative Decoding with Multi-Stream Attention](https://aclanthology.org/2025.emnlp-main.986.pdf)
- **QMSum** (measurement instrument): *measured_by*, 2 papers
  > Summarization. We pick two summarization datasets from SCROLLS. QMSum [93] is a query-based summarization dataset, formed by meeting transcripts from multiple domains
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **ZeroSCROLLS** (measurement instrument): *measured_by*, 2 papers
  > "ZeroSCROLLS benchmark ... contains ten diverse natural language tasks that require understanding long input contexts, including summarization, question answering"
  - [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf)
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
- **BookSum** (measurement instrument): *measured_by*, 2 papers
  > BookSum [33] is a collection of datasets for long-form narrative summarization, including novels, plays, and stories (Section 4.1).
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Evaluating Copyright Takedown Methods for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/faed4276b52ef762879db4142655c699-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > For the dialogue generation and summarization tasks, we use GPT-4 for zero-shot pairwise evaluation, which is consistent with human judgments (see prompts in Appendix C.2.1). (Section 5.1)
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
- **MediaSum** (measurement instrument): *measured_by*, 1 paper
  > We use 61.5% test set data for XSUM (Narayan et al., 2018), 17.6% for CNN/DM (Nallapati et al., 2016), and 4.0% for MEDIASUM (Zhu et al., 2021). (Section 4.2).
  - [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf)
- **HaluEval** (measurement instrument): *measured_by*, 1 paper
  > Similar to DRS, we adopt the summarization data from the HaluEval [40] benchmark as the evaluation dataset (denoted as HaluSum).
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **TACT** (measurement instrument): *measured_by*, 1 paper
  > "Through TACT, the model is implicitly required to address information extraction (IE) challenges such as coreference resolution [Lee et al., 2017, Joshi et al., 2019, Kirstain et al., 2021], multi-hop reasoning [Lin et al., 2018, Dua et al., 2019, Zhao et al., 2022], summarization"
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **PubMed** (measurement instrument): *measured_by*, 1 paper
  > We further evaluate the methods on three summarization datasets. ... PubMed (Tang et al., 2023) is a collection of medical scientific articles where the goal is to summarize the conclusions of the authors... (Section 4.1)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **SummEval** (measurement instrument): *measured_by*, 1 paper
  > For this task, we use the SummEval (Fabbri et al., 2021) for text summarization evaluation. (Section 4)
  - [MetaMetrics: Calibrating Metrics for Generation Tasks Using Human Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1b248453bca182b6138b8c14a75340d-Paper-Conference.pdf)
- **TofuEval** (measurement instrument): *measured_by*, 1 paper
  > To test ADACAD on longer-form generation tasks, we evaluate on three standard summarization tasks: CNN-DM (See et al., 2017), XSum (Narayan et al., 2018), and TofuEval (Tang et al., 2024). (Section 4.1).
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
- **RULER** (measurement instrument): *measured_by*, 1 paper
  > A significant portion of long-context evaluation datasets, including RULER (Hsieh et al., 2024b), LongBench (Bai et al., 2024), LongBench v2 (Bai et al., 2025), and LOFT (Lee et al., 2024), primarily assess retrieval and summarization rather than complex reasoning. (Section 2)
  - [GSM-$∞$: How Do your LLMs Behave over Infinitely Increasing Reasoning Complexity and Context Length?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25m/zhou25m.pdf)
- **LongBench v2** (measurement instrument): *measured_by*, 1 paper
  > A significant portion of long-context evaluation datasets, including RULER (Hsieh et al., 2024b), LongBench (Bai et al., 2024), LongBench v2 (Bai et al., 2025), and LOFT (Lee et al., 2024), primarily assess retrieval and summarization rather than complex reasoning. (Section 2)
  - [GSM-$∞$: How Do your LLMs Behave over Infinitely Increasing Reasoning Complexity and Context Length?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25m/zhou25m.pdf)
- **LOFT** (measurement instrument): *measured_by*, 1 paper
  > A significant portion of long-context evaluation datasets, including RULER (Hsieh et al., 2024b), LongBench (Bai et al., 2024), LongBench v2 (Bai et al., 2025), and LOFT (Lee et al., 2024), primarily assess retrieval and summarization rather than complex reasoning. (Section 2)
  - [GSM-$∞$: How Do your LLMs Behave over Infinitely Increasing Reasoning Complexity and Context Length?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25m/zhou25m.pdf)
- **AUTO-J** (measurement instrument): *measured_by*, 1 paper
  > Since human-labeled summaries are available, we measure the win rate of the model-generated summaries against the human ones using the Auto-J model (Li et al., 2023a). (Section 7.1)
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)

### → Text summarization
- **Long-context understanding** (construct): *causes*, 5 papers
  > LLMs equipped with longer context lengths excel at handling complex tasks (Caciularu et al., 2023; Bairi et al., 2023; Mazumder & Liu, 2022), especially those with long input, e.g., document summarization. (Section 1)
  - [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf)
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
  - [E2LLM: Encoder Elongated Large Language Models for Long-Context Understanding and Reasoning](https://aclanthology.org/2025.emnlp-main.970.pdf)
  - [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf)
  - [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf)
- **Coreference resolution** (behavioral indicator): *causes*, 2 papers
  > When addressing tasks involving long-dependency issues, such as summarization... coreference resolution methods demonstrate a clear advantage over other approaches... (Section 5.1)
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
  - [Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.18.pdf)

### Associated with
- **Prompt understanding** (construct), 1 paper
  > while generally robust in classification tasks and generation tasks that mainly rely on prompt understanding (e.g., summarization, chat question-answering), we found that CS models struggle at high-level reasoning and understanding tasks.
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
- **Conditional text generation** (behavioral indicator), 1 paper
  > This issue arises in typical conditional text generation tasks, such as text summarization and data-to-text generation, where the goal is to produce fluent text based on contextual input. (ABSTRACT)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Verbosity** (construct), 1 paper
  > Consider tasks in which the lengths of the responses need to be contained in the range [llow, lhigh] to control verbosity; for example, in summarization tasks (Makino et al., 2019). (Section 6.2)
  - [L3Ms — Lagrange Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/92d3d2a9801211ca3693ccb2faa1316f-Paper-Conference.pdf)
- **Instruction following ability** (construct), 1 paper
  > Weaker instruction-following at 128k length. For summarization tasks, the summaries generated by Llama-3.1-70B-Instruct at 128k tokens become longer and often contain details not present in the reference. (Section 7.1)
  - [On Many-Shot In-Context Learning for Long-Context Evaluation](https://aclanthology.org/2025.acl-long.1245.pdf)
- **In-context learning** (construct), 1 paper
  > ICL has proven remarkably successful in handling complex tasks, including summarization (Jain et al., 2023; Baek et al., 2024) and reasoning (Wang et al., 2024a; Lee et al., 2024; Chen et al., 2024b). (Section 2)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
- **Adaptability** (construct), 1 paper
  > Li et al. (2024) investigates the factors that play a role in domain adaptation for text summarization.
  - [DA-Pred: Performance Prediction for Text Summarization under Domain-Shift and Instruct-Tuning](https://aclanthology.org/2025.emnlp-main.387.pdf)
- **Language modeling ability** (construct), 1 paper
  > To assess whether our IDK-tuning might harm other different downstream language skills... we evaluate the IDK-tuned Mistral-7B-v0.1 on the task of text summarization
  - [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > Instruction Following: four tasks to paraphrase, simplify, summarize, or generate stories
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Named entity recognition** (behavioral indicator), 1 paper
  > It is commonly accepted that the summarization task, at least in the news domain, requires NER skills to be performed effectively.
  - [Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.18.pdf)
