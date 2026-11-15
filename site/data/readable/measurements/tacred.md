# TACRED
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Most papers describe TACRED as a large-scale benchmark dataset for relation extraction. Definitions commonly trace it to the TAC Knowledge Base Population challenges, and one paper specifies it as a large-scale English dataset from the TACKBP4 challenge with 42 distinct relations. One definition adds that it contains annotated entity pairs and relations from news and web text, and one paper refers to TACRED together with variants such as TACRED-Revisit and Re-TACRED.

**What it is claimed to measure.** Across the papers, the use claims converge on a single target: TACRED is used to measure relation extraction. Papers link it to one behavioral indicator, Relation extraction, and to no constructs, describing it as one of the "widely used RE benchmark datasets" and as part of "standard relation extraction benchmarks" for evaluating relation extraction performance.

**Space of uses.** Papers most often position TACRED as an evaluation benchmark used alongside other relation extraction datasets, especially SemEval, FewRel, TACREV, TACRED-Revisit, and Re-TACRED. Several papers describe experiments on benchmark sets that include TACRED, and some report few-shot settings on it, such as "5-way 5-shot," or compare methods against multiple baselines on TACRED and FewRel. One paper uses it differently by converting the dataset from relation extraction to slot filling for training, stating that this was done "to increase the complexity of the task".

## Sources

**TACRED** (6 papers: [BayesPrompt: Prompting Large-Scale Pre-Trained Language Models on Few-shot Inference via Debiased Domain Abstraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/5fcfda9e2a28c62f1ba54bcfa09ebdbc-Paper-Conference.pdf), [GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf), [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf), [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.70.pdf), [Mutual-pairing Data Augmentation for Fewshot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.205.pdf), [M-BRe: Discovering Training Samples for Relation Extraction from Unlabeled Texts with Large Language Models](https://aclanthology.org/2025.emnlp-main.264.pdf))
> A large-scale benchmark dataset for relation extraction, derived from the annual Text Analysis Conference (TAC) Knowledge Base Population (KBP) challenges.

## Relationships

### → TACRED
- **Relation extraction** (behavioral indicator): *measured_by*, 4 papers
  > We evaluate BayesPrompt on four RE datasets, namely SemEval 2010 Task 8 (SemEval), TACRED (Zhang et al., 2017), TACREV (Alt et al., 2020), and ReTACRED (Stoica et al., 2021). (Section 6)
  - [BayesPrompt: Prompting Large-Scale Pre-Trained Language Models on Few-shot Inference via Debiased Domain Abstraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/5fcfda9e2a28c62f1ba54bcfa09ebdbc-Paper-Conference.pdf)
  - [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.70.pdf)
  - [Mutual-pairing Data Augmentation for Fewshot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.205.pdf)
  - [M-BRe: Discovering Training Samples for Relation Extraction from Unlabeled Texts with Large Language Models](https://aclanthology.org/2025.emnlp-main.264.pdf)
