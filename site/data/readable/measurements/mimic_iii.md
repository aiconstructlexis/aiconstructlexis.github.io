# MIMIC-III
**Type:** Measurement instrument  
**Supporting papers:** 8  

## State of the Field

**What it is.** Across the surveyed work, MIMIC-III is most commonly described as a publicly available, de-identified in-patient or critical care EHR dataset from the Medical Information Mart for Intensive Care project. Definitions consistently tie it to patients who stayed in critical care units, while some papers describe particular contents such as discharge summaries or radiology reports used for clinical NLP evaluation. A smaller strand also treats it as the source dataset for EHRCon and as a database of ICU patient records from Beth Israel Deaconess Medical Center.

**What it is claimed to measure.** Papers link MIMIC-III to 2 behavioral indicators and 1 construct. The prevailing usage is to measure mortality prediction, with hospital readmission prediction also reported, and a smaller line of work using it to measure privacy preservation. Overall, the recorded measurement claims are concentrated more on predictive behavioral indicators than on a broad range of constructs.

**Space of uses.** Papers do not link it to other measurement instruments. In use, one paper places it alongside MIMIC-IV and EHRShot as a public EHR dataset, while other papers use it as the data source for downstream evaluations such as mortality prediction, sepsis prediction, EHR consistency checking, and clinical text summarization.

## Sources

**MIMIC-III** (6 papers: [Multimodal Medical Code Tokenizer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25b/su25b.pdf), [Not What the Doctor Ordered: Surveying LLM-based De-identification and Quantifying Clinical Information Loss](https://aclanthology.org/2025.emnlp-main.1637.pdf), [EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/file/a291dad965af9bc2e39ffeb2ca1c6dc0-Paper-Datasets_and_Benchmarks_Track.pdf), [FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf), [Knowledge-Empowered Dynamic Graph Network for Irregularly Sampled Medical Time Series](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c04aea54c2a60a632a47bd451cd2849-Paper-Conference.pdf), [SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/97fe251c25b6f99a2a23b330a75b11d4-Paper-Conference.pdf))
> A publicly available in-patient dataset from the MIMIC (Medical Information Mart for Intensive Care) project, containing de-identified health data associated with patients who stayed in critical care units.

## Relationships

### → MIMIC-III
- **Mortality prediction** (behavioral indicator): *measured_by*, 2 papers
  > Mortality Prediction involves using various data points and a classification or predictive model to estimate the likelihood of a patient’s survival or death during their stay in the Intensive Care Unit (ICU). We extract the data from MIMIC-III using the ICU-oriented preprocessing pipeline [78]. (Section 4.1).
  - [FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Hospital readmission prediction** (behavioral indicator): *measured_by*, 1 paper
  > Extensive experiments demonstrate that KARE outperforms leading models by up to 10.8-15.0% on MIMIC-III and 12.6-12.7% on MIMIC-IV for mortality and readmission predictions. (Abstract)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Privacy preservation** (construct): *measured_by*, 1 paper
  > Table 3: Privacy protection performance under the private entity known setting on the MIMIC-III dataset.
  - [Controlled Generation for Private Synthetic Text](https://aclanthology.org/2025.emnlp-main.1663.pdf)
