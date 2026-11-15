# Code generation
**Type:** Behavioral indicator  
**Supporting papers:** 513  
**Also known as:** Code problem solving, Interactive coding, Function completion, Chart-to-code generation, Action execution program generation, Evaluation program generation, Visual program generation, Whole-function generation, Text-to-ES query generation, Feature function generation, Stub file generation, Backend application generation, Multi-agent system generation, Program generation, Standalone function implementation, Python code generation, Verilog code generation, Program synthesis, Code synthesis, Sequential edit generation, Policy-to-code translation, EDA code generation, LaTeX code generation, Cone code generation, Code comprehension and generation, Data visualization code generation, Mockup-to-code generation, Game code generation, Heuristic function generation, Text-to-Python generation, ORM code generation, Chart code generation, Reference image to slide generation, Slide code generation, Prolog program generation, Text-to-visualization generation, Visualization code generation, Repo-level code generation, Multilingual code generation, Function-level code generation, Class-level code generation, Data science programming, Text-to-code generation, Continuation writing, Code generation ability, Code generation capability, Verilog generation, Program synthesis capability, Dependency invocation, API invocation generation, Requirement fulfillment, Code implementation, Programming language generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats code generation as a task or output pattern: producing executable or functionally correct source code from a natural-language description, prompt, docstring, or other specification. Many papers make success execution-based, requiring the code to be syntactically valid and to pass test cases, hidden tests, or other correctness checks, while some describe it more loosely as producing code snippets, tokens, or completions. A smaller line uses the same label for a model ability or capability to produce such code, rather than for the task itself.

**Variants.** Variants are most often function-oriented, including function completion from signatures and docstrings, standalone or whole-function generation, and class-level or repository-level generation. Another cluster uses program synthesis or code synthesis framings, including sequential edit generation and programs that invoke dependencies or APIs, and papers also single out language-specific forms such as Python, multilingual code, and Verilog. A smaller multimodal line studies chart-to-code and visual program generation, alongside mockup-to-code or slide generation, and one paper treats interactive coding as solving filesystem tasks with Bash commands.

**Space of elicitation and scores.** Papers link code generation to 29 measurement instruments, most often HumanEval and MBPP, followed by APPS, LiveCodeBench, and EvalPlus. These are typically benchmark datasets or evaluation suites, and the common scoring pattern is execution or pass-based checking on test cases: papers describe HumanEval and MBPP as function-oriented Python tasks, APPS as competitive programming, LiveCodeBench as contamination-free code generation, and EvalPlus as augmented test suites for HumanEval and MBPP. Many other instruments are also linked, spanning multilingual, data science, class-level, and web or chart settings.

**What it is taken as evidence of.** Papers link code generation to 15 constructs, but they do not converge on a single construct it reflects. The most prevalent connection is with Reasoning: several papers claim a causal relationship from Reasoning to code generation, while one paper claims a causal relationship from code-generation data to Reasoning. It is also reported as related to Coding ability and Algorithmic reasoning, and papers claim causal relationships from Planning and Expressive power to code generation; other papers connect it to additional constructs in both causal and related terms.

## Sources

**Code problem solving** (2 papers: [The Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/9aa4e5caaf6d62767787500ee487c7fb-Paper-Conference.pdf), [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf))
> The task of generating functionally correct code that solves a given programming problem, typically described in natural language.

**Code generation** (83 papers: [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf), [Substance Beats Style: Why Beginning Students Fail to Code with LLMs](https://aclanthology.org/2025.naacl-long.433.pdf), [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf), [Waste Not, Want Not; Recycled Gumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.292.pdf), [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf), [Knowledge Graph-Guided Retrieval Augmented Generation](https://aclanthology.org/2025.naacl-long.449.pdf), [Language Models can Categorize System Inputs for Performance Analysis](https://aclanthology.org/2025.naacl-long.317.pdf), [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf), [CodeSCM: Causal Analysis for Multi-Modal Code Generation](https://aclanthology.org/2025.naacl-long.345.pdf), [SLIM: Let LLM Learn More and Forget Less with Soft LoRA and Identity Mixture](https://aclanthology.org/2025.naacl-long.246.pdf), [Dynamic Data Mixing Maximizes Instruction Tuning for Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.80.pdf), [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf), [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning](https://aclanthology.org/2025.naacl-long.519.pdf), [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf), [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf), [TurtleBench: A Visual Programming Benchmark in Turtle Geometry](https://aclanthology.org/2025.naacl-long.607.pdf), [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf), [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.245.pdf), [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf), [C2: Scalable Auto-Feedback for LLM-based Chart Generation](https://aclanthology.org/2025.naacl-long.232.pdf), [MoDification: Mixture of Depths Made Easy](https://aclanthology.org/2025.naacl-long.265.pdf), [CVE-Bench: Benchmarking LLM-based Software Engineering Agent's Ability to Repair Real-World CVE Vulnerabilities](https://aclanthology.org/2025.naacl-long.212.pdf), [Benchmarking Language Model Creativity: A Case Study on Code Generation](https://aclanthology.org/2025.naacl-long.141.pdf), [mHumanEval - A Multilingual Benchmark to Evaluate Large Language Models for Code Generation](https://aclanthology.org/2025.naacl-long.570.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf), [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf), [ELABORATION: A Comprehensive Benchmark on Human-LLM Competitive Programming](https://aclanthology.org/2025.acl-long.4.pdf), [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf), [Limits of Transformer Language Models on Learning to Compose Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e797d5139ad94fc2dc2080c09119f29-Paper-Conference.pdf), [#InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/9dae2a90bae49dc874ce1ca8fcc20879-Paper-Conference.pdf), [$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf), [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf), [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf), [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf), [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf), [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf), [BESA: Pruning Large Language Models with Blockwise Parameter-Efficient Sparsity Allocation](https://proceedings.iclr.cc/paper_files/paper/2024/file/21e315d40ac1db66c80c78e86a447ca1-Paper-Conference.pdf), [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf), [CODE REPRESENTATION LEARNING AT SCALE](https://proceedings.iclr.cc/paper_files/paper/2024/file/cfbba5249393100ada0bfb37557d2fd9-Paper-Conference.pdf), [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf), [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf), [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf), [Eureka: Human-Level Reward Design via Coding Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf), [ExeDec: Execution Decomposition for Compositional Generalization in Neural Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/c43b2989b1ba055aa713a4abbe4a8b05-Paper-Conference.pdf), [GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf), [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf), [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf), [Knowledge Fusion of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4fd5cfd2e31bebbccfa5ffa354c04bdc-Paper-Conference.pdf), [L2MAC: Large Language Model Automatic Computer for Extensive Code Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/9e74900c3f6100c56add4bf417547848-Paper-Conference.pdf), [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf), [LLM-Assisted Code Cleaning For Training Accurate Code Generators](https://proceedings.iclr.cc/paper_files/paper/2024/file/41137f3997ade899893ccd3973592d4b-Paper-Conference.pdf), [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf), [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf), [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf), [Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf), [LayoutNUWA: Revealing the Hidden Layout Expertise of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6a1e4c756d700d9aedcc1896a7e6fb0-Paper-Conference.pdf), [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a0d3ae989a382ce6e50312bc35bf7e1-Paper-Conference.pdf), [MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/15425f2df99aa1ba52712c9a4afc8536-Paper-Conference.pdf), [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf), [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://proceedings.iclr.cc/paper_files/paper/2024/file/6507b115562bb0a305f1958ccc87355a-Paper-Conference.pdf), [Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/639a9a172c044fbb64175b5fad42e9a5-Paper-Conference.pdf), [Predicting Emergent Abilities with Infinite Resolution Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e6d14709eae0cbc49a1d19d87fb8b21-Paper-Conference.pdf), [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf), [Raidar: geneRative AI Detection viA Rewriting](https://proceedings.iclr.cc/paper_files/paper/2024/file/1888b9df34b0d9eea6e009a1fdd55c4f-Paper-Conference.pdf), [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf), [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf), [Test-Time Training on Nearest Neighbors for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f02f1185b97518ab5bd7ebde466992d3-Paper-Conference.pdf), [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf), [To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d04d97593c8c33d415337f408ed0e1b-Paper-Conference.pdf), [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf), [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf), [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf), [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf), [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf), [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf), [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf), [Surge: On the Potential of Large Language Models as General-Purpose Surrogate Code Executors](https://aclanthology.org/2025.emnlp-main.162.pdf))
> The task of producing functional source code in a programming language based on a natural language description or other specifications.

**Interactive coding** (1 paper: [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf))
> The task of solving filesystem manipulation problems by issuing a sequence of Bash commands in an interactive terminal.

**Function completion** (1 paper: [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf))
> A specific code generation task where the model must complete the body of a function given its signature and docstring.

**Chart-to-code generation** (2 papers: [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf), [ChartCoder: Advancing Multimodal Large Language Model for Chart-to-Code Generation](https://aclanthology.org/2025.acl-long.363.pdf))
> Generating executable code from a chart image and textual instruction so that the code reproduces or modifies the chart.

**Visual program generation** (2 papers: [Retrieval-Augmented Fine-Tuning With Preference Optimization For Visual Program Generation](https://aclanthology.org/2025.acl-long.1106.pdf), [Understanding Complexity in VideoQA via Visual Program Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eyzaguirre25a/eyzaguirre25a.pdf))
> The task of generating code for a visual programming language, typically in a text-based format like XML, JSON, or a metaprogram, based on a user's natural language instruction.

**Whole-function generation** (1 paper: [Can Language Models Replace Programmers for Coding? REPOCOD Says `Not Yet'](https://aclanthology.org/2025.acl-long.1204.pdf))
> Generating complete function bodies from natural language descriptions and repository context, as opposed to single-line or partial code completions.

**Action execution program generation** (1 paper: [ASPERA: A Simulated Environment to Evaluate Planning for Complex Action Execution](https://aclanthology.org/2025.acl-long.1234.pdf))
> Producing a Python program that satisfies a user's natural language request by composing primitives from an assistant library, including proper use of control flow and function calls.

**Evaluation program generation** (1 paper: [ASPERA: A Simulated Environment to Evaluate Planning for Complex Action Execution](https://aclanthology.org/2025.acl-long.1234.pdf))
> Generating a program that executes an action execution program and verifies its correctness through assertions that check goal completion and absence of side effects.

**Text-to-ES query generation** (1 paper: [Text-to-ES Bench: A Comprehensive Benchmark for Converting Natural Language to Elasticsearch Query](https://aclanthology.org/2025.acl-long.971.pdf))
> The specific task of converting a natural language question into an executable Elasticsearch (ES) query, which may include both a DSL query body and post-processing code.

**Feature function generation** (1 paper: [ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25at/chen25at.pdf))
> The observable action of generating structured, executable code, specifically Python functions, that represents task-relevant features based on multimodal inputs.

**Stub file generation** (1 paper: [TypyBench: Evaluating LLM Type Inference for Untyped Python Repositories](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25l/dong25l.pdf))
> Producing a .pyi file containing only type annotations for functions and variables in a corresponding untyped Python file, preserving the original function signatures without implementation.

**Program generation** (3 papers: [GRAIL: Graph Edit Distance and Node Alignment using LLM-Generated Code](https://raw.githubusercontent.com/mlresearch/v267/main/assets/verma25a/verma25a.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.289.pdf))
> The process by which the LLM produces executable code that computes or approximates Graph Edit Distance based on input graph pairs.

**Backend application generation** (1 paper: [BaxBench: Can LLMs Generate Correct and Secure Backends?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vero25a/vero25a.pdf))
> Producing a complete, self-contained backend application with multiple files and functions that implements specified API endpoints and handles requests correctly.

**Multi-agent system generation** (1 paper: [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf))
> The task of generating an executable code representation of a multi-agent system based on a natural language user query.

**Standalone function implementation** (1 paper: [Synthesizing Software Engineering Data in a Test-Driven Manner](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cn/zhang25cn.pdf))
> The task of writing a single, self-contained function based on a given specification, without dependencies on a larger codebase.

**Python code generation** (3 papers: [Syntactic and Semantic Control of Large Language Models via Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf), [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf), [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.322.pdf))
> The task of generating Python code, particularly for data science applications, to solve a problem specified in natural language and via test cases.

**Verilog code generation** (1 paper: [CraftRTL: High-quality Synthetic Data Generation for Verilog Code Models with Correct-by-Construction Non-Textual Representations and Targeted Code Repair](https://proceedings.iclr.cc/paper_files/paper/2025/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf))
> The task of producing functionally correct Verilog code from a natural language or non-textual problem description.

**Program synthesis** (7 papers: [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf), [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf), [Program Synthesis Benchmark for Visual Programming in XLogoOnline Environment](https://aclanthology.org/2025.acl-long.769.pdf), [LILO: Learning Interpretable Libraries by Compressing and Documenting Code](https://proceedings.iclr.cc/paper_files/paper/2024/file/819cebb05f993840e8a52d7564c5c282-Paper-Conference.pdf), [Flexible and Efficient Grammar-Constrained Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25l/park25l.pdf), [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf))
> Generating executable programs that implement environment dynamics or solve coding problems from specifications and examples.

**Code synthesis** (3 papers: [LLMDFA: Analyzing Dataflow in Code with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9dcde1eb9c597f68c1d375bbecf3fc-Paper-Conference.pdf), [LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://aclanthology.org/2025.emnlp-main.314.pdf), [OctoPack: Instruction Tuning Code Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1ec299a5229034141e58aeded0d0b9de-Paper-Conference.pdf))
> Generating scripts that implement source/sink extraction or path-condition solving using external libraries and solvers.

**Sequential edit generation** (1 paper: [Training Language Models on Synthetic Edit Sequences Improves Code Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43f900f571de6c96a70d5724a0fb565-Paper-Conference.pdf))
> The observable process of generating a program as a sequence of incremental insertion edits, rather than producing the entire program in a single pass.

**Policy-to-code translation** (1 paper: [PricingLogic: Evaluating LLMs Reasoning on Complex Tourism Pricing Tasks](https://aclanthology.org/2025.emnlp-main.393.pdf))
> The specific task of converting natural language policy documents into executable functions in a programming language.

**LaTeX code generation** (1 paper: [Do Slides Help? Multi-modal Context for Automatic Transcription of Conference Talks](https://aclanthology.org/2025.emnlp-main.814.pdf))
> The task of generating compilable LaTeX source code from a textual description or prompt.

**EDA code generation** (1 paper: [Reliable and Cost-Effective Exploratory Data Analysis via Graph-Guided RAG](https://aclanthology.org/2025.emnlp-main.836.pdf))
> The task of automatically producing executable Python code to perform Exploratory Data Analysis (EDA) on a given dataset.

**Cone code generation** (1 paper: [SynC-LLM: Generation of Large-Scale Synthetic Circuit Code with Hierarchical Language Models](https://aclanthology.org/2025.emnlp-main.877.pdf))
> Generating HDL code for combinational logic cones that determine the next state of a register, based on functional descriptions and I/O constraints.

**Code comprehension and generation** (1 paper: [Priority on High-Quality: Selecting Instruction Data via Consistency Verification of Noise Injection](https://aclanthology.org/2025.emnlp-main.1048.pdf))
> The observable task of understanding and producing computer code based on a natural language prompt.

**Coding** (1 paper: [Reinforcement Learning for Large Language Models via Group Preference Reward Shaping](https://aclanthology.org/2025.emnlp-main.1085.pdf))
> The task of generating executable source code in a programming language based on a natural language description.

**Mockup-to-code generation** (1 paper: [WebMMU: A Benchmark for Multimodal Multilingual Website Understanding and Code Generation](https://aclanthology.org/2025.emnlp-main.1276.pdf))
> The task of generating structured HTML and CSS code from a visual representation of a webpage, such as a hand-drawn sketch or a digital mockup.

**Data visualization code generation** (1 paper: [Identifying & Interactively Refining Ambiguous User Goals for Data Visualization Code Generation](https://aclanthology.org/2025.emnlp-main.1283.pdf))
> The observable task of producing executable code that creates a data plot or visualization based on a natural language prompt.

**Game code generation** (1 paper: [Cardiverse: Harnessing LLMs for Novel Card Game Prototyping](https://aclanthology.org/2025.emnlp-main.1511.pdf))
> Producing executable game code from a natural-language description of game mechanics.

**Heuristic function generation** (1 paper: [Cardiverse: Harnessing LLMs for Novel Card Game Prototyping](https://aclanthology.org/2025.emnlp-main.1511.pdf))
> Converting natural language strategies into executable Python functions that score candidate actions based on game state.

**Text-to-Python generation** (1 paper: [STARQA: A Question Answering Dataset for Complex Analytical Reasoning over Structured Databases](https://aclanthology.org/2025.emnlp-main.1749.pdf))
> Generating Python code from natural language instructions to perform data processing, computation, or reasoning tasks not easily expressible in SQL.

**ORM code generation** (1 paper: [Dialect-SQL: An Adaptive Framework for Bridging the Dialect Gap in Text-to-SQL](https://aclanthology.org/2025.emnlp-main.178.pdf))
> The task of generating Object Relational Mapping (ORM) code from a natural language question, which serves as a dialect-agnostic intermediate representation.

**Chart code generation** (1 paper: [AMACE: Automatic Multi-Agent Chart Evolution for Iteratively Tailored Chart Generation](https://aclanthology.org/2025.emnlp-main.1089.pdf))
> Producing executable code (e.g., Python with matplotlib) that renders a data table into a visual chart according to specified conditions.

**Reference image to slide generation** (1 paper: [SlideCoder: Layout-aware RAG-enhanced Hierarchical Slide Generation from Design](https://aclanthology.org/2025.emnlp-main.458.pdf))
> The task of automatically generating executable code to create an editable slide that is visually and structurally consistent with a given reference image.

**Slide code generation** (1 paper: [SlideCoder: Layout-aware RAG-enhanced Hierarchical Slide Generation from Design](https://aclanthology.org/2025.emnlp-main.458.pdf))
> Producing Python code using the python-pptx library that, when executed, generates a slide matching a reference image in layout and visual appearance.

**Prolog program generation** (1 paper: [Predicate-Guided Generation for Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.462.pdf))
> The production of an executable Prolog program that encodes logical constraints from a math problem and yields a symbolic answer upon execution.

**Text-to-visualization generation** (1 paper: [Text2Vis: A Challenging and Diverse Benchmark for Generating Multimodal Visualizations from Text](https://aclanthology.org/2025.emnlp-main.1622.pdf))
> Producing visualization code and a chart from a natural-language query and data table.

**Visualization code generation** (1 paper: [Text2Vis: A Challenging and Diverse Benchmark for Generating Multimodal Visualizations from Text](https://aclanthology.org/2025.emnlp-main.1622.pdf))
> Producing executable Python code using libraries like Matplotlib or Seaborn to generate a chart from a data table and natural language query.

**Repo-level code generation** (1 paper: [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf))
> Generating code for a target function given a natural language requirement and repository context, simulating real-world developer coding processes.

**Multilingual code generation** (1 paper: [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf))
> The task of generating functionally correct code in various programming languages, such as Python, C++, Java, JavaScript, and Go.

**Function-level code generation** (1 paper: [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf))
> The task of generating a complete, self-contained function based on a natural language description of its purpose and behavior.

**Class-level code generation** (1 paper: [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf))
> The task of generating the implementation of a class and its methods, given a code skeleton containing class- and method-level information.

**Data science programming** (1 paper: [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf))
> The task of completing a partial code snippet to solve a data science problem, often involving specific libraries and data manipulation techniques.

**Text-to-code generation** (1 paper: [Reranking Laws for Language Generation: A Communication-Theoretic Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/c8b2f897e45770595656a79a9ad91e89-Paper-Conference.pdf))
> The task of generating executable source code from a natural language description or prompt.

**Continuation writing** (1 paper: [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf))
> The behavior of completing a partial, incomplete SQL query to form a complete and valid query that answers a given question.

**Code generation ability** (5 papers: [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf), [MaestroMotif: Skill Design from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/2dc5a0faac8102fd47363795f71126ee-Paper-Conference.pdf), [ChartCoder: Advancing Multimodal Large Language Model for Chart-to-Code Generation](https://aclanthology.org/2025.acl-long.363.pdf), [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf))
> The latent aptitude of a large language model to generate correct and functional code snippets from natural language specifications.

**Code generation capability** (5 papers: [Can Large Language Models Analyze Graphs like Professionals? A Benchmark, Datasets and Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff417c3993894694e88ffc4d3f53d28b-Paper-Datasets_and_Benchmarks_Track.pdf), [Real2Code: Reconstruct Articulated Objects via Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/028fcbcf85435d39a40c4d61b42c99a4-Paper-Conference.pdf), [WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models](https://aclanthology.org/2025.acl-long.246.pdf), [Automated Benchmark Generation for Repository-Level Coding Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vergopoulos25a/vergopoulos25a.pdf), [Learning from Few Samples: A Novel Approach for High-Quality Malcode Generation](https://aclanthology.org/2025.emnlp-main.70.pdf))
> The latent ability of a model to produce syntactically correct and functional programming code to solve specified problems.

**Verilog generation** (1 paper: [DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf))
> The latent ability of a model to produce syntactically correct and functionally accurate Verilog code from natural language specifications.

**Program synthesis capability** (1 paper: [LLMDFA: Analyzing Dataflow in Code with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9dcde1eb9c597f68c1d375bbecf3fc-Paper-Conference.pdf))
> The latent ability to generate executable code or scripts that implement analysis logic or invoke external tools.

**Dependency invocation** (1 paper: [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf))
> The observable behavior of a model generating code that calls or uses other functions, classes, or modules defined within the provided context.

**API invocation generation** (1 paper: [CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25t/wang25t.pdf))
> The observable behavior of generating a specific line or block of code that calls a function, method, or class initializer from an external library.

**Requirement fulfillment** (1 paper: [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf))
> Producing code that satisfies itemized software requirements and passes corresponding verification tests.

**Code implementation** (1 paper: [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf))
> The task of generating functional source code based on a natural language description or problem statement.

**Programming language generation** (1 paper: [Prototype Conditioned Generative Replay for Continual Learning in NLP](https://aclanthology.org/2025.naacl-long.636.pdf))
> The task of generating source code in a specific programming language.

## Relationships

### Code generation →
- **HumanEval** (measurement instrument): *measured_by*, 131 papers
  > We evaluate SEC in the following tasks and datasets (details in Appendix A.1): ... Code Generation: HumanEval (Chen et al., 2021). (Section 3.1)
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
  - [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf)
  - [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf)
  - [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf)
  - [Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bc4f74e35bcfe8cfe43b0a860786d6a-Paper-Conference.pdf)
  - [Parameter Competition Balancing for Model Merging](https://proceedings.neurips.cc/paper_files/paper/2024/file/99fc8bc48b917c301a80cb74d91c0c06-Paper-Conference.pdf)
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
  - [Can Large Language Models Analyze Graphs like Professionals? A Benchmark, Datasets and Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff417c3993894694e88ffc4d3f53d28b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Unchosen Experts Can Contribute Too: Unleashing MoE Models’ Power by Self-Contrast](https://proceedings.neurips.cc/paper_files/paper/2024/file/f77012b463892a3f2ac56d3a6086fc5b-Paper-Conference.pdf)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [Judge Decoding: Faster Speculative Sampling Requires Going Beyond Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/656d6174fd5ffb01c843f269649ab5cb-Paper-Conference.pdf)
  - [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf)
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
  - [InstructRAG: Instructing Retrieval-Augmented Generation via Self-Synthesized Rationales](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdce0de17dc3cf97019a35baa65aebd0-Paper-Conference.pdf)
  - [Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d022216357816e483433914204aa80ee-Paper-Conference.pdf)
  - [Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf)
  - [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf)
  - [PEARL: Parallel Speculative Decoding with Adaptive Draft Length](https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf)
  - [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [Mixture of Attentions For Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f31bf160569618084ba9bdc2a8de29d0-Paper-Conference.pdf)
  - [Model Equality Testing: Which Model is this API Serving?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d73234a13815fc1f9779dd17d89be9b4-Paper-Conference.pdf)
  - [AFlow: Automating Agentic Workflow Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5492ecbce4439401798dcd2c90be94cd-Paper-Conference.pdf)
  - [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf)
  - [Learning Harmonized Representations for Speculative Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/575286a73f238b6516ce0467d67eadb2-Paper-Conference.pdf)
  - [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf)
  - [Distributed Speculative Inference (DSI): Speculation Parallelism for Provably Faster Lossless Language Model Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/b36554b97da741b1c48c9de05c73993e-Paper-Conference.pdf)
  - [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbc461518c59a2a8d64e70e2c38c4a0e-Paper-Conference.pdf)
  - [Training Language Models to Self-Correct via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf)
  - [The Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/9aa4e5caaf6d62767787500ee487c7fb-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Leveraging Submodule Linearity Enhances Task Arithmetic Performance in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c983bf84ddbf8c71b2fd19a9d48186b-Paper-Conference.pdf)
  - [Commit0: Library Generation from Scratch](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fcefa894924bb1688041b7a26fb8aea-Paper-Conference.pdf)
  - [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf)
  - [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf)
  - [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf)
  - [mHumanEval - A Multilingual Benchmark to Evaluate Large Language Models for Code Generation](https://aclanthology.org/2025.naacl-long.570.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
  - [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf)
  - [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
  - [Fusing Highly Specialized Language Models for Comprehensive Expertise](https://aclanthology.org/2025.acl-long.42.pdf)
  - [Faster Speculative Decoding via Effective Draft Decoder with Pruned Candidate Tree](https://aclanthology.org/2025.acl-long.486.pdf)
  - [“Give Me BF16 or Give Me Death”? Accuracy-Performance Trade-Offs in LLM Quantization](https://aclanthology.org/2025.acl-long.1304.pdf)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [Refining Salience-Aware Sparse Fine-Tuning Strategies for Language Models](https://aclanthology.org/2025.acl-long.1541.pdf)
  - [Neural Incompatibility: The Unbridgeable Gap of Cross-Scale Parametric Knowledge Transfer in Large Language Models](https://aclanthology.org/2025.acl-long.1047.pdf)
  - [LESA: Learnable LLM Layer Scaling-Up](https://aclanthology.org/2025.acl-long.1095.pdf)
  - [MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.240.pdf)
  - [WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models](https://aclanthology.org/2025.acl-long.246.pdf)
  - [Learning to Reason from Feedback at Test-Time](https://aclanthology.org/2025.acl-long.262.pdf)
  - [Watermarking Large Language Models: An Unbiased and Low-risk Method](https://aclanthology.org/2025.acl-long.391.pdf)
  - [SPECTRA: Faster Large Language Model Inference with Optimized Internal and External Speculation](https://aclanthology.org/2025.acl-long.685.pdf)
  - [Adapt Once, Thrive with Updates: Transferable Parameter-Efficient Fine-Tuning on Evolving Base Models](https://aclanthology.org/2025.acl-long.719.pdf)
  - [IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory](https://aclanthology.org/2025.acl-long.761.pdf)
  - [LongRecipe: Recipe for Efficient Long Context Generalization in Large Language Models](https://aclanthology.org/2025.acl-long.581.pdf)
  - [BeamLoRA: Beam-Constraint Low-Rank Adaptation](https://aclanthology.org/2025.acl-long.582.pdf)
  - [SAM Decoding: Speculative Decoding via Suffix Automaton](https://aclanthology.org/2025.acl-long.595.pdf)
  - [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.621.pdf)
  - [SCAR: Data Selection via Style Consistency-Aware Response Ranking for Efficient Instruction-Tuning of Large Language Models](https://aclanthology.org/2025.acl-long.625.pdf)
  - [Qwen2.5-xCoder: Multi-Agent Collaboration for Multilingual Code Instruction Tuning](https://aclanthology.org/2025.acl-long.642.pdf)
  - [ImPart: Importance-Aware Delta-Sparsification for Improved Model Compression and Merging in LLMs](https://aclanthology.org/2025.acl-long.921.pdf)
  - [CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/min25b/min25b.pdf)
  - [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf)
  - [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf)
  - [LoRA-One: One-Step Full Gradient Could Suffice for Fine-Tuning Large Language Models, Provably and Efficiently](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ax/zhang25ax.pdf)
  - [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf)
  - [Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf)
  - [Synthesizing Software Engineering Data in a Test-Driven Manner](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cn/zhang25cn.pdf)
  - [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cu/zhang25cu.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
  - [Automated Benchmark Generation for Repository-Level Coding Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vergopoulos25a/vergopoulos25a.pdf)
  - [Gumiho: A Hybrid Architecture to Prioritize Early Tokens in Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dg/li25dg.pdf)
  - [Boosting Multi-Domain Fine-Tuning of Large Language Models through Evolving Interactions between Samples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25q/liang25q.pdf)
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
  - [SeedLoRA: A Fusion Approach to Efficient LLM Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25o/liu25o.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
  - [LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf)
  - [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf)
  - [Make LoRA Great Again: Boosting LoRA with Adaptive Singular Values and Mixture-of-Experts Optimization Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25g/fan25g.pdf)
  - [Fast Large Language Model Collaborative Decoding via Speculation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25c/fu25c.pdf)
  - [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aa/chen25aa.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ay/huang25ay.pdf)
  - [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf)
  - [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf)
  - [EpiCoder: Encompassing Diversity and Complexity in Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bi/wang25bi.pdf)
  - [NICE Data Selection for Instruction Tuning in LLMs with Non-differentiable Evaluation Metric](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bm/wang25bm.pdf)
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [EcoTune: Token-Efficient Multi-Fidelity Hyperparameter Optimization for Large Language Model Inference](https://aclanthology.org/2025.emnlp-main.394.pdf)
  - [Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment](https://aclanthology.org/2025.emnlp-main.406.pdf)
  - [Alignment with Fill-In-the-Middle for Enhancing Code Generation](https://aclanthology.org/2025.emnlp-main.419.pdf)
  - [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf)
  - [Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality](https://aclanthology.org/2025.emnlp-main.1138.pdf)
  - [Compound AI Systems Optimization: A Survey of Methods, Challenges, and Future Directions](https://aclanthology.org/2025.emnlp-main.1463.pdf)
  - [CLMTracing: Black-box User-level Watermarking for Code Language Model Tracing](https://aclanthology.org/2025.emnlp-main.1475.pdf)
  - [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf)
  - [Dovetail: A CPU/GPU Heterogeneous Speculative Decoding for LLM inference](https://aclanthology.org/2025.emnlp-main.879.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [Group-Aware Reinforcement Learning for Output Diversity in Large Language Models](https://aclanthology.org/2025.emnlp-main.1649.pdf)
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
  - [ReSo: A Reward-driven Self-organizing LLM-based Multi-Agent System for Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.808.pdf)
  - [ZERA: Zero-init Instruction Evolving Refinement Agent – From Zero Instructions to Structured Prompts via Principle-based Optimization](https://aclanthology.org/2025.emnlp-main.1190.pdf)
  - [Firewall Routing: Blocking Leads to Better Hybrid Inference for LLMs](https://aclanthology.org/2025.emnlp-main.331.pdf)
  - [Invisible Entropy: Towards Safe and Efficient Low-Entropy LLM Watermarking](https://aclanthology.org/2025.emnlp-main.341.pdf)
  - [Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning](https://aclanthology.org/2025.emnlp-main.350.pdf)
  - [Arena-lite: Efficient and Reliable Large Language Model Evaluation via Tournament-Based Direct Comparisons](https://aclanthology.org/2025.emnlp-main.360.pdf)
  - [AnyMAC: Cascading Flexible Multi-Agent Collaboration via Next-Agent Prediction](https://aclanthology.org/2025.emnlp-main.584.pdf)
  - [Understanding the Information Propagation Effects of Communication Topologies in LLM-based Multi-Agent Systems](https://aclanthology.org/2025.emnlp-main.623.pdf)
  - [Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLMs](https://aclanthology.org/2025.emnlp-main.1754.pdf)
- **MBPP** (measurement instrument): *measured_by*, 79 papers
  > Text-to-Code (T2C): Given a textual context, the model is prompted to generate the corresponding code snippet. ... We perform 3-shot inference on the MBPP dataset (Austin et al., 2021) and report P@1. (Section 4.3)
  - [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf)
  - [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf)
  - [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf)
  - [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf)
  - [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf)
  - [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf)
  - [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf)
  - [Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bc4f74e35bcfe8cfe43b0a860786d6a-Paper-Conference.pdf)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
  - [Reranking Laws for Language Generation: A Communication-Theoretic Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/c8b2f897e45770595656a79a9ad91e89-Paper-Conference.pdf)
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [Can Large Language Models Analyze Graphs like Professionals? A Benchmark, Datasets and Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff417c3993894694e88ffc4d3f53d28b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf)
  - [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf)
  - [Unchosen Experts Can Contribute Too: Unleashing MoE Models’ Power by Self-Contrast](https://proceedings.neurips.cc/paper_files/paper/2024/file/f77012b463892a3f2ac56d3a6086fc5b-Paper-Conference.pdf)
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
  - [SciInstruct: a Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02ee6b7295f720407b56c457b34c54d5-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
  - [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
  - [Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [AFlow: Automating Agentic Workflow Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5492ecbce4439401798dcd2c90be94cd-Paper-Conference.pdf)
  - [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf)
  - [Distributed Speculative Inference (DSI): Speculation Parallelism for Provably Faster Lossless Language Model Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/b36554b97da741b1c48c9de05c73993e-Paper-Conference.pdf)
  - [ADePT: Adaptive Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/93e45db754dd0f82339763055c6cda56-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Fine-tuning with Reserved Majority for Noise Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/4b6898c70d5b328deaf2216aefd8f77a-Paper-Conference.pdf)
  - [Dynamic Data Mixing Maximizes Instruction Tuning for Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.80.pdf)
  - [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf)
  - [mHumanEval - A Multilingual Benchmark to Evaluate Large Language Models for Code Generation](https://aclanthology.org/2025.naacl-long.570.pdf)
  - [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf)
  - [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [Refining Salience-Aware Sparse Fine-Tuning Strategies for Language Models](https://aclanthology.org/2025.acl-long.1541.pdf)
  - [Neural Incompatibility: The Unbridgeable Gap of Cross-Scale Parametric Knowledge Transfer in Large Language Models](https://aclanthology.org/2025.acl-long.1047.pdf)
  - [LESA: Learnable LLM Layer Scaling-Up](https://aclanthology.org/2025.acl-long.1095.pdf)
  - [WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models](https://aclanthology.org/2025.acl-long.246.pdf)
  - [Learning to Reason from Feedback at Test-Time](https://aclanthology.org/2025.acl-long.262.pdf)
  - [Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks](https://aclanthology.org/2025.acl-long.317.pdf)
  - [SPECTRA: Faster Large Language Model Inference with Optimized Internal and External Speculation](https://aclanthology.org/2025.acl-long.685.pdf)
  - [Adapt Once, Thrive with Updates: Transferable Parameter-Efficient Fine-Tuning on Evolving Base Models](https://aclanthology.org/2025.acl-long.719.pdf)
  - [IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory](https://aclanthology.org/2025.acl-long.761.pdf)
  - [BeamLoRA: Beam-Constraint Low-Rank Adaptation](https://aclanthology.org/2025.acl-long.582.pdf)
  - [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.621.pdf)
  - [Qwen2.5-xCoder: Multi-Agent Collaboration for Multilingual Code Instruction Tuning](https://aclanthology.org/2025.acl-long.642.pdf)
  - [ImPart: Importance-Aware Delta-Sparsification for Improved Model Compression and Merging in LLMs](https://aclanthology.org/2025.acl-long.921.pdf)
  - [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf)
  - [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf)
  - [Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf)
  - [Synthesizing Software Engineering Data in a Test-Driven Manner](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cn/zhang25cn.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
  - [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf)
  - [Optimizing Temperature for Language Models with Multi-Sample Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25f/du25f.pdf)
  - [Text-to-LoRA: Instant Transformer Adaption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/charakorn25a/charakorn25a.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf)
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
  - [EpiCoder: Encompassing Diversity and Complexity in Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bi/wang25bi.pdf)
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [Alignment with Fill-In-the-Middle for Enhancing Code Generation](https://aclanthology.org/2025.emnlp-main.419.pdf)
  - [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf)
  - [RLAE: Reinforcement Learning-Assisted Ensemble for LLMs](https://aclanthology.org/2025.emnlp-main.680.pdf)
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf)
  - [Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality](https://aclanthology.org/2025.emnlp-main.1138.pdf)
  - [Compound AI Systems Optimization: A Survey of Methods, Challenges, and Future Directions](https://aclanthology.org/2025.emnlp-main.1463.pdf)
  - [CLMTracing: Black-box User-level Watermarking for Code Language Model Tracing](https://aclanthology.org/2025.emnlp-main.1475.pdf)
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
  - [ZERA: Zero-init Instruction Evolving Refinement Agent – From Zero Instructions to Structured Prompts via Principle-based Optimization](https://aclanthology.org/2025.emnlp-main.1190.pdf)
  - [Invisible Entropy: Towards Safe and Efficient Low-Entropy LLM Watermarking](https://aclanthology.org/2025.emnlp-main.341.pdf)
  - [Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning](https://aclanthology.org/2025.emnlp-main.350.pdf)
- **APPS** (measurement instrument): *measured_by*, 14 papers
  > In line with prior RL-based works (Le et al., 2022; Shojaee et al., 2023; Liu et al., 2023), we evaluate B-Coder on the challenging code contests benchmark APPS (Hendrycks et al., 2021). (Section 5)
  - [$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf)
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf)
  - [DeFT: Decoding with Flash Tree-attention for Efficient Tree-structured LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6df53f082619d02b9fad64a022e5de3-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf)
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
  - [Personality-Guided Code Generation Using Large Language Models](https://aclanthology.org/2025.acl-long.54.pdf)
  - [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.621.pdf)
  - [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf)
  - [RethinkMCTS: Refining Erroneous Thoughts in Monte Carlo Tree Search for Code Generation](https://aclanthology.org/2025.emnlp-main.410.pdf)
  - [Alignment with Fill-In-the-Middle for Enhancing Code Generation](https://aclanthology.org/2025.emnlp-main.419.pdf)
- **LiveCodeBench** (measurement instrument): *measured_by*, 13 papers
  > LiveCodeBench [21] is a benchmark for contamination-free evaluation. ... we focus on the code generation task for assessing LLM function generation. (Section 3.1)
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf)
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
  - [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
  - [AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aq/liu25aq.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [Alignment with Fill-In-the-Middle for Enhancing Code Generation](https://aclanthology.org/2025.emnlp-main.419.pdf)
  - [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf)
  - [AlphaOne: Reasoning Models Thinking Slow and Fast at Test Time](https://aclanthology.org/2025.emnlp-main.570.pdf)
  - [Process-Supervised Reinforcement Learning for Code Generation](https://aclanthology.org/2025.emnlp-main.719.pdf)
- **EvalPlus** (measurement instrument): *measured_by*, 11 papers
  > HumanEval [8] and MBPP [3] are the two most widely-used benchmarks for function-level code generation. We use their test augmented versions, i.e., HumanEval+ and MBPP+, with 80×/35× more test cases for rigorous evaluation [38]. (Section 3.1)
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
  - [Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf)
  - [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf)
  - [Personality-Guided Code Generation Using Large Language Models](https://aclanthology.org/2025.acl-long.54.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
  - [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [CodeArena: Evaluating and Aligning CodeLLMs on Human Preference](https://aclanthology.org/2025.emnlp-main.489.pdf)
- **HumanEval+** (measurement instrument): *measured_by*, 10 papers
  > HumanEval [8] and MBPP [3] are the two most widely-used benchmarks for function-level code generation. We use their test augmented versions, i.e., HumanEval+ and MBPP+, with 80×/35× more test cases for rigorous evaluation [38]. (Section 3.1)
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
  - [Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf)
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
  - [CodeSCM: Causal Analysis for Multi-Modal Code Generation](https://aclanthology.org/2025.naacl-long.345.pdf)
  - [Personality-Guided Code Generation Using Large Language Models](https://aclanthology.org/2025.acl-long.54.pdf)
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
  - [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.727.pdf)
- **DS-1000** (measurement instrument): *measured_by*, 5 papers
  > Through comprehensive experiments on five prominent code generation benchmarks, namely HumanEval, HumanEval+, MBPP, DS-1000, and MultiPL-E, our models showcase outstanding performance. (ABSTRACT)
  - [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf)
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
  - [Syntactic and Semantic Control of Large Language Models via Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf)
  - [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50e9ad960ae78b741a6b4fea533f2eaf-Paper-Conference.pdf)
  - [Persona-Augmented Benchmarking: Evaluating LLMs Across Diverse Writing Styles](https://aclanthology.org/2025.emnlp-main.1155.pdf)
- **BigCodeBench** (measurement instrument): *measured_by*, 5 papers
  > Our BigCodeBench focuses on evaluating the fundamental code generation capability of LLMs, which is also an essential path toward strong code agents. (Section 5)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
  - [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf)
  - [EpiCoder: Encompassing Diversity and Complexity in Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bi/wang25bi.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
- **CodeContests** (measurement instrument): *measured_by*, 5 papers
  > “For Dsrc, we chose the CodeContests dataset (Li et al., 2022), a competitive programming problem dataset where each problem comes with multiple correct and incorrect solutions.”
  - [Generative Monoculture in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
  - [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.621.pdf)
  - [Optimizing Language Models for Inference Time Objectives using Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25o/tang25o.pdf)
  - [Improving Diversity in Language Models: When Temperature Fails, Change the Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/verine25a/verine25a.pdf)
- **MultiPL-E** (measurement instrument): *measured_by*, 4 papers
  > The evaluation of FLORA, LORA, and IA3 was conducted on the MultiPL-E benchmark (Cassano et al., 2023), which contains the translation of two unit-test driven Python benchmarks (HumanEval and MBPP) to 18 other programming languages. (Section 4.2)
  - [Batched Low-Rank Adaptation of Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/66247b78cb1aa7259dcf856a18c9e294-Paper-Conference.pdf)
  - [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf)
  - [SCAR: Data Selection via Style Consistency-Aware Response Ranking for Efficient Instruction-Tuning of Large Language Models](https://aclanthology.org/2025.acl-long.625.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
- **HumanEvalPack** (measurement instrument): *measured_by*, 2 papers
  > HUMANEVALSYNTHESIZE (NL!C) Given a natural language docstring or comment describing the desired code, the model is tasked to synthesize the correct code. (Section 3)
  - [OctoPack: Instruction Tuning Code Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1ec299a5229034141e58aeded0d0b9de-Paper-Conference.pdf)
  - [From Understanding to Generation: An Efficient Shortcut for Evaluating Language Models](https://aclanthology.org/2025.emnlp-main.1148.pdf)
- **Codeforces** (measurement instrument): *measured_by*, 2 papers
  > we analyze Codeforces and Project Euler, two longitudinal code generation/problem solving websites. (Section 1)
  - [To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d04d97593c8c33d415337f408ed0e1b-Paper-Conference.pdf)
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **ClassEval** (measurement instrument): *measured_by*, 2 papers
  > We evaluate code LLMs on class-level code generation using ClassEval [13], a collection of 100 class-level Python code generation tasks, covering 100 classes and 410 methods, with an average of 33 tests per class and 8 tests per method. (Section 3.2)
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
  - [SPECTRA: Faster Large Language Model Inference with Optimized Internal and External Speculation](https://aclanthology.org/2025.acl-long.685.pdf)
- **HumanEval-X** (measurement instrument): *measured_by*, 2 papers
  > We compare the pass@1 accuracy of the base models and the corresponding fine-tuned AlchemistCoder models on Humaneval-X [49]. (Section 3.2, under heading 'Results on multilingual code generation.')
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
- **TACO** (measurement instrument): *measured_by*, 2 papers
  > For the coding experiments, we adopt a subset of TACO, a dataset focused on algorithmic code generation with problems sourced from various programming contest platforms (Li et al., 2023). (Section 4.1)
  - [Learning How Hard to Think: Input-Adaptive Allocation of LM Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf)
  - [Optimizing Language Models for Inference Time Objectives using Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25o/tang25o.pdf)
- **bigcode-evaluation-harness** (measurement instrument): *measured_by*, 2 papers
  > We used the Bigcode Evaluation Harness (Ben Allal et al., 2022) as the evaluation tool, sampling 50 solutions per problem with a temperature of 0.2, and report both Pass@1 and Pass@10.
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
  - [any4: Learned 4-bit Numeric Representation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/elhoushi25a/elhoushi25a.pdf)
- **LeetCode Contest** (measurement instrument): *measured_by*, 2 papers
  > To evaluate code LLMs on more challenging problems, we construct the LeetCode Contest benchmark.
  - [Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > LongBench This benchmark contains a variety of zero-shot long context tasks, such as: Single/Multi Document QA, Summarization, Coding, etc. (Section 5)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > MT-bench (Zheng et al., 2023), which evaluates chatbot responses across various dimensions such as writing, roleplay, coding, mathematics, reasoning, STEM, and humanities, using GPT-4 for grading (Section 5).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **EvoEval** (measurement instrument): *measured_by*, 1 paper
  > We evaluated the models on benchmarks corresponding to their respective training levels. In Section 3.2, we evaluate the model’s ability using five function-level code generation benchmarks. Specifically, HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), BigCodeBench (Zhuo et al., 2025), EvoEval (Xia et al., 2024) and FullStackBench (Liu et al., 2024). (Section 3.2)
  - [EpiCoder: Encompassing Diversity and Complexity in Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bi/wang25bi.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > In this experiment, we test Trace’s ability in joint prompt optimization and code generation. ... We use the Big-Bench Hard dataset [21] (15 examples for training, 5 for validation, and the rest for testing). (Section 5.3)
  - [Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/83ba7056bce2c3c3c27e17397cf3e1f0-Paper-Conference.pdf)
- **LeetCode** (measurement instrument): *measured_by*, 1 paper
  > ...HumanEval [4] and LeetCode [12] for coding... (Section 5.2)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
- **Data analysis** (behavioral indicator): *causes*, 1 paper
  > we use large language models (LLMs) enhanced by code generation to automatically generate high-quality data analysis, which will later be refined by human annotators. (Abstract)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > Results in Table 2 show that this code-writing approach effectively reduced hallucination rates, particularly on large graphs.
  - [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf)
- **BigCodeBench-Complete** (measurement instrument): *measured_by*, 1 paper
  > We assess two common programming scenarios: (1) Code Completion (BigCodeBench-Complete), which evaluates the capability of code generation based on the structured docstrings; and (2) Instruction to Code (BigCodeBench-Instruct), which evaluates the ability to complete programming tasks based on natural-language-oriented (NL-oriented) instructions. (Introduction)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
- **CodeSearchNet** (measurement instrument): *measured_by*, 1 paper
  > For an additional dataset on the code generation task. We choose the CodeSearchNet dataset (Husain et al., 2019) for evaluation. (Section 5.3)
  - [Selective Aggregation for Low-Rank Adaptation in Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53a37f820d5be5930415d964f4a0187-Paper-Conference.pdf)
- **Logical reasoning** (construct): *causes*, 1 paper
  > In logical reasoning tasks like Date Understanding, LLM’s reasoning ability is degraded when using code, as shown in Appendix Section G. (Section 3.3)
  - [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf)
- **GUI automation** (behavioral indicator): *causes*, 1 paper
  > OSCAR generates executable Python code to directly interface with the OS, enabling semantically clear and precise actions, ensuring broad applicability across diverse tasks. (Section 2)
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **ChartMimic** (measurement instrument): *measured_by*, 1 paper
  > ChartMimic places emphasis on evaluating LMMs’ capacity to harmonize a blend of cognitive capabilities, encompassing visual understanding, code generation, and cross-modal reasoning. (Abstract)
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
- **Execution-based evaluation** (measurement instrument): *measured_by*, 1 paper
  > The execution-based method executes generated code against test cases to measure the success rate.
  - [McEval: Massively Multilingual Code Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/dad66bb085bab14fbca07cfa4271f00b-Paper-Conference.pdf)
- **ChartX** (measurement instrument): *measured_by*, 1 paper
  > Similarly, Plot2Code (Wu et al., 2024) and ChartX (Xia et al., 2024) also evaluate MLLMs code generation ability, especially for text and data reproducibility (Section 2.2).
  - [ChartCoder: Advancing Multimodal Large Language Model for Chart-to-Code Generation](https://aclanthology.org/2025.acl-long.363.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 1 paper
  > To test our hypothesis, we break down the prompts in Alpaca Eval 2.0 (Li et al., 2023) into different categories. ... We select four representative tasks: two are objective tasks that can be verified: mathematical reasoning or calculation (Math) and Coding...
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > mixing code-generation data has been suggested to enhance a model’s reasoning and logical abilities (Dong et al., 2024). (Section 2)
  - [Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality](https://aclanthology.org/2025.emnlp-main.1138.pdf)
- **WebMMU** (measurement instrument): *measured_by*, 1 paper
  > We present WebMMU, a multilingual benchmark that evaluates three core web tasks: (1) website visual question answering, (2) code editing involving HTML/CSS/JavaScript, and (3) mockup-to-code generation.
  - [WebMMU: A Benchmark for Multimodal Multilingual Website Understanding and Code Generation](https://aclanthology.org/2025.emnlp-main.1276.pdf)

### → Code generation
- **Reasoning** (construct): *causes*, 7 papers
  > A host of prompting techniques have shown how to leverage the In-Context Learning (ICL) abilities of LLMs to enhance a model's reasoning skills, and, as a result, the quality of generated programs.
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [Are Large Language Models Ready for Multi-Turn Tabular Data Analysis?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25aj/li25aj.pdf)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
  - [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf)
- **Instruction following** (behavioral indicator): *causes*, 3 papers
  > math and code problems are formatted as instructions, enhancing instruction following capabilities enables LLMs to better address these tasks. (Section 4)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
- **Self-correction** (behavioral indicator): *causes*, 2 papers
  > Self-Debugging (SD) is both complementary to and beneficial for M1... Applying SD on TAs can provide S-score benefits... M1 achieves consistent improvements.
  - [Can LLMs Learn by Teaching for Better Reasoning? A Preliminary Study](https://proceedings.neurips.cc/paper_files/paper/2024/file/8340b085045cf13f1f0b6c2c4cc0a89c-Paper-Conference.pdf)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Planning** (construct): *causes*, 2 papers
  > The AEP examples contain planning steps, that outline a possible decomposition of the task (lines 7, 14, 17) to encourage step-by-step thinking and to improve generation quality. (Section 2.3.1)
  - [ASPERA: A Simulated Environment to Evaluate Planning for Complex Action Execution](https://aclanthology.org/2025.acl-long.1234.pdf)
  - [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://proceedings.iclr.cc/paper_files/paper/2025/file/e01c431bbb83153632c0dcfaf8ccda0a-Paper-Conference.pdf)
- **Semantic parsing** (behavioral indicator): *causes*, 2 papers
  > we integrate structure-based prompt parsing and multi-stage verification to ensure the quality of resulting solutions and instructions prior to actual code implementation, thereby improving overall performance.
  - [AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf)
  - [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.289.pdf)
- **GUI understanding** (construct): *causes*, 1 paper
  > To further demonstrate how GUI understanding capability enhances mainstream GUI-related tasks, including generating operational code (Cheng et al., 2024) and providing chat assistance (Hong et al., 2024), we conduct experiments as follows... (Section 4.2)
  - [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf)
- **Expressive power** (construct): *causes*, 1 paper
  > the limited expressive capacity of LoRA, stemming from the low-rank constraint, has been recognized as a bottleneck, particularly in rigorous tasks like code generation and mathematical reasoning.
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)

### Associated with
- **Coding ability** (construct), 2 papers
  > For code generation, Luo et al. (2023b) adapt the evol-instruct method to the coding domain, resulting in the WIZARDCODER model, which demonstrates superior coding abilities compared to generally trained LLMs. (Section 1)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
- **Chart generation** (behavioral indicator), 2 papers
  > the LLM is prompted to provide fine-grained feedback considering the downstream application, i.e., chart generation via code generation.
  - [C2: Scalable Auto-Feedback for LLM-based Chart Generation](https://aclanthology.org/2025.naacl-long.232.pdf)
  - [METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](https://aclanthology.org/2025.acl-long.1452.pdf)
- **Tool use** (behavioral indicator), 1 paper
  > The actor then generates revised actions, which could include a combination of tool usage through programming language (code generation) along with natural language explanations of how the tools are employed. (Section 4.1).
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **Data transformation** (behavioral indicator), 1 paper
  > Beyond grid puzzles, PBE is a general paradigm for structured reasoning and data transformation tasks
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
- **Symbolic regression** (behavioral indicator), 1 paper
  > We formulate symbolic regression (SR) as a program synthesis [6] problem. (Section 2)
  - [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf)
- **Code infilling** (behavioral indicator), 1 paper
  > “The local file denotes the code file where the reference code is in. This setting simulates the scenario where developers infill code in the middle of a file.”
  - [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Coding** (behavioral indicator), 1 paper
  > Coding: The ability to write, synthesize, document, debug, and review code across various programming languages. (Section 2.1)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Inductive reasoning** (construct), 1 paper
  > We represent functions f as Python code, meaning that induction synthesizes programs (Section 1).
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **State tracking** (behavioral indicator), 1 paper
  > In recurrent models, Gated DeltaNet shows consistent advantages, especially in ... Code tasks, demonstrating its superior capabilities in ... state tracking, respectively.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Joint prediction** (behavioral indicator), 1 paper
  > "joint estimation via LLM code generation"
  - [Real2Code: Reconstruct Articulated Objects via Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/028fcbcf85435d39a40c4d61b42c99a4-Paper-Conference.pdf)
- **Self-improvement** (construct), 1 paper
  > Zelikman et al. (2023) applied recursive self-improvement to code generation, where the target of improvement was the optimizer itself.
  - [Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement](https://aclanthology.org/2025.acl-long.1354.pdf)
- **Long-context understanding** (construct), 1 paper
  > The research community increasingly recognizes long-context modeling as a crucial capability for next-generation large language models, driven by diverse real-world applications ranging from... repository-level code generation (Zhang et al., 2023a; Zhang et al.)... (Introduction).
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
- **Algorithmic reasoning** (construct), 1 paper
  > However, complex programming tasks requiring multi-step algorithmic reasoning—such as implementing dynamic programming solutions or optimizing parallel computation patterns—remain challenging (Section 1)
  - [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf)
- **Long-form text generation** (behavioral indicator), 1 paper
  > In contrast, long-response tasks, such as essay writing and code generation, generate a substantial number of output tokens during the decode phase, requiring sustained attention over growing sequences of self-generated tokens. (Section 1)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
- **Robustness** (construct), 1 paper
  > We... demonstrate robustness by showing retention of code generation and general problem-solving abilities post adaptation. (Section 1)
  - [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)
- **Conjecture generation** (behavioral indicator), 1 paper
  > Conjecture generation is a crucial component in current evolutionary approaches to mathematical discovery... The basic idea is that because computer code is more interpretable than raw ML predictions, one can use an LLM to generate (human-interpretable) code that solves a mathematical task. This is often known as program synthesis. (Section 5).
  - [Machine Learning meets Algebraic Combinatorics: A Suite of Datasets Capturing Research-level Conjecturing Ability in Pure Mathematics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chau25a/chau25a.pdf)
- **Code debugging** (behavioral indicator), 1 paper
  > we model self-repair as consisting of four stages: code generation, code execution, feedback generation, and code repair.
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > mathematical reasoning with code (Section 4.1), where LMs must use reasoning and coding to answer mathematical questions. (Section 4)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
- **Task decomposition** (behavioral indicator), 1 paper
  > RL-GPT decomposes the task into “find a tree" and “cut a log", solving the former with code generation and the latter with RL.
  - [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf)
- **Logical consistency** (construct), 1 paper
  > By iterative preference alignment, the code generator learns to improve the logic consistency with the domain knowledge. (Abstract)
  - [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.245.pdf)
- **Chain of thought** (behavioral indicator), 1 paper
  > training LLMs to generate code first and then output the CoT to explain reasoning steps for code generation is more effective. (Abstract)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **Utility preservation** (construct), 1 paper
  > As a foundation model, f ′ is expected to retain abilities such as text and code generation, question answering, instruction-following, and basic mathematical reasoning.
  - [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf)
- **Visual editing** (behavioral indicator), 1 paper
  > simple visual editing actions generated as Python code from multimodal LLMs (Section 1. Introduction)
  - [ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25d/fu25d.pdf)
- **Symbolic reasoning** (construct), 1 paper
  > “symbolic computing via code generation is adept at handling rigorous operations”
  - [CodeSteer: Symbolic-Augmented Language Models via Code/Text Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25x/chen25x.pdf)
- **Plan generation** (behavioral indicator), 1 paper
  > In the second step, a complete code is generated based on the outlined plan by Agent B. (Section 4.1.1)
  - [Code-Generated Graph Representations Using Multiple LLM Agents for Material Properties Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25an/huang25an.pdf)
