# CSCD-NS
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** The definitions treat CSCD-NS as a Chinese Spelling Correction benchmark dataset, described as high-quality and as containing character errors that primarily stem from pinyin input methods, with many homophonic and word-level errors. In Enhancing Character-Level Understanding in LLMs through Token Internal Structure Learning, it is grouped with LEMON as one of two newer CSC benchmarks, in contrast to earlier datasets such as SIGHAN.

**What it is claimed to measure.** Papers use it in a focused way rather than across many targets: it is linked to 1 behavioral indicator, Chinese spelling correction, and to no constructs. One paper explicitly uses CSCD-NS as one of two CSC benchmarks for evaluating Chinese spelling correction.

**Space of uses.** Usage is shown mainly as a paired benchmark: papers use it alongside LEMON, and one study says the pair was selected to address limitations identified in previous datasets like SIGHAN. No other measurement instruments are linked to it.

## Sources

**CSCD-NS** (1 paper: [Enhancing Character-Level Understanding in LLMs through Token Internal Structure Learning](https://aclanthology.org/2025.acl-long.194.pdf))
> A high-quality Chinese Spelling Correction (CSC) benchmark dataset where character errors primarily originate from pinyin input methods, featuring many homophonic and word-level errors.

## Relationships

### → CSCD-NS
- **Chinese spelling correction** (behavioral indicator): *measured_by*, 1 paper
  > Following recent works, we use two CSC benchmarks, LEMON (Wu et al., 2023) and CSCD-NS (Hu et al., 2024). (Section 3.1)
  - [Evolving Chinese Spelling Correction with Corrector-Verifier Collaboration](https://aclanthology.org/2025.emnlp-main.1477.pdf)
