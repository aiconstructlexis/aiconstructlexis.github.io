# Context retention
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Information retention, Sustained context management, Memory retention  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats context retention as the ability to maintain, store, access, and use relevant information over long contexts, multiple conversational turns, or long generated sequences. Most definitions stay close to this long-context or multi-turn framing, though one paper makes the boundary explicit by defining information retention as storing and accessing relevant facts within a long context, distinct from reasoning over them in sequence. A smaller line uses the memory retention label more broadly, referring either to preserving knowledge not targeted for unlearning or to preserving recorded memories so they can support later recall.

**Space of facets.** Papers organize the construct mainly by setting: long and complex contexts, multi-turn dialogue or instruction streams, long output generation, and settings where later actions or function call results must use earlier context correctly. The clearest conceptual contrast is with sequential reasoning, while other quoted passages discuss it alongside coherence management and dynamic decision-making rather than as the same thing. The naming is not uniform: information retention, sustained context management, and memory retention are used for closely related long-context abilities, but memory retention is also used for untargeted knowledge preservation after unlearning and for later recall from recorded memories.

**Space of measurement.** No measurement instrument is linked to it. Papers link it to 2 behavioral indicators, Instruction following and Task completion, and to 1 construct, Coherence. In the quoted usages, it is examined through sequential instruction tasks, multi-turn long context queries or function call results, and long output generation over extended sequences; the reported outcomes mirror the definitions' focus on maintaining and using earlier information, because failures are described as loss of adherence to task instructions, incomplete task execution, and loss of coherence.

**Links.** Only causal links are reported. One paper claims a causal relationship from context retention to Coherence and to Instruction following, stating that memory retention issues often lead to loss of coherence and adherence to task instructions. Another paper claims a causal relationship from context retention to Task completion, reporting that agents can lose context during complex tasks or app transitions, which leads to incomplete task execution.

## Sources

**Information retention** (1 paper: [seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs](https://aclanthology.org/2025.emnlp-main.1714.pdf))
> The capacity to store and access relevant facts within a long context, distinct from the ability to reason over them in sequence.

**Context retention** (1 paper: [LoCt-Instruct: An Automatic Pipeline for Constructing Datasets of Logical Continuous Instructions](https://aclanthology.org/2025.emnlp-main.1734.pdf))
> The ability to maintain and utilize information presented over long and complex contexts or across multiple conversational turns.

**Sustained context management** (1 paper: [The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf))
> The ability to maintain relevant conversational or task context across multiple turns and use it correctly in later actions.

**Memory retention** (1 paper: [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf))
> The model's ability to maintain and access information and instructions over the course of generating a long sequence of text.

## Relationships

### Context retention →
- **Coherence** (construct): *causes*, 1 paper
  > This highlights the memory retention issue in long-context models, which often leads to a loss of coherence and adherence to task instructions. (Section 3.2)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > This highlights the memory retention issue in long-context models, which often leads to a loss of coherence and adherence to task instructions. (Section 3.2)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **Task completion** (behavioral indicator): *causes*, 1 paper
  > Memory retention mechanisms can be improved as well, especially for handling long, multi-step tasks that span multiple apps. Current agents often lose context during complex tasks or app transitions, which leads to incomplete task execution.
  - [SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf)
