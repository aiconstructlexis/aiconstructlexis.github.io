# CRUXEval
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** CRUXEVAL, CRUX, CruxEval  

## State of the Field

**What it is.** Across the cited papers, CRUXEval is most commonly described as a benchmark for code reasoning, code understanding, and execution. Many definitions make this concrete as execution-result, code-output, or input-output prediction, and some papers explicitly split it into CruxEval-I for input prediction and CruxEval-O for output prediction; one paper further describes it as 800 Python functions created with a "generate-and-filter" approach with CodeLlama. A smaller framing refers to it more broadly as a benchmark for reasoning abilities in code generation and understanding.

**What it is claimed to measure.** Papers use CRUXEval to measure 3 constructs and 2 behavioral indicators. The prevailing usage is to measure code reasoning, followed by abductive code reasoning and broader reasoning; among behavioral indicators, code output prediction is the more common use, followed by code input prediction. The linked claims largely converge on reasoning about code execution, including tasks that ask a model to predict the input given the output of a function and vice versa.

**Space of uses.** Papers typically position CRUXEval as an evaluation benchmark within broader suites, often alongside LiveCodeBench and sometimes with DS-1000 or LCB-Exec. Some authors use CRUXEval and LiveCodeBench as representative datasets for validating deductive and abductive capabilities, one paper includes it among logical reasoning benchmarks, and another says a code execution scenario is based on CRUXEval's output-prediction setup.

**Concerns raised.** One survey states that CRUXEval, along with several other benchmarks, has incomplete coverage with respect to real-world repository-scale tasks.

## Sources

**CRUXEVAL** (4 papers: [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf), [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf), [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf), [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf))
> A benchmark that measures reasoning and execution abilities through code output prediction.

**CRUXEval** (3 papers: [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf), [WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models](https://aclanthology.org/2025.acl-long.246.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf))
> A benchmark designed to evaluate code understanding and execution, used in the paper to test both deductive and abductive code reasoning.

**CRUX** (1 paper: [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf))
> A benchmark used to evaluate a model's reasoning abilities in the context of code generation and understanding.

**CruxEval** (1 paper: [CodeIO: Condensing Reasoning Patterns via Code Input-Output Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25t/li25t.pdf))
> CruxEval is a benchmark for evaluating code understanding and execution-result prediction.

## Relationships

### → CRUXEval
- **Code reasoning** (construct): *measured_by*, 3 papers
  > These tasks assess the model’s ability to reason about the execution of simple Python programs by asking it to predict the input given the output of a function and vice-versa (Section 4.1).
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
  - [WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models](https://aclanthology.org/2025.acl-long.246.pdf)
  - [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1672.pdf)
- **Code output prediction** (behavioral indicator): *measured_by*, 3 papers
  > two code-understanding tasks—namely, CruxEval-I (input prediction) and CruxEval-O (output prediction) from CruxEval benchmark [6] (Section 4.1).
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **Code input prediction** (behavioral indicator): *measured_by*, 1 paper
  > two code-understanding tasks—namely, CruxEval-I (input prediction) and CruxEval-O (output prediction) from CruxEval benchmark [6] (Section 4.1).
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
- **Abductive code reasoning** (construct): *measured_by*, 1 paper
  > Deductive code and abductive code reasoning can be regarded as opposite processes; therefore, we selected two identical and representative datasets, CRUXEval (Gu et al., 2024) and LiveCodeBench (Jain et al., 2024), as benchmarks to validate these two capabilities.
  - [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > Furthermore, we also evaluate all the models on four logical reasoning benchmarks to verify the impact of these alignment methods on model’s reasoning abilities, including: ... CRUX (Gu et al., 2024) (Code)...
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
