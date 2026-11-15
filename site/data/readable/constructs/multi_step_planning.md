# Multi-step planning
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Natural planning, Step-by-step planning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats multi-step planning as choosing, producing, or executing an ordered sequence of actions, subgoals, or subtasks over multiple steps to reach a goal. Several descriptions make the long horizon explicit, stressing step-by-step planning toward a goal and noting that early decisions can affect later steps or future outcomes. A smaller line of work uses the name natural planning for a closely related idea, framing it as decomposing an input problem into an ordered sequence of intermediate subgoals that guide solution generation and explicitly separating it from classical AI planning.

**Space of facets.** Papers mainly organize the construct around decomposition into subgoals: one related construct is Task decomposition, and some descriptions define planning itself as creating a plan by decomposing a task into sub-goals or sub-tasks and then iteratively executing each sub-task. The clearest naming distinction is between multi-step planning and natural planning, with the latter used for the subgoal-decomposition framing and contrasted with classical AI planning. In benchmark-oriented descriptions, multi-step planning also appears alongside pathfinding, logic skills, spatial navigation, rule understanding, and constraint satisfaction.

**Space of measurement.** Operationalization centers on one measurement instrument, SPaRC, and one behavioral indicator, Task decomposition. SPaRC is a reasoning challenge that measures multi-step planning through long-term, step-by-step path planning, where errors earlier in the reasoning chain can affect later steps. The linked behavioral indicator captures the construct as decomposing an input problem into an ordered sequence of intermediate subgoals, so the operationalizations mostly match the decomposition and extended-horizon definitions.

**Links.** Beyond measurement, one paper reports that multi-step planning is related to Task decomposition, using decomposition into ordered intermediate subgoals as the shared formulation. One paper also claims a causal relationship from multi-step planning to Complex reasoning, stating that planning trajectories improve complex reasoning capabilities.

## Sources

**Multi-step planning** (2 papers: [MONA: Myopic Optimization with Non-myopic Approval Can Mitigate Multi-step Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/farquhar25a/farquhar25a.pdf), [Can LLMs Help You at Work? A Sandbox for Evaluating LLM Agents in Enterprise Environments](https://aclanthology.org/2025.emnlp-main.466.pdf))
> Selecting a sequence of actions across multiple steps to achieve a goal or manipulate future outcomes.

**Natural planning** (1 paper: [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1087.pdf))
> The ability to decompose a problem into an ordered sequence of intermediate subgoals that guide solution generation.

## Relationships

### Multi-step planning →
- **SPaRC** (measurement instrument): *measured_by*, 1 paper
  > Empirically, SPaRC reveals critical limitations in current reasoning models regarding spatial reasoning, rule-based reasoning, multi-step planning, and constraint satisfaction. (Section 5)
  - [SPaRC: A Spatial Pathfinding Reasoning Challenge](https://aclanthology.org/2025.emnlp-main.526.pdf)
- **Complex reasoning** (construct): *causes*, 1 paper
  > Our detailed analysis demonstrates how planning trajectories improves complex reasoning capabilities, showing that PLAN-TUNING is an effective strategy for improving task-specific performance of smaller LLMs. (Abstract)
  - [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1087.pdf)

### Associated with
- **Task decomposition** (behavioral indicator), 1 paper
  > In this work, we formalize natural planning—distinct from classical AI planning (which is not the focus of this work)—as the process of decomposing an input problem x into an ordered sequence of intermediate subgoals that guide its solution. (Section 3.1)
  - [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1087.pdf)
