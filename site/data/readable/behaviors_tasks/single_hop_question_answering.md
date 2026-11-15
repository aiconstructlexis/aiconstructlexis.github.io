# Single-hop question answering
**Type:** Behavioral indicator  
**Supporting papers:** 5  

## State of the Field

**Space of definitions.** In the usage in the papers, this is treated as answering a question that can be resolved with a single piece of retrieved information. A quoted passage further places it among "simple single-hop tasks," using "chunk" as the candidate structure type for them.

**Variants.** Observed variants are limited to close phrasings: "single-hop QA," "simple single-hop tasks," and "single-fact questions." Across these phrasings, the scope stays on questions answerable from one fact or one retrieved piece of information.

**Space of elicitation and scores.** Papers measure it with 2 instruments, BABILong and Natural Questions. Natural Questions is explicitly labeled "Single-hop QA," while BABILong is linked to "answering single-fact questions," with one paper reporting "a modest 60% accuracy" in that setting.

## Sources

**Single-hop question answering** (1 paper: [StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf))
> Answering a question that can be resolved with a single piece of retrieved information.

## Relationships

### Single-hop question answering →
- **Natural Questions** (measurement instrument): *measured_by*, 1 paper
  > “Natural Questions (NQ; Kwiatkowski et al., 2019), Single-hop QA”
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
- **BABILong** (measurement instrument): *measured_by*, 1 paper
  > "Retrieval-Augmented Generation methods achieve a modest 60% accuracy in answering single-fact questions"
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
