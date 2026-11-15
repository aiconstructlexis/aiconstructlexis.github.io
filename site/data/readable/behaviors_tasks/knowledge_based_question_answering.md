# Knowledge-based question answering
**Type:** Behavioral indicator  
**Supporting papers:** 19  
**Also known as:** Knowledge question answering, Knowledge-intensive question answering  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is answering questions by making inferences over domain-specific or general knowledge. Many definitions emphasize factual or conceptual questions that require recalling, retrieving, and synthesizing specialized, external, or long-tail knowledge, often from short contexts, while some frame the task more specifically as answering a question from knowledge articles, a knowledge base, or dispersed provided documents. Papers also differ on where the knowledge comes from, with some descriptions allowing internal or external knowledge sources and others focusing on document-grounded answering.

**Variants.** Authors use several nearby labels, most commonly knowledge-based question answering, knowledge question answering, and knowledge-intensive question answering. The settings span specialized domains such as education, medicine, finance, and CRM knowledge-article repositories, with additional work on open-domain and time-sensitive questions, Chinese knowledge quiz tasks, and document-grounded settings built from large sets of dispersed documents.

**Space of elicitation and scores.** Papers link this behavior to 6 measurement instruments, including question-answering benchmarks and datasets used for knowledge-intensive reasoning. The most frequently linked are ARC, MMLU, Natural Questions, PubMedQA, and SciQA, with 1 other instrument also linked. The linked descriptions emphasize varied elicitation settings, including grade-school science questions, shorter-context knowledge QA, biomedical reasoning from abstracts, and reasoning over an open research knowledge graph.

**What it is taken as evidence of.** Only 2 constructs are linked, and the recorded links treat them as related rather than as direct evidence claims. One paper relates this behavior to Reasoning by describing the model as making inferences from necessary reasoning background, while another relates it to Parametric knowledge by describing this question type as evaluating internal knowledge retained by the base language model. Papers therefore relate it to both Reasoning and Parametric knowledge, rather than presenting a single shared construct link.

## Sources

**Knowledge-based question answering** (4 papers: [Cost-efficient Knowledge-based Question Answering with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0aafec03d59db29a92fa683bd783374-Paper-Conference.pdf), [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf), [StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf), [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318.pdf))
> The task of answering questions by making inferences over a body of domain-specific or general knowledge.

**Knowledge question answering** (4 papers: [CRMArena: Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks in Realistic Environments](https://aclanthology.org/2025.naacl-long.194.pdf), [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf), [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf), [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf))
> Answering domain-specific factual or conceptual questions from short contexts, often requiring retrieval of specialized knowledge.

**Knowledge-intensive question answering** (3 papers: [Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf), [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf))
> The task of answering questions that require recalling and synthesizing specific factual information, such as details about a historical figure.

## Relationships

### Knowledge-based question answering →
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > “Datastore scaling brings major improvements to knowledge-intensive question answering tasks such as NQ and TQA”
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 1 paper
  > “Datastore scaling brings major improvements to knowledge-intensive question answering tasks such as NQ and TQA”
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **ARC** (measurement instrument): *measured_by*, 1 paper
  > For knowledge-intensive reasoning, we use datasets that require deep domain understanding. ARC (Clark et al., 2018) tests advanced reasoning with grade-school science questions
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **PubMedQA** (measurement instrument): *measured_by*, 1 paper
  > For knowledge-intensive reasoning, we use datasets that require deep domain understanding. ... PubMedQA (Jin et al., 2019) assesses biomedical reasoning from abstracts
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **SciQA** (measurement instrument): *measured_by*, 1 paper
  > For knowledge-intensive reasoning, we use datasets that require deep domain understanding. ... and SciQA (Auer et al., 2023) challenges models using the Open Research Knowledge Graph.
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > We first evaluated knowledge QA tasks that contain shorter context but require more challenging knowledge. Three subtopics of MMLU (Hendrycks et al., 2020) are considered (Section 4.1).
  - [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf)

### Associated with
- **Reasoning** (construct), 1 paper
  > Given a question, the model is required to make inferences based on necessary reasoning background [14]. (Section 1)
  - [Cost-efficient Knowledge-based Question Answering with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0aafec03d59db29a92fa683bd783374-Paper-Conference.pdf)
- **Parametric knowledge** (construct), 1 paper
  > Knowledge-based Question Answering (KG): This type of question evaluates the model’s internal knowledge, which is retained by the base large language models (Section 2.2).
  - [Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf)
