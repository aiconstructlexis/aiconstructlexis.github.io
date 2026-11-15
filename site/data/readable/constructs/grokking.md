# Grokking
**Type:** Construct  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the papers, grokking is most commonly treated as an observable training phenomenon in which test-set generalization improves abruptly long after near-perfect training-set performance has already been reached through memorization. Some descriptions phrase the shift as an "abrupt change from random guessing to generalization" after the model memorized the training set, but the shared framing is delayed generalization after the training set has already been fit.

**Space of facets.** In the papers, grokking is positioned between memorization and generalization: models are described as first memorizing, or remaining at random guessing, and only later generalizing on the test set. One account also says it "results from the model learning very structured representations," adding a representation-level description alongside the memorization to generalization transition.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to grokking. Instead, papers operationalize it through the described pattern of train and test performance, sudden test-set improvement long after near-perfect training performance, and one paper treats whether models "grok faster and achieve better performance" as evidence of stronger grokking behavior.

**Links.** Several papers claim a causal relationship from grokking to implicit reasoning, stating that transformers can learn implicit reasoning "only through grokking" and that grokking-based data augmentation can unlock implicit multi-hop reasoning capabilities. Papers also relate grokking to memorization, describing generalization as appearing well after memorization of the training set, and relate generalization to grokking through a sudden transition from pure memorization to near-perfect generalization.

## Sources

**Grokking** (2 papers: [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf), [Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.407.pdf))
> A phenomenon where a model's generalization performance abruptly improves long after it has achieved near-perfect performance on the training set through memorization.

## Relationships

### Grokking →
- **Implicit reasoning** (construct): *causes*, 2 papers
  > transformers can learn implicit reasoning, but only through grokking, i.e., extended training far beyond overfitting.
  - [Grokking of Implicit Reasoning in Transformers: A Mechanistic Journey to the Edge of Generalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad217e0c7fecc71bdf48660ad6714b07-Paper-Conference.pdf)
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)

### Associated with
- **Memorization** (construct), 1 paper
  > Power et al. [24] discovered Grokking, where models trained on modular arithmetic datasets have an abrupt change from random guessing to generalization on the test set way after the model memorized the training set. (Section 2)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Generalization** (construct), 1 paper
  > “under certain conditions, overparameterized neural networks suddenly transition from pure memorization to near-perfect generalization”
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
