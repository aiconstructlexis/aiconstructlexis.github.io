# PTB
**Type:** Measurement instrument  
**Supporting papers:** 35  
**Also known as:** Penn Treebank, Penn Treebank (PTB), Penn Tree Bank  

## State of the Field

**What it is.** Across papers, PTB is most commonly described as the Penn Treebank, a language-modeling benchmark, corpus, or dataset used for evaluating models on text prediction. The prevailing description is evaluation via perplexity, though some definitions frame it more specifically as a benchmark for next-token prediction, zero-shot performance, or log-loss under canonicality enforcement. A few papers specify particular forms of the resource, including a test split with 3761 strings, 82k words, and 439k characters, validation-set use, and a version preprocessed by Dyer et al. (2016); one paper instead uses PTB sentences annotated with PropBank as source material for analyzing grammatical features.

**What it is claimed to measure.** Papers link PTB to one construct and one behavioral indicator, so the reported measurement claims are concentrated rather than spread across many targets. The most common claim is that papers use PTB to measure language modeling ability, typically by reporting perplexity on PTB, and a separate line of work uses it to measure text generation, again through perplexity in language generation experiments. The relationship language is consistent across these claims: PTB is reported as measuring language modeling ability and text generation.

**Space of uses.** Papers most often use PTB alongside WikiText-2 and C4, and more occasionally with LAMBADA and WikiText103. In use, it is commonly one of a small set of benchmark datasets for reporting perplexity of pruned, quantized, compressed, or otherwise evaluated language models; some papers also use it under zero-shot settings without fine-tuning, and one paper uses PTB sentences as analysis material rather than as the main benchmark outcome.

## Sources

**PTB** (11 papers: [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf), [BESA: Pruning Large Language Models with Blockwise Parameter-Efficient Sparsity Allocation](https://proceedings.iclr.cc/paper_files/paper/2024/file/21e315d40ac1db66c80c78e86a447ca1-Paper-Conference.pdf), [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf), [PB-LLM: Partially Binarized Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3ab228c4703c4459b1a600ebadc5732c-Paper-Conference.pdf), [QLLM: Accurate and Efficient Low-Bitwidth Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/437bc4ccafd3fc6d4289bd10940be42b-Paper-Conference.pdf), [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf), [DLP: Dynamic Layerwise Pruning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25l/chen25l.pdf), [GRASP: Replace Redundant Layers with Adaptive Singular Parameters for Efficient Model Compression](https://aclanthology.org/2025.emnlp-main.1338.pdf), [FedSpaLLM: Federated Pruning of Large Language Models](https://aclanthology.org/2025.naacl-long.424.pdf), [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf), [Towards Next-Level Post-Training Quantization of Hyper-Scale Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab6eba9a853087993addff937c8cec87-Paper-Conference.pdf))
> PTB (Penn Treebank) is a language-modeling benchmark used to evaluate pruned models via perplexity.

**Penn Treebank** (1 paper: [Language Models over Canonical Byte-Pair Encodings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vieira25b/vieira25b.pdf))
> Corpus used for evaluating language models, specifically its test split containing 3761 strings, used here to measure log-loss improvements under canonicality enforcement.

**Penn Tree Bank** (1 paper: [Learning from Teaching Regularization: Generalizable Correlations Should be Easy to Imitate](https://proceedings.neurips.cc/paper_files/paper/2024/file/01ce1ae7f94d139e4917f9e4425a4f38-Paper-Conference.pdf))
> A language modeling benchmark used to evaluate next-token prediction performance in unsupervised pretraining experiments.

## Relationships

### → PTB
- **Text generation** (behavioral indicator): *measured_by*, 3 papers
  > we evaluate quantized models by reporting the perplexity of language generation experiments, specifically on WikiText2 (Merity et al., 2016), PTB (Marcus et al., 1994)), C4 (Raffel et al., 2020). (Section 4.1)
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
  - [STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **Language modeling ability** (construct): *measured_by*, 2 papers
  > We evaluate quantized model performance by two metrics. Firstly, we measure perplexity, measured on the WikiText2 (Merity et al., 2016), Penn Treebank (Marcus et al., 1994) and C4 (Raffel et al., 2020) datasets. (Section 5)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
