# LongEval
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across definitions, LongEval is most commonly described as a benchmark for long-context performance, or for tasks that require understanding long-span context. The prevailing description is a retrieval-focused benchmark composed of topic retrieval and line retrieval tasks with varying prompt lengths, while another paper characterizes it more broadly as an early benchmark with various long context retrieval tasks.

**What it is claimed to measure.** Papers link LongEval to one construct and one behavioral indicator. The prevailing measurement claim is Long-context understanding, with papers describing LongEval as designed to measure long-context performance; a smaller line of work uses it to measure Synthetic recall and describes it as a benchmark for long-context retrieval abilities where answer tokens can be separated from non-answer tokens.

**Space of uses.** No other measurement instrument is linked to it. Papers use it as a benchmark for additional experiments and more comprehensive analyses of model scalability in long-context settings, and another paper positions StreamEval as a dataset inspired by LongEval.

## Sources

**LongEval** (3 papers: [Efficient Streaming Language Models with Attention Sinks](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e5fd18f863cbe6d8ae392a93fd271c9-Paper-Conference.pdf), [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf), [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf))
> A benchmark designed to measure the long-context performance of language models, consisting of topic retrieval and line retrieval tasks with varying prompt lengths.

## Relationships

### → LongEval
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > we conducted additional experiments on the LongEval benchmark (Li et al., 2023), which is designed to measure long-context performance (Section 5.3).
  - [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf)
- **Synthetic recall** (behavioral indicator): *measured_by*, 1 paper
  > we conduct experiments on LongEval (Li et al., 2023a), a benchmark for long-context retrieval abilities, where we can separate the answer tokens that match the desired answers (e.g., <45129> in Figure 2(a)) from non-answer tokens. (Section 2.1)
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
