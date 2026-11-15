# Language proficiency
**Type:** Construct  
**Supporting papers:** 24  
**Also known as:** Linguistic competence, Linguistic competency, Language ability, Language competence, Linguistic proficiency, Language capability, Language-specific performance, Linguistic capability, Linguistic ability, Language skills  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats language proficiency as an underlying or latent language competence: a model's ability to understand and generate language, often with explicit reference to syntax, semantics, morphology, grammar, orthography, and vocabulary, and sometimes to higher-order or compositional understanding. A smaller line of work defines it more narrowly through acceptability judgments, grammatically correct target-language output, or target-versus-source language capacity gaps, while another broadens it to overall performance across diverse language tasks. Definitions also vary on whether the construct is a general property of the model, a language-specific capability shaped by training data coverage, or a level inferred from performance at a developmental stage.

**Space of facets.** Papers use many near-synonymous labels for this construct, including linguistic competence, linguistic competency, language competence, linguistic proficiency, language ability, language capability, linguistic capability, linguistic ability, language skills, and language-specific performance. The most common facet breakdown is structural: syntax, morphology, semantics, orthography, vocabulary, and sometimes pragmatics, with examples such as agreement, binding, island constraints, coherence, and grammatical accuracy; one paper also places synonyms and antonyms under a language capability category used to assess linguistic proficiency. Some authors tie these abilities to compositional understanding or sentence acceptability, whereas others treat them as broad skills across diverse tasks or as a capability that should be retained during multimodal or other specialized training.

**Space of measurement.** Operationalization is entirely instrument-based: papers link it to 6 measurement instruments and no behavioral indicators. The most frequently linked instruments are BLiMP, MMLU, Open LLM Leaderboard, TurBLiMP, and sBLIMP, plus 1 other instrument; these are all benchmarks or challenge metrics, with BLiMP described as a fine-grained evaluation of core linguistic competence, TurBLiMP as linguistic minimal pairs, the Open LLM Leaderboard average as an indicator of overall language proficiency, MMLU as a check on general linguistic capability, and sBLIMP paired with another ZeroSpeech metric to measure language capability objectively. These operationalizations line up with papers that emphasize grammar and formal structure, but they also widen the construct to general benchmark performance across tasks.

**Links.** Beyond measurement, papers link it to 1 construct. One paper claims a causal relationship from language proficiency to Cross-lingual generalization, stating that weaker proficiency in Arabic and Hebrew limits cross-linguistic transfer of a knowledge-free reasoning component, and that improving proficiency in the target language can alleviate that limitation. Papers do not report correlational or undirected related links for this construct.

## Sources

**Linguistic competence** (2 papers: [Geometric Signatures of Compositionality Across a Language Model's Lifetime](https://aclanthology.org/2025.acl-long.265.pdf), [SLlama: Parameter-Efficient Language Model Architecture for Enhanced Linguistic Competence Under Strict Data Constraints](https://aclanthology.org/2025.emnlp-main.1198.pdf))
> The latent ability of a language model to perform higher-order linguistic tasks requiring syntactic and semantic understanding, which emerges over training and is marked by phase transitions in behavior and representation.

**Linguistic competency** (1 paper: [QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.6.pdf))
> A model's general capability in a language, assessed by its ability to correctly distinguish acceptable sentences from unacceptable ones.

**Language competence** (1 paper: [Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations](https://aclanthology.org/2025.naacl-long.46.pdf))
> The underlying level of linguistic proficiency a model exhibits at a given developmental stage, inferred from its output quality relative to training progress.

**Linguistic proficiency** (3 papers: [ITALIC: An Italian Culture-Aware Natural Language Benchmark](https://aclanthology.org/2025.naacl-long.68.pdf), [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf), [Unveiling Encoder-Free Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5e2217482fa75556f1970be809acd3f8-Paper-Conference.pdf))
> The underlying capacity of a model to master the structural and grammatical rules of a language, including morphology, syntax, orthography, and vocabulary usage in context.

**Language proficiency** (3 papers: [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf), [A Culturally-diverse Multilingual Multimodal Video Benchmark & Model](https://aclanthology.org/2025.emnlp-main.1012.pdf), [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf))
> The model's competence in understanding and generating text in a particular language, influenced by the amount and quality of training data for that language.

**Language ability** (1 paper: [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf))
> The model's general proficiency in a given language, operationalized as the capacity gap between a target language and a source language, independent of specific tasks.

**Language capability** (2 papers: [SEA: Supervised Embedding Alignment for Token-Level Visual-Textual Integration in MLLMs](https://aclanthology.org/2025.emnlp-main.55.pdf), [Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf))
> The model's underlying proficiency in understanding and generating human language, which can be preserved or degraded during multimodal adaptation.

**Language-specific performance** (1 paper: [Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1016.pdf))
> The latent capability of a multilingual LLM to perform accurately in a particular language, reflecting differences in training data coverage and model fluency.

**Linguistic capability** (1 paper: [Ada-K Routing: Boosting the Efficiency of MoE-based LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/df22a19686a558e74f038e6277a51f68-Paper-Conference.pdf))
> The model's underlying ability to maintain language modeling performance while being optimized for routing efficiency.

**Linguistic ability** (1 paper: [Plug-in and Fine-tuning: Bridging the Gap between Small Language Models and Large Language Models](https://aclanthology.org/2025.acl-long.271.pdf))
> The latent capacity of a model to understand and produce language effectively, including syntax, semantics, and pragmatics, derived from pre-training on diverse textual data.

**Language skills** (1 paper: [Neuron Empirical Gradient: Discovering and Quantifying Neurons' Global Linear Controllability](https://aclanthology.org/2025.acl-long.1041.pdf))
> General cognitive abilities of a language model to perform diverse language understanding tasks, such as sentiment classification or factual reasoning, which are stably represented across contexts and can be probed through neuron behavior.

## Relationships

### Language proficiency →
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > To validate that the detoxified representations of PaCE are still effective on general linguistic capability... we apply PaCE to detoxify MMLU questions... to show that the detoxification will not significantly degrade the LLM's reasoning capability.
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
- **BLiMP** (measurement instrument): *measured_by*, 1 paper
  > BLiMP provides a fine-grained evaluation of core linguistic competence. (Section 2)
  - [SLlama: Parameter-Efficient Language Model Architecture for Enhanced Linguistic Competence Under Strict Data Constraints](https://aclanthology.org/2025.emnlp-main.1198.pdf)
- **Open LLM Leaderboard** (measurement instrument): *measured_by*, 1 paper
  > The average score across the 6 tasks (Average column) is commonly used as an indicator of overall language proficiency. (Table 2)
  - [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf)
- **sWUGGY** (measurement instrument): *measured_by*, 1 paper
  > We adopt the commonly-used metrics (Borsos et al., 2023; Hassid et al., 2023; Maiti et al., 2024) from the ZeroSpeech challenge (Nguyen et al., 2020): sWUGGY and sBLIMP to measure language capability objectively.
  - [A Variational Framework for Improving Naturalness in Generative Spoken Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25z/chen25z.pdf)
- **sBLIMP** (measurement instrument): *measured_by*, 1 paper
  > We adopt the commonly-used metrics (Borsos et al., 2023; Hassid et al., 2023; Maiti et al., 2024) from the ZeroSpeech challenge (Nguyen et al., 2020): sWUGGY and sBLIMP to measure language capability objectively.
  - [A Variational Framework for Improving Naturalness in Generative Spoken Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25z/chen25z.pdf)
- **TurBLiMP** (measurement instrument): *measured_by*, 1 paper
  > We introduce TurBLiMP, the first Turkish benchmark of linguistic minimal pairs, designed to evaluate the linguistic abilities of monolingual and multilingual language models (LMs). (Abstract)
  - [TurBLiMP: A Turkish Benchmark of Linguistic Minimal Pairs](https://aclanthology.org/2025.emnlp-main.834.pdf)
- **Cross-lingual generalization** (construct): *causes*, 1 paper
  > "This suggests that proficiency in Arabic and Hebrew limits the cross-linguistic transfer of the knowledge-free reasoning component, while improving proficiency in the target language can alleviate this limitation."
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
