# Workflow generation
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Node chain generation  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats workflow generation as producing a structured, executable workflow in response to a user query, often in code form. A smaller framing narrows the behavior to producing an ordered sequence of subtasks that serves as the topological sequence for a workflow. One paper describes WorkflowBench as "the first dataset explicitly designed for workflow generation" (WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models).

**Variants.** Papers mainly use the general label workflow generation, though one paper uses node chain generation for the version centered on an ordered subtask sequence. The main variation is whether the target output is a full structured, executable workflow or the ordered chain of subtasks that organizes that workflow.

**Space of elicitation and scores.** Papers do not link workflow generation to any measurement instrument.

**What it is taken as evidence of.** Papers do not link this behavior to any construct.

## Sources

**Workflow generation** (2 papers: [WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d7259031023c5aa463187c4a31c95c8-Paper-Conference.pdf), [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf))
> The observable behavior of producing a structured, executable workflow, typically in the form of code, in response to a user query.

**Node chain generation** (1 paper: [Benchmarking Agentic Workflow Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/adbe936993aa7cf41e45054d8b72f183-Paper-Conference.pdf))
> Producing an ordered sequence of subtasks that serves as a topological sequence for a workflow.
