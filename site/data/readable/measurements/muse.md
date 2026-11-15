# MUSE
**Type:** Measurement instrument  
**Supporting papers:** 11  

## State of the Field

**What it is.** Across the surveyed work, MUSE is most commonly described as a comprehensive machine unlearning evaluation benchmark for language models, framed as Machine Unlearning Six-Way Evaluation and said to evaluate unlearned models across six desiderata or facets. Definitions place it in news and book materials, with verbatim-text and question-answer knowledge sets, though some papers narrow the description to copyrighted-information removal and emphasize two scenarios, Books from the Harry Potter series and News from BBC News. A smaller description focuses only on the BBC News portion, where passages are split into Forget and Retain sets to evaluate knowledge removal and utility preservation through question answering.

**What it is claimed to measure.** In the recorded relationships, MUSE is linked to 3 constructs and 1 behavioral indicator, so papers use it across several measurement targets rather than centering it on a single construct. The explicit links are to Knowledge memorization, Utility preservation, and Verbatim memorization, plus the behavioral indicator Privacy leakage, and one definition also frames MUSE as evaluating six desirable properties of unlearning more broadly.

**Space of uses.** Papers position MUSE as an evaluation setting for unlearning methods, alternately calling it a comprehensive benchmark and, in one usage, a dataset on which a method is evaluated. It appears alongside WMDP in one experimental setup. It is linked to 1 other instrument, TOFU, and one paper relates the two by contrasting TOFU's synthetic question-answer evaluation with MUSE's real-world unlearning challenges.

**Concerns raised.** One paper uses MUSE to highlight a drawback in current methods: applying unlearning to larger corpora leads to a decline in general language usefulness.

## Sources

**MUSE** (4 papers: [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf), [Towards LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective and Beyond](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25e/fan25e.pdf), [SEPS: A Separability Measure for Robust Unlearning in LLMs](https://aclanthology.org/2025.emnlp-main.283.pdf), [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.444.pdf))
> Machine Unlearning Six-Way Evaluation, a benchmark that evaluates unlearned language models across six desiderata using news and book corpora with verbatim-text and question-answer knowledge sets.

## Relationships

### → MUSE
- **Verbatim memorization** (construct): *measured_by*, 1 paper
  > We address this issue by proposing MUSE, a comprehensive machine unlearning evaluation benchmark that enumerates six diverse desirable properties for unlearned models: (1) no verbatim memorization, (2) no knowledge memorization, (3) no privacy leakage, (4) utility preservation on data not intended for removal, (5) scalability with respect to the size of removal requests, and (6) sustainability over sequential unlearning requests. (Section 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Knowledge memorization** (construct): *measured_by*, 1 paper
  > We address this issue by proposing MUSE, a comprehensive machine unlearning evaluation benchmark that enumerates six diverse desirable properties for unlearned models: (1) no verbatim memorization, (2) no knowledge memorization, (3) no privacy leakage, (4) utility preservation on data not intended for removal, (5) scalability with respect to the size of removal requests, and (6) sustainability over sequential unlearning requests. (Section 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Privacy leakage** (behavioral indicator): *measured_by*, 1 paper
  > We address this issue by proposing MUSE, a comprehensive machine unlearning evaluation benchmark that enumerates six diverse desirable properties for unlearned models: (1) no verbatim memorization, (2) no knowledge memorization, (3) no privacy leakage, (4) utility preservation on data not intended for removal, (5) scalability with respect to the size of removal requests, and (6) sustainability over sequential unlearning requests. (Section 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Utility preservation** (construct): *measured_by*, 1 paper
  > We address this issue by proposing MUSE, a comprehensive machine unlearning evaluation benchmark that enumerates six diverse desirable properties for unlearned models: (1) no verbatim memorization, (2) no knowledge memorization, (3) no privacy leakage, (4) utility preservation on data not intended for removal, (5) scalability with respect to the size of removal requests, and (6) sustainability over sequential unlearning requests. (Section 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)

### Associated with
- **TOFU** (measurement instrument), 1 paper
  > Unlike the previous benchmark TOFU (Maini et al., 2024), which evaluates unlearning on synthetic Q&A datasets, MUSE tackles real-world unlearning challenges (Table 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
