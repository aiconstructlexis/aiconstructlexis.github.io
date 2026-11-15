# Citation quality
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Attribution groundedness  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats citation quality as how well generated citations are relevant to the response's claims and actually support them, especially in RAG settings. Several definitions phrase this as a latent ability of the model or generator to identify and reference relevant source passages, produce claims that are fully supported by cited documents, and avoid irrelevant or unsupported sources; another paper uses the nearby label attribution groundedness for whether citations are relevant and sufficiently support the attached claims. A smaller framing, in survey generation, broadens the concept to selecting academically impactful, relevant, and credible sources and to checking whether references are fabricated or hallucinated.

**Space of facets.** Papers most often break the construct into facets of citation relevance and claim support, sometimes making the negative case explicit as avoiding irrelevant documents. Some operational breakdowns add finer structure: one paper evaluates citation recall and precision at the level of atomic claims and also tracks the coefficient of variation of citation positions, so citation position regularity is included in that usage. The naming is not fully uniform: one paper uses attribution groundedness as a nearby label, and another places citation quality under honesty for RAG application while describing responses as firmly rooted in the provided documents with appropriate attribution.

**Space of measurement.** Papers link citation quality to 1 measurement instrument and no behavioral indicators. The linked instrument is TRUE, used as an NLI model for entailment judgments in citation quality evaluation. Beyond that linked instrument, measurement is usually made explicit through retrieval- and citation-based metrics: passage-level relevance judgments summarized with Recall@k and MAP@k, claim-level citation recall and precision, the coefficient of variation of citation positions, F1GC as the harmonic mean of Pcite and Rcite for citation groundedness, and citation accuracy checks for fabricated or hallucinated references. Most of these operationalizations target relevance and support, and the survey-generation usage also evaluates source credibility and fabrication.

**Links.** The only explicit non-measurement link reported is that citation quality is related to Faithfulness. In that formulation, evaluating whether a response cites relevant passages is used for measuring faithfulness.

## Sources

**Citation quality** (4 papers: [PA-RAG: RAG Alignment via Multi-Perspective Preference Optimization](https://aclanthology.org/2025.naacl-long.459.pdf), [MIRAGE-Bench: Automatic Multilingual Benchmark Arena for Retrieval-Augmented Generation Systems](https://aclanthology.org/2025.naacl-long.14.pdf), [ALiiCE: Evaluating Positional Fine-grained Citation Generation](https://aclanthology.org/2025.naacl-long.23.pdf), [SurveyGen: Quality-Aware Scientific Survey Generation with Large Language Models](https://aclanthology.org/2025.emnlp-main.136.pdf))
> The latent ability of a model to correctly identify and reference relevant source passages when generating a response, reflecting its grounding and traceability.

**Attribution groundedness** (1 paper: [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf))
> The quality of an LLM's generated citations in a RAG context, specifically whether the citations are relevant and sufficiently support the claims they are attached to.

## Relationships

### Citation quality →
- **TRUE** (measurement instrument): *measured_by*, 2 papers
  > We use TRUE3, a fine-tuned T5-11B (Raffel et al., 2020) model as the NLI model for the judgement of entailment in citation quality. (Section 4)
  - [ALiiCE: Evaluating Positional Fine-grained Citation Generation](https://aclanthology.org/2025.naacl-long.23.pdf)
  - [PA-RAG: RAG Alignment via Multi-Perspective Preference Optimization](https://aclanthology.org/2025.naacl-long.459.pdf)

### Associated with
- **Faithfulness** (construct), 1 paper
  > Using passage-level relevance judgments for all queries (or qrels) information available in MIRACL, we evaluate whether the system’s response cites the relevant passages, crucial for measuring faithfulness.
  - [MIRAGE-Bench: Automatic Multilingual Benchmark Arena for Retrieval-Augmented Generation Systems](https://aclanthology.org/2025.naacl-long.14.pdf)
