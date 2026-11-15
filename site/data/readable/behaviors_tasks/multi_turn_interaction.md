# Multi-turn interaction
**Type:** Behavioral indicator  
**Supporting papers:** 6  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats multi-turn interaction as carrying out a task through repeated action-observation cycles over multiple steps, often with an environment. Definitions agree on the iterative pattern: papers describe a loop that continues across turns, sometimes until a termination action or a final answer, with turns involving new observations and a response such as a thought, action, or revised solution. A smaller line of work uses the same label for interaction with critique or with a guiding model, where several rounds of prompts and responses are used to refine a solution, and one definition also emphasizes maintaining context and updating state across user-agent exchanges to achieve a goal.

**Variants.** Papers study this behavior in several settings: real-time interaction with an executable computer environment, back-and-forth exchange with a text-based environment, interaction trajectories that involve both an environment and critique, and guided rounds between a task-solving model and a separate guiding model. Across these variants, the main difference is what the model interacts with, an environment, a critique process, another model, or a user, and how turns are described, for example as observation-thought-action cycles or as user-agent exchanges. Some authors also pair the term with multi-turn reasoning and interactive capabilities.

**Space of elicitation and scores.** Only one measurement instrument is linked to this behavior, MINT. One paper adopts MINT for multi-turn evaluation and limits that use to coding and math problems, and no other instrument is linked to it in these papers.

**What it is taken as evidence of.** No paper links this behavior to a construct, so it is not explicitly used as evidence of a named construct in the surveyed work.

## Sources

**Multi-turn interaction** (5 papers: [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/file/c2f71567cd53464161cab3336e8fc865-Paper-Datasets_and_Benchmarks_Track.pdf), [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf), [CodeSteer: Symbolic-Augmented Language Models via Code/Text Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25x/chen25x.pdf), [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://aclanthology.org/2025.emnlp-main.152.pdf), [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf))
> Carrying out a task through repeated action-observation cycles over multiple steps in a computer environment.

## Relationships

### Multi-turn interaction →
- **MINT** (measurement instrument): *measured_by*, 1 paper
  > For multi-turn evaluation, we adopt MINT (Wang et al., 2023b) and only consider the coding and math problems.
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
