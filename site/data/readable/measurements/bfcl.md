# BFCL
**Type:** Measurement instrument  
**Supporting papers:** 13  
**Also known as:** Berkeley Function-Calling Benchmark  

## State of the Field

**What it is.** Most papers describe BFCL, often expanded as the Berkeley Function-Calling Leaderboard or Benchmark for Function Calling, as a comprehensive benchmark or leaderboard for evaluating LLM function calling or tool use. Definitions variously say it covers single-turn, multi-turn, hallucination, and executable settings, or Non-live, Live, Multi-turn, and Hallucination samples, with evaluation through AST, executable function evaluation, and relevance detection. A smaller line of description presents it as assessing an agent's ability to reason and execute function calls across programming languages and application domains, including simple, multiple, and parallel calls. Some papers also mention real-world APIs and use-cases such as agent tasks and enterprise workflows, and refer to BFCL v2 and BFCL v3.

**What it is claimed to measure.** Across papers, the claims cluster around tool use and closely related function-calling ability. BFCL is linked to 2 behavioral indicators and 1 construct, and papers most often use it to measure Tool use, with additional uses for Hallucination and for the construct Tool use ability. The supporting language stays near whether models can invoke functions or tools, including assessments of correct API calls, whether the correct tool was called with the correct parameters, and performance on a hallucination category.

**Space of uses.** Papers frequently use BFCL for experimental evaluation, sometimes reporting results directly on the BFCL leaderboard. Some studies pair it with APIBank or T-Eval, while others use BFCL v3 as a data source, adapt test cases from its live&simple category, or use it to evaluate models' helpfulness on benign tasks. Papers do not link BFCL to another measurement instrument.

**Concerns raised.** One paper describes a narrower evaluation setup: like other current benchmarks, BFCL focuses on cases where the correct tool is provided and the user gives enough information to call it, and then evaluates whether the correct tool was called with the correct parameters.

## Sources

**BFCL** (8 papers: [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf), [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf), [CRITICTOOL: Evaluating Self-Critique Capabilities of Large Language Models in Tool-Calling Error Scenarios](https://aclanthology.org/2025.emnlp-main.1355.pdf), [Tool Preferences in Agentic LLMs are Unreliable](https://aclanthology.org/2025.emnlp-main.1060.pdf), [ToolSafety: A Comprehensive Dataset for Enhancing Safety in LLM-Based Agent Tool Invocations](https://aclanthology.org/2025.emnlp-main.714.pdf), [iTool: Reinforced Fine-Tuning with Dynamic Deficiency Calibration for Advanced Tool Use](https://aclanthology.org/2025.emnlp-main.701.pdf), [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf), [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf))
> BFCL (Benchmark for Function Calling) is a benchmark used to evaluate LLM function-calling performance across single-turn, multi-turn, hallucination, and executable categories.

**Berkeley Function-Calling Benchmark** (1 paper: [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf))
> Extensive benchmark assessing function-calling capabilities across programming languages and application domains, including simple, multiple, and parallel function calls, with evaluation via AST accuracy, execution, and relevance detection.

## Relationships

### → BFCL
- **Tool use** (behavioral indicator): *measured_by*, 5 papers
  > function calling (BFCL)
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
  - [Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf)
  - [When2Call: When (not) to Call Tools](https://aclanthology.org/2025.naacl-long.174.pdf)
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)
  - [The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)
- **Tool use ability** (construct): *measured_by*, 1 paper
  > Experiments are conducted on two representative benchmarks, including BFCL Yan et al. (2024) and API-Bank Li et al. (2023). The two benchmarks are comprehensive and executable function call evaluations specifically designed to assess the ability of LLMs to invoke functions.
  - [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *measured_by*, 1 paper
  > Accuracy performance comparison on BFCL-v3 leaderboard (updated on 09/20/2024). ... Hallucination (Table 2)
  - [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)
