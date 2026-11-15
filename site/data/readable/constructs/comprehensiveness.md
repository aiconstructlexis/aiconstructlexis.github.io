# Comprehensiveness
**Type:** Construct  
**Supporting papers:** 15  
**Also known as:** Answer comprehensiveness  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage describes comprehensiveness as whether an output covers enough information to fully answer a query or instruction, or to support a downstream task. Definitions agree on the idea of complete coverage, but they differ in what the output is expected to cover: some focus on all aspects or facets of the answer, while others require all source documents' perspectives, all relevant video details, a broad range of legal cases and situational variations, or all relevant aspects of a user's situation. A smaller line of work labels the same general idea answer comprehensiveness, defined as addressing the full set of important facets in an open-ended question.

**Space of facets.** When papers make the construct more specific, they do so by naming units of coverage: aspects or facets of a query, source documents and their perspectives, fine-grained actions and details, or sub-questions. One paper breaks answer comprehensiveness into coverage of core, background, and follow-up sub-questions. Another treats comprehensiveness as similar to completeness and even recall-like, as the fraction of gold reference items covered by candidate review sentences, and discusses it alongside relevance and a balance with conciseness.

**Space of measurement.** Papers link comprehensiveness to 2 measurement instruments and no behavioral indicators. The linked instruments are Human evaluation, implemented as judges rating outputs on a 1-5 Likert scale for comprehensiveness, and LLM-as-a-judge, where comprehensiveness appears as one of several multi-perspective criteria. Other papers make the measurement target explicit as sub-question coverage, measuring how well a system addresses different facets of a question, or as recall-like coverage of a gold set. These operationalizations keep the focus on coverage of needed information.

**Links.** Across papers, comprehensiveness is related to Faithfulness in one formulation: faithfulness is assessed with the complementary criteria of comprehensiveness and sufficiency. No paper reports a causal relationship or a correlation involving comprehensiveness.

## Sources

**Comprehensiveness** (8 papers: [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/be3b0d51a2b86cb4ffe50f13480217e0-Paper-Conference.pdf), [RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation](https://proceedings.iclr.cc/paper_files/paper/2024/file/bda88ed2892f5e61c9a9bf215c566913-Paper-Conference.pdf), [Artemis: Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf), [MoDS: Moderating a Mixture of Document Speakers to Summarize Debatable Queries in Document Collections](https://aclanthology.org/2025.naacl-long.20.pdf), [CRScore: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells](https://aclanthology.org/2025.naacl-long.457.pdf), [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf), [Automating Legal Interpretation with LLMs: Retrieval, Generation, and Evaluation](https://aclanthology.org/2025.acl-long.204.pdf), [DeepWell-Adol: A Scalable Expert-Based Dialogue Corpus for Adolescent Positive Mental Health and Wellbeing Promotion](https://aclanthology.org/2025.emnlp-main.646.pdf))
> The extent to which a summary contains enough information to answer the query or support the downstream task, regardless of whether every detail is directly copied from the source documents.

**Answer comprehensiveness** (1 paper: [Do RAG Systems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage](https://aclanthology.org/2025.naacl-long.301.pdf))
> The extent to which a response addresses the full set of important facets needed for a complete answer to an open-ended question.

## Relationships

### Comprehensiveness →
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > Using a 1-5 Likert scale, the judges are asked to rate the model output based on five criteria: comprehensiveness, layness, meaning preservation, conciseness, and fluency. (Section 5.3.3).
  - [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > The evaluation framework uses multi-perspective criteria by LLM-as-a-judge, such as comprehensiveness, specificity, and relevance. (Section 1)
  - [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.891.pdf)

### Associated with
- **Faithfulness** (construct), 1 paper
  > To assess the faithfulness of the aforementioned methods, we adopt two complementary criteria: comprehensiveness and sufficiency (DeYoung et al., 2020). (Section 4.2)
  - [NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1769.pdf)
