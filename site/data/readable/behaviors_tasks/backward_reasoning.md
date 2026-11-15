# Backward reasoning
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage is a reverse-solution task: the model is given the original answer, or the answer together with the solution, and must infer a concealed input or missing value. Papers describe this as concealing one of the inputs and computing it from the provided answer, or as inferring missing information from the solution to reason backwards and check consistency; a smaller formulation, in "Reverse Thinking Makes LLMs Stronger Reasoners", treats it as solving a reversed question and generating step-by-step backward reasoning back toward the original problem context.

**Variants.** Variants mainly differ in what is hidden and what intermediate object is posed. Most formulations mask one input or a numerical value from the original problem and ask for recovery from the original answer or solution, while another formulation derives a backward question from the solution and asks for a step-by-step justification; papers use both "reversed reasoning" and "backward reasoning" for these forms.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead operationalize it directly through masked-input and reversed-question prompts, such as requiring the model to infer a missing value from the original solution or to generate backward reasoning from a backward question.

**What it is taken as evidence of.** The only linked construct is Mathematical reasoning, and that link is not framed as measurement. Instead, one paper claims a causal relationship from backward reasoning to mathematical reasoning, reporting improved mathematical reasoning ability.

## Sources

**Backward reasoning** (3 papers: [MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0b0e6ac2da44d5839b13f90625b357-Paper-Conference.pdf), [CogMath: Assessing LLMs’ Authentic Mathematical Ability from a Human Cognitive Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ab/liu25ab.pdf), [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf))
> The observable task of computing a missing input variable in a problem when the final answer is already provided.

## Relationships

### Backward reasoning →
- **Mathematical reasoning** (construct): *causes*, 1 paper
  > ...demonstrating the effectiveness of SV and FOBAR augmentation data in improving mathematical reasoning ability. (Section 4.3)
  - [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c400474e8a36d0812fdee52739288b12-Paper-Conference.pdf)
