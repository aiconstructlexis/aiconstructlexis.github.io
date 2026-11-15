# Internal consistency
**Type:** Construct  
**Supporting papers:** 5  

## State of the Field

**Space of definitions.** Papers use the term in two different ways. One framing, stated in Calibrating Reasoning in Language Models with Internal Consistency, defines it as agreement between latent predictions decoded from intermediate layers and the final prediction, reflecting the stability of the model's internal reasoning process and serving as a measure of confidence. Another, in Compositional Causal Reasoning Evaluation in Language Models, defines it as giving equivalent answers to theoretically equivalent queries, regardless of correctness relative to ground truth, so the split is between layer-wise internal agreement and concordance across equivalent outputs.

**Space of facets.** The main contrast papers draw is with external validity. One paper treats compositional consistency as involving both agreement with ground truth, labeled external validity, and concordance among the model's own responses, labeled internal consistency. Across these uses, the same name covers both agreement among internal layer-wise predictions and equivalence among responses to theoretically equivalent queries.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. Instead, papers operationalize it directly by examining the agreement of latent predictions decoded from intermediate layers with the final prediction, or by checking whether theoretically equivalent quantities are inferred to be equivalent up to some error δ. These operationalizations follow the two definitions rather than converging on a single named instrument.

**Links.** Reported links are mostly associative. One paper claims a causal relationship from internal consistency to reasoning, reporting that up-weighting reasoning paths with high internal consistency boosted reasoning performance. Other papers relate calibration to internal consistency, describe it as a useful indicator of output correctness, relate internal consistency to robustness by linking layer consistency to robustness, and relate compositional consistency to internal consistency by treating the latter as concordance among the model's responses.

## Sources

**Internal consistency** (1 paper: [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf))
> The degree of agreement between latent predictions decoded from intermediate layers and the final prediction, reflecting the stability of the model's internal reasoning process.

## Relationships

### Internal consistency →
- **Reasoning** (construct): *causes*, 1 paper
  > we propose a new approach to calibrate reasoning by up-weighting reasoning paths with high internal consistency, resulting in a significant boost in reasoning performance. (Abstract)
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)

### Associated with
- **Calibration** (construct), 1 paper
  > This measure offers a straightforward method to gauge the level of internal consistency, serving as a useful indicator of the output’s correctness (i.e., calibration), without requiring additional training. (Section 3.2)
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
- **Robustness** (construct), 1 paper
  > By linking layer consistency to robustness, CROW provides practical and effective protection against backdoor threats. (Section 1)
  - [CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/min25b/min25b.pdf)
- **Compositional consistency** (construct), 1 paper
  > We measure compositional consistency with respect to ground truth (external validity) and concordance among the LM’s responses (internal consistency) (Fig. 1). (Section 1)
  - [Compositional Causal Reasoning Evaluation in Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/maasch25a/maasch25a.pdf)
