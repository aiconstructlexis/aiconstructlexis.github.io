# Relation extraction
**Type:** Behavioral indicator  
**Supporting papers:** 27  
**Also known as:** Knowledge triple extraction  

## State of the Field

**Space of definitions.** Across the papers, relation extraction is usually treated as a task over entity relations that is evaluated on RE benchmarks, and one explicit definition spells it out as knowledge triple extraction: decomposing document content into structured ⟨head entity, relation, tail entity⟩ triples with an LLM using in-context learning. In that formulation, the model extracts triples for each retrieved document independently and is instructed to extract all knowledge triples in a document in a single pass. Elsewhere, papers frame the same behavior as relation prediction or extraction in sentence-level and document-level settings.

**Variants.** The papers use several variant names and settings, including knowledge triple extraction, low-resource relation extraction, biomedical relation extraction, and few-shot continual relation extraction. The studied settings range from sentence-level RE with ten relation classes to document-level RE, including binary chemical-disease relations and five-class chemical-protein relations. A smaller line of work focuses on sequentially identifying new relations with limited labeled samples, and another highlights recall on rare relations.

**Space of elicitation and scores.** Papers measure relation extraction with six linked instruments, all benchmark datasets. The most frequent are SemEval 2010 Task 8 and TACRED, followed by ZsRE, BC5CDR, and ChemProt, with one other benchmark also linked. These instruments are described as standard or widely used RE benchmarks spanning sentence-level, document-level, and biomedical settings; one paper reports macro-F1, and another discusses recall on rare relations in ablations.

**What it is taken as evidence of.** Only two constructs are linked to relation extraction, and the papers connect them in different ways rather than converging on a single shared construct. One line of work relates relation extraction to continual learning through the few-shot continual setting, while another paper claims a causal relationship from logical reasoning to relation extraction, using logical rules to elicit deductive reasoning ability for more precise relation prediction.

## Sources

**Knowledge triple extraction** (1 paper: [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf))
> Decomposing document content into structured ⟨head entity, relation, tail entity⟩ triples using an LLM with in-context learning.

## Relationships

### Relation extraction →
- **TACRED** (measurement instrument): *measured_by*, 4 papers
  > We evaluate BayesPrompt on four RE datasets, namely SemEval 2010 Task 8 (SemEval), TACRED (Zhang et al., 2017), TACREV (Alt et al., 2020), and ReTACRED (Stoica et al., 2021). (Section 6)
  - [BayesPrompt: Prompting Large-Scale Pre-Trained Language Models on Few-shot Inference via Debiased Domain Abstraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/5fcfda9e2a28c62f1ba54bcfa09ebdbc-Paper-Conference.pdf)
  - [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.70.pdf)
  - [Mutual-pairing Data Augmentation for Fewshot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.205.pdf)
  - [M-BRe: Discovering Training Samples for Relation Extraction from Unlabeled Texts with Large Language Models](https://aclanthology.org/2025.emnlp-main.264.pdf)
- **SemEval 2010 Task 8** (measurement instrument): *measured_by*, 4 papers
  > We evaluate BayesPrompt on four RE datasets, namely SemEval 2010 Task 8 (SemEval), TACRED (Zhang et al., 2017), TACREV (Alt et al., 2020), and ReTACRED (Stoica et al., 2021). (Section 6)
  - [BayesPrompt: Prompting Large-Scale Pre-Trained Language Models on Few-shot Inference via Debiased Domain Abstraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/5fcfda9e2a28c62f1ba54bcfa09ebdbc-Paper-Conference.pdf)
  - [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.70.pdf)
  - [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf)
  - [M-BRe: Discovering Training Samples for Relation Extraction from Unlabeled Texts with Large Language Models](https://aclanthology.org/2025.emnlp-main.264.pdf)
- **ZsRE** (measurement instrument): *measured_by*, 2 papers
  > We use a relation extraction dataset ZSRE (Meng et al., 2022a) and a conversational question answering dataset CoQA (Reddy et al., 2019) to represent unrelated tasks
  - [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf)
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
- **BC5CDR** (measurement instrument): *measured_by*, 1 paper
  > BC5CDR is a document-level RE dataset featuring binary relations between chemical and disease entities (Li et al., 2016). (Section 5.1)
  - [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf)
- **ChemProt** (measurement instrument): *measured_by*, 1 paper
  > ChemProt is a chemical-protein dataset featuring five relation classes (Taboureau et al., 2010). (Section 5.1)
  - [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf)
- **REBEL** (measurement instrument): *measured_by*, 1 paper
  > On relation extraction (RE), our pipeline achieves 65.8% macro-F1 on REBEL, an 8-point gain over the prior state of the art... (Abstract)
  - [Automated Knowledge Graph Construction using Large Language Models and Sentence Complexity Modelling](https://aclanthology.org/2025.emnlp-main.783.pdf)
- **Information retrieval** (behavioral indicator): *causes*, 1 paper
  > KiRAG decomposes documents into knowledge triples and performs iterative retrieval with these triples to enable a factually reliable retrieval process. (Abstract)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)

### → Relation extraction
- **Logical reasoning** (construct): *causes*, 1 paper
  > We use these logical rules to elicit the deductive reasoning ability of the LLM, enabling more precise relation prediction. (Section 1)
  - [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.70.pdf)
- **Natural language inference** (behavioral indicator): *causes*, 1 paper
  > Recent research efforts have explored the potential of leveraging natural language inference (NLI) techniques to enhance relation extraction (RE). (Abstract)
  - [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf)
- **Coreference resolution** (behavioral indicator): *causes*, 1 paper
  > Ablation studies demonstrate that integrating coreference and decomposition increases recall on rare relations by over 20%. (Abstract)
  - [Automated Knowledge Graph Construction using Large Language Models and Sentence Complexity Modelling](https://aclanthology.org/2025.emnlp-main.783.pdf)
- **Text simplification** (behavioral indicator): *causes*, 1 paper
  > Ablation studies demonstrate that integrating coreference and decomposition increases recall on rare relations by over 20%. (Abstract)
  - [Automated Knowledge Graph Construction using Large Language Models and Sentence Complexity Modelling](https://aclanthology.org/2025.emnlp-main.783.pdf)

### Associated with
- **Few-shot task performance** (behavioral indicator), 1 paper
  > Few-shot Continual Relation Extraction (FCRE) has emerged as a significant challenge in information extraction, necessitating that relation extraction (RE) systems can sequentially identify new relations with limited labeled samples. (Abstract)
  - [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Continual learning** (construct), 1 paper
  > Few-shot Continual Relation Extraction (FCRE) has emerged as a significant challenge in information extraction, necessitating that relation extraction (RE) systems can sequentially identify new relations with limited labeled samples. (Abstract)
  - [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf)
