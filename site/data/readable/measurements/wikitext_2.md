# WikiText-2
**Type:** Measurement instrument  
**Supporting papers:** 139  
**Also known as:** Wikitext-2, wikitext-2, WikiText2, Wikitext2, WikiText-V2, WikiText2-v1, WT-2  

## State of the Field

**What it is.** Across papers, the dominant framing is a language modeling benchmark or dataset, usually described as cleaned, curated, or high-quality Wikipedia text and evaluated with perplexity on validation or test text. Several papers treat it as a held-out benchmark for compressed, quantized, pruned, or fine-tuned models, while some use the training split, train models from scratch on it, or run zero-shot evaluation without fine-tuning. Papers also use several surface forms, including WikiText2, Wikitext2, and WT-2, and a smaller line of work mentions variants such as WikiText2-v1, described as over 100 million tokens and used for hidden-state analysis plus validation-set perplexity, and WikiText-V2.

**What it is claimed to measure.** Papers link WikiText-2 to 7 constructs and 1 behavioral indicator. The prevailing claims use it to measure language modeling ability and the behavioral indicator text generation, usually through perplexity or LM loss; several papers also state that lower perplexity on Wikitext-2 reflects stronger language modeling ability. Less commonly, papers report it as measuring general ability, generative ability, and linguistic quality, with additional construct-level links appearing beyond those claims.

**Space of uses.** In use, papers most often position WikiText-2 as a recurring perplexity benchmark for model comparison, commonly alongside C4 and PTB, and also with WikiText-103 and LAMBADA in multi-benchmark evaluations. A smaller line of work uses it as calibration data, for example by selecting random token segments or samples from WikiText-2, and some papers use its training split for slicing, hypernetwork training, or training models from scratch. Among named instrument-to-instrument links, one paper relates it to lm-evaluation-harness by stating that it uses the harness to report results on Wikitext2.

**Concerns raised.** Explicit concerns are limited. One paper says current PTQ methods typically rely on domain-specific calibration datasets such as WikiText-2, but also says that perplexity on C4 more accurately reflects the performance of different methods.

## Sources

**WikiText-2** (20 papers: [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf), [Dynamic Sparse No Training: Training-Free Fine-tuning for Sparse LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf), [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf), [LQ-LoRA: Low-rank plus Quantized Matrix Decomposition for Efficient Language Model Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/d97a16cb83d74195b76e0bf1e85bf072-Paper-Conference.pdf), [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf), [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf), [SliceGPT: Compress Large Language Models by Deleting Rows and Columns](https://proceedings.iclr.cc/paper_files/paper/2024/file/316648eb8b4ffb6010f531b07848c300-Paper-Conference.pdf), [SeedLM: Compressing LLM Weights into Seeds of Pseudo-Random Generators](https://proceedings.iclr.cc/paper_files/paper/2025/file/222a2a46018a1e7b55ba48ba11932d04-Paper-Conference.pdf), [HIGGS: Pushing the Limits of Large Language Model Quantization via the Linearity Theorem](https://aclanthology.org/2025.naacl-long.543.pdf), [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf), [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf), [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aa/chen25aa.pdf), [QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.240.pdf), [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf), [DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf), [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf), [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf), [ShiftAddLLM: Accelerating Pretrained LLMs via Post-Training Multiplication-Less Reparameterization](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c30a37c75f062e0bf79297c73db8c6c-Paper-Conference.pdf), [Towards Next-Level Post-Training Quantization of Hyper-Scale Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab6eba9a853087993addff937c8cec87-Paper-Conference.pdf), [fMRI predictors based on language models of increasing complexity recover brain left lateralization](https://proceedings.neurips.cc/paper_files/paper/2024/file/e28e19d00b23fe0265f433fa05a96b06-Paper-Conference.pdf))
> Language modeling benchmark that evaluates perplexity on a standard validation set to assess generative performance of pruned LLMs.

**wikitext-2** (2 papers: [The LLM Surgeon](https://proceedings.iclr.cc/paper_files/paper/2024/file/38a1671ab0747b6ffe4d1c6ef117a3a9-Paper-Conference.pdf), [On Support Samples of Next Word Prediction](https://aclanthology.org/2025.acl-long.507.pdf))
> A standard benchmark dataset derived from Wikipedia articles, used to evaluate the language modeling capabilities of models after compression.

**Wikitext-2** (2 papers: [JoMA: Demystifying Multilayer Transformers via Joint Dynamics of MLP and Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c93b3cd3bc60c0fe7b0c2d74a2da966-Paper-Conference.pdf), [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf))
> A language modeling dataset (Wikitext2) used to train models from scratch and observe their training dynamics.

**WikiText2** (10 papers: [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf), [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf), [SKIM: Any-bit Quantization Pushing The Limits of Post-Training Quantization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25c/bai25c.pdf), [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf), [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf), [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf), [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf), [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf), [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf), [SlimGPT: Layer-wise Structured Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf))
> A language modeling dataset used here as a generation evaluation dataset for measuring quantized model performance.

**Wikitext2** (1 paper: [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf))
> A language modeling benchmark dataset (also known as WikiText-2) used to evaluate model performance via perplexity.

**WikiText-V2** (1 paper: [PICASO: Permutation-Invariant Context Composition with State Space Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0730b81dbc16cce7e85b519cb7fe5a8d-Paper-Conference.pdf))
> A large-scale language modeling benchmark dataset derived from high-quality Wikipedia articles, used to evaluate a model's ability to predict text continuations.

**WikiText2-v1** (1 paper: [Demystifying Singular Defects in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25es/wang25es.pdf))
> A dataset of over 100 million tokens from high-quality Wikipedia articles, used in this paper for analyzing hidden states and evaluating model perplexity after quantization.

**WT-2** (1 paper: [FedSpaLLM: Federated Pruning of Large Language Models](https://aclanthology.org/2025.naacl-long.424.pdf))
> Short for WikiText-2, a language modeling benchmark dataset derived from Wikipedia articles, used to evaluate model perplexity.

## Relationships

### → WikiText-2
- **Text generation** (behavioral indicator): *measured_by*, 11 papers
  > we evaluate quantized models by reporting the perplexity of language generation experiments, specifically on WikiText2 (Merity et al., 2016), PTB (Marcus et al., 1994)), C4 (Raffel et al., 2020). (Section 4.1)
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
  - [OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f2fc4053a66edfa430bcdf9a6ff3b17-Paper-Conference.pdf)
  - [MoDeGPT: Modular Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb7214d2fdfd84165b08539d59c92e07-Paper-Conference.pdf)
  - [STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking](https://proceedings.iclr.cc/paper_files/paper/2025/file/510e7d39fce008a3e31de54b8f5be9ac-Paper-Conference.pdf)
  - [Probe Pruning: Accelerating LLMs through Dynamic Pruning via Model-Probing](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44efaa3b7a389ea56c7ee9d6589e800-Paper-Conference.pdf)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
  - [La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cj/liu25cj.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
  - [Machine-generated text detection prevents language model collapse](https://aclanthology.org/2025.emnlp-main.1506.pdf)
- **Language modeling ability** (construct): *measured_by*, 6 papers
  > WikiText-2 and WikiText-103 (Merity et al., 2016) are two commonly used language modeling benchmarks consisting of high-quality Wikipedia articles. (Section 4.1.1)
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
  - [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf)
  - [Mixture of Weight-shared Heterogeneous Group Attention Experts for Dynamic Token-wise KV Optimization](https://aclanthology.org/2025.emnlp-main.1166.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > "To ensure the desired model capabilities are not impacted by editing, we measure the perplexity of the model on the dev split of WikiText-2"
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > “for long-context modeling, we use Wikitext-2 (Merity, 2016) and PG19 (Rae et al., 2019) datasets for evaluation.”
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > For inference ability, we choose six datasets including Hellaswag [48], PIQA [1], WinoGrande [32], QNLI [31], MNLI [44], and WikiText2 [28] for evaluation.
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generative ability** (construct): *measured_by*, 1 paper
  > We assess the generative capabilities of the sparsified models on the WikiText2 (Merity et al., 2016) and C4 (Raffel et al., 2020b) datasets. (Section 4.1)
  - [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf)
- **Linguistic quality** (construct): *measured_by*, 1 paper
  > log perplexity, the average negative log-likelihood of generated tokens on the Wikitext-2 dataset (Merity et al., 2016); ... The latter two metrics measure general language quality (Section 3.1)
  - [How Does DPO Reduce Toxicity? A Mechanistic Neuron-Level Analysis](https://aclanthology.org/2025.emnlp-main.1501.pdf)
- **Text generation quality** (construct): *measured_by*, 1 paper
  > “For the base model, we evaluate the quality of text generation using the WikiText2 (Merity et al., 2016), PTB (Marcus et al., 1994), and C4 (Raffel et al., 2020) datasets.”
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)

### Associated with
- **lm-evaluation-harness** (measurement instrument), 1 paper
  > We use lm-evaluation-harness to report results on Wikitext2
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
