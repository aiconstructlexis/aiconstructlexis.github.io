# Redundancy
**Type:** Construct  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** One paper defines redundancy as an internal representation property: features are distributed across multiple neurons rather than concentrated in a single unit, and this distribution is said to support robustness to noise or perturbation. The accompanying quoted passage uses the same framing, describing redundancy as distributed feature coding that discourages monosemantic code.

**Space of facets.** Usage in the papers organizes redundancy through contrasts rather than subtypes: it is opposed to features being concentrated in a single unit, and one quoted passage says this distributed coding discourages monosemantic code. A related paper also connects redundancy to polysemanticity and describes polysemantic code as favoring redundancy for robustness.

**Space of measurement.** Redundancy is linked to 1 measurement instrument and no behavioral indicators. The only linked instrument is LLM-as-a-judge: one paper assesses redundancy by instructing an LLM to count the number of unique main statements within a set of candidate summaries. This operationalization concerns summary content, whereas the explicit definition concerns how features are distributed across neurons.

**Links.** Beyond measurement, the only reported link is that redundancy is related to polysemanticity. One paper describes polysemantic code as favoring redundancy for robustness, and no causal or correlational relationship is reported.

## Sources

**Redundancy** (1 paper: [Polysemantic Dropout: Conformal OOD Detection for Specialized LLMs](https://aclanthology.org/2025.emnlp-main.595.pdf))
> The extent to which features are distributed across multiple neurons rather than concentrated in a single unit, supporting robustness to perturbation.

## Relationships

### Redundancy →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > To assess redundancy, we instruct an LLM to count the number of unique main statements within a set of candidate summaries. (Section 3.5)
  - [Argument Summarization and its Evaluation in the Era of Large Language Models](https://aclanthology.org/2025.emnlp-main.1797.pdf)

### Associated with
- **Polysemanticity** (construct), 1 paper
  > Marshall and Kirchner (2024) connect information theory with polysemanticity where polysemantic code learned by LLMs is not only efficient but also favors redundancy for robustness (Fig. 2 of their paper).
  - [Polysemantic Dropout: Conformal OOD Detection for Specialized LLMs](https://aclanthology.org/2025.emnlp-main.595.pdf)
