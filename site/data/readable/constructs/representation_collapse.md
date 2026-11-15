# Representation collapse
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Representational collapse  

## State of the Field

**Space of definitions.** Most definitions here treat representation collapse as a loss of distinctness in a model's representations: either the distortion and degradation of general pre-trained features during fine-tuning, or hidden features in deeper layers becoming highly similar. In this usage, papers describe later or intermediate layer states as overly alike, reducing expressive capacity and performance. A smaller line of work, using the label representational collapse, defines it as distinct input sequences yielding arbitrarily close last-token representations at the last layer, especially under low-precision arithmetic, so the main difference is whether collapse is framed as internal feature degradation across training and depth or as sequence-level indistinguishability at the final representation.

**Space of facets.** Papers break the construct down by where the collapse appears: in pre-trained features during downstream fine-tuning, in intermediate or later hidden states across depth, and in the final token at the last layer. Some descriptions make it explicitly layerwise, quantifying similarity between adjacent-layer inputs and describing progressive collapse in later layers, while others cast it as distinct sequences becoming arbitrarily close. Papers also use both representation collapse and representational collapse across these framings, and some descriptions place it alongside over-smoothing or say it occurs when internal representation diversity diminishes.

**Space of measurement.** No paper links it to a measurement instrument. Papers link it to one behavioral indicator, token copying, but the usage in the papers treats copying errors as an effect of collapse rather than as a direct measurement. Operationally, papers make collapse visible through representational similarity analyses, for example cosine similarity between inputs of adjacent layers, with later layers reported above 0.97 similarity in one case, or by showing that distinct sequences can have arbitrarily close final-token representations as sequence length increases; these operationalizations follow the definitions by testing whether representations stop remaining distinct.

**Links.** Papers link representation collapse to three constructs and one behavioral indicator. One paper claims a causal relationship from representation diversity to representation collapse, saying better token diversity can slow the collapse phenomenon, and another paper treats the two as related. Separate papers claim causal relationships from representation collapse to expressive power, described as reducing the ability to represent diverse features, to reasoning, described as limiting reasoning capabilities, and to token copying, where indistinguishable sequences are said to lead to errors in tasks involving counting or copying.

## Sources

**Representation collapse** (2 papers: [LiNeS: Post-training Layer Scaling Prevents Forgetting and Enhances Model Merging](https://proceedings.iclr.cc/paper_files/paper/2025/file/43ae0b566b802b2d00e525b672794b82-Paper-Conference.pdf), [MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25d/xiao25d.pdf))
> The distortion and degradation of general, pre-trained feature representations within a model during the process of fine-tuning on a specific downstream task.

**Representational collapse** (1 paper: [Transformers need glasses! Information over-squashing in language tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1d35561c4a4a0e0b6012b2af531e149-Paper-Conference.pdf))
> A phenomenon where distinct input sequences produce arbitrarily close final-token representations, making them indistinguishable to the model, especially with low-precision arithmetic.

## Relationships

### Representation collapse →
- **Token copying** (behavioral indicator): *causes*, 1 paper
  > As a result, the model is provably unable to respond to these sequences in different ways—leading to errors in, e.g., tasks involving counting or copying. (Abstract)
  - [Transformers need glasses! Information over-squashing in language tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1d35561c4a4a0e0b6012b2af531e149-Paper-Conference.pdf)
- **Expressive power** (construct): *causes*, 1 paper
  > This phenomenon, often referred to as the “over-smoothing” problem, substantially reduces the transformers’ ability to represent diverse features (Section 1).
  - [Transformer Meets Twicing: Harnessing Unattended Residual Information](https://proceedings.iclr.cc/paper_files/paper/2025/file/90cdfb6ac8d9f96bdf0ce92f5f05c391-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > "representation collapse in the model’s intermediate layers as a key factor limiting their reasoning capabilities"
  - [Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)

### → Representation collapse
- **Representation diversity** (construct): *causes*, 2 papers
  > We empirically demonstrate in Figure 1 that Twicing Attention mechanism promotes better token diversity and, therefore, it is able to slow down representation collapse phenomenon in transformers. (Section 5).
  - [Transformer Meets Twicing: Harnessing Unattended Residual Information](https://proceedings.iclr.cc/paper_files/paper/2025/file/90cdfb6ac8d9f96bdf0ce92f5f05c391-Paper-Conference.pdf)
  - [Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)
