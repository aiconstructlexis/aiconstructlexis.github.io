# BANKING77
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** BANKING, Banking-77, Banking77, Bank77  

## State of the Field

**What it is.** Across papers, the prevailing usage treats BANKING77, also written as BANKING, Banking-77, or Banking77, as a banking-domain intent classification benchmark built from customer banking or online banking queries and organized into 77 intent classes or categories. Definitions commonly frame it as a fine-grained intent detection or classification resource for domain-specific language understanding, and some papers place it among benchmarks used for in-context learning. A smaller line of work uses the name Bank77 and describes it instead as an intent discovery dataset for finding unknown intents in user utterances.

**What it is claimed to measure.** Papers link BANKING77 to 1 construct and 2 behavioral indicators. The prevailing reported use is to measure Intent classification, with additional papers using it to measure Text classification; one paper also reports it as measuring Reasoning, describing evaluations of reasoning accuracy with prompt engineering and demonstration selection across BANKING77 and other benchmarks. Taken together, papers more often report it as measuring classification behaviors than as measuring a construct.

**Space of uses.** Across papers, BANKING77 often appears inside multi-dataset evaluations rather than as a standalone instrument. It is used alongside CLINC, 20 Newsgroups, Patent, Imdb, and GoEmotion, among other benchmarks, and papers position it for fine-tuning and baseline comparison under simulated data heterogeneity, for intent detection and text classification evaluation, and for in-context learning settings including long-context and demonstration-selection setups.

## Sources

**BANKING77** (1 paper: [Towards Robust and Efficient Federated Low-Rank Adaptation with Heterogeneous Clients](https://aclanthology.org/2025.acl-long.19.pdf))
> A dataset for intent classification, used in this paper to evaluate model performance under various simulated data heterogeneity settings in a federated learning context.

**BANKING** (2 papers: [TestNUC: Enhancing Test-Time Computing Approaches and Scaling through Neighboring Unlabeled Data Consistency](https://aclanthology.org/2025.acl-long.1486.pdf), [Towards Automated Error Discovery: A Study in Conversational AI](https://aclanthology.org/2025.emnlp-main.1.pdf))
> Intent classification dataset focused on customer banking queries, used to evaluate fine-grained intent detection in real-world domains.

**Banking-77** (3 papers: [Efficient Many-Shot In-Context Learning with Dynamic Block-Sparse Attention](https://aclanthology.org/2025.acl-long.1542.pdf), [DINT Transformer](https://aclanthology.org/2025.emnlp-main.495.pdf), [In-Context Learning with Long-Context Models: An In-Depth Exploration](https://aclanthology.org/2025.naacl-long.605.pdf))
> A customer service intent classification dataset in the banking domain with 77 intent classes, used to evaluate domain-specific language understanding.

**Banking77** (2 papers: [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf), [EMO: Embedding Model Distillation via Intra-Model Relation and Optimal Transport Alignments](https://aclanthology.org/2025.emnlp-main.385.pdf))
> Intent classification dataset in the banking domain with 77 classes, used to evaluate fine-grained classification under in-context learning settings.

**Bank77** (1 paper: [Co-Evolving LLMs and Embedding Models via Density-Guided Preference Optimization for Text Clustering](https://aclanthology.org/2025.emnlp-main.241.pdf))
> A dataset for intent discovery, aiming to identify unknown intents within user utterances.

## Relationships

### → BANKING77
- **Intent classification** (behavioral indicator): *measured_by*, 2 papers
  > We report top-1 accuracy for finetuning classification tasks on the ... 77-class Banking-77 (B77) (Casanueva et al., 2020).
  - [Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf)
  - [Towards Automated Error Discovery: A Study in Conversational AI](https://aclanthology.org/2025.emnlp-main.1.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > This section presents a comprehensive evaluation of the reasoning accuracy of both closed-source and open-source LLMs using a range of prompt engineering and demonstration selection techniques across four benchmark datasets: BANKING77, CLINC150, HWU64, and LIU54. (Section 4.4)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **Text classification** (behavioral indicator): *measured_by*, 1 paper
  > Text Classification: Requires models to capture the overall semantics of a single text input. We use Patent (Sharma et al., 2019), Imdb and Banking77 (both from MTEB (Muennighoff et al., 2023)). (Section 4.1)
  - [EMO: Embedding Model Distillation via Intra-Model Relation and Optimal Transport Alignments](https://aclanthology.org/2025.emnlp-main.385.pdf)
