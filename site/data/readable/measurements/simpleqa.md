# SimpleQA
**Type:** Measurement instrument  
**Supporting papers:** 9  

## State of the Field

**What it is.** Papers most commonly describe SimpleQA as an OpenAI benchmark made up of numerous concise, fact-oriented, fact-seeking questions for assessing LLM factual capabilities in general knowledge. A narrower description presents it specifically as a factuality benchmark in which model responses are categorized as correct, incorrect, or not attempted.

**What it is claimed to measure.** Papers use SimpleQA to measure two constructs, Factuality and Truthfulness, and one behavioral indicator, Factual question answering. The prevailing usage stays within factual evaluation: one paper says it was proposed to measure short-form factuality in LLMs, another takes it for truthfulness, and another describes it as evaluating the ability of language models to answer fact-seeking questions.

**Space of uses.** The clearest paired use is alongside FreshQA-2025-04-28, where a paper presents the two as factuality benchmarks for fact-seeking questions. Otherwise, no measurement instrument is linked to it, and papers position SimpleQA as a benchmark used for short-form factuality or truthfulness evaluation.

## Sources

**SimpleQA** (2 papers: [Chinese SafetyQA: A Safety Short-form Factuality Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.732.pdf), [Thinking Out Loud: Do Reasoning Models Know When They're Right?](https://aclanthology.org/2025.emnlp-main.73.pdf))
> A benchmark introduced by OpenAI comprising numerous concise, fact-oriented questions to assess the factual capabilities of LLMs in general knowledge areas.

## Relationships

### → SimpleQA
- **Factuality** (construct): *measured_by*, 1 paper
  > Recently, SimpleQA (Wei et al., 2024) has been proposed to measure the short-form factuality in LLMs (Section 2).
  - [Chinese SimpleQA: A Chinese Factuality Evaluation for Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)
- **Truthfulness** (construct): *measured_by*, 1 paper
  > We take SimpleQA (Wei et al., 2024b) for truthfulness... (Section 3.1)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **Factual question answering** (behavioral indicator): *measured_by*, 1 paper
  > Factuality: SimpleQA (Wei et al., 2024) and FreshQA-2025-04-28 (Vu et al., 2023), two factuality benchmarks that evaluate the ability of language models to answer fact-seeking questions. (Section 3.2)
  - [Thinking Out Loud: Do Reasoning Models Know When They're Right?](https://aclanthology.org/2025.emnlp-main.73.pdf)
