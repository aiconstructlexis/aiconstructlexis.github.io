# Closed-book question answering
**Type:** Behavioral indicator  
**Supporting papers:** 11  
**Also known as:** Closed-book retrieval  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats closed-book question answering as answering questions from knowledge stored in the model's parameters, internal knowledge, or parametric memory, without external documents, evidence, or other supporting context. In descriptions that specify the procedure, the model is given only the question, with no supporting evidence in the prompt, and is instructed to provide an answer. Some papers further describe the questions as factual or knowledge-intensive, and one paper uses the alternate name closed-book retrieval for answering a query or retrieving information without any external context or knowledge source.

**Variants.** Most papers study it as closed-book QA over datasets such as TriviaQA, WebQuestions, Natural Questions, and EntityQuestions. These settings are described as knowledge-intensive questions, natural web queries, and a CBQA-specific dataset with knowledge extracted from Wikipedia. A smaller line of work uses the name closed-book retrieval and includes memory-intensive retrieval, including a phone-book task.

**Space of elicitation and scores.** Papers link this behavior to 3 measurement instruments, all question-answering datasets: EntityQuestions, TriviaQA, and WebQuestions. EntityQuestions is described as CBQA-specific, TriviaQA supplies knowledge-intensive questions, and WebQuestions appears as a closed-book question-answering dataset sourced from natural web queries.

**What it is taken as evidence of.** Papers do not present this behavior as evidence of a construct. One paper instead reports that it is related to Hallucination, describing hallucinations in closed-book question answering as cases where the model generates incorrect or fabricated answers.

## Sources

**Closed-book question answering** (7 papers: [Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://proceedings.iclr.cc/paper_files/paper/2024/file/99261adc8a6356b38bcf999bba9a26dc-Paper-Conference.pdf), [Benchmarking and Improving Generator-Validator Consistency of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfcb583d225b1db8d3ca2331f6785774-Paper-Conference.pdf), [Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce806d8b4bf38cd92d483e5a0490d983-Paper-Conference.pdf), [The Cost of Scaling Down Large Language Models: Reducing Model Size Affects Memory before In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/bb68f698772f14b6d8eaef4529fb9176-Paper-Conference.pdf), [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf), [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf), [Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels](https://aclanthology.org/2025.emnlp-main.25.pdf))
> The task of answering questions based on general knowledge stored in the model's parameters, without access to external documents.

**Closed-book retrieval** (1 paper: [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf))
> The task of answering a query or retrieving information without access to any external context or knowledge source.

## Relationships

### Closed-book question answering →
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > Closed book QA: TriviaQA (Joshi et al., 2017), web_questions (Berant et al., 2013) (Section 5.1).
  - [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf)
- **WebQuestions** (measurement instrument): *measured_by*, 1 paper
  > Closed book QA: TriviaQA (Joshi et al., 2017), web_questions (Berant et al., 2013) (Section 5.1).
  - [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf)
- **EntityQuestions** (measurement instrument): *measured_by*, 1 paper
  > we use the ENTITYQUESTIONS (Sciavolino et al., 2021) to construct the training and testing datasets for our experiments, which is a CBQA-specific dataset containing knowledge across 24 topics extracted from Wikipedia (Section 3.1).
  - [Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels](https://aclanthology.org/2025.emnlp-main.25.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > One significant challenge in CBQA is addressing hallucinations-instances where the model generates incorrect or fabricated answers (Section 2).
  - [Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels](https://aclanthology.org/2025.emnlp-main.25.pdf)
