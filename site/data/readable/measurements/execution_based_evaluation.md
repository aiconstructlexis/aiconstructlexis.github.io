# Execution-based evaluation
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** Sandbox execution, Execution-based focused evaluation  

## State of the Field

**What it is.** Across the papers, the prevailing description is of an evaluation method or protocol that verifies success through execution, rather than relying on static demonstrations or string matching. Most definitions instantiate this either as running generated code against test cases and checking whether outputs match expected results, or as using custom scripts to check the final state of a computer environment. A narrower variant, called execution-based focused evaluation, has annotators obtain database results programmatically and write scripts that focus on the essential components of the answer while ignoring non-essential columns, and one paper describes sandbox execution in a secure, isolated Docker-based environment for validating code and test cases.

**What it is claimed to measure.** Papers link this instrument to 1 behavioral indicator and no constructs. The measurement claim converges on code generation: papers report that the execution-based method runs generated code against test cases to measure success rate, with generated outputs expected to equal the target outputs.

**Space of uses.** Papers link it to 1 other measurement instrument, OSWorld, and describe that benchmark as supporting task setup, interactive learning, and execution-based evaluation of open-ended computer tasks. More broadly, papers position execution-based evaluation as the checking stage inside larger workflows: OSWorld provides example-wise execution-based evaluation for tasks, code-focused work samples multiple responses per task and validates them in a sandbox environment, and database-oriented work requires annotators to write evaluation scripts after obtaining results programmatically.

## Sources

**Execution-based evaluation** (2 papers: [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf), [McEval: Massively Multilingual Code Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/dad66bb085bab14fbca07cfa4271f00b-Paper-Conference.pdf))
> A method of evaluation where task completion is verified by a custom script that checks the final state of the computer environment, rather than relying on static demonstrations or string matching.

**Sandbox execution** (1 paper: [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf))
> An evaluation procedure where model-generated code and test cases are executed in a secure, isolated environment to validate correctness.

**Execution-based focused evaluation** (1 paper: [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://proceedings.iclr.cc/paper_files/paper/2025/file/46c10f6c8ea5aa6f267bcdabcb123f97-Paper-Conference.pdf))
> An evaluation protocol where scripts programmatically obtain results from the database and assess success by focusing on the essential components of the answer, ignoring non-essential columns.

## Relationships

### → Execution-based evaluation
- **Code generation** (behavioral indicator): *measured_by*, 1 paper
  > The execution-based method executes generated code against test cases to measure the success rate.
  - [McEval: Massively Multilingual Code Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/dad66bb085bab14fbca07cfa4271f00b-Paper-Conference.pdf)

### Associated with
- **OSWorld** (measurement instrument), 1 paper
  > “supporting task setup, interactive learning, and execution-based evaluation of open-ended computer tasks”
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
