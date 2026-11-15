# DialogSum
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** Dialogsum  

## State of the Field

**What it is.** Most papers treat DialogSum as a dialogue summarization dataset or benchmark. Definitions and quoted passages describe it as a large-scale resource of dialogues paired with manually labeled summaries, and one description adds topics and a total of 13,460 dialogues. A smaller line of work uses it beyond dialogue summarization evaluation, rebuilding it for instruction tuning, using it as dialogue context for grammar analysis, or using it for summary-to-dialogue generation.

**What it is claimed to measure.** Across papers, DialogSum is linked to 3 behavioral indicators and no constructs. The prevailing use is to measure Dialogue summarization, and papers also use it to measure Text summarization and, in a smaller framing, Abstractive summarization. All 3 linked behavioral indicators are summarization-related.

**Space of uses.** No other measurement instrument is linked to it. Papers most often position it as an evaluation benchmark, including zero-shot generative evaluation, decoding-stage experiments, assessment of efficient inference methods, and evaluation after coreset selection or alignment; some papers instead rebuild it for fine-tuning an event summary module, use it as context data for controlled response generation and grammar co-occurrence analysis, or use it for summary-to-dialogue generation. When papers name companion datasets, examples include CNN/DM, DailyDialog, Wizard of Wikipedia, E-Dialogue, and BeaverTails.

## Sources

**DialogSum** (6 papers: [STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf), [Grammar Control in Dialogue Response Generation for Language Learning Chatbots](https://aclanthology.org/2025.naacl-long.495.pdf), [Hello Again! LLM-powered Personalized Agent for Long-term Dialogue](https://aclanthology.org/2025.naacl-long.272.pdf), [Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](https://aclanthology.org/2025.acl-long.210.pdf), [FLRC: Fine-grained Low-Rank Compressor for Efficient LLM Inference](https://aclanthology.org/2025.emnlp-main.755.pdf), [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf))
> A dialogue summarization dataset used to evaluate fine-tuning performance after coreset selection.

**Dialogsum** (1 paper: [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf))
> A benchmark dataset used for evaluating dialogue summarization performance.

## Relationships

### → DialogSum
- **Dialogue summarization** (behavioral indicator): *measured_by*, 5 papers
  > DialogSum is a large-scale dialogue summarization dataset, consisting of 13,460 dialogues with corresponding manually labeled summaries and topics. (Appendix B.1)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)
  - [STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf)
  - [Data Whisperer: Efficient Data Selection for Task-Specific LLM Fine-Tuning via Few-Shot In-Context Learning](https://aclanthology.org/2025.acl-long.1135.pdf)
- **Text summarization** (behavioral indicator): *measured_by*, 3 papers
  > For the decoding stage evaluation, we conduct experiments on two summarization benchmarks: DialogSum (Chen et al., 2021) and CNN/DM (Hermann et al., 2015) (Section 4.1).
  - [FLRC: Fine-grained Low-Rank Compressor for Efficient LLM Inference](https://aclanthology.org/2025.emnlp-main.755.pdf)
  - [Efficient Compositional Multi-tasking for On-device Large Language Models](https://aclanthology.org/2025.emnlp-main.1429.pdf)
  - [Speculative Streaming: Efficient and Scalable Speculative Decoding with Multi-Stream Attention](https://aclanthology.org/2025.emnlp-main.986.pdf)
- **Abstractive summarization** (behavioral indicator): *measured_by*, 1 paper
  > Our experiments are mainly conducted using the following two datasets of abstractive summarization: ... • DialogSum (Chen et al., 2021) is a dialogue summarization dataset of 13,460 dialogues with manually labeled summaries and topics.
  - [Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b054fadf1ccd80b37d465f6082629934-Paper-Conference.pdf)
