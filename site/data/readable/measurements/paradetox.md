# ParaDetox
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across definitions and quoted passages, ParaDetox is described as a dataset of paired toxic and non-toxic paraphrased sentences. Papers characterize it as containing pairwise toxic and non-toxic sentences generated using paraphrasing, and one definition says it is used to identify toxicity-related features in a model's activations.

**What it is claimed to measure.** Papers use ParaDetox to measure one construct and one behavioral indicator. One usage measures Toxicity from its paired toxic and non-toxic sentences, while another reports using it for Conditional text generation and describes it as imposing the strongest conditional constraints among the compared datasets.

**Space of uses.** Papers do not link ParaDetox to other measurement instruments. In the usage in the papers evidence, one paper uses it alongside RocStories when contrasting datasets with different levels of conditional constraints, positioning ParaDetox as the more strongly constrained option rather than the relatively open-ended one.

## Sources

**ParaDetox** (1 paper: [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf))
> A dataset containing pairs of toxic and non-toxic paraphrased sentences, used to identify toxicity-related features in a model's activations.

## Relationships

### → ParaDetox
- **Toxicity** (construct): *measured_by*, 1 paper
  > "we use the ParaDetox dataset (Logacheva et al., 2022) containing pairwise “non-toxic” and “toxic” sentences"
  - [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf)
- **Conditional text generation** (behavioral indicator): *measured_by*, 1 paper
  > In particular, we focus on two datasets that significantly differ in their level of conditional constraints: RocStories (Mostafazadeh et al., 2016), which is relatively open-ended, and Paradetox (Logacheva et al., 2022), which imposes the strongest conditional constraints (Section 5.1).
  - [Conditional [MASK] Discrete Diffusion Language Model](https://aclanthology.org/2025.emnlp-main.450.pdf)
