# MMAU
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across the papers, MMAU is most commonly described as a benchmark for expert-level audio reasoning and audio understanding, with sound and music subsets. Definitions also frame it as a Massive Multi-Task Audio Understanding and Reasoning Benchmark for large audio-language models, and one description says it includes information extraction and reasoning questions. The reported results for "MMAU Sound" and "MMAU Music" further show that papers treat those subsets as distinct reported parts of the benchmark.

**What it is claimed to measure.** Papers use MMAU to measure 5 constructs and 3 behavioral indicators, so its reported measurement role is spread across several targets rather than centered on a single one. The most frequently named construct links are audio understanding, audio perception, audio reasoning, domain knowledge, and reasoning, while the linked behavioral indicators are information extraction, knowledge retrieval, and tool use. In the relationship evidence, papers describe it as evaluating understanding and reasoning in complex audio QA tasks, advanced perception and reasoning with domain-specific knowledge, expert-level multimodal reasoning and knowledge-retrieval capabilities, and, in one usage, tool use performance.

**Space of uses.** No measurement instrument is linked to it. Papers position MMAU as an evaluation benchmark for understanding and reasoning capabilities in complex audio QA tasks and, in one survey framing, for auditory expertise, including musical understanding such as melodic structure, harmony, instrument identification, and contextual music interpretation. A smaller usage treats it as a tool-use evaluation setting, where papers report Tool Execution and Tool Planning on MMAU.

## Sources

**MMAU** (1 paper: [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf))
> A benchmark for evaluating expert-level audio reasoning, with sound and music subsets that assess complex understanding beyond basic classification.

## Relationships

### → MMAU
- **Audio understanding** (construct): *measured_by*, 2 papers
  > To further evaluate our model’s understanding and reasoning capabilities in complex audio QA tasks, we conducted experiments on AIR-Bench Chat (Yang et al., 2024) and MMAU (Sakshi et al., 2024) benchmarks. (Section 4.2.2)
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
  - [Towards Holistic Evaluation of Large Audio-Language Models: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **Audio perception** (construct): *measured_by*, 1 paper
  > MMAU emphasizes advanced perception and reasoning with domain-specific knowledge, challenging models to tackle tasks akin to those faced by experts. (ABSTRACT)
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Domain knowledge** (construct): *measured_by*, 1 paper
  > MMAU emphasizes advanced perception and reasoning with domain-specific knowledge, challenging models to tackle tasks akin to those faced by experts. (ABSTRACT)
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Knowledge retrieval** (behavioral indicator): *measured_by*, 1 paper
  > We introduce the Massive Multi-Task Audio Understanding and Reasoning Benchmark (MMAU), a novel benchmark designed to evaluate the expert-level multimodal reasoning and knowledge-retrieval capabilities of large audio-language models (LALMs). (Section 3.1)
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Information extraction** (behavioral indicator): *measured_by*, 1 paper
  > “It includes information extraction1 and reasoning 2 questions”
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > “It includes information extraction1 and reasoning 2 questions”
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Tool use** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate the tool use performance on MMAU (Yin et al., 2024) and report the performance on Tool Execution and Tool Planning.
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
- **Audio reasoning** (construct): *measured_by*, 1 paper
  > To further evaluate our model’s understanding and reasoning capabilities in complex audio QA tasks, we conducted experiments on AIR-Bench Chat (Yang et al., 2024) and MMAU (Sakshi et al., 2024) benchmarks. (Section 4.2.2)
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
