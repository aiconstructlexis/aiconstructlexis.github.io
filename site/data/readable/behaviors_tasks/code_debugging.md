# Code debugging
**Type:** Behavioral indicator  
**Supporting papers:** 75  
**Also known as:** Bug fixing, Code repair, Debugging, Self-repair, Self-debugging, Runtime debugging, Bug identification, Crash resolution, Program repair, Data science code debugging, Code correction, Noise correction, Code fixing, Debugging capability, Debugging ability, Self-repair capability, Patch generation, Code patch generation, Reflective debugging  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats code debugging as identifying and correcting errors in provided or existing code, whether a snippet, a generated program, or a larger codebase. Many formulations make it interactive or iterative: models revise code in response to runtime feedback, execution results, exception messages, or failing tests until the code works, becomes correct, or reaches successful execution. Smaller formulations narrow success to making minimal edits that preserve style, producing a patch or diff that resolves a repository issue, or editing a kernel so a reproducer no longer crashes within the allotted window.

**Variants.** The naming varies widely, with common alternatives including code repair, bug fixing, debugging, program repair, and self-debugging. Papers study it at different scopes, from function-level fixes with test cases to class- or file-level edits and repository patching, and in narrower domains such as visual JavaScript software, Linux kernel crash resolution, data science Python scripts that require identifying, localizing, and explaining logical runtime errors, and SQL query correction. Some formulations separate bug identification from fixing, while others frame self-repair as correcting the model's own generated code after feedback.

**Space of elicitation and scores.** Papers measure it with 10 instruments. The most frequently linked are HumanEvalFix, InfiniteBench, APPS, Arena-Hard, and Codeforces, and these are mostly benchmark or dataset based evaluations of bug fixing, self-repair, or long-context code debugging. Other work uses additional benchmarks and one human evaluation that scores explanations and repaired code.

**What it is taken as evidence of.** Papers link it to 1 construct: one study reports that code debugging correlates with Generation diversity, describing better repair performance alongside more diverse fixes. Beyond this construct link, the recorded relationships do not show broader agreement on what construct it reflects. A few papers also claim causal relationships from self-correction, feedback generation, and textual reasoning to code debugging, and some relate it to code generation and fault localization.

## Sources

**Code debugging** (6 papers: [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf), [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf), [CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases](https://aclanthology.org/2025.naacl-long.7.pdf), [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf), [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf), [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://proceedings.iclr.cc/paper_files/paper/2024/file/6507b115562bb0a305f1958ccc87355a-Paper-Conference.pdf))
> The process of interactively modifying and correcting code based on feedback from a runtime environment to resolve errors and achieve successful execution.

**Code repair** (2 papers: [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf), [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf))
> The observable task of identifying and fixing errors in a provided code snippet to make it correct.

**Bug fixing** (4 papers: [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf), [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf), [UnitCoder: Scalable Code Synthesis from Pre-training Corpora](https://aclanthology.org/2025.emnlp-main.286.pdf), [DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance by Adaptive Tree Traversal](https://aclanthology.org/2025.acl-long.973.pdf))
> The observable task of identifying and correcting errors or unintended behaviors in a software codebase based on a problem description.

**Debugging** (2 papers: [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf), [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf))
> The task of identifying and fixing errors in existing computer code.

**Self-repair** (1 paper: [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf))
> The observable task of fixing an incorrect program after being provided with error feedback, such as an exception message or a failing test case.

**Self-debugging** (4 papers: [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50e9ad960ae78b741a6b4fea533f2eaf-Paper-Conference.pdf), [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf), [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf))
> The observable process where a model identifies errors in its own generated code or reasoning and attempts to correct them.

**Runtime debugging** (1 paper: [AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf))
> Diagnosing and fixing issues that arise during code execution.

**Bug identification** (1 paper: [Position: Scaling LLM Agents Requires Asymptotic Analysis with LLM Primitives](https://raw.githubusercontent.com/mlresearch/v267/main/assets/meyerson25a/meyerson25a.pdf))
> The action of locating and describing a flaw or error within a piece of code.

**Crash resolution** (1 paper: [kGym: A Platform and Dataset to Benchmark Large Language Models on Linux Kernel Crash Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/8e9ed2a28af7d9085180e3817b2c9a57-Paper-Datasets_and_Benchmarks_Track.pdf))
> Editing the kernel so that the reproducer no longer causes a crash within the allotted execution window.

**Program repair** (3 papers: [Hints-In-Browser: Benchmarking Language Models for Programming Feedback Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/34cc2ded6daba59357134c0b9fb06bfe-Paper-Datasets_and_Benchmarks_Track.pdf), [Revisit Self-Debugging with Self-Generated Tests for Code Generation](https://aclanthology.org/2025.acl-long.881.pdf), [EffiCoder: Enhancing Code Generation in Large Language Models through Efficiency-Aware Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25as/huang25as.pdf))
> Generating a repaired version of a buggy program with minimal edits that preserves the original context and style.

**Data science code debugging** (1 paper: [Why Stop at One Error? Benchmarking LLMs as Data Science Code Debuggers for Multi-Hop and Multi-Bug Errors](https://aclanthology.org/2025.emnlp-main.878.pdf))
> The task of identifying, localizing, and explaining logical runtime errors within Python scripts that use data science libraries.

**Code correction** (1 paper: [TALON: A Multi-Agent Framework for Long-Table Exploration and Question Answering](https://aclanthology.org/2025.emnlp-main.1393.pdf))
> The observable process of identifying an error in a generated code snippet and producing a revised version of the code to fix the error.

**Noise correction** (1 paper: [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf))
> The task of evaluating a given SQL query against a question and database, determining if it is correct, and providing a revised query if it is not.

**Code fixing** (1 paper: [CopySpec: Accelerating LLMs with Speculative Copy-and-Paste](https://aclanthology.org/2025.emnlp-main.1337.pdf))
> Editing existing code to correct errors such as indentation or syntax issues.

**Debugging capability** (1 paper: [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf))
> The latent ability to identify, analyze, and correct errors in source code.

**Debugging ability** (1 paper: [Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/83ba7056bce2c3c3c27e17397cf3e1f0-Paper-Conference.pdf))
> The latent capability of a large language model to identify, analyze, and correct errors in source code or computational workflows.

**Self-repair capability** (1 paper: [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf))
> The latent ability to use error feedback to revise an initially flawed program into a correct solution.

**Patch generation** (1 paper: [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf))
> The observable action of producing a set of code changes (a patch) intended to resolve a software issue.

**Code patch generation** (1 paper: [UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench](https://aclanthology.org/2025.acl-long.189.pdf))
> Producing a diff-formatted patch file that specifies additions, deletions, and modifications to source code in order to resolve a software issue.

**Reflective debugging** (1 paper: [Flow-of-Options: Diversified and Improved LLM Reasoning by Thinking Through Options](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nair25c/nair25c.pdf))
> The process of an LLM agent identifying errors in the code it has generated and attempting to correct them.

## Relationships

### Code debugging →
- **InfiniteBench** (measurement instrument): *measured_by*, 3 papers
  > Table 2: Performance of single-step reasoning on InfiniteBench (Zhang et al., 2024a). ... Code.Debug
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
  - [CommVQ: Commutative Vector Quantization for KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25du/li25du.pdf)
- **HumanEvalFix** (measurement instrument): *measured_by*, 3 papers
  > HUMANEVALFIX (NL+C!C) Given an incorrect code function with a subtle bug and accompanying unit tests, the model is tasked to ﬁx the function. (Section 3)
  - [OctoPack: Instruction Tuning Code Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1ec299a5229034141e58aeded0d0b9de-Paper-Conference.pdf)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
  - [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)
- **APPS** (measurement instrument): *measured_by*, 2 papers
  > We evaluate our NL-DEBUGGING framework on two widely used code datasets: APPS (Hendrycks et al., 2021) and Codeforces (Team, 2024). (Section 4.1.1)
  - [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **EvalPlus** (measurement instrument): *measured_by*, 1 paper
  > We evaluate their static debug and self-refine capabilities on EvalPlus with five iterations.
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 1 paper
  > Conversely, ArenaHard, sampling 500 tasks from ChatbotArena, displays an excessive concentration on coding and debugging tasks, accounting for over 57% of its content. (Section 1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **LiveCodeBench** (measurement instrument): *measured_by*, 1 paper
  > "we evaluate the execution-feedback-based multi-turn coding using the self-repair scenario"
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > To measure the quality of generated contents from DCE-LLM, we conduct a human evaluation of both explanations and repaired code.
  - [DCE-LLM: Dead Code Elimination with Large Language Models](https://aclanthology.org/2025.naacl-long.501.pdf)
- **Generation diversity** (construct): *correlates*, 1 paper
  > The superior performance of AuPairs produced by Gemini-1.5-Pro corresponds to highly diverse fixes (Fig. 8, top right). (Section 3.7. High Code-specific Diversity)
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
- **Codeforces** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our NL-DEBUGGING framework on two widely used code datasets: APPS (Hendrycks et al., 2021) and Codeforces (Team, 2024). (Section 4.1.1)
  - [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf)
- **Defects4J** (measurement instrument): *measured_by*, 1 paper
  > To assess HLP’s impact on practical applications beyond code completion, we evaluate the performance of code repair using Defects4J (Just et al., 2014). (Section 4.3)
  - [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1672.pdf)
- **HumanEval** (measurement instrument): *measured_by*, 1 paper
  > In this paper, we analyze Code Llama, GPT-3.5 and GPT-4’s ability to perform self-repair on problems taken from HumanEval and APPS.
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)

### → Code debugging
- **Self-correction** (behavioral indicator): *causes*, 3 papers
  > “SELF-DEBUGGING can teach the LLM to perform rubber duck debugging”
  - [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
  - [DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation](https://aclanthology.org/2025.emnlp-main.58.pdf)
- **Feedback generation** (behavioral indicator): *causes*, 1 paper
  > Finally, this feedback is used by the code model to repair the program (5). (Figure 1 caption)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Textual reasoning** (behavioral indicator): *causes*, 1 paper
  > Our findings highlight the potential of natural language reasoning to advance automated code debugging and address complex programming challenges. (Abstract)
  - [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf)

### Associated with
- **Hint generation** (behavioral indicator), 1 paper
  > While this fixed program Pr is not directly used to provide feedback to learners, it is typically used as an intermediate step when generating hints. (Section 3.1)
  - [Hints-In-Browser: Benchmarking Language Models for Programming Feedback Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/34cc2ded6daba59357134c0b9fb06bfe-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Coding** (behavioral indicator), 1 paper
  > Coding: The ability to write, synthesize, document, debug, and review code across various programming languages. (Section 2.1)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Fault localization** (behavioral indicator), 1 paper
  > Software debugging is a time-consuming endeavor involving a series of steps, such as fault localization and patch generation, each requiring thorough analysis and a deep understanding of the underlying logic.
  - [UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging](https://aclanthology.org/2025.emnlp-main.921.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > we model self-repair as consisting of four stages: code generation, code execution, feedback generation, and code repair.
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
