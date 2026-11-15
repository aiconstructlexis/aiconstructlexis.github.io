# Semantic representation
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Text representation quality, Embedding capability, Semantic representational power  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this as a representational quality or latent ability: models are described as producing high-fidelity, contextually rich text embeddings that capture semantic meaning, or as internally encoding the meaning of words and sentences in vector form. The main variation is where the property is located, some papers frame it as an internal quality and structure of representations, while others frame it as the ability to generate downstream-useful embeddings; a smaller line also emphasizes preserving semantic relationships between words or concepts, and some definitions tie stronger embedding capability to bidirectional modeling or bidirectional attention.

**Space of facets.** Papers use several labels for nearby formulations of the construct, including text representation quality, embedding capability, and semantic representational power. Beyond that naming variation, one line of work breaks it into separate abilities to represent subsequent context and to use preceding context, reporting that bidirectional attention improves the former but weakens the latter, while another frames representational power in terms of acquiring interpretable monosemantic features while preserving the semantic relationship of words.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. When papers do indicate how they assess it, they do so descriptively, through phrases such as "higher-quality text representations," "embedding performance," the quality of "word meaning representations," or preservation of semantic relationships; one paper also says traditional metrics such as Mean Squared Error and L0 sparsity "ignore the evaluation of the semantic representational power".

## Sources

**Text representation quality** (1 paper: [Look Both Ways and No Sink: Converting LLMs into Text Encoders without Training](https://aclanthology.org/2025.acl-long.1113.pdf))
> The latent ability of a model to generate high-fidelity, contextually rich embeddings that effectively capture semantic meaning for downstream tasks.

**Semantic representation** (1 paper: [Learning to Look at the Other Side: A Semantic Probing Study of Word Embeddings in LLMs with Enabled Bidirectional Attention](https://aclanthology.org/2025.acl-long.1132.pdf))
> The quality and structure of how a model internally encodes the meaning of words and sentences in its vector representations.

**Embedding capability** (1 paper: [What Limits Bidirectional Model’s Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25y/li25y.pdf))
> The latent ability of a model to produce high-quality text representations that capture semantic meaning, enhanced by bidirectional modeling but typically at the cost of generative performance in unidirectional models.

**Semantic representational power** (1 paper: [Rethinking Evaluation of Sparse Autoencoders through the Representation of Polysemous Words](https://proceedings.iclr.cc/paper_files/paper/2025/file/380a0b16a7e6f8c5010f798c9f2d3c61-Paper-Conference.pdf))
> The capacity of a model's internal representations to accurately capture and preserve the semantic relationships between words or concepts.
