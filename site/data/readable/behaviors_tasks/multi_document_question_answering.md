# Multi-document question answering
**Type:** Behavioral indicator  
**Supporting papers:** 19  
**Also known as:** Multi-Document Question Answering (MDQA)  

## State of the Field

**Space of definitions.** Most commonly, papers frame multi-document question answering as answering a question from a set of provided documents where only one document, the gold document, contains the answer and the remaining documents are distractors. A smaller line of work uses broader language, describing the task as retrieving, identifying, integrating, or synthesizing relevant information from multiple documents in long-context or retrieval-augmented settings. Across these formulations, success is producing an answer from the supplied context while ignoring irrelevant material, and some papers explicitly use the setup to place a single relevant document among distractors.

**Variants.** Papers use the names multi-document question answering, multi-document QA, and MDQA. The task appears in long-context settings, including extremely long contexts, with contexts of k documents, often 10 or 30, and in retrieval setups that evaluate top-5, top-10, or top-20 retrieved documents. A smaller variant is visually rich and multimodal, where the system must localize evidence across a large corpus of unstructured documents.

**Space of elicitation and scores.** Papers link this behavior to 2 measurement instruments, 2WikiMultiHopQA and LongBench. LongBench is used as a benchmark that includes multi-doc QA among its task categories, and one paper measures the behavior with 2Wiki-MultihopQA from LongBench, comprising 200 samples. Beyond instrument choice, one long-context evaluation reports performance with exact match, EM, on this task.

**What it is taken as evidence of.** The only construct linked in papers is positional bias, so construct usage is narrow. That link is framed as related rather than as a direct indicator, with one paper grouping retrieval-augmented question-answering among tasks that pose position bias. No other construct is linked.

## Sources

**Multi-document question answering** (3 papers: [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf), [Core Context Aware Transformers for Long Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cg/chen25cg.pdf), [Accelerate Parallelizable Reasoning via Parallel Decoding within One Sequence](https://aclanthology.org/2025.emnlp-main.457.pdf))
> The task of answering a question based on information contained within one of several documents provided in the context, where other documents act as distractors.

**Multi-Document Question Answering (MDQA)** (1 paper: [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf))
> An evaluation task introduced by Liu et al. (2023) to probe the "lost-in-the-middle" effect by placing a single relevant document among multiple distractor documents and asking a question about it.

## Relationships

### Multi-document question answering →
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > "These tasks belong to 6 categories in total: single-doc QA, multi-doc QA, summarization, few-shot learning, synthetic, and code."
  - [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf)
- **2WikiMultiHopQA** (measurement instrument): *measured_by*, 1 paper
  > The multi-document QA task involves "2Wiki-MultihopQA" from LongBench (Bai et al., 2023), comprising 200 samples. (Section 4.2)
  - [Accelerate Parallelizable Reasoning via Parallel Decoding within One Sequence](https://aclanthology.org/2025.emnlp-main.457.pdf)

### Associated with
- **Positional bias** (construct), 1 paper
  > We select four tasks that pose position bias: ... retrieval-augmented question-answering (Liu et al., 2024) that asks LMs to answer questions based on retrieved documents
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
