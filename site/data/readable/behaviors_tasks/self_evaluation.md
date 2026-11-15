# Self-evaluation
**Type:** Behavioral indicator  
**Supporting papers:** 11  
**Also known as:** Inconsistency identification, Self-review, Self-assessment, Self-grading  

## State of the Field

**Space of definitions.** Most commonly described as the model judging the correctness or quality of its own output, self-evaluation appears at the level of summaries, generated text, answers, and intermediate reasoning steps. Papers often operationalize the judgment as a score or confidence estimate, but some ask for written feedback such as an issues report and detailed advice; a smaller line of work extends the behavior to identifying inconsistencies against a dialogue context, checking novelty against a paper database, or assessing generated definition, formulation, and code from execution results. In Towards Multi-dimensional Evaluation of LLM Summarization across Domains and Languages, one formulation defines a "self-evaluation bias rate" as the difference between a model's score for its own summary and the average score from other evaluators.

**Variants.** Papers use several labels for closely related variants, most often self-evaluation, but also inconsistency identification, self-review, self-assessment, and self-grading. The recurring settings are judging summaries, appraising generated text against a criterion such as harmlessness, deciding whether an answer is correct or which answer is better, and assessing the feasibility or correctness of a reasoning path or step. Narrower variants ask the model to identify and categorize inconsistencies between dialogue responses and contexts, pre-check a generated abstract's novelty by comparing it with existing papers, rate components such as a definer, formulator, and code generator based on execution results, or decide whether its own earlier output is an instance of a concept.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers usually elicit it through prompts or follow-up queries that ask the model to evaluate its own production, often yielding a scalar score, a confidence level, a true or false likelihood, or verbal feedback. Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees gives a representative example, asking the model to evaluate the correctness of its answer and using likelihood P(true) as confidence; other papers compare the self-score with other evaluators' average scores, ask the same model in a separate query to grade its response, or base ratings on execution results.

**What it is taken as evidence of.** Papers link it to 2 constructs rather than consistently tying it to a single construct. Confidence is related to self-evaluation in one paper, which defines confidence by using the score and token probability used when the LLM self-evaluates, while another paper claims a causal relationship from self-evaluation to Text generation quality and says evaluation can potentially improve the generated text. Beyond constructs, papers link it to 1 behavioral indicator, with a paper claiming a causal relationship from self-evaluation to Self-correction and stating that self-evaluation and exploration let the model abandon erroneous paths and select the correct one.

## Sources

**Self-evaluation** (6 papers: [Towards Multi-dimensional Evaluation of LLM Summarization across Domains and Languages](https://aclanthology.org/2025.acl-long.702.pdf), [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf), [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf), [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf), [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf), [Do LLMs estimate uncertainty well in instruction-following?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf))
> An LLM assessing the quality of its own generated summary, potentially exhibiting bias in scoring.

**Inconsistency identification** (1 paper: [Enhancing Goal-oriented Proactive Dialogue Systems via Consistency Reflection and Correction](https://aclanthology.org/2025.acl-long.1050.pdf))
> The observable behavior of a model analyzing its own output against a context and explicitly identifying and categorizing types of inconsistencies.

**Self-review** (1 paper: [Many Heads Are Better Than One: Improved Scientific Idea Generation by A LLM-Based Multi-Agent System](https://aclanthology.org/2025.acl-long.1368.pdf))
> A final check where an agent assesses the novelty of a generated abstract by comparing it against a database of existing papers.

**Self-assessment** (1 paper: [Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf))
> Evaluating whether the generated definition, formulation, and code are correct based on the execution result.

**Self-grading** (1 paper: [Potemkin Understanding in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mancoridis25a/mancoridis25a.pdf))
> Evaluating whether a generated response or answer to a question is correct according to the model's own understanding of a concept.

## Relationships

### Self-evaluation →
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > Since the model possesses self-evaluation and exploration capabilities, it can abandon erroneous paths and select the correct one (Figure 1).
  - [GRAT: Guiding Retrieval-Augmented Reasoning through Process Rewards Tree Search](https://aclanthology.org/2025.acl-long.1352.pdf)
- **Text generation quality** (construct): *causes*, 1 paper
  > This result suggests that evaluation can potentially improve the quality of the generated text, which serves as a stepping stone for building RLC method. (Section 4.3)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)

### Associated with
- **Confidence** (construct), 1 paper
  > We define confidence by utilizing the score and the probability of the token responded by the LLM to self-evaluate.
  - [Enhancing Graph Of Thought: Enhancing Prompts with LLM Rationales and Dynamic Temperature Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/c87245c9e8882bc1b6d4ec343d430e71-Paper-Conference.pdf)
