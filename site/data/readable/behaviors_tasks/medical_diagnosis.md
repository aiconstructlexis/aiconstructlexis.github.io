# Medical diagnosis
**Type:** Behavioral indicator  
**Supporting papers:** 21  
**Also known as:** Disease Prediction, Differential diagnosis, ECG abnormal detection, Diagnosis classification, Diagnosis prediction, New diagnosis assignment, Arrhythmia diagnosis, Full-path clinical diagnosis, Phenotype prediction, Pathology detection, Seizure detection, Diagnosis extraction, Abnormal detection, Clinical diagnosis, Disease diagnosis  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats medical diagnosis as predicting, identifying, or selecting a disease or clinical condition from available evidence, including symptoms, patient profiles, admission data, clinical notes, longitudinal EHR histories, and other clinical data. Most formulations expect a final label, code, or diagnosis class, sometimes from a fixed candidate set or a predefined set of acute care conditions, while a smaller line of work frames it as differential diagnosis, generating a list of possible conditions or selecting the most likely option from several possibilities. Other definitions broaden the behavior to binary or multiclass abnormality detection in physiological signals, or to a sequential process that orders examinations, integrates their results, and then arrives at a final diagnosis.

**Variants.** The main variants span differential diagnosis, diagnosis prediction or classification from notes and longitudinal EHRs, and signal-based diagnosis in ECG and EEG. Papers also describe phenotype prediction and new diagnosis assignment, where the target is a disease manifestation or the first occurrence of a diagnosis, alongside arrhythmia diagnosis, pathology detection, seizure detection, and abnormal detection. A smaller set studies full-path clinical diagnosis with sequential examinations, or diagnosis extraction from dialogue and multimodal evidence, and one paper uses disease diagnosis for plant disease reasoning from visual symptoms and contextual knowledge.

**Space of elicitation and scores.** Papers link medical diagnosis to two dataset-based instruments, with DDXPlus appearing most often and MIMIC-IV also used. DDXPlus is described as a large-scale EHR dataset used to test diagnosing complex and diverse medical conditions, including making a diagnosis from patient profiles with a fixed set of 49 diagnoses. MIMIC-IV is used by converting clinical records into test samples for full-path clinical diagnosis.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects. Instead, medical diagnosis is related to Medical reasoning and to Interpretability and explainability, and separate papers claim causal relationships from Semantic understanding to Medical diagnosis and from Temporal dependency modeling to Medical diagnosis. The linked construct-level uses therefore remain split across related and causal framings rather than one prevailing construct interpretation.

## Sources

**Disease Prediction** (1 paper: [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf))
> Inferring the patient's disease or diagnosis based on available medical information.

**Differential diagnosis** (2 papers: [MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf), [MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zuo25a/zuo25a.pdf))
> The observable task of generating a list of possible medical conditions that could explain a given set of patient symptoms and clinical data.

**ECG abnormal detection** (1 paper: [FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf))
> Classifying ECG signals as abnormal or normal.

**Diagnosis classification** (1 paper: [Instruction Tuning Large Language Models to Understand Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/file/62986e0a78780fe5f17b495aeded5bab-Paper-Datasets_and_Benchmarks_Track.pdf))
> The clinical predictive task of identifying which of a predefined set of acute care conditions are present for a patient based on their admission data.

**Medical diagnosis** (2 papers: [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf), [Position: AI Scaling: From Up to Down and Out](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25fh/wang25fh.pdf))
> Selecting a diagnosis from a fixed set based on a patient profile and symptoms.

**Diagnosis prediction** (2 papers: [DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/892850bf793e03b5c410dfd9425b94c8-Paper-Datasets_and_Benchmarks_Track.pdf), [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf))
> Predicting the patient’s primary discharge diagnosis from a clinical note, optionally with external knowledge.

**Phenotype prediction** (1 paper: [Multimodal Medical Code Tokenizer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25b/su25b.pdf))
> Identifying the specific clinical manifestation or subtype of a disease based on a patient's medical history.

**New diagnosis assignment** (1 paper: [Multimodal Medical Code Tokenizer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25b/su25b.pdf))
> Predicting the first occurrence of a disease diagnosis in a patient's record based on longitudinal health data.

**Arrhythmia diagnosis** (1 paper: [Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf))
> Identifying abnormal heart rhythms from ECG signals, distinguishing between normal and various types of arrhythmic heartbeats.

**Full-path clinical diagnosis** (1 paper: [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf))
> The task of simulating a real-world diagnostic process by sequentially ordering examinations, integrating information from results, and arriving at a final diagnosis.

**Disease diagnosis** (4 papers: [CLIMB: Data Foundations for Large Scale Multimodal Clinical Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25b/dai25b.pdf), [DDO: Dual-Decision Optimization for LLM-Based Medical Consultation via Multi-Agent Collaboration](https://aclanthology.org/2025.emnlp-main.1340.pdf), [Agri-CM3: A Chinese Massive Multi-modal, Multi-level Benchmark for Agricultural Understanding and Reasoning](https://aclanthology.org/2025.acl-long.576.pdf), [Knowledge-Augmented Multimodal Clinical Rationale Generation for Disease Diagnosis with Small Language Models](https://aclanthology.org/2025.acl-long.540.pdf))
> The observable task of identifying a specific disease or medical condition from a patient's clinical data.

**Pathology detection** (1 paper: [EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gijsen25a/gijsen25a.pdf))
> The observable task of classifying an EEG recording as either normal or containing pathological abnormalities.

**Seizure detection** (1 paper: [EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gijsen25a/gijsen25a.pdf))
> The observable task of classifying a segment of an EEG recording as containing either seizure or background activity.

**Diagnosis extraction** (1 paper: [3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark](https://aclanthology.org/2025.emnlp-main.1353.pdf))
> Identifying and outputting the correct medical diagnosis from a dialogue or input context based on symptoms and visual evidence.

**Abnormal detection** (1 paper: [NeuroLM: A Universal Multi-task Foundation Model for Bridging the Gap between Language and EEG Signals](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf))
> Classifying EEG records as clinically normal or abnormal.

**Clinical diagnosis** (1 paper: [Knowledge-Aware Co-Reasoning for Multidisciplinary Collaboration](https://aclanthology.org/2025.emnlp-main.687.pdf))
> Producing a diagnostic answer for a medical query or case.

## Relationships

### Medical diagnosis →
- **DDXPlus** (measurement instrument): *measured_by*, 2 papers
  > To assess LLMs’ continuous improvement in applying expert knowledge, we use the DDXPlus [23] dataset, where agents must make a medical diagnosis out of 49 diagnoses based on patient profiles detailing their symptoms. (Section 3.2)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Knowledge-Aware Co-Reasoning for Multidisciplinary Collaboration](https://aclanthology.org/2025.emnlp-main.687.pdf)
- **MIMIC-IV** (measurement instrument): *measured_by*, 1 paper
  > we leverage the MIMIC-IV dataset ... we convert these records into test samples for the full-path clinical diagnosis task. (Section 3.3)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)

### → Medical diagnosis
- **Semantic understanding** (construct): *causes*, 1 paper
  > Language Models (LMs) have advanced diagnosis prediction by leveraging the semantic understanding of medical concepts in Electronic Health Records (EHRs). (Abstract)
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)
- **Temporal dependency modeling** (construct): *causes*, 1 paper
  > Capturing these overlaps while maintaining an awareness of the temporal progression is essential for accurate diagnosis prediction. (Section 2.3. Box-aware Diagnosis Prediction)
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)

### Associated with
- **Medical reasoning** (construct), 1 paper
  > For High-Level tasks (f3), we follow Hager et al. (2024) and assess LLMs’ capabilities of solving scenario-based problems using a full-path clinical diagnosis task, as illustrated in Figure 3. (Section 3.3)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
- **Interpretability and explainability** (construct), 1 paper
  > By quantifying the overlap between boxes, our method provides intuitive insights into the relationships between medical concepts, thereby improving the accuracy and interpretability of model predictions. (Section 2.3.2. VOLUME-BASED DIAGNOSIS PREDICTION)
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)
- **Zero-shot classification** (behavioral indicator), 1 paper
  > Pathology detection via zero-shot (ZS) and linear probing at 1%, 10%, and 100% labeled data of the TUAB training set. (Table 2)
  - [EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gijsen25a/gijsen25a.pdf)
