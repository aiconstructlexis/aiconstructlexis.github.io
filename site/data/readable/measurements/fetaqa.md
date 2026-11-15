# FeTaQA
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** FetaQA  

## State of the Field

**What it is.** Across these papers, FeTaQA is most commonly described as a table question answering benchmark or dataset with open-ended, free-form, long-form natural-language answers. Definitions repeatedly say that answering requires fetching multiple entities from a table, aggregating or reasoning over them, sometimes across multiple table sections, and producing a coherent response; one paper also describes it as an English dataset of Wikipedia tables paired with questions, answers, and supporting table cells. A smaller use treats FetaQA as table-language data adapted into training formats for table-language interleaved learning and for training column embeddings, rather than only as an evaluation benchmark.

**What it is claimed to measure.** Papers link FeTaQA to 3 behavioral indicators and 1 construct. The prevailing use is to measure Table question answering, with several papers explicitly naming it as a TableQA benchmark or dataset. Smaller lines of work also report it as measuring Data-to-text generation and Long-form question answering, and one paper uses it to measure Table reasoning, so the recorded links are concentrated on table question answering with a few additional framings.

**Space of uses.** Papers do not link it directly to other measurement instruments. In practice, they often place it alongside other tabular benchmarks, especially WikiTQ, and sometimes TabFact, WikiSQL, and HiTab, while one broader task collection includes it with FEVER and HotpotQA. Most commonly it appears as one benchmark in a multi-dataset evaluation suite or main results table, though some papers use it as an external test set and another adapts it for training table-language interleaved models and column embeddings.

**Concerns raised.** One paper notes that self-consistency is not applicable because FeTaQA is treated as an open-ended generation task. Other papers note that its long-form answers are evaluated with overlap-based metrics such as Sacre-BLEU, or with ROUGE-1, ROUGE-2, and ROUGE-L for the more complex long-form setting.

## Sources

**FeTaQA** (8 papers: [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf), [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf), [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf), [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf), [LLaSA: Large Language and Structured Data Assistant](https://aclanthology.org/2025.naacl-long.97.pdf), [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf), [CoT-based Synthesizer: Enhancing LLM Performance through Answer Synthesis](https://aclanthology.org/2025.acl-long.315.pdf), [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf))
> FeTaQA, a table question answering benchmark with long-form natural-language answers that require fetching multiple entities and reasoning over them.

**FetaQA** (1 paper: [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf))
> A table-language dataset adapted here into training formats for table-language interleaved learning.

## Relationships

### → FeTaQA
- **Table question answering** (behavioral indicator): *measured_by*, 6 papers
  > CABINET establishes new SoTA on three challenging table QA datasets (WikiTQ, FeTaQA and WikiSQL) significantly outperforming various strong baselines (§ 4.1). (Section 1)
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
  - [TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](https://aclanthology.org/2025.acl-long.1090.pdf)
  - [CoT-based Synthesizer: Enhancing LLM Performance through Answer Synthesis](https://aclanthology.org/2025.acl-long.315.pdf)
- **Table reasoning** (construct): *measured_by*, 1 paper
  > We validate CHAIN-OF-TABLE with three tabular benchmarks to evaluate table-based reasoning: WikiTQ (Pasupat & Liang, 2015), TabFact (Chen et al., 2019), and FeTaQA (Nan et al., 2022). (Section 2)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
- **Data-to-text generation** (behavioral indicator): *measured_by*, 1 paper
  > We first run experiments on four data-to-text generation datasets. ... FeTaQA (Nan et al., 2022) is an English table question answering dataset... (Section 4.1)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Long-form question answering** (behavioral indicator): *measured_by*, 1 paper
  > For more complex tasks in FeTaQA, which involve long-form question answering, we evaluate performance using ROUGE-1, ROUGE-2, and ROUGE-L metrics
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
