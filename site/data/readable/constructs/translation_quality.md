# Translation quality
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Terminology accuracy  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats translation quality as an overall judgment of translated output, usually centered on fluency, adequacy, accuracy or correctness, fidelity, and preservation of source meaning, whether assessed automatically or by humans. Definitions vary on whether the construct is attached to the translated text itself or to a model's latent ability to produce such text, but both framings stay broad. A smaller line of work narrows the concept to terminology accuracy in finance, defining it through correct translation of domain-specific terms and conceptual consistency across languages.

**Space of facets.** Papers most often break the construct into recurring facets such as fluency, adequacy, correctness, understanding, fidelity, and, in multimodal work, contextual appropriateness. As one study puts it, quality can be judged by "problems related to their fluency, adequacy, and understanding" (Bayelemabaga: Creating Resources for Bambara NLP). Other papers describe it through a balance between translatability and meaning preservation, and several discuss it separately from hallucination avoidance, latency, or estimated probability, rather than using those quantities as translation quality itself.

**Space of measurement.** Operationally, papers link translation quality to 4 measurement instruments and 1 behavioral indicator. The most frequently linked instruments are FLORES, Human evaluation, MQM, and WMT: FLORES and WMT are described as benchmarks, while MQM and human evaluation rely on human annotations or judgments. Other papers operationalize quality with neural metrics, reference-based comparison to a ground-truth translation, and a combined evaluation metric balancing translatability and meaning preservation; this mostly lines up with the broad definitions, while the finance-focused framing instead measures the proportion of correctly matched domain terms.

**Links.** Beyond measurement, one paper claims a causal relationship from text simplification to translation quality, stating that simplification "most reliably improves translation quality" (Automatic Input Rewriting Improves Translation with Large Language Models). No papers here report correlational links or broader related-to links with other constructs.

## Sources

**Translation quality** (7 papers: [DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf), [Anticipating Future with Large Language Model for Simultaneous Machine Translation](https://aclanthology.org/2025.naacl-long.286.pdf), [Automatic Input Rewriting Improves Translation with Large Language Models](https://aclanthology.org/2025.naacl-long.542.pdf), [Bayelemabaga: Creating Resources for Bambara NLP](https://aclanthology.org/2025.naacl-long.602.pdf), [Mitigating Hallucinated Translations in Large Language Models with Hallucination-focused Preference Optimization](https://aclanthology.org/2025.naacl-long.175.pdf), [Unveiling the Power of Source: Source-based Minimum Bayes Risk Decoding for Neural Machine Translation](https://aclanthology.org/2025.acl-long.149.pdf), [SHIFT: Selected Helpful Informative Frame for Video-guided Machine Translation](https://aclanthology.org/2025.emnlp-main.161.pdf))
> The overall degree of excellence of a translated text, encompassing aspects like fluency, adequacy, and correctness, as judged by automated or human evaluation.

**Terminology accuracy** (1 paper: [The Impact of Domain-Specific Terminology on Machine Translation for Finance in European Languages](https://aclanthology.org/2025.naacl-long.140.pdf))
> The latent ability of a model to correctly translate domain-specific financial terms, reflecting its grasp of specialized vocabulary and conceptual consistency across languages.

## Relationships

### Translation quality →
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > “We also conducted machine and human evaluations of translations from studied models to compare the machine translation quality of encoder-decoder and decoder-only models.”
  - [Bayelemabaga: Creating Resources for Bambara NLP](https://aclanthology.org/2025.naacl-long.602.pdf)
- **WMT** (measurement instrument): *measured_by*, 1 paper
  > Benchmarks like WMT (Freitag et al., 2021b), MLQE-PE (Fomicheva et al., 2020), and FLORES (Team et al., 2022) have become central to evaluating translation quality. (Section 2)
  - [Evaluating Language Translation Models by Playing Telephone](https://aclanthology.org/2025.emnlp-main.524.pdf)
- **FLORES** (measurement instrument): *measured_by*, 1 paper
  > Benchmarks like WMT (Freitag et al., 2021b), MLQE-PE (Fomicheva et al., 2020), and FLORES (Team et al., 2022) have become central to evaluating translation quality. (Section 2)
  - [Evaluating Language Translation Models by Playing Telephone](https://aclanthology.org/2025.emnlp-main.524.pdf)
- **MQM** (measurement instrument): *measured_by*, 1 paper
  > We compare our telephone-supervised evaluation models to existing metrics using WMT MQM human annotations. (Section 5.1)
  - [Evaluating Language Translation Models by Playing Telephone](https://aclanthology.org/2025.emnlp-main.524.pdf)

### → Translation quality
- **Text simplification** (behavioral indicator): *causes*, 1 paper
  > simplification most reliably improves translation quality. (Section 1)
  - [Automatic Input Rewriting Improves Translation with Large Language Models](https://aclanthology.org/2025.naacl-long.542.pdf)
