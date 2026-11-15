# Query-focused summarization
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Query-based summarization  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is generating a summary, or in one formulation a response, over one or more documents that is tailored to a given query and emphasizes information relevant to that query. Most descriptions place the task in long-document or long-context settings, while a smaller formulation specifies a user-provided query over one or more long documents and asks for a response that cites arbitrary-length text spans from the input. Definitions also vary between framing the output as answering the query, summarizing context in response to a generated query, and producing a concise summary focused on a queried topic.

**Variants.** Papers use several nearby names, most commonly "query-focused summarization" and also "query-based summarization"; one paper further labels the long-context setting as "LCQFS" and another abbreviates the task as "QFS." The settings mentioned span one or more long documents, dialogues where "a question to summarize certain topic is raised about the dialogue," and materials such as meeting transcripts, podcast transcripts, and narratives.

**Space of elicitation and scores.** In the linked measurement work, it is measured by one instrument, QMSum. That instrument is described as a human-annotated benchmark for a query-based multi-domain meeting summarization task, consisting of query-summary pairs over meetings in multiple domains.

**What it is taken as evidence of.** The papers do not link this behavior to any construct as what it is evidence of.

## Sources

**Query-focused summarization** (3 papers: [StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf), [Unstructured Evidence Attribution for Long Context Query Focused Summarization](https://aclanthology.org/2025.emnlp-main.95.pdf), [ETHIC: Evaluating Large Language Models on Long-Context Tasks with High Information Coverage](https://aclanthology.org/2025.naacl-long.283.pdf))
> Generating a summary of one or more documents that is specifically tailored to answer a given query.

**Query-based summarization** (1 paper: [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf))
> Producing a concise summary focused on a specific query or topic from a long document, such as meeting transcripts or narratives.

## Relationships

### Query-focused summarization →
- **QMSum** (measurement instrument): *measured_by*, 1 paper
  > QMSum (Zhong et al., 2021) is a human-annotated benchmark for a query-based multi-domain meeting summarization task, which consists of 1,808 query-summary pairs over 232 meetings in multiple domains. (Section 5.1)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
