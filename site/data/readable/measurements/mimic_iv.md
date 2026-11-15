# MIMIC-IV
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** In the definitions, MIMIC-IV is described as a large-scale multimodal clinical dataset. Papers pair that description with patient outcome prediction tasks, specifically length of stay and 48-hour in-hospital mortality, and one paper also says its records are converted into test samples for a full-path clinical diagnosis task.

**What it is claimed to measure.** Across the papers, MIMIC-IV is linked to 3 behavioral indicators and no constructs. Papers use it to measure hospital readmission prediction, medical diagnosis, and mortality prediction. Definitions also describe it as evaluating patient outcome prediction, including length of stay and in-hospital mortality.

**Space of uses.** Papers use it as an evaluation dataset, and no other measurement instrument is linked to it. Across the uses, models are transferred to MIMIC-IV for length of stay and 48-hour in-hospital mortality tasks, its records are leveraged to create test samples for full-path clinical diagnosis, and results are reported on mortality and readmission prediction.

## Sources

**MIMIC-IV** (1 paper: [CLIMB: Data Foundations for Large Scale Multimodal Clinical Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25b/dai25b.pdf))
> A large-scale multimodal clinical dataset used to evaluate multimodal fusion strategies for patient outcome prediction, including length of stay and in-hospital mortality.

## Relationships

### → MIMIC-IV
- **Medical diagnosis** (behavioral indicator): *measured_by*, 1 paper
  > we leverage the MIMIC-IV dataset ... we convert these records into test samples for the full-path clinical diagnosis task. (Section 3.3)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
- **Mortality prediction** (behavioral indicator): *measured_by*, 1 paper
  > Extensive experiments demonstrate that KARE outperforms leading models by up to 10.8-15.0% on MIMIC-III and 12.6-12.7% on MIMIC-IV for mortality and readmission predictions. (Abstract)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Hospital readmission prediction** (behavioral indicator): *measured_by*, 1 paper
  > Extensive experiments demonstrate that KARE outperforms leading models by up to 10.8-15.0% on MIMIC-III and 12.6-12.7% on MIMIC-IV for mortality and readmission predictions. (Abstract)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
