# Completeness
**Type:** Construct  
**Supporting papers:** 26  
**Also known as:** Response informativeness, Information coverage, Factual completeness  

## State of the Field

**Space of definitions.** Across the surveyed work, completeness is most commonly framed as full coverage without omission: responses, summaries, retrieved sets, or decomposed representations should include all relevant items, facts, or context, sometimes "all and only" the items that satisfy the constraints. Many definitions also add sufficiency of detail, describing outputs as providing in-depth and in-breadth information or as covering all question-relevant key points. A smaller line of work treats completeness as a property of a plan or reasoning system, either that a set of sub-tasks contains all information needed for a comprehensive answer, or that a system can find a valid proof whenever one exists. Another minority framing narrows it to factual completeness, meaning that a claim and its evidence contain all critical context needed for a non-misleading interpretation.

**Space of facets.** Papers use several alternative labels for overlapping ideas: response informativeness names the completeness of an answer in RAG, information coverage refers to capturing all relevant claims and facts, and factual completeness extends the term to whether claims and evidence include all critical context. The concept is also organized by what it is attached to, including answer content, source-to-summary coverage, table decomposition, retrieval results, planning decompositions, and proof search. Several papers pair completeness with neighboring criteria rather than treating it alone, most often correctness or accuracy, while others place it beside consistency, solvability, non-redundancy, soundness, relevance, and verbosity.

**Space of measurement.** Papers link completeness to no measurement instrument, one behavioral indicator, Question answering, and no constructs. In practice, most operationalizations are direct coverage scores: one retrieval paper defines it as the fraction of ground-truth answers with an approximate match, a summarization paper uses the proportion of covered key-facts, and a text-to-table paper measures information coverage by mapping each ground-truth tuple to its most similar generated counterpart. Some papers also use direct assessments, for example a 1 to 5 Likert scale for whether decomposed tables retain the information needed to answer a query, or criteria asking whether a response covers all question-relevant key points and sufficient detail. These operationalizations largely mirror the prevailing definition as preserving or covering all relevant content without omission.

**Links.** One paper reports that completeness is related to Question answering, stating that question-answering systems can have attributes of relevance, verbosity, and completeness. No causal or correlational links are reported.

## Sources

**Completeness** (8 papers: [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf), [KITAB: Evaluating LLMs on Constraint Satisfaction for Information Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/82846e19e6d42ebfd4ace4361def29ae-Paper-Conference.pdf), [Agent-Oriented Planning in Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/31610e68fe41a62e460e044216a10766-Paper-Conference.pdf), [DETQUS: Decomposition-Enhanced Transformers for QUery-focused Summarization](https://aclanthology.org/2025.naacl-long.138.pdf), [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf), [Learning to Summarize from LLM-generated Feedback](https://aclanthology.org/2025.naacl-long.38.pdf), [LongReward: Improving Long-context Large Language Models with AI Feedback](https://aclanthology.org/2025.acl-long.187.pdf), [TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain](https://aclanthology.org/2025.emnlp-main.43.pdf))
> The extent to which the model retrieves all and only the items that satisfy the given constraints, without omitting valid solutions.

**Response informativeness** (1 paper: [PA-RAG: RAG Alignment via Multi-Perspective Preference Optimization](https://aclanthology.org/2025.naacl-long.459.pdf))
> The latent ability of a RAG generator to fully utilize valuable information from retrieved documents to produce complete and correct answers.

**Information coverage** (1 paper: [Map&Make: Schema Guided Text to Table Generation](https://aclanthology.org/2025.acl-long.1460.pdf))
> The ability of a model to capture and represent all relevant claims and facts from a source text in its generated output.

**Factual completeness** (1 paper: [The Missing Parts: Augmenting Fact Verification with Half Truth Detection](https://aclanthology.org/2025.emnlp-main.1724.pdf))
> The degree to which a claim and its supporting evidence contain all critical context necessary for a non-misleading interpretation.

## Relationships

### Associated with
- **Question answering** (behavioral indicator), 1 paper
  > question-answering systems can have attributes of relevance, verbosity, and completeness [52].
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
