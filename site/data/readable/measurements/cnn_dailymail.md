# CNN/DailyMail
**Type:** Measurement instrument  
**Supporting papers:** 70  
**Also known as:** CNN-DM, CNN/Daily Mail, CNN Dailymail, CNNDM, CNN / DailyMail, CNN, CNN-DailyMail, CNN/Dailymail, CNN Daily Mail, CNN/DM, CNN-Daily Mail dataset  

## State of the Field

**What it is.** Across papers, CNN/DailyMail is most commonly described as a large-scale news summarization dataset or benchmark, built from CNN and Daily Mail articles paired with human-written summaries. The prevailing description is for text or abstractive summarization, with summaries often described as multi-sentence and sometimes as highlights; a few papers further frame it as a single-document generative summarization corpus. Definitions differ in minor details, with one paper describing it as containing just over 300k unique news articles and another using article-highlight pairs from it for citation attribution.

**What it is claimed to measure.** Papers link it to 4 behavioral indicators and 2 constructs. The dominant measurement claim is Text summarization, and papers also use it to measure Abstractive summarization, News summarization, and Text generation. Construct links are narrower: one paper uses it to measure Out-of-distribution generalization by treating CNN/DailyMail as an OOD test set for summarization, and another reports it as measuring Text generation quality, with quality measured by ROUGE-2 for CNNDM.

**Space of uses.** No other measurement instrument is linked to it. Papers often use it alongside XSum, and also with DialogSum, BBC, WMT EnDe, and SAMSUM. They position it both as a regular summarization benchmark in multi-task evaluations and as a testbed for fine-tuning, zero-shot evaluation, early-exit or speculative decoding studies, with smaller uses as an out-of-distribution test set and for citation attribution.

**Concerns raised.** A smaller line of work raises contamination concerns: one paper describes CNNDM as a dataset with higher risk of pretraining contamination and uses it to assess performance under that condition.

## Sources

**CNN/Daily Mail** (7 papers: [Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf), [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf), [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf), [Vanishing Gradients in Reinforcement Finetuning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b09bb02b90584e2be94ff3ae09289bc-Paper-Conference.pdf), [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf), [Faster In-Context Learning for LLMs via N-Gram Trie Speculative Decoding](https://aclanthology.org/2025.emnlp-main.911.pdf), [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf))
> A large-scale dataset of news articles paired with multi-sentence summaries, commonly used for evaluating text summarization.

**CNN/DM** (4 papers: [Conformal Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf), [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf), [Fast yet Safe: Early-Exiting with Risk Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea5a63f7ddb82e58623693fd1f4933f7-Paper-Conference.pdf), [FLRC: Fine-grained Low-Rank Compressor for Efficient LLM Inference](https://aclanthology.org/2025.emnlp-main.755.pdf))
> The CNN/Daily Mail dataset, a large collection of news articles paired with human-written summaries, widely used for evaluating text summarization models.

**CNN-DM** (1 paper: [Unbiased Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c5b00c5bdcc6fe35907dbcca03d27652-Paper-Conference.pdf))
> The CNN/Daily Mail dataset, a large-scale corpus of news articles paired with multi-sentence summaries, used for evaluating text summarization models.

**CNN Dailymail** (1 paper: [Cascade Speculative Drafting for Even Faster LLM Inference](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cb5b083ba4f5ca6bd05dd307a2fb354-Paper-Conference.pdf))
> A dataset for text summarization, used in a simulation to evaluate the performance of speculative decoding.

**CNN/DailyMail** (5 papers: [Efficient Beam Search for Large Language Models Using Trie-Based Decoding](https://aclanthology.org/2025.emnlp-main.748.pdf), [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf), [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf), [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf), [Unveiling LoRA Intrinsic Ranks via Salience Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9f00cb7dd5fbdc2175d55e2fdf1b05-Paper-Conference.pdf))
> A dataset consisting of news articles paired with multi-sentence summaries, commonly used to evaluate abstractive text summarization.

**CNNDM** (1 paper: [Paired by the Teacher: Turning Unpaired Data into High-Fidelity Pairs for Low-Resource Text Generation](https://aclanthology.org/2025.emnlp-main.1030.pdf))
> Document summarization benchmark based on CNN and Daily Mail articles, used to assess performance in settings with potential pretraining contamination.

**CNN / DailyMail** (1 paper: [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf))
> A widely used dataset for abstractive text summarization, consisting of news articles from CNN and the Daily Mail paired with human-written summaries.

**CNN** (1 paper: [Whoever Started the interference Should End It: Guiding Data-Free Model Merging via Task Vectors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25h/cheng25h.pdf))
> A benchmark used to evaluate summarization or news-related language understanding in the paper's Qwen-14B evaluation table.

**CNN-DailyMail** (1 paper: [Towards Optimal Multi-draft Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0907335ecf28faf15be54485dbcbe70e-Paper-Conference.pdf))
> A dataset consisting of news articles and their corresponding summaries, used to evaluate text summarization.

**CNN/Dailymail** (1 paper: [On Speeding Up Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a38cfba4c717e5a37b200294615e546e-Paper-Conference.pdf))
> A dataset of news articles paired with summaries, commonly used for evaluating text summarization.

**CNN Daily Mail** (1 paper: [Distributed Speculative Inference (DSI): Speculation Parallelism for Provably Faster Lossless Language Model Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/b36554b97da741b1c48c9de05c73993e-Paper-Conference.pdf))
> A dataset for text summarization, composed of news articles from CNN and the Daily Mail paired with human-written summaries. The paper refers to it as CNN-DM in tables.

**CNN-Daily Mail dataset** (1 paper: [Time-Reversal Provides Unsupervised Feedback to LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/34aec5ab2f99a8f592e0cca4974013f2-Paper-Conference.pdf))
> A dataset consisting of pairs of news articles and their corresponding highlights (summaries), used here to evaluate citation attribution.

## Relationships

### → CNN/DailyMail
- **Text summarization** (behavioral indicator): *measured_by*, 39 papers
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
- **Abstractive summarization** (behavioral indicator): *measured_by*, 2 papers
  > To comprehensively evaluate our method, we selected four datasets from different tasks: ...CNN/DM (See et al., 2017) for abstractive summarization... (Section 4.1)
  - [Faster Speculative Decoding via Effective Draft Decoder with Pruned Candidate Tree](https://aclanthology.org/2025.acl-long.486.pdf)
  - [Language Models Can be Efficiently Steered via Minimal Embedding Layer Transformations](https://aclanthology.org/2025.emnlp-main.1170.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > To evaluate out-of-distribution (OOD) generalisation, we specify ... one or more out-of-distribution (OOD) test sets for each task... For summarisation, the ... OOD test set is the CNN/DailyMail test set (Section 5.1).
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 1 paper
  > For the NLG task, we finetune the encoder-decoder model BART-large [11] and T5-base [21] on the text summarization datasets XSum [19] and CNN/DailyMail [8]
  - [Unveiling LoRA Intrinsic Ranks via Salience Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9f00cb7dd5fbdc2175d55e2fdf1b05-Paper-Conference.pdf)
- **News summarization** (behavioral indicator): *measured_by*, 1 paper
  > We conducted experiments on edge-deployable models... evaluating their zero-shot generative performance on news summarization... using the CNN/DM... dataset (Section 5)
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)
- **Text generation quality** (construct): *measured_by*, 1 paper
  > "Quality is measured in terms of BLEU for WMT and ROUGE-2 for XSum and CNNDM."
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
