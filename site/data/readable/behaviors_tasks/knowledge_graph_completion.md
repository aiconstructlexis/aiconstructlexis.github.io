# Knowledge graph completion
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across papers, the task is treated as completing an incomplete knowledge-graph triple, though the missing slot differs across definitions. Some definitions make success predicting the missing relation for a given head and tail pair, stated as "Given a head entity h and a tail entity t, this task is to predict the missing relation between them," while others define success as inferring the missing head or tail entity from an incomplete factual triple.

**Variants.** The studied settings vary. One line narrows the task to urban knowledge graphs and specifically to geospatial relationship completion, phrased as asking models to "complete the geospatial relationship" between entities, with evaluations reported in New York City and Chicago. Another paper relates knowledge graph completion to triple classification, assessing the correctness of a triple (h, r, t), and to link prediction, identifying the most plausible tail entity for a query (h, r, ?).

**Space of elicitation and scores.** Papers measure it with 4 linked instruments. The linked dataset-based instruments are WN18RR and FB15k-237, which papers describe as conventional or widely used KGC datasets, while another evaluation setup uses Human evaluation and LLM-as-a-judge, including GPT-4-based self-evaluation in an urban KGC study.

**What it is taken as evidence of.** No construct is linked to it, so the papers do not record a construct that this behavior is taken to indicate.

## Sources

**Knowledge graph completion** (2 papers: [UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf), [Retrieval, Reasoning, Re-ranking: A Context-Enriched Framework for Knowledge Graph Completion](https://aclanthology.org/2025.naacl-long.221.pdf))
> Predicting the missing relation between a given head entity and tail entity pair.

## Relationships

### Knowledge graph completion →
- **WN18RR** (measurement instrument): *measured_by*, 2 papers
  > We evaluate MKGL on the FB15k-237 and WN18RR datasets, which are widely used by most KG completion methods (Section 4.1)
  - [MKGL: Mastery of a Three-Word Language](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe03053bd2cf5b5c56de1e463bc53e1a-Paper-Conference.pdf)
  - [Retrieval, Reasoning, Re-ranking: A Context-Enriched Framework for Knowledge Graph Completion](https://aclanthology.org/2025.naacl-long.221.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > We conduct comprehensive experiments on two UrbanKGC tasks in two metropolises (New York City and Chicago) using both human evaluation and GPT-4-based self-evaluation. (Section 1)
  - [UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > We conduct comprehensive experiments on two UrbanKGC tasks in two metropolises (New York City and Chicago) using both human evaluation and GPT-4-based self-evaluation. (Section 1)
  - [UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf)
- **FB15k-237** (measurement instrument): *measured_by*, 1 paper
  > We evaluate MKGL on the FB15k-237 and WN18RR datasets, which are widely used by most KG completion methods (Section 4.1)
  - [MKGL: Mastery of a Three-Word Language](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe03053bd2cf5b5c56de1e463bc53e1a-Paper-Conference.pdf)

### Associated with
- **Triple classification** (behavioral indicator), 1 paper
  > our work focuses on KGC, specifically addressing two tasks: (i) triple classification, assessing the correctness of a given triple (h, r, t), and (ii) link prediction, identifying the most plausible tail entity t for a given query (h, r, ?). (Section 3)
  - [Enhancing Large Language Model for Knowledge Graph Completion via Structure-Aware Alignment-Tuning](https://aclanthology.org/2025.emnlp-main.1061.pdf)
- **Link prediction** (behavioral indicator), 1 paper
  > our work focuses on KGC, specifically addressing two tasks: (i) triple classification, assessing the correctness of a given triple (h, r, t), and (ii) link prediction, identifying the most plausible tail entity t for a given query (h, r, ?). (Section 3)
  - [Enhancing Large Language Model for Knowledge Graph Completion via Structure-Aware Alignment-Tuning](https://aclanthology.org/2025.emnlp-main.1061.pdf)
