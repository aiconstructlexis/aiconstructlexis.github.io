# Machine translation
**Type:** Behavioral indicator  
**Supporting papers:** 215  
**Also known as:** Translation, Classical Chinese to modern Chinese translation, Modern Chinese to classical Chinese translation, Ancient poetry translation, Ancient poetry to English translation, Zero-shot translation, Legal translation, Context-dependent translation, Document translation, Concise translation, Monotonic translation, Self-translation, Pronoun translation, Proper noun translation, Language translation, Text translation, Dictionary-based translation, Gender-neutral translation, Lyrics translation, Text-only translation, Domain-specific translation, Cross-lingual generation, Multi-domain translation, Code-switched translation, Explicit translation, Spoken-only language translation, Paragraph-level translation, Pseudo-document translation, Sentence translation, Loanword translation, Braille-to-text translation, Gendered translation, Classical Chinese poetry translation, Cross-cultural translation, Multi-hop translation, Single-hop translation, Plain-text translation, Translation generation, Chain-of-thought translation, Neural Machine Translation, In-context translation, Many-to-many multilingual translation  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is the conversion of source-language text, sentences, or sequences into a target-language output, usually framed as a language generation or seq2seq task. Success is most commonly described as preserving meaning or producing a semantically equivalent target text, and some definitions add fluency, accuracy, or natural sentence structure. Some papers elicit it with explicit prompts that name the source and target languages, and some evaluate it both as a held-in task and as a generation task.

**Variants.** Beyond the generic sentence-to-sentence setup, papers study bilingual, bi-directional, one-to-many, and many-to-many multilingual translation, including low-resource, zero-shot, in-context, and self-translation settings. Recurring granularity and subtask variants include sentence, paragraph-level, pseudo-document, and full document translation, as well as context-dependent, pronoun, proper noun, dictionary-based, gender-neutral or gendered, and monotonic or concise translation. A smaller line of work extends the label to domain or modality constrained cases, including legal or finance translation, text found in images or document images, lyrics, Braille-to-text, spoken-only language translation from IPA, classical Chinese and ancient poetry, cross-cultural translation, and synthetic single-hop or multi-hop translation.

**Space of elicitation and scores.** Papers link machine translation to 19 measurement instruments. The most frequently linked are FLORES-200, FLORES, Flores-101, WMT16, and IWSLT 2017. These are mostly benchmark datasets, and the quoted passages also show scoring with BLEU, BLEURT, RougeL, adequacy and fluency judgments, fine-grained quality annotations, and judge-based evaluation.

**What it is taken as evidence of.** Papers link machine translation to 3 constructs, and they do not converge on a single one. One paper claims a causal relationship from Cross-lingual alignment to Machine translation, describing alignment as a mechanistic explanation of improved translation performance, while other papers report Machine translation as related to Cross-lingual generalization and to Stereotyping through reported gender bias in translation systems. Across these papers, the behavior is connected to several constructs with mixed relation types rather than to one agreed construct.

## Sources

**Machine translation** (47 papers: [A Benchmark for Learning to Translate a New Language from One Grammar Book](https://proceedings.iclr.cc/paper_files/paper/2024/file/52d63f9e4b81f866bf69fb3c834aad47-Paper-Conference.pdf), [A Paradigm Shift in Machine Translation: Boosting Translation Performance of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b9536e186a77feff516893a5f393f7a-Paper-Conference.pdf), [Are Bert Family Good Instruction Followers? A Study on Their Potential And Limitations](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a13eb0c08247364066e8d86551c3090-Paper-Conference.pdf), [Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf), [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf), [Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce806d8b4bf38cd92d483e5a0490d983-Paper-Conference.pdf), [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf), [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/be3b0d51a2b86cb4ffe50f13480217e0-Paper-Conference.pdf), [Stack Attention: Improving the Ability of Transformers to Model Hierarchical Patterns](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e4322fddd833f83c855660ac65e428d-Paper-Conference.pdf), [The Reasonableness Behind Unreasonable Translation Capability of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/61f945d12b07c778801bd169da40762c-Paper-Conference.pdf), [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf), [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf), [Unbiased Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c5b00c5bdcc6fe35907dbcca03d27652-Paper-Conference.pdf), [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf), [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf), [A Watermark for Order-Agnostic Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ce8e3434c7b486bbddff9745b2a1722-Paper-Conference.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.458.pdf), [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf), [Upsample or Upweight? Balanced Training on Heavily Imbalanced Datasets](https://aclanthology.org/2025.naacl-long.171.pdf), [Matina: A Large-Scale 73B Token Persian Text Corpus](https://aclanthology.org/2025.naacl-long.462.pdf), [RAP: A Metric for Balancing Repetition and Performance in Open-Source Large Language Models](https://aclanthology.org/2025.naacl-long.69.pdf), [The Impact of Domain-Specific Terminology on Machine Translation for Finance in European Languages](https://aclanthology.org/2025.naacl-long.140.pdf), [Bayelemabaga: Creating Resources for Bambara NLP](https://aclanthology.org/2025.naacl-long.602.pdf), [PromptRefine: Enhancing Few-Shot Performance on Low-Resource Indic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.17.pdf), [Large Language Models Share Representations of Latent Grammatical Concepts Across Typologically Diverse Languages](https://aclanthology.org/2025.naacl-long.312.pdf), [BiMark: Unbiased Multilayer Watermarking for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25u/feng25u.pdf), [SLoW: Select Low-frequency Words! Automatic Dictionary Selection for Translation on Large Language Models](https://aclanthology.org/2025.emnlp-main.46.pdf), [Batayan: A Filipino NLP benchmark for evaluating Large Language Models](https://aclanthology.org/2025.acl-long.1509.pdf), [Beyond Text Compression: Evaluating Tokenizers Across Scales](https://aclanthology.org/2025.acl-long.1546.pdf), [Byte Latent Transformer: Patches Scale Better Than Tokens](https://aclanthology.org/2025.acl-long.453.pdf), [ConsistencyChecker: Tree-based Evaluation of LLM Generalization Capabilities](https://aclanthology.org/2025.acl-long.1585.pdf), [D.Va: Validate Your Demonstration First Before You Use It](https://aclanthology.org/2025.acl-long.129.pdf), [DialUp! Modeling the Language Continuum by Adapting Models to Dialects and Dialects to Models](https://aclanthology.org/2025.acl-long.989.pdf), [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf), [GrammaMT: Improving Machine Translation with Grammar-Informed In-Context Learning](https://aclanthology.org/2025.acl-long.1447.pdf), [Improved Unbiased Watermark for Large Language Models](https://aclanthology.org/2025.acl-long.1005.pdf), [Is linguistically-motivated data augmentation worth it?](https://aclanthology.org/2025.acl-long.1307.pdf), [Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs](https://aclanthology.org/2025.acl-long.778.pdf), [MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.240.pdf), [Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages](https://aclanthology.org/2025.acl-long.893.pdf), [ONEBench to Test Them All: Sample-Level Benchmarking Over Open-Ended Capabilities](https://aclanthology.org/2025.acl-long.1560.pdf), [Plug-in and Fine-tuning: Bridging the Gap between Small Language Models and Large Language Models](https://aclanthology.org/2025.acl-long.271.pdf), [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf), [ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](https://aclanthology.org/2025.acl-long.239.pdf), [Warmup Generations: A Task-Agnostic Approach for Guiding Sequence-to-Sequence Learning with Unsupervised Initial State Generation](https://aclanthology.org/2025.acl-long.434.pdf), [Where Are We? Evaluating LLM Performance on African Languages](https://aclanthology.org/2025.acl-long.1572.pdf))
> Translating text from one language to another, evaluated as both a held-in and generation task.

**Translation** (8 papers: [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf), [Leveraging Submodule Linearity Enhances Task Arithmetic Performance in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c983bf84ddbf8c71b2fd19a9d48186b-Paper-Conference.pdf), [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf), [A-TASC: Asian TED-Based Automatic Subtitling Corpus](https://aclanthology.org/2025.acl-long.157.pdf), [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1602.pdf), [LLMs can be easily Confused by Instructional Distractions](https://aclanthology.org/2025.acl-long.957.pdf), [On Many-Shot In-Context Learning for Long-Context Evaluation](https://aclanthology.org/2025.acl-long.1245.pdf), [The Invisible Hand: Unveiling Provider Bias in Large Language Models for Code Generation](https://aclanthology.org/2025.acl-long.1038.pdf))
> The task of converting text from a source language to a target language.

**Classical Chinese to modern Chinese translation** (1 paper: [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of translating a given text from classical Chinese into modern Chinese.

**Modern Chinese to classical Chinese translation** (1 paper: [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of translating a given text from modern Chinese into classical Chinese.

**Ancient poetry translation** (1 paper: [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of translating ancient poetry into modern Chinese while preserving its meaning and sentiment.

**Ancient poetry to English translation** (1 paper: [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of translating ancient Chinese poetry into English.

**Zero-shot translation** (1 paper: [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf))
> Translating text from a source language to a target language without any explicit training examples for that language pair.

**Legal translation** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> Translating legal texts between Chinese and English.

**Context-dependent translation** (1 paper: [DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf))
> The task of translating ambiguous words or phrases that require surrounding text or discourse context for correct interpretation.

**Document translation** (2 papers: [DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf), [FilBench: Can LLMs Understand and Generate Filipino?](https://aclanthology.org/2025.emnlp-main.127.pdf))
> Generating a target language version of a source document, often sentence-by-sentence.

**Self-translation** (1 paper: [Language Imbalance Driven Rewarding for Multilingual Self-improving](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cdee7247c410907b32fcbc12a605823-Paper-Conference.pdf))
> The task of a model translating its own generated responses from one language to another.

**Monotonic translation** (1 paper: [SimulPL: Aligning Human Preferences in Simultaneous Machine Translation](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5111676c19e5945473acf20ad7026f-Paper-Conference.pdf))
> The behavior of generating a translation where the target word order largely follows the source word order, minimizing reordering.

**Concise translation** (1 paper: [SimulPL: Aligning Human Preferences in Simultaneous Machine Translation](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5111676c19e5945473acf20ad7026f-Paper-Conference.pdf))
> The behavior of producing translations that are shorter than a literal rendering and focus on essential information points.

**Pronoun translation** (1 paper: [DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf))
> The observable task of correctly translating pronouns, which often requires resolving coreferences using document-level context.

**Proper noun translation** (1 paper: [DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/285149554f6fbed6e2f9ec72d131bd23-Paper-Conference.pdf))
> The specific sub-task of translating named entities such as people, locations, and organizations from a source to a target language.

**Language translation** (2 papers: [On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf), [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf))
> Translating text from one language to another, specifically English to French in the paper's experiment.

**Text translation** (2 papers: [Can We Predict Performance of Large Models across Vision-Language Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25y/zhao25y.pdf), [FB-Bench: A Fine-Grained Multi-Task Benchmark for Evaluating LLMs' Responsiveness to Human Feedback](https://aclanthology.org/2025.emnlp-main.471.pdf))
> The task of translating text found within an image from one language to another.

**Dictionary-based translation** (1 paper: [SLoW: Select Low-frequency Words! Automatic Dictionary Selection for Translation on Large Language Models](https://aclanthology.org/2025.emnlp-main.46.pdf))
> Producing translated text by incorporating external bilingual dictionaries into the prompt to guide word-level mappings during generation.

**Lyrics translation** (1 paper: [MAVL: A Multilingual Audio-Video Lyrics Dataset for Animated Song Translation](https://aclanthology.org/2025.emnlp-main.689.pdf))
> Producing translated lyric text from source lyrics, often under constraints of meaning, rhythm, and singability.

**Gender-neutral translation** (1 paper: [Mind the Inclusivity Gap: Multilingual Gender-Neutral Translation Evaluation with mGeNTE](https://aclanthology.org/2025.emnlp-main.692.pdf))
> The task of translating text into a target language using unmarked forms that do not specify gender, especially when the source text is ambiguous or refers to unspecified individuals.

**Text-only translation** (1 paper: [SHIFT: Selected Helpful Informative Frame for Video-guided Machine Translation](https://aclanthology.org/2025.emnlp-main.161.pdf))
> Producing a translated output using only the source text as input, without any visual context.

**Domain-specific translation** (1 paper: [FilBench: Can LLMs Understand and Generate Filipino?](https://aclanthology.org/2025.emnlp-main.127.pdf))
> Translating text from a specialized domain into another language.

**Cross-lingual generation** (1 paper: [AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment](https://aclanthology.org/2025.emnlp-main.328.pdf))
> Producing text in a target language based on input in a different source language, such as translating from Arabic to English or vice versa.

**Multi-domain translation** (1 paper: [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf))
> Translating text between languages while correctly handling words whose meanings vary across different domains such as law, science, or news.

**Code-switched translation** (1 paper: [MultiMed-ST: Large-scale Many-to-many Multilingual Medical Speech Translation](https://aclanthology.org/2025.emnlp-main.599.pdf))
> The observable behavior of translating sentences where terms from a foreign language (e.g., English) are retained within the source text of another language.

**Explicit translation** (1 paper: [Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline](https://aclanthology.org/2025.emnlp-main.762.pdf))
> Translating an English word or answer into a specified target language when directly prompted to do so.

**Spoken-only language translation** (1 paper: [Can Large Language Models Translate Spoken-Only Languages through International Phonetic Transcription?](https://aclanthology.org/2025.emnlp-main.1195.pdf))
> The observable task of generating a translation in a written high-resource language from an input sentence that is represented using the International Phonetic Alphabet (IPA) from a spoken-only language.

**Paragraph-level translation** (1 paper: [BOUQuET : dataset, Benchmark and Open initiative for Universal Quality Evaluation in Translation](https://aclanthology.org/2025.emnlp-main.1400.pdf))
> Translating entire paragraphs of text, which requires maintaining context and coherence beyond individual sentences.

**Pseudo-document translation** (1 paper: [AFRIDOC-MT: Document-level MT Corpus for African Languages](https://aclanthology.org/2025.emnlp-main.1413.pdf))
> An observable task where a long document is split into fixed-size chunks of sentences, which are then translated as single units.

**Sentence translation** (2 papers: [AFRIDOC-MT: Document-level MT Corpus for African Languages](https://aclanthology.org/2025.emnlp-main.1413.pdf), [TEACH: A Contrastive Knowledge Adaptive Distillation Framework for Classical Chinese Understanding](https://aclanthology.org/2025.acl-long.178.pdf))
> Translating individual sentences in isolation, without leveraging or preserving inter-sentential context.

**Loanword translation** (1 paper: [Leveraging Loanword Constraints for Improving Machine Translation in a Low-Resource Multilingual Context](https://aclanthology.org/2025.emnlp-main.1406.pdf))
> The observable act of translating a loanword from the source language into its correct target-language equivalent, respecting orthographic and phonological norms.

**Braille-to-text translation** (1 paper: [BrailleLLM: Braille Instruction Tuning with Large Language Models for Braille Domain Tasks](https://aclanthology.org/2025.emnlp-main.1454.pdf))
> The observable task of converting a sequence of Braille symbols into its corresponding plain text representation.

**Gendered translation** (1 paper: [Assumed Identities: Quantifying Gender Bias in Machine Translation of Gender-Ambiguous Occupational Terms](https://aclanthology.org/2025.emnlp-main.1640.pdf))
> The observable act of assigning a masculine or feminine grammatical form to an occupation in translation when the source term is gender-ambiguous.

**Classical Chinese poetry translation** (1 paper: [Benchmarking LLMs for Translating Classical Chinese Poetry: Evaluating Adequacy, Fluency, and Elegance](https://aclanthology.org/2025.emnlp-main.1678.pdf))
> Producing English translations of classical Chinese poems while preserving meaning, rhyme, structure, and aesthetic qualities.

**Cross-cultural translation** (1 paper: [DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context](https://aclanthology.org/2025.emnlp-main.1706.pdf))
> The task of translating text from a source language to a target language while also adapting culture-specific entities to ensure relevance and comprehension for the target audience.

**Multi-hop translation** (1 paper: [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf))
> Given a source text and intermediate bilingual dictionaries, the model translates across multiple synthetic languages.

**Single-hop translation** (1 paper: [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf))
> Given a source text in one synthetic language, the model translates it into another language using a direct bilingual dictionary.

**Plain-text translation** (1 paper: [Single-to-mix Modality Alignment with Multimodal Large Language Model for Document Image Machine Translation](https://aclanthology.org/2025.acl-long.606.pdf))
> Translating the textual content of a document image after removing non-textual elements like formulas and tables, focusing on linguistic accuracy.

**Translation generation** (1 paper: [Enhancing Machine Translation with Self-Supervised Preference Data](https://aclanthology.org/2025.acl-long.1165.pdf))
> The observable task of producing a target language text given a source language text as input.

**Chain-of-thought translation** (1 paper: [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf))
> Producing a translation by first reasoning through the input in steps, such as reading the sentence and then translating it.

**Neural Machine Translation** (1 paper: [MBR and QE Finetuning: Training-time Distillation of the Best and Most Expensive Decoding Methods](https://proceedings.iclr.cc/paper_files/paper/2024/file/ae817e85f71ef86d5c9566598e185b89-Paper-Conference.pdf))
> The task of automatically translating text from a source language to a target language using a neural network model.

**In-context translation** (1 paper: [Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study](https://aclanthology.org/2025.naacl-long.280.pdf))
> The observable behavior of generating a translation for a source sentence when provided with a few example translation pairs in the context.

**Many-to-many multilingual translation** (1 paper: [Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study](https://aclanthology.org/2025.naacl-long.280.pdf))
> Translating between any pair of 28 supported languages in both directions, including non-English and non-Chinese pivot translations.

## Relationships

### Machine translation →
- **FLORES-200** (measurement instrument): *measured_by*, 11 papers
  > Translating text from a non-English language to English: We carry out these evaluations in a 5-shot in-context learning paradigm on the FLORES-200 (Costa-juss`a et al., 2022) dataset. (Section 4.2)
  - [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf)
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf)
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
  - [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf)
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)
  - [DialUp! Modeling the Language Continuum by Adapting Models to Dialects and Dialects to Models](https://aclanthology.org/2025.acl-long.989.pdf)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
  - [Tuning Less, Prompting More: In-Context Preference Learning Pipeline for Natural Language Transformation](https://aclanthology.org/2025.emnlp-main.737.pdf)
  - [It's All About In-Context Learning! Teaching Extremely Low-Resource Languages to LLMs](https://aclanthology.org/2025.emnlp-main.1502.pdf)
  - [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **FLORES** (measurement instrument): *measured_by*, 8 papers
  > For MT of English to non-English (en-xx) and non-English to English (xx-en), we use FLORES (Goyal et al., 2022; NLLB Team et al., 2022) as it supports all the languages that we experiment with. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
  - [Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf)
  - [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf)
  - [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf)
  - [ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](https://aclanthology.org/2025.acl-long.239.pdf)
  - [Warmup Generations: A Task-Agnostic Approach for Guiding Sequence-to-Sequence Learning with Unsupervised Initial State Generation](https://aclanthology.org/2025.acl-long.434.pdf)
  - [Co-Eval: Augmenting LLM-based Evaluation with Machine Metrics](https://aclanthology.org/2025.emnlp-main.1307.pdf)
  - [SLoW: Select Low-frequency Words! Automatic Dictionary Selection for Translation on Large Language Models](https://aclanthology.org/2025.emnlp-main.46.pdf)
- **Flores-101** (measurement instrument): *measured_by*, 5 papers
  > In Table 10, we used the translation dataset Flores-101 [Fan et al., 2021] as the evaluation set (Section A.5)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
  - [KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.458.pdf)
  - [Byte Latent Transformer: Patches Scale Better Than Tokens](https://aclanthology.org/2025.acl-long.453.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
- **WMT16** (measurement instrument): *measured_by*, 5 papers
  > and also the Romanian–English and German–English pairs from the WMT16 workshop (Bojar et al., 2016). (Section 4.3)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
  - [Improving Language Model Distillation through Hidden State Matching](https://proceedings.iclr.cc/paper_files/paper/2025/file/2fb462e23667ad5e6471a4e9af8e4774-Paper-Conference.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.240.pdf)
- **IWSLT 2017** (measurement instrument): *measured_by*, 4 papers
  > This section provides an analysis of the correlation between text evaluation and established metrics using two datasets: the CNN/Daily Mail dataset (Nallapati et al., 2016) for text summarization and the IWSLT 2017 dataset (Cettolo et al., 2017) for text translation. (Section 4.2)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
  - [Improving Language Model Distillation through Hidden State Matching](https://proceedings.iclr.cc/paper_files/paper/2025/file/2fb462e23667ad5e6471a4e9af8e4774-Paper-Conference.pdf)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
  - [Heads up! Large Language Models Can Perform Tasks Without Your Instruction via Selective Attention Head Masking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25l/han25l.pdf)
- **WMT14** (measurement instrument): *measured_by*, 4 papers
  > we use the French–English pair from the outdated 2014 shared task at the Workshop on Statistical Machine Translation (WMT14; Bojar et al., 2014) (Section 4.3)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
  - [Improving Language Model Distillation through Hidden State Matching](https://proceedings.iclr.cc/paper_files/paper/2025/file/2fb462e23667ad5e6471a4e9af8e4774-Paper-Conference.pdf)
  - [UNCERTAINTY-LINE: Length-Invariant Estimation of Uncertainty for Large Language Models](https://aclanthology.org/2025.emnlp-main.400.pdf)
- **WMT** (measurement instrument): *measured_by*, 3 papers
  > "WMT for machine translation"
  - [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf)
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
  - [When Life Gives You Samples: The Benefits of Scaling up Inference Compute for Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.1402.pdf)
- **WMT14 en-de** (measurement instrument): *measured_by*, 3 papers
  > Specially, we adopt WMT14 English-German (En-De) and WMT19 English-Chinese (En-Zh) (Kocmi et al., 2022) for translation. (Section 2)
  - [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf)
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
  - [On Teacher Hacking in Language Model Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tiapkin25a/tiapkin25a.pdf)
- **WMT14 De-En** (measurement instrument): *measured_by*, 2 papers
  > We selected CNN/DM, GSM8K, Alpaca (Taori et al., 2023), WMT14 DE-EN, and Nature Questions (Kwiatkowski et al., 2019) for the evaluation on summarization, reasoning, instruction following, translation, and question answering tasks, respectively. (Section 5.3)
  - [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf)
  - [polybasic Speculative Decoding Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25az/wang25az.pdf)
- **WMT19** (measurement instrument): *measured_by*, 2 papers
  > We use WMT14 (Bojar et al., 2014), IWSLT14 (Cettolo et al., 2014), afroMT (Reid et al., 2021), IWSLT17 (Cettolo et al., 2017), WMT18 (Bojar et al., 2018), and WMT19 (Barrault et al., 2019) for machine translation (Section 4.1)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
  - [UNCERTAINTY-LINE: Length-Invariant Estimation of Uncertainty for Large Language Models](https://aclanthology.org/2025.emnlp-main.400.pdf)
- **NTREX-128** (measurement instrument): *measured_by*, 2 papers
  > “Generation (GN) Document translation NTREX-128 (Federmann et al., 2022)”
  - [FilBench: Can LLMs Understand and Generate Filipino?](https://aclanthology.org/2025.emnlp-main.127.pdf)
  - [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on tasks selected from BIG-Bench Hard (BBH) [43], a collection of diverse tasks considered to be challenging to LLMs ... the tasks include numerical reasoning, commonsense problem-solving, logical deduction, linguistic manipulation, machine translation, and tabular reasoning, among others. (Section 3.1)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **WMT18** (measurement instrument): *measured_by*, 1 paper
  > We use WMT14 (Bojar et al., 2014), IWSLT14 (Cettolo et al., 2014), afroMT (Reid et al., 2021), IWSLT17 (Cettolo et al., 2017), WMT18 (Bojar et al., 2018), and WMT19 (Barrault et al., 2019) for machine translation (Section 4.1)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **XNLI** (measurement instrument): *measured_by*, 1 paper
  > Machine translation uses the XNLI (Conneau et al., 2018) parallel corpus for 15 languages... (Section 3.3)
  - [Heads up! Large Language Models Can Perform Tasks Without Your Instruction via Selective Attention Head Masking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25l/han25l.pdf)
- **MQM** (measurement instrument): *measured_by*, 1 paper
  > "we focus on the setting of machine translation, an application where substantial amounts of fine-grained information is already readily available, namely Multidimensional Quality Metrics (MQM) data"
  - [Learning from others’ mistakes: Finetuning machine translation models with span-level error annotations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25p/zhang25p.pdf)
- **LoraxBench** (measurement instrument): *measured_by*, 1 paper
  > We introduce LORAXBENCH, a benchmark that focuses on low-resource languages of Indonesia and covers 6 diverse tasks: reading comprehension, open-domain QA, language inference, causal reasoning, translation, and cultural QA. (Abstract)
  - [LORAXBENCH: A Multitask, Multilingual Benchmark Suite for 20 Indonesian Languages](https://aclanthology.org/2025.emnlp-main.881.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > Table 2 shows that large language models effectively evaluate classical Chinese poetry translation... (Section 7.1)
  - [Benchmarking LLMs for Translating Classical Chinese Poetry: Evaluating Adequacy, Fluency, and Elegance](https://aclanthology.org/2025.emnlp-main.1678.pdf)
- **WMT24++** (measurement instrument): *measured_by*, 1 paper
  > We use the WMT24++ (Deutsch et al., 2025) dataset as our test set
  - [Please Translate Again: Two Simple Experiments on Whether Human-Like Reasoning Helps Translation](https://aclanthology.org/2025.emnlp-main.1031.pdf)

### → Machine translation
- **Cross-lingual alignment** (construct): *causes*, 1 paper
  > We present cross-lingual attention alignment of the ﬁnetuned models across Mufu input as a mechanistic explanation of the improvement in translation performance.
  - [Mufu: Multilingual Fused Learning for Low-Resource Translation with LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44ae90136013a8d0e2d24f6015b6097-Paper-Conference.pdf)
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > both models approach 0% accuracy on multi-hop translations when CoT is disabled, indicating the necessity of CoT on SYNC.
  - [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf)

### Associated with
- **OPUS-100** (measurement instrument), 2 papers
  > For multilingual translation, we train a single model for eight directions en-{es,fa,fr,it,ko,ru,tr,zh} from the opus-100 corpus (Zhang et al., 2020) using 1M parallel sentences for each direction. (Section 5.1)
  - [Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf)
  - [Upsample or Upweight? Balanced Training on Heavily Imbalanced Datasets](https://aclanthology.org/2025.naacl-long.171.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > Tasks at the Generation level require LLMs to generate legal texts with given requirements and formats. We construct four tasks at this level: ...Legal Translation (5-3)... (Section C.3.5)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Stereotyping** (construct), 1 paper
  > Machine Translation systems have become indispensable tools for cross-linguistic communication, yet they frequently exhibit gender biases that reinforce societal stereotypes (Blodgett et al., 2020; Menis-Mastromichalakis et al., 2025). (Section 1)
  - [Assumed Identities: Quantifying Gender Bias in Machine Translation of Gender-Ambiguous Occupational Terms](https://aclanthology.org/2025.emnlp-main.1640.pdf)
- **Cross-lingual generalization** (construct), 1 paper
  > We conducted continued pre-training of open-source LLMs using corpora obtained through various transliteration methods, analyzed cross-lingual transfer performance across text classification, named entity recognition, machine reading comprehension, knowledge extraction, and machine translation tasks (Section 1).
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)
- **State tracking** (behavioral indicator), 1 paper
  > A more challenging task, Multi-hop Translation, further requires the model to perform a sequence of translations across multiple languages. ... the model must correctly apply consecutive bilingual dictionaries while keeping track of the translated outputs across the intermediate languages.
  - [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf)
