# Constraint adherence
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Constraint following, Constraint satisfaction  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this behavior as producing outputs that obey explicit rules or requirements in the prompt or task. Most definitions focus on compliance that can be checked directly, such as plans whose actions satisfy stated constraints, responses that meet formatting, structural, or stylistic rules, or solutions that respect prohibitions like not using a particular technique; a smaller line of work phrases it as a latent ability to satisfy multiple design constraints at once, including component usage, efficiency, output voltage, and feasibility. Success is therefore framed in domain-specific terms, from avoiding illegal actions and unsatisfied goals to obeying answer-length or other structural restrictions.

**Variants.** Papers also use nearby labels such as constraint following and constraint satisfaction. The behavior is studied in several settings: planning, where agents are expected to generate plans that reference and obey prompt constraints, with failures described as unmet preconditions in BlocksWorld and unfulfilled hard constraints in TravelPlanner; crosswords, where the relevant constraints are answer length and character overlaps; code generation, where authors incrementally add new denial-style restrictions to force new strategies; prompt-conditioned response generation, where verifiable requirements can include formatting or stylistic rules such as alliteration; and circuit topology generation, where outputs are expected to satisfy component-pool, efficiency, and output-voltage constraints.

**Space of elicitation and scores.** Only one measurement instrument is linked to it, Blocksworld, a planning benchmark in which agents execute actions from an initial state to a goal state and all actions must adhere to prompt-defined constraints. Beyond that named instrument, papers operationalize the behavior by checking whether plans violate constraints and become illegal or leave goals unsatisfied, whether crossword answers obey length limits, whether responses satisfy verifiable formatting or stylistic rules, and whether generated code follows denial-prompted restrictions.

**What it is taken as evidence of.** It is linked to two constructs, with different kinds of claims rather than a single shared interpretation. One paper reports that Constraint adherence is related to Length control ability, describing adherence to length constraints as a component of crossword solving, while another paper claims a causal relationship from Model selection ability to Constraint adherence, saying that balancing model capabilities, licensing requirements, resource constraints, and performance metrics in model selection aligns execution with task requirements and practical considerations.

## Sources

**Constraint adherence** (3 papers: [AUTOCIRCUIT-RL: Reinforcement Learning-Driven LLM for Automated Circuit Topology Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vijayaraghavan25a/vijayaraghavan25a.pdf), [Revealing the Barriers of Language Agents in Planning](https://aclanthology.org/2025.naacl-long.93.pdf), [Language Models are Crossword Solvers](https://aclanthology.org/2025.naacl-long.104.pdf))
> The latent ability of the model to generate outputs that satisfy multiple, specified design constraints such as component usage, efficiency, and output voltage.

**Constraint following** (1 paper: [Benchmarking Language Model Creativity: A Case Study on Code Generation](https://aclanthology.org/2025.naacl-long.141.pdf))
> The observable behavior of adhering to explicitly stated prohibitions or requirements when generating a solution, such as not using a specific programming technique.

**Constraint satisfaction** (1 paper: [A Systematic Examination of Preference Learning through the Lens of Instruction-Following](https://aclanthology.org/2025.naacl-long.552.pdf))
> The observable behavior of a model generating responses that meet specific, verifiable requirements such as formatting, structural, or stylistic rules defined in the prompt.

## Relationships

### Constraint adherence →
- **Blocksworld** (measurement instrument): *measured_by*, 1 paper
  > BlocksWorld (Valmeekam et al., 2024a) is a planning benchmark that provides a domain description, including action and constraint definitions, and requires agents to execute actions to transition from an initial state to a goal state. All actions must adhere to the constraints outlined in the prompt. (Section 3.1)
  - [Revealing the Barriers of Language Agents in Planning](https://aclanthology.org/2025.naacl-long.93.pdf)

### → Constraint adherence
- **Model selection ability** (construct): *causes*, 1 paper
  > "By balancing these factors: model capabilities, licensing requirements, resource constraints, and performance metrics, we systematically select the most suitable model for each action. This ensures that the execution of the plan is aligned with both the technical requirements of the tasks and the practical considerations of the user."
  - [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf)

### Associated with
- **Length control ability** (construct), 1 paper
  > “the ability of LLMs to adhere to length constraints, which is a critical component of solving crossword puzzles”
  - [Language Models are Crossword Solvers](https://aclanthology.org/2025.naacl-long.104.pdf)
