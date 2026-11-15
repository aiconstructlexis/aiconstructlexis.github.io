# Calculation error
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats calculation error as an observable error in which a model gives an incorrect result because of mistakes in numerical or symbolic computation, even when the reasoning process may otherwise be correct. In "UGMathBench: A Diverse and Dynamic Benchmark for Undergraduate-Level Mathematical Reasoning with Large Language Models," this behavior is described as a major concern, and the paper states that calculation errors, including numerical and expression errors, form the largest error category it reports.

**Variants.** The only explicit variants named in the papers are numeric calculation error and expression calculation error. No other task settings, domains, or modalities are separately distinguished for this behavior in the evidence.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument, Manual error analysis. The recorded use is an in-depth human analysis of error cases, where authors identify common error types and include calculation error among them, rather than scoring it with an automated metric or benchmark-specific rubric.

**What it is taken as evidence of.** Papers do not link calculation error to any construct in the recorded relationships, so the evidence does not specify what broader construct this behavior is taken to indicate.

## Sources

**Calculation error** (1 paper: [UGMathBench: A Diverse and Dynamic Benchmark for Undergraduate-Level Mathematical Reasoning with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c3af3531df85264decc31382cb319781-Paper-Conference.pdf))
> An observable error where the model produces an incorrect result due to mistakes in numerical or symbolic computation, despite potentially having a correct reasoning process.

## Relationships

### Calculation error →
- **Manual error analysis** (measurement instrument): *measured_by*, 1 paper
  > we conduct an in-depth human analysis of the error cases... Through in-depth analysis, we have identified the following ﬁve common error types that current MLLMs are likely to make: ... (5) Calculation Error... (Section 4)
  - [Are Multimodal LLMs Robust Against Adversarial Perturbations? RoMMath: A Systematic Evaluation on Multimodal Math Reasoning](https://aclanthology.org/2025.naacl-long.582.pdf)
