# Long-horizon task completion
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Composite task solving, Sequential task completion  

## State of the Field

**Space of definitions.** Across definitions, the shared framing is successful completion of an ordered, multi-stage task rather than a single step: papers describe sequences of distinct subtasks or goals that must be carried out in order, and one definition makes progression explicitly depend on prior task success. Success is described as finishing the whole sequence, for example by completing six distinct tasks that each contain at least five subtasks or by completing up to five language instructions consecutively. A smaller variation uses broader goal-based wording, describing multi-stage tasks that combine goals such as reaching locations, collecting items, and surviving until a final objective.

**Variants.** Papers use several nearby names for this behavior, including long-horizon task completion, composite task solving, and sequential task completion. The settings vary from a robot carrying out consecutive language instructions to an agent handling composite game goals tied to location and game status, with examples such as finding the entrance to the Gnomish Mines, ascending back to the main branch, and then traveling toward Delphi. Another formulation presents it as six distinct long-horizon tasks, each composed of at least five subtasks.

**Space of elicitation and scores.** No measurement instrument is linked to it. In the papers' own operationalizations, scoring is still success-based: one study labels the outcome as "Task Completed in a Sequence (Success Rate)," and another evaluates it by successful completion of six distinct tasks, each with at least five subtasks. Across these descriptions, the behavior is elicited as an ordered sequence and scored by whether that sequence is completed successfully.

**What it is taken as evidence of.** Papers do not explicitly treat this behavior as evidence of a construct. The only linked construct is planning, and one paper claims a causal relationship from planning to long-horizon task completion in the context of complex tasks. The same line of work also links one behavioral indicator, self-reflection, with a claimed causal relationship to long-horizon task completion, arguing that failure on any sub-goal halts later ones and that reflection is used to identify and rectify errors promptly.

## Sources

**Long-horizon task completion** (1 paper: [VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions](https://proceedings.neurips.cc/paper_files/paper/2024/file/8e6f3d53b2bef98fce17e699557f5f11-Paper-Conference.pdf))
> The observable execution of a complex task that requires completing a sequence of multiple, distinct subtasks in a specific order.

**Composite task solving** (1 paper: [MaestroMotif: Skill Design from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/2dc5a0faac8102fd47363795f71126ee-Paper-Conference.pdf))
> Completing multi-stage tasks that require sequencing several goals over time, such as reaching locations, collecting items, and surviving until a final objective is met.

**Sequential task completion** (1 paper: [Vision-Language Foundation Models as Effective Robot Imitators](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf))
> Successfully executing a chain of up to five language-instructed tasks in sequence, where progression depends on prior task success.

## Relationships

### → Long-horizon task completion
- **Planning** (construct): *causes*, 1 paper
  > Relevant studies indicate that the human brain is essential for planning and reflection, while the cerebellum controls low-level actions, both crucial for complex tasks [40, 41]. (Section 2.2)
  - [Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > The failure of any sub-goal halts the execution of subsequent ones, leading to overall task failure. Therefore, a reflection module is essential to identify and rectify errors promptly. (Section 2.2)
  - [Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf)
