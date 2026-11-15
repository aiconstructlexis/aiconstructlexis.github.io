# Task learning
**Type:** Construct  
**Supporting papers:** 7  
**Also known as:** Task inference  

## State of the Field

**Space of definitions.** Most definitions treat task learning as learning how to perform a task from in-context demonstrations by learning the input-label mapping, often phrased as solving the target task solely from demonstrations. A minority framing further specifies this as inferring and applying new mappings that were not seen during pre-training. A smaller line of work uses the label task inference and defines the construct as deducing the abstract task or class-to-label rule from input-output examples in context, explicitly contrasting this with simply copying a label.

**Space of facets.** Systematization is mostly by contrast. Papers distinguish it from task recognition, and one formulation also contrasts inferring the task from context with simply copying a label. The naming is not fully uniform: most authors use task learning, while some use task inference for inferring the underlying task from examples, and one paper describes that inference ability as a form of meta-learning.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. The operational descriptions stay at the level of task performance: solving a target task from demonstrations alone, inferring the underlying task from example pairs, or, in one study, showing gains above NON-BIJECTIVE shuffles as indicative of task learning rather than task recognition. Another paper frames the target behavior as inferring and applying new input-label mappings not seen during pre-training.

**Links.** It is linked to 3 constructs: In-context learning, Meta-learning, and Task recognition. Papers describe it as related to In-context learning, with one account of effective ICL saying the model infers the underlying task from examples and refines predictions based on that inferred task, and as related to Meta-learning, with task inference ability described as a form of meta-learning. It is also reported to correlate with Task recognition, and one paper states that their performance changes in opposite directions.

## Sources

**Task learning** (2 papers: [Investigating the Pre-Training Dynamics of In-Context Learning: Task Recognition vs. Task Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/83d349b6eb8125588b5f091e2d47525c-Paper-Conference.pdf), [ICL CIPHERS: Quantifying “Learning” in In-Context Learning via Substitution Ciphers](https://aclanthology.org/2025.emnlp-main.1316.pdf))
> The ability of a language model to learn how to perform a task solely by learning the input-label mapping from the provided in-context demonstrations.

**Task inference** (1 paper: [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf))
> The model's capacity to deduce the abstract rule or mapping (e.g., class-to-label function) from a set of input-output examples provided in context.

## Relationships

### Task learning →
- **Task recognition** (construct): *correlates*, 1 paper
  > “the performance of task recognition and task learning changes in the opposite direction”
  - [Investigating the Pre-Training Dynamics of In-Context Learning: Task Recognition vs. Task Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/83d349b6eb8125588b5f091e2d47525c-Paper-Conference.pdf)

### Associated with
- **In-context learning** (construct), 1 paper
  > In effective ICL, the model infers the underlying task from the examples provided and refines its predictions based on the inferred task. (Section 2.1)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
- **Meta-learning** (construct), 1 paper
  > This task inference ability is recognized as a form of meta-learning (Min et al., 2022a). (Section 1)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
