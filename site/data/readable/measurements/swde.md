# SWDE
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across the papers, SWDE is described either as an information extraction benchmark used as a recall-intensive evaluation of long-sequence retrieval, or as an information-retrieval benchmark designed to evaluate retrieval from in-context passages scraped from HTML/PDFs. Papers therefore use overlapping but not identical labels for it.

**What it is claimed to measure.** Papers use SWDE to measure 2 behavioral indicators and 1 construct. The behavioral-indicator links are to Information extraction and Synthetic recall, and the construct link is to Associative recall ability; one paper reports that "Recall" represents the average performance across FDA, SWDE, and SQuAD.

**Space of uses.** Papers do not link SWDE to any other measurement instrument. Instead, they present it within broader evaluation setups: one paper places it among "six recall-intensive tasks," another assesses retrieval on FDA and SWDE, and another includes it in a "Recall" average with FDA and SQuAD.

## Sources

**SWDE** (2 papers: [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf))
> An information extraction benchmark used as a recall-intensive evaluation of long-sequence retrieval.

## Relationships

### → SWDE
- **Synthetic recall** (behavioral indicator): *measured_by*, 1 paper
  > Specifically, we assess information retrieval on FDA [93] and SWDE [49], which are designed to evaluate retrieval from in-context passages scraped from HTML/PDFs. (Section 4.1.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Information extraction** (behavioral indicator): *measured_by*, 1 paper
  > we consider the following six recall-intensive tasks: information extraction tasks like FDA and SWDE (Arora et al., 2024a; 2023b; Wu et al., 2021; Deng et al., 2022) (Section 5.2)
  - [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf)
- **Associative recall ability** (construct): *measured_by*, 1 paper
  > “Recall” represents the average performance across FDA, SWDE, and SQuAD. (Table 7)
  - [Scaling up the State Size of RNN LLMs for Long-Context Scenarios](https://aclanthology.org/2025.acl-long.564.pdf)
