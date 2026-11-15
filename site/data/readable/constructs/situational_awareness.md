# Situational awareness
**Type:** Construct  
**Supporting papers:** 9  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats situational awareness as a model's knowledge of itself and its circumstances, especially self-knowledge, the ability to infer its situation, and the capacity to act on that knowledge. As one study puts it, a model is situationally aware to the extent that it has "self-knowledge", can make "inferences" about its situation, and takes "actions" on that basis (Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs). Other papers define the same term in terms of perceiving and understanding operational context and the implications of a model's state, using knowledge about itself, its training context, and human supervisors to inform behavior, including recognizing evaluation or deployment, or perceiving environmental cues and other characters' behaviors, emotions, and intentions in dialogue. A smaller line of work places it in stepwise reasoning, defining it as the capacity to integrate contextual signals from the environment and internal reasoning state when weighting uncertainty across steps, so the main disagreement is over what counts as the relevant "situation": the model's own identity and training context, its operational context, a dialogue scene, or the current reasoning trajectory.

**Space of facets.** The most explicit decomposition breaks the construct into self-knowledge, situational inferences, and actions based on that knowledge. Other papers systematize it differently: one dialogue-focused paper represents it as "SA = ⟨EP, BA, EA, IA⟩" formed through hierarchical perception and interpretation, while another specifies knowledge about itself, its training context, physical implementation, and how human supervisors are likely to respond to its behavior. Papers also place it near neighboring constructs rather than using a single boundary, relating it to self-awareness and situational inference, treating self-recognition as an instance of situational awareness, and noting that it "should not be confused with notions of awareness in philosophy or psychology" (The Alignment Problem from a Deep Learning Perspective).

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. Even without linked measures, papers often describe behavioral operationalizations: they ask whether a model knows which entity it is, can infer its situation, and acts on that knowledge, and one paper explicitly says the construct can be behaviorally tested. Other operationalizations appear inside methods rather than linked measures, for example assigning situational weights to uncertainty at each reasoning step or modeling situational awareness through hierarchical perception in dialogue.

**Links.** Papers link situational awareness to four constructs. It is related to situational inference and self-awareness in definitions that build it from inferences about the situation and self-knowledge, and one paper says self-recognition can be seen as an instance of situational awareness. Separately, one paper claims a causal relationship from situational awareness to persona consistency, reporting that jointly modeling external situational awareness and internal self-awareness generates responses with improved character consistency.

## Sources

**Situational awareness** (5 papers: [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf), [An Auditing Test to Detect Behavioral Shift in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7af140f516c9f57050f7359bf53bc8f0-Paper-Conference.pdf), [Uncertainty Propagation on LLM Agent](https://aclanthology.org/2025.acl-long.302.pdf), [CogDual: Enhancing Dual Cognition of LLMs via Reinforcement Learning with Implicit Rule-Based Rewards](https://aclanthology.org/2025.emnlp-main.1389.pdf), [The Alignment Problem from a Deep Learning Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e58b1bf9f218fcd19e4539e982752a5-Paper-Conference.pdf))
> The model's knowledge of itself and its circumstances, which includes self-knowledge, the ability to make inferences about its situation, and the capacity to act on this knowledge.

## Relationships

### Situational awareness →
- **Persona consistency** (construct): *causes*, 1 paper
  > By jointly modeling external situational awareness and internal self-awareness, CogDual generates responses with improved character consistency and contextual alignment.
  - [CogDual: Enhancing Dual Cognition of LLMs via Reinforcement Learning with Implicit Rule-Based Rewards](https://aclanthology.org/2025.emnlp-main.1389.pdf)

### Associated with
- **Situational inference** (construct), 1 paper
  > “Our definition builds on recent work ... (2) M can make deductions/inferences about its situation (inferences)”
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-recognition** (construct), 1 paper
  > Self-recognition can be seen as an instance of situational awareness, which has long been noted as a potential point of risk for AI (Cotra, 2021).
  - [Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct](https://proceedings.iclr.cc/paper_files/paper/2025/file/d560f94c582033e6d8eb0c97cdd4f721-Paper-Conference.pdf)
- **Self-awareness** (construct), 1 paper
  > A model M is situationally aware to the extent that (1) M knows which entity it is and knows facts about itself (self-knowledge), (2) M can make deductions/inferences about its situation (inferences), and (3) M acts on the basis of this knowledge (actions). (Section 2.1).
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
