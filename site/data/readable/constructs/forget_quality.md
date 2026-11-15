# Forget quality
**Type:** Construct  
**Supporting papers:** 2  

## State of the Field

The degree to which an unlearning method successfully removes the influence of specified data from a model, often measured by comparing the unlearned model's outputs to a model never trained on the data.

## Sources

**Forget quality** (1 paper: [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf))
> The degree to which an unlearning method successfully removes the influence of specified data from a model, often measured by comparing the unlearned model's outputs to a model never trained on the data.

## Relationships

### Forget quality →
- **TOFU** (measurement instrument): *measured_by*, 2 papers
  > To assess forget quality and model utility, we mainly use two metrics proposed alongside the TOFU dataset, Forget Quality (FQ) and Model Utility (MU) (Maini et al., 2024a). (Section 4.3)
  - [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf)
  - [Balancing Forget Quality and Model Utility: A Reverse KL-Divergence Knowledge Distillation Approach for Better Unlearning in LLMs](https://aclanthology.org/2025.naacl-long.60.pdf)
- **Utility preservation** (construct): *correlates*, 2 papers
  > Through the evaluation of four baseline VLM unlearning algorithms within FIUBENCH, we find that all methods remain limited in their unlearning performance, with significant trade-offs between model utility and forget quality.
  - [Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/dafb7f4ced9ac559e077fc611d6e96e5-Paper-Conference.pdf)
  - [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf)
- **Membership inference attack** (measurement instrument): *measured_by*, 1 paper
  > To determine whether private information still exists in VLMs after unlearning more accurately, we proposed to use MIAs for evaluation. (Section 2.5.3)
  - [Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/dafb7f4ced9ac559e077fc611d6e96e5-Paper-Conference.pdf)
