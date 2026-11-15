# Multilingual ability
**Type:** Construct  
**Supporting papers:** 72  
**Also known as:** Multilingual capability, Multilinguality, Multilingual performance, Bilingual ability, Multilingual proficiency, Multilingualism, Multilingual capabilities, Multi-lingual abilities, General multilingual utility, Multilingual competence  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage is a model-level capacity to understand and generate across multiple languages. Many papers also fold in task performance or consistency across languages, often contrasting high-resource with underrepresented or non-dominant languages, and some narrow the construct to non-English comprehension and reasoning or to performing the same task when the language changes. A smaller line of work broadens the construct to include fluency, preservation of meaning, grammatical correctness, dialect or register handling, language fidelity in vision-language settings, or cultural nuance, while a few papers use domain-bounded versions such as bilingual English-Chinese medical ability or multilingual ability in shopping, finance, legal visualization, or machine translation.

**Space of facets.** Papers break the construct into different facets rather than a single agreed schema. Some divide it into language understanding and language fidelity in vision-language settings, or into multilingual concept understanding and multilingual user behavior alignment, while others emphasize consistency across tasks, prompts, and languages. The naming is loose: multilingual ability, capability, performance, proficiency, competence, multilinguality, and multilingualism are often used for closely similar ideas, with narrower variants such as bilingual ability and general multilingual utility. Several papers also separate language ability from cultural understanding, stating that language skill and cultural understanding should be discussed separately and that multilingual capability alone does not guarantee cultural understanding.

**Space of measurement.** The construct is linked to 12 measurement instruments and 1 behavioral indicator. Operationalization is overwhelmingly benchmark-based: TyDi QA is repeatedly used for multilingual ability or capabilities, A-OKVQA is translated into other languages to test whether VQA remains invariant when the language changes, and ARC-Challenge and MGSM are also used for cross-language performance, with 8 other instruments extending this to translated, native, parallel, retrieval, and multitask evaluation; the only linked behavioral indicator is grammatical error correction. These measures mostly instantiate multilingual ability as performance on tasks across languages, which is narrower than definitions that also mention fluency, language fidelity, writing systems, dialects, or cultural nuance.

**Links.** No correlational links are recorded. Papers connect multilingual ability to five constructs: one paper explicitly claims a causal relationship from cross-lingual alignment to multilingual ability, and another explicitly claims a causal relationship from cross-lingual generalization to multilingual ability, while a separate paper links the latter pair more generally. Other work relates multilingual ability to expert specialization, language bias, and commonsense reasoning.

## Sources

**Multilingual ability** (2 papers: [Centurio: On Drivers of Multilingual Ability of Large Vision-Language Model](https://aclanthology.org/2025.acl-long.143.pdf), [Learn and Unlearn: Addressing Misinformation in Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.516.pdf))
> The latent capacity of a model to understand and generate content across multiple languages, encompassing both language understanding and language fidelity in vision-language contexts.

**Multilingual capability** (2 papers: [NusaAksara: A Multimodal and Multilingual Benchmark for Preserving Indonesian Indigenous Scripts](https://aclanthology.org/2025.acl-long.1377.pdf), [MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.79.pdf))
> The ability of a model to understand and generate text across a diverse range of languages and writing systems.

**Multilinguality** (2 papers: [Browsing Lost Unformed Recollections: A Benchmark for Tip-of-the-Tongue Search and Reasoning](https://aclanthology.org/2025.acl-long.406.pdf), [ViClaim: A Multilingual Multilabel Dataset for Automatic Claim Detection in Videos](https://aclanthology.org/2025.emnlp-main.21.pdf))
> The ability to understand and reason using textual information in languages other than English, particularly when such content is essential to resolving a query.

**Multilingual performance** (1 paper: [M-Wanda: Improving One-Shot Pruning for Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.1369.pdf))
> The latent ability of a model to maintain strong language understanding and task performance across multiple languages, particularly balancing performance between high-resource and underrepresented languages.

**Bilingual ability** (1 paper: [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf))
> The capacity to operate in both English and Chinese for medical vision-language tasks, including report generation and question answering.

**Multilingual proficiency** (1 paper: [MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf))
> The model's capability to understand and process information in multiple languages.

**Multilingualism** (1 paper: [The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models](https://aclanthology.org/2025.naacl-long.303.pdf))
> The ability to understand, generate, and reason in multiple languages while preserving meaning, cultural nuance, and grammatical correctness.

**Multilingual capabilities** (1 paper: [P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs](https://aclanthology.org/2025.emnlp-main.242.pdf))
> The ability of a model to perform effectively across a diverse range of tasks and languages beyond English.

**Multi-lingual abilities** (1 paper: [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf))
> The capability of a model to understand and perform tasks across multiple languages within the online shopping domain.

**General multilingual utility** (1 paper: [MPO: Multilingual Safety Alignment via Reward Gap Optimization](https://aclanthology.org/2025.acl-long.1149.pdf))
> The model's overall effectiveness and performance on a wide range of non-safety-related tasks across multiple languages.

**Multilingual competence** (1 paper: [Grounding Multilingual Multimodal LLMs With Cultural Knowledge](https://aclanthology.org/2025.emnlp-main.1232.pdf))
> The model's ability to understand and generate text effectively across multiple languages.

## Relationships

### Multilingual ability →
- **TyDi QA** (measurement instrument): *measured_by*, 5 papers
  > We use Big Bench Hard (BBH; Suzgun et al. (2022)) as a testbed for reasoning ability, HumanEval (Chen et al., 2021) for coding ability, and TydiQA (Clark et al., 2020) for multilingual ability.
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
  - [Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf)
  - [MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf)
- **MMMLU** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the LLMs’ capability across languages, researchers developed various multilingual benchmarks. Many rely on English translation, including XNLI (Conneau et al., 2018), MMMLU (Hendrycks et al., 2021a)... (Section 2)
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.364.pdf)
- **MGSM** (measurement instrument): *measured_by*, 1 paper
  > We found all the FLAN-MOE perform poorly on multi-lingual benchmarks including TyDiQA and MGSM. (Section 4.3).
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **A-OKVQA** (measurement instrument): *measured_by*, 1 paper
  > We augment A-OKVQA [34] by translating the questions and answers from English to either Chinese, Hindi, Spanish, or Swahili to test whether the VLMs are invariant to VQA in different languages. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **WMT16** (measurement instrument): *measured_by*, 1 paper
  > Multilinguality contains LAMBADA Multilingual [45], WMT 2014 [8], and WMT 2016 [52] (Section 4.1)
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
- **MIRACL** (measurement instrument): *measured_by*, 1 paper
  > Our main evaluations are conducted on BEIR (Thakur et al., 2021) and MIRACL (Zhang et al., 2023), to assess the generalization of dense retrievers and multilingual retrieval capability. (Section 4.5).
  - [DRAMA: Diverse Augmentation from Large Language Models to Smaller Dense Retrievers](https://aclanthology.org/2025.acl-long.1457.pdf)
- **WildChat** (measurement instrument): *measured_by*, 1 paper
  > (2) Multilingual Capability: Assessed with MultiAlpaca and WildChat datasets, covering French, Canadian French, German, and Italian, with English questions from MKQA. (Section 5.3. FPO Achieves Accurate Control Over Model Capabilities)
  - [Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf)
- **P-MMEval** (measurement instrument): *measured_by*, 1 paper
  > We develop a multilingual multi-task benchmark P-MMEVAL that includes both fundamental and capability-specialized tasks, which ensures consistent language coverage across various datasets and provides parallel samples across different languages. This benchmark facilitates a thorough assessment of multilingual capabilities and enables unprecedented fairness and consistency in evaluating cross-lingual transfer capabilities. (Section 1)
  - [P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs](https://aclanthology.org/2025.emnlp-main.242.pdf)
- **NOVA-63** (measurement instrument): *measured_by*, 1 paper
  > We propose NOVA-63, a general large-scale discipline-balanced, native multilingual benchmark with 89,107 questions in 14 languages across 63 academic disciplines, to comprehensively evaluate the multilingual capabilities of LLMs using native content. (Section 1)
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.364.pdf)
- **MHellaSwag** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the LLMs’ capability across languages, researchers developed various multilingual benchmarks. Many rely on English translation, including... MHellaswag (Dac Lai et al., 2023)... (Section 2)
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.364.pdf)
- **MMLU-ProX** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the LLMs’ capability across languages, researchers developed various multilingual benchmarks. Many rely on English translation, including... MMLU-ProX (Xuan et al., 2025)... (Section 2)
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.364.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > As shown in table 1, the resulting merged model surpasses each language-specific variant by up to 19% in accuracy on the ARC-Challenge dataset (Clark et al., 2018).
  - [MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mencattini25a/mencattini25a.pdf)

### → Multilingual ability
- **Cross-lingual generalization** (construct): *causes*, 2 papers
  > Researchers have attributed this phenomenon to cross-lingual transfer in LLM training, where linguistic patterns and knowledge acquired from high-resource languages (particularly English) appear to transfer effectively to enhance performance on the other languages (Section 1).
  - [Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training](https://aclanthology.org/2025.emnlp-main.1380.pdf)
  - [Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf)
- **Cross-lingual alignment** (construct): *causes*, 1 paper
  > We present ShifCon framework, designed to boost the performance of non-dominant languages by aligning their internal forward process with that of the dominant language.
  - [ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](https://aclanthology.org/2025.acl-long.239.pdf)

### Associated with
- **Expert specialization** (construct), 1 paper
  > The ﬁne-grained specialization of FLAN-MOE models, particularly when ﬁne-tuned on English-only instructions, can inadvertently lead to a narrowing of the model’s capacity to effectively process and generate content in multiple languages. (Section 4.3).
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **Language bias** (construct), 1 paper
  > Large language models (LLMs) have demonstrated multilingual capabilities, yet they are mostly English-centric due to the imbalanced training corpora. (Abstract)
  - [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf)
- **Grammatical error correction** (behavioral indicator), 1 paper
  > Given the need for language learning across different languages, multilingual GEC has become an important area of research. (Section 1)
  - [Explanation based In-Context Demonstrations Retrieval for Multilingual Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.251.pdf)
- **Commonsense reasoning** (construct), 1 paper
  > We measure the language model’s multilingual capabilities by evaluating its translation and common-sense reasoning performance.
  - [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1602.pdf)
