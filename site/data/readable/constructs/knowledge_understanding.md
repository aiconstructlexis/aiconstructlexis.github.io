# Knowledge understanding
**Type:** Construct  
**Supporting papers:** 8  
**Also known as:** Knowledge comprehension, Knowledge and understanding  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats knowledge understanding as a model ability, often a latent one, to comprehend, represent, and use factual, conceptual, or domain knowledge when processing inputs and generating outputs. Most definitions also stress correct application, either to information presented in a question or to broader general world and domain-specific knowledge on diverse cognitive tasks. A smaller variation broadens the construct to include acquiring and retaining knowledge from training data, and some papers pair it with reasoning or distinguish it from instruction-following.

**Space of facets.** Papers use closely related labels, especially knowledge comprehension, knowledge understanding, and knowledge and understanding, for largely overlapping ideas centered on using knowledge. The construct is sometimes scoped narrowly to factual or conceptual information in a question, and elsewhere more broadly to general world knowledge, domain-specific knowledge, or world knowledge across STEM, social sciences, and humanities, including spoken interactions. One line of work also refers to an understanding level with concept tasks and relates it to knowledge memorization.

**Space of measurement.** Operationalization is entirely instrument-based in the recorded links: the construct is linked to 5 measurement instruments and no behavioral indicators. The named instruments are MMMLU, Open LLM Leaderboard v2, TruthfulQA, VoxEval, and lm-evaluation-harness. Papers use them to evaluate knowledge comprehension or knowledge and understanding through multilingual evaluation, pure speech interactions, or broader suites of zero-shot natural language tasks.

**Links.** Outside measurement, one paper claims a causal relationship from Knowledge memorization to Knowledge understanding. Its evidence says the memorization level shows notable correlations with concept tasks in the understanding level, and interprets this as those high-level tasks relying heavily on knowledge memory. No correlates or undirected related links are reported.

## Sources

**Knowledge comprehension** (1 paper: [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf))
> The ability of a model to understand and correctly apply factual or conceptual information presented in a question.

**Knowledge understanding** (1 paper: [Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf))
> The latent ability to represent and use factual or domain knowledge when processing inputs and generating outputs.

**Knowledge and understanding** (1 paper: [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf))
> The latent ability of a model to acquire, retain, and apply general world knowledge and domain-specific information from training data to perform well on diverse cognitive tasks.

## Relationships

### Knowledge understanding →
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our models on a total of 9 different zero-shot benchmarks to assess their abilities across various natural language tasks like common sense reasoning, general language understanding and knowledge understanding using the LLM Evaluation Harness [14]. (Section 4.3)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **Open LLM Leaderboard v2** (measurement instrument): *measured_by*, 1 paper
  > We use Open LLM Leaderboard 2 (Fourrier et al., 2024), and TruthfulQA (Lin et al., 2021) for the evaluation. (Section 3.2, under the heading 'Knowledge & Understanding')
  - [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > We use Open LLM Leaderboard 2 (Fourrier et al., 2024), and TruthfulQA (Lin et al., 2021) for the evaluation. (Section 3.2, under the heading 'Knowledge & Understanding')
  - [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf)
- **VoxEval** (measurement instrument): *measured_by*, 1 paper
  > To address these limitations, we present VoxEval, a novel SpeechQA benchmark that assesses SLMs’ knowledge understanding through pure speech interactions. (Abstract)
  - [VoxEval: Benchmarking the Knowledge Understanding Capabilities of End-to-End Spoken Language Models](https://aclanthology.org/2025.acl-long.818.pdf)
- **MMMLU** (measurement instrument): *measured_by*, 1 paper
  > the OpenAI multilingual version of MMLU (MMMLU)1 for knowledge comprehension (Section 2)
  - [P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs](https://aclanthology.org/2025.emnlp-main.242.pdf)

### → Knowledge understanding
- **Knowledge memorization** (construct): *causes*, 1 paper
  > The knowledge memorization (KM) level shows notable correlations with other levels, especially with the concept tasks in the understanding level ... which indicates that these high-level tasks rely heavily on knowledge memory. (Section 3)
  - [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf)
