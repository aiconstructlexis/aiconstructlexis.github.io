# Alignment tax
**Type:** Construct  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the surveyed work, the explicit definition treats alignment tax as degradation in a model's general capabilities or performance on other tasks after fine-tuning to align with human preferences or safety objectives. A narrower usage also appears in which harms to reasoning ability under preference optimization are referred to as alignment tax, so the main variation is between a broad other-task capability loss and a specific loss in reasoning.

**Space of facets.** Formal systematization is sparse. Papers do not divide the construct into facets or subtypes; instead, they use it alongside neighboring labels and outcomes, with one paper saying training can lead to "knowledge forgetting" or "alignment tax," eroding a pre-trained model's encoded knowledge, and another tying the term to harm in reasoning ability.

**Space of measurement.** Operationalization is limited. Papers link alignment tax to one measurement instrument, the Open LLM Leaderboard, a benchmark used to evaluate whether methods reduce alignment tax across leaderboard tasks, and no behavioral indicators are linked. Separately, one paper says, "To evaluate alignment tax, we measure how far our RLHF policy has drifted from its SFT initialization," so the observed measurement space is benchmark task performance after alignment and analysis of drift from the SFT starting point.

**Links.** Papers link alignment tax to two constructs. One paper claims a causal relationship from Generation diversity to Alignment tax, with evidence framed as suppressing alternative plausible outputs during training leading to "knowledge forgetting" or "alignment tax." Another paper relates Alignment tax to Reasoning, stating that preference optimization methods that align models with human values often harm reasoning ability and refer to this harm as alignment tax.

## Sources

**Alignment tax** (1 paper: [Asynchronous RLHF: Faster and More Efficient Off-Policy RL for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b99315234cc95e6ef281f9155b68832-Paper-Conference.pdf))
> The degradation of a model's general capabilities or performance on other tasks as a result of being fine-tuned to align with specific human preferences or safety objectives.

## Relationships

### Alignment tax →
- **Open LLM Leaderboard** (measurement instrument): *measured_by*, 1 paper
  > In this section, we show that GEM also helps mitigate forgetting and reduce alignment tax. We evaluate the models across six tasks: ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande, as listed on the OpenLLM leaderboard. (Section 6.2)
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)

### → Alignment tax
- **Generation diversity** (construct): *causes*, 1 paper
  > by suppressing alternative plausible outputs during training, CE can lead to “knowledge forgetting” or “alignment tax”, eroding the pre-trained model’s encoded knowledge (Section 1)
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)

### Associated with
- **Reasoning** (construct), 1 paper
  > Recent studies (Ouyang et al., 2022; Lin et al., 2023) have shown that using preference optimization methods to align LLMs with human values often harms their reasoning ability, referred to as the alignment tax.
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
