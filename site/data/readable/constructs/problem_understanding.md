# Problem understanding
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Problem comprehension  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this as an ability, often a latent one, to understand a task or problem statement and its relevant context. In code generation work, it is framed narrowly as comprehending the requirements and repository-level context of a code generation task, while mathematical reasoning papers use the near-synonym "problem comprehension" for understanding the semantic content, structure, quantities, relationships, and given conditions of a math problem, including separating relevant from irrelevant information and noticing missing or contradictory conditions.

**Space of facets.** Some authors present it as a stage in solving a problem: one paper says the "problem comprehension stage" involves analyzing word semantics, text structure, and given conditions, and another treats failures as "problem comprehension errors". Within the math framing, robust understanding is described as preserving the problem's meaning despite changes in wording or sentence structure, whereas the code generation framing centers on leveraging stronger models' "problem-understanding capabilities" to augment context. Across papers, the same family of terms is used for both repository-level coding tasks and mathematical problem solving, with the clearest variation being domain and scope.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. The recorded use therefore stays at the level of task descriptions, such as accurate variable definition and extraction of relevant information from a math problem, robustness to wording changes, understanding given conditions, and comprehension of repository-level requirements and context.

## Sources

**Problem understanding** (1 paper: [An Empirical Study on Strong-Weak Model Collaboration for Repo-level Code Generation](https://aclanthology.org/2025.emnlp-main.1043.pdf))
> The latent ability of a model to comprehend the requirements and context of a code generation task, particularly at the repository level.

**Problem comprehension** (2 papers: [Parrot: A Training Pipeline Enhances Both Program CoT and Natural Language CoT for Reasoning](https://aclanthology.org/2025.emnlp-main.1366.pdf), [CogMath: Assessing LLMs’ Authentic Mathematical Ability from a Human Cognitive Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ab/liu25ab.pdf))
> The ability to understand and extract relevant information from a mathematical problem statement, including identifying key quantities and relationships.
