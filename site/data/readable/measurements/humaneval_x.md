# HumanEval-X
**Type:** Measurement instrument  
**Supporting papers:** 7  
**Also known as:** HumanEval-Multi  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats HumanEval-X as a multilingual benchmark for code generation, often described as a multilingual extension of HumanEval. Definitions describe it as translating HumanEval’s Python problems into multiple languages, and one paper further characterizes it as a comprehensive benchmark covering Python, C++, Java, JavaScript, and Go. A smaller naming variant, HumanEval-Multi, refers to the multilingual version of HumanEval and describes it as evaluating the functional correctness of model-generated code, used as a test dataset for utility.

**What it is claimed to measure.** Papers link this instrument to 2 behavioral indicators and to no constructs. The dominant claim is that it measures Code generation: papers report pass@1 on HumanEval-X for multilingual code generation and say it aims to evaluate multilingual code generation abilities. A smaller line of work uses it to measure Code translation, with one paper reporting Java-to-C++ translation performance on the HumanEval-X benchmark.

**Space of uses.** Papers commonly place it inside broader code evaluation suites, including use as one of several code benchmarks. Some papers use the multilingual version as a test dataset for utility, while another uses evaluation on the HumanEval-X dataset to report variation in expert activation frequencies within MoE blocks. No measurement instrument is linked to it.

## Sources

**HumanEval-X** (3 papers: [MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duanmu25a/duanmu25a.pdf), [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf), [StackEval: Benchmarking LLMs in Coding Assistance](https://proceedings.neurips.cc/paper_files/paper/2024/file/4126a607bbe2836cb6ca0eb45b75618b-Paper-Datasets_and_Benchmarks_Track.pdf))
> A multilingual benchmark for evaluating the code generation capabilities of large language models.

**HumanEval-Multi** (1 paper: [ProSec: Fortifying Code LLMs with Proactive Security Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25aa/xu25aa.pdf))
> A multilingual benchmark for evaluating the functional correctness of model-generated code, used in this paper to assess model utility.

## Relationships

### → HumanEval-X
- **Code generation** (behavioral indicator): *measured_by*, 2 papers
  > We compare the pass@1 accuracy of the base models and the corresponding fine-tuned AlchemistCoder models on Humaneval-X [49]. (Section 3.2, under heading 'Results on multilingual code generation.')
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
- **Code translation** (behavioral indicator): *measured_by*, 1 paper
  > underperforms for Java-to-C++ translation on the HumanEval-X benchmark (48.8% versus 82.3%).
  - [PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25m/hu25m.pdf)
