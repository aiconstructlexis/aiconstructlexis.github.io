# Medical question answering
**Type:** Behavioral indicator  
**Supporting papers:** 40  
**Also known as:** Biomedicine inquiry answering, Answering medical questions, Biomedical question answering, Medical answer generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as answering questions in medicine, biomedicine, clinical contexts, or patient care, usually with success framed as producing relevant, accurate, and sometimes comprehensive or clinically relevant answers. Some authors formulate it as benchmark or exam-style question answering, often multiple choice or clinical vignettes, while one paper instead defines it as answering complex biomedicine inquiries by retrieving entities such as drugs, diseases, or genes from a biomedical knowledge base. One study describes the task as "answering open-ended questions about medical conditions" (Fine-Tuning Language Models for Factuality).

**Variants.** Papers use several closely related labels, most often "medical question answering," but also "biomedical question answering," "answering medical questions," "medical answer generation," and "biomedicine inquiry answering." The settings include open-domain medical question-answer pairs, translated benchmark questions, questions based on biomedical literature or scientific abstracts, multiple-choice problems tied to medical licensing exams, and precision-medicine inquiries over textual and relational knowledge bases.

**Space of elicitation and scores.** Papers link this behavior to 10 measurement instruments, and the dominant operationalization is benchmark-based. It is most often measured by MedQA, PubMedQA, and MedMCQA, with CMB-Clin and CMB-Exam also appearing among the linked instruments. These instruments include multiple-choice and closed-book medical QA benchmarks, open-domain or multi-round medical Q&A sets, and one evaluation framework for open-ended medical consultation tasks; as one paper notes, it evaluates "three closed-book medical QA benchmarks" (Rationale-Guided Retrieval Augmented Generation for Medical Question Answering).

**What it is taken as evidence of.** No construct is linked to it, so the papers do not specify a shared construct that this behavior is taken to indicate.

## Sources

**Medical question answering** (7 papers: [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf), [Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1551c01d7a3d0bf21e2518331e9f7074-Paper-Conference.pdf), [AutoMedEval: Harnessing Language Models for Automatic Medical Capability Evaluation](https://aclanthology.org/2025.acl-long.314.pdf), [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf), [RewardDS: Privacy-Preserving Fine-Tuning for Large Language Models via Reward Driven Data Synthesis](https://aclanthology.org/2025.emnlp-main.223.pdf), [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf), [Rationale-Guided Retrieval Augmented Generation for Medical Question Answering](https://aclanthology.org/2025.naacl-long.635.pdf))
> The observable task of answering questions related to biomedical research and clinical contexts.

**Biomedicine inquiry answering** (1 paper: [STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of retrieving entities such as drugs, diseases, or genes from a biomedical knowledge base to answer complex questions.

**Answering medical questions** (2 papers: [MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3ac952d0264ef7a505393868a70a46b6-Paper-Datasets_and_Benchmarks_Track.pdf), [Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf))
> The observable action of an LLM providing responses to queries regarding medical knowledge or patient care.

**Biomedical question answering** (2 papers: [DIDS: Domain Impact-aware Data Sampling for Large Language Model Training](https://aclanthology.org/2025.emnlp-main.215.pdf), [Mol-Instructions: A Large-Scale Biomolecular Instruction Dataset for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d346d91999074dd8d6073d4c3b13733b-Paper-Conference.pdf))
> The observable task of answering questions related to biology and medicine, often requiring specialized domain knowledge.

**Medical answer generation** (1 paper: [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf))
> The task of generating informative and accurate textual answers to questions in the medical domain.

## Relationships

### Medical question answering →
- **MedQA** (measurement instrument): *measured_by*, 5 papers
  > After training on MedAlpaca for Medical (M) domain or MedAlpaca/Alpaca-GPT4 for Medical&General (M&G) domain, we test the models at round 60 on the evaluation datasets for Medical (M) domain, i.e., MedQA [10], and MedMCQA [22]. (Section 4.2)
  - [DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf)
  - [Rationale-Guided Retrieval Augmented Generation for Medical Question Answering](https://aclanthology.org/2025.naacl-long.635.pdf)
  - [RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning](https://aclanthology.org/2025.emnlp-main.1630.pdf)
  - [Split-Merge: Scalable and Memory-Efficient Merging of Expert LLMs](https://aclanthology.org/2025.emnlp-main.1533.pdf)
  - [A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making](https://aclanthology.org/2025.emnlp-main.1699.pdf)
- **PubMedQA** (measurement instrument): *measured_by*, 4 papers
  > For the medical domain, we select the PubMedQA dataset [74], which includes 211.3K artificially generated QA training instances and 1K test instances (Section 4.4).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
  - [Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment](https://aclanthology.org/2025.emnlp-main.406.pdf)
  - [Shh, don't say that! Domain Certification in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/27befed4547edcb4bdeacef9472cadee-Paper-Conference.pdf)
- **MedMCQA** (measurement instrument): *measured_by*, 2 papers
  > After training on MedAlpaca for Medical (M) domain or MedAlpaca/Alpaca-GPT4 for Medical&General (M&G) domain, we test the models at round 60 on the evaluation datasets for Medical (M) domain, i.e., MedQA [10], and MedMCQA [22]. (Section 4.2)
  - [DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf)
  - [Rationale-Guided Retrieval Augmented Generation for Medical Question Answering](https://aclanthology.org/2025.naacl-long.635.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > For this evaluation, we use three medical QA datasets, including MMLU (Hendrycks et al., 2021), MedDDx (Su et al., 2024), and AfrimedQA (Olatunji et al., 2024).
  - [Multimodal Medical Code Tokenizer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25b/su25b.pdf)
- **MMLU-Med** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our RAG2 framework using three closed-book medical QA benchmarks—MedQA (Jin et al., 2021), MedMCQA (Pal et al., 2022), and MMLU-Med (Hendrycks et al., 2021)—where no oracle documents are present. (Section 1)
  - [Rationale-Guided Retrieval Augmented Generation for Medical Question Answering](https://aclanthology.org/2025.naacl-long.635.pdf)
- **MMCU-Medical** (measurement instrument): *measured_by*, 1 paper
  > Our experiments are conducted on two open-source query sets: MMCU-Medical (Zeng, 2023) and CMB-Exam (Wang et al., 2023d) datasets, which are designed for multi-task Q&A and encompass single and multiple-choice questions in the medical field (Section 5.1)
  - [HyKGE: A Hypothesis Knowledge Graph Enhanced RAG Framework for Accurate and Reliable Medical LLMs Responses](https://aclanthology.org/2025.acl-long.580.pdf)
- **CMB-Exam** (measurement instrument): *measured_by*, 1 paper
  > Our experiments are conducted on two open-source query sets: MMCU-Medical (Zeng, 2023) and CMB-Exam (Wang et al., 2023d) datasets, which are designed for multi-task Q&A and encompass single and multiple-choice questions in the medical field (Section 5.1)
  - [HyKGE: A Hypothesis Knowledge Graph Enhanced RAG Framework for Accurate and Reliable Medical LLMs Responses](https://aclanthology.org/2025.acl-long.580.pdf)
- **CMB-Clin** (measurement instrument): *measured_by*, 1 paper
  > one open-domain Q&A dataset CMB-Clin (Wang et al., 2023d) which is the inaugural multi-round question-answering dataset based on real, complex medical diagnosis and treatment records. (Section 5.1)
  - [HyKGE: A Hypothesis Knowledge Graph Enhanced RAG Framework for Accurate and Reliable Medical LLMs Responses](https://aclanthology.org/2025.acl-long.580.pdf)
- **MinosEval** (measurement instrument): *measured_by*, 1 paper
  > To address the limitations of traditional metrics for open-ended medical consultation tasks, we adopt MinosEval (Fan et al., 2025), a framework for evaluating medical question answering. (Section 4.2)
  - [Leveraging Knowledge Graph-Enhanced LLMs for Context-Aware Medical Consultation](https://aclanthology.org/2025.emnlp-main.1549.pdf)
- **MMLU-Medical** (measurement instrument): *measured_by*, 1 paper
  > we use Google Translate to translate the questions and answers from the medical-clinical section of the MMLU dataset (Section 3.1.2).
  - [Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1551c01d7a3d0bf21e2518331e9f7074-Paper-Conference.pdf)
