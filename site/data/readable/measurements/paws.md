# PAWS
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across the surveyed work, the prevailing framing is PAWS as a benchmark or dataset for paraphrase detection or paraphrase identification. Definitions describe it as evaluating whether two sentences are semantically equivalent and helping assess whether models distinguish paraphrases from non-paraphrases, and one paper further characterizes it as sentence pairs with high lexical overlap that may still have different meanings. Some authors also expand the name as Paraphrase Adversaries from Word Scrambling.

**What it is claimed to measure.** Papers most commonly use PAWS to measure paraphrase detection, and it is linked to 1 behavioral indicator, Paraphrase detection. Beyond that dominant use, it is linked to 1 construct, Out-of-distribution generalization: a smaller line of work uses PAWS as an OOD evaluation dataset for paraphrase identification and reports it as suitable for evaluating OOD robustness.

**Space of uses.** No other measurement instrument is linked to it. Papers position PAWS as one task within broader evaluation suites, including dataset compositions for paraphrase detection, multi-task finetuning across diverse tasks, OOD evaluation for paraphrase identification, and downstream evaluation in model-merging work; one study reports gains of +3.17% and +12.38% on PAWS.

## Sources

**PAWS** (3 papers: [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf), [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf))
> Paraphrase detection benchmark that evaluates whether two sentences are semantically equivalent, used to assess model performance in distinguishing paraphrases from non-paraphrases.

## Relationships

### → PAWS
- **Paraphrase detection** (behavioral indicator): *measured_by*, 5 papers
  > PAWS ... Paraphrase Identification (Table 1: Dataset Statistics.)
  - [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > We used OOD evaluation datasets for NLI and paraphrase identification... for paraphrase identification, we used PAWS (Zhang et al., 1919)... making them suitable benchmarks for evaluating the OOD robustness of ICL. (Section 4.1)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
