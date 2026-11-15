# Metacognition
**Type:** Construct  
**Supporting papers:** 13  
**Also known as:** Introspection, Meta-cognition, Metacognitive abilities, Meta-cognitive reasoning, Metacognitive capabilities, Metacognitive capability, Cognitive reflection, Metacognitive monitoring, Meta-reflection, Intrinsic metacognitive learning  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage treats metacognition as a higher-order, usually latent capacity for self-assessment, self-monitoring, and self-regulation: models assess their own knowledge and limitations, monitor reasoning, self-verify outputs, reason about uncertainty, and sometimes model their own competence or learning progress. A smaller line uses the narrower label introspection, defined as access to facts about the model itself, or to internal representations, that cannot be derived from training data alone. The main disagreement is about scope, from checking the correctness of current answers or deciding whether to use tools, to broader abilities for planning learning, applying prior insights, or recognizing patterns across repeated feedback cycles.

**Space of facets.** The terminology is not stable. Papers use metacognition alongside, and sometimes in place of, introspection, self-awareness, self-knowledge, self-reflection, cognitive reflection, meta-reasoning, meta-reflection, and metacognitive monitoring; within these families, narrower facets include capability awareness, awareness of knowledge limits, self-awareness of reasoning boundaries, and competence or learning-progress monitoring. A recurring split is between local monitoring, such as step-error awareness, correcting one's own generation, or self-verification, and broader regulation, such as selecting external tools, guiding curriculum learning, or adapting learning plans over time.

**Space of measurement.** No measurement instrument is linked to metacognition; papers link it instead to 2 behavioral indicators, Clarifying question generation and Self-verification. Beyond those links, papers describe bespoke benchmark-style tasks and probes rather than a recurring instrument: INTROSPECT tasks for gaining information about oneself through "internal" mechanisms, observation tasks that score the correctness of reasoning steps from internal states, and task settings where models choose tools, refuse or abstain under contradictory definitions, or predict their own competence and learning progress. These operationalizations usually match the dominant self-assessment and regulation framing, though the introspection version is narrower because it asks for access to self-facts rather than only better task behavior.

**Links.** Across the cited papers, causal claims run from Metacognition to Clarifying question generation, Self-improvement, and Task generalization. Related links connect Metacognition with Self-awareness and Self-verification, and one paper also relates Calibration to Metacognition by arguing that calibrated self-predictions would be evidence of introspection. No correlational link is reported.

## Sources

**Introspection** (2 papers: [Looking Inward: Language Models Can Learn About Themselves by Introspection](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf), [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability of a model to access and report facts about itself that cannot be logically or inductively derived from its training data alone.

**Meta-cognition** (1 paper: [Adaptive Tool Use in Large Language Models with Meta-Cognition Trigger](https://aclanthology.org/2025.acl-long.655.pdf))
> The latent ability of an LLM to assess and regulate its own knowledge and limitations, enabling informed decisions about whether to rely on internal knowledge or external tools.

**Metacognition** (1 paper: [What Makes a Good Natural Language Prompt?](https://aclanthology.org/2025.acl-long.292.pdf))
> The model's ability to self-monitor its own cognitive processes, including reasoning and self-verification of its outputs to ensure correctness and reliability.

**Metacognitive abilities** (1 paper: [Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf))
> The model's capacity to leverage higher-order thinking, such as applying insights from prior experiences to new problems.

**Meta-cognitive reasoning** (1 paper: [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf))
> The ability to reason about one’s own generative uncertainty and identify which questions best distinguish among candidate solutions.

**Metacognitive capabilities** (1 paper: [LLMs Don't Know Their Own Decision Boundaries: The Unreliability of Self-Generated Counterfactual Explanations](https://aclanthology.org/2025.emnlp-main.1231.pdf))
> Higher-order cognitive abilities related to a model's awareness and understanding of its own knowledge and reasoning processes.

**Metacognitive capability** (1 paper: [Do LLMs Adhere to Label Definitions? Examining Their Receptivity to External Label Definitions](https://aclanthology.org/2025.emnlp-main.1648.pdf))
> The latent ability of an LLM to detect inconsistencies or contradictions in input instructions and respond with self-monitoring behaviors such as abstention or refusal to answer.

**Cognitive reflection** (1 paper: [ThinkTuning: Instilling Cognitive Reflections without Distillation](https://aclanthology.org/2025.emnlp-main.1592.pdf))
> The latent tendency to engage in self-reflective thinking, including questioning initial responses and considering alternative reasoning paths.

**Metacognitive monitoring** (1 paper: [MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gaven25a/gaven25a.pdf))
> The latent ability of an LLM agent to model its own competence and learning progress across goals by leveraging semantic relationships, enabling self-directed curriculum learning.

**Meta-reflection** (1 paper: [Reflection-Bench: Evaluating Epistemic Agency in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cu/li25cu.pdf))
> The higher-order capacity to recognize and anticipate global patterns across multiple cycles of prediction, action, and feedback, enabling regulation beyond local adaptation.

**Intrinsic metacognitive learning** (1 paper: [Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cw/liu25cw.pdf))
> The latent capacity of an agent to autonomously and adaptively refine its learning strategies through self-assessment, self-planning, and self-evaluation, without reliance on fixed, human-designed mechanisms.

## Relationships

### Metacognition →
- **Clarifying question generation** (behavioral indicator): *causes*, 1 paper
  > Yet, generating effective clarifying questions requires LLM agents to engage in a form of meta-cognitive reasoning, an ability LLMs may presently lack.
  - [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > We argue that sustainable, generalized self-improvement requires agents to develop intrinsic metacognitive learning abilities. (Section 1)
  - [Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cw/liu25cw.pdf)
- **Task generalization** (construct): *causes*, 1 paper
  > Our approach integrates self-awareness, monitoring, evaluation, regulation, and meta-reflection, to enhance LLMs’ ability to refine reasoning strategies and generalize across tasks.
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)

### Associated with
- **Calibration** (construct), 1 paper
  > If a model’s self-predictions are calibrated with respect to its ground-truth behavior, this suggests the model takes into account information about itself that was not in its training data. This would provide further evidence of introspection. (Section 3.3)
  - [Looking Inward: Language Models Can Learn About Themselves by Introspection](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf)
- **Self-awareness** (construct), 1 paper
  > M can obtain knowledge of itself via direct access to its representations (introspection). (Section 2.1).
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-verification** (behavioral indicator), 1 paper
  > Metacognition: This assesses prompts in explicitly guiding models to reason, self-monitor, and self-verify outputs to meet expectations and enhance reliability (e.b. Wang and Zhao (2024)).
  - [What Makes a Good Natural Language Prompt?](https://aclanthology.org/2025.acl-long.292.pdf)
