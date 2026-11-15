# Self-awareness
**Type:** Construct  
**Supporting papers:** 8  
**Also known as:** Self-assessment, Writing style knowledge, Competence boundary awareness  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats self-awareness as a model’s understanding or reasoning about itself, especially its own identity, state, or existence, often as a broader target than introspection. One paper defines introspection more narrowly as access to facts about oneself that cannot be derived from training data alone, while related self-awareness tasks extend to identity- or state-directed reasoning. Other papers, often under nearby labels such as self-assessment or competence boundary awareness, use the term for evaluating one’s own knowledge, skills, strengths, weaknesses, limits, and feasible actions, and some quoted passages narrow it further to role identity and style, knowledge of the model’s own writing style, or the ability to assess and correct its own generations. The main point of variation is what the model is aware of: itself as an entity, its capabilities and limits, or the correctness and style of its outputs.

**Space of facets.** Papers break the construct into several facets rather than using a single subtype scheme. One role-playing formulation splits it into role style and role knowledge, while another self-awareness module separates capability-aware and mission-aware solvability when analyzing whether a task is feasible. The construct is also organized through nearby labels: introspection is a narrower way of obtaining facts about oneself, metacognition and self-assessment overlap with monitoring and evaluating one’s own knowledge or reasoning, and one paper places self-knowledge inside situational awareness. At the same time, the same name is used for different targets, from boundary awareness to self-verification and error correction.

**Space of measurement.** No named measurement instrument is linked to self-awareness, while 3 behavioral indicators are linked: Hallucination, Self-correction, and Self-verification. In the papers, operationalization instead appears through task framings such as accessing facts about oneself, recognizing one’s own writing style, judging capability boundaries, and assessing or correcting one’s own generation. These operationalizations mirror the split between self-knowledge, capability awareness, and error detection, rather than converging on a shared named instrument.

**Links.** Papers claim causal relationships from self-awareness to Hallucination, Self-improvement, and Persona consistency. The reported language is that introspecting an agent’s operational state lets it adapt accordingly, that self-awareness would help mitigate hallucinations and discourage attempts at unsolvable or unethical tasks, and that jointly modeling internal self-awareness with external awareness of the situation yields improved character consistency and contextual alignment. Papers also report related links from self-awareness to Self-correction and Self-verification. Beyond these, self-awareness is linked to 6 constructs overall, with 4 additional related constructs that point both toward self-awareness and outward from it; no correlational link is reported.

## Sources

**Self-awareness** (3 papers: [Looking Inward: Language Models Can Learn About Themselves by Introspection](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf), [OmniCharacter: Towards Immersive Role-Playing Agents with Seamless Speech-Language Personality Interaction](https://aclanthology.org/2025.acl-long.1276.pdf), [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf))
> A model's capacity to understand and reason about its own identity, state, or existence, tested as a potential generalization of introspection.

**Self-assessment** (1 paper: [Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cw/liu25cw.pdf))
> The ability of an agent to accurately evaluate its own knowledge, skills, strengths, and weaknesses.

**Writing style knowledge** (1 paper: [Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct](https://proceedings.iclr.cc/paper_files/paper/2025/file/d560f94c582033e6d8eb0c97cdd4f721-Paper-Conference.pdf))
> The latent knowledge of characteristics of the model’s own generated writing that supports distinguishing it from other text.

**Competence boundary awareness** (1 paper: [Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents](https://aclanthology.org/2025.emnlp-main.249.pdf))
> The ability of an agent to analyze task flows and environmental states to determine its own feasible actions, recognize its limitations, and identify when help is needed.

## Relationships

### Self-awareness →
- **Self-improvement** (construct): *causes*, 1 paper
  > By introspecting these elements, the agent gains an understanding of its own operational state and can adapt accordingly.
  - [Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement](https://aclanthology.org/2025.acl-long.1354.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > This capability [self-awareness] would help mitigate hallucinations, discourage attempts at solving unsolvable problems, and prevent engagement in unethical tasks, ensuring more responsible and reliable behavior.
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)
- **Persona consistency** (construct): *causes*, 1 paper
  > By jointly modeling external situational awareness and internal self-awareness, CogDual generates responses with improved character consistency and contextual alignment.
  - [CogDual: Enhancing Dual Cognition of LLMs via Reinforcement Learning with Implicit Rule-Based Rewards](https://aclanthology.org/2025.emnlp-main.1389.pdf)

### Associated with
- **Honesty** (construct), 1 paper
  > Crucially, the AI should be honest about its capabilities and knowledge levels. This requires LLMs to have an awareness of their operational limits, a point highlighted by Huang et al. [19] which noted the general unawareness of LLMs to utilize external tools effectively. (Section 2)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Self-correction** (behavioral indicator), 1 paper
  > Self-awareness, i.e., the ability to assess and correct one’s generation, is a fundamental aspect of human intelligence...
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Knowledge boundary awareness** (construct), 1 paper
  > Our self-awareness module (Fig. 3) comprises two core components...: (1) assessing the task’s solvability p(ΘI) and p(ΘE), based on the model’s technic and cognitive capabilities, where capability-aware solvability and mission-aware solvability are considered simultaneously
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)
- **Self-verification** (behavioral indicator), 1 paper
  > “Self-awareness, i.e., the ability to assess and correct one’s generation”
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Situational awareness** (construct), 1 paper
  > A model M is situationally aware to the extent that (1) M knows which entity it is and knows facts about itself (self-knowledge), (2) M can make deductions/inferences about its situation (inferences), and (3) M acts on the basis of this knowledge (actions). (Section 2.1).
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Metacognition** (construct), 1 paper
  > M can obtain knowledge of itself via direct access to its representations (introspection). (Section 2.1).
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
