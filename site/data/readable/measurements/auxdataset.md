# AUXDATASET
**Type:** Measurement instrument  
**Supporting papers:** 2  

## State of the Field

A 10-terabyte web-text corpus used as a proxy for proprietary training data when searching for exact substring matches in model outputs.

## Sources

**AUXDATASET** (1 paper: [Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf))
> A 10-terabyte web-text corpus used as a proxy for proprietary training data when searching for exact substring matches in model outputs.

## Relationships

### → AUXDATASET
- **Memorization** (construct): *measured_by*, 1 paper
  > We thus call a subsequence of a generation memorized if (as in Deﬁnition 1) a 50-token-length subsequence exactly appears in AUXDATASET. (Section 3)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
- **Training data regurgitation** (behavioral indicator): *measured_by*, 1 paper
  > To verify the success of our attack, we construct a 9 terabyte dataset (AUXDATASET), combining many sources of Internet text, to serve as a proxy for the unknown training datasets for these production models. (Section 1)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
