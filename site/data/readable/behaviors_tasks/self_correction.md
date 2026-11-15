# Self-correction
**Type:** Behavioral indicator  
**Supporting papers:** 198  
**Also known as:** Self-correction and refinement, Noise correction, Error correction, Correcting errors, Fact refinement, Patch refinement, Answer refinement, Natural language refinement, Self-refinement, Assessment refinement, Chain-of-thought correction, Thought refinement, Multi-round self-correction, Invalid SMILES correction, Response refinement, Iterative self-correction, Self-checking, Iterative chart refinement, Response correction, Self-enhancement, Artifact refinement, Iterative response refinement, Iterative revision, Output editing, Rationale refinement, Description revision, Failure correction, Answer correction, Reflection, Self-debugging, Progressive refinement, Refinement, Self-examination, Query regeneration, Reasoning correction  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats self-correction as an iterative loop in which a model reviews an earlier output, identifies an error or inadequacy, and produces a revised version. Most papers frame the target as code, reasoning, proofs, answers, plans, or tool calls, often using signals such as execution results, verifier feedback, solver checks, error messages, critiques, or user feedback; some instead describe it more generally as a latent ability to verify and rectify its own outputs. Success is usually the production of a more correct, valid, executable, aligned, or self-contained revision, though papers differ on whether the judge is the model itself, an external tool or environment, another agent, or human-provided feedback or rubrics.

**Variants.** Papers study this behavior most often in code and reasoning settings, especially revising code from execution feedback, correcting reasoning traces, and rewriting an initial answer or response over multiple rounds. Common labels include error correction, self-refinement, self-debugging, response refinement, and self-checking. Smaller lines of work apply the same pattern to queries, patches, actions, facts, and multimodal descriptions, while keeping the same loop of finding a problem and generating an updated output.

**Space of elicitation and scores.** Papers link self-correction to 4 measurement instruments: GSM8K, MOLERR2FIX, MR-Ben, and Winoground. Their recorded uses frame measurement as self-correction on GSM8K, locating and correcting reasoning errors in MR-Ben, a structured error-to-fix pipeline in MOLERR2FIX, and self-correcting hallucinations in Winoground. Across these instruments, scoring centers on correction behavior rather than only the initial output.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects. Among 11 linked constructs, the most frequently linked outward targets are reasoning, coding ability, instruction following ability, long-horizon planning, and problem-solving ability, with 6 other linked constructs. Most linked construct relations are recorded as causal, though a smaller line of work records self-correction as related to a construct rather than as its cause.

## Sources

**Noise correction** (1 paper: [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf))
> The task of evaluating a given SQL query against a question and database, determining if it is correct, and providing a revised query if it is not.

**Error correction** (11 papers: [ImProver: Agent-Based Automated Proof Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/4864005cfdea7ebd07086ed1b9846825-Paper-Conference.pdf), [Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents](https://aclanthology.org/2025.emnlp-main.249.pdf), [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf), [An interpretable error correction method for enhancing code-to-code translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e01f4ef7ffeedf3317a44461d18df9d-Paper-Conference.pdf), [Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf), [L2MAC: Large Language Model Automatic Computer for Extensive Code Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/9e74900c3f6100c56add4bf417547848-Paper-Conference.pdf), [Tree-Planner: Efficient Close-loop Task Planning with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d53538ba21c05fa361d2b21704172753-Paper-Conference.pdf), [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf), [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf), [Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://aclanthology.org/2025.naacl-long.83.pdf), [CSR-Bench: Benchmarking LLM Agents in Deployment of Computer Science Research Repositories](https://aclanthology.org/2025.naacl-long.633.pdf))
> The process of identifying and fixing errors in a generated proof, often through an iterative refinement process that uses feedback from a verifier.

**Correcting errors** (1 paper: [A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf))
> The observable task of identifying and rectifying mistakes in a given artifact, such as code or text.

**Fact refinement** (1 paper: [VeriFact: Enhancing Long-Form Factuality Evaluation with Refined Fact Extraction and Reference Facts](https://aclanthology.org/2025.emnlp-main.905.pdf))
> The process of revising incomplete or missing facts by incorporating omitted conditions, comparanda, or relational context to make them self-contained and verifiable.

**Patch refinement** (2 papers: [UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging](https://aclanthology.org/2025.emnlp-main.921.pdf), [PatchPilot: A Cost-Efficient Software Engineering Agent with Early Attempts on Formal Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cf/li25cf.pdf))
> Evaluating a generated patch for correctness, performance, or maintainability and producing an improved version or detailed analysis report.

**Response revision** (1 paper: [Spontaneous Giving and Calculated Greed in Language Models](https://aclanthology.org/2025.emnlp-main.267.pdf))
> The observable act of reviewing an initial response and generating an updated one.

**Natural language refinement** (1 paper: [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf))
> The observable act of modifying a natural language description of code logic to correct errors, based on execution feedback and analysis.

**Self-correction** (24 papers: [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf), [The Impossibility of Fair LLMs](https://aclanthology.org/2025.acl-long.5.pdf), [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf), [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf), [Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf), [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf), [MUSTARD: Mastering Uniform Synthesis of Theorem and Proof Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e118ba9ee76c20df728b42a35fb4704-Paper-Conference.pdf), [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://proceedings.iclr.cc/paper_files/paper/2024/file/52f050499cf82fa8efb588e263f6f3a7-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [Plan-on-Graph: Self-Correcting Adaptive Planning of Large Language Model on Knowledge Graphs](https://proceedings.neurips.cc/paper_files/paper/2024/file/4254e856d01a5e7b7ea050477c3ef9b9-Paper-Conference.pdf), [AgentStudio: A Toolkit for Building General Virtual Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/172fe9f8cc55953bad5c24774bf0142b-Paper-Conference.pdf), [Cascading Large Language Models for Salient Event Graph Generation](https://aclanthology.org/2025.naacl-long.112.pdf), [CharacterBox: Evaluating the Role-Playing Capabilities of LLMs in Text-Based Virtual Worlds](https://aclanthology.org/2025.naacl-long.323.pdf), [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf), [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf), [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.538.pdf), [Open-World Attribute Mining for E-Commerce Products with Multimodal Self-Correction Instruction Tuning](https://aclanthology.org/2025.acl-long.85.pdf), [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf), [CVE-Bench: A Benchmark for AI Agents’ Ability to Exploit Real-World Web Application Vulnerabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25i/zhu25i.pdf), [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf), [Improving LLM Safety Alignment with Dual-Objective Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25c/zhao25c.pdf), [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf), [Reflection-Window Decoding: Text Generation with Selective Refinement](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25a/tang25a.pdf))
> Iteratively improving generated code or reasoning by analyzing execution feedback and revising outputs accordingly.

**Self-refinement** (3 papers: [User Feedback in Human-LLM Dialogues: A Lens to Understand Users But Noisy as a Learning Signal](https://aclanthology.org/2025.emnlp-main.133.pdf), [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf), [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf))
> The observable behavior of a model updating its own response in a subsequent turn based on user feedback, even if the improvement is limited.

**Assessment refinement** (1 paper: [Two Heads Are Better Than One: Dual-Model Verbal Reflection at Inference-Time](https://aclanthology.org/2025.emnlp-main.155.pdf))
> The observable act of revising an initial assessment and its rationale in response to critical feedback.

**Chain-of-thought correction** (1 paper: [DICE: Structured Reasoning in LLMs through SLM-Guided Chain-of-Thought Correction](https://aclanthology.org/2025.emnlp-main.355.pdf))
> The process of analyzing an initial reasoning trace (chain-of-thought) and refining it to improve accuracy or format compliance.

**Thought refinement** (1 paper: [RethinkMCTS: Refining Erroneous Thoughts in Monte Carlo Tree Search for Code Generation](https://aclanthology.org/2025.emnlp-main.410.pdf))
> Regenerating or revising a prior reasoning step based on execution feedback to correct logical errors and improve the reasoning trajectory.

**Multi-round self-correction** (1 paper: [A Probabilistic Inference Scaling Theory for LLM Self-Correction](https://aclanthology.org/2025.emnlp-main.685.pdf))
> The observable process where a model iteratively refines a sequence of answers for a given question, with each new answer being a correction of the previous one.

**Invalid SMILES correction** (1 paper: [How to Make Large Language Models Generate 100% Valid Molecules?](https://aclanthology.org/2025.emnlp-main.1350.pdf))
> Modifying a syntactically or semantically invalid SMILES string to produce a valid one, either through iterative refinement or structural transformation.

**Response refinement** (2 papers: [MultiAgentESC: A LLM-based Multi-Agent Collaboration Framework for Emotional Support Conversation](https://aclanthology.org/2025.emnlp-main.232.pdf), [The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models](https://aclanthology.org/2025.naacl-long.303.pdf))
> Improving a selected response by evaluating its consistency with the conversation, alignment with the chosen strategy, and effectiveness in alleviating emotional stress.

**Iterative self-correction** (1 paper: [ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming](https://aclanthology.org/2025.emnlp-main.809.pdf))
> Revising generated constraint model code over multiple rounds using feedback from a symbolic solver and retrieved correction exemplars.

**Self-checking** (2 papers: [MA-GTS: A Multi-Agent Framework for Solving Complex Graph Problems in Real-World Applications](https://aclanthology.org/2025.emnlp-main.973.pdf), [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf))
> An iterative process where the model refines its solution over multiple rounds to improve correctness and verify results.

**Iterative chart refinement** (1 paper: [AMACE: Automatic Multi-Agent Chart Evolution for Iteratively Tailored Chart Generation](https://aclanthology.org/2025.emnlp-main.1089.pdf))
> The observable process of modifying chart code and visual output across multiple steps based on feedback from evaluation agents.

**Artifact refinement** (1 paper: [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf))
> The observable action of an agent modifying and improving a piece of work (an artifact) based on instructions or feedback from another agent.

**Iterative response refinement** (2 papers: [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf), [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf))
> Producing a revised answer over multiple attempts that improves on earlier outputs.

**Response correction** (1 paper: [Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf))
> The observable action of rectifying the model's output response, including updating outdated answers or incorrect classifications.

**Self-enhancement** (1 paper: [DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf))
> The observable behavior of a model re-generating a data item to produce an improved version, using its own prior self-reflection as guidance.

**Iterative revision** (1 paper: [Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf))
> The observable behavior of generating a sequence of answers, where each new answer is conditioned on the model's previous attempts.

**Rationale refinement** (1 paper: [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf))
> The observable act of modifying a previously generated rationale to improve its quality, which can be done by the same model (self-refinement) or a different model (cross-refinement).

**Output editing** (1 paper: [Uncovering Gaps in How Humans and LLMs Interpret Subjective Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362fbc0d182c6b4b8dadb90177239e4-Paper-Conference.pdf))
> The observable task where an LLM revises its own previously generated text to better align with a specified subjective quality or constitutional principle.

**Description revision** (1 paper: [PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebf8764ecf0688cdd9fe1e5a9c525d0d-Paper-Conference.pdf))
> The observable task of editing a given textual description to improve its accuracy or quality with respect to an associated image.

**Failure correction** (1 paper: [Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d6e85e88495104442af94c98e899659-Paper-Conference.pdf))
> Revising an action choice after a failed execution by proposing a more suitable next action.

**Answer correction** (1 paper: [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf))
> Editing or rewriting an initial model answer into a revised answer that better satisfies the desired criteria.

**Self-debugging** (3 papers: [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf), [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf))
> The model's capacity to identify and correct errors in its own generated code based on feedback from code execution.

**Reflection** (1 paper: [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf))
> The ability of the model to evaluate past decision sequences, identify errors, and generate corrected reasoning to improve future performance.

**Progressive refinement** (1 paper: [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf))
> The ability of a model to iteratively improve the accuracy, depth, and quality of its responses starting from an initial thought or approximate solution.

**Refinement** (1 paper: [SPRI: Aligning Large Language Models with Context-Situated Principles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhan25a/zhan25a.pdf))
> The ability of a model to iteratively improve its output based on feedback or further instructions.

**Self-examination** (1 paper: [Empowering LLM Agents with Zero-Shot Optimal Decision-Making through Q-learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c25de6a9da675464ebb925e430c58325-Paper-Conference.pdf))
> An observable process where a model uses its own capabilities to check, validate, and correct its generated outputs, such as actions or state predictions.

**Query regeneration** (1 paper: [Dialect-SQL: An Adaptive Framework for Bridging the Dialect Gap in Text-to-SQL](https://aclanthology.org/2025.emnlp-main.178.pdf))
> An iterative process where the model attempts to generate a new query if the previous one fails execution or contains syntax errors.

**Reasoning correction** (1 paper: [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf))
> The observable action of modifying a previously generated reasoning trajectory to fix an identified error.

## Relationships

### Self-correction →
- **Code debugging** (behavioral indicator): *causes*, 3 papers
  > “SELF-DEBUGGING can teach the LLM to perform rubber duck debugging”
  - [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
  - [DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation](https://aclanthology.org/2025.emnlp-main.58.pdf)
- **Reasoning** (construct): *causes*, 2 papers
  > To the best of our knowledge, we are the first to incorporate a reflection mechanism for self-correction and adaptive KG exploration into KG-augmented LLMs, effectively augmenting the LLM’s reasoning ability. (Section 1)
  - [Plan-on-Graph: Self-Correcting Adaptive Planning of Large Language Model on Knowledge Graphs](https://proceedings.neurips.cc/paper_files/paper/2024/file/4254e856d01a5e7b7ea050477c3ef9b9-Paper-Conference.pdf)
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Question answering** (behavioral indicator): *causes*, 2 papers
  > PoG (Chen et al., 2024a) integrates reflection and self-correction mechanisms to adaptively explore the reasoning paths over KG via an LLM agent, and then augments the LLM in complex reasoning and question answering based on the retrieved knowledge paths. (Section 3.2.3)
  - [Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities](https://aclanthology.org/2025.emnlp-main.1249.pdf)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Code generation** (behavioral indicator): *causes*, 2 papers
  > Self-Debugging (SD) is both complementary to and beneficial for M1... Applying SD on TAs can provide S-score benefits... M1 achieves consistent improvements.
  - [Can LLMs Learn by Teaching for Better Reasoning? A Preliminary Study](https://proceedings.neurips.cc/paper_files/paper/2024/file/8340b085045cf13f1f0b6c2c4cc0a89c-Paper-Conference.pdf)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hallucination** (behavioral indicator): *causes*, 2 papers
  > to prevent hallucinations in LLMs, such as sacrificing solving accuracy to avoid execution errors, the model alignment and self-correction mechanism are adopted in LLMOPT. (Abstract)
  - [LLMOPT: Learning to Define and Solve General Optimization Problems from Scratch](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbe6dd68b0cf2b1d43b458d2b8ca31b0-Paper-Conference.pdf)
  - [Empowering LLM Agents with Zero-Shot Optimal Decision-Making through Q-learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c25de6a9da675464ebb925e430c58325-Paper-Conference.pdf)
- **Mathematical problem solving** (behavioral indicator): *causes*, 1 paper
  > GPT4-Code’s robust performance in solving math problems derives not only from its ability to generate accurate step-by-step code, but also from its self-debugging mechanism.
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Coding ability** (construct): *causes*, 1 paper
  > teaching large language models to perform SELF-DEBUGGING without human guidance is another promising path to enhance coding capability and reduce the sampling cost required to accomplish challenging tasks.
  - [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf)
- **MR-Ben** (measurement instrument): *measured_by*, 1 paper
  > Unlike prior efforts, MR-Ben goes beyond accuracy by assessing the ability to locate potential errors in the reasoning process and provide explanations and corrections. (Section 2).
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
- **Winoground** (measurement instrument): *measured_by*, 1 paper
  > In this section, we evaluate on WinoGround (Thrush et al., 2022) dataset to show whether given extra token-level annotation cues, the vision language model is able to self-correct its own hallucinations. (Section 5.3)
  - [TLDR: Token-Level Detective Reward Model for Large Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > Our analysis shows that self-refinement enables the robustness of agent capability and the diversity of agent environments and thoughts further enhances the performance. (Section 11)
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
- **Instruction following ability** (construct): *causes*, 1 paper
  > Refinement preference pairs enhance instruction-following capability more effectively. (Section 3.5)
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **Problem-solving ability** (construct): *causes*, 1 paper
  > ...post-prompting strategies are limited by the model’s intrinsic self-correction capabilities, thereby failing to significantly enhance problem-solving capabilities. (Section 2)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Long-horizon planning** (construct): *causes*, 1 paper
  > “self-refinement ... iteratively improves a previously generated plan” and “bidirectional dependency ... thus improving its ability to plan ahead”
  - [Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cd/li25cd.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > GSM8K evaluates the model’s self-correction capabilities... (Section 4.2)
  - [CopySpec: Accelerating LLMs with Speculative Copy-and-Paste](https://aclanthology.org/2025.emnlp-main.1337.pdf)
- **MOLERR2FIX** (measurement instrument): *measured_by*, 1 paper
  > MOLERR2FIX introduces a structured chain-like, four-stage Error-to-Fix evaluation pipeline—detection, localization, explanation, and revision—offering a fine-grained and progressive framework for assessing LLMs in chemical reasoning. (Section 1)
  - [MolErr2Fix: Benchmarking LLM Trustworthiness in Chemistry via Modular Error Detection, Localization, Explanation, and Correction](https://aclanthology.org/2025.emnlp-main.977.pdf)
- **Toxicity** (construct): *causes*, 1 paper
  > The results in Table 3 demonstrate that 1) CRITIC substantially lowers the occurrence of toxic generations, while preserving fluency and diversity as the vanilla LLMs. (Section 4.3 Results)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)

### → Self-correction
- **Self-reflection** (behavioral indicator): *causes*, 6 papers
  > without the reflection mechanism, the system is prone to mistakes in logical reasoning and lacks the ability for self correction. (Section 4.5)
  - [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf)
  - [DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf)
  - [Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
  - [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://aclanthology.org/2025.naacl-long.447.pdf)
  - [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf)
  - [CRITICTOOL: Evaluating Self-Critique Capabilities of Large Language Models in Tool-Calling Error Scenarios](https://aclanthology.org/2025.emnlp-main.1355.pdf)
- **Code execution** (behavioral indicator): *causes*, 1 paper
  > The analysis reveals that GPT4-Code’s strong performance is not solely due to its code generation and execution abilities but also its capacity to adjust its problem-solving strategies based on feedback from code execution—a process we term self-debugging
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > imbue an LLM with the capability to recursively detect and correct its previous mistakes in subsequent iterations.
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Critique generation** (behavioral indicator): *causes*, 1 paper
  > Additional studies confirm the utility of generated critiques for Critic-RM in identifying and correcting mistakes made by LLMs.
  - [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **Self-evaluation** (behavioral indicator): *causes*, 1 paper
  > Since the model possesses self-evaluation and exploration capabilities, it can abandon erroneous paths and select the correct one (Figure 1).
  - [GRAT: Guiding Retrieval-Augmented Reasoning through Process Rewards Tree Search](https://aclanthology.org/2025.acl-long.1352.pdf)
- **Long chain-of-thought generation** (behavioral indicator): *causes*, 1 paper
  > A proven approach for scaling inference compute is to generate long chains-of-thought (CoTs), enabling models to engage in structured reasoning strategies such as backtracking and error correction. (Abstract)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Self-verification** (behavioral indicator): *causes*, 1 paper
  > ...enables LLMs to self-correct their outputs through self-verification.
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Error detection** (behavioral indicator): *causes*, 1 paper
  > Without accurate error identifications, self-correction becomes more challenging. (Section 1)
  - [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf)

### Associated with
- **System 2 thinking** (construct), 1 paper
  > state-of-the-art LLMs (OpenAI, 2024, 2025) are capable of self-correction—often referred to as “system 2” reasoning (Xiang et al., 2025)—without explicit external verification. (Introduction)
  - [Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.699.pdf)
- **Self-awareness** (construct), 1 paper
  > Self-awareness, i.e., the ability to assess and correct one’s generation, is a fundamental aspect of human intelligence...
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Self-reflection ability** (construct), 1 paper
  > “Reflection Quality ... analyzes whether each reflection step drives the question towards correctness.”
  - [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)
- **Iterative refinement** (behavioral indicator), 1 paper
  > Visually grounded inputs enable closed-loop iterative refinement: We highlight the critical role of grounded visual inputs in articulating ambiguous and complex objects, leveraging such inputs in a closed-loop system that self-evaluates and self-improves its articulations. (Section 1)
  - [Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf)
- **Multi-agent collaboration** (behavioral indicator), 1 paper
  > “we propose DPSDP: Direct Policy Search by Dynamic Programming, an RL algorithm designed to train a multi-agent LLM system to iteratively improve its responses for reasoning tasks with self-generated data”
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
