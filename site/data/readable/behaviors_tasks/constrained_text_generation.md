# Constrained text generation
**Type:** Behavioral indicator  
**Supporting papers:** 10  
**Also known as:** Constrained generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this as an observable task where a model must generate text that obeys predefined rules or constraints. Papers commonly describe success in terms of satisfying externally imposed lexical, semantic, topical, or formal requirements, such as adhering to a topic, avoiding certain words, including specified concepts, or producing a short text that illustrates selected skills within a sentence limit. A smaller line of work frames constrained generation as producing an element in a constraint set while remaining in the generator's support, stated as generating a string in the allowed set with positive probability under the generator. Some papers also explicitly cast the constraints as logical, describing difficulty with outputs that adhere to logical constraints.

**Variants.** Papers use several nearby labels, including constrained text generation, constrained generation, and constrained decoding. Recurring variants include topic-conditioned generation, generation that avoids certain words, multi-constraint writing that combines a topic, short length, and multiple required skills, and decoding tasks presented as constrained commonsense generation (CommonGen) or harmless text generation (HTG). Some work emphasizes structural or logical constraints, while another formulation defines the target more abstractly as any string in a specified constraint set.

**Space of elicitation and scores.** No measurement instrument is linked to it. The papers operationalize it through task formulations and decoding settings, but no linked instrument is recorded as eliciting or scoring the behavior.

**What it is taken as evidence of.** The only linked construct is Logical reasoning, and the recorded relationship is related rather than measured_by, correlates, or causes. The supporting claim presents constrained text generation as one direction for incorporating logical and compositional challenges. No other construct link is recorded.

## Sources

**Constrained text generation** (3 papers: [COLLIE: Systematic Construction of Constrained Text Generation Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/a77eadda332b6d4a9ae1e0e4024555f2-Paper-Conference.pdf), [SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bbf38332580c1bed99fa99bc9ee53229-Paper-Conference.pdf), [Constrained Decoding with Speculative Lookaheads](https://aclanthology.org/2025.naacl-long.239.pdf))
> The observable task of producing text that must adhere to a specific set of predefined rules or constraints.

**Constrained generation** (2 papers: [On the Query Complexity of Verifier-Assisted Language Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/botta25a/botta25a.pdf), [Controllable Generation via Locally Constrained Resampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/d98ce7a82af78cd02968e79ea3fe89e8-Paper-Conference.pdf))
> The latent ability of a language model to produce outputs that satisfy externally imposed structural constraints while remaining in the generator's support.

## Relationships

### Associated with
- **Logical reasoning** (construct), 1 paper
  > We posit that one direction is incorporating logical and compositional challenges via constrained text generation.
  - [COLLIE: Systematic Construction of Constrained Text Generation Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/a77eadda332b6d4a9ae1e0e4024555f2-Paper-Conference.pdf)
