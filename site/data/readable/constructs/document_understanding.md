# Document understanding
**Type:** Construct  
**Supporting papers:** 24  
**Also known as:** Document comprehension, Document reasoning, Document-level understanding  

## State of the Field

**Space of definitions.** Most definitions treat document understanding as extracting, interpreting, and using information from documents, often to answer questions or support extraction, and often in multimodal settings with text, images, tables, figures, or layout. Some papers explicitly place it in retrieval settings, describing the need to use relevant information from a retrieved document and to reason over that document. A smaller line of work frames it more broadly as a latent capacity to understand document content, structure, context, and positional cues in complex or unstructured documents, while a minority narrows it to document-level understanding, meaning synthesis of information and relations across an entire document beyond isolated sentences; one paper instead defines document comprehension as the observable task of answering questions about a document image.

**Space of facets.** Across papers, the concept spans several facets: content understanding, document structure and context, layout and positional cues, multimodal elements such as text, figures, tables, and images, and, in a narrower usage, relations that span texts, paragraphs, or chapters within a document. Papers often use "document understanding" and "document comprehension" for overlapping territory, while "document-level understanding" appears as a narrower label for whole-document synthesis. One paper also presents DocVQA as an end-to-end paradigm for document understanding and says its query-response framework applies across document understanding tasks such as document classification and information extraction.

**Space of measurement.** Operationalization is benchmark-based. The construct is linked to 8 measurement instruments and no behavioral indicators; the most frequently linked are DocVQA, ChartQA, SROIE, FUNSD, and InfoVQA, plus 3 other instruments. Papers use these as document, OCR, or chart understanding benchmarks, which follows the common definitions centered on answering questions about documents and extracting or reasoning over document content, and one benchmark paper notes that direct parsed-content comparison was not undertaken because well-defined standards for direct quality assessment were absent.

**Links.** Beyond measurement, one paper claims a causal relationship from visual perception to document understanding, reporting that enhanced visual perception improves performance on document analysis tasks. One paper also reports that document understanding is related to long-context understanding by listing it among long-context tasks. No correlational links are reported.

## Sources

**Document understanding** (6 papers: [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf), [DocMIA: Document-Level Membership Inference Attacks against DocVQA Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/231a8daf4f64935d0c7c6586f290b24f-Paper-Conference.pdf), [MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval](https://aclanthology.org/2025.emnlp-main.708.pdf), [MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf), [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf), [LEO-MINI: An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts](https://aclanthology.org/2025.emnlp-main.368.pdf))
> The ability to extract and use relevant information from a retrieved document to answer a question.

**Document comprehension** (3 papers: [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf), [Enhancing Document Understanding with Group Position Embedding: A Novel Approach to Incorporate Layout Information](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d57b2c9e75aa0fd11d8ab3abde6615c-Paper-Conference.pdf), [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf))
> The latent ability to understand and interpret the content, structure, and context of complex, unstructured documents.

**Document-level understanding** (1 paper: [DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25am/xu25am.pdf))
> The capacity to synthesize information and identify relationships across an entire document, beyond the scope of individual sentences.

## Relationships

### Document understanding →
- **DocVQA** (measurement instrument): *measured_by*, 6 papers
  > In order to illustrate the impact of having long in-context text, we evaluate the model for document understanding on DocVQA [15] and OCR VQA [34]. (Section 3.1)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
  - [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf)
  - [MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/461f1fd5f92e5ca95764a88304dc39f7-Paper-Conference.pdf)
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
- **ChartQA** (measurement instrument): *measured_by*, 2 papers
  > document understanding/Optical character recognition (OCR) benchmarks: DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), AI2D (Kembhavi et al., 2016) and TextVQA (Singh et al., 2019). (Section 4.1)
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
  - [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf)
- **SROIE** (measurement instrument): *measured_by*, 2 papers
  > For document understanding, ... We utilize benchmarks such as ChartQA (Masry et al., 2022), DocVQA (Mathew et al., 2021), InfoVQA (Mathew et al., 2022), TextVQA (Singh et al., 2019), STVQA (Biten et al., 2019), FUNSD (Jaume et al., 2019), SROIE (Huang et al., 2019), POIE (Kuang et al., 2023) and OCR-Bench (Liu et al., 2023c). (Section 4.1)
  - [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf)
  - [Towards Statistical Factuality Guarantee for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.576.pdf)
- **InfoVQA** (measurement instrument): *measured_by*, 1 paper
  > For document understanding, ... We utilize benchmarks such as ChartQA (Masry et al., 2022), DocVQA (Mathew et al., 2021), InfoVQA (Mathew et al., 2022), TextVQA (Singh et al., 2019), STVQA (Biten et al., 2019), FUNSD (Jaume et al., 2019), SROIE (Huang et al., 2019), POIE (Kuang et al., 2023) and OCR-Bench (Liu et al., 2023c). (Section 4.1)
  - [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf)
- **OCR-VQA** (measurement instrument): *measured_by*, 1 paper
  > In order to illustrate the impact of having long in-context text, we evaluate the model for document understanding on DocVQA [15] and OCR VQA [34]. (Section 3.1)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > "We also observe that xRAG performs well in tasks that require document understanding, such as TriviaQA."
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
- **TextVQA** (measurement instrument): *measured_by*, 1 paper
  > For document understanding, ... We utilize benchmarks such as ChartQA (Masry et al., 2022), DocVQA (Mathew et al., 2021), InfoVQA (Mathew et al., 2022), TextVQA (Singh et al., 2019), STVQA (Biten et al., 2019), FUNSD (Jaume et al., 2019), SROIE (Huang et al., 2019), POIE (Kuang et al., 2023) and OCR-Bench (Liu et al., 2023c). (Section 4.1)
  - [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf)
- **FUNSD** (measurement instrument): *measured_by*, 1 paper
  > For document understanding, ... We utilize benchmarks such as ChartQA (Masry et al., 2022), DocVQA (Mathew et al., 2021), InfoVQA (Mathew et al., 2022), TextVQA (Singh et al., 2019), STVQA (Biten et al., 2019), FUNSD (Jaume et al., 2019), SROIE (Huang et al., 2019), POIE (Kuang et al., 2023) and OCR-Bench (Liu et al., 2023c). (Section 4.1)
  - [Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf)

### → Document understanding
- **Visual perception** (construct): *causes*, 1 paper
  > Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. (ABSTRACT)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)

### Associated with
- **Long-context understanding** (construct), 1 paper
  > Large language models (LLMs) have advanced to support long-context tasks such as document understanding (Li et al., 2024a), multi-turn dialogues (Yi et al., 2024), repository-level code completion (Jimenez et al., 2024), and complex reasoning (Zhou et al., 2025).
  - [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf)
