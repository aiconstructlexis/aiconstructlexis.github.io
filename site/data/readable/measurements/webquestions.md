# WebQuestions
**Type:** Measurement instrument  
**Supporting papers:** 40  
**Also known as:** WebQuestion, WebQS, WebQ, WebQs, Webquestions, Web Questions, WQA, web_questions  

## State of the Field

**What it is.** Across papers, WebQuestions is most commonly described as an open-domain question answering dataset or benchmark. Definitions repeatedly say its questions come from web queries, Google Search, or the Google Suggest API, and several add that answers are entities in Freebase; some papers further describe it as open-ended text QA, factual question answering, or a fact-recall or closed-book benchmark, and one definition says questions focus on a single named entity. A smaller speech-oriented line repurposes it for spoken QA by synthesizing audio versions from the original dataset, while papers also mention using its training split and a test set of 2032 questions.

**What it is claimed to measure.** Papers use WebQuestions to measure 6 behavioral indicators and 3 constructs. The prevailing use is for open-domain question answering, with smaller lines of work using it for spoken question answering, factual recall, world knowledge, and closed-book question answering, and papers also reporting it as measuring other targets. Overall, the claims spread across several behaviors and constructs rather than centering on one construct.

**Space of uses.** No measurement instrument is linked to it. In practice, papers usually evaluate it alongside Natural Questions and TriviaQA, sometimes with HotpotQA, SQuAD, and Llama Questions, and they position it as one item in broader benchmark suites, including open-domain QA comparisons, closed-book QA averages, 1-shot or 5-shot exact match evaluations, and spoken QA tests. Some authors also use its training split to construct training data or sample from it, and one paper treats it as an unseen evaluation task.

## Sources

**WebQuestions** (15 papers: [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf), [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf), [SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/428ceef2cd8a53add7213e04d1746479-Paper-Conference.pdf), [The Cost of Scaling Down Large Language Models: Reducing Model Size Affects Memory before In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/bb68f698772f14b6d8eaef4529fb9176-Paper-Conference.pdf), [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf), [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf), [On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf), [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf), [PA-RAG: RAG Alignment via Multi-Perspective Preference Optimization](https://aclanthology.org/2025.naacl-long.459.pdf), [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf), [CartesianMoE: Boosting Knowledge Sharing among Experts via Cartesian Product Routing in Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.505.pdf), [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf), [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1371.pdf), [DSMoE: Matrix-Partitioned Experts with Dynamic Routing for Computation-Efficient Dense LLMs](https://aclanthology.org/2025.emnlp-main.997.pdf), [HydraRAG: Structured Cross-Source Enhanced Large Language Model Reasoning](https://aclanthology.org/2025.emnlp-main.730.pdf))
> An open-domain question answering dataset used to examine more generic QA performance.

**WebQuestion** (1 paper: [Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b054fadf1ccd80b37d465f6082629934-Paper-Conference.pdf))
> A generative question answering dataset used to evaluate models on open-domain QA tasks, referenced in the appendix for additional experiments.

**WebQS** (1 paper: [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf))
> A question-answering benchmark used to evaluate world knowledge retention.

**WebQ** (2 papers: [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf), [Unveil: Unified Visual-Textual Integration and Distillation for Multi-modal Document Retrieval](https://aclanthology.org/2025.acl-long.1166.pdf))
> The WebQuestions (WebQ) dataset, an open-domain question answering benchmark where questions are sourced from the web and answers are entities in Freebase.

**WebQs** (2 papers: [Theory, Analysis, and Best Practices for Sigmoid Self-Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/a43b459e9fab3a703148ba0c83b8a442-Paper-Conference.pdf), [GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models](https://aclanthology.org/2025.acl-long.255.pdf))
> The WebQuestions dataset, which consists of questions from Google Search that can be answered using Freebase, testing open-domain question answering.

**Webquestions** (1 paper: [Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf))
> A question-answering dataset of questions from web users, used as an unseen evaluation task.

**Web Questions** (4 papers: [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf), [Freeze-Omni: A Smart and Low Latency Speech-to-speech Dialogue Model with Frozen LLM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25aw/wang25aw.pdf), [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf), [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf))
> A dataset for spoken question answering that contains questions sourced from the web, requiring the model to provide factual answers.

**WQA** (1 paper: [Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a0b1082fc7823c4c68abcab4fa850e9c-Paper-Conference.pdf))
> Web-based QA benchmark used to evaluate question answering over web information.

**web_questions** (1 paper: [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf))
> Question answering dataset consisting of factual questions extracted from web queries, used to evaluate in-context learning performance.

## Relationships

### → WebQuestions
- **Open-domain question answering** (behavioral indicator): *measured_by*, 8 papers
  > Moreover, in order to examine ToG on more generic tasks, we also prepare one open-domain QA dataset: WebQuestions (Berant et al., 2013);
  - [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf)
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
  - [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf)
  - [GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](https://aclanthology.org/2025.acl-long.527.pdf)
  - [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1371.pdf)
  - [A Theory for Token-Level Harmonization in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a461bdff86cc07e976bb6c518810398-Paper-Conference.pdf)
- **Spoken question answering** (behavioral indicator): *measured_by*, 3 papers
  > Similarly, on the Web Questions test set, the proposed model attains an accuracy of 6.1%, while SpeechGPT yields a comparable accuracy of 6.5%. (Section 4.2.3)
  - [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf)
  - [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf)
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
- **Factual recall** (behavioral indicator): *measured_by*, 2 papers
  > (f) fact recall (WebQuestions (Berant et al., 2013), Natural Questions (Kwiatkowski et al., 2019)) (Section 4.2)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf)
- **World knowledge** (construct): *measured_by*, 2 papers
  > The world knowledge is evaluated by the exact match scores (%) on TriviaQA [23], NQ open [29], and WebQS [4] (Section 4).
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **Closed-book question answering** (behavioral indicator): *measured_by*, 1 paper
  > Closed book QA: TriviaQA (Joshi et al., 2017), web_questions (Berant et al., 2013) (Section 5.1).
  - [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf)
- **Knowledge graph question answering** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate LMP on five KGQA datasets: WebQSP (Yih et al., 2016), CWQ (Talmor and Berant, 2018), and GrailQA (Gu et al., 2021) for multi-hop QA; Simple Questions (Bordes et al., 2015) for single-hop QA; WebQuestions (Berant et al., 2013) for open-domain QA. (Section 4.1.1)
  - [Digest the Knowledge: Large Language Models empowered Message Passing for Knowledge Graph Question Answering](https://aclanthology.org/2025.acl-long.750.pdf)
- **Multi-hop reasoning** (construct): *measured_by*, 1 paper
  > We evaluate our approach on four standard KBQA datasets, all of which require multi-hop reasoning: ComplexWebQuestions (CWQ), WebQuestionsSP (WebQSP), WebQuestions, and GrailQA (Section 5).
  - [iQUEST: An Iterative Question-Guided Framework for Knowledge Base Question Answering](https://aclanthology.org/2025.acl-long.760.pdf)
- **Multi-hop question answering** (behavioral indicator): *measured_by*, 1 paper
  > We conduct experiments on five multi-hop QA datasets: HotPotQA (Yang et al., 2018), 2WikiMultiHopQA (2Wiki) (Ho et al., 2020), MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2023) and WebQuestions (WebQA) (Berant et al., 2013). (Section 4.1)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)
- **Factuality** (construct): *measured_by*, 1 paper
  > We evaluate factual correctness and spoken question answering abilities of our model on Llama Questions (Nachmani et al., 2024), and a synthesized audio version of TriviaQA (Joshi et al., 2017) and Web Questions (Berant et al., 2013). (Section 5.4)
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
