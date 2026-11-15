# Sequential reasoning
**Type:** Construct  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing framing is of a latent or inferred ability to understand and reason over sequences across multiple steps. One formulation centers sequences of actions and states in a dynamic environment and stresses maintaining a coherent interpretation over time, while another uses dialogue histories as the example and ties the ability to processing prior utterances in order to choose an appropriate next action. Quoted passages use the term in settings where models "struggle with multi-step sequential reasoning" and where the next token "requires complex, sequential reasoning" over what has been said so far.

**Space of facets.** The usage in the papers spans sequences of actions and states in dynamic environments, long-horizon sequential tasks, and histories of utterances in dialogue. In nearby framing, papers mention it together with compositional reasoning, planning, and length generalization, and one related account links it to multi-hop reasoning by describing sequential reasoning as stepwise chart interpretation.

**Space of measurement.** Operationalization is narrow in the papers: sequential reasoning is linked to 1 measurement instrument and no behavioral indicators. The named instrument is seqBench, described as a tunable benchmark designed explicitly to probe and analyze sequential reasoning capabilities in language models. The measurement framing is presented as direct, with the benchmark introduced to probe the capability itself.

**Links.** Beyond measurement, one paper reports that Multi-hop reasoning is related to Sequential reasoning, stating that sequential reasoning evaluates the model's ability to perform multi-hop reasoning through stepwise chart interpretation.

## Sources

**Sequential reasoning** (2 papers: [ReSeeding Latent States for Sequential Language Understanding](https://aclanthology.org/2025.emnlp-main.1281.pdf), [Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9531a3e64e6167c7e1e671157082682-Paper-Conference.pdf))
> The latent ability to understand and reason over sequences of actions and states, maintaining coherent interpretation across multiple steps in a dynamic environment.

## Relationships

### Sequential reasoning →
- **seqBench** (measurement instrument): *measured_by*, 1 paper
  > we introduce seqBench, a tunable benchmark designed explicitly to probe and analyze sequential reasoning capabilities in language models. (Section 1)
  - [seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs](https://aclanthology.org/2025.emnlp-main.1714.pdf)

### Associated with
- **Multi-hop reasoning** (construct), 1 paper
  > Sequential Reasoning evaluates the model’s ability to perform multi-hop reasoning, interpreting charts in a stepwise manner. (Section 1)
  - [MultiChartQA: Benchmarking Vision-Language Models on Multi-Chart Problems](https://aclanthology.org/2025.naacl-long.566.pdf)
