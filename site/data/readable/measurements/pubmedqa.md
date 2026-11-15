# PubMedQA
**Type:** Measurement instrument  
**Supporting papers:** 44  
**Also known as:** PubmedQA, Pubmedqa  

## State of the Field

**What it is.** Across papers, PubMedQA is most commonly described as a biomedical question-answering benchmark built from PubMed abstracts or articles, usually asking yes, no, or maybe questions grounded in a corresponding abstract. Some definitions say its QA pairs are formulated from PubMed articles, with questions derived from titles; several also describe corresponding contexts and sometimes long-form or free-form explanations or answers, while a smaller line of work treats it as a biomedical multiple-choice dataset or simply as a held-out evaluation benchmark. Papers mention multiple reused portions of the resource, including validation and test sets and the pqa_labeled split.

**What it is claimed to measure.** Papers link PubMedQA to 2 constructs and 3 behavioral indicators. The prevailing usage is to measure medical question answering, and smaller lines of work use it to measure knowledge-based question answering and natural language inference; on the construct side, papers also use it to measure contextual reasoning and medical knowledge. Overall, papers use it for several different targets rather than only one, although medical question answering is the most recurrent behavioral framing.

**Space of uses.** Papers commonly position PubMedQA as an evaluation benchmark, including held-out evaluation, cross-evaluation, validation and testing, and distribution-shift or out-of-domain checks. It often appears alongside other medical or biomedical benchmarks such as MedQA, MedMCQA, BioASQ, ChemProt, and USMLE, and some papers adapt it into retrieval-based QA by using its abstracts as a knowledge base or derive long-context samples from its contextual passages. The only linked instrument is MedHallu, which papers relate to PubMedQA because MedHallu is derived from question-answer pairs sourced from it.

**Concerns raised.** One paper says that while benchmarks such as PubMedQA may be useful for assessing clinical domain knowledge, they are not sufficient for evaluating models' practical capabilities in assisting healthcare professionals in real-world clinical settings.

## Sources

**PubmedQA** (9 papers: [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf), [AMOR: A Recipe for Building Adaptable Modular Knowledge Agents Through Process Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4595e77b045971a654edc5e3cd31989-Paper-Conference.pdf), [DPIC: Decoupling Prompt and Intrinsic Characteristics for LLM Generated Text Detection](https://proceedings.neurips.cc/paper_files/paper/2024/file/1d35af80e775e342f4cd3792e4405837-Paper-Conference.pdf), [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf), [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf), [MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf), [MedCalc-Bench: Evaluating Large Language Models for Medical Calculations](https://proceedings.neurips.cc/paper_files/paper/2024/file/99e81750f3fdfcaf9613db2dbf4bd623-Paper-Datasets_and_Benchmarks_Track.pdf), [MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3ac952d0264ef7a505393868a70a46b6-Paper-Datasets_and_Benchmarks_Track.pdf), [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf))
> A held-out question-answering benchmark used in the paper’s single-task finetuning comparisons.

**PubMedQA** (13 papers: [Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf), [DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/d4ce6738e84876aa79f13c8bc8b7c5eb-Paper-Conference.pdf), [Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf), [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/be3b0d51a2b86cb4ffe50f13480217e0-Paper-Conference.pdf), [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [Shh, don't say that! Domain Certification in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/27befed4547edcb4bdeacef9472cadee-Paper-Conference.pdf), [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.444.pdf), [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf), [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.575.pdf), [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf), [TrimLLM: Progressive Layer Dropping for Domain-Specific LLMs](https://aclanthology.org/2025.acl-long.33.pdf), [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf), [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143.pdf))
> A question answering dataset designed for biomedical research questions, where answers are yes/no/maybe and may require a long-form explanation.

**Pubmedqa** (1 paper: [Dynamic Uncertainty Ranking: Enhancing Retrieval-Augmented In-Context Learning for Long-Tail Knowledge in LLMs](https://aclanthology.org/2025.naacl-long.453.pdf))
> Biomedical multiple-choice question-answering dataset used to evaluate LLM performance on domain-specific long-tail knowledge in the medical field.

## Relationships

### → PubMedQA
- **Medical question answering** (behavioral indicator): *measured_by*, 4 papers
  > For the medical domain, we select the PubMedQA dataset [74], which includes 211.3K artificially generated QA training instances and 1K test instances (Section 4.4).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
  - [Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment](https://aclanthology.org/2025.emnlp-main.406.pdf)
  - [Shh, don't say that! Domain Certification in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/27befed4547edcb4bdeacef9472cadee-Paper-Conference.pdf)
- **Medical knowledge** (construct): *measured_by*, 1 paper
  > While these benchmarks may be useful for assessing the clinical domain knowledge of LLMs, they are not sufficient for evaluating the practical capabilities of models in assisting healthcare professionals in real-world clinical settings [37]. (Section 2)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Knowledge-based question answering** (behavioral indicator): *measured_by*, 1 paper
  > For knowledge-intensive reasoning, we use datasets that require deep domain understanding. ... PubMedQA (Jin et al., 2019) assesses biomedical reasoning from abstracts
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **Contextual reasoning** (construct): *measured_by*, 1 paper
  > we select the PubMedQA dataset and derive long-context QA samples to evaluate the effectiveness of HMT. Two metrics are employed: for long answers, we compute the PPL to assess the contextual reasoning of HMT (Section 5.1)
  - [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf)
- **Natural language inference** (behavioral indicator): *measured_by*, 1 paper
  > For yes/no QA, we select PubMedQA (Jin et al., 2019), an English natural language inference task related to medical research papers. (Section 4.2)
  - [AQuilt: Weaving Logic and Self-Inspection into Low-Cost, High-Relevance Data Synthesis for Specialist LLMs](https://aclanthology.org/2025.emnlp-main.293.pdf)

### Associated with
- **MedHallu** (measurement instrument), 1 paper
  > MedHallu comprises 10,000 high-quality question-answer pairs derived from the established PubMedQA dataset.
  - [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143.pdf)
