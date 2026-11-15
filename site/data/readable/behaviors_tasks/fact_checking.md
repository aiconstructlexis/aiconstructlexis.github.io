# Fact checking
**Type:** Behavioral indicator  
**Supporting papers:** 79  
**Also known as:** Veracity analysis, Factuality checking, Fact extraction and verification, Veracity judgment, Claim verification, Fact verification, Table fact verification, Statement verification, Verdict prediction, Factual consistency evaluation, Veracity labeling, Answer verification, Answer correctness assessment, Sentence-level verification, Factual verification, Veracity prediction, Fact-checking, Truthfulness prediction, Statement validation, Legal fact verification, Table-based fact verification, Sub-claim verification  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is verifying the truthfulness or veracity of a claim, statement, or queried fact against retrieved evidence, a grounding document, a corpus, or another knowledge source. Most papers treat success as a veracity label such as Supported or Refuted, or a binary True or False judgment; a smaller line also includes NotEnoughInfo, Unsupported, or other categories, sometimes together with extracted evidence or explanations. Some work broadens the task to deciding whether to believe a claim or news item after synthesizing possibly missing or contradictory evidence, and some explicitly stage it as claim detection or extraction, evidence retrieval, and verdict prediction. As one survey puts it, veracity prediction uses 'claims and the evidence that aligns with them' (The Psychology of Falsehood: A Human-Centric Survey of Misinformation Detection).

**Variants.** Recurring settings include scientific claim verification against abstracts or papers, news and misinformation claims, table-grounded verification, and knowledge-base or knowledge-graph checking, including propositional logic queries. Smaller variants turn the unit of analysis into medical or legal statements, out-of-context image captions, sub-claims or triplets, or generated outputs such as answers, sentences, summaries, and dialogue responses.

**Space of elicitation and scores.** Papers measure this behavior with 16 instruments. FEVER appears most often, followed by FEVEROUS, SciFact, HoVer, and TabFact. These are mostly fact-checking or fact-verification benchmarks and datasets, spanning three-class claim verification, complex evidence settings, scientific claims, multi-hop verification, and table-grounded judgments.

**What it is taken as evidence of.** Papers connect this behavior to 8 constructs, but they do not converge on a single construct it is taken to reflect. The most frequent links are that it is related to interpretability and explainability, that one paper claims a causal relationship from chain-of-thought reasoning to fact checking, and that it is related to faithfulness, logical consistency, and multi-hop reasoning. Papers also connect it to several other constructs.

## Sources

**Veracity prediction** (4 papers: [The Psychology of Falsehood: A Human-Centric Survey of Misinformation Detection](https://aclanthology.org/2025.emnlp-main.428.pdf), [COVE: COntext and VEracity prediction for out-of-context images](https://aclanthology.org/2025.naacl-long.102.pdf), [Grounding Fallacies Misrepresenting Scientific Publications in Evidence](https://aclanthology.org/2025.naacl-long.491.pdf), [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf))
> The task of classifying a claim as true, false, or another relevant category based on retrieved evidence.

**Veracity analysis** (1 paper: [Attacks by Content: Automated Fact-checking is an AI Security Issue](https://aclanthology.org/2025.emnlp-main.431.pdf))
> The process of synthesizing evidence to make a judgment on whether a claim should be believed, including handling cases of missing or contradictory evidence.

**Fact extraction and verification** (1 paper: [AgentPro: Enhancing LLM Agents with Automated Process Supervision](https://aclanthology.org/2025.emnlp-main.506.pdf))
> The task of identifying factual claims in text and verifying their correctness against a knowledge source.

**Factuality checking** (1 paper: [MusKGC: A Flexible Multi-source Knowledge Enhancement Framework for Open-World Knowledge Graph Completion](https://aclanthology.org/2025.emnlp-main.508.pdf))
> Judging whether a generated fact is entailed by retrieved evidence.

**Fact checking** (5 papers: [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf), [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf), [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf), [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf), [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf))
> The task of verifying the truthfulness of a given claim against a corpus of evidence.

**Veracity judgment** (1 paper: [A Multi-Agent Framework with Automated Decision Rule Optimization for Cross-Domain Misinformation Detection](https://aclanthology.org/2025.emnlp-main.291.pdf))
> The task of making a final determination on whether a piece of news is true or false, based on provided analysis, evidence, and decision rules.

**Claim verification** (3 papers: [SciRIFF: A Resource to Enhance Language Model Instruction-Following over Scientific Literature](https://aclanthology.org/2025.emnlp-main.310.pdf), [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf), [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.575.pdf))
> Determining whether a scientific claim is supported or refuted by evidence in a given abstract or paper, often accompanied by extracted supporting or refuting statements.

**Fact verification** (10 papers: [InfoGain-RAG: Boosting Retrieval-Augmented Generation through Document Information Gain-based Reranking and Filtering](https://aclanthology.org/2025.emnlp-main.365.pdf), [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf), [Grounding by Trying: LLMs with Reinforcement Learning-Enhanced Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/4169f1425b80c3a6e7daa84a1d09b077-Paper-Conference.pdf), [Curriculum Debiasing: Toward Robust Parameter-Efficient Fine-Tuning Against Dataset Biases](https://aclanthology.org/2025.acl-long.469.pdf), [DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation](https://aclanthology.org/2025.acl-long.358.pdf), [Towards Multi-dimensional Evaluation of LLM Summarization across Domains and Languages](https://aclanthology.org/2025.acl-long.702.pdf), [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf), [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf), [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf), [CORRECT: Context- and Reference-Augmented Reasoning and Prompting for Fact-Checking](https://aclanthology.org/2025.naacl-long.154.pdf))
> The task of determining whether a given claim is supported or refuted by evidence from a provided knowledge source.

**Table fact verification** (1 paper: [Can GRPO Boost Complex Multimodal Table Understanding?](https://aclanthology.org/2025.emnlp-main.637.pdf))
> The task of determining whether a given statement is true or false based on the content of an associated table.

**Statement verification** (2 papers: [Unsupervised Hallucination Detection by Inspecting Reasoning Processes](https://aclanthology.org/2025.emnlp-main.1124.pdf), [Reliable and Diverse Evaluation of LLM Medical Knowledge Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/91a5bb5e5939cb075f5f2464d7b8bbf0-Paper-Conference.pdf))
> The observable behavior of a model assessing whether a given statement is factually correct, often through step-by-step reasoning.

**Verdict prediction** (1 paper: [Adversarial Attacks Against Automated Fact-Checking: A Survey](https://aclanthology.org/2025.emnlp-main.1171.pdf))
> Classifying the truthfulness of a claim based on retrieved evidence, typically as Supported, Refuted, or NotEnoughInfo.

**Factual consistency evaluation** (1 paper: [Are LLMs Better than Reported? Detecting Label Errors and Mitigating Their Effect on Model Performance](https://aclanthology.org/2025.emnlp-main.1360.pdf))
> Assessing whether a generated text (e.g., summary, dialogue response) is factually consistent with respect to a grounding text or source document.

**Veracity labeling** (1 paper: [MedFact: A Large-scale Chinese Dataset for Evidence-based Medical Fact-checking of LLM Responses](https://aclanthology.org/2025.emnlp-main.1646.pdf))
> Assigning a truthfulness label to a claim-evidence pair after reviewing both elements, either through human annotation or LLM-assisted labeling.

**Answer verification** (1 paper: [DocAgent: An Agentic Framework for Multi-Modal Long-Context Document Understanding](https://aclanthology.org/2025.emnlp-main.893.pdf))
> The process of cross-checking a generated answer against complementary sources or modalities to confirm its accuracy and completeness.

**Sentence-level verification** (1 paper: [Efficient Real-time Refinement of Language Model Text Generation](https://aclanthology.org/2025.emnlp-main.1753.pdf))
> The observable process of checking the factual correctness of individual sentences as they are generated during text production.

**Factual verification** (1 paper: [When Truthful Representations Flip Under Deceptive Instructions?](https://aclanthology.org/2025.emnlp-main.826.pdf))
> The observable task of assessing a given factual statement and producing a binary output of "True" or "False" based on the instructional context.

**Fact-checking** (8 papers: [Logical Consistency of Large Language Models in Fact-Checking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3209cf3312b2cbb68e33644362ddc2bd-Paper-Conference.pdf), [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf), [Can External Validation Tools Improve Annotation Quality for LLM-as-a-Judge?](https://aclanthology.org/2025.acl-long.779.pdf), [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf), [Neuron Empirical Gradient: Discovering and Quantifying Neurons' Global Linear Controllability](https://aclanthology.org/2025.acl-long.1041.pdf), [Beemo: Benchmark of Expert-edited Machine-generated Outputs](https://aclanthology.org/2025.naacl-long.357.pdf), [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.320.pdf), [Is your benchmark truly adversarial? AdvScore: Evaluating Human-Grounded Adversarialness](https://aclanthology.org/2025.naacl-long.27.pdf))
> The observable task of verifying a queried fact against a provided knowledge base, such as a knowledge graph, and producing a binary response indicating its validity.

**Truthfulness prediction** (1 paper: [GameArena: Evaluating LLM Reasoning through Live Computer Games](https://proceedings.iclr.cc/paper_files/paper/2025/file/520416e27d3b0cef3cd70a083e2991c7-Paper-Conference.pdf))
> Predicting whether a human statement is true or false after questioning.

**Statement validation** (1 paper: [Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25n/zhou25n.pdf))
> Determining whether a given medical statement is true or false, requiring precise discrimination of knowledge without the aid of multiple-choice options.

**Legal fact verification** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> Selecting facts that can be logically inferred from evidence in a legal case.

**Table-based fact verification** (1 paper: [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf))
> The task of determining whether a given natural language statement is true or false based on the content of a provided table.

**Sub-claim verification** (1 paper: [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf))
> Evaluating the truthfulness of individual triplets or sub-claims by retrieving relevant documents and determining whether they support or refute the claim.

## Relationships

### Fact checking →
- **FEVER** (measurement instrument): *measured_by*, 10 papers
  > We use the FEVER (Thorne et al., 2018) dataset for all our experiments and comparison against previous methods. (Section 4.1)
  - [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
  - [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf)
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
  - [FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models](https://aclanthology.org/2025.naacl-long.534.pdf)
  - [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf)
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
  - [AgentPro: Enhancing LLM Agents with Automated Process Supervision](https://aclanthology.org/2025.emnlp-main.506.pdf)
  - [Adversarial Attacks Against Automated Fact-Checking: A Survey](https://aclanthology.org/2025.emnlp-main.1171.pdf)
- **FEVEROUS** (measurement instrument): *measured_by*, 6 papers
  > FEVEROUS, on the other hand, is a fact-verification dataset that requires the identification of multiple relevant tables for reasoning and verifying factual questions.
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
  - [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf)
  - [Refining Attention for Explainable and Noise-Robust Fact-Checking with Transformers](https://aclanthology.org/2025.emnlp-main.1295.pdf)
- **SciFact** (measurement instrument): *measured_by*, 5 papers
  > Besides, we also take into account the SCIFACT [26] dataset, notable for its inclusion of scientific claims (Section 4.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [CORRECT: Context- and Reference-Augmented Reasoning and Prompting for Fact-Checking](https://aclanthology.org/2025.naacl-long.154.pdf)
  - [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf)
  - [Refining Attention for Explainable and Noise-Robust Fact-Checking with Transformers](https://aclanthology.org/2025.emnlp-main.1295.pdf)
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
- **HoVer** (measurement instrument): *measured_by*, 4 papers
  > Claim Verification The task involves assessing a given claim against a set of evidence documents to determine whether they support or refute the claim [12]. We consider HOVER [24] and FEVEROUS [25]... (Section 4.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
  - [Grounding by Trying: LLMs with Reinforcement Learning-Enhanced Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/4169f1425b80c3a6e7daa84a1d09b077-Paper-Conference.pdf)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
  - [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf)
- **TabFact** (measurement instrument): *measured_by*, 4 papers
  > We evaluate our method on three datasets covering fact verification, short-form, and long-form question-answering tasks... (a) TabFact (Chen et al., 2019): A fact verification benchmark utilizing Wikipedia tables. (Section 3)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
  - [TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](https://aclanthology.org/2025.acl-long.1090.pdf)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
  - [Can GRPO Boost Complex Multimodal Table Understanding?](https://aclanthology.org/2025.emnlp-main.637.pdf)
- **Creak** (measurement instrument): *measured_by*, 3 papers
  > and one fact-checking dataset: Creak (Onoe et al., 2021).
  - [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf)
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **PubHealth** (measurement instrument): *measured_by*, 2 papers
  > PubHealth is a dataset of medical claims spanning a variety of biomedical subjects and it requires the RAG system to verify a given claim based on the retrieved documents. (Section 4)
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
  - [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf)
- **FM2** (measurement instrument): *measured_by*, 2 papers
  > We use four popular datasets for fact-checking: Feverous, AVeriTeC, FM2 and SciFact.
  - [Refining Attention for Explainable and Noise-Robust Fact-Checking with Transformers](https://aclanthology.org/2025.emnlp-main.1295.pdf)
  - [InfoGain-RAG: Boosting Retrieval-Augmented Generation through Document Information Gain-based Reranking and Filtering](https://aclanthology.org/2025.emnlp-main.365.pdf)
- **Climate-FEVER** (measurement instrument): *measured_by*, 2 papers
  > “Climate-FEVER (Diggelmann et al., 2021), Fact checking”
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
  - [Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision](https://aclanthology.org/2025.emnlp-main.1624.pdf)
- **FB15k-237** (measurement instrument): *measured_by*, 1 paper
  > We show that SFAVEL yields a significant improvement over prior state-of-the-art, both over unsupervised and supervised methods, on the FEVER fact verification challenge (+8% accuracy) and the FB15k-237 dataset (+5.3% Hits@1). (Section 5)
  - [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
- **CounterFact** (measurement instrument): *measured_by*, 1 paper
  > Counterfact Fact-Checking (Meng et al., 2022a) is a data set with factual statements consisting of a statement with corresponding fact.
  - [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate a biography-generation task (Min et al., 2023) and TruthfulQA (Lin et al., 2022) which is a benchmark for testing false beliefs or misconceptions. (Section 4.1, Fact verification)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
- **RTE** (measurement instrument): *measured_by*, 1 paper
  > "the RTE dataset [49], a classification task where the model is tasked to verify the correctness of statements"
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > LongBench (Bai et al., 2024): Focused on medium-context tasks (10K tokens), it assesses summarization, QA, and fact-checking across multiple domains...
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **LOFT** (measurement instrument): *measured_by*, 1 paper
  > “LOFT (7 retrieval tasks including argumentative retrieval, fact-checking, web search, multi-hop reasoning QA, etc)”
  - [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf)

### → Fact checking
- **Chain-of-thought reasoning** (construct): *causes*, 1 paper
  > we extend this by incorporating agent-based LLM, enabling iterative interactions with the knowledge base to resolve ambiguous entities and execute multi-step reasoning for more robust and in-depth claim verification. (Section 2)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > The model then performs reasoning over this combined information to predict the label Yp of the claim and generates a human-readable explanation Ye. (Section 3.4)
  - [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > the LLM world knowledge conversion produces hallucinatory evidence, directly impacting claim validation (Section 4.7)
  - [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf)

### Associated with
- **Information retrieval** (behavioral indicator), 2 papers
  > Most recent works typically divide the fact verification task into two stages. The first stage retrieves a relatively small subset of evidence from a knowledge source (e.g. a knowledge graph) that is relevant to verify a given claim. (Section 2)
  - [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf)
- **Interpretability and explainability** (construct), 2 papers
  > Claim verification is a long-standing and challenging task that demands not only high accuracy but also explainability of the verification process. (Abstract)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
  - [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf)
- **Multi-hop reasoning** (construct), 1 paper
  > ...we conduct experiments using Llama2-70B [2], GPT-3.5 [1], and GPT-4 [3] on various contextually aware multi-hop reasoning tasks, including claim verification [12], question answering [13], and reading comprehension [14] (Section 1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Understanding** (construct), 1 paper
  > Tasks at the Understanding level examine the ability to comprehend and interpret facts, entities, concepts, and relationships in legal texts... We construct five tasks at this level: ...Legal Fact Verification (2-2)... (Section C.3.2)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (construct), 1 paper
  > fact verification is one area in which assessing the robustness of models developed for this task is crucial. (Section 1)
  - [FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models](https://aclanthology.org/2025.naacl-long.534.pdf)
- **Misinformation detection** (behavioral indicator), 1 paper
  > Consequently, fact-checking based methods (Thorne and Vlachos, 2018; Nakov et al., 2021) have been the mainstream for fake news detection. (Section 1)
  - [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf)
- **Faithfulness** (construct), 1 paper
  > We consider the task of fact-checking claims against grounding documents, where the goal is to assess factual consistency based on provided textual evidence (Section 1).
  - [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf)
- **SAFE** (measurement instrument), 1 paper
  > ...and determining whether a fact is supported by the search results.
  - [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf)
- **Logical consistency** (construct), 1 paper
  > "We assess and improve the logical consistency of LLMs in propositional logic queries and logic rules, particularly in the context of fact-checking."
  - [Logical Consistency of Large Language Models in Fact-Checking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3209cf3312b2cbb68e33644362ddc2bd-Paper-Conference.pdf)
