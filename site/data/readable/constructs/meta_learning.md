# Meta-learning
**Type:** Construct  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats meta-learning as learning how to perform a new task from a few examples by inferring task rules, not merely retrieving or copying from context. Definitions largely agree on rapid adaptation from limited data, though they differ slightly in emphasis: one describes an ability to learn from few-shot examples, while another frames a latent capacity to acquire abstract reasoning strategies that generalize and then quickly specialize to new domains with minimal supervision.

**Space of facets.** Papers most often place meta-learning in direct relation to In-context learning: one recurring framing says current research explains the in-context learning mechanism through two approaches, meta-learning and knowledge retrieval, and another associates success on few-shot examples with the ability to meta-learn. Another formulation ties it to task inference or Task learning, calling task inference ability a form of meta-learning, and one paper uses the Reversal curse as a contrast case by describing it as a failure of meta-learning.

**Space of measurement.** The recorded operationalization is sparse: no measurement instrument, benchmark, human evaluation, LLM-as-a-judge, probe, or analysis is linked to meta-learning. Papers link it to 1 behavioral indicator, Protein understanding, and to 4 constructs, In-context learning, Generalization, Reversal curse, and Task learning; when made concrete in prose, it is through learning from few-shot examples, task inference, and rapid adaptation to new tasks with minimal supervision.

**Links.** Several papers relate meta-learning to In-context learning, describing it as one of the two main approaches used to explain the in-context learning mechanism, and another says the Transformer can be viewed as a powerful meta-learner in this setting. One paper also relates it to Task learning via task inference ability, one relates it to the Reversal curse by calling that phenomenon a failure of meta-learning, and one paper claims causal relationships from Meta-learning to Protein understanding and to Generalization, citing positive transfer to unseen fitness prediction tasks and generalization after in-context meta-learning followed by fine-tuning; no correlational link is reported.

## Sources

**Meta-learning** (2 papers: [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf), [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.727.pdf))
> The ability to learn how to perform a new task by inferring its rules from a few examples, rather than simply retrieving or copying information from the context.

## Relationships

### Meta-learning →
- **Protein understanding** (behavioral indicator): *causes*, 1 paper
  > we propose meta-learning over a distribution of standard fitness prediction tasks, and demonstrate positive transfer to unseen fitness prediction tasks. (ABSTRACT)
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > Using Metalic’s unique combination of in-context meta-learning followed by fine-tuning, we enable the generalization of extensive fine-tuning, while also precluding expensive computation. (Section 3.2)
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)

### Associated with
- **In-context learning** (construct), 3 papers
  > Broadly speaking, current research identifies two main approaches to explain the ICL mechanism (Dong et al., 2024; Li et al., 2024): 1) Meta-learning, 2) Knowledge retrieval.
  - [Learning vs Retrieval: The Role of In-Context Examples in Regression with Large Language Models](https://aclanthology.org/2025.naacl-long.417.pdf)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
  - [On Understanding Attention-Based In-Context Learning for Categorical Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25u/wang25u.pdf)
- **Reversal curse** (construct), 1 paper
  > Nevertheless, the Reversal Curse demonstrates a failure of meta-learning.
  - [The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”](https://proceedings.iclr.cc/paper_files/paper/2024/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf)
- **Task learning** (construct), 1 paper
  > This task inference ability is recognized as a form of meta-learning (Min et al., 2022a). (Section 1)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
