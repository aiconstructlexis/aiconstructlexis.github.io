# Critique ability
**Type:** Construct  
**Supporting papers:** 19  
**Also known as:** Self-critique, Self-critique ability, Critiquing ability, Discrimination, Critique capability, Peer review capability, Critical judgment  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats critique ability as a model's capacity to evaluate responses, identify flaws or errors, and provide feedback that supports revision or correction. Most definitions center self-critique, either as an observable behavior in which a model is instructed to critique and iteratively revise its own output, or as a latent capacity to evaluate its own reasoning process, sometimes without external feedback and sometimes explicitly contrasted with critiquing other models' reasoning. A smaller line of work narrows the construct to academic peer review or critical judgment, while one broader formulation extends it across feedback, comparison, correction, and meta-feedback.

**Space of facets.** Papers systematize the construct along several facets. One formulation evaluates it through feedback, comparison, correction, and meta-feedback, while another treats effective critique as combining discrimination, the ability to evaluate, rank, and recognize mistakes, with critiquing, the ability to provide actionable feedback for improvement; in the mistake-analysis framing, discrimination is contrasted with generation and described as easier than generation. Several papers also distinguish self-critique from cross-model critique, and application-specific variants appear as peer review capability and critical judgment.

**Space of measurement.** Papers link critique ability to 1 measurement instrument and no behavioral indicators. The linked instrument is CRITICTOOL, a benchmark for self-critique in tool utilization and tool-calling error scenarios, which is described as evaluating self-critique across multiple dimensions. Elsewhere, papers describe assessment through self-critique scores or by whether a critic drives a task-performing model toward correct outputs, so the recorded operationalization mostly targets error identification and correction in self-generated outputs, while the broader peer-review and critical-judgment variants are not tied to a named instrument.

**Links.** Individual papers claim causal relationships from critique ability to self-improvement and to reasoning. For self-improvement, the recorded evidence says critique ability enables the analysis and correction of flaws in responses; for reasoning, the recorded evidence says self-critique mechanisms improve performance in complex reasoning tasks by enabling error correction, induction and deduction, and switching thinking insights. Separate papers report that critique ability is related to multi-hop reasoning, framed as generating subquestions and answering them step by step with retrieved passages, and is related to weak-to-strong generalization, where weaker critic models guide stronger task-performing models.

## Sources

**Self-critique** (5 papers: [Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf), [Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf), [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf), [Fixing Distribution Shifts of LLM Self-Critique via On-Policy Self-Play Training](https://aclanthology.org/2025.acl-long.865.pdf), [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf))
> The observable behavior where a model is instructed to critique its own output as a step towards improving it.

**Self-critique ability** (1 paper: [Can Large Language Models Detect Errors in Long Chain-of-Thought Reasoning?](https://aclanthology.org/2025.acl-long.905.pdf))
> The latent capacity of a model to accurately evaluate and identify errors in its own reasoning process, as opposed to evaluating others' reasoning.

**Critiquing ability** (1 paper: [Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf))
> The capacity to generate feedback that both accurately assesses a solution and helps improve it in subsequent revisions.

**Discrimination** (1 paper: [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf))
> The latent ability of a model to identify and analyze potential mistakes, errors, or harmful elements within a given response.

**Critique ability** (1 paper: [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf))
> The latent capability of Large Language Models to identify and rectify flaws in responses, encompassing feedback, comparison, correction, and meta-feedback dimensions.

**Critique capability** (1 paper: [ProcessBench: Identifying Process Errors in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.50.pdf))
> The latent ability of a general language model to analyze, evaluate, and provide feedback on the correctness of reasoning steps in a solution, including identifying errors and explaining them.

**Peer review capability** (1 paper: [Benchmarking LLMs' Judgments with No Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9b0e4e205bdf232da9f74bfb9469539-Paper-Conference.pdf))
> The ability of an LLM to generate useful, high-quality academic peer reviews for research papers.

**Critical judgment** (1 paper: [Benchmarking LLMs' Judgments with No Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9b0e4e205bdf232da9f74bfb9469539-Paper-Conference.pdf))
> The ability to provide substantive evaluative feedback that identifies strengths, weaknesses, and constructive critique beyond merely restating surface content.

## Relationships

### Critique ability →
- **Self-improvement** (construct): *causes*, 1 paper
  > Critique ability is crucial for the self-improvement [1, 2] of LLMs, as it enables the effective analysis and correction of flaws in responses [3, 4]. (Introduction)
  - [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > Self-critique mechanisms significantly improve the performance of language models in complex reasoning tasks by giving them the ability to correct errors, conduct induction and deduction, and switch thinking insights. (Abstract)
  - [Fixing Distribution Shifts of LLM Self-Critique via On-Policy Self-Play Training](https://aclanthology.org/2025.acl-long.865.pdf)
- **CRITICTOOL** (measurement instrument): *measured_by*, 1 paper
  > we introduce CRITICTOOL, the first self-critique evaluation benchmark for tool utilization of LLMs. (Section 1)
  - [CRITICTOOL: Evaluating Self-Critique Capabilities of Large Language Models in Tool-Calling Error Scenarios](https://aclanthology.org/2025.emnlp-main.1355.pdf)

### Associated with
- **Multi-hop reasoning** (construct), 1 paper
  > “To answer multi-hop reasoning questions, self-critique involves prompting the LLM to generate subquestions and answer them using retrieved passages in a step-by-step manner.”
  - [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
- **Weak-to-strong generalization** (construct), 1 paper
  > Our experiments demonstrate that relatively weaker critic models can effectively guide stronger task-performing models such as GPT-4o (Table 3), exhibiting a similar phenomenon to weak-to-strong generalization (Christiano et al., 2018; Burns et al., 2023), where weaker models can be trained to effectively supervise more capable ones. (Section 1)
  - [Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf)
