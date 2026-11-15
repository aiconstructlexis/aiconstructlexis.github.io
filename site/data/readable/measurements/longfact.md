# LongFact
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across papers, LongFact is treated as a resource for evaluating factuality in long-form generation, though its format is described differently. One description presents it as a dataset with 250 prompts, while another describes a GPT-4-generated prompt set for benchmarking long-form factuality in open domains, with 2,280 fact-seeking prompts or questions across 38 manually selected topics; as one paper puts it, it contains "2,280 fact-seeking prompts that solicit long-form responses across 38 manually-selected topics" (Long-form factuality in large language models).

**What it is claimed to measure.** Papers describe it as evaluating factuality in long-form generation, and the recorded measurement links connect it to two behavioral indicators, Hallucination and Long-form text generation, with no linked constructs. The measurement claims therefore spread across these two indicators: one paper reports "hallucination on LongFact," while another uses it as the measure for Long-form text generation.

**Space of uses.** No other measurement instrument is linked to it in the papers. Papers position it as a benchmark or evaluation set: one paper includes it among "four fact-seeking long-form generation datasets," while another presents it as a prompt set for benchmarking long-form factuality in open domains.

## Sources

**LongFact** (2 papers: [Improving Factuality with Explicit Working Memory](https://aclanthology.org/2025.acl-long.548.pdf), [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf))
> A dataset with 250 prompts designed to evaluate the factuality of models in long-form generation tasks.

## Relationships

### → LongFact
- **Long-form text generation** (behavioral indicator): *measured_by*, 1 paper
  > “LongFact consists of 2,280 fact-seeking prompts that solicit long-form responses across 38 manually-selected topics.”
  - [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *measured_by*, 1 paper
  > hallucination on LongFact (Figure 1).
  - [Aligning Large Language Models to Follow Instructions and Hallucinate Less via Effective Data Filtering](https://aclanthology.org/2025.acl-long.804.pdf)
