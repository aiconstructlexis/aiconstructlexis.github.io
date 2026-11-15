# Biography
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** Biography dataset  

## State of the Field

**What it is.** Across papers, Biography is most commonly described as a fact-seeking long-form generation dataset centered on biographical information, used to evaluate factual consistency in narrative generation. Some authors instead describe it as a test set for biography generation used for out-of-domain evaluation of factuality. The descriptions differ on format details: one gives 181 prompts, while another says it uses a subset as the test set with 183 questions about biography generation.

**What it is claimed to measure.** Papers link Biography to 2 constructs and 1 behavioral indicator. The linked behavioral indicator is biography generation, and papers also use Biography to measure factuality, including by reporting FactScore on the out-of-domain Biography dataset. A smaller line of work uses a synthetic Biography dataset to measure knowledge forgetting.

**Space of uses.** It is linked to 1 other measurement instrument, FActScore, which papers use alongside Biography for fact-verification. In that pairing, Biography is positioned as the out-of-domain test set and FActScore as the corresponding evaluation strategy; elsewhere papers simply refer to evaluating a biography-generation task with Biography.

## Sources

**Biography** (2 papers: [Improving Factuality with Explicit Working Memory](https://aclanthology.org/2025.acl-long.548.pdf), [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf))
> Fact-seeking long-form generation dataset with 181 prompts centered on biographical information, used to evaluate factual consistency in narrative generation.

**Biography dataset** (1 paper: [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf))
> A test set containing questions about generating biographies, used for out-of-domain evaluation of factuality.

## Relationships

### → Biography
- **Biography generation** (behavioral indicator): *measured_by*, 2 papers
  > "Fact verification. We evaluate a biography-generation task (Min et al., 2023)"
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Factuality** (construct): *measured_by*, 1 paper
  > its FactScore on the out-of-domain Biography dataset is also improved from 30.29% to 39.39% (Section 1).
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Knowledge forgetting** (construct): *measured_by*, 1 paper
  > “we constructed a synthetic dataset, the Biography dataset, and designed controlled experiments to investigate the underlying causes of spurious forgetting”
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)

### Associated with
- **FActScore** (measurement instrument), 1 paper
  > ANAH and Biography represent the in-domain and out-of-domain test sets, respectively. ANAH-v2 and FactScore represent the corresponding evaluation strategies (Table 1).
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
