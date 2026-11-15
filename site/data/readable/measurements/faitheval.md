# FaithEval
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Papers describe FaithEval as an evaluation benchmark. One framing presents it as designed to measure and reduce model hallucination across different challenging scenarios, while another presents it as a novel and comprehensive benchmark for evaluating the faithfulness of LLMs in contextual scenarios. One paper further describes it as comprising 4.9K high-quality problems built through a four-stage context construction and validation framework.

**What it is claimed to measure.** Papers use FaithEval to measure 1 construct and 1 behavioral indicator. The construct link is Context faithfulness, with papers describing the benchmark as tailored to evaluate the faithfulness of LLMs in contextual scenarios. It is also linked to Hallucination, in work that cites an ablation study on FaithEval as showing reduced hallucinations.

**Space of uses.** In use, papers relate FaithEval to 2 other instruments, Human evaluation and LLM-as-a-judge. One description says its problems are validated through LLM-based auto-evaluation and human validation, and another says a separate LLM judge is used to verify whether a new answer is valid given the context. It also appears as an ablation benchmark in work assessing robustness to noisy contexts while reporting reduced hallucinations.

## Sources

**FaithEval** (1 paper: [Efficient OpAmp Adaptation for Zoom Attention to Golden Contexts](https://aclanthology.org/2025.acl-long.653.pdf))
> An evaluation benchmark designed to measure and reduce model hallucination across different challenging scenarios.

## Relationships

### → FaithEval
- **Context faithfulness** (construct): *measured_by*, 1 paper
  > “we introduce FaithEval, a novel and comprehensive benchmark tailored to evaluate the faithfulness of LLMs in contextual scenarios”
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *measured_by*, 1 paper
  > As shown in Table 5, the ablation study on FaithEval (Ming et al., 2024) demonstrates that OpAmp not only enhances robustness to noisy contexts but also reduces hallucinations as a valuable secondary benefit.
  - [Efficient OpAmp Adaptation for Zoom Attention to Golden Contexts](https://aclanthology.org/2025.acl-long.653.pdf)

### Associated with
- **Human evaluation** (measurement instrument), 1 paper
  > FaithEval comprises 4.9K high-quality problems in total, validated through a rigorous four-stage context construction and validation framework, employing both LLM-based auto-evaluation and human validation.
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument), 1 paper
  > “we validate the quality of the new context by using a separate LLM judge to verify whether the new answer is valid given the context”
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
