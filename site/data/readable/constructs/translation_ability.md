# Translation ability
**Type:** Construct  
**Supporting papers:** 7  
**Also known as:** Translation capability, Machine translation capability, Translation performance  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats translation ability as a latent or underlying capacity of a model to translate text between languages accurately and fluently, often inferred from performance across multiple language pairs or directions. Some authors narrow this to low-resource translation, where the capacity is to produce correct target-language outputs from source-language input, and another line frames it as machine translation capability that can transfer to speech translation tasks. A smaller usage describes the same area as translation performance, emphasizing monitored changes in translation behavior rather than only the latent capacity.

**Space of facets.** Papers use several nearby labels, including translation capability, machine translation capability, translation ability, and translation performance. The first three are mostly used for an underlying model property, while translation performance is used when papers discuss detecting or monitoring changes in model behavior. The construct is also situated in different settings: diverse translation directions, multilingual models trained without parallel data, low-resource translation with grammatical explanations, and transfer from text translation to speech translation.

**Space of measurement.** Operationalization is narrow. Papers link translation ability to one measurement instrument, Super-NaturalInstructions, and the recorded use evaluates English-Spanish and English-French translations from that instrument. No behavioral indicator and no linked construct are associated with it. This measurement matches definitions that treat the construct as something inferred from translation task performance.

**Links.** In recorded relationships, translation ability is measured by Super-NaturalInstructions. Beyond that measurement link, no papers record causal, correlational, or other related links involving this construct.

## Sources

**Translation capability** (3 papers: [A Paradigm Shift in Machine Translation: Boosting Translation Performance of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b9536e186a77feff516893a5f393f7a-Paper-Conference.pdf), [The Reasonableness Behind Unreasonable Translation Capability of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/61f945d12b07c778801bd169da40762c-Paper-Conference.pdf), [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1602.pdf))
> The underlying capacity of a model to accurately and fluently translate between languages, inferred from performance across diverse translation directions.

**Machine translation capability** (1 paper: [Making LLMs Better Many-to-Many Speech-to-Text Translators with Curriculum Learning](https://aclanthology.org/2025.acl-long.610.pdf))
> The latent ability of a large language model to translate text between different languages, which can be transferred to improve performance on speech translation tasks.

**Translation ability** (1 paper: [Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf))
> The latent capacity to produce correct target-language translations from source-language input across low-resource settings.

**Translation performance** (1 paper: [An Auditing Test to Detect Behavioral Shift in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7af140f516c9f57050f7359bf53bc8f0-Paper-Conference.pdf))
> The capability of a language model to accurately and fluently translate text from a source language to a target language.

## Relationships

### Translation ability →
- **Super-NaturalInstructions** (measurement instrument): *measured_by*, 1 paper
  > We evaluate Llama3 (8B-Instruct) on English-Spanish and English-French translations from SuperNI.
  - [An Auditing Test to Detect Behavioral Shift in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7af140f516c9f57050f7359bf53bc8f0-Paper-Conference.pdf)
