# Single-document question answering
**Type:** Behavioral indicator  
**Supporting papers:** 6  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this as question answering grounded in one provided document. Definitions largely agree that the answer should be based on information contained within that document, while a smaller wording difference is that some papers explicitly describe the input as a single long document and one definition says the task may require extracting or reasoning over its information.

**Variants.** Papers most often name the behavior Single-Document QA or Single-Doc QA. The recurring setting is long-context evaluation, where it appears as one task category alongside categories such as multi-document QA, summarization, dialogue understanding, few-shot learning, synthetic tasks, and code.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument, LongBench. One paper reports that it is measured by LongBench and describes LongBench as covering six main task categories, including single-document question answering.

**What it is taken as evidence of.** Across the papers, no construct is linked to this behavior, so they do not report what construct it is taken to indicate.

## Sources

**Single-document question answering** (4 papers: [L-CiteEval: A Suite for Evaluating Fidelity of Long-context Models](https://aclanthology.org/2025.acl-long.263.pdf), [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf), [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ag/xu25ag.pdf), [GATEAU: Selecting Influential Samples for Long Context Alignment](https://aclanthology.org/2025.emnlp-main.375.pdf))
> The task of answering a question based on information contained within a single provided document.

## Relationships

### Single-document question answering →
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > LongBench includes nearly 5000 test samples and covers six main task categories, such as single-document question answering (SQA)... (Section 2)
  - [MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560.pdf)
