# Linguistic similarity
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Cross-lingual sharing  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats linguistic similarity as an internal representational property of multilingual models: languages are similar to the extent that the model uses shared internal representations or parameters for them, or shows overlapping neuron activations. One paper calculates it from overlapping neurons in the model's "internal linguistic spectrum," and another uses the nearby label cross-lingual sharing for layers with high inter-language activation similarity. A smaller line of work frames it more broadly as relatedness between languages in terms of script, vocabulary, and grammatical structures, so the main disagreement is whether similarity is located in the model's neural space or in externally described language resemblance.

**Space of facets.** No paper provides a detailed subtype taxonomy. Instead, papers use several partially overlapping labels, including cross-lingual sharing, linguistic similarity, language distance, linguistic proximity, and an "internal linguistic spectrum." These labels follow the same split seen in the definitions, with some papers emphasizing shared representations and neuron overlap, and others emphasizing closeness in script, vocabulary, and grammar.

**Space of measurement.** It is linked to no measurement instrument and no behavioral indicator. Even so, papers operationalize it through model analyses: overlapping neuron activation patterns, direct calculations of linguistic similarity or "language distance" between language pairs, and inter-language activation similarity across layers are the recurring approaches, while one paper discusses closeness through script, vocabulary, and grammatical structures. The activation-based operationalizations match the dominant internal-space definitions, whereas the script-vocabulary-grammar framing is broader than those analyses.

**Links.** The reported links all connect it to cross-lingual generalization. One paper reports that cross-lingual generalization correlates with linguistic similarity, stating that language similarity is "tied to transfer" and that closely related languages "demonstrate strong interdependence"; another paper treats linguistic similarity as related to cross-lingual generalization. No causal relationship is reported.

## Sources

**Cross-lingual sharing** (1 paper: [M-Wanda: Improving One-Shot Pruning for Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.1369.pdf))
> The degree to which a model utilizes shared internal representations and parameters to process information across different languages.

**Linguistic similarity** (1 paper: [Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages](https://aclanthology.org/2025.emnlp-main.1407.pdf))
> The degree to which languages are represented similarly in the model's internal neural space, inferred from overlapping neuron activation patterns rather than external linguistic features.

## Relationships

### → Linguistic similarity
- **Cross-lingual generalization** (construct): *correlates*, 2 papers
  > Our results show that both pretraining size and language similarity are tied to transfer, but the former has a stronger correlation.
  - [Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf)
  - [PARME: Parallel Corpora for Low-Resourced Middle Eastern Languages](https://aclanthology.org/2025.acl-long.1451.pdf)
