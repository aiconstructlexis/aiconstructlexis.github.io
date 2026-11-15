# Label prediction
**Type:** Behavioral indicator  
**Supporting papers:** 6  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats label prediction as producing the correct class label for a target item from its context sequence. A second formulation describes it as generating the final answer or classification label for an input question or premise, explicitly separate from the reasoning process. Success is framed as outputting the label itself, as in predicting the label of a target token or emitting a prediction label under the "< Predict >" prefix.

**Variants.** Variation appears mainly in task framing. Some papers study label prediction as target-token classification from a context sequence, while others treat it as final-answer classification for a question or premise. Label prediction is also related to explanation generation in some papers, which describe balancing accurate label prediction with faithful rationale generation, or training label prediction and rationale generation together.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers operationalize it directly as a prediction task, for example by training a network to predict the label of a target token, by having a smaller language model output a prediction label with the input prefix "< Predict >", or by finetuning with ground-truth labels.

**What it is taken as evidence of.** Papers do not link label prediction to any construct. The only recorded relationship connects it to explanation generation as a related behavioral indicator.

## Sources

**Label prediction** (2 papers: [Differential learning kinetics govern the transition from memorization to generalization during in-context learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/187f9ba4cd5a59477305ac712282a1cd-Paper-Conference.pdf), [QCRD: Quality-guided Contrastive Rationale Distillation for Large Language Models](https://aclanthology.org/2025.emnlp-main.724.pdf))
> Producing the correct class label for a target item given its context sequence.

## Relationships

### Associated with
- **Explanation generation** (behavioral indicator), 2 papers
  > Such domain insensitivity compromises their effectiveness, especially when balancing the dual demands of accurate label prediction and faithful rationale generation, which remains a challenge (Radhakrishnan et al., 2023). (Section 1).
  - [Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference](https://aclanthology.org/2025.acl-long.340.pdf)
  - [QCRD: Quality-guided Contrastive Rationale Distillation for Large Language Models](https://aclanthology.org/2025.emnlp-main.724.pdf)
