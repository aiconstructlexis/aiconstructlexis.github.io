# Memory
**Type:** Construct  
**Supporting papers:** 16  
**Also known as:** Memory capacity, Long-term context retention, Information retention, Long-context memory  

## State of the Field

**Space of definitions.** Across papers, memory is most commonly treated as a model or agent capacity to retain, store, recall, and access earlier information so it can be used later, whether in long sequences, long contexts, or multi-step interaction histories. Several definitions make this explicitly long-range, describing "incorporating long-range information in context," retaining context beyond a fixed window, or preserving information from earlier video frames for later questions. A smaller line of work narrows memory to retrieval of factual knowledge stored in model parameters, independent of logical inference, while another frames it as active retrieval and maintenance over short sequences for recalling past stimuli or decisions.

**Space of facets.** The term is spread across nearby labels such as memory capacity, context retention, long-term context retention, information retention, and long-context memory. Papers also use it for different substrates and contents: recurrent or attention state size, conversational history, long video streams, past observations and attempted actions, spatial memory, and parametric memory as knowledge in the model's parameters. A recurring distinction is between memory and reasoning, with papers describing memory recall as retrieving relevant knowledge or storing and accessing facts, separate from chaining them into multi-step inference, and another paper treating memory and reasoning as separate cognitive abilities.

**Space of measurement.** Memory is linked to 3 measurement instruments and no behavioral indicators. All linked instruments are benchmarks: HELMET and LongMemEval are used to assess long-context memory, with LongMemEval described as covering six memory tasks for chat assistants, and TextWorld is used for long-horizon tasks requiring memory alongside planning, exploration, and commonsense. These linked measures line up most directly with the long-context and long-horizon definitions.

**Links.** Papers report 2 construct-level links. One paper claims a causal relationship from chain-of-thought reasoning to memory, stating that chain-of-thought helps identify relevant information from long texts and improves recall of long-context memory. Another paper reports a related link from long-context understanding to memory, with reduced state size described as a bottleneck for long-context understanding; no correlational links are reported.

## Sources

**Memory capacity** (3 papers: [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [Scaling up the State Size of RNN LLMs for Long-Context Scenarios](https://aclanthology.org/2025.acl-long.564.pdf), [Flexibly Utilize Memory for Long-Term Conversation via a Fragment-then-Compose Framework](https://aclanthology.org/2025.emnlp-main.1069.pdf))
> The latent ability of a model to store and access information over a sequence, which can be implicitly increased by architectural features.

**Memory** (4 papers: [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf), [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/01a83bc2f2732a58e6aa731e659e7101-Paper-Conference.pdf), [Disentangling Memory and Reasoning Ability in Large Language Models](https://aclanthology.org/2025.acl-long.84.pdf), [VisEscape: A Benchmark for Evaluating Exploration-driven Decision-making in Virtual Escape Rooms](https://aclanthology.org/2025.emnlp-main.810.pdf))
> The capacity to incorporate and retain relevant long-range interaction history when selecting the next action.

**Context retention** (1 paper: [Training Free Exponential Context Extension via Cascading KV Cache](https://proceedings.iclr.cc/paper_files/paper/2025/file/19a567abaec3990cb40d7a013556fecd-Paper-Conference.pdf))
> The model's ability to maintain and access information from earlier parts of a long sequence for use in later predictions.

**Long-term context retention** (1 paper: [Streaming Video Question-Answering with In-context Video KV-Cache Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/67a9b444cbcd647572c88194619f72d5-Paper-Conference.pdf))
> The model's ability to preserve and access relevant information from earlier parts of a long video stream to answer questions posed later.

**Information retention** (1 paper: [seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs](https://aclanthology.org/2025.emnlp-main.1714.pdf))
> The capacity to store and access relevant facts within a long context, distinct from the ability to reason over them in sequence.

**Long-context memory** (1 paper: [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf))
> The ability of a model to effectively recall, process, and utilize information from very long input sequences.

## Relationships

### Memory →
- **TextWorld** (measurement instrument): *measured_by*, 1 paper
  > tasks requiring long-horizon memory and planning, exploration, and commonsense in TextWorld
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
- **LongMemEval** (measurement instrument): *measured_by*, 1 paper
  > LONGMEMEVAL was a challenging benchmark designed to evaluate the long-context memory ability of chat assistants across six memory tasks... (Section 4.1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **HELMET** (measurement instrument): *measured_by*, 1 paper
  > To assess long-context memory and extrapolation ability, two benchmarks are adopted: ... an application-centric benchmark HELMET (Yen et al., 2024). (Section 1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)

### → Memory
- **Chain-of-thought reasoning** (construct): *causes*, 1 paper
  > Mamba can effectively identify key information from long texts through CoT thinking, thus significantly improving its ability to recall long-context memory. (Section 1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)

### Associated with
- **Long-context understanding** (construct), 1 paper
  > Despite these improvements, the state sizes of RNNs remain much smaller than those of Transformers with a 2k context length, making state size a critical bottleneck for long-context understanding.
  - [Scaling up the State Size of RNN LLMs for Long-Context Scenarios](https://aclanthology.org/2025.acl-long.564.pdf)
