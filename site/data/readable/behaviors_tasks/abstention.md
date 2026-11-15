# Abstention
**Type:** Behavioral indicator  
**Supporting papers:** 24  
**Also known as:** Abstaining from answering, Answer abstention, Selective answering, Task avoidance, Ill-defined problem rejection, Task skipping  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats abstention as withholding a substantive or final answer when the model is uncertain, not confident, lacks necessary knowledge, or cannot answer from the provided information. Common realizations are explicit non-answer outputs such as I don't know, Unknown, NO-RESPONSE, or other refusal-like signals, and several papers also treat asking for more information or a clarification question as abstention. A smaller line of work narrows it to selective answering above a confidence threshold, or to not giving a definitive answer as instructed, including rejecting ill-defined problems or skipping tasks when tools or information are missing. One paper also claims a causal relationship from Abstention to Hallucination, stating that shifting toward abstention prevents hallucinations.

**Variants.** Most variants stay within question answering, but papers study it under several nearby names: answer abstention, selective answering, task avoidance, ill-defined problem rejection, and task skipping. In clinical reasoning, abstention can mean not answering and instead asking an information-seeking question; in retrieval settings it can mean abstaining when the passage lacks the answer; in multimodal question answering it can mean outputting a reserved keyword when the image lacks the needed information. Other variants treat it as refusing unsolvable math problems, skipping tool-augmented queries after an awareness check, or as an allowed option in multiple-choice scoring with negative marking.

**Space of elicitation and scores.** Papers link abstention to 4 measurement instruments: LLM-as-a-judge, LLMEval, LongMemEval, and TDIUC. These instruments score or elicit the behavior in different ways, including judge labels such as abstention versus direct answer, benchmark ratings of correct, abstain, or hallucinate, a benchmark that lists abstention as one core ability, and absurd visual questions that should not be answered. Outside named instruments, papers often operationalize abstention with explicit abstain instructions, confidence thresholds for returning no answer, reserved outputs such as I don't know, NO-RESPONSE, doesnotapply, [IDK], or no, and in one case a distinction between consistent refusal and partly abstained outputs across multiple samples.

**What it is taken as evidence of.** Papers link abstention to 9 constructs. One paper claims a causal relationship from Calibration to Abstention, while others report Abstention is related to Confidence, Factuality, Generalization, and Honesty; 4 other construct links are also recorded with a mix of related and causal directions. The linked constructs therefore span several framings rather than one common target construct.

## Sources

**Abstention** (4 papers: [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf), [Sufficient Context: A New Lens on Retrieval Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf), [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf), [Which of These Best Describes Multiple Choice Evaluation with LLMs? A) Forced B) Flawed C) Fixable D) All of the Above](https://aclanthology.org/2025.acl-long.169.pdf))
> The observable behavior of refraining from providing a final answer when confidence is low, opting instead to ask a question.

**Abstaining from answering** (3 papers: [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf), [Learning to Route LLMs with Confidence Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25b/chuang25b.pdf), [Do RAG Systems Really Suffer From Positional Bias?](https://aclanthology.org/2025.emnlp-main.1422.pdf))
> Withholding an answer by emitting an uncertainty signal or equivalent refusal-like output instead of a substantive response.

**Answer abstention** (1 paper: [Fictitious Synthetic Data Can Improve LLM Factuality via Prerequisite Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/98ecdc722006c2959babbdbdeb22eb75-Paper-Conference.pdf))
> The model's action of declining to answer a question, often by stating "I don't know", when it lacks the necessary knowledge.

**Selective answering** (1 paper: [QA-Calibration of Language Model Confidence Scores](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd96cb9a239c37b39dbf34f3f5a4c56f-Paper-Conference.pdf))
> The observable behavior of returning an answer only when confidence exceeds a threshold, otherwise abstaining from responding.

**Task avoidance** (1 paper: [Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf))
> The behavior of a model failing to provide a definitive answer to a task as instructed in the prompt.

**Ill-defined problem rejection** (1 paper: [VCSearch: Bridging the Gap Between Well-Defined and Ill-Defined Problems in Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.642.pdf))
> The observable behavior of a model refusing to generate a solution when presented with a mathematical problem that has missing or contradictory conditions.

**Task skipping** (1 paper: [Benchmarking Failures in Tool-Augmented Language Models](https://aclanthology.org/2025.naacl-long.149.pdf))
> Choosing not to attempt a task when the model determines it lacks necessary information or tools to solve it.

## Relationships

### Abstention →
- **TDIUC** (measurement instrument): *measured_by*, 1 paper
  > We evaluate on TDIUC (Kafle & Kanan, 2017), a VQA dataset containing absurd questions (∼22% of a total number of questions), that are not related to the image and thus should not be answered.
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **LLMEval** (measurement instrument): *measured_by*, 1 paper
  > Then, for each example, we can rate it as “correct” or “abstain” or “hallucinate” depending on the LLMEval output. (Section 4.2)
  - [Sufficient Context: A New Lens on Retrieval Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf)
- **LongMemEval** (measurement instrument): *measured_by*, 1 paper
  > We introduce LONGMEMEVAL, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. (Abstract)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > CDA successfully shifts the distribution towards abstention, preventing hallucinations. (Section 6.6, Figure 10)
  - [When to Speak, When to Abstain: Contrastive Decoding with Abstention](https://aclanthology.org/2025.acl-long.479.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > A pretrained LLM-as-judge labels responses as either abstention (clarification or refusal) or direct answer... (Section 4.1)
  - [Sparse Neurons Carry Strong Signals of Question Ambiguity in LLMs](https://aclanthology.org/2025.emnlp-main.813.pdf)

### → Abstention
- **In-context learning** (construct): *causes*, 1 paper
  > “ICL significantly improves abstention.”
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Calibration** (construct): *causes*, 1 paper
  > Finally, finetuning with our listener-aware method leads to an emergent increase in model abstention (e.g. saying “I don’t know”) for answers that are likely to be wrong, trading recall for precision. (Abstract)
  - [LACIE: Listener-Aware Finetuning for Calibration in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8eaf3bcdc105423a972ed90eb07217-Paper-Conference.pdf)

### Associated with
- **Honesty** (construct), 1 paper
  > LMMs must be ... honest (e.g., abstention or the ability to say I don’t know...)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Generalization** (construct), 1 paper
  > generalizability: whether abstention extends to concept’s descendants (Section 1)
  - [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.353.pdf)
- **Specificity** (construct), 1 paper
  > specificity: whether questions about ancestor and sibling concepts are not refused, where abstention is undesirable. (Section 1)
  - [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.353.pdf)
- **Truthfulness** (construct), 1 paper
  > It evaluates whether models can provide factually accurate responses, or appropriately abstain when uncertain. (Section 2.1)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **Factuality** (construct), 1 paper
  > We define L(∅, ·) = 0, which indicates that we do not penalize the model for abstaining from responding when it is uncertain, as here we only focus on the assurance of factuality while neglecting other aspects of reliability such as omission of information. (Section 3.1)
  - [Towards Statistical Factuality Guarantee for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.576.pdf)
- **Confidence** (construct), 1 paper
  > The goal of the Abstention Module is to evaluate the confidence level of the Expert system
  - [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf)
- **Knowledge boundary awareness** (construct), 1 paper
  > To address the critical limitation of RAFT models regarding their inability to abstain from answering when queries fall outside both knowledge boundaries (✘✘), we construct a comprehensive preference dataset that captures the desired behavior for each quadrant. (Section 5)
  - [Divide-Then-Align: Honest Alignment based on the Knowledge Boundary of RAG](https://aclanthology.org/2025.acl-long.561.pdf)
