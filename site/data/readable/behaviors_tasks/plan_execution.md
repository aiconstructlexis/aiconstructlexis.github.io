# Plan execution
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats plan execution as carrying out a generated plan step by step. Most commonly, success is described as following sequential steps to solve a task or reach a verdict, with one paper noting that users see only the first step and that later steps appear "one at a time for cognitive ease," while another describes the model as executing an evaluation plan step by step to analyze responses, verify criteria, and arrive at a final verdict. A smaller formulation treats execution as performing each planned action correctly by retrieving and running associated code snippets.

**Variants.** Papers study this behavior in several settings. One line uses human task following, where a user follows an LLM-generated plan with steps revealed sequentially and with support such as calculator or web search. Another treats it as self-execution of planned actions by retrieving Python code snippets associated with an execute relation. A further variant appears in evaluation, where the model follows an evaluation plan through intermediate checks, such as verifying whether a response contains required attributes, before producing a final judgment.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, the papers describe elicitation procedurally: a user is given one random plan and sees the next step only after submitting an answer, planned actions are executed by retrieving associated Python code, or the model follows an evaluation plan to produce intermediate judgments and a final verdict.

**What it is taken as evidence of.** No construct is linked to it. The papers do not explicitly state that this behavior indicates a broader construct.

## Sources

**Plan execution** (3 papers: [A Good Plan is Hard to Find: Aligning Models with Preferences is Misaligned with What Helps Users](https://aclanthology.org/2025.emnlp-main.585.pdf), [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf), [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf))
> Following an LLM-generated step-by-step plan to solve a task, with each step revealed sequentially and supported by tools like calculator or web search.
