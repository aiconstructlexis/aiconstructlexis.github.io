# T-Eval
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across papers, the prevailing usage treats T-Eval as an out-of-distribution benchmark for LLMs. Definitions describe it as evaluating multi-step decision-making and API utilization, sometimes as an OOD task planning dataset, while a smaller framing presents it as a tool-use benchmark that measures the ability to interact with external tools and APIs to complete tasks. One paper also describes it as widely used.

**What it is claimed to measure.** Papers use T-Eval to measure three constructs and two behavioral indicators. The linked constructs are Decision-making, Planning, and Reasoning, and the linked behavioral indicators are Action execution and Instruction following. One paper further says that T-Eval assesses six core competencies: planning, reasoning, retrieval, understanding, instruction following, and reviewing.

**Space of uses.** In usage descriptions, papers position T-Eval as an OOD evaluation for generalization. One paper uses it for zero-shot generalization experiments, and another places it with ToolBench and ToolAlpaca in an Action Execution category.

## Sources

**T-Eval** (2 papers: [WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d7259031023c5aa463187c4a31c95c8-Paper-Conference.pdf), [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf))
> An out-of-distribution benchmark designed to evaluate the multi-step decision-making and API utilization capabilities of LLMs.

## Relationships

### → T-Eval
- **Planning** (construct): *measured_by*, 1 paper
  > We utilize T-Eval (Chen et al., 2023c), which assesses six core competencies: planning, reasoning, retrieval, understanding, instruction following, and reviewing. (Sec. 4.1)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Action execution** (behavioral indicator): *measured_by*, 1 paper
  > We categorize the agentic tasks into three types: (1) Action Execution: T-Eval (Chen et al., 2023c), ToolBench (Qin et al., 2023a), and ToolAlpaca (Tang et al., 2023b) (Sec. 2.2)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > We utilize T-Eval (Chen et al., 2023c), which assesses six core competencies: planning, reasoning, retrieval, understanding, instruction following, and reviewing. (Sec. 4.1)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > We utilize T-Eval (Chen et al., 2023c), which assesses six core competencies: planning, reasoning, retrieval, understanding, instruction following, and reviewing. (Sec. 4.1)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Decision-making** (construct): *measured_by*, 1 paper
  > “we conduct experiments using an OOD benchmark, T-Eval, a widely-used benchmark to evaluate the multi-step decision-making capability of LLMs to utilize APIs.”
  - [WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d7259031023c5aa463187c4a31c95c8-Paper-Conference.pdf)
