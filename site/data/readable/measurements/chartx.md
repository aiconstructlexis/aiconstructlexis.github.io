# ChartX
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across the papers, the prevailing framing is a chart-to-code benchmark for assessing text and data reproducibility in generated code, with attention to accurate rendering of chart content. A smaller usage treats ChartX as a figure description dataset, specifically as one of the sampled sources for F2TBenchmark. One paper further describes it as providing fixed instructions to GPT-4 to write code that procedurally generates predefined chart types and settings in bulk.

**What it is claimed to measure.** Papers link ChartX to 2 behavioral indicators and no constructs. The recorded uses are Code generation, where one paper says it evaluates MLLMs' code generation ability, especially for text and data reproducibility, and Figure-to-text generation, where another paper lists it under figure description. The measurement claims therefore spread across 2 behavioral indicators rather than converging on a construct.

**Space of uses.** In chart-to-code work, papers use ChartX alongside ChartMimic and Plot2Code as one of the benchmarks on which methods are evaluated. In figure-to-text work, one paper uses it differently, as one of the sampled sources for F2TBenchmark.

**Concerns raised.** A concern raised in one paper is that ChartX generates charts by giving GPT-4 fixed instructions to produce predefined chart types and settings in bulk, which that paper characterizes as artificial charts from a narrow distribution.

## Sources

**ChartX** (3 papers: [ChartCoder: Advancing Multimodal Large Language Model for Chart-to-Code Generation](https://aclanthology.org/2025.acl-long.363.pdf), [F2TEval: Human-Aligned Multi-Dimensional Evaluation for Figure-to-Text Task](https://aclanthology.org/2025.emnlp-main.195.pdf), [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf))
> Chart-to-code benchmark assessing text and data reproducibility in generated code, with a focus on accurate rendering of chart content.

## Relationships

### → ChartX
- **Code generation** (behavioral indicator): *measured_by*, 1 paper
  > Similarly, Plot2Code (Wu et al., 2024) and ChartX (Xia et al., 2024) also evaluate MLLMs code generation ability, especially for text and data reproducibility (Section 2.2).
  - [ChartCoder: Advancing Multimodal Large Language Model for Chart-to-Code Generation](https://aclanthology.org/2025.acl-long.363.pdf)
- **Figure-to-text generation** (behavioral indicator): *measured_by*, 1 paper
  > "ChartX (Xia et al., 2024) | Figure Des."
  - [F2TEval: Human-Aligned Multi-Dimensional Evaluation for Figure-to-Text Task](https://aclanthology.org/2025.emnlp-main.195.pdf)
