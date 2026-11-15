# Code execution
**Type:** Behavioral indicator  
**Supporting papers:** 16  
**Also known as:** Automatic debugging, SQL query execution, Program execution  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is running generated or provided code in an interpreter, sandbox, or other execution environment and returning the resulting output or feedback. This behavior is most commonly used to compute or transform information for an answer, validate functional correctness, or carry out calculations and algorithmic steps. Some papers emphasize that the model can "generate and execute code incrementally" and then use the results to correct buggy or illogical steps, while a smaller line makes success explicit as correctly executing SQL queries or deterministically evaluating whether safety conditions are met.

**Variants.** Papers study it in several settings: math problem solving with incremental execution and intermediate sub-tasks, answer verification through sandboxed runs, execution of guardrail code through an external engine, and script or command execution by OS agents to extend their action space. Additional names include SQL query execution, for running queries on database tables, and program execution, for running knowledge-intensive programs in a secure environment to compute outputs from extracted variables. One paper also uses the nearby label automatic debugging for inferring program state from partial code, such as a variable value at a specific line, without executing the program.

**Space of elicitation and scores.** Papers do not link it to any measurement instrument. Instead, they usually operationalize the behavior by whether code is actually run in environments such as an interpreter, sandbox, external engine, code interpreter, or system executor, and whether that run yields execution results, output, feedback, or a final decision and explanation. Some descriptions also stress incremental execution across turns.

**What it is taken as evidence of.** Papers do not link it to any construct. The reported relationships instead point to other behaviors: one paper claims a causal relationship from code execution to self-correction, describing strategy adjustment from execution feedback as self-debugging; another paper claims a causal relationship from code execution to self-reflection and refinement after returning execution results; and one paper reports it as related to tool use, where tool use includes web browsing, code execution, and file uploads.

## Sources

**Code execution** (9 papers: [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf), [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf), [Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf), [Stealth edits to large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c8168a8eca2eb23f6b1f5019371043e-Paper-Conference.pdf), [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf), [GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiang25a/xiang25a.pdf), [Agentic-R1: Distilled Dual-Strategy Reasoning](https://aclanthology.org/2025.emnlp-main.604.pdf), [Can External Validation Tools Improve Annotation Quality for LLM-as-a-Judge?](https://aclanthology.org/2025.acl-long.779.pdf), [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369.pdf))
> The observable process where the model runs generated code within an interpreter and receives the output.

**Automatic debugging** (1 paper: [A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf))
> The task of inferring the state of a program, such as the value of a variable at a specific line, given only partial code.

**SQL query execution** (1 paper: [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf))
> The observable behavior of processing and correctly executing SQL queries on database tables.

**Program execution** (1 paper: [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.245.pdf))
> Running generated knowledge-intensive programs in a secure environment to compute intermediate or final outputs based on extracted variables.

## Relationships

### Code execution →
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > The analysis reveals that GPT4-Code’s strong performance is not solely due to its code generation and execution abilities but also its capacity to adjust its problem-solving strategies based on feedback from code execution—a process we term self-debugging
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > After the LLM generates a response containing code, we execute the code and return the results for further self-reflection and refinement.
  - [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf)

### Associated with
- **Tool use** (behavioral indicator), 1 paper
  > Tool Use: The ability to interact with external tools and APIs, including functions such as web browsing, code execution, and file uploads. (Section 2.1)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
