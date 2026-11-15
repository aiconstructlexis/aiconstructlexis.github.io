# Language modeling ability
**Type:** Construct  
**Supporting papers:** 29  
**Also known as:** Language modeling quality, Language modeling capability, Language modelling capability, Predictive capability, Predictive performance, Source-language modeling  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats language modeling ability as a model-level, often latent capability to understand and generate plausible, coherent, or meaningful text. Most definitions tie it to next-token prediction, token probability distributions, prediction loss, or perplexity, and one paper explicitly defines the general ability as independent of factual correctness. A smaller line of work defines it more operationally as performance on broad language-modeling evaluations across domains and tasks, and a few papers narrow the scope to a retriever encoder's capacity to model document text or a decoder's source-language modeling ability for translation and transcription.

**Space of facets.** Papers do not offer a stable facet taxonomy, and instead organize the concept through overlapping names and scopes. The dominant near-synonyms are language modeling quality, language modeling capability, and language modelling capability, while some authors use predictive capability or predictive performance for closely related ideas, with the latter explicitly defined through metrics like perplexity and zero-shot task accuracy. The same label is also used for different scopes: general or basic language modeling ability, short-context language modeling ability, a retriever-specific version tied to document modeling, and source-language modeling; a recurring distinction separates this ability from factual knowledge or factual correctness.

**Space of measurement.** Operationalization is broad but benchmark-centered: papers link the construct to 15 measurement instruments and 1 behavioral indicator. The most frequently linked instruments are WikiText-2, LAMBADA, WikiText, WikiText-103, and C4, and papers usually operationalize the construct with perplexity, log perplexity, cross-entropy loss, or prediction loss, with one paper stating that lower perplexity on WikiText-2 reflects stronger language modeling ability. Papers also use 10 other instruments, and some assessments move beyond next-token evaluation to downstream-task suites, short-context tasks, zero-shot accuracy, and benchmark-specific scores. These choices mostly match definitions centered on token prediction and probability modeling, though some operationalizations broaden the construct to general language tasks.

**Links.** Beyond measurement, papers only report related links. One paper relates language modeling ability to text generation quality, phrasing the connection as a hypothesis that perplexity measurements and generation quality are strongly related. Another paper treats text summarization as related when checking whether a tuning method might harm other downstream language skills. No papers claim a causal relationship or correlation.

## Sources

**Language modeling quality** (1 paper: [Cost-Optimal Grouped-Query Attention for Long-Context Modeling](https://aclanthology.org/2025.emnlp-main.272.pdf))
> The model's underlying ability to understand and generate coherent and probable sequences of text, typically measured by its prediction loss.

**Language modeling ability** (6 papers: [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf), [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf), [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf), [Perplexity Trap: PLM-Based Retrievers Overrate Low Perplexity Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf), [KV-Latent: Dimensional-level KV Cache Reduction with Frequency-aware Rotary Positional Embedding](https://aclanthology.org/2025.acl-long.77.pdf), [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf))
> The model's core capability to understand and generate plausible, meaningful text, which should be preserved during debiasing interventions.

**Language modeling capability** (4 papers: [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf), [Beware of Calibration Data for Pruning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ede933e10afa991a10b6f36b6522129-Paper-Conference.pdf), [Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models](https://aclanthology.org/2025.acl-long.118.pdf), [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf))
> The fundamental ability of a model to understand and generate plausible sequences of text, which can be recovered more easily than factual knowledge during fine-tuning.

**Language modelling capability** (1 paper: [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf))
> The latent ability of the model to predict and generate coherent language sequences, often inferred from probability distributions over tokens.

**Predictive capability** (1 paper: [Language Modeling Is Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/3cbf627fa24fb6cb576e04e689b9428b-Paper-Conference.pdf))
> The latent ability of a model to accurately predict the next symbol in a sequence based on prior context, reflecting its underlying probabilistic modeling strength.

**Predictive performance** (1 paper: [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf))
> The overall ability of a language model to make accurate predictions, as measured by metrics like perplexity and zero-shot task accuracy.

**Source-language modeling** (1 paper: [Whisper-UT: A Unified Translation Framework for Speech and Text](https://aclanthology.org/2025.emnlp-main.148.pdf))
> The latent ability of the decoder to understand and represent the source language effectively, whether derived from speech or text, which supports improved translation and transcription.

## Relationships

### Language modeling ability →
- **WikiText-2** (measurement instrument): *measured_by*, 6 papers
  > WikiText-2 and WikiText-103 (Merity et al., 2016) are two commonly used language modeling benchmarks consisting of high-quality Wikipedia articles. (Section 4.1.1)
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
  - [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf)
  - [Mixture of Weight-shared Heterogeneous Group Attention Experts for Dynamic Token-wise KV Optimization](https://aclanthology.org/2025.emnlp-main.1166.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **WikiText-103** (measurement instrument): *measured_by*, 3 papers
  > WikiText-2 and WikiText-103 (Merity et al., 2016) are two commonly used language modeling benchmarks consisting of high-quality Wikipedia articles. (Section 4.1.1)
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
  - [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 3 papers
  > We chose the LAMBADA dataset (Paperno et al., 2016) for evaluation, as it tests a model’s ability to predict the final word of a passage, directly assessing language modeling capability without relying on specific knowledge, making it suitable for comparing models with small-scale training. (Section 6.3.2)
  - [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf)
  - [LLM Data Selection and Utilization via Dynamic Bi-level Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25g/yu25g.pdf)
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **WikiText** (measurement instrument): *measured_by*, 3 papers
  > “we examine the impact of these intervention strategies on both task performance and language modeling capability, with the latter measured using cross-entropy loss on the pre-training dataset (i.e, WikiText).”
  - [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf)
  - [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **PTB** (measurement instrument): *measured_by*, 2 papers
  > We evaluate quantized model performance by two metrics. Firstly, we measure perplexity, measured on the WikiText2 (Merity et al., 2016), Penn Treebank (Marcus et al., 1994) and C4 (Raffel et al., 2020) datasets. (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
- **C4** (measurement instrument): *measured_by*, 2 papers
  > We evaluate quantized model performance by two metrics. Firstly, we measure perplexity, measured on the WikiText2 (Merity et al., 2016), Penn Treebank (Marcus et al., 1994) and C4 (Raffel et al., 2020) datasets. (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
- **WritingPrompts** (measurement instrument): *measured_by*, 1 paper
  > We use 6 English textual corpora from 5 different domains for comprehensive evaluation... (4) WritingPrompts (Fan et al., 2018) features text from the writing prompts forum of Reddit. (Section 4.1.1)
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **AG News** (measurement instrument): *measured_by*, 1 paper
  > We use 6 English textual corpora from 5 different domains for comprehensive evaluation... (5) AG News (Zhang et al., 2015) is a collection of news articles from diverse domains (Section 4.1.1)
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **StereoSet** (measurement instrument): *measured_by*, 1 paper
  > LMS is used to evaluate the language modeling abilities of models.
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurement instrument): *measured_by*, 1 paper
  > Instead, we choose the Alpaca (Taori et al., 2023) dataset, distinct from all four calibration data sources, as our language modeling test data. (Section 5.1)
  - [Beware of Calibration Data for Pruning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ede933e10afa991a10b6f36b6522129-Paper-Conference.pdf)
- **DCLM** (measurement instrument): *measured_by*, 1 paper
  > We also test the language modeling capability of the LMs on a subset of DCLM (Li et al., 2024a), a high-quality corpus carefully curated with complex pipelines, to examine how well LMs capture broad and diverse knowledge. (Section 3.1)
  - [MiniPLM: Knowledge Distillation for Pre-training Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea05e4fc0299c27648c9985266abad47-Paper-Conference.pdf)
- **GLUE** (measurement instrument): *measured_by*, 1 paper
  > To further assess preservation of language modeling capability, we also evaluated on downstream tasks: MLMs on GLUE tasks... (Section 3.3).
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > To further assess preservation of language modeling capability, we also evaluated on downstream tasks: ... ALMs using the LM Evaluation Harness (Gao et al., 2024) across 5 benchmarks... (Section 3.3).
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
- **RTE** (measurement instrument): *measured_by*, 1 paper
  > In addition, experiments on short-context language modeling tasks, like the RTE (Dagan et al., 2005)... show that our method does not affect the basic language modeling ability of Mamba. (Section 1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **PG-19** (measurement instrument): *measured_by*, 1 paper
  > “For general language tasks, models are tested for next token generation tasks with Wikitext-103 (Merity et al., 2016) (2-3k words per sample) and PG-19 (Rae et al., 2019) datasets”
  - [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf)

### Associated with
- **Text generation quality** (construct), 1 paper
  > While we believe that perplexity measurements and generation quality are strongly related, this is a hypothesis we aim to investigate in future work. (Section 6)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Text summarization** (behavioral indicator), 1 paper
  > To assess whether our IDK-tuning might harm other different downstream language skills... we evaluate the IDK-tuned Mistral-7B-v0.1 on the task of text summarization
  - [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf)
