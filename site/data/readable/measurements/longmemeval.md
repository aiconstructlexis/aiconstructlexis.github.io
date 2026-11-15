# LongMemEval
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across the cited work, LongMemEval is described both as a long-term multi-session conversation dataset for evaluating response generation and memory utilization, and as a benchmark for chat assistants' long-context memory. One description presents it as evaluating five core long-term memory abilities, information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention, while another calls it a challenging benchmark covering six memory tasks. The prevailing usage is therefore as a memory-focused evaluation resource, though papers differ on whether they frame it primarily as a dataset or as a benchmark and on how many task categories it contains.

**What it is claimed to measure.** Papers use LongMemEval to measure 6 constructs and 2 behavioral indicators. The most common links are to multi-session reasoning and temporal reasoning, which multiple papers say the benchmark evaluates; other papers also use it to measure length generalization and the behavioral indicators abstention and information extraction, with 3 other constructs also reported. Overall, the measurement claims are spread across several memory and reasoning targets rather than concentrated on a single construct.

**Space of uses.** Papers position LongMemEval as a benchmark for assessing long-context memory, response generation, and related reasoning abilities. No measurement instrument is linked to it, though one paper uses it alongside CLIPPER on two long-context, multi-hop reasoning tasks, and another describes it as a chat-form benchmark within a two-benchmark setup for long-context memory and extrapolation ability.

## Sources

**LongMemEval** (1 paper: [Flexibly Utilize Memory for Long-Term Conversation via a Fragment-then-Compose Framework](https://aclanthology.org/2025.emnlp-main.1069.pdf))
> A long-term multi-session conversation dataset used to evaluate response generation and memory utilization.

## Relationships

### → LongMemEval
- **Multi-session reasoning** (construct): *measured_by*, 2 papers
  > We introduce LONGMEMEVAL, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. (Abstract)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **Temporal reasoning** (construct): *measured_by*, 2 papers
  > We introduce LONGMEMEVAL, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. (Abstract)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **Information extraction** (behavioral indicator): *measured_by*, 1 paper
  > We introduce LONGMEMEVAL, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. (Abstract)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **Abstention** (behavioral indicator): *measured_by*, 1 paper
  > We introduce LONGMEMEVAL, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. (Abstract)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **Memory** (construct): *measured_by*, 1 paper
  > LONGMEMEVAL was a challenging benchmark designed to evaluate the long-context memory ability of chat assistants across six memory tasks... (Section 4.1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **Length generalization** (construct): *measured_by*, 1 paper
  > To assess long-context memory and extrapolation ability, two benchmarks are adopted: a chat-form benchmark LONGMEMEVAL... (Section 1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **Multi-hop reasoning** (construct): *measured_by*, 1 paper
  > We evaluate QRRETRIEVER on two long-context, multi-hop reasoning tasks: LongMemEval (Wu et al., 2025a) and CLIPPER (Pham et al., 2025). (Section 1)
  - [Query-Focused Retrieval Heads Improve Long-Context Reasoning and Re-ranking](https://aclanthology.org/2025.emnlp-main.1214.pdf)
- **Long-term memory** (construct): *measured_by*, 1 paper
  > “LONGMEMEVAL ... was a challenging benchmark designed to evaluate the long-context memory ability of chat assistants across six memory tasks, including ... knowledge update (KU) ...”
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
