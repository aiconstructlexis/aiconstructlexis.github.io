# ASQA
**Type:** Measurement instrument  
**Supporting papers:** 23  

## State of the Field

**What it is.** Most papers describe ASQA as a benchmark or dataset for long-form question answering over ambiguous, often factoid, queries, where systems are evaluated on answers that cover multiple valid or plausible interpretations. Some definitions emphasize attributable factoid and long-form QA tasks, while a smaller one frames it around long-form, multi-hop answers with supporting evidence and citation quality; papers also describe it as collected from, or extending, AmbigQA.

**What it is claimed to measure.** Papers tie ASQA to several targets rather than only one. It is used to measure 3 constructs, Factuality, Trustworthiness, and Unanswerability detection ability, and 2 behavioral indicators, Ambiguous question answering and Long-form question answering; the reported operationalizations include official ASQA metrics where Disambiguous-Rouge combines ROUGE-L and Disambig-F1 for factual correctness, as well as TRUST-SCORE and Grounded Refusals F1 on ASQA.

**Space of uses.** Papers commonly include ASQA in multi-dataset evaluations, often alongside ELI5 and QAMPARI, and sometimes with SituatedQA, to evaluate LLM outputs on long-form or ambiguous QA. Some papers evaluate on its test set, while another draws questions from its training split together with WebQuestions and Natural Questions to construct training data, and another uses it to evaluate citation generation performance.

**Concerns raised.** One paper raises a specific annotation concern, stating that ASQA extends AmbigQA by generating long-form answers to cover multiple answers, but that its annotation process leads to logical inconsistencies when linking different answer components.

## Sources

**ASQA** (6 papers: [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf), [Diversify-verify-adapt: Efficient and Robust Retrieval-Augmented Ambiguous Question Answering](https://aclanthology.org/2025.naacl-long.56.pdf), [PA-RAG: RAG Alignment via Multi-Perspective Preference Optimization](https://aclanthology.org/2025.naacl-long.459.pdf), [ALiiCE: Evaluating Positional Fine-grained Citation Generation](https://aclanthology.org/2025.naacl-long.23.pdf), [Hierarchical Document Refinement for Long-context Retrieval-augmented Generation](https://aclanthology.org/2025.acl-long.176.pdf), [CondAmbigQA: A Benchmark and Dataset for Conditional Ambiguous Question Answering](https://aclanthology.org/2025.emnlp-main.115.pdf))
> A benchmark dataset for attributable, long-form question-answering tasks used for evaluation.

## Relationships

### → ASQA
- **Trustworthiness** (construct): *measured_by*, 1 paper
  > Table 2: LLaMA family evaluated on the ASQA, QAMPARI, and ELI5 datasets. ... TRUST := TRUST-SCORE (Table 2)
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **Unanswerability detection ability** (construct): *measured_by*, 1 paper
  > Table 2: LLaMA family evaluated on the ASQA, QAMPARI, and ELI5 datasets. ... F1GR := Grounded Refusals F1 (Table 2)
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **Ambiguous question answering** (behavioral indicator): *measured_by*, 1 paper
  > We utilize the most recent ambiguous QA dataset, ASQA (Stelmakh et al., 2022). (Section 2)
  - [Diversify-verify-adapt: Efficient and Robust Retrieval-Augmented Ambiguous Question Answering](https://aclanthology.org/2025.naacl-long.56.pdf)
- **Long-form question answering** (behavioral indicator): *measured_by*, 1 paper
  > “To the best of our knowledge, ASQA (Stelmakh et al., 2022) is the only dataset that falls into this category. ASQA is a long-form QA dataset derived from a subset of ambiguous questions in the AmbigNQ dataset (Min et al., 2020). Its statistics and corresponding URL are provided in Table 4. The dataset is designed to evaluate how well systems can generate comprehensive answers that cover all valid interpretations.”
  - [Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey](https://aclanthology.org/2025.emnlp-main.482.pdf)
- **Factuality** (construct): *measured_by*, 1 paper
  > In this paper, to evaluate the quantitative performance of methods on ASQA, we follow the official metrics and report: Disambiguous-Rouge (DR) as the overall score, which combines ROUGE-L (R-L) (Lin, 2004) for text quality and Disambig-F1 (Dis-F1; QA accuracy score based on RoBERTa large (Liu et al., 2019)) for factual correctness.
  - [Efficient Real-time Refinement of Language Model Text Generation](https://aclanthology.org/2025.emnlp-main.1753.pdf)
