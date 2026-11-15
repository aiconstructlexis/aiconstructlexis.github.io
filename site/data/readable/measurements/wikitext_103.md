# WikiText-103
**Type:** Measurement instrument  
**Supporting papers:** 61  
**Also known as:** Wikitext-103, WIKITEXT-103, Wikitext103, WIKITEXT103, WikiText103, wikitext-103-v1  

## State of the Field

**What it is.** Papers most commonly describe WikiText-103 as a larger WikiText language modeling benchmark or corpus derived from high-quality Wikipedia articles. The prevailing use is evaluation of language modeling performance, especially perplexity, though some papers use it for pre-training, as an evaluation domain for open-ended generation, or as source text for embeddings, character strings, or word-splitting experiments. Definitions and quoted passages also refer to variants and subsets such as Wikitext-103-v1, train, validation, and test splits, development and test sets, and held-out or validation sequences.

**What it is claimed to measure.** Papers link WikiText-103 to 1 construct and 3 behavioral indicators. The dominant claim is that it measures language modeling ability: papers frame it as a benchmark for language modeling, autoregressive modeling, and next-token generation, often through perplexity. Smaller lines of work report it as measuring text continuation, text generation, and text infilling, including use of validation-set sequences for MAUVE-based infilling evaluation and Wikitext-103-v1 for generation tasks.

**Space of uses.** Most papers position it as a standard or commonly used language modeling benchmark, often used for zero-shot likelihood, word prediction, and open-ended continuation evaluation. It is often used alongside other corpora, including WikiText-2, Penn Treebank, LAMBADA, GAP Corpus, and PG-19, while some studies instead use it as training data, as a source of prompts or continuations, to estimate model quantities, or to compute forgetting relative to a base model. Papers do not link it to any other measurement instrument.

## Sources

**WikiText-103** (15 papers: [A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf), [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf), [Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf), [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf), [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf), [Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf), [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.444.pdf), [Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.407.pdf), [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf), [Dynamic Sparse Training of Diagonally Sparse Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tyagi25a/tyagi25a.pdf), [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf), [ESPACE: Dimensionality Reduction of Activations for Model Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6591cc41be737e9ba4cc487ac8082d-Paper-Conference.pdf), [Learning from Teaching Regularization: Generalizable Correlations Should be Easy to Imitate](https://proceedings.neurips.cc/paper_files/paper/2024/file/01ce1ae7f94d139e4917f9e4425a4f38-Paper-Conference.pdf), [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf), [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf))
> A larger version of the WikiText benchmark, derived from high-quality Wikipedia articles for language modeling evaluation.

**Wikitext-103** (7 papers: [Language Model Decoding as Direct Metrics Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf), [RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation](https://proceedings.iclr.cc/paper_files/paper/2024/file/bda88ed2892f5e61c9a9bf215c566913-Paper-Conference.pdf), [Understanding In-Context Learning from Repetitions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d88f6f81e1aaf606776ffdd06fdf24ef-Paper-Conference.pdf), [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf), [ReGLA: Refining Gated Linear Attention](https://aclanthology.org/2025.naacl-long.147.pdf), [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf), [On Support Samples of Next Word Prediction](https://aclanthology.org/2025.acl-long.507.pdf))
> A large-scale language modeling corpus derived from high-quality Wikipedia articles, used here as an evaluation domain for open-ended text generation.

**Wikitext103** (1 paper: [Efficient Perplexity Bound and Ratio Matching in Discrete Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/23e6f78bdec844a9f7b6c957de2aae91-Paper-Conference.pdf))
> A larger version of the Wikitext dataset, derived from Wikipedia articles and used for evaluating language model perplexity.

**WIKITEXT103** (1 paper: [Neural ODE Transformers: Analyzing Internal Dynamics and Adaptive Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/82e3509393670d9d478c359b4ce6f950-Paper-Conference.pdf))
> A benchmark dataset derived from high-quality Wikipedia articles, used for evaluating language modeling performance.

**WikiText103** (2 papers: [Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a365e37c18fb91af547a2f0012a89e98-Paper-Conference.pdf), [Tractable Transformers for Flexible Conditional Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ao/liu25ao.pdf))
> A larger language modeling benchmark used to evaluate zero-shot text likelihood on a held-out corpus.

**WIKITEXT-103** (1 paper: [From Tokens to Words: On the Inner Lexicon of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aef75887979ae1287b5deb54a1e3cbda-Paper-Conference.pdf))
> A large English language modeling dataset used to source text for experiments on splitting single-token words and analyzing attention patterns.

**wikitext-103-v1** (1 paper: [From Language Models over Tokens to Language Models over Characters](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vieira25a/vieira25a.pdf))
> A large language modeling corpus derived from high-quality Wikipedia articles, used in this paper as a source of character strings for evaluating model performance.

## Relationships

### → WikiText-103
- **Language modeling ability** (construct): *measured_by*, 3 papers
  > WikiText-2 and WikiText-103 (Merity et al., 2016) are two commonly used language modeling benchmarks consisting of high-quality Wikipedia articles. (Section 4.1.1)
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
  - [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf)
- **Text continuation** (behavioral indicator): *measured_by*, 1 paper
  > WikiText-103 (Merity et al., 2017) is a standard benchmark for language modeling... (Section 4.1, Text completion)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
- **Text infilling** (behavioral indicator): *measured_by*, 1 paper
  > Evaluation of text infilling performance using the MAUVE score (↑) with 5 prompt masks... For all methods, we use the same set of 2,000 text sequences from the validation set of WikiText-103
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 1 paper
  > "For the latter, we follow (Tong et al., 2023) to use Wikitext-103-v1, a large-scale dataset derived from Wikipedia articles for language modeling tasks."
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
