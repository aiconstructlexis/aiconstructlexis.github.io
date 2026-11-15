# Accuracy
**Type:** Construct  
**Supporting papers:** 39  
**Also known as:** Correctness, Task correctness, Prediction correctness, Proof correctness, Response correctness, Formal correctness, Formulation correctness, Response accuracy, Code correctness, Chart correctness, Proof accuracy, Truth alignment, Code reliability  

## State of the Field

**Space of definitions.** Most definitions treat accuracy as answer or response correctness, whether a model's output is factually or logically right for the instruction, input, or task, and papers often use accuracy and correctness interchangeably. A smaller line of work narrows it to artifact-specific validity, such as code that passes test cases, proofs accepted by a proof assistant, plans satisfying formal preconditions and postconditions, optimization formulations that reflect problem requirements, charts that match query intent and data, or hiring decisions that identify qualified candidates. Another recurring split is between output-level scoring and latent ability framings, with some papers defining prediction correctness, response correctness, code correctness, or code reliability as model capacities, sometimes adding format compliance or consistency of executability.

**Space of facets.** Papers mostly organize the concept by what is being checked: final answers and responses, rationales and proofs, or structured artifacts such as code, plans, optimization models, charts, insights, and generated relation-extraction samples. Across these uses, the labels correctness, task correctness, response correctness, proof accuracy, truth alignment, and code reliability overlap heavily around matching ground truth or task requirements, but they are not identical. Truth alignment adds producing the correct result in the desired format, one correctness definition requires the final answer to meet formatting constraints, proof accuracy requires steps to be both correct and relevant, and insight correctness is defined as the mean truth value of constituent claims.

**Space of measurement.** Accuracy is linked to 4 measurement instruments and 2 behavioral indicators. The most recurrent linked instrument is LLM-as-a-judge, where GPT-4 rates paired responses on a 1 to 10 scale for accuracy alongside other criteria; other linked instruments are human evaluation, expert evaluation, and GEMBA-MQM. Papers also operationalize accuracy through direct ground-truth comparison or exact match, private test cases and unit tests for code, proof assistant acceptance, symbolic plan validation, averaging claim truth values, average ROUGE-F1, and hidden-state or CoE analyses that estimate response correctness; these usually mirror the definitions by checking whether outputs match ground truth, execute correctly, or satisfy formal constraints, though some papers use desired format, ROUGE-F1, or internal-state estimates rather than only direct answer checking.

**Links.** Outside measurement, the recorded links are only related links, not causal or correlational claims, and no construct-to-construct link is recorded. One paper relates accuracy to instruction following through the formulation "Truth Alignment = Reasoning Capability + Instruction Following." Another relates it to hallucination, defining accuracy as whether responses contain hallucination and present correct attributes.

## Sources

**Correctness** (7 papers: [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf), [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf), [ZERA: Zero-init Instruction Evolving Refinement Agent – From Zero Instructions to Structured Prompts via Principle-based Optimization](https://aclanthology.org/2025.emnlp-main.1190.pdf), [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf), [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf), [ALiiCE: Evaluating Positional Fine-grained Citation Generation](https://aclanthology.org/2025.naacl-long.23.pdf))
> The degree to which a generated program is functionally accurate, meaning it produces the expected output for all given inputs as defined by a set of test cases.

**Accuracy** (7 papers: [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf), [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf), [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf), [HyKGE: A Hypothesis Knowledge Graph Enhanced RAG Framework for Accurate and Reliable Medical LLMs Responses](https://aclanthology.org/2025.acl-long.580.pdf), [Two Tickets are Better than One: Fair and Accurate Hiring Under Strategic LLM Manipulations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cohen25a/cohen25a.pdf), [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.891.pdf), [Elevating Legal LLM Responses: Harnessing Trainable Logical Structures and Semantic Knowledge with Legal Reasoning](https://aclanthology.org/2025.naacl-long.290.pdf))
> The degree to which a model's response correctly aligns with factual or logically valid outcomes for a given instruction and input.

**Task correctness** (1 paper: [Tailoring Self-Rationalizers with Multi-Reward Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf))
> The extent to which the model's predicted answer is right for the question after generating a rationale.

**Prediction correctness** (1 paper: [Beyond Accuracy: Ensuring Correct Predictions With Correct Rationales](https://proceedings.neurips.cc/paper_files/paper/2024/file/4bbeef01d9753fd5a29e9fd02d275698-Paper-Conference.pdf))
> The latent ability of a model to produce accurate predictions, typically measured by task-specific accuracy metrics.

**Proof correctness** (1 paper: [ImProver: Agent-Based Automated Proof Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/4864005cfdea7ebd07086ed1b9846825-Paper-Conference.pdf))
> The property that a generated proof is valid and accepted by the proof assistant as establishing the theorem statement.

**Response correctness** (2 papers: [Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b0b1cfc8ede53f452cabf8b9cf4eef76-Paper-Conference.pdf), [3DS: Medical Domain Adaptation of LLMs via Decomposed Difficulty-based Data Selection](https://aclanthology.org/2025.emnlp-main.983.pdf))
> The latent property of a model's generated response being factually or logically correct for a given input, which can be inferred from internal model states.

**Formulation correctness** (1 paper: [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf))
> The degree to which a generated mathematical optimization model accurately and faithfully represents the requirements and constraints of a real-world problem described in natural language.

**Formal correctness** (1 paper: [Hierarchical Planning for Complex Tasks with Knowledge Graph-RAG and Symbolic Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/petruzzellis25a/petruzzellis25a.pdf))
> The extent to which a generated plan satisfies the formal preconditions and postconditions required for execution.

**Response accuracy** (1 paper: [Video2Roleplay: A Multimodal Dataset and Framework for Video-Guided Role-playing Agents](https://aclanthology.org/2025.emnlp-main.1209.pdf))
> The ability of the model to correctly understand and address user questions or conversational prompts based on the provided context.

**Code correctness** (1 paper: [UnitCoder: Scalable Code Synthesis from Pre-training Corpora](https://aclanthology.org/2025.emnlp-main.286.pdf))
> The latent property of a model to generate functionally accurate code that passes defined test cases without logical or syntactic errors.

**Chart correctness** (1 paper: [Text2Vis: A Challenging and Diverse Benchmark for Generating Multimodal Visualizations from Text](https://aclanthology.org/2025.emnlp-main.1622.pdf))
> The extent to which a generated chart accurately reflects the query intent and the underlying data.

**Proof accuracy** (1 paper: [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf))
> The degree to which a model's generated reasoning steps are both logically correct and relevant to the final conclusion, reflecting faithful internal reasoning.

**Truth alignment** (1 paper: [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf))
> The extent to which a model's outputs match the ground truth in the required answer form for a task.

**Code reliability** (1 paper: [Reliable and Cost-Effective Exploratory Data Analysis via Graph-Guided RAG](https://aclanthology.org/2025.emnlp-main.836.pdf))
> The latent property of a model to consistently generate code that is syntactically correct and executable without errors.

## Relationships

### Accuracy →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > We prompt GPT-4 to rate responses from various decoding strategies on relevance, accuracy, and insightfulness, scoring them from 1 to 10. (Table 2)
  - [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
- **GEMBA-MQM** (measurement instrument): *measured_by*, 1 paper
  > our analysis reveals that GEMBA-MQM’s performance is primarily driven by Accuracy aspects, with less reliability in evaluating Fluency, Style, and Terminology (Section 5).
  - [How Good Are LLMs for Literary Translation, Really? Literary Translation Evaluation with Humans and LLMs](https://aclanthology.org/2025.naacl-long.548.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > Human evaluation focuses on three aspects: 1) Accuracy: the aspect evaluates whether the generated answers are correct and free from factual errors.
  - [Elevating Legal LLM Responses: Harnessing Trainable Logical Structures and Semantic Knowledge with Legal Reasoning](https://aclanthology.org/2025.naacl-long.290.pdf)
- **Expert evaluation** (measurement instrument): *measured_by*, 1 paper
  > An optimization expert manually reviewed each model and assessed the correctness of four key components: decision variables, objective function, equality constraints, and inequality constraints.
  - [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf)

### Associated with
- **Instruction following** (behavioral indicator), 1 paper
  > “Truth Alignment = Reasoning Capability + Instruction Following”
  - [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hallucination** (behavioral indicator), 1 paper
  > accuracy: whether the responses contains any hallucination, and present correct attributes; (Section 4)
  - [MR. Judge: Multimodal Reasoner as a Judge](https://aclanthology.org/2025.emnlp-main.1021.pdf)
