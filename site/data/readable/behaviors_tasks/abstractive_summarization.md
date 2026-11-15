# Abstractive summarization
**Type:** Behavioral indicator  
**Supporting papers:** 19  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is a generation task: producing a concise summary of a source document that captures its main or salient ideas, often through paraphrase or other novel phrasing rather than extracting exact spans. Many definitions add coherence, fluency, or informativeness, and some, including Filipino-focused work, also require faithfulness and avoiding hallucination. A smaller line of work describes the setting as models responding to queries given context, while another contrasts it with extractive summarization by describing an abstractive revision as more concise and natural-sounding.

**Variants.** Papers study this behavior in several settings, including news summarization, dialogue summarization, multilingual summarization, Filipino summarization, long-document summarization, and user-generated posts paired with concise summaries. One paper describes a news variant that requires single-sentence summaries from BBC articles, and another treats document-based question-answering, meeting summarization, and clinical report generation as abstractive summarization tasks. Another paper positions it alongside extractive summarization, where an extractive summary is revised into an abstractive one.

**Space of elicitation and scores.** Papers measure it with six instruments, most often XSum. CNN/DailyMail and XLSum are also recurring, with DialogSum and Plutus-ben appearing as additional instruments, and one other instrument. These instruments are described as datasets or benchmarks, covering news article summaries, multilingual article-summary pairs, dialogue summaries, and broader task suites.

**What it is taken as evidence of.** Papers do not explicitly treat this behavior as evidence of any construct. The links beyond measurement instead relate it to other behaviors: one paper relates it to hallucination by defining hallucinations in this setting as grounding errors where the output contains information not supported by the context, and another relates it to extractive summarization by contrasting an extractive summary with a more concise and natural-sounding abstractive revision.

## Sources

**Abstractive summarization** (12 papers: [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf), [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf), [Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b054fadf1ccd80b37d465f6082629934-Paper-Conference.pdf), [BOND: Aligning LLMs with Best-of-N Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/947f37882a394140f7add476bb99d1d3-Paper-Conference.pdf), [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf), [Batayan: A Filipino NLP benchmark for evaluating Large Language Models](https://aclanthology.org/2025.acl-long.1509.pdf), [Beyond N-Grams: Rethinking Evaluation Metrics and Strategies for Multilingual Abstractive Summarization](https://aclanthology.org/2025.acl-long.932.pdf), [CC-Tuning: A Cross-Lingual Connection Mechanism for Improving Joint Multilingual Supervised Fine-Tuning](https://aclanthology.org/2025.acl-long.933.pdf), [Faster Speculative Decoding via Effective Draft Decoder with Pruned Candidate Tree](https://aclanthology.org/2025.acl-long.486.pdf), [SARA: Salience-Aware Reinforced Adaptive Decoding for Large Language Models in Abstractive Summarization](https://aclanthology.org/2025.acl-long.1236.pdf), [Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf), [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf))
> The task of generating a concise and coherent summary that captures the main ideas of a source document, potentially using novel phrasing.

## Relationships

### Abstractive summarization →
- **XSum** (measurement instrument): *measured_by*, 6 papers
  > We start by evaluating GKD on an abstractive summarization task of generating a summary that captures salient ideas of the input document. To do so, we use the XSum dataset (Narayan et al., 2018) (Section 4.1).
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [BOND: Aligning LLMs with Best-of-N Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/947f37882a394140f7add476bb99d1d3-Paper-Conference.pdf)
  - [Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf)
  - [UNCERTAINTY-LINE: Length-Invariant Estimation of Uncertainty for Large Language Models](https://aclanthology.org/2025.emnlp-main.400.pdf)
- **XLSum** (measurement instrument): *measured_by*, 2 papers
  > summarization using XSum [42] and XLSum [19] (Introduction).
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [CC-Tuning: A Cross-Lingual Connection Mechanism for Improving Joint Multilingual Supervised Fine-Tuning](https://aclanthology.org/2025.acl-long.933.pdf)
- **CNN/DailyMail** (measurement instrument): *measured_by*, 2 papers
  > To comprehensively evaluate our method, we selected four datasets from different tasks: ...CNN/DM (See et al., 2017) for abstractive summarization... (Section 4.1)
  - [Faster Speculative Decoding via Effective Draft Decoder with Pruned Candidate Tree](https://aclanthology.org/2025.acl-long.486.pdf)
  - [Language Models Can be Efficiently Steered via Minimal Embedding Layer Transformations](https://aclanthology.org/2025.emnlp-main.1170.pdf)
- **DialogSum** (measurement instrument): *measured_by*, 1 paper
  > Our experiments are mainly conducted using the following two datasets of abstractive summarization: ... • DialogSum (Chen et al., 2021) is a dialogue summarization dataset of 13,460 dialogues with manually labeled summaries and topics.
  - [Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b054fadf1ccd80b37d465f6082629934-Paper-Conference.pdf)
- **Reddit TL;DR** (measurement instrument): *measured_by*, 1 paper
  > “It contains user-generated posts paired with concise summaries, providing a challenging benchmark for abstractive summarization tasks.”
  - [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf)
- **Plutus-ben** (measurement instrument): *measured_by*, 1 paper
  > “Plutus-ben addresses six core tasks: numeric/textual named entity recognition, question answering, extractive summarization, abstractive summarization, and topic classification.”
  - [Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance](https://aclanthology.org/2025.emnlp-main.1535.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > Hallucinations in the abstractive summarization setting are grounding errors: errors where the output contains some information that is not supported by the context. (Section 2.1)
  - [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf)
- **Extractive summarization** (behavioral indicator), 1 paper
  > in the second stage of the pipeline (Figure 1’s last panel), we prompt the LLM again to revise the extractive summary in order to obtain a more concise and natural-sounding data description, which is known as abstractive summarization (Gupta & Gupta, 2019). (Section 3.1)
  - [MuHBoost: Multi-Label Boosting For Practical Longitudinal Human Behavior Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca2963d1cfb25e93362e86fb427a9524-Paper-Conference.pdf)
