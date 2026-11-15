# Passkey retrieval
**Type:** Measurement instrument  
**Supporting papers:** 18  
**Also known as:** Passkey retrieval task, Passkey Retrieval Task, Passkey Retrieval  

## State of the Field

**What it is.** Across papers, the prevailing usage treats passkey retrieval as a synthetic long-context task or benchmark in which a model must recover a random passkey, usually a five-digit number, hidden at some depth in a long document or in long, meaningless or distracting text. Definitions differ slightly in calling it a task, benchmark, or evaluation protocol, but they converge on the same setup: the model is asked to find, retrieve, and sometimes repeat a short target token embedded within a lengthy context. Some papers further describe it as a needle-in-haystack setting for testing long-range dependency, information retention, or the maximum distance that a token can attend to during inference.

**What it is claimed to measure.** Papers link this instrument to 1 construct and 2 behavioral indicators. The most common use is to measure Synthetic recall, with papers describing it as assessing whether a model can retrieve an n-digit or five-digit passkey from a large context, and one paper reporting "perfect memory recall on the Passkey Retrieval task." A smaller line of work uses it to measure Context retrieval, and another uses it to measure Long-context understanding, describing the task as widely used to evaluate the maximum context length a model can effectively handle.

**Space of uses.** Papers commonly use passkey retrieval as a synthetic long-context evaluation, often reporting retrieval accuracy or accuracy on passkey retrieval. Usage varies by where the passkey is placed, with papers describing random sequence depth, a given depth, random location, and different difficulty levels; one protocol uses a contiguous 2K token sample from Wiki-Text, and another pairs passkey accuracy with perplexity on a validation set from C4. No measurement instrument is linked to it.

## Sources

**Passkey retrieval** (4 papers: [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf), [LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/211ab571cc9f3802afa6ffff52ae3e5b-Paper-Conference.pdf), [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf), [YaRN: Efficient Context Window Extension of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/874a4d89f2d04b4bcf9a2c19545cf040-Paper-Conference.pdf))
> Task where a model must retrieve a hidden passkey (random number) embedded in long, distracting text; used to evaluate maximum effective context length.

**Passkey retrieval task** (2 papers: [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf), [Understanding and Improving Length Generalization in Recurrent Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/buitrago25a/buitrago25a.pdf))
> A long-context retrieval evaluation in which a hidden 5-digit code must be recovered from within a long input sequence.

**Passkey Retrieval Task** (1 paper: [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf))
> A synthetic evaluation protocol designed to test long-context retrieval by requiring a model to find and repeat a random passkey hidden within a long text sample.

**Passkey Retrieval** (1 paper: [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf))
> A needle-in-haystack benchmark that evaluates a model's ability to retrieve a short target token (e.g., a five-digit number) from a long context of distractor text, testing long-range dependency and information retention.

## Relationships

### → Passkey retrieval
- **Synthetic recall** (behavioral indicator): *measured_by*, 6 papers
  > The passkey retrieval task as defined in Mohtashami and Jaggi (2023) measures a model’s ability to retrieve a simple passkey (i.e., a five-digit number) from amongst a large amount of otherwise meaningless text. (Section 4.3)
  - [YaRN: Efficient Context Window Extension of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/874a4d89f2d04b4bcf9a2c19545cf040-Paper-Conference.pdf)
  - [Extending LLM Context Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.28.pdf)
  - [Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf)
  - [Rethinking Addressing in Language Models via Contextualized Equivariant Positional Encoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25t/zhu25t.pdf)
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **Context retrieval** (behavioral indicator): *measured_by*, 1 paper
  > Additionally, evaluations on the passkey retrieval task [33, 29] reveal that SSA substantially enhances the retrieval capabilities of the transformer, shown in Table 4.
  - [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > “The task is widely used to evaluate the maximum context length that the model can effectively handle.”
  - [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf)
