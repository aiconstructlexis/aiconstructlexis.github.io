# MKQA
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across the papers, MKQA is most commonly described as a multilingual or cross-lingual question answering benchmark. Definitions differ in emphasis: one describes it as a multilingual open-domain benchmark derived from Natural Questions, another as an open-ended question-answering benchmark used to assess multilingual retrieval-augmented answering, and another as a cross-lingual QA dataset used as a knowledge retrieval benchmark in interpretability analysis. One study further specifies that it consists of 10k knowledge question-answer pairs aligned across 26 languages.

**What it is claimed to measure.** Papers link MKQA to 3 behavioral indicators and no constructs. The prevailing usage is to measure multilingual question answering, including multilingual open-ended QA and multilingual ODQA evaluation. Smaller lines of work use it to measure knowledge retrieval, where it is selected as a representative dataset for interpretability analysis, and information retrieval, where a paper uses it to evaluate cross-lingual retrieval performance.

**Space of uses.** In use, papers usually place MKQA alongside other QA benchmarks rather than presenting it alone. One setup uses it with MLQA and XOR-TyDi QA as tasks said to best represent multilingual open-ended question-answering, while an interpretability analysis uses it with BoolQ and AmbigQA as representative datasets of knowledge retrieval tasks. Another evaluation includes it among six benchmarks covering reasoning, understanding, and generation, and one retrieval study uses it specifically for cross-lingual retrieval performance.

## Sources

**MKQA** (3 papers: [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf), [Improving Multilingual Retrieval-Augmented Language Models through Dialectic Reasoning Argumentations](https://aclanthology.org/2025.emnlp-main.461.pdf))
> Multilingual Knowledge Questions and Answers, a cross-lingual question answering dataset used as a knowledge retrieval benchmark in interpretability analysis.

## Relationships

### → MKQA
- **Multilingual question answering** (behavioral indicator): *measured_by*, 3 papers
  > We use a simple multilingual knowledge QA task called MKQA (Longpre et al., 2021), which consists of 10k knowledge question-answer pairs aligned across 26 languages. (Section 6.2).
  - [The Transfer Neurons Hypothesis: An Underlying Mechanism for Language Latent Space Transitions in Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.1618.pdf)
  - [XLQA: A Benchmark for Locale-Aware Multilingual Open-Domain Question Answering](https://aclanthology.org/2025.emnlp-main.1466.pdf)
  - [Improving Multilingual Retrieval-Augmented Language Models through Dialectic Reasoning Argumentations](https://aclanthology.org/2025.emnlp-main.461.pdf)
- **Knowledge retrieval** (behavioral indicator): *measured_by*, 1 paper
  > We selected MKQA (Longpre et al., 2021), BoolQ (Clark et al., 2019), and AmbigQA (Min et al., 2020) as representative datasets of knowledge retrieval tasks for the interpretability analysis. (Section 5.3)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > “To evaluate cross-lingual retrieval performance, we conducted comprehensive experiments using the Multilingual Knowledge Questions & Answers (MKQA) benchmark”
  - [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf)
