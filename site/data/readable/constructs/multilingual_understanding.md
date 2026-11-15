# Multilingual understanding
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Cross-lingual understanding, Multilingual comprehension, Multilingual perception and comprehension, Multilingual language understanding  

## State of the Field

**Space of definitions.** Most commonly, papers treat multilingual understanding as a latent ability to comprehend inputs and answer questions or perform tasks accurately across multiple languages, rather than only one dominant language. Definitions often make the scope explicitly inclusive of underrepresented, understudied, high- and low-resource, or local languages, and one study highlights a gap in understanding multilingual prompts and reports worse performance when questions are asked in local languages. A recurring alternative label, cross-lingual understanding, emphasizes transferring knowledge across languages or responding in a language different from the model's dominant training language while preserving meaning and accuracy, while some authors broaden the construct to include generation, cultural nuance, or multimodal processing.

**Space of facets.** Papers use several overlapping labels for closely related capabilities, including multilingual understanding, cross-lingual understanding, multilingual comprehension, multilingual perception and comprehension, and multilingual language understanding. The construct is specialized by setting: some papers distinguish native usage from cross-lingual scenarios and pair it with cross-cultural or regional knowledge, while others place it in multimodal, video, or table reasoning contexts. Papers do not explicitly equate it with, nest it under, or contrast it against another named construct.

**Space of measurement.** Operationalization relies on 6 measurement instruments and no linked behavioral indicators. The named instruments are C-Eval, CSRT, CVQA, Chatbot Arena, and INCLUDE, plus 1 other instrument; they are described as a broad suite of general benchmarks that covers multilingual understanding, LLM evaluation for safety and multilingual understanding, benchmarking with English and local-language questions, evaluation across user queries and tasks including multilingual understanding, and a benchmark built from regional resources. The remaining instrument evaluates sentence understanding in multiple languages by determining the relation between sentence pairs, so measurement mostly tests question answering, task performance, or sentence understanding across languages, sometimes in settings such as local languages or regional knowledge.

## Sources

**Multilingual understanding** (2 papers: [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf), [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf))
> The latent capacity to process and answer questions accurately across multiple languages, including underrepresented and understudied ones.

**Cross-lingual understanding** (3 papers: [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf), [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf), [Disentangling Language and Culture for Evaluating Multilingual Large Language Models](https://aclanthology.org/2025.acl-long.1082.pdf))
> The ability to comprehend and perform tasks involving multiple languages, particularly by transferring knowledge from one language to another.

**Multilingual comprehension** (1 paper: [A Culturally-diverse Multilingual Multimodal Video Benchmark & Model](https://aclanthology.org/2025.emnlp-main.1012.pdf))
> The latent ability of a model to understand and generate responses in multiple languages, particularly across both high- and low-resource languages, while preserving linguistic and cultural nuance.

**Multilingual perception and comprehension** (1 paper: [TVQACML: Benchmarking Text-Centric Visual Question Answering in Multilingual Chinese Minority Languages](https://aclanthology.org/2025.emnlp-main.705.pdf))
> The model's capability to process and understand information presented in multiple languages, especially in a multimodal context.

**Multilingual language understanding** (1 paper: [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf))
> The latent ability of an LLM to comprehend and answer questions accurately across multiple languages rather than only in one dominant language.

## Relationships

### Multilingual understanding →
- **CVQA** (measurement instrument): *measured_by*, 1 paper
  > “CVQA is written in both English and local languages, enabling us to benchmark multilingual MLLMs and English-only MLLMs.”
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
- **INCLUDE** (measurement instrument): *measured_by*, 1 paper
  > we design a pipeline to collect a large multilingual language understanding benchmark (i.e., INCLUDE) by collecting regional resources (e.g., educational, professional, and practical tests) that are specific to countries and originally created by native speakers of each country’s official languages. (Section 1)
  - [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf)
- **Chatbot Arena** (measurement instrument): *measured_by*, 1 paper
  > The most popular one is the Chatbot Arena (Chiang et al., 2024b), which contains over one million user queries and evaluates models in various tasks such as code, math, and multilingual understanding. (Section 5)
  - [Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf)
- **CSRT** (measurement instrument): *measured_by*, 1 paper
  > The CSRT enables LLM evaluation in terms of both safety and multilingual understanding. (Figure 1)
  - [Code-Switching Red-Teaming: LLM Evaluation for Safety and Multilingual Understanding](https://aclanthology.org/2025.acl-long.657.pdf)
- **C-Eval** (measurement instrument): *measured_by*, 1 paper
  > a broad suite of general benchmarks—...CEval...—that cover ... multilingual understanding. (Section 4.1)
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf)
- **XNLI** (measurement instrument): *measured_by*, 1 paper
  > We use the widely adopted XNLI dataset (Conneau et al., 2018) for evaluation, which assesses sentence understanding in multiple languages by determining the relationship between sentence pairs. (Section 3.3)
  - [From Neurons to Semantics: Evaluating Cross-Linguistic Alignment Capabilities of Large Language Models via Neurons Alignment](https://aclanthology.org/2025.acl-long.1406.pdf)
