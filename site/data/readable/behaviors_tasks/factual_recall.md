# Factual recall
**Type:** Behavioral indicator  
**Supporting papers:** 62  
**Also known as:** Knowledge recall, Paraphrased factual recall, Factual knowledge retrieval, Event recall, Fact recall, Bridge entity recall, Fact retrieval, Fact recalling, Memory recall, Inverse search, Forward search, Answer extraction, Factual prediction, Long-term knowledge recall, Single-hop factual recall, Factual probing, Relation prediction, Knowledge retrieval  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats factual recall as retrieving or generating the correct fact from a subject-relation prompt or direct question, often as completing a subject-relation-object triple or next-token continuation such as 'The Eiffel Tower is in' with the correct object. Many papers frame the fact as stored in model parameters or pretraining data and not supplied by the current context, for example recalling capitals, birth years, birthdays, GDP, or other attribute values. Success is usually the correct object, tail entity, answer token, or short answer against a gold answer, though some papers count a predicted prefix of the object as correct, and one long-form usage defines recall as the percentage of provided facts among all relevant supported facts in a response.

**Variants.** Papers study nearby variants under names including knowledge recall, fact retrieval, factual knowledge retrieval, long-term knowledge recall, relation prediction, knowledge retrieval, and factual probing. The most common variants remain single-hop factual questions or templated triple completion, but authors also examine paraphrased prompts for edited facts, direct questions over country capitals or numerical attributes, and tail-entity completion from relation-specific templates. Smaller lines of work treat recall as event recall from a narrative, bridge-entity recall as an intermediate step in multi-hop questions, forward versus inverse search from attributes, answer extraction when the correct answer replaces a propagated relation token, or recall of previously learned knowledge after editing or unlearning.

**Space of elicitation and scores.** Papers measure factual recall with 7 instruments, most often TriviaQA, CounterFact, MMLU, Natural Questions, and WebQuestions. These are mostly QA or benchmark settings: some papers describe TriviaQA and Natural Questions as factual recall without complex reasoning, another groups TriviaQA, WebQuestions, and CounterFact as open-ended recall-intensive datasets, and MMLU appears as a general fact recall benchmark.

**What it is taken as evidence of.** Papers link factual recall to 6 constructs, and they do not converge on a single construct it reflects. The most prevalent linkage is that it is related to knowledge manipulation, with papers placing knowledge recall, reasoning, and transfer under that umbrella or listing retrieval and inverse search among knowledge manipulations. Elsewhere, papers report that it correlates with factuality and is related to in-context learning, in-context reasoning, memorization, and other constructs.

## Sources

**Paraphrased factual recall** (1 paper: [Revealing and Mitigating Over-Attention in Knowledge Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/35cb54b887e7aafe74829677cce6c5c6-Paper-Conference.pdf))
> The task of predicting the correct edited object when the prompt is a paraphrase of the original subject and relation, used to test generalization.

**Factual recall** (5 papers: [Revealing and Mitigating Over-Attention in Knowledge Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/35cb54b887e7aafe74829677cce6c5c6-Paper-Conference.pdf), [When Long Helps Short: How Context Length in Supervised Fine-tuning Affects Behavior of Large Language Models](https://aclanthology.org/2025.emnlp-main.522.pdf), [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf), [Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching](https://proceedings.iclr.cc/paper_files/paper/2024/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf), [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf))
> Predicting the object of a factual association from a prompt containing the subject and relation.

**Knowledge recall** (1 paper: [Towards Effective Evaluations and Comparisons for LLM Unlearning Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/3a91841d2bcc0b13a3d0d5d60c9f0581-Paper-Conference.pdf))
> Reproducing targeted information or outputs that were previously learned, especially after unlearning or under attack.

**Factual knowledge retrieval** (3 papers: [Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/26d3c9a66836ded8f34a944f2bfe868e-Paper-Conference.pdf), [On Relation-Specific Neurons in Large Language Models](https://aclanthology.org/2025.emnlp-main.52.pdf), [Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf))
> The observable task of generating a specific value (e.g., a birth date) when prompted with a subject name and an attribute (e.g., 'birthday').

**Event recall** (1 paper: [Episodic Memories Generation and Evaluation Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ff013b7e372ba5b790352ccd6908f03-Paper-Conference.pdf))
> The observable action of retrieving specific event details from a provided narrative context.

**Fact recall** (2 papers: [Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa27ac7aca4e462da1439b43ceebc04c-Paper-Conference.pdf), [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf))
> The behavior of retrieving and stating factual information stored in the model's parameters, often without reliance on a provided context.

**Bridge entity recall** (1 paper: [Unveiling Internal Reasoning Modes in LLMs: A Deep Dive into Latent Reasoning vs. Factual Shortcuts with Attribute Rate Ratio](https://aclanthology.org/2025.emnlp-main.111.pdf))
> The observable generation or internal activation of an intermediate entity (e.g., 'France') that connects two relational hops in a multi-hop question.

**Fact retrieval** (1 paper: [Do LLMs dream of elephants (when told not to)? Latent concept association and associative memory in transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d3626b603cac298c9f7573b1df00cac-Paper-Conference.pdf))
> Predicting a factual next token or answer from a context that encodes a known fact.

**Fact recalling** (1 paper: [Delving into the Reversal Curse: How Far Can Large Language Models Generalize?](https://proceedings.neurips.cc/paper_files/paper/2024/file/36b6180f3dab4025ba763e853b044814-Paper-Conference.pdf))
> The observable process of retrieving and articulating a relevant fact from memory in response to a query, often as an intermediate step in problem-solving.

**Memory recall** (1 paper: [Do LLMs dream of elephants (when told not to)? Latent concept association and associative memory in transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d3626b603cac298c9f7573b1df00cac-Paper-Conference.pdf))
> Retrieving an output token from a context distribution in the synthetic latent concept association setting.

**Inverse search** (1 paper: [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf))
> Identifying an entity from its attributes when the knowledge was presented only in the forward direction during training.

**Forward search** (1 paper: [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf))
> The observable task of retrieving information that sequentially follows a given piece of information, used as a baseline to contrast with inverse search.

**Answer extraction** (1 paper: [Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline](https://aclanthology.org/2025.emnlp-main.762.pdf))
> Replacing the propagated relation token with the correct factual answer token in the final prediction sequence.

**Factual prediction** (1 paper: [Scalable Influence and Fact Tracing for Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/65798a76cc176c29b6bfefe84b0a03ff-Paper-Conference.pdf))
> The task of completing a natural language prompt with a specific factual entity, such as filling in the object of a subject-relation pair.

**Long-term knowledge recall** (1 paper: [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf))
> The latent ability to access and retrieve stored factual knowledge about the world, such as historical, scientific, or geographical facts, independent of the current context.

**Single-hop factual recall** (1 paper: [Locate-then-edit for Multi-hop Factual Recall under Knowledge Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aq/zhang25aq.pdf))
> Correctly answering a direct factual question where the subject is explicitly stated and only one fact needs to be retrieved.

**Factual probing** (1 paper: [Zero-Shot Continuous Prompt Transfer: Generalizing Task Semantics Across Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/05f0734db34deb367fc66f1482528044-Paper-Conference.pdf))
> The task of predicting a correct entity (object) from a model's vocabulary, given a subject and a relation, to test the model's stored factual knowledge.

**Relation prediction** (1 paper: [Linearity of Relation Decoding in Transformer Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b6d7285306fe896fca9b2e9a02ff6ec-Paper-Conference.pdf))
> The observable behavior of generating the correct object token (e.g., 'trumpet') when prompted with a subject and relation (e.g., 'Miles Davis plays the'), reflecting the model's ability to retrieve and express relational knowledge.

**Knowledge retrieval** (4 papers: [Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25af/huang25af.pdf), [M+: Extending MemoryLLM with Scalable Long-Term Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25au/wang25au.pdf), [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf))
> Recalling factual knowledge not present in the input context, such as general world knowledge, to answer a question correctly.

## Relationships

### Factual recall →
- **TriviaQA** (measurement instrument): *measured_by*, 3 papers
  > We plot the accuracy versus sparsity for the OPT-13B, OPT-30B, LLaMA-13B, and LLaMA-33B models on TriviaQA dataset for fact recall evaluation (left).
  - [The Cost of Scaling Down Large Language Models: Reducing Model Size Affects Memory before In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/bb68f698772f14b6d8eaef4529fb9176-Paper-Conference.pdf)
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
  - [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf)
- **CounterFact** (measurement instrument): *measured_by*, 2 papers
  > We use the ﬁrst 1000 examples from the COUNTERFACT dataset (Meng et al., 2022a), and ﬁlter from them 40 pairs of facts across 8 relations that the model recalls correctly.
  - [Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching](https://proceedings.iclr.cc/paper_files/paper/2024/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf)
  - [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf)
- **WebQuestions** (measurement instrument): *measured_by*, 2 papers
  > (f) fact recall (WebQuestions (Berant et al., 2013), Natural Questions (Kwiatkowski et al., 2019)) (Section 4.2)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 2 papers
  > (f) fact recall (WebQuestions (Berant et al., 2013), Natural Questions (Kwiatkowski et al., 2019)) (Section 4.2)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 2 papers
  > We track the progress of IFT based on the performance on four standard benchmarks: ... MMLU (Hendrycks et al., 2021) (general fact recall)... (Section 3.1)
  - [Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa27ac7aca4e462da1439b43ceebc04c-Paper-Conference.pdf)
  - [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf)
- **Factuality** (construct): *correlates*, 1 paper
  > Our results show a large increase in factual precision of IDK-tuned models while causing only a small decrease in recall of factual knowledge
  - [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the fact recall ability of the adapted model, we use two question answering (QA) datasets, SQuAD (Rajpurkar et al., 2016) and StreamingQA (Liska et al., 2022)... (Section 4.1)
  - [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf)
- **ARC** (measurement instrument): *measured_by*, 1 paper
  > All of the datasets studied, with the partial exception of MMLU (Hendrycks et al., 2021b), are “recall-intensive” in that they largely depend on recalling factual information learned during training; we studied both multiple-choice datasets (MMLU, ARC (Clark et al., 2018)1) and open-ended ones (TriviaQA (Joshi et al., 2017), WebQuestions (Berant et al., 2013), CounterFact (Meng et al., 2022)). (Section 3)
  - [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf)

### Associated with
- **Knowledge manipulation** (construct), 2 papers
  > enhance the knowledge manipulation (e.g., knowledge recall, reasoning, and transfer) ability of LLMs. (Section 1)
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)
  - [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf)
- **Memorization** (construct), 1 paper
  > a model’s ability to recall memorized facts from its pretraining data deteriorates faster than its ability to recognize structured patterns as we decrease the size of the model through compression, distinguishing between compressible tasks where generalization is possible and incompressible tasks that correspond to sheer memorization. (Section 1)
  - [Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/11715d433f6f8b9106baae0df023deb3-Paper-Conference.pdf)
- **Reversal curse** (construct), 1 paper
  > ...when trained on “A → B” (e.g., Tom is the parent of John), LLM fails to directly conclude “B ← A” (e.g., John is the child of Tom) during inference even if the two sentences are semantically identical, which is known as the “reversal curse”. (Abstract)
  - [Towards a Theoretical Understanding of the 'Reversal Curse' via Training Dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4b95476f673e6e538f80862f622ba2f-Paper-Conference.pdf)
- **In-context reasoning** (construct), 1 paper
  > Under this definition, we list a few simple examples of reasoning that we will consider below: ... • Factual recall (Section 2.1).
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator), 1 paper
  > The two-stage theory states that the process of memory recall begins with a search and retrieval process, and then a decision or recognition process where the correct information is chosen from what has been retrieved (Bahrick, 1970; Watkins and Gardiner, 1979). (Section 2.1)
  - [MADial-Bench: Towards Real-world Evaluation of Memory-Augmented Dialogue Generation](https://aclanthology.org/2025.naacl-long.499.pdf)
- **In-context learning** (construct), 1 paper
  > While fact recall begins to significantly degrade when more than 30% of weights are removed through pruning, in-context learning capabilities show remarkable resilience, maintaining performance even with aggressive pruning of up to 60-70% of weights. (Section 5.1)
  - [Position: Enough of Scaling LLMs! Lets Focus on Downscaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25c/goel25c.pdf)
- **Knowledge generation** (behavioral indicator), 1 paper
  > Knowledge recall: Generated knowledge prompting (Liu et al., 2022) asks the model to recall or synthesize relevant knowledge before answering, simulating a form of self-retrieval and improving performance on commonsense benchmarks. (Section 2)
  - [Prior Prompt Engineering for Reinforcement Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1590.pdf)
