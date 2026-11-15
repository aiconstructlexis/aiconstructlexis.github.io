# Cross-lingual generalization
**Type:** Construct  
**Supporting papers:** 53  
**Also known as:** Cross-lingual adaptability, Cross-lingual knowledge transfer, Cross-lingual transfer, Language generalization, Crosslingual transfer, Cross-lingual linguistic capabilities, Multilingual transfer, Cross-lingual transferability, Cross-lingual generalisation, Multilingual generalization, Generalization to unseen languages  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats cross-lingual generalization as a model ability to carry knowledge, skills, or representations learned in one language into another, usually from English or another high-resource language to low-resource or unseen languages. Many definitions stress effective performance without explicit target-language training, including zero-shot transfer and generalization across unequal-resource languages, and several quoted passages describe mutual enhancements across languages or gains on unseen target languages. Definitions differ mainly on what is being generalized: some frame a latent transfer ability, some define it through aligned hidden, token, or discourse representations across languages, and a smaller set narrows it to particular behaviors such as reasoning, grammatical concept sharing, hallucination mitigation, or named entity recognition.

**Space of facets.** Across the definitions, the term sits in a family of near-synonymous labels rather than a single standardized wording. The most recurrent neighboring names are Cross-lingual transfer, Multilingual generalization, Cross-lingual knowledge transfer, Cross-lingual transferability, and Language generalization, with several other labels used for narrower variants. Within this family, some papers foreground shared multilingual spaces or aligned token, hidden, and discourse representations, while others use the same label family for specific transfers of reasoning, grammatical concepts, or other learned behaviors, and one definition contrasts such generalization with language-specific memorization.

**Space of measurement.** Papers mostly operationalize the construct behaviorally, by testing whether a model trained, tuned, or prompted in one language can perform in another language, often zero-shot and often on low-resource or unseen languages. In explicit measured_by links, it is connected to 3 instruments, C-Eval, TibetanQA, and XNLI, and quoted passages also describe English-to-target transfer setups, unseen-language zero-shot experiments, and multilingual task evaluations across several tasks. Papers link it to 7 behavioral indicators, including Definition generation and Instruction following, plus 5 others. This mostly matches the dominant transfer-based definitions, although papers that define it through shared or aligned representations still often assess it through downstream cross-language performance.

**Links.** Papers link cross-lingual generalization to 6 constructs and 7 behavioral indicators. One paper reports that it correlates with Linguistic similarity, while others claim causal relationships from Cross-lingual alignment, Language proficiency, and Knowledge retrieval to cross-lingual generalization, and one paper records a causal relationship from cross-lingual generalization to Multilingual ability. Another paper attributes its emergence to compression during pre-training, and several papers record additional causal or related links to downstream task settings in sign-language, instruction, translation, classification, and reasoning evaluations.

## Sources

**Cross-lingual generalization** (6 papers: [Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e9034dd5420660d86c8c360c35a895e-Paper-Conference.pdf), [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf), [Large Language Models Share Representations of Latent Grammatical Concepts Across Typologically Diverse Languages](https://aclanthology.org/2025.naacl-long.312.pdf), [Mitigating Hallucinated Translations in Large Language Models with Hallucination-focused Preference Optimization](https://aclanthology.org/2025.naacl-long.175.pdf), [Large Margin Representation Learning for Robust Cross-lingual Named Entity Recognition](https://aclanthology.org/2025.acl-long.215.pdf), [Judging Quality Across Languages: A Multilingual Approach to Pretraining Data Filtering with Language Models](https://aclanthology.org/2025.emnlp-main.449.pdf))
> The latent ability of a multilingual model to transfer knowledge from high-resource to low-resource languages, particularly when linguistic and data conditions differ significantly.

**Multilingual generalization** (3 papers: [Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1551c01d7a3d0bf21e2518331e9f7074-Paper-Conference.pdf), [LED-Merging: Mitigating Safety-Utility Conflicts in Model Merging with Location-Election-Disjoint](https://aclanthology.org/2025.acl-long.1055.pdf), [DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models' Understanding on Indian Culture](https://aclanthology.org/2025.emnlp-main.68.pdf))
> The model's ability to perform effectively on languages, particularly low-resource ones, without being explicitly or extensively trained on them.

**Cross-lingual adaptability** (1 paper: [From English to Second Language Mastery: Enhancing LLMs with Cross-Lingual Continued Instruction Tuning](https://aclanthology.org/2025.acl-long.1121.pdf))
> The latent ability of a model to transfer knowledge and skills from English to a target language, adjusting to language-specific patterns while retaining universal linguistic principles.

**Cross-lingual knowledge transfer** (2 papers: [TokAlign: Efficient Vocabulary Adaptation via Token Alignment](https://aclanthology.org/2025.acl-long.207.pdf), [Measuring the Effect of Disfluency in Multilingual Knowledge Probing Benchmarks](https://aclanthology.org/2025.emnlp-main.539.pdf))
> The ability of a model trained primarily on one language (e.g., English) to effectively perform tasks in other languages by leveraging aligned token representations.

**Cross-lingual transfer** (8 papers: [Second Language (Arabic) Acquisition of LLMs via Progressive Vocabulary Expansion](https://aclanthology.org/2025.acl-long.100.pdf), [Language Imbalance Driven Rewarding for Multilingual Self-improving](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cdee7247c410907b32fcbc12a605823-Paper-Conference.pdf), [Improving Cross Lingual Transfer by Pretraining with Active Forgetting](https://aclanthology.org/2025.emnlp-main.120.pdf), [IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models](https://aclanthology.org/2025.naacl-long.139.pdf), [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf), [A Survey of NLP Progress in Sino-Tibetan Low-Resource Languages](https://aclanthology.org/2025.naacl-long.396.pdf), [Soft Language Prompts for Language Transfer](https://aclanthology.org/2025.naacl-long.517.pdf), [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf))
> The capacity of a model to leverage knowledge acquired in one language (e.g., English) to enhance performance in another language (e.g., Arabic) during pre-training and inference.

**Language generalization** (1 paper: [Probing LLMs for Multilingual Discourse Generalization Through a Unified Label Set](https://aclanthology.org/2025.acl-long.915.pdf))
> The degree to which a model's discourse representations are aligned across different languages, enabling performance on multilingual tasks without language-specific adaptation.

**Crosslingual transfer** (1 paper: [On the Acquisition of Shared Grammatical Representations in Bilingual Language Models](https://aclanthology.org/2025.acl-long.1010.pdf))
> The ability of a multilingual model to apply knowledge learned from one language to improve performance or enable capabilities in another language.

**Cross-lingual linguistic capabilities** (1 paper: [QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.6.pdf))
> The ability of a multilingual model to transfer linguistic knowledge across languages, particularly in understanding and applying grammatical rules from one language to another.

**Multilingual transfer** (1 paper: [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf))
> The phenomenon where training a model on multiple languages, including high-resource ones, improves its performance on low-resource languages.

**Cross-lingual transferability** (2 papers: [Shared Path: Unraveling Memorization in Multilingual LLMs through Language Similarities](https://aclanthology.org/2025.emnlp-main.978.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf))
> The capability of a multilingual model to apply knowledge learned from one language to another, enabled by shared representations in a multilingual space.

**Cross-lingual generalisation** (1 paper: [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.577.pdf))
> The ability of a model trained or tuned in one language to effectively apply reasoning skills to other languages, especially low-resource ones, without performance degradation.

**Generalization to unseen languages** (1 paper: [LingGym: How Far Are LLMs from Thinking Like Field Linguists?](https://aclanthology.org/2025.emnlp-main.69.pdf))
> The model's ability to apply learned linguistic principles to languages and structures not encountered during its training phase.

## Relationships

### Cross-lingual generalization →
- **Multilingual ability** (construct): *causes*, 2 papers
  > Researchers have attributed this phenomenon to cross-lingual transfer in LLM training, where linguistic patterns and knowledge acquired from high-resource languages (particularly English) appear to transfer effectively to enhance performance on the other languages (Section 1).
  - [Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training](https://aclanthology.org/2025.emnlp-main.1380.pdf)
  - [Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf)
- **Linguistic similarity** (construct): *correlates*, 2 papers
  > Our results show that both pretraining size and language similarity are tied to transfer, but the former has a stronger correlation.
  - [Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf)
  - [PARME: Parallel Corpora for Low-Resourced Middle Eastern Languages](https://aclanthology.org/2025.acl-long.1451.pdf)
- **XNLI** (measurement instrument): *measured_by*, 1 paper
  > Models are then fine-tuned on the XNLI dataset, for both cross-lingual zero-shot transfer from English and target language fine-tuning.
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **Sign language translation** (behavioral indicator): *causes*, 1 paper
  > experiments in sentence-level translation and sign language identiﬁcation which demonstrate multilingual transfer beneﬁts both higher- and lower-resource sign languages. (Section 5)
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)
- **Sign language identification** (behavioral indicator): *causes*, 1 paper
  > experiments in sentence-level translation and sign language identiﬁcation which demonstrate multilingual transfer beneﬁts both higher- and lower-resource sign languages. (Section 5)
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)
- **C-Eval** (measurement instrument): *measured_by*, 1 paper
  > "SEC’s competitive performance on C-Eval shows its capability in the cross-linguistic scenario"
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
- **TibetanQA** (measurement instrument): *measured_by*, 1 paper
  > ...followed by zero-shot testing on the TibetanQA dataset (Sun et al., 2021) to assess their cross-lingual transfer capabilities (Section 4.3).
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)

### → Cross-lingual generalization
- **Semantic abstraction** (construct): *causes*, 1 paper
  > We hypothesize that cross-lingual generalization emerges through compression during pre-training. (Section 3)
  - [Cross-Lingual Generalization and Compression: From Language-Specific to Shared Neurons](https://aclanthology.org/2025.acl-long.661.pdf)
- **Cross-lingual alignment** (construct): *causes*, 1 paper
  > These metrics confirm that multi-way pretraining promotes a more coherent, language-agnostic embedding space, which drives the observed improvements in downstream performance and cross-lingual transfer. (Section 4.3)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
- **Knowledge retrieval** (behavioral indicator): *causes*, 1 paper
  > the requirement for knowledge retrieval significantly hinders the model’s cross-lingual transferability when solving reasoning tasks. (Section 4.1)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
- **Language proficiency** (construct): *causes*, 1 paper
  > "This suggests that proficiency in Arabic and Hebrew limits the cross-linguistic transfer of the knowledge-free reasoning component, while improving proficiency in the target language can alleviate this limitation."
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)

### Associated with
- **Definition generation** (behavioral indicator), 1 paper
  > In this section, we investigate whether models fine-tuned on individual languages (see Section 3) or multiple languages (see Section 4) can transfer their learned knowledge to other, unseen languages for the task of Definition Generation. (Section 5)
  - [Definition Generation for Word Meaning Modeling: Monolingual, Multilingual, and Cross-Lingual Perspectives](https://aclanthology.org/2025.emnlp-main.1321.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > We question whether instruction-following capabilities could be directly transferred to new languages without dedicated instruction data, and whether instruction-tuned models could be adapted through continued pretraining, similar to base models. (Section 1)
  - [Instructing Large Language Models for Low-Resource Languages: A Systematic Study for Basque](https://aclanthology.org/2025.emnlp-main.1484.pdf)
- **In-context reasoning** (construct), 1 paper
  > "the knowledge-free reasoning capability can be nearly perfectly transferred across various source-target language directions"
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
- **Text classification** (behavioral indicator), 1 paper
  > We conducted continued pre-training of open-source LLMs using corpora obtained through various transliteration methods, analyzed cross-lingual transfer performance across text classification, named entity recognition, machine reading comprehension, knowledge extraction, and machine translation tasks (Section 1).
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)
- **Machine translation** (behavioral indicator), 1 paper
  > We conducted continued pre-training of open-source LLMs using corpora obtained through various transliteration methods, analyzed cross-lingual transfer performance across text classification, named entity recognition, machine reading comprehension, knowledge extraction, and machine translation tasks (Section 1).
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)
