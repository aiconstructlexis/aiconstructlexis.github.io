# Long-context generation
**Type:** Behavioral indicator  
**Supporting papers:** 2  

## State of the Field

Generating text while conditioning on very long input contexts, often beyond 100K tokens.

## Sources

**Long-context generation** (1 paper: [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf))
> Generating text while conditioning on very long input contexts, often beyond 100K tokens.

## Relationships

### Long-context generation →
- **LongBench** (measurement instrument): *measured_by*, 2 papers
  > Accuracy comparison between offline searched layer-wise KV cache precision using KVTuner in Table 5 and 6 and uniform KV precision settings of the sensitive Qwen2.5-7B-Instruct on 20 LongBench long context generation benchmarks. (Table 7)
  - [KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dd/li25dd.pdf)
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **L-Eval** (measurement instrument): *measured_by*, 1 paper
  > evaluate the enhanced LLM's capability to zero-shot undertake multiple tasks in long context understanding and generation, as detailed in Section 4.2... Following the L-Eval benchmark [1]
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **LongGenBench** (measurement instrument): *measured_by*, 1 paper
  > In this work, we leverage LONGGENBENCH, which focuses on long-input and long-output tasks (Liu et al., 2024c), to optimize KV cache compression in scenarios where the output can be as long as 8K tokens (Section 6).
  - [SCOPE: Optimizing Key-Value Cache Compression in Long-context Generation](https://aclanthology.org/2025.acl-long.529.pdf)

### → Long-context generation
- **Contextual understanding** (construct): *causes*, 1 paper
  > These results underscore MoICE's efficacy in enhancing LLMs' ability to understand and generate long contexts, both of which require high context awareness.
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
