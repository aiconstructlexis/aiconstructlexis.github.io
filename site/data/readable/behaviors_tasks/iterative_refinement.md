# Iterative refinement
**Type:** Behavioral indicator  
**Supporting papers:** 58  
**Also known as:** Self-debugging, Stepwise revision, Self-refinement, Self-revision, Response refinement, Error refinement, Iterative self-calibration, Answer revision, Argument revision, Code revision, Program refinement, Refinement during generation, Solution optimization, Multi-step rectification, Action refinement, Solution revision, Iterative critique-revision, Iterative hypothesis refinement, Critique and refinement, Hypothesis refinement, Cross-refinement, Refinement, Solution refinement, Refinement capability, Progressive refinement, Program revision, Knowledge refinement, Iterative reflection capability, Solution rewriting, Multi-turn revision  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as making multiple attempts at a task and revising later outputs in light of earlier ones, with feedback carried through context, critique, verification signals, or even parameter updates. What counts as success is usually an improved or corrected answer, plan, program, rationale, or other output, though papers differ on who or what supplies the signal: execution or verifier feedback, critic or peer comments, uncertainty scores, visual comparison against a reference, and counterarguments all appear. A smaller line of work narrows the behavior to targeted revision, such as changing only the identified wrong reasoning steps while keeping earlier correct steps unchanged, or revising previously generated text before continuing generation. Some authors also frame the same phenomenon as a latent capacity to improve outputs through repeated feedback and revision, rather than only as an observed sequence of edits.

**Variants.** The variant space is broad. Common labels include self-revision, self-refinement, response refinement, solution refinement, and iterative critique-revision, and papers apply them to code debugging and program verification, mathematical step correction and solution rewriting, scientific idea or hypothesis refinement, and multimodal comparison tasks such as charts, webpages, and scene graphs. Other papers study domain-specific revision of actions, answers, arguments, medical multiple-choice responses, retrieval-augmented answers, and partially generated text during decoding.

**Space of elicitation and scores.** Only 2 measurement instruments are linked to this behavior, GPQA and MMLU. Both are used in work on solution optimization, specifically GPQA and the Machine Learning and College Physics subsets of MMLU.

**What it is taken as evidence of.** Papers link this behavior to 5 constructs, but they do not converge on a single construct it reflects. Some papers claim a causal relationship from iterative refinement to text generation quality and semantic alignment, others claim causal relationships from abstract reasoning and chain-of-thought reasoning to iterative refinement, and another reports it as related to inductive reasoning.

## Sources

**Self-debugging** (1 paper: [ExploraCoder: Advancing Code Generation for Multiple Unseen APIs via Planning and Chained Exploration](https://aclanthology.org/2025.acl-long.887.pdf))
> The observable process where a model identifies errors in its own generated code based on execution feedback and attempts to correct them.

**Stepwise revision** (1 paper: [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf))
> The observable behavior of modifying specific reasoning steps identified as incorrect while preserving earlier correct steps in an iterative manner.

**Self-revision** (3 papers: [Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?](https://aclanthology.org/2025.acl-long.232.pdf), [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf), [Design2Code: Benchmarking Multimodal Code Generation for Automated Front-End Engineering](https://aclanthology.org/2025.naacl-long.199.pdf))
> The observable act of a model extending its reasoning process to re-evaluate and modify its previous statements, often indicated by explicit markers like "Wait" or "Alternatively".

**Self-refinement** (5 papers: [Knowledge Boundary of Large Language Models: A Survey](https://aclanthology.org/2025.acl-long.256.pdf), [Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cd/li25cd.pdf), [Automated Hypothesis Validation with Agentic Sequential Falsifications](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25n/huang25n.pdf), [OptMATH: A Scalable Bidirectional Data Synthesis Framework for Optimization Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25o/lu25o.pdf), [Safety Reasoning with Guidelines](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cg/wang25cg.pdf))
> Iteratively improving an initial response through self-evaluation and regeneration, either within a single model or via multi-agent debate.

**Response refinement** (3 papers: [PopAlign: Diversifying Contrasting Patterns for a More Comprehensive Alignment](https://aclanthology.org/2025.acl-long.1403.pdf), [MultiAgentESC: A LLM-based Multi-Agent Collaboration Framework for Emotional Support Conversation](https://aclanthology.org/2025.emnlp-main.232.pdf), [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf))
> Generating an initial response and then improving it in a subsequent turn through explicit refinement instructions, creating a contrast between raw and polished outputs.

**Iterative refinement** (6 papers: [Learning to Reason from Feedback at Test-Time](https://aclanthology.org/2025.acl-long.262.pdf), [Generalists vs. Specialists: Evaluating LLMs on Highly-Constrained Biophysical Sequence Optimization Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bg/chen25bg.pdf), [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf), [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](https://aclanthology.org/2025.naacl-long.342.pdf), [One Unified Model for Diverse Tasks: Emotion Cause Analysis via Self-Promote Cognitive Structure Modeling](https://aclanthology.org/2025.naacl-long.516.pdf), [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf))
> Generating multiple attempts at solving a problem, where later outputs are influenced by feedback on earlier ones, either through context or parameter updates.

**Error refinement** (1 paper: [LLM Meets Scene Graph: Can Large Language Models Understand and Generate Scene Graphs? A Benchmark and Empirical Study](https://aclanthology.org/2025.acl-long.1036.pdf))
> The task of correcting an erroneous scene graph to align with a given textual description and context.

**Iterative self-calibration** (1 paper: [SGIC: A Self-Guided Iterative Calibration Framework for RAG](https://aclanthology.org/2025.acl-long.1376.pdf))
> An observable process where a model repeatedly refines its generated answer over multiple rounds, using its previous outputs and associated uncertainty scores as input for the next iteration.

**Argument revision** (1 paper: [Tree-of-Debate: Multi-Persona Debate Trees Elicit Critical Thinking for Scientific Comparative Analysis](https://aclanthology.org/2025.acl-long.1422.pdf))
> The observable process by which a model updates its claims in response to counterarguments, incorporating new reasoning or evidence to refine its position.

**Code revision** (1 paper: [METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](https://aclanthology.org/2025.acl-long.1452.pdf))
> Modifying existing code based on feedback from critique agents to correct visual or structural mismatches with a reference chart.

**Answer revision** (1 paper: [MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning](https://aclanthology.org/2025.acl-long.1459.pdf))
> The observable change in an agent's response from one turn to the next, reflecting updates based on peer input.

**Program refinement** (1 paper: [AlphaVerus: Bootstrapping Formally Verified Code Generation through Self-Improving Translation and Treefinement](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25a/aggarwal25a.pdf))
> Iteratively modifying an incorrect or partially verified program using feedback from a verifier to produce a fully verified version.

**Refinement during generation** (1 paper: [Reflection-Window Decoding: Text Generation with Selective Refinement](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25a/tang25a.pdf))
> The observable act of revising or correcting a segment of previously generated text before continuing with new content, triggered by a pausing criterion.

**Action refinement** (1 paper: [Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wan25g/wan25g.pdf))
> The process by which an LLM generates improved actions for suboptimal decisions identified in RL trajectories, validated through environment simulation.

**Solution revision** (1 paper: [Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf))
> Modifying an existing code solution based on feedback to improve correctness or efficiency.

**Solution optimization** (1 paper: [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf))
> The iterative refinement of answers to complex scientific or technical questions through self-evaluation and critique, aiming to improve accuracy over multiple steps.

**Multi-step rectification** (1 paper: [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf))
> Correcting an incorrect answer to a medical question by first identifying its inaccuracy and then providing the correct response from remaining options, simulating sequential clinical reasoning.

**Iterative critique-revision** (1 paper: [Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf))
> An observable multi-step process where a critic model provides feedback on a solution, which a generator model then uses to produce a revised solution.

**Iterative hypothesis refinement** (1 paper: [From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery](https://aclanthology.org/2025.emnlp-main.895.pdf))
> The observable process of progressively improving a scientific hypothesis through repeated cycles of evaluation and modification.

**Critique and refinement** (1 paper: [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf))
> The observable behavior of a critic agent evaluating responses from other agents and then generating an updated, improved response based on that evaluation.

**Hypothesis refinement** (1 paper: [MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses](https://proceedings.iclr.cc/paper_files/paper/2025/file/51fd9a7d1706023cb9f8210cc6ac357c-Paper-Conference.pdf))
> Improving generated hypotheses based on feedback regarding validness, novelty, clarity, and significance.

**Cross-refinement** (1 paper: [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf))
> Improving a rationale using a different model variant than the one that generated it.

**Refinement** (1 paper: [SPRI: Aligning Large Language Models with Context-Situated Principles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhan25a/zhan25a.pdf))
> The ability of a model to iteratively improve its output based on feedback or further instructions.

**Solution refinement** (2 papers: [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf), [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf))
> The latent ability of an LLM to dynamically improve its answers to complex scientific or technical questions through iterative self-evaluation and critique.

**Refinement capability** (1 paper: [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf))
> The latent ability of a model to correct or improve a response that fails to follow an instruction, ideally with minimal irrelevant revisions.

**Progressive refinement** (1 paper: [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf))
> The ability of a model to iteratively improve the accuracy, depth, and quality of its responses starting from an initial thought or approximate solution.

**Program revision** (1 paper: [Synthesizing Programmatic Reinforcement Learning Policies with Large Language Model Guided Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf887f2bfe2776584e3bce80ed206ef-Paper-Conference.pdf))
> Updating previously generated programs using feedback such as rewards or execution traces.

**Knowledge refinement** (1 paper: [NeSyC: A Neuro-symbolic Continual Learner For Complex Embodied Tasks in Open Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/d569e4655e2835e3d38310b67c5ad646-Paper-Conference.pdf))
> Re-entering the reformulation phase to update generalized knowledge after failures or detected inconsistencies.

**Iterative reflection capability** (1 paper: [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.502.pdf))
> The latent ability of a model to effectively refine its responses over multiple cycles of self-evaluation and revision, avoiding degradation due to redundancy, drift, or stubbornness.

**Solution rewriting** (1 paper: [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf))
> Producing an improved version of a mathematical solution based on critique, using the model's rewriting capabilities.

**Multi-turn revision** (1 paper: [CodeIO: Condensing Reasoning Patterns via Code Input-Output Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25t/li25t.pdf))
> Iteratively refining reasoning outputs based on execution feedback, where incorrect predictions are revised in subsequent turns using feedback from code execution.

## Relationships

### Iterative refinement →
- **Text generation quality** (construct): *causes*, 2 papers
  > "This iterative refinement process continues for several cycles until obtaining a more robust and comprehensive response."
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
  - [Federated In-Context Learning: Iterative Refinement for Improved Answer Quality](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25db/wang25db.pdf)
- **Semantic alignment** (construct): *causes*, 1 paper
  > This optimization process plays a crucial role in enhancing the semantic consistency and visual quality of the generated WordArt. (Section 4.3)
  - [MetaDesigner: Advancing Artistic Typography through AI-Driven, User-Centric, and Multilingual WordArt Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/a10c3d85879c29331ba4d73ede56c7d3-Paper-Conference.pdf)
- **GPQA** (measurement instrument): *measured_by*, 1 paper
  > In solution optimization, we assess performance on the Google-proof Question Answering (GPQA) benchmark (Rein et al., 2023)... (Section 4)
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > In solution optimization, we assess performance on ... the Machine Learning and College Physics subsets of MMLU (Hendrycks et al., 2020)... (Section 4)
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)

### → Iterative refinement
- **Self-verification** (behavioral indicator): *causes*, 1 paper
  > Incorporated with CSV, the model becomes capable of using code to verify answers, then reviewing and adjusting how it arrived at the solution if the verification result is False, aiming at obtaining the correct answer.
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > Self-reflection plays a pivotal role, allowing autonomous agents to iteratively refine past actions, make improvements, and prevent repetitive errors. (Section 2)
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **Abstract reasoning** (construct): *causes*, 1 paper
  > We propose Instruct-of-Reflection (IoRT), a dynamic iterative reflection framework that integrates abstract reasoning into the reflection process, generating adaptive instruction to regulate the iterative reflection. (§ 7)
  - [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.502.pdf)
- **Chain-of-thought reasoning** (construct): *causes*, 1 paper
  > the Actor refines suboptimal actions via multi-step reasoning and environment validation (Abstract).
  - [Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wan25g/wan25g.pdf)

### Associated with
- **Hypothesis generation** (behavioral indicator), 2 papers
  > Iterative hypothesis refinement employs a three-step process: proposing, selecting, and refining hypotheses in the form of textual rules. (Abstract).
  - [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf)
  - [MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses](https://proceedings.iclr.cc/paper_files/paper/2025/file/51fd9a7d1706023cb9f8210cc6ac357c-Paper-Conference.pdf)
- **Inductive reasoning** (construct), 1 paper
  > This work investigates LMs’ inductive reasoning capabilities through the lens of iterative hypothesis refinement (Section 1).
  - [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf)
- **Self-correction** (behavioral indicator), 1 paper
  > Visually grounded inputs enable closed-loop iterative refinement: We highlight the critical role of grounded visual inputs in articulating ambiguous and complex objects, leveraging such inputs in a closed-loop system that self-evaluates and self-improves its articulations. (Section 1)
  - [Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf)
