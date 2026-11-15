# Schema matching
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Table join prediction, Attribute alignment  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this behavior as finding semantic correspondences between columns or attributes drawn from different tables or knowledge graphs. Most definitions focus on table columns, either as a binary decision about whether a pair of columns in two tables are related or as creating a valid mapping between columns so two tables can be joined. A smaller line of work casts it as attribute alignment across knowledge graphs, where attributes are matched when they have the same semantic meaning even if their labels differ; across these framings, success is described as identifying the semantic correspondence itself.

**Variants.** Papers use several nearby names for the behavior, including schema matching, table join prediction, and attribute alignment. The table-focused variant is studied on two tables with partially overlapping columns and asks for a join mapping from the first table to the second, while the knowledge-graph variant focuses on attributes from different knowledge graphs whose labels may differ. Papers also relate schema matching to three other behavioral indicators: candidate generation, confidence scoring, and data analysis.

**Space of elicitation and scores.** Only one measurement instrument is linked to this behavior: Wikidata, which papers use to measure schema matching and describe as a general knowledge base. No other measurement instrument is linked.

**What it is taken as evidence of.** Three constructs are linked to schema matching, but the links are not framed as schema matching measuring a single construct. Instead, papers claim causal relationships from contextual understanding, in-context learning, and semantic understanding to schema matching: contextual understanding is said to help reason about schema hierarchies and identify potential matches, in-context learning is said to let off-the-shelf LLMs solve attribute alignment without fine-tuning, and semantic understanding is said to be needed beyond basic lexical comparison when different labels represent the same concept. These claims do not center on one shared construct.

## Sources

**Schema matching** (1 paper: [Table-LLM-Specialist: Language Model Specialists for Tables using Iterative Fine-tuning](https://aclanthology.org/2025.emnlp-main.1795.pdf))
> Determining whether two columns from different tables are semantically related, treated as a binary classification task.

**Table join prediction** (1 paper: [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf))
> The task of identifying and creating a valid mapping of columns between two tables to perform a join.

**Attribute alignment** (1 paper: [Tackling Uncertain Correspondences for Multi-Modal Entity Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf))
> The task of identifying and matching attributes from different knowledge graphs that have the same semantic meaning, even if their labels differ, often performed using an LLM.

## Relationships

### Schema matching →
- **Wikidata** (measurement instrument): *measured_by*, 1 paper
  > Specifically, we evaluate Matchmaker on Magellan (e-commerce) and WikiData (general knowledge base). (Section 5.4)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)

### → Schema matching
- **Semantic understanding** (construct): *causes*, 1 paper
  > Aligning attributes across different MMKGs is challenging due to the variations in the expression of identical attributes. It necessitates more than a basic lexical comparison and requires a profound semantic understanding to ascertain whether attributes with different labels indeed represent the same concept. (Section 4.1)
  - [Tackling Uncertain Correspondences for Multi-Modal Entity Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf)
- **In-context learning** (construct): *causes*, 1 paper
  > With in-context learning, off-the-shelf LLM can solve attribute alignment without fine-tuning. (Section 4.1)
  - [Tackling Uncertain Correspondences for Multi-Modal Entity Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf)
- **Contextual understanding** (construct): *causes*, 1 paper
  > This contextual understanding enables LLMs to effectively reason about schema hierarchies and identify potential matches. (Section 4)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)

### Associated with
- **Candidate generation** (behavioral indicator), 1 paper
  > we propose Matchmaker - a compositional language model program for schema matching, comprised of candidate generation, refinement and confidence scoring. (Abstract)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
- **Confidence scoring** (behavioral indicator), 1 paper
  > we propose Matchmaker - a compositional language model program for schema matching, comprised of candidate generation, refinement and confidence scoring. (Abstract)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
- **Data analysis** (behavioral indicator), 1 paper
  > “Data Analysis: three tasks using recent datasets from Kaggle and Socrata, specifically, ... predicting which columns can be used to join two tables”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
