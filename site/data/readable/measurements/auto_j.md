# AUTO-J
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** AutoJ Eval  

## State of the Field

**What it is.** Across the papers, AUTO-J is most commonly treated as an automated judge, described as a 13B-parameter generative judge model or more generally an LLM-based evaluator. Definitions emphasize its use for rating response helpfulness on a numeric scale, while another description says it is used to assess the distance between a reference answer and a model output. Some authors distinguish AutoJ Eval, an in-domain pairwise-comparison test set from AUTO-J with 58 prompts and 1,392 response pairs labeled by human annotators as win, tie, or lose.

**What it is claimed to measure.** The reported measurement claims are narrow rather than spread across many targets: papers link AUTO-J to one construct, Helpfulness, and one behavioral indicator, Text summarization. For Helpfulness, papers use it to provide ratings on a 1 to 10 scale for model responses; for Text summarization, a paper reports using the Auto-J model to measure the win rate of model-generated summaries against human summaries.

**Space of uses.** Papers position AUTO-J mainly as an automated evaluator or judge. It is used alongside other evaluators in some reports, including joint rating with GPT-4, and one paper mentions it with ARES and PROMETHEUS as LLM judges for assessing reference-output distance. A smaller usage treats AutoJ Eval as an in-domain pairwise-comparison set with human preference labels.

## Sources

**AUTO-J** (2 papers: [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf), [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf))
> A 13B-parameter generative judge model used as an automated evaluator to rate the helpfulness of model responses on a numeric scale.

**AutoJ Eval** (1 paper: [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf))
> An in-domain pairwise-comparison test set from AUTO-J containing 58 prompts and 1,392 response pairs labeled as win, tie, or lose.

## Relationships

### → AUTO-J
- **Helpfulness** (construct): *measured_by*, 1 paper
  > To evaluate the model’s responses, we enlist the assistance of both AUTO-J (Li et al., 2023a) and GPT-4 (i.e., gpt-4-0613; OpenAI (2023a)), which provide ratings on a scale of 1 to 10. (Section 4.6)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **Text summarization** (behavioral indicator): *measured_by*, 1 paper
  > Since human-labeled summaries are available, we measure the win rate of the model-generated summaries against the human ones using the Auto-J model (Li et al., 2023a). (Section 7.1)
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
