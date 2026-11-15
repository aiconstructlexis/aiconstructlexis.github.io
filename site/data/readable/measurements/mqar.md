# MQAR
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** Multi-query associative recall  

## State of the Field

**What it is.** Across the papers, MQAR is most commonly treated as a benchmark for associative recall, and one paper further describes it as a synthetic diagnostic task. Definitions describe sequences or contexts with multiple query tokens, where the model must retrieve and output the value associated with each queried item from the surrounding context; some descriptions add multiple pairs and distractors, and one paper notes that this can require multiple associative recalls in a single forward pass at varying sequence positions.

**What it is claimed to measure.** Papers link MQAR to one construct, Associative recall ability, and one behavioral indicator, Key-value retrieval. The prevailing usage is concentrated rather than spread across many targets: papers say a model's recall capability is assessed using the MQAR task, and that the task's goal is to correctly predict the associated value at the query positions while non-query positions are ignored.

**Space of uses.** The papers do not link MQAR to other measurement instruments. Instead, they position it directly as an evaluation benchmark for associative recall capabilities and retrieval from context; one paper presents analytical solutions to the MQAR task using the Mamba architecture, and another describes training a small-parameter model from scratch on a specific dataset for the task.

## Sources

**MQAR** (3 papers: [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf), [Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ab/huang25ab.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf))
> The Multi-Query Associative Recall task, a benchmark designed to assess a model's ability to retrieve values associated with keys from a context.

**Multi-query associative recall** (1 paper: [Zoology: Measuring and Improving Recall in Efficient Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/448fc91f669c15d10364ee01d512cc10-Paper-Conference.pdf))
> The observable task of identifying multiple query tokens within a sequence and, for each, recalling and outputting the value token that followed its first appearance as a key.

## Relationships

### → MQAR
- **Key-value retrieval** (behavioral indicator): *measured_by*, 2 papers
  > Multi-Query Associative Recall (MQAR) Task. (Figure 1)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
  - [Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ab/huang25ab.pdf)
- **Associative recall ability** (construct): *measured_by*, 1 paper
  > The model’s recall capability is assessed using the MQAR Task (See Appendix D.7), as described in Arora et al. (2024a). (Figure 1)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
