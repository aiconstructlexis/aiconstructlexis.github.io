# PAWS-X
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Across papers, PAWS-X is most commonly treated as a multilingual benchmark or dataset for paraphrase identification, where the model must decide whether two sentences have the same meaning. Some authors frame it more broadly as a multilingual natural language understanding benchmark for evaluating performance across languages, while others describe paired sentences across seven languages, adversarially constructed paraphrase pairs, and a task of distinguishing semantically equivalent sentences from near-duplicates. Definitions also mention both full multilingual use and, in one application, the Spanish portion of the dataset.

**What it is claimed to measure.** Its reported measurement role is concentrated: papers link it to 1 behavioral indicator, Paraphrase detection, and to no constructs. The prevailing usage is to treat PAWS-X as measuring paraphrase identification or paraphrase detection, including in descriptions of a cross-lingual adversarial dataset for paraphrase identification.

**Space of uses.** No other measurement instruments are linked to it. Papers commonly place it inside broader multilingual evaluation suites, for example among several benchmarks covering reasoning, understanding, and generation, or among task collections spanning NLU, NLG, MT, and QA. A smaller line of use is more targeted, with one paper using it for within-language paraphrase retrieval and another using the Spanish portion for paraphrase identification.

## Sources

**PAWS-X** (4 papers: [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf), [Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models](https://aclanthology.org/2025.acl-long.118.pdf), [M-Wanda: Improving One-Shot Pruning for Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.1369.pdf))
> A multilingual benchmark for paraphrase identification, requiring the model to determine if two sentences have the same meaning.

## Relationships

### → PAWS-X
- **Paraphrase detection** (behavioral indicator): *measured_by*, 2 papers
  > For paraphrase identification, we used the Spanish portion of PAWS-X (Yang et al., 2019), a multilingual dataset containing adversarially constructed paraphrase pairs. (Section 5.2)
  - [Exploring morphology-aware tokenization: A case study on Spanish language modeling](https://aclanthology.org/2025.emnlp-main.1552.pdf)
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf)
