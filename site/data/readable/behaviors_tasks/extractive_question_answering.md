# Extractive question answering
**Type:** Behavioral indicator  
**Supporting papers:** 7  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this behavior as answering a question by extracting the answer from provided text, usually a passage, prefix, context document, or source documents. Most formulations describe the answer as a direct text span from the input, while a smaller formulation allows the answer to be extracted or composed from a prefix. One narrower description further requires the answer to be a contiguous span that can be taken from the documents without additional reasoning.

**Variants.** Papers study it in several input settings. Some descriptions center on passage or prefix-based question answering, including a setup where a decoder-only model attends to the full prefix to generate the target answer. Another line treats it as a long-context task over large documents such as research papers, financial reports, and legal documents, with questions that require information extraction from the input, and a narrower domain-specific variant uses source documents whose answers are directly extractable spans.

**Space of elicitation and scores.** Papers link this behavior to two measurement instruments: CoQA and SQuAD v1.1. One paper lists both under extractive question answering, and these are the only linked instruments for eliciting or scoring it.

**What it is taken as evidence of.** No construct is linked to this behavior, so papers do not specify through construct links what broader concept it is taken to indicate.

## Sources

**Extractive question answering** (4 papers: [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf), [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf), [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf), [OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.292.pdf))
> Producing an answer by extracting or composing it from a provided passage or prefix.

## Relationships

### Extractive question answering →
- **SQuAD v1.1** (measurement instrument): *measured_by*, 3 papers
  > (b) extractive question answering (SQuAD (Rajpurkar et al., 2016), CoQA (Reddy et al., 2019)) (Section 4.2)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
- **CoQA** (measurement instrument): *measured_by*, 1 paper
  > (b) extractive question answering (SQuAD (Rajpurkar et al., 2016), CoQA (Reddy et al., 2019)) (Section 4.2)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
