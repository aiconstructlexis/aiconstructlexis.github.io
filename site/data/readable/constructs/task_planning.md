# Task planning
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Problem decomposition  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing framing treats task planning as decomposing a high-level goal or natural-language instruction into a sequence of executable actions, skills, or steps, usually at mid-level or low-level granularity. A smaller line of work describes it as formulating and refining action sequences in an interactive environment, or as close-loop planning that updates the plan from real-time observations while pursuing a goal. A separate position paper uses the nearby label problem decomposition for a latent ability of a system design to break complex tasks into independently solvable subproblems, explicitly tying that ability to asymptotic improvements in computational cost.

**Space of facets.** Papers mainly differentiate the construct by plan granularity and planning mode. Some describe sequences of mid-level actions or skills, others use low-level skills or steps, and one paper singles out close-loop task planning as generating a plan while adapting it to observations. The neighboring terms task decomposition, request decomposition, and problem decomposition appear as related decomposition stages or abilities, and no other constructs are linked to task planning.

**Space of measurement.** The linked measurement space is narrow: papers connect task planning to 2 measurement instruments, RestBench and TaskBench, and both are benchmarks. In this benchmark-based operationalization, task planning is instantiated through performance on benchmark task suites, including HuggingFace, Multimedia, and Daily Life API tasks from TaskBench and TMDB API tasks from RestBench. Papers also link it to 1 behavioral indicator, Task decomposition, but that connection is recorded as a related behavior rather than as a measurement instrument.

**Links.** No causal or correlational relationships are claimed. One paper reports that Task decomposition is related to Task planning, describing an LLM-based planning setup in which request decomposition comes first, breaking an ambiguous user request into concrete steps.

## Sources

**Task planning** (4 papers: [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf), [Tree-Planner: Efficient Close-loop Task Planning with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d53538ba21c05fa361d2b21704172753-Paper-Conference.pdf), [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf), [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://aclanthology.org/2025.acl-long.277.pdf))
> The ability to decompose a high-level goal into a sequence of executable mid-level actions or skills.

**Problem decomposition** (1 paper: [Position: Scaling LLM Agents Requires Asymptotic Analysis with LLM Primitives](https://raw.githubusercontent.com/mlresearch/v267/main/assets/meyerson25a/meyerson25a.pdf))
> The latent ability of a system design to break down complex tasks into smaller, independently solvable subproblems, enabling asymptotic improvements in computational cost.

## Relationships

### Task planning →
- **TaskBench** (measurement instrument): *measured_by*, 1 paper
  > We utilize four datasets across two task planning benchmarks: HuggingFace tasks, Multimedia tasks, and Daily Life API tasks from TaskBench [45], as well as TMDB API tasks from RestBench [50]. (Section 5.1)
  - [Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf)
- **RestBench** (measurement instrument): *measured_by*, 1 paper
  > We utilize four datasets across two task planning benchmarks: HuggingFace tasks, Multimedia tasks, and Daily Life API tasks from TaskBench [45], as well as TMDB API tasks from RestBench [50]. (Section 5.1)
  - [Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf)

### Associated with
- **Task decomposition** (behavioral indicator), 1 paper
  > The current solution of task planning is purely based on LLMs and involves two stages [45, 46]. The first stage involves request decomposition, where a user’s ambiguous request is broken down into concrete steps via LLMs. (Section 2.2)
  - [Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf)
