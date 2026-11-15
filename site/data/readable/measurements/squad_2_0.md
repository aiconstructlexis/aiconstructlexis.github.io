# SQuAD 2.0
**Type:** Measurement instrument  
**Supporting papers:** 22  
**Also known as:** SQuAD v2, SQuAD 2, SQuADv2, SQuAD2.0, SQuAD2, SQuAD v2.0  

## State of the Field

**What it is.** Across papers, this benchmark appears under several surface forms, including SQuAD v2, SQuAD v2.0, SQuADv2, and SQuAD2, but the prevailing description is the Stanford Question Answering Dataset v2.0, a reading comprehension or question answering benchmark built from Wikipedia articles or passages. Most definitions emphasize span-based answering with some unanswerable questions, so models are expected either to extract an answer or abstain, including to "reject when the context is insufficient." A smaller group of papers describes it as source material for other resources or tasks, including a True-False dataset, the UQA corpus, and a document retrieval task sampled from SQuAD v2.

**What it is claimed to measure.** Papers use it to measure 4 behavioral indicators and no constructs. The prevailing measurement claim is Machine reading comprehension, and several papers also report it as measuring Question answering; smaller lines of work report it as measuring Document question answering and Information retrieval. Overall, the reported uses cluster around reading comprehension and QA behaviors rather than around constructs.

**Space of uses.** No measurement instrument is linked to it in the recorded relationships. In the quoted passages, it also appears alongside GLUE in several benchmark setups, and a few papers mention it with SQuAD v1.1, TruthfulQA, UQuAD1.0, and TriviaQA. Papers usually position it as a downstream benchmark for reading comprehension or QA, including one-shot evaluation, fine-tuning, and evaluation without fine-tuning, though some repurpose it as source data for derived corpora or tasks.

## Sources

**SQuAD 2.0** (6 papers: [Representation Deficiency in Masked Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfde7fb279709eff53faa074b45840d8-Paper-Conference.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [Are the Hidden States Hiding Something? Testing the Limits of Factuality-Encoding Capabilities in LLMs](https://aclanthology.org/2025.acl-long.304.pdf), [ExLM: Rethinking the Impact of $\texttt[MASK]$ Tokens in Masked Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zheng25q/zheng25q.pdf), [From Understanding to Generation: An Efficient Shortcut for Evaluating Language Models](https://aclanthology.org/2025.emnlp-main.1148.pdf), [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf))
> The Stanford Question Answering Dataset 2.0, a reading comprehension dataset that includes unanswerable questions, used to evaluate a model's ability to abstain from answering when no correct answer is present in the context.

**SQuAD v2** (2 papers: [D.Va: Validate Your Demonstration First Before You Use It](https://aclanthology.org/2025.acl-long.129.pdf), [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf))
> Question answering dataset combining span extraction and unanswerable questions, requiring models to either extract an answer or correctly identify when no answer exists.

**SQuAD v2.0** (1 paper: [SCOP: Evaluating the Comprehension Process of Large Language Models from a Cognitive View](https://aclanthology.org/2025.acl-long.852.pdf))
> The Stanford Question Answering Dataset v2.0, a reading comprehension benchmark based on expository Wikipedia articles where answers are text spans and some questions may be unanswerable.

**SQuAD 2** (1 paper: [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf))
> Question answering benchmark with unanswerable questions, used to assess a model's ability to refrain from answering when context is insufficient.

**SQuADv2** (2 papers: [A Middle Path for On-Premises LLM Deployment: Preserving Privacy Without Sacrificing Model Confidentiality](https://aclanthology.org/2025.emnlp-main.420.pdf), [Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf))
> The Stanford Question Answering Dataset (SQuAD) version 2.0, which includes unanswerable questions to test a model's ability to abstain from answering when the text does not support it.

**SQuAD2.0** (1 paper: [PakBBQ: A Culturally Adapted Bias Benchmark for QA](https://aclanthology.org/2025.emnlp-main.818.pdf))
> The Stanford Question Answering Dataset version 2.0, used as a source for creating other QA corpora like UQA.

**SQuAD2** (1 paper: [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf))
> The Stanford Question Answering Dataset (version 2), which includes unanswerable questions to test whether a model knows what it doesn't know.

## Relationships

### → SQuAD 2.0
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 5 papers
  > “our reading comprehension (RC) fine-tuning datasets include SQuAD 2.0 ...”
  - [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
  - [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf)
  - [From Understanding to Generation: An Efficient Shortcut for Evaluating Language Models](https://aclanthology.org/2025.emnlp-main.1148.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 3 papers
  > SuperContext is validated on a comprehensive OOD benchmarks GLUE-X (Yang et al., 2022), and a QA dataset, SQuAD 2.0 (Rajpurkar et al., 2018). (Section 2)
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
  - [RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates](https://aclanthology.org/2025.acl-long.1293.pdf)
  - [RECALL: REpresentation-aligned Catastrophic-forgetting ALLeviation via Hierarchical Model Merging](https://aclanthology.org/2025.emnlp-main.829.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > Document Retrieval In this task the model receives a query and Ndocs randomly assorted documents, and its objective is to return the id of the matching document. Our data is sampled from SQuAD v2 (Rajpurkar et al., 2018). (Section 5)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
- **Document question answering** (behavioral indicator): *measured_by*, 1 paper
  > “To this end, we focus on three open-book QA datasets: 1. SQuAD 2.0 (Rajpurkar et al., 2018): A reading comprehension benchmark where a model is presented a question along with a Wikipedia article containing the answer.”
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
