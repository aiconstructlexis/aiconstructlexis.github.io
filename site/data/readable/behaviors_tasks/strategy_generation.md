# Strategy generation
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Anticipatory plan generation, Code-form plan generation, Strategy formulation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is the production of a high-level plan or strategy in language before later solution steps, most often before answering or before generating code. Definitions converge on abstract solution paths rather than detailed calculations or specific operations: papers describe multiple strategies in English, a plan that rehearses the whole reasoning path, or an open-ended strategy proposed from the goal, interaction history, prior strategies, and latest observation. A smaller usage frames the behavior as generating natural language criteria or strategies for classifying user satisfaction.

**Variants.** Papers study several named variants: anticipatory plan generation, code-form plan generation, and strategy formulation. These variants differ mainly in form and setting, including natural language plans for coding problems, pseudocode-style plans that summarize high-level reasoning structure, abstract ideas that identify relevant concepts and principles, and strategy generation for dialogue-based user satisfaction classification. Some formulations ask for multiple candidate strategies, while others ask for one intended solution path before the answer.

**Space of elicitation and scores.** No measurement instrument is linked to it. The descriptions instead show elicitation through prompts that ask for high-level strategies first, multiple strategies in English, or an abstract plan before answering.

**What it is taken as evidence of.** Papers connect this behavior to two constructs, and they do not converge on a single target construct. The more common link is a claimed causal relationship from strategy generation to Reasoning, with papers describing strategy generation as enhancing reasoning ability or enabling models to tackle coding problems using reasoning capabilities. A smaller line of work claims a causal relationship from strategy generation to Sequential decision-making, reporting better performance on decision-making tasks when responses are generated with planning rather than directly.

## Sources

**Strategy generation** (3 papers: [LLM-guided Plan and Retrieval: A Strategic Alignment for Interpretable User Satisfaction Estimation in Dialogue](https://aclanthology.org/2025.naacl-long.523.pdf), [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf), [EPO: Explicit Policy Optimization for Strategic Reasoning in LLMs via Reinforcement Learning](https://aclanthology.org/2025.acl-long.747.pdf))
> Producing high-level natural language plans or approaches for solving a coding problem before generating code.

**Anticipatory plan generation** (1 paper: [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf))
> Producing a high-level plan before answering that outlines the intended solution path without detailed calculations.

**Code-form plan generation** (1 paper: [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf))
> Producing pseudocode-style plans that summarize the high-level reasoning structure for solving a prompt.

**Strategy formulation** (1 paper: [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf))
> The observable behavior of generating high-level plans or abstract ideas for solving a problem, including identification of relevant concepts and principles without detailing specific operations.

## Relationships

### Strategy generation →
- **Reasoning** (construct): *causes*, 2 papers
  > These S+ and S−guide the generation of new strategies to optimize overall performance, enhancing reasoning ability and avoiding redundancy. (Section 3.1.1)
  - [LLM-guided Plan and Retrieval: A Strategic Alignment for Interpretable User Satisfaction Estimation in Dialogue](https://aclanthology.org/2025.naacl-long.523.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
- **Sequential decision-making** (construct): *causes*, 1 paper
  > CODEPLAN consistently and significantly outperforms directly generating responses without planning, yielding a relative 25.1% performance gain averaged across 13 challenging reasoning benchmarks spanning mathematical reasoning, symbolic reasoning, instruction-following, multi-hop question answering, and decision-making tasks.
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
