# LongGenBench
**Type:** Measurement instrument  
**Supporting papers:** 2  

## State of the Field

Benchmark designed for extreme-length generation with multi-shot in-context examples, testing long-context reasoning and comprehension.

## Sources

**LongGenBench** (1 paper: [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf))
> Benchmark designed for extreme-length generation with multi-shot in-context examples, testing long-context reasoning and comprehension.

## Relationships

### → LongGenBench
- **Long-form text generation** (behavioral indicator): *measured_by*, 2 papers
  > We introduced LongGenBench, a synthetic benchmark that evaluates long-form generation capabilities of language models by testing their ability to follow instructions over extended sequences. (Section 6)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > We introduced LongGenBench, a synthetic benchmark that evaluates long-form generation capabilities of language models by testing their ability to follow instructions over extended sequences. (Section 6)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **Long-context generation** (behavioral indicator): *measured_by*, 1 paper
  > In this work, we leverage LONGGENBENCH, which focuses on long-input and long-output tasks (Liu et al., 2024c), to optimize KV cache compression in scenarios where the output can be as long as 8K tokens (Section 6).
  - [SCOPE: Optimizing Key-Value Cache Compression in Long-context Generation](https://aclanthology.org/2025.acl-long.529.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > (3) Long-Context Understanding: LongBench (Bai et al., 2024), LongGenBench (Liu et al., 2024a), and Needle-in-the-haystack (Kamradt, 2023) (Sec. 2.2)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
