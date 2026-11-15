# Named entity recognition
**Type:** Behavioral indicator  
**Supporting papers:** 61  
**Also known as:** Named entity extraction, Numeric named entity recognition, Textual named entity recognition, Legal named-entity recognition, Entity recognition, Named entity detection  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats named entity recognition as identifying entity mentions in text and assigning them semantic types, most often person, organization, and location. Several definitions make the success condition explicit as extracting all entities or spans and determining their types, for example, "Given a passage, your task is to extract all entities and identify their entity types" (UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition). Most formulations use predefined labels, though some allow open or domain-specific categories, and a smaller line of work narrows the task to extraction or detection only, such as extracting entities from notes or finding all mentions of one specific entity type.

**Variants.** Papers study cross-lingual and multilingual NER, including transfer across many languages and token-level labeling in multilingual queries, alongside zero-shot and domain-specific settings. Domain adaptations include social media note extraction, legal texts, Greek financial text with separate numeric and textual NER, shopping queries for brands or product lines, urban entity recognition before relation extraction, and spoken language understanding where slot filling is recast as entity detection. Another strand studies named entity detection for specific types such as chemicals, genes, or diseases.

**Space of elicitation and scores.** Papers link this behavior to 5 measurement instruments. The instruments named most often are CoNLL-2003, CrossNER, OntoNotes, Plutus-ben, and WikiAnn. The linked instruments are all described as datasets or benchmarks for NER-style evaluation, covering news text in CoNLL-2003, multi-domain data in CrossNER, web text in OntoNotes, Greek financial tasks in Plutus-ben, and low-resource language data in WikiAnn.

**What it is taken as evidence of.** Papers do not offer multiple construct framings here. The only linked construct is Understanding, and LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models places named-entity recognition among tasks at the Understanding level, describing that level as examining the ability to comprehend and interpret facts, entities, concepts, and relationships in legal texts. Beyond this related link, papers do not connect the behavior to other constructs.

## Sources

**Named entity recognition** (3 papers: [Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f9a44cb707ede42a659ad85d940dd55-Paper-Conference.pdf), [Heads up! Large Language Models Can Perform Tasks Without Your Instruction via Selective Attention Head Masking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25l/han25l.pdf), [Improving Low-Resource Sequence Labeling with Knowledge Fusion and Contextual Label Explanations](https://aclanthology.org/2025.emnlp-main.288.pdf))
> The observable task of identifying and categorizing named entities (like people, organizations, or locations) in text.

**Named entity extraction** (1 paper: [SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf))
> Identifying and extracting named entities such as people, places, or organizations from social media notes.

**Numeric named entity recognition** (1 paper: [Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance](https://aclanthology.org/2025.emnlp-main.1535.pdf))
> The task of identifying and classifying numerical expressions in text into predefined categories like monetary, percentage, temporal, and quantity.

**Textual named entity recognition** (1 paper: [Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance](https://aclanthology.org/2025.emnlp-main.1535.pdf))
> Detecting and categorizing named entities such as persons, locations, and organizations in Greek financial texts, particularly in complex linguistic expressions.

**Legal named-entity recognition** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> Extracting all named entities from a legal text and determining their specific entity types.

**Entity recognition** (2 papers: [UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf), [ECLM: Entity Level Language Model for Spoken Language Understanding with Chain of Intent](https://aclanthology.org/2025.acl-long.1061.pdf))
> Identifying relevant urban entities in text before relation extraction.

**Named entity detection** (1 paper: [PICLe: Pseudo-annotations for In-Context Learning in Low-Resource Named Entity Detection](https://aclanthology.org/2025.naacl-long.518.pdf))
> The observable task of identifying and extracting all mentions of a specific type of entity (e.g., chemicals, genes, diseases) from a given text.

## Relationships

### Named entity recognition →
- **CoNLL-2003** (measurement instrument): *measured_by*, 5 papers
  > For Named Entity Recognition (NER), we use English CoNLL03 (Tjong Kim Sang, 2002) as train/dev data (Section 4.1)
  - [Constrained Decoding for Cross-lingual Label Projection](https://proceedings.iclr.cc/paper_files/paper/2024/file/67390075fe466276797f489115582cdc-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [Transplant Then Regenerate: A New Paradigm for Text Data Augmentation](https://aclanthology.org/2025.emnlp-main.702.pdf)
  - [LLMs are Better Than You Think: Label-Guided In-Context Learning for Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.1441.pdf)
- **CrossNER** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our framework on two widely used benchmarks CrossNER (Liu et al., 2021) and MIT (Ushio and Camacho-Collados, 2021), which contain datasets from seven domains (AI, Literature, Music, Politics, Science, Movie, and Restaurant) in total. (Section 4.1)
  - [Selecting and Merging: Towards Adaptable and Scalable Named Entity Recognition with Large Language Models](https://aclanthology.org/2025.acl-long.487.pdf)
- **WikiAnn** (measurement instrument): *measured_by*, 1 paper
  > in WikiAnn (Pan et al., 2017) named entity recognition (NER) dataset, where all ST languages other than Chinese (Mandarin) amount to 131K name mentions
  - [A Survey of NLP Progress in Sino-Tibetan Low-Resource Languages](https://aclanthology.org/2025.naacl-long.396.pdf)
- **OntoNotes** (measurement instrument): *measured_by*, 1 paper
  > To demonstrate the effectiveness of our method, we evaluate it on five NER datasets... These datasets include... OntoNotes (Weischedel et al., 2013) for web text from various sources.
  - [LLMs are Better Than You Think: Label-Guided In-Context Learning for Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.1441.pdf)
- **Plutus-ben** (measurement instrument): *measured_by*, 1 paper
  > “Plutus-ben addresses six core tasks: numeric/textual named entity recognition, question answering, extractive summarization, abstractive summarization, and topic classification.”
  - [Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance](https://aclanthology.org/2025.emnlp-main.1535.pdf)

### Associated with
- **Understanding** (construct), 1 paper
  > Tasks at the Understanding level examine the ability to comprehend and interpret facts, entities, concepts, and relationships in legal texts... We construct five tasks at this level: ...Named-entity Recognition (2-5). (Section C.3.2)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text summarization** (behavioral indicator), 1 paper
  > It is commonly accepted that the summarization task, at least in the news domain, requires NER skills to be performed effectively.
  - [Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.18.pdf)
- **Information retrieval** (behavioral indicator), 1 paper
  > Information Retrieval. Effective search functionality is essential in SNS. Models should interpret query intent and retrieve relevant information from large datasets, delivering the most accurate results. Tasks: (3) Note-NER. Extracts named entities from note content.
  - [SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf)
