# MMLongBench-Doc
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** MMLongBench  

## State of the Field

**What it is.** Across papers, the prevailing usage is as a benchmark dataset for multi-modal long-context document understanding or document question answering on long, information-rich PDFs. Papers refer to it both as MMLongBench-Doc and MMLongBench, with descriptions emphasizing extensive documents, diverse multi-modal elements, complex layouts, and questions whose answers may require integrating text, images, and charts across many pages; one definition also notes expert-annotated questions and several document categories.

**What it is claimed to measure.** Papers link it to three constructs and one behavioral indicator, so its reported measurement role is spread across several targets rather than centered on one. It is reported as measuring localization ability, multimodal document understanding, and retrieval effectiveness, and papers also use it to measure hallucination; one description says its question types evaluate long-context document understanding from complementary aspects, including localization ability and hallucination severity, while another uses it to compare retrieval accuracy.

**Space of uses.** Most papers position it as one benchmark within a broader evaluation suite rather than as a standalone instrument. It is used alongside DocBench in document understanding experiments, alongside other datasets from three benchmarks in broader evaluations, and in retrieval-focused comparisons with SlideVQA, DUDE, DocVQA, and VisR-Bench.

## Sources

**MMLongBench-Doc** (1 paper: [DocAgent: An Agentic Framework for Multi-Modal Long-Context Document Understanding](https://aclanthology.org/2025.emnlp-main.893.pdf))
> A benchmark dataset for multi-modal long-context document understanding, comprising extensive PDF documents with expert-annotated questions whose answers may require integrating text, images, and charts across many pages.

**MMLongBench** (2 papers: [MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval](https://aclanthology.org/2025.emnlp-main.708.pdf), [SimpleDoc: Multi-Modal Document Understanding with Dual-Cue Page Retrieval and Iterative Refinement](https://aclanthology.org/2025.emnlp-main.1443.pdf))
> A benchmark dataset for evaluating document question answering on lengthy, information-rich documents with diverse multi-modal elements.

## Relationships

### → MMLongBench-Doc
- **Hallucination** (behavioral indicator): *measured_by*, 1 paper
  > These three types of questions evaluate the LVLMs’s long-context DU capabilities from complementary aspects: the localization ability, the cross-page comprehension ability, and the hallucination severity, respectively. (Section 3.4)
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Localization ability** (construct): *measured_by*, 1 paper
  > “(1) 494 single-page questions (with one evidence page) mainly to evaluate localization abilities”
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal document understanding** (construct): *measured_by*, 1 paper
  > These three types of questions evaluate the LVLMs’s long-context DU capabilities from complementary aspects: the localization ability, the cross-page comprehension ability, and the hallucination severity, respectively. (Section 3.4)
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Retrieval effectiveness** (construct): *measured_by*, 1 paper
  > “We first evaluate the retrieval accuracy of the Col-retrieval module within SV-RAG and compare it with several baselines on SlideVQA, MMLongBench-Doc, DUDE, DocVQA and VisR-Bench.”
  - [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
