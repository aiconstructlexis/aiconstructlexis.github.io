# Medical knowledge
**Type:** Construct  
**Supporting papers:** 11  
**Also known as:** Clinical domain knowledge, Clinical knowledge, Preliminary knowledge grasp  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is a model's embedded or acquired body of medically relevant knowledge, centered on diseases, symptoms, treatments, medications, procedures, and related concepts used in practice. Several definitions present this as latent or encoded knowledge inside the model, while some also describe the model as possessing and applying factual information and principles, or as relying on such knowledge to interpret clinical texts. Definitions differ mainly on scope and on whether reasoning is included: some include procedures and reasoning within clinical domain knowledge, whereas a smaller line of work narrows the construct to preliminary knowledge grasp, meaning memorizing and initially understanding foundational facts and definitions without complex reasoning or application.

**Space of facets.** Papers use nearby labels, mainly medical knowledge, clinical domain knowledge, and clinical knowledge, for overlapping content about diseases, symptoms, procedures, medications, and related clinical concepts. One paper organizes it as the lowest level in a multi-cognitive hierarchy, preliminary knowledge grasp, associated with textbook and lecture learning, memorization, and initial understanding. Another recurring distinction separates medical knowledge from advanced reasoning: tasks with little to no reasoning are described as assessing medical knowledge and are grouped under understanding rather than higher-level reasoning.

**Space of measurement.** Operationalization is concentrated in benchmark-based question answering. Papers link the construct to 4 measurement instruments, with MedMCQA and MedQA appearing most often, followed by MMLU-Medical and PubMedQA, and to 1 behavioral indicator, multiple-choice question answering. The common setup is assessment through QA or MCQ tasks; papers say such benchmarks can assess clinical domain knowledge, but one paper says most medical QA benchmarks mainly focus on preliminary knowledge grasp, and another says they are not sufficient for evaluating practical capabilities in real-world clinical settings.

**Links.** Beyond measurement, one paper reports that medical knowledge is related to multiple-choice question answering, describing MCQs as simple knowledge-recalling tasks for low-level evaluation in which the model selects the correct answer from candidate options. No causal or correlational relationships are reported.

## Sources

**Medical knowledge** (3 papers: [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf), [MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zuo25a/zuo25a.pdf), [Causal Tree Extraction from Medical Case Reports: A Novel Task for Experts-like Text Comprehension](https://aclanthology.org/2025.emnlp-main.1313.pdf))
> The extent of a model's embedded knowledge about medical concepts, including diseases, symptoms, treatments, and medications.

**Clinical domain knowledge** (1 paper: [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf))
> The extent of an LLM's acquired knowledge about medical concepts, procedures, and reasoning, typically inferred from performance on tasks like answering questions from medical licensing exams.

**Clinical knowledge** (1 paper: [Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf))
> The latent body of medically relevant knowledge about diseases, symptoms, procedures, medications, and related concepts used in practice.

**Preliminary knowledge grasp** (1 paper: [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf))
> The latent ability to memorize and initially understand foundational medical knowledge, such as facts and definitions, without requiring complex reasoning or application.

## Relationships

### Medical knowledge →
- **MedQA** (measurement instrument): *measured_by*, 2 papers
  > While these benchmarks may be useful for assessing the clinical domain knowledge of LLMs, they are not sufficient for evaluating the practical capabilities of models in assisting healthcare professionals in real-world clinical settings [37]. (Section 2)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
- **MedMCQA** (measurement instrument): *measured_by*, 2 papers
  > While these benchmarks may be useful for assessing the clinical domain knowledge of LLMs, they are not sufficient for evaluating the practical capabilities of models in assisting healthcare professionals in real-world clinical settings [37]. (Section 2)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
- **PubMedQA** (measurement instrument): *measured_by*, 1 paper
  > While these benchmarks may be useful for assessing the clinical domain knowledge of LLMs, they are not sufficient for evaluating the practical capabilities of models in assisting healthcare professionals in real-world clinical settings [37]. (Section 2)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLU-Medical** (measurement instrument): *measured_by*, 1 paper
  > While these benchmarks may be useful for assessing the clinical domain knowledge of LLMs, they are not sufficient for evaluating the practical capabilities of models in assisting healthcare professionals in real-world clinical settings [37]. (Section 2)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Multiple-choice question answering** (behavioral indicator), 1 paper
  > For Low-Level tasks (f1), we adopt multiple-choice questions (MCQs) as simple knowledge recalling tasks for Low-Level, where the model is required to recognize the correct answer from multiple candidate options (see the left part of Figure 2). (Section 3.3)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
