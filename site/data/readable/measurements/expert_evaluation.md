# Expert evaluation
**Type:** Measurement instrument  
**Supporting papers:** 90  
**Also known as:** Human expert evaluation, Expert annotation, Human expert annotation, Expert relevance annotation, Expert explanation evaluation, Expert annotation evaluation, Expert verification evaluation, Clinical reader study, Physician reader study, Human expert review, Expert review, Expert human evaluation, Clinician evaluation, Domain-expert evaluation, Domain scholar evaluation, Pilot expert validation, Human-as-a-Judge, Human expert validation, Domain expert evaluation  

## State of the Field

**What it is.** Across papers, the prevailing usage is a domain-specific human assessment protocol: experts or other qualified evaluators manually review model outputs, annotations, or benchmark items against references, task requirements, or explicit rubrics. Definitions vary in name, including human expert evaluation, expert annotation, expert review, reader study, validation, and human-as-a-judge, but most describe independent scoring or comparison by clinicians, physicians, radiologists, legal experts, translators, researchers, or other subject-matter specialists; some papers instead use native speakers, students, or trained participants. Common formats include pairwise comparisons, rubric-based ratings, binary judgments, blind or randomized review, and consensus adjudication after disagreements, and some papers use the protocol not only to assess model outputs but also to validate labels, benchmark items, or human performance baselines.

**What it is claimed to measure.** Papers use expert evaluation to measure five constructs, Accuracy, Faithfulness, Fluency, Legal accuracy, and Relevance, and one behavioral indicator, Hallucination. The linked claims are spread across several dimensions rather than centered on a single construct: papers describe faithfulness and relevance as judged by expert human annotators, use expert review of generated components to assess accuracy, use legal experts to score fluency and legal accuracy, and use manual expert annotation to assess hallucination when automatic detection was described as unreliable.

**Space of uses.** Most papers position expert evaluation as a direct manual check on system outputs or data quality, and a smaller line of work uses it to set human baselines on benchmark tasks. It is linked to three other measurement instruments, LLM-as-a-judge, EHRNoteQA, and GAVIE; papers report that LLM-as-a-judge correlates with expert evaluation, EHRNoteQA correlates with clinician-evaluated performance, and GAVIE is related to expert evaluation through reported alignment with human evaluation.

**Concerns raised.** Where papers discuss caution, they focus on validity and reliability rather than on a single substantive flaw: some papers present expert annotation as a more reliable estimate than crowdsourced labels, another turns to experts because incomplete text annotations meant GPT-4 could not reliably detect hallucinations, and several reduce disagreement or bias through consensus adjudication, blind review, or randomized review.

## Sources

**Human expert evaluation** (10 papers: [Are Multimodal LLMs Robust Against Adversarial Perturbations? RoMMath: A Systematic Evaluation on Multimodal Math Reasoning](https://aclanthology.org/2025.naacl-long.582.pdf), [Multimodal Cognitive Reframing Therapy via Multi-hop Psychotherapeutic Reasoning](https://aclanthology.org/2025.naacl-long.250.pdf), [Is a Peeled Apple Still Red? Evaluating LLMs' Ability for Conceptual Combination with Property Type](https://aclanthology.org/2025.naacl-long.456.pdf), [AutoParLLM: GNN-guided Context Generation for Zero-Shot Code Parallelization using LLMs](https://aclanthology.org/2025.naacl-long.593.pdf), [FLEX: Expert-level False-Less EXecution Metric for Text-to-SQL Benchmark](https://aclanthology.org/2025.naacl-long.228.pdf), [LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks](https://aclanthology.org/2025.acl-long.183.pdf), [AssoCiAm: A Benchmark for Evaluating Association Thinking while Circumventing Ambiguity](https://aclanthology.org/2025.emnlp-main.263.pdf), [Dial-In LLM: Human-Aligned LLM-in-the-loop Intent Clustering for Customer Service Dialogues](https://aclanthology.org/2025.emnlp-main.300.pdf), [Transferable Direct Prompt Injection via Activation-Guided MCMC Sampling](https://aclanthology.org/2025.emnlp-main.102.pdf), [VisFinEval: A Scenario-Driven Chinese Multimodal Benchmark for Holistic Financial Understanding](https://aclanthology.org/2025.emnlp-main.1229.pdf))
> A process where human experts with extensive SQL experience independently evaluate the semantic correctness of generated queries, with discrepancies resolved through consensus.

**Expert evaluation** (3 papers: [MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf), [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf), [Ask Patients with Patience: Enabling LLMs for Human-Centric Medical Dialogue with Grounded Reasoning](https://aclanthology.org/2025.emnlp-main.142.pdf))
> A human evaluation protocol in which medical professionals assess the accuracy of generated descriptions against ground-truth annotations.

**Expert annotation** (3 papers: [CompA: Addressing the Gap in Compositional Reasoning in Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/43c18853329c7504996b255252b6cb1f-Paper-Conference.pdf), [Human Feedback is not Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2024/file/f719b8ca81221f380836e573d479c223-Paper-Conference.pdf), [Are LLMs Better than Reported? Detecting Label Errors and Mitigating Their Effect on Model Performance](https://aclanthology.org/2025.emnlp-main.1360.pdf))
> A human evaluation procedure in which subject-matter experts annotate audio events and validate or correct captions for benchmark and training data.

**Human expert annotation** (2 papers: [DarkBench: Benchmarking Dark Patterns in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f6421fbc2351067ef9c75e4bcd12af5-Paper-Conference.pdf), [LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://aclanthology.org/2025.emnlp-main.314.pdf))
> An evaluation procedure where human experts in a specific domain review and validate model outputs or automated annotations.

**Expert relevance annotation** (1 paper: [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf))
> A human evaluation protocol where domain experts (senior medical students) annotate the relevance of microtheory facts for a specific task (USMLE tests) using a 5-point rubric.

**Expert explanation evaluation** (1 paper: [Decision Information Meets Large Language Models: The Future of Explainable Operations Research](https://proceedings.iclr.cc/paper_files/paper/2025/file/a48e5877c7bf86a513950ab23b360498-Paper-Conference.pdf))
> A human blind review protocol where OR experts anonymously score the explanations generated by different methods.

**Expert verification evaluation** (1 paper: [MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.79.pdf))
> Human evaluation in which professional translators assess translation quality on accuracy, fluency, and completeness using a 5-point Likert scale.

**Clinical reader study** (1 paper: [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf))
> A human evaluation involving clinicians who score model outputs on correctness, completeness, and logical flow using USMLE-style questions from MedQA.

**Physician reader study** (1 paper: [Process-Supervised Reward Models for Verifying Clinical Note Generation: A Scalable Approach Guided by Domain Expertise](https://aclanthology.org/2025.emnlp-main.967.pdf))
> Human evaluation involving nine physicians who assessed the quality of clinical notes selected by different PRM checkpoints through blinded, randomized review.

**Human expert review** (1 paper: [Structuring Radiology Reports: Challenging LLMs with Lightweight Models](https://aclanthology.org/2025.emnlp-main.392.pdf))
> An evaluation protocol where five board-certified radiologists assessed 223 generated reports for errors and adherence to a predefined template compared to their original free-form counterparts.

**Expert review** (1 paper: [X-FLoRA: Cross-modal Federated Learning with Modality-expert LoRA for Medical VQA](https://aclanthology.org/2025.emnlp-main.422.pdf))
> A human evaluation protocol where domain experts, such as radiologists or physicians, assess the quality, clinical alignment, and reliability of model-generated responses.

**Expert human evaluation** (2 papers: [CoCoLex: Confidence-guided Copy-based Decoding for Grounded Legal Text Generation](https://aclanthology.org/2025.acl-long.931.pdf), [NormGenesis: Multicultural Dialogue Generation via Exemplar-Guided Social Norm Modeling and Violation Recovery](https://aclanthology.org/2025.emnlp-main.1715.pdf))
> A human evaluation protocol where a legal expert assesses model-generated responses on a 5-point Likert scale across criteria including correctness, faithfulness, fluency, and coherence.

**Clinician evaluation** (1 paper: [uMedSum: A Unified Framework for Clinical Abstractive Summarization](https://aclanthology.org/2025.acl-long.134.pdf))
> A human evaluation protocol where domain experts (in this case, two orthopaedic surgeons) perform pairwise comparisons of summaries based on overall quality and annotate errors like confabulations or missing information.

**Domain-expert evaluation** (1 paper: [Tree-of-Debate: Multi-Persona Debate Trees Elicit Critical Thinking for Scientific Comparative Analysis](https://aclanthology.org/2025.acl-long.1422.pdf))
> A human evaluation protocol where researchers with deep expertise in a specific field assess the quality of model outputs, such as comparative summaries, based on criteria like factuality, breadth, and contextualization.

**Domain scholar evaluation** (1 paper: [OntologyRAG-Q: Resource Development and Benchmarking for Retrieval-Augmented Question Answering in Qur'anic Tafsir](https://aclanthology.org/2025.emnlp-main.784.pdf))
> Expert evaluation by an Islamic scholarship domain expert using a 5-point scale to assess the accuracy and correctness of model responses, with qualitative feedback on answer quality.

**Pilot expert validation** (1 paper: [ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning](https://aclanthology.org/2025.emnlp-main.1344.pdf))
> A human evaluation protocol where board-certified physicians review a sample of model-generated examples to assess their medical quality.

**Human-as-a-Judge** (1 paper: [Agent-as-a-Judge: Evaluate Agents with Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuge25a/zhuge25a.pdf))
> A human expert evaluation protocol in which expert evaluators review agent outputs and decide whether each requirement was satisfied, including consensus adjudication.

**Human expert validation** (1 paper: [IFIR: A Comprehensive Benchmark for Evaluating Instruction-Following in Expert-Domain Information Retrieval](https://aclanthology.org/2025.naacl-long.511.pdf))
> A procedure in which domain experts assess the quality of instruction-following queries and relevant passages in IFIR, rating criteria such as naturalness, fluency, and relevance on a 5-point scale.

**Domain expert evaluation** (1 paper: [Matter-of-Fact: A Benchmark for Verifying the Feasibility of Literature-Supported Claims in Materials Science](https://aclanthology.org/2025.emnlp-main.203.pdf))
> Human evaluation by a materials science expert to validate the correctness and feasibility of claims, serving as a gold standard for benchmark quality assessment.

## Relationships

### Expert evaluation →
- **LLM-as-a-judge** (measurement instrument): *correlates*, 1 paper
  > employ a combination of expert human evaluation and LLM-as-a-Judge (using GPT-4-turbo-2024-04-09)... has a higher correlation (≈0.97%) to expert human evaluations
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)

### → Expert evaluation
- **Faithfulness** (construct): *measured_by*, 1 paper
  > Automatic evaluation of retrieval augmented generation (RAG) systems relies on fine-grained dimensions like faithfulness and relevance, as judged by expert human annotators.
  - [MEMERAG: A Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1101.pdf)
- **Relevance** (construct): *measured_by*, 1 paper
  > Automatic evaluation of retrieval augmented generation (RAG) systems relies on fine-grained dimensions like faithfulness and relevance, as judged by expert human annotators.
  - [MEMERAG: A Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1101.pdf)
- **Accuracy** (construct): *measured_by*, 1 paper
  > An optimization expert manually reviewed each model and assessed the correctness of four key components: decision variables, objective function, equality constraints, and inequality constraints.
  - [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf)
- **Fluency** (construct): *measured_by*, 1 paper
  > Following the revision, each QA instance is evaluated by three different legal experts using five criteria: Fluency, Practicality, Relevance, Legal Accuracy, and Complexity. (Section 3.3)
  - [KoBLEX: Open Legal Question Answering with Multi-hop Reasoning](https://aclanthology.org/2025.emnlp-main.200.pdf)
- **Legal accuracy** (construct): *measured_by*, 1 paper
  > Following the revision, each QA instance is evaluated by three different legal experts using five criteria: Fluency, Practicality, Relevance, Legal Accuracy, and Complexity. (Section 3.3)
  - [KoBLEX: Open Legal Question Answering with Multi-hop Reasoning](https://aclanthology.org/2025.emnlp-main.200.pdf)
- **Hallucination** (behavioral indicator): *measured_by*, 1 paper
  > Due to incomplete text annotations on the MMHal, GPT-4 couldn't reliably detect hallucinations. To make the results more reliable, we invited experts to manually annotate the data
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **EHRNoteQA** (measurement instrument): *correlates*, 1 paper
  > Results show that LLM performance on EHRNoteQA have higher correlation with clinician-evaluated performance (Spearman(ρ): 0.78, Kendall(τ ): 0.62)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **GAVIE** (measurement instrument), 1 paper
  > From our experiments, we show that GAVIE is not only stable but also aligns with human evaluation. (Section 1)
  - [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)
