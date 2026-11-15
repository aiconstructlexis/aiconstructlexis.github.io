# Cross-lingual consistency
**Type:** Construct  
**Supporting papers:** 5  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage treats cross-lingual consistency as whether a multilingual model gives semantically equivalent and correct outputs to the same factual query across languages. A smaller framing uses the term more broadly for model performance that stays stable and comparable across languages, especially within the same language family, so the main difference is between output-level consistency on parallel factual queries and performance-level stability across multilingual evaluations.

**Space of facets.** When papers organize the construct, they mainly do so by comparison unit: some focus on language pairs and parallel facts, while others discuss consistency among language families and within a family. This makes pairwise cross-language comparison and family-level comparison the main facets visible in the paper descriptions.

**Space of measurement.** Papers link the construct to one measurement instrument, XSafety, a parallel dataset benchmark, and to no behavioral indicators. Operationally, measurement is explicit and comparative: one paper reports a consistency score on XSafety by comparing English with each target language, and another evaluates consistency with the overlap ratio of correct predictions for parallel facts between language pairs, so assessment centers on whether correct answers align across matched multilingual inputs.

## Sources

**Cross-lingual consistency** (2 papers: [Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models](https://aclanthology.org/2025.acl-long.253.pdf), [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.364.pdf))
> The degree to which a multilingual model produces semantically equivalent and correct outputs for the same factual query when presented in different languages.

## Relationships

### Cross-lingual consistency →
- **XSafety** (measurement instrument): *measured_by*, 1 paper
  > We report consistency score on XSafety, a parallel dataset, comparing English with each target language across several models in Figure 5. (Section 5.2)
  - [MrGuard: A Multilingual Reasoning Guardrail for Universal LLM Safety](https://aclanthology.org/2025.emnlp-main.1392.pdf)
