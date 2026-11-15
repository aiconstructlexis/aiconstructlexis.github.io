# FinQA
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Across the papers, FinQA is most commonly described as a financial question-answering benchmark or dataset. The most specific definition presents it as a held-out dataset where answering requires generating a Python-executable math expression from a question and financial tables, while other papers describe it more broadly as a benchmark focused on knowledge-based question answering or as a financial QA dataset that primarily assesses text generation.

**What it is claimed to measure.** Across papers, it is linked to 1 construct and no behavioral indicators, and the linked construct is Financial reasoning. The only recorded measurement claim is that papers use FinQA to measure Financial reasoning, with one paper describing FinQA and ConvFinQA as datasets developed to benchmark models for numerical reasoning tasks in the financial domain, so the reported use converges on that single construct rather than spreading across several.

**Space of uses.** Papers usually position FinQA as an evaluation resource. One paper uses it as a held-out dataset to evaluate generalization on questions and tables, another uses it with Fin-Fact to construct reranking tasks, and other discussion places it alongside FinanceBench and ConvFinQA. No measurement instrument is linked to it.

## Sources

**FinQA** (3 papers: [LLaSA: Large Language and Structured Data Assistant](https://aclanthology.org/2025.naacl-long.97.pdf), [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318.pdf), [FinMTEB: Finance Massive Text Embedding Benchmark](https://aclanthology.org/2025.emnlp-main.179.pdf))
> A held-out dataset that requires generating a Python-executable math expression to answer questions based on financial tables.

## Relationships

### → FinQA
- **Financial reasoning** (construct): *measured_by*, 1 paper
  > datasets such as FinQA (Chen et al., 2021b) and ConvFinQA (Chen et al., 2022) have been developed to benchmark deep learning models for such numerical reasoning tasks in the financial domain.
  - [Program of Thoughts for Financial Reasoning: Leveraging Dynamic In-Context Examples and Generative Retrieval](https://aclanthology.org/2025.emnlp-main.1577.pdf)
