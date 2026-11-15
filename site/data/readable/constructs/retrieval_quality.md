# Retrieval quality
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Knowledge retrieval depth, Retrieval noise reduction  

## State of the Field

**Space of definitions.** Across the papers, retrieval quality is framed around the quality of what the retrieval stage brings back. Definitions emphasize retrieving "informative, non-redundant, and relevant" documents or facts, or retrieving information that is sufficiently detailed and complete for complex questions. A narrower framing treats it as the outcome of reducing irrelevant facts in the retrieved subgraph, so the main difference is whether authors describe a broad retrieval-quality property or foreground depth and completeness versus noise reduction.

**Space of facets.** Papers use closely related labels to foreground different aspects of the construct: "knowledge retrieval depth" focuses on detailed and complete retrieval, while "retrieval noise reduction" focuses on minimizing irrelevant facts. Some descriptions also pair retrieval quality with retrieval fidelity, document retrieval accuracy, and more precise query formulation, but no paper explicitly links it to other constructs through nesting, equivalence, or contrast.

**Space of measurement.** Operationalization is narrow in the linked literature: retrieval quality is linked to 1 measurement instrument, HotpotQA, and to no behavioral indicators. In that use, HotpotQA's evaluation script measures F1 score, precision, and recall between retrieved chunks and referenced facts. This operationalization most directly reflects the definitions that stress relevant retrieval, while the depth/completeness and noise-reduction framings are not separately linked to instruments or indicators.

**Links.** The only reported relationship is a measured_by link: retrieval quality is measured by HotpotQA, using its evaluation script to compare retrieved chunks with referenced facts through F1, precision, and recall. No papers report causal, correlational, or other related links to additional constructs or indicators.

## Sources

**Retrieval quality** (1 paper: [StepSearch: Igniting LLMs Search Ability via Step-Wise Proximal Policy Optimization](https://aclanthology.org/2025.emnlp-main.1106.pdf))
> The degree to which the model retrieves informative, non-redundant, and relevant documents during a search process, reflecting its strategic use of external knowledge sources.

**Knowledge retrieval depth** (1 paper: [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf))
> The extent to which a system can retrieve sufficiently detailed and complete information for answering complex questions.

**Retrieval noise reduction** (1 paper: [D-RAG: Differentiable Retrieval-Augmented Generation for Knowledge Graph Question Answering](https://aclanthology.org/2025.emnlp-main.1793.pdf))
> The observable outcome of a retrieval process that minimizes the number of irrelevant facts included in the retrieved subgraph.

## Relationships

### Retrieval quality →
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > “For retrieval quality, we use the evaluation script provided by HotpotQA to measure the F1 score, precision, and recall between the retrieved chunks and referenced facts.”
  - [Knowledge Graph-Guided Retrieval Augmented Generation](https://aclanthology.org/2025.naacl-long.449.pdf)
