# XLSum
**Type:** Measurement instrument  
**Supporting papers:** 11  
**Also known as:** XLSUM, XL-Sum  

## State of the Field

**What it is.** Across the surveyed work, XLSum is most commonly described as a large-scale multilingual summarization dataset or benchmark, usually for abstractive summarization and sometimes explicitly for news or cross-lingual summarization. Most descriptions say it covers 44 languages, though one paper describes 45 languages; papers also characterize it as created from BBC articles, as comprising professionally annotated article-summary pairs, and as evaluating generation through a one-sentence summary of a context or article. A smaller line of work uses only the English subset or portion, and one paper describes that subset as the largest publicly available summarization dataset, with 307,000 training samples and 11,500 test samples.

**What it is claimed to measure.** Papers use XLSum to measure 3 behavioral indicators and no constructs. The prevailing use is for Text summarization, with additional use for Abstractive summarization and, less often, News summarization. All recorded measurement claims stay within summarization tasks.

**Space of uses.** No measurement instrument is linked to it. Papers commonly place it in multilingual or generation benchmark suites, and one study selects the text summarization task with XLSum as the reference task for evaluating multilingual performance. Usage varies from fine-tuning and evaluation on the English subset, to work on 6 languages with GPT-4 as a judge, to random sampling from the test set; some papers also mention it alongside XSum for transfer setups or alongside XNLI in mixed evaluations.

## Sources

**XLSum** (4 papers: [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf), [Improving Cross Lingual Transfer by Pretraining with Active Forgetting](https://aclanthology.org/2025.emnlp-main.120.pdf), [How do Large Language Models Handle Multilingualism?](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bd359b32ab8b2a6bbafa1ed2856cf40-Paper-Conference.pdf), [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf))
> A summarization dataset used to evaluate text summarization from projected embeddings.

**XLSUM** (3 papers: [Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf))
> A large, publicly available multilingual dataset for news summarization, used in this work for its English subset to fine-tune and evaluate Llama models.

**XL-Sum** (3 papers: [Drop-Upcycling: Training Sparse Mixture of Experts with Partial Re-initialization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d24b7366d714b09a977946ef0d9bf3ad-Paper-Conference.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf))
> Cross-lingual summarization benchmark evaluating the model's ability to condense text.

## Relationships

### → XLSum
- **Text summarization** (behavioral indicator): *measured_by*, 5 papers
  > We select the text summarization task with the XLSum (Hasan et al., 2021) dataset as the reference task to evaluate multilingual performance as it requires the model to comprehend the input text and generate a coherent fragment. (Section 2.3)
  - [How do Large Language Models Handle Multilingualism?](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bd359b32ab8b2a6bbafa1ed2856cf40-Paper-Conference.pdf)
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
  - [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf)
  - [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf)
- **Abstractive summarization** (behavioral indicator): *measured_by*, 2 papers
  > summarization using XSum [42] and XLSum [19] (Introduction).
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [CC-Tuning: A Cross-Lingual Connection Mechanism for Improving Joint Multilingual Supervised Fine-Tuning](https://aclanthology.org/2025.acl-long.933.pdf)
- **News summarization** (behavioral indicator): *measured_by*, 1 paper
  > We utilize the English summarization subset of the XLSUM dataset (Hasan et al., 2021)
  - [Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)
