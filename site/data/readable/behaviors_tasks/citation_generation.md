# Citation generation
**Type:** Behavioral indicator  
**Supporting papers:** 22  
**Also known as:** Reference generation, Block-level citation, Page-level citation, Image-referenced answering, Generation with citations, Sentence-level citation generation, Chunk-level citation generation, Attribution, Attributed text generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as generating an answer together with explicit source support for its content, usually attached to each sentence, statement, or claim. Papers commonly require references to source documents, passages, chunks, or sentences so that each claim is supported by cited material, and some definitions add that irrelevant citations should be avoided. A broader framing also counts quotes, URLs, or extracted context as the supporting output.

**Variants.** Papers study several granularities and modalities. A recurrent distinction is between fine-grained sentence or claim level citation, where each response statement is followed by a citation sequence or passage ID, and chunk-level citation, where larger text blocks such as short paragraphs are cited instead. Other variants require citing the correct source page, marking a precise block with a bounding box, or explicitly naming the referenced image in the answer. A smaller line treats the behavior as producing full academic references with metadata, parenthetical author-date citations, or numbered attributions that map generated text to input triplets.

**Space of elicitation and scores.** No measurement instrument is linked to it in these papers. Papers operationalize it directly through the required output format, for example citations after each sentence or statement, both statements and supporting evidence, or page, block, or image references in multimodal settings.

**What it is taken as evidence of.** Papers link it to two constructs, but not in a single common way. One paper claims a causal relationship from citation generation to Fidelity, reporting that responses with citation can boost fidelity, while another paper treats citation generation as related to Political bias by analyzing political leaning in generated citations.

## Sources

**Citation generation** (7 papers: [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf), [MoDS: Moderating a Mixture of Document Speakers to Summarize Debatable Queries in Document Collections](https://aclanthology.org/2025.naacl-long.20.pdf), [PA-RAG: RAG Alignment via Multi-Perspective Preference Optimization](https://aclanthology.org/2025.naacl-long.459.pdf), [CORG: Generating Answers from Complex, Interrelated Contexts](https://aclanthology.org/2025.naacl-long.428.pdf), [L-CiteEval: A Suite for Evaluating Fidelity of Long-context Models](https://aclanthology.org/2025.acl-long.263.pdf), [CiteBART: Learning to Generate Citations for Local Citation Recommendation](https://aclanthology.org/2025.emnlp-main.89.pdf), [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf))
> Producing citations, quotes, URLs, or extracted context intended to support a generated response.

**Reference generation** (1 paper: [Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](https://aclanthology.org/2025.emnlp-main.83.pdf))
> Producing a list of academic citations with full metadata (title, authors, journal, year, etc.) based on a given research topic.

**Page-level citation** (1 paper: [FinRAGBench-V: A Benchmark for Multimodal RAG with Visual Citation in the Financial Domain](https://aclanthology.org/2025.emnlp-main.211.pdf))
> The specific behavior of identifying and outputting a reference to the correct source page that contains evidence for a generated answer.

**Block-level citation** (1 paper: [FinRAGBench-V: A Benchmark for Multimodal RAG with Visual Citation in the Financial Domain](https://aclanthology.org/2025.emnlp-main.211.pdf))
> The specific behavior of identifying and outputting coordinates for a bounding box around the precise region within a source page that contains evidence for a generated answer.

**Image-referenced answering** (1 paper: [Learning Interleaved Image-Text Comprehension in Vision-Language Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b441276ce6097177f1c001b3ea643f7a-Paper-Conference.pdf))
> The observable behavior of explicitly citing a specific image from the input context within a generated answer, often using a standardized format like '[Picture n]'.

**Generation with citations** (1 paper: [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf))
> The task of generating a long-form answer to a multi-faceted question and correctly attributing each sentence to the source passages provided in the context.

**Sentence-level citation generation** (1 paper: [SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25a/chuang25a.pdf))
> Producing citations after individual response statements that reference specific sentences from the provided context.

**Chunk-level citation generation** (1 paper: [SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25a/chuang25a.pdf))
> The behavior of citing larger blocks of text, such as paragraphs, as evidence for a generated statement.

**Attribution** (1 paper: [Evaluating and Improving Graph to Text Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.513.pdf))
> Marking segments of generated text with sequential numbers that correspond to specific input triplets to indicate source grounding.

**Attributed text generation** (1 paper: [Think&Cite: Improving Attributed Text Generation with Self-Guided Tree Search and Progress Reward Modeling](https://aclanthology.org/2025.acl-long.490.pdf))
> The task of generating text that includes in-text citations to a provided corpus as supporting evidence for its statements.

## Relationships

### Citation generation →
- **Fidelity** (construct): *causes*, 1 paper
  > we can find that model response with citation can boost both the model performance and its fidelity. (Section 5.2)
  - [L-CiteEval: A Suite for Evaluating Fidelity of Long-context Models](https://aclanthology.org/2025.acl-long.263.pdf)

### Associated with
- **Political bias** (construct), 1 paper
  > this paper focuses on empirically quantifying and analyzing the political leaning of LLM in citation generation. (Section 2)
  - [Media Source Matters More Than Content: Unveiling Political Bias in LLM-Generated Citations](https://aclanthology.org/2025.emnlp-main.872.pdf)
