# Model selection ability
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Algorithm selection, Model selection  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing framing is a context-dependent selection capacity: papers describe either a latent mechanism or an ability by which a model chooses the most suitable function, algorithm, or function class from candidates using the task, data, or context. One study says ICL can automatically select the best pretraining functions according to the downstream context, which matches the view of selection among pre-trained capabilities. A smaller usage applies the same label to identifying the optimal LLM from candidate models for downstream tasks under resource constraints, so the main variation is whether selection is over internal functions or over whole models.

**Space of facets.** Papers use the nearby labels algorithm selection and model selection for closely related content, both centered on choosing among alternatives in context. The function-level usage ranges from selecting among pretraining functions to model selection between different function class families. One paper further treats algorithm selection as involving parallel preferences, explicitly including low-test-error preference.

**Space of measurement.** No measurement instrument is linked to this construct. Instead, it is linked to two behavioral indicators, Action selection and Constraint adherence, and the operationalization is behavioral: deciding which tasks to perform, in what order, and which model is most suitable for each task, or selecting models by balancing capabilities, licensing requirements, resource constraints, and performance metrics. These uses stay close to the definitions' emphasis on choosing among alternatives in context, but they are presented as related behaviors and a causal claim rather than as formal measures.

**Links.** Papers mainly connect the construct to adjacent preferences and decision behaviors. Low-test-error preference is reported as related to model selection ability, with one paper describing algorithm selection as including that preference; Action selection is also related, in work where an agent chooses which restoration tasks to perform, their order, and which model suits each task. A separate paper claims a causal relationship from Model selection ability to Constraint adherence, stating that selecting the most suitable model for each action by balancing capabilities, licensing requirements, resource constraints, and performance metrics ensures execution aligns with the technical requirements of the tasks and the practical considerations of the user; no correlational link is reported.

## Sources

**Algorithm selection** (1 paper: [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf))
> The latent mechanism by which a model, when faced with a new task, selects and implements the most suitable function or algorithm from its repertoire of pre-trained capabilities.

**Model selection** (1 paper: [Selective induction Heads: How Transformers Select Causal Structures in Context](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf))
> The ability of a model to choose the best-fitting model or function class from a set of candidates based on the provided data or context.

## Relationships

### Model selection ability →
- **Constraint adherence** (behavioral indicator): *causes*, 1 paper
  > "By balancing these factors: model capabilities, licensing requirements, resource constraints, and performance metrics, we systematically select the most suitable model for each action. This ensures that the execution of the plan is aligned with both the technical requirements of the tasks and the practical considerations of the user."
  - [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf)

### Associated with
- **Action selection** (behavioral indicator), 1 paper
  > RestoreAgent can provide the best decisions, including which image restoration tasks need to be performed, the order of their execution, and which model is most suitable for each task. (Section 3.2.1)
  - [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf)
- **Low-test-error preference** (construct), 1 paper
  > “we theoretically reveal the algorithm-selection mechanism for ICL. We find there simultaneously exist two parallel mechanisms: the Low-test-error preference and the Similar-input-distribution preference.”
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
