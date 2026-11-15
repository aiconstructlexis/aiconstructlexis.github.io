# Specialization
**Type:** Construct  
**Supporting papers:** 9  
**Also known as:** Skill specialization  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage treats specialization as models or expert components acquiring distinct roles or expertise, usually through targeted finetuning, for example specializing models into generation and critique functions or retrieving the correct expert for held-in tasks. A smaller line of work uses the term for narrow competence in a few skills or topics, with one paper warning that models can "specialize in a few skills, at the expense of others" while maximizing Elo ratings, and another describing specialist models as giving up generality to focus on a few specific topics. The main axis of disagreement is whether specialization is system-level differentiation across models or a model-level concentration on a narrow skill or domain.

**Space of facets.** Papers break the concept down by what becomes specialized: distinct functionalities such as generation versus critique, expert modules tied to held-in tasks and oracle-expert retrieval, and narrow target domains or topics. The same label also covers both specialization across models and specialization in a model performing well on only a few skills, and one paper pairs specialization with diversification across models and responses. Generalization is the construct explicitly linked to specialization, and some papers describe the two as something to balance.

**Space of measurement.** Operationalization is sparse: papers link specialization to one measurement instrument, The Pile, and to no behavioral indicators. In the linked use, 16 datasets from The Pile are treated as target specialization sets, so the explicit measurement attached to the construct matches the narrow-domain framing of specialization. The role-based and skill-concentration framings are described in the papers but are not linked to an instrument or behavioral indicator.

**Links.** A small amount of relational evidence connects generalization and specialization. Papers report that Generalization is related to Specialization: one says models focused on generalization may have unsatisfactory specialized abilities in medical time series, and another says that separating common dimensions from complementary, expert-specific dimensions seeks a balance between generalization and specialization.

## Sources

**Skill specialization** (1 paper: [Re-evaluating Open-ended Evaluation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/57a009897ab00e2d811a4581ad1f7239-Paper-Conference.pdf))
> The tendency of a model to develop high competency in a few specific skills, potentially at the expense of other, less-represented skills, often as a result of optimizing for a flawed evaluation metric.

**Specialization** (3 papers: [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf), [Soup-of-Experts: Pretraining Specialist Models via Parameters Averaging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ablin25a/ablin25a.pdf), [Glider: Global and Local Instruction-Driven Expert Router](https://aclanthology.org/2025.emnlp-main.319.pdf))
> The process by which individual models within a multiagent system develop distinct functionalities or expertise, such as generation or critique, through targeted finetuning.

## Relationships

### Specialization →
- **The Pile** (measurement instrument): *measured_by*, 1 paper
  > We consider 16 datasets from the PILE (Gao et al., 2020) as target specialization sets (Section 3)
  - [Soup-of-Experts: Pretraining Specialist Models via Parameters Averaging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ablin25a/ablin25a.pdf)

### Associated with
- **Generalization** (construct), 2 papers
  > These pre-trained TSFMs focus on generalization with a wide domain of time series, where their specialized abilities in medical time series may not be satisfactory. Therefore, we propose a lightweight TSFM personalization scheme to tackle the specialization ability. (Section 2.1).
  - [Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf)
  - [Split-Merge: Scalable and Memory-Efficient Merging of Expert LLMs](https://aclanthology.org/2025.emnlp-main.1533.pdf)
