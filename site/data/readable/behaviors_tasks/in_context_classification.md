# In-context classification
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this as predicting the correct label for a target item from exemplars given in context as item-label pairs. The setup is described as an alternating sequence of N items and N labels followed by a query item, x1, l1, x2, l2, ..., xN, lN, xq, ?, and one description calls it a common in-context learning paradigm in which the network’s response to a target item is measured. Success is framed as predicting the target item’s label, and one formulation specifies the prediction objective with binary cross-entropy loss.

**Variants.** Most descriptions keep the same target-label prediction task but vary the classification regime. Papers discuss both binary and multi-class versions, and one paper explicitly treats in-context binary classification as a special case of the general multi-class setting. One line of work studies the task on Gaussian mixtures, and a related setting examines distribution shift through a different norms condition.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior. In the task descriptions themselves, elicitation comes from providing a sequence of item-label pairs in context and querying the label of the target item, and one formulation specifies the prediction objective with binary cross-entropy loss.

**What it is taken as evidence of.** Papers do not directly frame this behavior through recorded measured_by links. Instead, one paper relates in-context classification to in-context learning by studying binary and multi-class classification of Gaussian mixtures during ICL, and the same paper also relates it to robustness, noting that under a different norms distribution shift, performance deteriorates more for a 1-layer model while 3-layer transformers show better robustness. The recorded links therefore use related framings for in-context learning and robustness, rather than an explicit shared claim that this behavior reflects one construct in particular.

## Sources

**In-context classification** (2 papers: [Differential learning kinetics govern the transition from memorization to generalization during in-context learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/187f9ba4cd5a59477305ac712282a1cd-Paper-Conference.pdf), [The mechanistic basis of data dependence and abrupt learning in an in-context classification task](https://proceedings.iclr.cc/paper_files/paper/2024/file/540a3bf4863672cdaebfed69fa2ce335-Paper-Conference.pdf))
> The observable task of predicting the correct label for a target item based on a sequence of item-label pair exemplars provided in the context.

## Relationships

### Associated with
- **In-context learning** (construct), 1 paper
  > In this work, we study the training dynamics of a single-layer transformer for both binary and multi-class classification of Gaussian mixtures during ICL, a fundamental problem in machine learning.
  - [On the Training Convergence of Transformers for In-Context Classification of Gaussian Mixtures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25q/shen25q.pdf)
- **Binary classification** (behavioral indicator), 1 paper
  > In this section, we study the learning dynamics of a single-layer transformer for in-context binary classification. It is a special case of the general multi-class classification.
  - [On the Training Convergence of Transformers for In-Context Classification of Gaussian Mixtures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25q/shen25q.pdf)
- **Robustness** (construct), 1 paper
  > in the ‘different norms’ setting, the performance of ‘1-layer’ deteriorates more significantly, while transformers with a more complex structure (’3-layer’) show better robustness under this distribution shift.
  - [On the Training Convergence of Transformers for In-Context Classification of Gaussian Mixtures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25q/shen25q.pdf)
