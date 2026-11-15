# Pointwise scoring
**Type:** Behavioral indicator  
**Supporting papers:** 13  
**Also known as:** Rating-based evaluation, Direct scoring, Single answer grading, Scoring, Point-wise scoring, Response rating, Overall rating assignment, Score prediction, Pointwise grading  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a single-response judging task in which an evaluator assigns a numerical or ordinal score to one model-generated answer, usually on a Likert or comparable evaluation scale. Most definitions make the success criterion the production of that scalar rating for the candidate response, often under predefined or specified criteria such as consistency, coherence, fluency, relevance, overall quality, usefulness, or perceived quality. A smaller line of work phrases the same behavior more narrowly as the final score-prediction step, and some descriptions note that the score can be given alongside reasoning or critique before a final rating is produced.

**Variants.** Papers use several near-synonymous names for this behavior, including direct scoring, rating-based evaluation, single answer grading, response rating, overall rating assignment, and pointwise grading. The dominant setting is evaluation of a single response, but papers place it in several domains, including natural language generation, alignment evaluation, and instruction-controllable summarization. Some papers also contrast pointwise scoring with pairwise comparison as an alternative evaluation mode, and a few make the scale concrete with examples such as 1 to 5 or 1 to 7.

**Space of elicitation and scores.** Papers link pointwise scoring to one measurement instrument, InstruSum. It is described as a benchmark representing pointwise scoring of instruction controllable summarization.

**What it is taken as evidence of.** No papers explicitly link pointwise scoring to a construct, so it is not presented as evidence of a named construct in the reported relationships.

## Sources

**Direct scoring** (1 paper: [Are Checklists Really Useful for Automatic Evaluation of Generative Tasks?](https://aclanthology.org/2025.emnlp-main.538.pdf))
> Assigning a numerical score to an LLM-generated response on a Likert scale based on predefined evaluation criteria.

**Rating-based evaluation** (1 paper: [Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction](https://aclanthology.org/2025.emnlp-main.569.pdf))
> The process of assigning a scalar score on a Likert scale to evaluate the quality of generated text, typically based on criteria like consistency, coherence, fluency, and relevance.

**Single answer grading** (1 paper: [JudgeLM: Fine-tuned Large Language Models are Scalable Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f8f73134e253845a8f82983219a8452-Paper-Conference.pdf))
> The observable task of evaluating a single model-generated answer and assigning it a score.

**Scoring** (1 paper: [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf))
> The observable task where an LLM judge provides a numerical score for a single given response based on specified criteria.

**Point-wise scoring** (1 paper: [BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf))
> Assigning a numerical score to a candidate response on an evaluation scale.

**Response rating** (1 paper: [Peering Through Preferences: Unraveling Feedback Acquisition for Aligning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/48a4f41ff000b121eabe7b2491b24aef-Paper-Conference.pdf))
> The observable act of assigning a numerical score (e.g., 1–7) to a single model-generated response based on its perceived quality.

**Overall rating assignment** (1 paper: [Generative Judge for Evaluating Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/747dc7c6566c74eb9a663bcd8d057c78-Paper-Conference.pdf))
> The task of assigning a numerical score to a single model response to quantify its overall quality or usefulness.

**Score prediction** (1 paper: [TRACT: Regression-Aware Fine-tuning Meets Chain-of-Thought Reasoning for LLM-as-a-Judge](https://aclanthology.org/2025.acl-long.147.pdf))
> The specific action of outputting a numerical score as the final step of an evaluation task.

**Pointwise grading** (1 paper: [Praetor: A Fine-Grained Generative LLM Evaluator with Instance-Level Customizable Evaluation Criteria](https://aclanthology.org/2025.acl-long.513.pdf))
> Assigning a numerical score to a single model response based on predefined or inferred evaluation criteria.

## Relationships

### Pointwise scoring →
- **InstruSum** (measurement instrument): *measured_by*, 1 paper
  > "We evaluate CAMIEVAL on two benchmarks, LLMBar (Zeng et al., 2023) and InstruSum (Liu et al., 2023c), which respectively represent pairwise evaluation of instruction-following and pointwise scoring of instruction controllable summarization."
  - [CAMIEval: Enhancing NLG Evaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.438.pdf)
