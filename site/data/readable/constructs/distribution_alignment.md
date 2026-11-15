# Distribution alignment
**Type:** Construct  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the definitions, the common core is distributional matching. One usage defines it as the degree to which selected training data matches representative examples from a target task so the model can learn the target distribution efficiently, while another uses the same term for a student model's ability to replicate a teacher's output probability distribution across tokens and contexts. The shared idea is alignment between distributions, but the papers differ on what is being aligned, training data to task examples versus student outputs to teacher outputs.

**Space of facets.** Rather than introducing named subtypes, the papers use the term at two levels. One line treats it as dataset-level alignment, where selected data should match representative examples from the target task, and another treats it as fine-grained, token-wise alignment, with dynamic emphasis of divergence or mixing for each token to better capture a teacher distribution. One paper also contrasts distribution alignment with calibration instead of treating them as the same construct.

**Space of measurement.** Papers do not link it to any measurement instrument or behavioral indicator. Still, they describe concrete operationalizations: one paper says it uses optimal transport to measure the discrepancy between the distribution assigned to candidate data and the target distribution, encouraging alignment between them, and another describes dynamic, per-token divergence control and per-token mixing to enable precise, fine-grained alignment with a teacher distribution. These operationalizations follow the same split as the definitions, candidate-data versus target-distribution matching in one case and token-level student-teacher distribution matching in the other.

**Links.** It is linked to one construct, Calibration, and that link is reported as related. One paper distinguishes the two by saying that its distribution alignment setting compares probabilities over the entire label set, whereas calibration compares only the predicted label probability to the ground truth.

## Sources

**Distribution alignment** (2 papers: [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf), [ToDi: Token-wise Distillation via Fine-Grained Divergence Control](https://aclanthology.org/2025.emnlp-main.409.pdf))
> The degree to which the distribution of selected training data matches the distribution of representative examples from a target task, enabling a model to learn the target distribution efficiently.

## Relationships

### Associated with
- **Calibration** (construct), 1 paper
  > Our proposed distribution alignment setting differs from calibration in that it compares the probabilities over the entire label set whereas calibration only compares the predicted label probability to the ground truth. (Section 2.3)
  - [Large Language Models Do Multi-Label Classification Differently](https://aclanthology.org/2025.emnlp-main.126.pdf)
