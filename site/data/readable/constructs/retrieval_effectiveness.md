# Retrieval effectiveness
**Type:** Construct  
**Supporting papers:** 8  
**Also known as:** Contextual relevance  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage stays within retrieval quality: papers describe it as the degree to which a retrieval system consistently returns relevant documents for a query, reflecting query-document alignment and contextual grounding. A closely related framing calls it contextual relevance, the latent trait of how well a retrieved chunk aligns with the broader context of a user's query and document structure, explicitly beyond surface-level semantic similarity. In one paper, the same label is used for generation instead, referring to responses that engage meaningfully with the input content and context, so the unit of analysis shifts from retrieval systems or chunks to generated responses.

**Space of facets.** The clearest breakdown treats retrieval along two dimensions, semantic similarity and contextual relevance: a Dual-Axis Retriever is described as expanding and filtering candidate chunks using both axes. Within that framing, contextual relevance is contrasted with surface similarity and tied to document structure and broader query context, while the system-level definition emphasizes relevant-document return, query-document alignment, and contextual grounding. Across these papers, nearby labels are used at different levels, covering system retrieval quality, chunk selection, and, in one case, response generation.

**Space of measurement.** Operationalization is concentrated in benchmarks: papers link retrieval effectiveness to 3 measurement instruments, BEIR, MMLongBench-Doc, and MS MARCO, and no behavioral indicators are linked to it. One paper states that retrieval effectiveness is evaluated with the retrieval benchmarks MS MARCO and BEIR, and another evaluates retrieval accuracy on MMLongBench-Doc. The linked instruments are all benchmark-based, keeping measurement at the level of retrieval performance and retrieval accuracy rather than a separate linked measure of contextual relevance.

## Sources

**Retrieval effectiveness** (1 paper: [KG-CQR: Leveraging Structured Relation Representations in Knowledge Graphs for Contextual Query Retrieval](https://aclanthology.org/2025.emnlp-main.824.pdf))
> The degree to which a retrieval system consistently returns relevant documents in response to a query, reflecting the quality of query-document alignment and contextual grounding.

**Contextual relevance** (1 paper: [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf))
> The latent trait reflecting how well a retrieved chunk aligns with the broader context of the user's query and document structure, beyond surface-level semantic similarity.

## Relationships

### Retrieval effectiveness →
- **MS MARCO** (measurement instrument): *measured_by*, 1 paper
  > We evaluate retrieval effectiveness using two retrieval benchmarks: MS MARCO (Bajaj et al., 2016) and BEIR (Thakur et al., 2021).
  - [ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance](https://aclanthology.org/2025.emnlp-main.963.pdf)
- **BEIR** (measurement instrument): *measured_by*, 1 paper
  > We evaluate retrieval effectiveness using two retrieval benchmarks: MS MARCO (Bajaj et al., 2016) and BEIR (Thakur et al., 2021).
  - [ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance](https://aclanthology.org/2025.emnlp-main.963.pdf)
- **MMLongBench-Doc** (measurement instrument): *measured_by*, 1 paper
  > “We first evaluate the retrieval accuracy of the Col-retrieval module within SV-RAG and compare it with several baselines on SlideVQA, MMLongBench-Doc, DUDE, DocVQA and VisR-Bench.”
  - [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
