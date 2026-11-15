# Self-reflection
**Type:** Behavioral indicator  
**Supporting papers:** 86  
**Also known as:** Self-feedback, Reflection on failure cases, Short-term reflection, Long-term reflection, Reflection, Reflection generation, Reflection step generation, Self-QA reflection, Error reflection, Self-reflection generation, Verbal reflection  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is an iterative review of the model's own prior outputs, reasoning steps, actions, or failures, usually to identify what went wrong and produce feedback, a correction, or a revised next attempt. Many definitions center on failure diagnosis, such as inspecting incorrect predictions, verbalizing reasons for failure, summarizing the root cause of prior attempts, or revising a retrieval or decision strategy. A smaller line of work defines the behavior more narrowly as explicit stepwise judgments, for example generating short reflections like 'This step is GOOD' or 'This step is BAD', adding verification steps such as 'Let's verify', or assigning a safety score under <reflection> and <safety degree> tags.

**Variants.** Papers study several named variants, including self-feedback, reflection on failure cases, short-term reflection, long-term reflection, and error reflection, plus other forms that ask for self-questioning, verbal feedback, or reflection-step generation. The same behavior is used in code and test planning, retrieval routing, heuristic evolution, text-based game planning, autonomous driving decisions, visual or audio-visual alignment, multi-agent memory updates, and financial decision making.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead elicit it directly through prompts or workflow modules, for example by integrating reflection into the generation prompt, routing outputs through a critic or reflector that returns feedback for the next iteration, asking the model to emit explicit <reflection> tags and safety scores, or triggering a reflection step when confidence falls below a threshold.

**What it is taken as evidence of.** Papers link it to 11 constructs rather than a single agreed target. The most recurrent construct link is a causal claim from self-reflection to Reasoning, and papers also record links involving System 2 thinking, Action planning, Agency, and Controllability, plus six other constructs. Most of these links are recorded as causal claims from self-reflection to the construct, though one paper reports a causal link in the reverse direction from System 2 thinking to self-reflection, and another records Action planning as related rather than causal.

## Sources

**Self-reflection** (9 papers: [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf), [Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf), [HybGRAG: Hybrid Retrieval-Augmented Generation on Textual and Relational Knowledge Bases](https://aclanthology.org/2025.acl-long.43.pdf), [Safety Reasoning with Guidelines](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cg/wang25cg.pdf), [MOSAIC: Modeling Social AI for Content Dissemination and Regulation in Multi-Agent Simulations](https://aclanthology.org/2025.emnlp-main.325.pdf), [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf), [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf), [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf), [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf))
> The observable behavior of generating an analysis or explanation of errors in code before attempting to correct them, often integrated into the generation prompt.

**Self-feedback** (1 paper: [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf))
> An observable process where a model analyzes its own incorrect outputs, reflects on the errors, and attempts to generate an improved response.

**Reflection on failure cases** (1 paper: [Can LLMs Learn by Teaching for Better Reasoning? A Preliminary Study](https://proceedings.neurips.cc/paper_files/paper/2024/file/8340b085045cf13f1f0b6c2c4cc0a89c-Paper-Conference.pdf))
> The behavior of analyzing incorrect outputs to understand the cause of the error and verbalize reasons for the failure.

**Short-term reflection** (1 paper: [ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ced59d480e07d290b6f29fc8798f195-Paper-Conference.pdf))
> The observable behavior of an LLM generating a comparative analysis of two parent heuristics to provide guidance for creating an improved offspring.

**Long-term reflection** (1 paper: [ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ced59d480e07d290b6f29fc8798f195-Paper-Conference.pdf))
> The observable behavior of an LLM summarizing and distilling insights from multiple short-term reflections to guide future heuristic improvements.

**Reflection** (2 papers: [Re-Aligning Language to Visual Objects with an Agentic Workflow](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d9057d84a9fc37523bf826232ea6820-Paper-Conference.pdf), [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf))
> Analyzing generated outputs to provide feedback for refining expressions in subsequent workflow cycles.

**Reflection generation** (2 papers: [Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf), [Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/837ff662214b04e7ea8c43f095fe0dd7-Paper-Conference.pdf))
> The production of short natural language judgments (e.g., 'This step is GOOD') about the appropriateness of past or candidate actions, used to enhance evaluation accuracy.

**Reflection step generation** (1 paper: [ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning](https://aclanthology.org/2025.emnlp-main.405.pdf))
> The observable act of a model generating a reasoning step that questions or verifies a prior step, often indicated by phrases like 'Let’s verify' or 'Wait, we can also check'.

**Self-QA reflection** (1 paper: [Coarse-to-Fine Grounded Memory for LLM Agent Planning](https://aclanthology.org/2025.emnlp-main.659.pdf))
> Answering self-generated questions about the current trajectory to support reflective correction during planning.

**Error reflection** (2 papers: [CRITICTOOL: Evaluating Self-Critique Capabilities of Large Language Models in Tool-Calling Error Scenarios](https://aclanthology.org/2025.emnlp-main.1355.pdf), [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.320.pdf))
> The observable process where a model identifies that an error occurred in a previous step and analyzes its specific category.

**Self-reflection generation** (1 paper: [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf))
> Producing a verbal summary of past failures that includes diagnostic reasoning and proposed improvements for future attempts.

**Verbal reflection** (1 paper: [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf))
> The observable generation of natural language feedback by a reflector model in response to a failed task trajectory, used to guide subsequent planning attempts.

## Relationships

### Self-reflection →
- **Self-correction** (behavioral indicator): *causes*, 6 papers
  > without the reflection mechanism, the system is prone to mistakes in logical reasoning and lacks the ability for self correction. (Section 4.5)
  - [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf)
  - [DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf)
  - [Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
  - [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf)
  - [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf)
  - [CRITICTOOL: Evaluating Self-Critique Capabilities of Large Language Models in Tool-Calling Error Scenarios](https://aclanthology.org/2025.emnlp-main.1355.pdf)
- **Reasoning** (construct): *causes*, 4 papers
  > ReEvo couples evolutionary search for efficiently exploring heuristic spaces, with self-reflections to boost the reasoning capabilities of LLMs.
  - [ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ced59d480e07d290b6f29fc8798f195-Paper-Conference.pdf)
  - [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf)
  - [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **Factuality** (construct): *causes*, 1 paper
  > We introduce a new framework called Self-Reflective Retrieval-Augmented Generation (SELF-RAG) that enhances an LM’s quality and factuality through retrieval and self-reflection. (ABSTRACT)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
- **Controllability** (construct): *causes*, 1 paper
  > Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements. (ABSTRACT)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
- **Iterative refinement** (behavioral indicator): *causes*, 1 paper
  > Self-reflection plays a pivotal role, allowing autonomous agents to iteratively refine past actions, make improvements, and prevent repetitive errors. (Section 2)
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **Multimodal alignment** (construct): *causes*, 1 paper
  > The tool use, planning, and reflection steps operate cyclically to become an agentic workflow where audio signals are gradually aligned to visual content.
  - [Aligning Audio-Visual Joint Representations with an Agentic Workflow](https://proceedings.neurips.cc/paper_files/paper/2024/file/6c0ff499edc529c7d8c9f05c7c0ccb82-Paper-Conference.pdf)
- **Long-horizon task completion** (behavioral indicator): *causes*, 1 paper
  > The failure of any sub-goal halts the execution of subsequent ones, leading to overall task failure. Therefore, a reflection module is essential to identify and rectify errors promptly. (Section 2.2)
  - [Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf)
- **Agency** (construct): *causes*, 1 paper
  > Emergent agentic abilities are strongly dependent on basic abilities like grounding, world modeling, and self-reflection.
  - [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Planning** (construct): *causes*, 1 paper
  > LEPA refines the plan through self-reflection, aiming to acquire plans that are instrumental in yielding correct solutions.
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **Logical consistency** (construct): *causes*, 1 paper
  > Multi-round self-reflection that encourages a single LLM to critically evaluate its previous responses has demonstrated the effectiveness of deliberation in improving logical coherence and qualities (Section 4.2.1)
  - [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > Reflection on self-generated CoT facilitates learning from mistakes. (Section 5.1)
  - [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf)
- **Error recovery** (construct): *causes*, 1 paper
  > SCRIBE combines domain-specific tools with a self-reflective inference pipeline that supports iterative reasoning, tool use, and error recovery. (Abstract)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)

### → Self-reflection
- **System 2 thinking** (construct): *causes*, 2 papers
  > This indicates that only LMMs with substantial reasoning capabilities can effectively engage in self-reflection and result optimization, underscoring the critical role of System 2 reasoning in addressing ChartMimic’s challenges. (Section 4.2)
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
  - [Agentic Knowledgeable Self-awareness](https://aclanthology.org/2025.acl-long.619.pdf)
- **Code execution** (behavioral indicator): *causes*, 1 paper
  > After the LLM generates a response containing code, we execute the code and return the results for further self-reflection and refinement.
  - [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf)
- **Error detection** (behavioral indicator): *causes*, 1 paper
  > The results show that CDG training significantly improves error detection in reasoning, particularly on the more challenging MATH500 dataset, enhancing the model’s self-reflection ability. (Section 4.2)
  - [Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bb/wang25bb.pdf)

### Associated with
- **Action planning** (construct), 1 paper
  > Otter contains a novel self-reflective action planner for deciding which code to read and which tests to write. (Abstract)
  - [Otter: Generating Tests from Issues to Validate SWE Patches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ahmed25b/ahmed25b.pdf)
- **Tool use** (behavioral indicator), 1 paper
  > After the tool use step, the refined expression is sent to an LLM-based reflector for feedback (i.e., reflection). (Section 1)
  - [Re-Aligning Language to Visual Objects with an Agentic Workflow](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d9057d84a9fc37523bf826232ea6820-Paper-Conference.pdf)
