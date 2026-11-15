# Relevance
**Type:** Construct  
**Supporting papers:** 34  
**Also known as:** Relation, Topic relevance  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats relevance as on-topic alignment: whether a model output, summary, argument, reasoning path, or document directly addresses the prompt, question, instruction, query, or debate topic and avoids unrelated or off-topic content. Many definitions use near-identical wording such as being pertinent and on-topic, staying focused on the main topic, or asking whether the output directly relates to the instruction. A smaller line of work treats it as a latent tendency or ability, either of a model to make task-relevant contributions in interaction or of a text to maintain pragmatic alignment with discourse topic and context, and a few task-specific definitions broaden it beyond strict topical match to include capturing key points, providing valuable extensions beyond the topic, or balancing topic coverage with off-topic avoidance.

**Space of facets.** Many papers place relevance inside broader evaluation schemes rather than giving it an internal taxonomy. It appears as one of the dimensions of instruction following, as a subjective criterion in debating under the label topic relevance, and as a pragmatic relevance condition within coherence assessment; one survey instead uses the near-synonymous label Relation for contributions that help solve the shared task goal. The same label is also applied to different units of analysis, including response relevance, document-to-question relevance, reasoning-path relevance, and code-review relevance, with one code-review formulation defining it as an overall quality balance through the formula "Rel = 2 · Con · Comp / (Con + Comp)".

**Space of measurement.** Operationally, papers link relevance to 4 measurement instruments and 3 behavioral indicators. The most common instruments are LLM-as-a-judge, followed by human evaluation, G-Eval, and expert evaluation: GPT-4 or GPT-4o rate response pairs or long-form answers for relevance, users or annotators score surveys, summaries, conversations, or research ideas on ordered scales, G-Eval scores summary relevance against reference labels, and expert annotators judge fine-grained dimensions such as faithfulness and relevance. These operationalizations mostly match the dominant on-topic framing, though some papers measure it indirectly, for example through the probability of generating a question from a document, through faithfulness and reward filters as an indirect signal, or through the formula "Rel = 2 · Con · Comp / (Con + Comp)".

**Links.** In reported links, one paper claims a causal relationship from Relevance to Information retrieval, stating that explicitly modeling relevance together with consistency trains a retriever to retrieve documents needed for answering a question. Papers also report 3 behavioral-indicator links and 2 construct links overall: Question answering is related to Relevance, Relevance is related to Reward hacking, and Consistency and Instruction following ability are each related to Relevance. One related claim says question-answering systems can have relevance as an attribute, another makes relevance one of the dimensions of instruction following, and the reward-hacking paper describes contextual relevance as an aspect of reward hacking.

## Sources

**Relevance** (13 papers: [Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf), [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf), [Human Feedback is not Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2024/file/f719b8ca81221f380836e573d479c223-Paper-Conference.pdf), [AutoSurvey: Large Language Models Can Automatically Write Surveys](https://proceedings.neurips.cc/paper_files/paper/2024/file/d07a9fc7da2e2ec0574c38d5f504d105-Paper-Conference.pdf), [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf), [Evaluating Small Language Models for News Summarization: Implications and Factors Influencing Performance](https://aclanthology.org/2025.naacl-long.253.pdf), [DETQUS: Decomposition-Enhanced Transformers for QUery-focused Summarization](https://aclanthology.org/2025.naacl-long.138.pdf), [WebQuality: A Large-scale Multi-modal Web Page Quality Assessment Dataset with Multiple Scoring Dimensions](https://aclanthology.org/2025.naacl-long.25.pdf), [CAMIEval: Enhancing NLG Evaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.438.pdf), [CRScore: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells](https://aclanthology.org/2025.naacl-long.457.pdf), [A Novel Computational Modeling Foundation for Automatic Coherence Assessment](https://aclanthology.org/2025.naacl-long.277.pdf), [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf), [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.24.pdf))
> The degree to which a model's generated response is pertinent and on-topic with respect to the user's prompt or question.

**Relation** (1 paper: [How to Enable Effective Cooperation Between Humans and NLP Models: A Survey of Principles, Formalizations, and Beyond](https://aclanthology.org/2025.acl-long.22.pdf))
> The latent tendency of a model to produce contributions that are relevant to the shared task goal during human-model interaction.

**Topic relevance** (1 paper: [InspireDebate: Multi-Dimensional Subjective-Objective Evaluation-Guided Reasoning and Optimization for Debating](https://aclanthology.org/2025.acl-long.1335.pdf))
> The degree to which the model's arguments directly address and align with the core debate topic, avoiding digression or irrelevance.

## Relationships

### Relevance →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 5 papers
  > We prompt GPT-4 to rate responses from various decoding strategies on relevance, accuracy, and insightfulness, scoring them from 1 to 10. (Table 2)
  - [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
  - [CaLMQA: Exploring culturally specific long-form question answering across 23 languages](https://aclanthology.org/2025.acl-long.578.pdf)
  - [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.891.pdf)
  - [TounsiBench: Benchmarking Large Language Models for Tunisian Arabic](https://aclanthology.org/2025.emnlp-main.1756.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 4 papers
  > Users are asked to rate the relevance, structure, and usefulness to their actual work of the generated survey on a scale from 1 (poor) to 5 (excellent).
  - [AutoSurvey: Large Language Models Can Automatically Write Surveys](https://proceedings.neurips.cc/paper_files/paper/2024/file/d07a9fc7da2e2ec0574c38d5f504d105-Paper-Conference.pdf)
  - [Evaluating Small Language Models for News Summarization: Implications and Factors Influencing Performance](https://aclanthology.org/2025.naacl-long.253.pdf)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
  - [Can Large Language Models Unlock Novel Scientific Research Ideas?](https://aclanthology.org/2025.emnlp-main.1704.pdf)
- **G-Eval** (measurement instrument): *measured_by*, 2 papers
  > For Event Summarization, we adopt G-Eval (Liu et al., 2023b), an LLM-based metric that evaluates the relevance, consistency, and coherence of generated summaries against reference labels. (Section 4.3)
  - [MemInsight: Autonomous Memory Augmentation for LLM Agents](https://aclanthology.org/2025.emnlp-main.1683.pdf)
  - [Paired by the Teacher: Turning Unpaired Data into High-Fidelity Pairs for Low-Resource Text Generation](https://aclanthology.org/2025.emnlp-main.1030.pdf)
- **Information retrieval** (behavioral indicator): *causes*, 1 paper
  > By explicitly modeling both consistency and relevance, our method trains a retriever to retrieve the documents necessary for answering a given question. (Section 3.2)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
- **Expert evaluation** (measurement instrument): *measured_by*, 1 paper
  > Automatic evaluation of retrieval augmented generation (RAG) systems relies on fine-grained dimensions like faithfulness and relevance, as judged by expert human annotators.
  - [MEMERAG: A Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1101.pdf)

### Associated with
- **Question answering** (behavioral indicator), 1 paper
  > question-answering systems can have attributes of relevance, verbosity, and completeness [52].
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **Instruction following ability** (construct), 1 paper
  > Specifically, we define three fundamental dimensions of instruction-following: relevance, factuality, and adherence. (Abstract)
  - [CAMIEval: Enhancing NLG Evaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.438.pdf)
- **Consistency** (construct), 1 paper
  > While the answer probability by itself seemed ineffective, its combination with the question probability becomes powerful, as it evaluates the consistency among relevant documents, with irrelevant ones already filtered out due to their low question probabilities. (Section 4.2.2)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
- **Reward hacking** (behavioral indicator), 1 paper
  > "increased energy loss reduces the upper bound of contextual relevance in LLMs, which is a critical aspect of reward hacking"
  - [The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25c/miao25c.pdf)
