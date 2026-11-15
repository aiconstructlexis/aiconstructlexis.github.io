# Semantic reasoning
**Type:** Construct  
**Supporting papers:** 12  

## State of the Field

**Space of definitions.** Across the cited definitions, the term is used for a model capacity to reason about meaning, but the scope shifts by setting. One framing describes understanding language instructions and their relation to objects and actions in an environment; another describes a latent multi-step inference ability that connects concepts not explicitly stated in text, including identifying implicit targets that lack explicit textual cues. The common element is reasoning over semantic content, while the difference is whether papers anchor it in situated instructions or in implicit textual inference.

**Space of facets.** Systematization is limited, but one paper places semantic reasoning as a subtype of text-based reasoning within natural language reasoning. Elsewhere, papers use it alongside other reasoning demands rather than as a standalone taxonomy: referring expression comprehension is described as requiring both spatial and semantic reasoning, and another quoted passage discusses visual and semantic reasoning together.

**Space of measurement.** No measurement instrument is linked to it. Operationalization is instead indirect through two behavioral indicators, Referring expression understanding and Table question answering: papers describe the former as localizing an object from a complex textual query that requires spatial and semantic reasoning, and the latter as Table QA involving complex semantic reasoning and free-form responses.

**Links.** Papers only record related, not causal or correlational, links. Referring expression understanding is related to semantic reasoning because REC is described as requiring both spatial and semantic reasoning; semantic reasoning is related to Table question answering through Table QA tasks involving complex semantic reasoning and free-form responses; and natural language reasoning is related to semantic reasoning because one taxonomy lists Semantic as a subtype of text-based reasoning.

## Sources

**Semantic reasoning** (2 papers: [HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3bfee3bc6639c36e6e7b058db909f760-Paper-Conference.pdf), [LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-Shot Stance Detection](https://aclanthology.org/2025.emnlp-main.299.pdf))
> The model's capacity to understand and reason about the meaning of language instructions and their relationship to objects and actions in the environment.

## Relationships

### Associated with
- **Referring expression understanding** (behavioral indicator), 1 paper
  > This work focuses on the challenging open-vocabulary detection task of Referring Expression Comprehension (REC) (Mao et al., 2016), which involves localizing an object in an image based on a complex textual query, requiring both spatial and semantic reasoning.
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **Table question answering** (behavioral indicator), 1 paper
  > We introduce Weaver , a novel methodology integrating SQL and LLM specifically designed for Table QA tasks involving complex semantic reasoning and free-form responses. (Section 2.1)
  - [Weaver: Interweaving SQL and LLM for Table Reasoning](https://aclanthology.org/2025.emnlp-main.1436.pdf)
- **Natural language reasoning** (construct), 1 paper
  > The first broad category, Text-Based (TB) Reasoning, includes explanations that depend solely on surface-level linguistic evidence found within the premise and hypothesis, without appealing to world knowledge. Six subtypes are defined: Coreference, Syntactic, Semantic, Pragmatic, Absence of Mention and Logic Conflict. (Section 3.1)
  - [LiTEx: A Linguistic Taxonomy of Explanations for Understanding Within-Label Variation in Natural Language Inference](https://aclanthology.org/2025.emnlp-main.1728.pdf)
