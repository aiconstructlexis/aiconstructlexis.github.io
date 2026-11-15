# Medical reasoning
**Type:** Construct  
**Supporting papers:** 15  
**Also known as:** Diagnostic reasoning, Scenario-based problem solving  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats medical reasoning as a latent or cognitive ability to apply medical knowledge and clinical logic in complex, domain-specific inference. Most definitions center this ability on analyzing patient information, considering differential diagnoses, and inferring a likely diagnosis, sometimes framed as support for medical analysis and diagnostic tasks. A smaller line of work broadens the scope to professional-level, multi-step diagnostic and prognostic thinking that integrates visual information with specialized knowledge, or to scenario-based problem solving in realistic clinical workflows.

**Space of facets.** In papers, the construct is organized most often around diagnosis, and "diagnostic reasoning" appears as a closely aligned label for the same general capability. Some authors extend it to prognosis or treat it as part of an L3 "scenario-based problem solving" level, where models plan across multiple steps, order examinations, and make diagnoses in realistic settings. One definition also draws a boundary by describing diagnostic reasoning as distinct from factual recall or pattern matching.

**Space of measurement.** Operationalization centers on 2 linked measurement instruments and 1 linked behavioral indicator. MedQA is described as constructed from USMLE questions to evaluate medical reasoning and knowledge in a multiple-choice format, while DDXPlus is described as using clinical vignettes to evaluate diagnostic reasoning abilities in a clinical-like setting; the linked behavioral indicator is Medical diagnosis through a full-path clinical diagnosis task for scenario-based problems. These measures target medical or diagnostic reasoning through question answering, vignette-based evaluation, and diagnosis tasks, which fits the diagnosis-centered definitions more directly than the broader workflow-oriented framing.

**Links.** Outside of measurement, papers record related links to 1 construct and 1 behavioral indicator. Medical reasoning is related to Interpretability and explainability in work that says evaluating interpretability in medical NLP should count both perception or reading and reasoning, and in work that describes explainability into a diagnostic reasoning process. Medical diagnosis is also related to medical reasoning through the use of a full-path clinical diagnosis task for assessing scenario-based problems.

## Sources

**Medical reasoning** (3 papers: [Biomedical Visual Instruction Tuning with Clinician Preference Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec33ab89b5986605cd7c331396e7e5c-Paper-Datasets_and_Benchmarks_Track.pdf), [Visual and Domain Knowledge for Professional-level Graph-of-Thought Medical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bao25b/bao25b.pdf), [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf))
> The ability to perform complex, domain-specific reasoning and inference to support medical analysis and diagnostic tasks.

**Diagnostic reasoning** (2 papers: [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf), [Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf))
> The cognitive ability to analyze patient information, consider differential diagnoses, and arrive at a likely medical diagnosis.

**Scenario-based problem solving** (1 paper: [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf))
> The latent ability to plan and solve problems in realistic medical scenarios by integrating information across multiple steps, ordering examinations, and making diagnoses under conditions that simulate real-world clinical workflows.

## Relationships

### Medical reasoning →
- **MedQA** (measurement instrument): *measured_by*, 1 paper
  > “MedQA was constructed from USMLE questions to evaluate the medical reasoning and knowledge of LLMs in a multiple-choice format.”
  - [Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf)
- **DDXPlus** (measurement instrument): *measured_by*, 1 paper
  > DDXPlus [73]... involve clinical vignettes... evaluating the AI’s diagnostic reasoning abilities similar to a clinical setting (Section 4.1).
  - [MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf)

### Associated with
- **Interpretability and explainability** (construct), 2 papers
  > This observation suggests that both perception, or reading (e.g., finding necessary information in the medical record) and reasoning (determining the disease based on the observations) should be counted when evaluating interpretability in LLM-based medical NLP tasks. (Section 1)
  - [DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/892850bf793e03b5c410dfd9425b94c8-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MEDDxAgent: A Unified Modular Agent Framework for Explainable Automatic Differential Diagnosis](https://aclanthology.org/2025.acl-long.677.pdf)
- **Medical diagnosis** (behavioral indicator), 1 paper
  > For High-Level tasks (f3), we follow Hager et al. (2024) and assess LLMs’ capabilities of solving scenario-based problems using a full-path clinical diagnosis task, as illustrated in Figure 3. (Section 3.3)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
