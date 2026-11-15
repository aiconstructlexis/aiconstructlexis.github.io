# NeedleBench
**Type:** Measurement instrument  
**Supporting papers:** 4  
**Also known as:** Needlebench  

## State of the Field

**What it is.** Papers most commonly describe NeedleBench as a long-context benchmark built around recall-intensive retrieval tasks. One definition frames it as evaluating whether models can comprehend and retrieve information from long input sequences, while another describes it as a suite of recall-intensive tasks for long-context retrieval and information finding. One paper adds that it tests retrieval and reasoning in complex contexts through three subtasks: Single-Needle Retrieval, Multi-Needle Retrieval, and Multi-Needle Reasoning, and another groups it with synthetic benchmarks that offer control over sequence length and complexity.

**What it is claimed to measure.** Across the papers here, the reported measurement use centers on one behavioral indicator: Synthetic recall. Papers claim NeedleBench measures this indicator, describing it as testing retrieval and reasoning in complex contexts and using it to assess recall or retrieval capabilities. Papers do not link it to any construct or to additional behavioral indicators.

**Space of uses.** In use, papers position NeedleBench as one of the long-context benchmarks focused on models' ability to understand long-context input sequences. One paper treats it, alongside Ruler, as a synthetic benchmark with better control over variables such as sequence length and complexity, while another uses it together with the MQAR task to assess recall or retrieval capabilities. Beyond those co-usage mentions, papers do not link NeedleBench to other measurement instruments.

## Sources

**Needlebench** (1 paper: [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf))
> A benchmark that evaluates long-context models on their ability to comprehend and retrieve information from long input sequences.

**NeedleBench** (1 paper: [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf))
> A suite of recall-intensive tasks designed to test long-context retrieval and information finding in large language models.

## Relationships

### → NeedleBench
- **Synthetic recall** (behavioral indicator): *measured_by*, 2 papers
  > NeedleBench (Li et al., 2024a): Tests retrieval and reasoning in complex contexts through three subtasks: Single-Needle Retrieval, Multi-Needle Retrieval, and Multi-Needle Reasoning.
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
