# Compression robustness
**Type:** Construct  
**Supporting papers:** 16  
**Also known as:** Task generalization, Performance recovery  

## State of the Field

**Space of definitions.** Across the papers, the construct is treated as preservation of model capability under compression. One framing defines it as maintaining performance when parameters are heavily compressed, including especially under large compression ratios; another treats it as preserving performance across in-domain and out-of-domain evaluation settings; a further framing recasts it as the latent ability of a pruned model to regain the functional capabilities of its dense counterpart after compression. The main difference is whether authors present it as observed performance retention or as a latent recovery ability inferred from observed metrics.

**Space of facets.** The papers organize the idea around overlapping aspects rather than a settled single terminology: stability under heavy compression, task generalization across evaluation settings, and post-pruning performance recovery. The labels "compression robustness," "task generalization," and "performance recovery" are used for these nearby emphases, so the same general theme is named differently and scoped differently across papers.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to it. In practice, papers operationalize it by checking whether compressed models maintain performance under large compression ratios, preserve performance across in-domain and out-of-domain settings, datasets, and compression ratios, or recover on metrics such as perplexity across tasks and sparsity levels after pruning. These operationalizations largely track the definitions directly, with some papers emphasizing maintenance under compression and another emphasizing recovery after pruning.

## Sources

**Compression robustness** (1 paper: [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf))
> The extent to which an LLM maintains performance when its parameters are heavily compressed.

**Task generalization** (1 paper: [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf))
> The extent to which a compressed model preserves performance across in-domain and out-of-domain evaluation settings.

**Performance recovery** (1 paper: [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf))
> The latent ability of a pruned model to regain the functional capabilities of its original dense counterpart after compression, inferred from improvements in metrics like perplexity across tasks and sparsity levels.
