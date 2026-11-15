# FLORES
**Type:** Measurement instrument  
**Supporting papers:** 11  
**Also known as:** Flores  

## State of the Field

**What it is.** Across papers, FLORES is most commonly described as a benchmark dataset for machine translation, often framed as multilingual or massively multilingual and used across many languages. Definitions describe it as evaluating text-to-text translation across over 200 languages, with one paper paraphrasing it as a set of short documents translated into 200 languages, while other papers emphasize low-resource evaluation, translation across languages and scripts, or high-quality translation between language pairs. A smaller line of work describes Flores as a dataset for bitext mining where the same sentences are shared across several language pairs, and some papers refer specifically to FLORES devtest for npi and gug.

**What it is claimed to measure.** Papers link FLORES to one behavioral indicator, Machine translation, and one construct, Translation quality, so the named measurement claims focus on these outcomes rather than a wider set. The prevailing usage is to measure machine translation: papers say they use or adopt FLORES to assess machine translation performance, including English to non-English and non-English to English settings and experiments on 100 languages. A smaller framing reports that it measures translation quality, with one paper grouping FLORES alongside WMT and MLQE-PE for that purpose.

**Space of uses.** Most papers position FLORES as a main test benchmark for translation, using it for testing, for prompt-based evaluation, or because it supports all the languages in a study. It is also used alongside other resources, especially WMT and MLQE-PE, and one paper places it beside AYA-WIKI for text generation and AYA-MLQA for question-answering in a broader generative evaluation. The only explicitly linked instrument is FLEURS-ASL, which one paper presents as an extension of FLORES/FLEURS to support American Sign Language.

## Sources

**FLORES** (4 papers: [Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf), [FLEURS-ASL: Including American Sign Language in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.314.pdf), [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf), [ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](https://aclanthology.org/2025.acl-long.239.pdf))
> A benchmark dataset for evaluating machine translation quality across many languages, particularly in low-resource settings.

**Flores** (1 paper: [MMTEB: Massive Multilingual Text Embedding Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0e3f908a2116ba529ad0a1530a3675-Paper-Conference.pdf))
> A dataset used in bitext mining tasks where sentences are shared across multiple language pairs.

## Relationships

### → FLORES
- **Machine translation** (behavioral indicator): *measured_by*, 8 papers
  > For MT of English to non-English (en-xx) and non-English to English (xx-en), we use FLORES (Goyal et al., 2022; NLLB Team et al., 2022) as it supports all the languages that we experiment with. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
  - [Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf)
  - [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf)
  - [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf)
  - [ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](https://aclanthology.org/2025.acl-long.239.pdf)
  - [Warmup Generations: A Task-Agnostic Approach for Guiding Sequence-to-Sequence Learning with Unsupervised Initial State Generation](https://aclanthology.org/2025.acl-long.434.pdf)
  - [Co-Eval: Augmenting LLM-based Evaluation with Machine Metrics](https://aclanthology.org/2025.emnlp-main.1307.pdf)
  - [SLoW: Select Low-frequency Words! Automatic Dictionary Selection for Translation on Large Language Models](https://aclanthology.org/2025.emnlp-main.46.pdf)
- **Translation quality** (construct): *measured_by*, 1 paper
  > Benchmarks like WMT (Freitag et al., 2021b), MLQE-PE (Fomicheva et al., 2020), and FLORES (Team et al., 2022) have become central to evaluating translation quality. (Section 2)
  - [Evaluating Language Translation Models by Playing Telephone](https://aclanthology.org/2025.emnlp-main.524.pdf)

### Associated with
- **FLEURS-ASL** (measurement instrument), 1 paper
  > In this paper, we introduce FLEURS-ASL, an extension of FLORES/FLEURS to support their ﬁrst sign language, American Sign Language. (Section 1)
  - [FLEURS-ASL: Including American Sign Language in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.314.pdf)
