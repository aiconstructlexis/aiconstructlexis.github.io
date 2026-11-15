# Blocksworld
**Type:** Measurement instrument  
**Supporting papers:** 15  
**Also known as:** BlocksWorld  

## State of the Field

**What it is.** Across papers, Blocksworld is most commonly treated as a classical planning benchmark or domain in which blocks are rearranged from an initial or source configuration to a specified goal configuration, often on a table and sometimes with the explicit rule that only one unstacked block may be moved at a time. Definitions vary at the margins: some papers formulate it in PDDL, some describe it as a symbolic or commonsense domain, some call it a planning dataset, and some place it within PlanBench or describe it as a real-world task planning benchmark that corresponds to path-finding in a state transition graph. A smaller line of work also defines task-specific splits inside it, including plan-length train, validation, and test partitions and in-distribution versus out-of-distribution block-count ranges.

**What it is claimed to measure.** Its reported measurement use is concentrated on Planning. Papers use Blocksworld to measure 2 constructs and 1 behavioral indicator, with Planning the prevailing target, described in relationship evidence as a real-world task planning benchmark, a symbolic planning problem, or simply the planning task on which a framework is evaluated. Smaller lines of work use it to measure Out-of-distribution generalization, for example by treating 3 to 7 blocks as in-distribution and 8 to 20 blocks as out-of-distribution, and an isolated paper reports it as measuring Constraint adherence because the benchmark provides action and constraint definitions and requires actions to follow those constraints.

**Space of uses.** Papers most often position Blocksworld as a main evaluation domain for planning-focused methods, though some use it as an additional testbed, including for noisy rationales and for out-of-distribution generalization to longer plans. In multi-benchmark setups it appears alongside other PDDL tasks such as Minigrid and Logistics, and alongside GSM-8K and BIG-Bench Hard Dyck Languages, while other work studies it within PlanBench. Papers do not explicitly link it to another measurement instrument.

## Sources

**Blocksworld** (5 papers: [System 1.x: Learning to Balance Fast and Slow Planning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/605e59e78284907aa4fce5280838def3-Paper-Conference.pdf), [HyperTree Planning: Enhancing LLM Reasoning via Hierarchical Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gui25b/gui25b.pdf), [ALPINE: Unveiling The Planning Capability of Autoregressive Learning in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d848cb2c84f0bba7f1f73cf232734c40-Paper-Conference.pdf), [Can Language Models Perform Robust Reasoning in Chain-of-thought Prompting with Noisy Rationales?](https://proceedings.neurips.cc/paper_files/paper/2024/file/dfaa29ed28dfa175bcc5e2a54aa199f8-Paper-Conference.pdf), [Chain of Thoughtlessness? An Analysis of CoT in Planning](https://proceedings.neurips.cc/paper_files/paper/2024/file/3365d974ce309623bd8151082d78206c-Paper-Conference.pdf))
> A classical planning benchmark that involves rearranging a stack of blocks into a target configuration by moving one unstacked block at a time.

**BlocksWorld** (2 papers: [Improving Large Language Model Planning with Action Sequence Similarity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b18c6549c77411d92e645027a25838a8-Paper-Conference.pdf), [PlanGenLLMs: A Modern Survey of LLM Planning Capabilities](https://aclanthology.org/2025.acl-long.958.pdf))
> A classical planning benchmark task, formulated in PDDL, that involves rearranging blocks on a table to achieve a specified goal configuration.

## Relationships

### → Blocksworld
- **Planning** (construct): *measured_by*, 4 papers
  > Finally, we validate these results on a real-world task planning benchmark, Blocksworld [22], which directly corresponds to the path-finding problem (see Appendix F). (Introduction).
  - [ALPINE: Unveiling The Planning Capability of Autoregressive Learning in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d848cb2c84f0bba7f1f73cf232734c40-Paper-Conference.pdf)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
  - [Automatic Curriculum Expert Iteration for Reliable LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9083c94382509473bdf5fc2672fc72b3-Paper-Conference.pdf)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > Since all the exemplar candidates are with 3-7 blocks, we denote test examples with 3-7 blocks as in-distribution (ID) and 8-20 blocks as out-of-distribution (OOD). (Figure 6)
  - [Improving Large Language Model Planning with Action Sequence Similarity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b18c6549c77411d92e645027a25838a8-Paper-Conference.pdf)
- **Constraint adherence** (behavioral indicator): *measured_by*, 1 paper
  > BlocksWorld (Valmeekam et al., 2024a) is a planning benchmark that provides a domain description, including action and constraint definitions, and requires agents to execute actions to transition from an initial state to a goal state. All actions must adhere to the constraints outlined in the prompt. (Section 3.1)
  - [Revealing the Barriers of Language Agents in Planning](https://aclanthology.org/2025.naacl-long.93.pdf)
