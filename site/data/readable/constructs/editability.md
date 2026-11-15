# Editability
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Multiple edits, Lifelong knowledge editing, Editing reliability  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing treats editability as a capacity for successful model modification under repeated or ongoing editing while preserving what is already there. Definitions describe it as an "inherent capacity" to be modified efficiently without harming overall performance, as the ability to "edit multiple times without forgetting previous edits," and as continuous integration of a stream of factual updates while retaining previously acquired knowledge. A smaller framing shifts the emphasis from a model-level capacity to a method-level evaluation dimension, defining editing reliability as the degree to which a concept editing method consistently controls a target concept across different inputs.

**Space of facets.** Papers organize this concept mainly around time and retention. Some use narrower labels such as multiple edits, centered on accumulating successive updates without interference, while others use lifelong knowledge editing for continuous incorporation of a stream of factual updates. One paper instead places editing reliability within a four-dimension evaluation framework, alongside output generalization, neuron-level consistency, and mathematical formalization, so the usage spans both retention across updates and consistency of concept control.

**Space of measurement.** No measurement instrument is linked to editability, and no measured_by relationship is recorded. Papers nevertheless show one explicit evaluation pattern for the reliability framing: concept editing methods are evaluated along editing reliability and related dimensions, and one study reports that "SAE achieves the best editing reliability." Beyond this, editability is linked to one behavioral indicator, Knowledge editing, but through a causal claim rather than as a measure.

**Links.** Only one directional link is reported. One paper claims a causal relationship from Knowledge editing to Editability, stating that sequential updates gradually deviate the model from its initial state and lead to degradation in editability; the same source also says that keeping the model in its initial state avoids degradation in editability caused by sequential editing.

## Sources

**Editability** (1 paper: [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf))
> The inherent capacity of a large language model to be successfully and efficiently modified by editing techniques while maintaining its overall performance.

**Multiple edits** (1 paper: [BalancEdit: Dynamically Balancing the Generality-Locality Trade-off in Multi-modal Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25e/guo25e.pdf))
> The latent ability of a model editing system to accumulate and retain multiple knowledge updates over time without forgetting previous edits or causing interference.

**Lifelong knowledge editing** (1 paper: [WikiBigEdit: Understanding the Limits of Lifelong Knowledge Editing in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thede25a/thede25a.pdf))
> The ability of a model to continuously integrate a stream of new or updated factual information while retaining previously acquired knowledge.

**Editing reliability** (1 paper: [Towards a Unified Paradigm of Concept Editing in Large Language Models](https://aclanthology.org/2025.emnlp-main.930.pdf))
> The degree to which a concept editing method consistently and effectively controls a target concept in a model's outputs across different inputs.

## Relationships

### → Editability
- **Knowledge editing** (behavioral indicator): *causes*, 1 paper
  > The sequential updates gradually deviate the model from its initial state, leading to degradation in its editability (Ma et al., 2024; Gupta et al., 2024b). (Section 1)
  - [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf)
