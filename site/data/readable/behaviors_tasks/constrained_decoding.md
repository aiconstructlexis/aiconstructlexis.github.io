# Constrained decoding
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Keyword-constrained generation  

## State of the Field

**Space of definitions.** Most definitions describe constrained decoding as generation during inference in which the output must satisfy predefined constraints. The recurring examples are structural or content constraints such as knowledge base membership, syntactic rules, templates, or a specified number of markers. A smaller usage frames it as keyword-constrained generation, where the response must include a given set of anchor keywords while remaining fluent, natural, and logically coherent.

**Variants.** Papers study several constrained forms of this behavior. One line uses template-based or marker-count constraints for cross-lingual label projection, while another describes structural, syntactic, or knowledge-based constraints more broadly. A narrower variant is keyword-constrained generation for longer responses, illustrated by prompts that require using all anchor keywords in a brief climate change analysis while maintaining natural flow.

**Space of elicitation and scores.** Papers link constrained decoding to one measurement instrument, CommonGen. One paper reports that keyword-constrained generation is measured by CommonGen, described there as a dataset, and no other instrument is linked.

**What it is taken as evidence of.** No construct is linked to constrained decoding in the recorded relationships. Accordingly, the papers do not explicitly treat it as evidence of any construct.

## Sources

**Constrained decoding** (2 papers: [Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction](https://aclanthology.org/2025.emnlp-main.926.pdf), [Constrained Decoding for Cross-lingual Label Projection](https://proceedings.iclr.cc/paper_files/paper/2024/file/67390075fe466276797f489115582cdc-Paper-Conference.pdf))
> Generating model outputs that adhere to predefined structural or content constraints, such as knowledge base membership or syntactic rules, during inference.

**Keyword-constrained generation** (1 paper: [Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLMs](https://aclanthology.org/2025.emnlp-main.1754.pdf))
> Producing fluent and logically coherent text that incorporates a specified set of keywords while maintaining natural flow and semantic integrity.

## Relationships

### Constrained decoding →
- **CommonGen** (measurement instrument): *measured_by*, 1 paper
  > We test keyword-constrained generation on the commonly used CommonGen (Lin et al., 2020) dataset.
  - [DeAL: Decoding-time Alignment for Large Language Models](https://aclanthology.org/2025.acl-long.1274.pdf)
