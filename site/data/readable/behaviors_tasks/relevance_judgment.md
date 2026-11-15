# Relevance judgment
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Document relevance assessment, Passage relevance assessment, Text relevance assessment  

## State of the Field

**Space of definitions.** Across the papers, it is treated as evaluating retrieved or given text against a query, question, task, or topic and making an explicit relevance judgment. Most formulations center on whether a document or passage is relevant or provides useful information for solving the task, while another framing emphasizes how well a piece of text aligns with a query or topic under semantic criteria. One formulation further requires the model to analyze documents one by one, produce reasoning chains, and then give a final judgement with an explanation.

**Variants.** Papers use closely related variants: document relevance assessment, passage relevance assessment, and text relevance assessment. They differ mainly in the unit being judged, retrieved documents, retrieved passages, or generic text, and in the criterion applied, relevance to a question, usefulness for solving the task, or semantic alignment to a query or topic.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, the papers describe direct elicitation through relevance decisions, such as asking for per-document analysis and a final judgement with explanation, predicting ISREL for a passage given x, d and yt, or assessing semantic alignment precision.

**What it is taken as evidence of.** No construct is linked to it, so the papers do not specify a broader construct that this behavior is taken to indicate.

## Sources

**Document relevance assessment** (1 paper: [Training Large Language Models for Retrieval-Augmented Question Answering through Backtracking Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/80790082a3b0e4fa9061730ee876f5ba-Paper-Conference.pdf))
> The observable task of evaluating one or more retrieved documents and making an explicit judgment about their relevance to a given query.

**Passage relevance assessment** (1 paper: [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf))
> Evaluating whether a retrieved passage provides useful information for solving the given task.

**Text relevance assessment** (1 paper: [GuideBench: Benchmarking Domain-Oriented Guideline Following for LLM Agents](https://aclanthology.org/2025.acl-long.557.pdf))
> The task of evaluating how well a piece of text aligns with a given query or topic based on specific semantic criteria.
