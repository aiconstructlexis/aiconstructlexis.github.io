# Action prediction
**Type:** Behavioral indicator  
**Supporting papers:** 25  
**Also known as:** Next-action prediction, Action sequence prediction, Chess move selection  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a next-step decision task in an interaction sequence: authors describe predicting or generating the next appropriate action needed to pursue a larger goal, often by identifying both the target element and the operation. As one study puts it, the output includes "a target element to interact with, along with the operation, such as click, type, or select an option" (A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis). Most formulations condition on the current webpage, screen, GUI state, or state plus prior actions or transitions, and success is commonly framed as agreement with the ground-truth next action; a smaller line of work requires the full predicted action sequence to align with human trajectories, and an isolated use casts it as selecting a legal chess move, including a checkmating move.

**Variants.** Papers use several nearby names, most often action prediction and next-action prediction, with action sequence prediction as a stricter sequential variant and chess move selection as a specialized case. The most common settings are web and UI interaction, including webpage tasks, UI screens with previous action history, GUIDE, and GUI-state prediction. Other variants appear in offline RL trajectory formats, Alfworld navigation logs, chess scenarios, and multimodal evaluations where action prediction is one of several tasks within hallucination scenarios.

**Space of elicitation and scores.** Papers link it to one measurement instrument, Mind2Web, which is used for real-world web action prediction tasks and described as measuring generalization across tasks, websites, and domains. Beyond that explicit instrument link, scoring is usually described as comparing predicted and true actions or checking whether the next action matches test-time ground truth. In sequence formulations, task-level success is achieved only when the entire predicted trajectory aligns with the ground-truth human trajectory.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects. Instead, they connect it to three constructs in different ways: one paper claims a causal relationship from GUI understanding to action prediction, another claims a causal relationship from spatiotemporal reasoning to action prediction, and a separate paper relates action prediction to moral reasoning by treating it as one of that work's core concepts. Separately, one paper relates action prediction to hallucination by including it among the tasks used in hallucination scenarios.

## Sources

**Action prediction** (5 papers: [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf), [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf), [Decomposed Prompt Decision Transformer for Efficient Unseen Task Generalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/de18052eb17cce56554a9637dd5aadba-Paper-Conference.pdf), [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf), [In-Context Reinforcement Learning From Suboptimal Historical Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25d/dong25d.pdf))
> The task of determining and generating the next appropriate action (e.g., which element to click, what text to type) in a sequence to accomplish a larger goal.

**Next-action prediction** (2 papers: [Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf), [Latent Factor Models Meets Instructions: Goal-conditioned Latent Factor Discovery without Task Supervision](https://aclanthology.org/2025.naacl-long.554.pdf))
> The task of predicting the next user action on a UI, given the screen and a history of previous actions.

**Action sequence prediction** (1 paper: [AdaptAgent: Adapting Multimodal Web Agents with Few-Shot Learning from Human Demonstrations](https://aclanthology.org/2025.acl-long.1008.pdf))
> Generating a correct sequence of actions (element selection and operation) that aligns with the ground-truth human trajectory to achieve task success.

**Chess move selection** (1 paper: [Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf))
> Choosing a legal chess move that best advances the position, including identifying a checkmating move.

## Relationships

### Action prediction →
- **Mind2Web** (measurement instrument): *measured_by*, 2 papers
  > It provides action prediction tasks that measure the generalization of LLMs across the tasks, websites, and their domains (e.g. travel, shopping) (Section 4.2).
  - [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)
  - [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf)

### → Action prediction
- **Spatiotemporal reasoning** (construct): *causes*, 1 paper
  > we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models’ spatial-temporal awareness for action prediction by encoding state-action trajectories visually. (ABSTRACT)
  - [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf)
- **GUI understanding** (construct): *causes*, 1 paper
  > Action Prediction builds on these skills, testing whether agents can execute interactions like clicking, dragging, and typing based on their UI understanding
  - [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nayak25a/nayak25a.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > Our benchmark encompasses six novel hallucination scenarios ... each covering ﬁve different tasks, i.e. object recognition, counting, attribute recognition, spatial reasoning, and action prediction.
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **Moral reasoning** (construct), 1 paper
  > While numerous tasks can be accomplished using UNIMORAL, we focus on four core concepts of moral reasoning: [I] Action Prediction (AP)... (Section 4)
  - [Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral](https://aclanthology.org/2025.acl-long.294.pdf)
