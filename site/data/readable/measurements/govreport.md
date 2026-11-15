# GovReport
**Type:** Measurement instrument  
**Supporting papers:** 14  
**Also known as:** SUM-GOVREPORT  

## State of the Field

**What it is.** Most papers describe GovReport as a long-document summarization dataset or benchmark built from U.S. government and congressional reports. The prevailing framing emphasizes long inputs, often stating an average document length of 7,866 tokens; one quoted passage adds that it comprises 19,402 reports, and another places it in the SCROLL benchmark for summarizing long government reports. A smaller naming variant treats it as SUM-GOVREPORT, described as a summarization task over long government reports with complex structure and content.

**What it is claimed to measure.** Papers use GovReport mainly to measure text summarization: it is linked to 1 behavioral indicator and 1 construct, and the recurring behavioral indicator is Text summarization. Several papers explicitly describe evaluation on GovReport as "the summarization task" or as testing "long text summarization capacity." A narrower line of use reports it as measuring Length generalization, with one paper including it in "length extrapolation on six long benchmarks."

**Space of uses.** No other measurement instrument is linked to it through recorded relationships. In use, papers commonly position GovReport as a long-context or long-document evaluation benchmark, and quoted passages show it being used alongside Proof-pile for long sequence language modeling, QMSum in SCROLL reporting, and Multi-News for summarization comparisons; as one paper puts it, "we utilize GovReport benchmark ... to test the long text summarization capacity" (IAM: Efficient Inference through Attention Mapping between Different-scale LLMs).

## Sources

**GovReport** (7 papers: [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf), [YaRN: Efficient Context Window Extension of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/874a4d89f2d04b4bcf9a2c19545cf040-Paper-Conference.pdf), [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf), [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf), [IAM: Efficient Inference through Attention Mapping between Different-scale LLMs](https://aclanthology.org/2025.acl-long.959.pdf), [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf))
> Summarization dataset of U.S. government and congressional reports, used to evaluate language modeling performance on long documents with an average length of 7,866 tokens.

**SUM-GOVREPORT** (1 paper: [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf))
> Summarization task involving long government reports with complex structure and content.

## Relationships

### → GovReport
- **Text summarization** (behavioral indicator): *measured_by*, 4 papers
  > GovReport [25] is a generic summarization dataset containing long reports published by the U.S. Government Accountability Office (Section 4.1).
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
  - [Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query](https://aclanthology.org/2025.emnlp-main.1732.pdf)
- **Length generalization** (construct): *measured_by*, 1 paper
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
