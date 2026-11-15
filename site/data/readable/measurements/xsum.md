# XSum
**Type:** Measurement instrument  
**Supporting papers:** 83  
**Also known as:** XSUM, Xsum, xSum, X-SUM  

## State of the Field

**What it is.** Across these papers, XSum is most commonly described as an extreme or abstractive news summarization dataset or benchmark. Definitions usually say it contains BBC news articles paired with human-written, abstractive summaries, often emphasizing that the task is to produce a short single-sentence summary in English; some papers instead describe it more narrowly as a news-domain collection used as human-written or model-generated text in detection experiments.

**What it is claimed to measure.** Papers use XSum to measure 5 behavioral indicators and 2 constructs. The prevailing claims are that it measures text summarization and abstractive summarization, while smaller lines of work report it as measuring text generation, downstream task performance, and fake news generation; papers also use it to measure the constructs generalization and text generation quality. Taken together, the measurement claims center on summarization but extend to a few broader or adjacent targets.

**Space of uses.** In use, papers most often treat XSum as a summarization benchmark for fine-tuning and evaluation, for example to validate generation quality, assess generative coherence and fluency, or test decoding methods on LLM generation tasks. It is frequently run alongside CNN/DailyMail, and some papers place it with WikiLingua, XLSum, WMT tasks, or GSM8K. A smaller line of work uses it as training data or as a source of human-written news text in detection studies, and one paper adds a separate hallucination evaluation on XSUM.

## Sources

**XSum** (14 papers: [Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy](https://proceedings.iclr.cc/paper_files/paper/2024/file/e537e071277a2e5fefaa78f87500c7b4-Paper-Conference.pdf), [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf), [Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf), [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf), [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf), [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf), [Multi-Draft Speculative Sampling: Canonical Decomposition and Theoretical Limits](https://proceedings.iclr.cc/paper_files/paper/2025/file/04cdf500730af7733a6b13cbbc230206-Paper-Conference.pdf), [Evaluating Small Language Models for News Summarization: Implications and Factors Influencing Performance](https://aclanthology.org/2025.naacl-long.253.pdf), [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf), [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf), [Learning to Substitute Words with Model-based Score Ranking](https://aclanthology.org/2025.naacl-long.576.pdf), [UniICL: An Efficient ICL Framework Unifying Compression, Selection, and Generation](https://aclanthology.org/2025.acl-long.24.pdf), [Online Detection of LLM-Generated Texts via Sequential Hypothesis Testing by Betting](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bn/chen25bn.pdf), [Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels](https://aclanthology.org/2025.emnlp-main.25.pdf))
> A summarization benchmark consisting of news articles paired with abstractive summaries.

**Xsum** (3 papers: [DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/d4ce6738e84876aa79f13c8bc8b7c5eb-Paper-Conference.pdf), [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf), [DPIC: Decoupling Prompt and Intrinsic Characteristics for LLM Generated Text Detection](https://proceedings.neurips.cc/paper_files/paper/2024/file/1d35af80e775e342f4cd3792e4405837-Paper-Conference.pdf))
> The Extreme Summarization dataset, used for evaluating abstractive text summarization systems.

**XSUM** (5 papers: [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf), [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf), [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf), [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf), [Amphista: Bi-directional Multi-head Decoding for Accelerating LLM Inference](https://aclanthology.org/2025.naacl-long.450.pdf))
> A benchmark for extreme summarization, where the task is to generate a short, one-sentence summary of a news article.

**xSum** (1 paper: [OpenDebateEvidence: A Massive-Scale Argument Mining and Summarization Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c630d28df1cff44314d5798f82e02ec-Paper-Datasets_and_Benchmarks_Track.pdf))
> A dataset designed for single-sentence news summarization, used to evaluate models on a non-argumentative summarization task.

**X-SUM** (1 paper: [Beyond Text Compression: Evaluating Tokenizers Across Scales](https://aclanthology.org/2025.acl-long.1546.pdf))
> A dataset for evaluating abstractive summarization of single-sentence summaries of news articles in English, used to assess generative coherence and fluency.

## Relationships

### → XSum
- **Text summarization** (behavioral indicator): *measured_by*, 34 papers
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
- **Abstractive summarization** (behavioral indicator): *measured_by*, 6 papers
  > We start by evaluating GKD on an abstractive summarization task of generating a summary that captures salient ideas of the input document. To do so, we use the XSum dataset (Narayan et al., 2018) (Section 4.1).
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [BOND: Aligning LLMs with Best-of-N Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/947f37882a394140f7add476bb99d1d3-Paper-Conference.pdf)
  - [Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf)
  - [UNCERTAINTY-LINE: Length-Invariant Estimation of Uncertainty for Large Language Models](https://aclanthology.org/2025.emnlp-main.400.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 2 papers
  > For the NLG task, we finetune the encoder-decoder model BART-large [11] and T5-base [21] on the text summarization datasets XSum [19] and CNN/DailyMail [8]
  - [Unveiling LoRA Intrinsic Ranks via Salience Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9f00cb7dd5fbdc2175d55e2fdf1b05-Paper-Conference.pdf)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf)
- **Downstream task performance** (behavioral indicator): *measured_by*, 1 paper
  > We assess their impact on task performance, diversity of model generations, and computational requirements. Concretely, we compare MLE-based next token prediction and different IRL methods for fine-tuning LLMs on common benchmarks. ... We use the following datasets and subsets for ablation in the following sections: XSUM, GSM8k, TLDR, and WMT22.
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > We conducted additional experiments to further evaluate the robustness and generalizability of our fine-tuning techniques. These experiments included assessments on the xSum dataset
  - [OpenDebateEvidence: A Massive-Scale Argument Mining and Summarization Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c630d28df1cff44314d5798f82e02ec-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Fake news generation** (behavioral indicator): *measured_by*, 1 paper
  > "and compare them with the real news articles from the XSum (Narayan et al., 2018) dataset"
  - [AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf)
- **Text generation quality** (construct): *measured_by*, 1 paper
  > "Quality is measured in terms of BLEU for WMT and ROUGE-2 for XSum and CNNDM."
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
