# CounterFact
**Type:** Measurement instrument  
**Supporting papers:** 39  
**Also known as:** COUNTERFACT, Counterfact  

## State of the Field

**What it is.** Most commonly, papers treat CounterFact as a factual question-answering or prompt dataset for evaluating factual knowledge and knowledge editing. Definitions often describe samples as (subject, relation, answer) tuples with paraphrased prompts, while a recurring alternative framing emphasizes counterfactual statements, or false facts, used as new knowledge for editing; some descriptions also mention neighboring datapoints, rephrased or unrelated queries, and prompt pairs. Papers sometimes use task-specific subsets or reformulations, including the first 1000 examples, filtered fact pairs the model already recalls, a subset restricted to one relation with a fixed target label, question reformulations, and old versus new knowledge partitions.

**What it is claimed to measure.** Papers link CounterFact to 8 constructs and 3 behavioral indicators, so its reported measurement role is spread across several targets rather than concentrated on one. The prevailing usage is to measure knowledge editing, and recurring work also uses it to evaluate editing locality, factual recall, factual knowledge, and fact checking. Across these claims, papers describe it as testing whether models recover or replace specific facts, preserve neighborhood behavior, or generate text consistent with a new fact.

**Space of uses.** Most papers position CounterFact as a widely adopted benchmark in model editing work, most often used alongside ZsRE. Smaller lines of work also pair it with MQuAKE, Bias in Bios, and ConflictQA, and one related-instrument claim says BMIKE-53 is constructed from CounterFact and other monolingual knowledge-editing datasets. Beyond headline benchmark use, papers also adapt it for specific procedures, including causal tracing, prompt reformulation into questions, filtered recalled-fact subsets, and relation-restricted test sets.

**Concerns raised.** A smaller concern appears in work on context utilization, where CounterFact is grouped with artificial datasets that are said to often fail to represent the complexity and diversity of realistically retrieved context. Another paper notes that, in its CounterFact setup, the model relies on provided counterfactual context to answer a simple question correctly, and that the task does not require complex reasoning.

## Sources

**CounterFact** (9 papers: [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf), [Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks](https://proceedings.iclr.cc/paper_files/paper/2024/file/c652e5f62fd1f5acbbf0d6413a1113e7-Paper-Conference.pdf), [Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b99d6cc40b05809c3d84b57a165448cd-Paper-Conference.pdf), [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf), [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf), [AdaEdit: Advancing Continuous Knowledge Editing For Large Language Models](https://aclanthology.org/2025.acl-long.208.pdf), [Do LLMs dream of elephants (when told not to)? Latent concept association and associative memory in transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d3626b603cac298c9f7573b1df00cac-Paper-Conference.pdf), [Reasons and Solutions for the Decline in Model Performance after Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f588e59e9ae6138d3ea9e4fdaa7e040-Paper-Conference.pdf), [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf))
> Question-answering dataset used to evaluate a model's factual knowledge, consisting of (subject, relation, answer) tuples with paraphrased prompts, designed to test recovery of specific facts.

**COUNTERFACT** (5 papers: [Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching](https://proceedings.iclr.cc/paper_files/paper/2024/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf), [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf), [Has this Fact been Edited? Detecting Knowledge Edits in Language Models](https://aclanthology.org/2025.naacl-long.492.pdf), [How to Make LLMs Forget: On Reversing In-Context Knowledge Edits](https://aclanthology.org/2025.naacl-long.630.pdf), [GeoEdit: Geometric Knowledge Editing for Large Language Models](https://aclanthology.org/2025.emnlp-main.676.pdf))
> The COUNTERFACT dataset, a collection of factual prompt pairs used to evaluate factual recall and fact editing interventions.

**Counterfact** (3 papers: [Everything is Editable: Extend Knowledge Editing to Unstructured Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/02763667a5761ff92bb15d8751bcd223-Paper-Conference.pdf), [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf), [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf))
> A dataset used for evaluating knowledge editing on structured, counterfactual statements.

## Relationships

### → CounterFact
- **Knowledge editing** (behavioral indicator): *measured_by*, 4 papers
  > “We evaluate AlphaEdit using two widely adopted benchmarks: the Counterfact dataset (Meng et al., 2022) and the ZsRE dataset (Levy et al., 2017).”
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
  - [Dynamic Retriever for In-Context Knowledge Editing via Policy Optimization](https://aclanthology.org/2025.emnlp-main.848.pdf)
  - [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.327.pdf)
  - [Mechanistic Unlearning: Robust Knowledge Unlearning and Editing via Mechanistic Localization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25k/guo25k.pdf)
- **Editing locality** (construct): *measured_by*, 3 papers
  > In the Counterfact dataset, we evaluate the models on Efficacy, Generality, and Locality, using success rates as metrics. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)
  - [REACT: Representation Extraction And Controllable Tuning to Overcome Overfitting in LLM Knowledge Editing](https://aclanthology.org/2025.emnlp-main.860.pdf)
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Factual recall** (behavioral indicator): *measured_by*, 2 papers
  > We use the ﬁrst 1000 examples from the COUNTERFACT dataset (Meng et al., 2022a), and ﬁlter from them 40 pairs of facts across 8 relations that the model recalls correctly.
  - [Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching](https://proceedings.iclr.cc/paper_files/paper/2024/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf)
  - [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf)
- **Factual knowledge** (construct): *measured_by*, 2 papers
  > The CounterFact dataset is used to test the model’s factual knowledge of data from Wikipedia. (Section 5.1)
  - [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
- **Generality** (construct): *measured_by*, 1 paper
  > In the Counterfact dataset, we evaluate the models on Efficacy, Generality, and Locality, using success rates as metrics. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Reliability** (construct): *measured_by*, 1 paper
  > experiments on COUNTERFACT and MQuAKE shows that our method preserves balanced basic editing performance (reliability, locality, and generality) under diverse editing scenarios.
  - [REACT: Representation Extraction And Controllable Tuning to Overcome Overfitting in LLM Knowledge Editing](https://aclanthology.org/2025.emnlp-main.860.pdf)
- **Fact checking** (behavioral indicator): *measured_by*, 1 paper
  > Counterfact Fact-Checking (Meng et al., 2022a) is a data set with factual statements consisting of a statement with corresponding fact.
  - [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf)
- **Knowledge conflict resolution** (construct): *measured_by*, 1 paper
  > We evaluate the effectiveness of PASTA at ... (iii) resolving in-context knowledge conflicts. For (iii), we study ... CounterFact (Meng et al., 2022a).
  - [Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b99d6cc40b05809c3d84b57a165448cd-Paper-Conference.pdf)
- **Knowledge integration efficacy** (construct): *measured_by*, 1 paper
  > In the Counterfact dataset, we evaluate the models on Efficacy, Generality, and Locality, using success rates as metrics. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Context utilization** (construct): *measured_by*, 1 paper
  > We compare DRUID to synthetic datasets (CounterFact, ConflictQA) and find that artificial datasets often fail to represent the complexity and diversity of realistically retrieved context (Abstract).
  - [A Reality Check on Context Utilisation for Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.968.pdf)
- **Context faithfulness** (construct): *measured_by*, 1 paper
  > we also conduct experiments on the CounterFact dataset (Meng et al., 2022), where the model must rely on the provided counterfactual context to answer a simple question correctly. The task does not require complex reasoning, making it well-suited for isolating and evaluating the role of context-faithful experts. (Section 3.3)
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf)

### Associated with
- **BMIKE-53** (measurement instrument), 1 paper
  > BMIKE-53 is constructed from three monolingual KE datasets: zsRE, CounterFact, and WikiFactDiff
  - [BMIKE-53: Investigating Cross-Lingual Knowledge Editing with In-Context Learning](https://aclanthology.org/2025.acl-long.798.pdf)
