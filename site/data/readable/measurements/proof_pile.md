# Proof-pile
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** Proof-Pile  

## State of the Field

**What it is.** Across the surveyed papers, Proof-pile is most commonly described as a long-context language modeling dataset centered on mathematical material, either as a cleaned Arxiv Math dataset or, more specifically, as a 13GB collection of long mathematical documents. The descriptions converge on long-form technical or scientific content with many long sequence samples, though some authors describe it more broadly as scientific and technical texts rather than emphasizing Arxiv Math.

**What it is claimed to measure.** Papers use Proof-pile to evaluate language modeling performance on long sequences, most often through perplexity, including long-sequence or long-context performance in technical, scientific, or mathematical domains. No paper links it to a named construct or behavioral indicator, so the recorded descriptions stay at the level of language modeling performance and perplexity rather than a broader measurement claim.

**Space of uses.** Papers most often use Proof-pile alongside GovReport for long-context evaluation, and another study places it beside PG19 and CodeParrot in a perplexity comparison. It is typically used in evaluation settings, with papers reporting perplexity on the test set or selecting random samples with at least 128k tokens each for evaluation.

## Sources

**Proof-pile** (3 papers: [LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/211ab571cc9f3802afa6ffff52ae3e5b-Paper-Conference.pdf), [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf), [YaRN: Efficient Context Window Extension of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/874a4d89f2d04b4bcf9a2c19545cf040-Paper-Conference.pdf))
> Cleaned Arxiv Math dataset used for evaluating long-sequence language modeling performance in scientific domains via perplexity.

**Proof-Pile** (1 paper: [A Silver Bullet or a Compromise for Full Attention? A Comprehensive Study of Gist Token-based Context Compression](https://aclanthology.org/2025.acl-long.241.pdf))
> A dataset of scientific and technical texts used for evaluating language modeling performance on domain-specific long-form content.
