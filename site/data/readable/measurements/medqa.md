# MedQA
**Type:** Measurement instrument  
**Supporting papers:** 49  
**Also known as:** MedQA-USMLE, MedQA-US  

## State of the Field

**What it is.** Across the surveyed papers, MedQA is most commonly described as a medical multiple-choice question answering benchmark built from USMLE or other professional medical board exam questions. Definitions usually present it as evaluating medical knowledge and reasoning, with some papers specifying clinical vignettes, patient-profile style contextualized questions, or questions curated by medical examination experts from various question banks; one paper also notes that MedQA included questions from Medbullets. Papers also mention variants: MedQA-USMLE is described either as an NBME-sourced subset or simply as MedQA, and MedQA-US as a challenging USMLE-based version.

**What it is claimed to measure.** Papers link MedQA to 4 constructs and 5 behavioral indicators. The prevailing use is to measure Medical question answering, Multiple-choice question answering, Question answering, Medical knowledge, and Medical reasoning; other papers report four additional linked targets. Overall, the reported measurement claims stay centered on medical QA and knowledge or reasoning evaluation, rather than on one single target.

**Space of uses.** No measurement instrument is linked to it. In use, papers commonly evaluate MedQA alongside MedMCQA, PubMedQA, and MMLU-Med, and some place it within broader benchmark collections such as MIRAGE or the Open Medical LLM Leaderboard. Some studies also use its question bank as a source of few-shot USMLE examples, convert it into an interactive benchmark, or include it as part of a capabilities component.

**Concerns raised.** A recurring limitation in the papers is that benchmarks such as MedQA are described as assessing clinical domain knowledge or preliminary knowledge grasp through question answering, but not as sufficient for evaluating models' practical capabilities in real-world clinical settings. Another paper characterizes MedQA as more oriented toward reasoning than pure factual recall, which it says poses bigger challenges for both the retriever and the language model.

## Sources

**MedQA** (19 papers: [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf), [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.575.pdf), [Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.182.pdf), [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.584.pdf), [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.538.pdf), [Rationale-Guided Retrieval Augmented Generation for Medical Question Answering](https://aclanthology.org/2025.naacl-long.635.pdf), [AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset](https://aclanthology.org/2025.acl-long.96.pdf), [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf), [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf), [DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf), [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf), [MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf), [MedCalc-Bench: Evaluating Large Language Models for Medical Calculations](https://proceedings.neurips.cc/paper_files/paper/2024/file/99e81750f3fdfcaf9613db2dbf4bd623-Paper-Datasets_and_Benchmarks_Track.pdf), [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf), [MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3ac952d0264ef7a505393868a70a46b6-Paper-Datasets_and_Benchmarks_Track.pdf), [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf), [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf), [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf), [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf))
> A dataset containing US Medical Licensing Examination (USMLE) questions used to evaluate model knowledge and reasoning in the medical domain.

**MedQA-USMLE** (3 papers: [Pattern Recognition or Medical Knowledge? The Problem with Multiple-Choice Questions in Medicine](https://aclanthology.org/2025.acl-long.266.pdf), [Cost-efficient Knowledge-based Question Answering with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0aafec03d59db29a92fa683bd783374-Paper-Conference.pdf), [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf))
> A medical multiple-choice question benchmark sourced from the National Board of Medical Examiners, containing clinical vignettes and knowledge-based questions used to evaluate LLM performance on human medical licensing exam content.

**MedQA-US** (1 paper: [Query-driven Document-level Scientific Evidence Extraction from Biomedical Studies](https://aclanthology.org/2025.acl-long.1359.pdf))
> A challenging question answering dataset containing multiple-choice questions from the United States Medical Licensing Examination (USMLE).

## Relationships

### → MedQA
- **Medical question answering** (behavioral indicator): *measured_by*, 5 papers
  > After training on MedAlpaca for Medical (M) domain or MedAlpaca/Alpaca-GPT4 for Medical&General (M&G) domain, we test the models at round 60 on the evaluation datasets for Medical (M) domain, i.e., MedQA [10], and MedMCQA [22]. (Section 4.2)
  - [DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf)
  - [Rationale-Guided Retrieval Augmented Generation for Medical Question Answering](https://aclanthology.org/2025.naacl-long.635.pdf)
  - [RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning](https://aclanthology.org/2025.emnlp-main.1630.pdf)
  - [Split-Merge: Scalable and Memory-Efficient Merging of Expert LLMs](https://aclanthology.org/2025.emnlp-main.1533.pdf)
  - [A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making](https://aclanthology.org/2025.emnlp-main.1699.pdf)
- **Medical knowledge** (construct): *measured_by*, 2 papers
  > While these benchmarks may be useful for assessing the clinical domain knowledge of LLMs, they are not sufficient for evaluating the practical capabilities of models in assisting healthcare professionals in real-world clinical settings [37]. (Section 2)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 2 papers
  > We also use MedQA, a collection of multiple-choice questions from the professional medical board exams (Jin et al., 2020).
  - [Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf)
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > ...while MedQA-USMLE [34] acts as a domain-specific QA benchmark. (Section 4.1)
  - [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
  - [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf)
- **Medical reasoning** (construct): *measured_by*, 1 paper
  > “MedQA was constructed from USMLE questions to evaluate the medical reasoning and knowledge of LLMs in a multiple-choice format.”
  - [Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > both MMLU and MedQA are more oriented toward reasoning rather than pure factual recall, which poses bigger challenges for both the retriever and the LM. (Section 4.2)
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Grounded response generation** (behavioral indicator): *measured_by*, 1 paper
  > Figure 6: % of test hypotheses fully groundable after adding various microtheories (n-sized Random, Usage, QC, & PC Mts) to a base Corpus. ... MedQA Grounding Rate (%) of Test Hypotheses
  - [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf)
- **Zero-shot generalization** (construct): *measured_by*, 1 paper
  > To further evaluate the generalizability of GCR, we conduct zero-shot transfer experiments on three new KGQA datasets: FreebaseQA, CSQA and MedQA (Section 5.1).
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **Knowledge graph question answering** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate KGQA benchmarks spanning different backbone KGs. ... MedQA (Jin et al., 2021) consists of questions extracted from USMLE exams. (Section 4.1)
  - [BYOKG-RAG: Multi-Strategy Graph Retrieval for Knowledge Graph Question Answering](https://aclanthology.org/2025.emnlp-main.1417.pdf)
