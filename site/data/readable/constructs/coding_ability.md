# Coding ability
**Type:** Construct  
**Supporting papers:** 47  
**Also known as:** Coding capability, Coding skill, Code programming, Programming capability, Coding proficiency, Coding capabilities, Coding skills, Programming ability, Programming skills, Python coding skill, Visual problem-solving, Programming  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats coding ability as a latent or general model capability for generating syntactically correct, functional code for programming tasks or prompts. Many definitions widen this to understanding code as well, and a smaller line of work also includes debugging, repair, completion, execution, summarization, documentation, review, or code manipulation. The clearest disagreement is scope: some authors use narrow versions such as correct Python code or basic programming skills, while others extend the term to software-level coding or to visual software problem-solving that requires interpreting screenshots, diagrams, or interface layouts. A minority framing treats programming capability as a performance-derived latent component, described as the third principal component of benchmark performance.

**Space of facets.** Papers commonly use coding ability, coding capability, programming ability, coding skills, and coding proficiency as near-synonyms, though the scopes are not identical. Some papers spell out subactivities such as code generation, understanding, debugging, repair, review, documentation, and summarization, and one taxonomy places code programming alongside text comprehension, creative language generation, common sense reasoning, mathematical reasoning, and application scheduling. Other papers distinguish function-level or basic programming skills from software-level and scientific coding capabilities, and one paper describes basic coding proficiency as a prerequisite for more advanced repository-level software engineering tasks.

**Space of measurement.** Operationalization is dominated by benchmark evaluation: papers link the construct to 8 measurement instruments, with HumanEval and MBPP used most often, followed by HumanEval+, LiveBench, and LiveCodeBench, plus 3 other instruments. These benchmarks make the construct concrete mainly through code completion or generation, basic programming skills, Python programming problems, recent Leetcode and AtCoder questions, and coding subsets inside broader evaluations; one paper explicitly uses HumanEval for coding ability, and another describes MBPP as characterizing Python coding skills. Papers also link it to 2 behavioral indicators, which again center on producing or revising correct code, so broader definitions that include activities like review or visual problem-solving are less directly captured by the linked instruments.

**Links.** Papers link coding ability to 5 constructs and 2 behavioral indicators. Several papers claim causal relationships around it: from coding ability to mathematical reasoning, and from reasoning, self-correction, and one other construct to coding ability; the recorded evidence includes statements that training on code enhances mathematical reasoning and that self-debugging can enhance coding capability. Coding ability is also reported to correlate with computer science knowledge and to be related to code generation, plus one other construct.

## Sources

**Coding ability** (4 papers: [GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf), [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://aclanthology.org/2025.emnlp-main.167.pdf))
> The latent capability of a large language model to generate syntactically correct and semantically meaningful code to implement a specified task.

**Coding capability** (5 papers: [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf), [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf), [YuLan-Mini: Pushing the Limits of Open Data-efficient Language Model](https://aclanthology.org/2025.acl-long.268.pdf), [CopySpec: Accelerating LLMs with Speculative Copy-and-Paste](https://aclanthology.org/2025.emnlp-main.1337.pdf))
> The general ability of an LLM to produce correct code across programming tasks and languages.

**Coding skill** (1 paper: [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf))
> The model's proficiency in generating, understanding, and debugging computer code.

**Coding** (1 paper: [Reward-Shifted Speculative Sampling Is An Efficient Test-Time Weak-to-Strong Aligner](https://aclanthology.org/2025.emnlp-main.578.pdf))
> The ability to generate or manipulate code in response to programming-related prompts.

**Code programming** (1 paper: [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf))
> The latent ability to write, understand, and execute code to solve computational problems.

**Programming capability** (1 paper: [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf))
> A latent ability specifically related to code understanding and generation, identified as the third principal component of benchmark performance.

**Coding proficiency** (1 paper: [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf))
> The latent ability to generate, understand, and repair code across various programming tasks.

**Coding capabilities** (1 paper: [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf))
> The model's competence on programming-oriented tasks and benchmarks, treated here as a capability that should be preserved after fine-tuning.

**Programming ability** (1 paper: [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf))
> The model's capability in understanding and generating code, which is shown to be highly correlated with its performance in computer science.

**Coding skills** (1 paper: [MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf))
> The model's ability to understand and generate functional computer code.

**Programming skills** (1 paper: [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf))
> The ability to correctly write and structure functional code to solve a given programming problem.

**Python coding skill** (1 paper: [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.322.pdf))
> The latent ability to produce correct Python code for programming problems.

**Visual problem-solving** (1 paper: [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf))
> The ability of an AI system to understand and resolve software issues that require interpreting visual information, such as screenshots, diagrams, or user interface layouts.

## Relationships

### Coding ability →
- **HumanEval** (measurement instrument): *measured_by*, 14 papers
  > In this ection, we first assess the agents’ coding capabilities using the Humaneval code completion dataset. (Section 3.2)
  - [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf)
  - [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf)
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
  - [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf)
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
  - [From Informal to Formal – Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs](https://aclanthology.org/2025.acl-long.1310.pdf)
  - [Large Language Models to Diffusion Finetuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cetin25a/cetin25a.pdf)
  - [CopySpec: Accelerating LLMs with Speculative Copy-and-Paste](https://aclanthology.org/2025.emnlp-main.1337.pdf)
- **MBPP** (measurement instrument): *measured_by*, 9 papers
  > We assess all models on three categories of benchmarks: ... (iii) Coding ability on MBPP [6] and HumanEval [9] (Section 4.1).
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf)
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
  - [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf)
  - [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.322.pdf)
  - [From Informal to Formal – Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs](https://aclanthology.org/2025.acl-long.1310.pdf)
  - [Large Language Models to Diffusion Finetuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cetin25a/cetin25a.pdf)
- **Mathematical reasoning** (construct): *causes*, 2 papers
  > Various studies (Azerbayev et al., 2024; Shao et al., 2024) have shown that training on code enhances the mathematical reasoning abilities of large language models (LLMs). (Section 1)
  - [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/bea94fe9c5573e74294657f692069d89-Paper-Conference.pdf)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Vicuna-Bench** (measurement instrument): *measured_by*, 1 paper
  > Figure 4 illustrates the Llama-2-7B-star_instruct's performance enhancements across nine metrics, with notable substantial improvements in math, coding and fermi problem-solving... Figure 4: Radar plot of detailed scores for Llama-2-7B-star_instrcut against the major baseline on different subtasks of (a) Vicuna-Bench and (b) MT-Bench.
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **LiveBench** (measurement instrument): *measured_by*, 1 paper
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Computer science knowledge** (construct): *correlates*, 1 paper
  > we consider this evidence suggests a strong correlation between CS proficiency and skills in Math and Code. (Section 3.5)
  - [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf)
- **HumanEval+** (measurement instrument): *measured_by*, 1 paper
  > Table 8: Performance of various LLMs on HumanEval, HumanEval+, MBPP, and MBPP+ benchmarks... The fine-tuned LLMs maintain their coding capabilities.
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
- **LiveCodeBench** (measurement instrument): *measured_by*, 1 paper
  > “Coding: code generation questions from recent Leetcode and AtCoder questions (via LiveCodeBench (Jain et al., 2024))”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **RewardBench** (measurement instrument): *measured_by*, 1 paper
  > RewardBench contains subsets that test RMs in targeted domains, including their coding ability, mathematical ability, and harmlessness. (Section 3.3)
  - [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://aclanthology.org/2025.emnlp-main.167.pdf)
- **MBXP** (measurement instrument): *measured_by*, 1 paper
  > The final metrics were derived from the average HumanEval and MBXP performances across all five languages. (Section 4.3.3)
  - [The Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/9aa4e5caaf6d62767787500ee487c7fb-Paper-Conference.pdf)

### → Coding ability
- **Reasoning** (construct): *causes*, 2 papers
  > This limitation stems from the restricted reasoning abilities of single LLMs... they struggle to tackle more complex coding tasks.
  - [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > teaching large language models to perform SELF-DEBUGGING without human guidance is another promising path to enhance coding capability and reduce the sampling cost required to accomplish challenging tasks.
  - [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf)
- **Long-context understanding** (construct): *causes*, 1 paper
  > This limitation stems from the restricted reasoning abilities of single LLMs and their lack of capacity for long-context understanding... they struggle to tackle more complex coding tasks.
  - [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf)

### Associated with
- **Code generation** (behavioral indicator), 2 papers
  > For code generation, Luo et al. (2023b) adapt the evol-instruct method to the coding domain, resulting in the WIZARDCODER model, which demonstrates superior coding abilities compared to generally trained LLMs. (Section 1)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
- **Agency** (construct), 1 paper
  > We observe that the ﬁtted weights assign signiﬁcant importance to programming capabilities (HumanEval) on both benchmarks, underscoring its signiﬁcance in deﬁning the agentic capabilities of LMs. (Sec. 4.2)
  - [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
