# Word sense disambiguation
**Type:** Behavioral indicator  
**Supporting papers:** 22  
**Also known as:** Sense labeling, Word-sense association, Homonym disambiguation, Pun interpretation, Polysemy disambiguation, Sense-aware task performance, Lexical disambiguation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is a Word-in-Context style binary judgment: given a word and two sentences, papers ask whether the word is used with the same sense in both, with positive cases defined as the same sense and negative cases as different senses or different homonyms. A recurring alternative treats it as selecting or assigning the correct sense of a target word in context from a predefined inventory or pool of candidate senses. Smaller formulations cast the same behavior as choosing the context-appropriate translation of an ambiguous word, resolving homonyms with context and POS cues, or associating pun words with their intended senses.

**Variants.** Papers study several named variants. The most common are Word-in-Context and polysemy disambiguation, both using paired sentences and a same-sense versus different-sense decision; Belarusian work uses the same pattern in BeWiC. Other variants include sense labeling, where models assign sense labels to polysemous words in a corpus, homonym disambiguation in Chinese with context similarity and POS conditions, word-sense association or pun interpretation for literal and figurative senses in puns, and lexical disambiguation in multi-domain translation, where success is the correct translation of a word with multiple meanings.

**Space of elicitation and scores.** Papers link this behavior to 2 measurement instruments. WiC is the prevailing instrument: papers use it as the word disambiguation or Word-in-Context benchmark, typically eliciting the binary same-sense versus different-sense judgment. SuperGLUE appears as the other linked instrument, in a smaller line of work that treats word sense disambiguation through the WiC task inside the broader benchmark.

**What it is taken as evidence of.** Only one construct link appears. Papers relate word sense disambiguation to positional bias, noting that some LLMs may rely on "superficial heuristics such as positional order" rather than evaluating definitions on semantic appropriateness in unbiased WSD tasks. No other construct link is recorded.

## Sources

**Word sense disambiguation** (6 papers: [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf), [BelarusianGLUE: Towards a Natural Language Understanding Benchmark for Belarusian](https://aclanthology.org/2025.acl-long.25.pdf), [Towards General-Domain Word Sense Disambiguation: Distilling Large Language Model into Compact Disambiguator](https://aclanthology.org/2025.emnlp-main.45.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [SANDWiCH: Semantical Analysis of Neighbours for Disambiguating Words in Context ad Hoc](https://aclanthology.org/2025.naacl-long.358.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf))
> Determining whether a target word is used with the same sense in two different sentences.

**Sense labeling** (1 paper: [Towards General-Domain Word Sense Disambiguation: Distilling Large Language Model into Compact Disambiguator](https://aclanthology.org/2025.emnlp-main.45.pdf))
> The task of assigning a specific sense label from a predefined inventory to a polysemous word within a given sentence from a corpus.

**Homonym disambiguation** (1 paper: [Context and POS in Action: A Comparative Study of Chinese Homonym Disambiguation in Human and Language Models](https://aclanthology.org/2025.emnlp-main.1404.pdf))
> The task of identifying the correct meaning of a word that has the same spelling or pronunciation as another word but a different meaning, based on its context.

**Pun interpretation** (1 paper: [Pun Unintended: LLMs and the Illusion of Humor Understanding](https://aclanthology.org/2025.emnlp-main.1419.pdf))
> The observable task of associating each word in an identified pun pair with its correct meaning or sense in the given context.

**Word-sense association** (1 paper: [Pun Unintended: LLMs and the Illusion of Humor Understanding](https://aclanthology.org/2025.emnlp-main.1419.pdf))
> Linking a word to its correct meaning in context, particularly distinguishing between literal and figurative senses in puns.

**Polysemy disambiguation** (1 paper: [Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks](https://aclanthology.org/2025.emnlp-main.1773.pdf))
> Producing a binary judgment on whether a polysemous word is used in the same sense across two different sentences.

**Lexical disambiguation** (1 paper: [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf))
> Selecting the correct translation of a word with multiple meanings based on domain context during translation.

## Relationships

### Word sense disambiguation →
- **WiC** (measurement instrument): *measured_by*, 5 papers
  > word disambiguation: WiC (Pilehvar & Camacho-Collados, 2019); (Section 5.1)
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
- **SuperGLUE** (measurement instrument): *measured_by*, 1 paper
  > The SuperGLUE benchmark comprises advanced language understanding tasks... word sense disambiguation (WiC; (Pilehvar and Camacho-Collados, 2019))... (Section 4.1)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)

### Associated with
- **Positional bias** (construct), 1 paper
  > This pattern highlights a potential limitation in some LLMs: rather than evaluating definitions purely on semantic appropriateness, they may rely on superficial heuristics such as positional order, which may compromise their reliability and generalization in unbiased WSD tasks (Section 3.2).
  - [Do Large Language Models Understand Word Senses?](https://aclanthology.org/2025.emnlp-main.1720.pdf)
