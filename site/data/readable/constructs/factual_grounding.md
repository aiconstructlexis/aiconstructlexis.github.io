# Factual grounding
**Type:** Construct  
**Supporting papers:** 6  

## State of the Field

**Space of definitions.** Across the usage in the papers, factual grounding is described as alignment between a model's outputs, real-world distributions, and factual information. The same paper also ties it to producing outputs "grounded in factual information and real-world context" and to aligning models with "real-world distributions" to support such grounding (LLM Bias Detection and Mitigation through the Lens of Desired Distributions).

**Space of facets.** The only explicit systematization frames it through a desired-distribution contrast: one paper pairs equal distributions with social equity, and real-world distributions with factual grounding. In that formulation, the axis of distinction is the reference distribution used to frame bias.

**Space of measurement.** Operationalization is minimal in the linked literature. No measurement instrument is linked to factual grounding, and the only linked behavioral indicator is Information retrieval; in the recorded relationships, it appears as a claimed cause of factual grounding rather than as a direct measure.

**Links.** One paper claims a causal relationship from Information retrieval to factual grounding, stating that retrieval-augmented generation is used "to enhance factual grounding and reduce hallucination" (Uncovering Argumentative Flow: A Question-Focus Discourse Structuring Framework). Another paper reports that factual grounding is related to Social bias through the choice of desired distribution, contrasting equal distributions for social equity with real-world distributions for factual grounding.

## Sources

**Factual grounding** (1 paper: [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf))
> The degree to which a model's outputs are aligned with real-world distributions and factual information.

## Relationships

### → Factual grounding
- **Information retrieval** (behavioral indicator): *causes*, 1 paper
  > Additionally, our reconstruction strategy uses retrieval-augmented generation to enhance factual grounding and reduce hallucination. (Limitations)
  - [Uncovering Argumentative Flow: A Question-Focus Discourse Structuring Framework](https://aclanthology.org/2025.emnlp-main.416.pdf)

### Associated with
- **Social bias** (construct), 1 paper
  > Depending on application, we frame bias relative to a desired distribution—equal (for social equity) or real-world (for factual grounding) (Section 6).
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
