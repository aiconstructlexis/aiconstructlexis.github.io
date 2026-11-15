# Consistency
**Type:** Construct  
**Supporting papers:** 85  
**Also known as:** Robustness to prompt variations, Self-consistency, Self-Consistency, Answer consistency, Output consistency, Performance consistency, Prediction consistency, Conceptual incoherence, Process consistency  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage describes consistency as stability or non-contradiction in outputs or decisions: models give the same or similar answers across paraphrased or semantically equivalent prompts, repeated identical prompts, reordered comparisons, multiple reasoning paths, or repeated task trials. Several definitions make this concrete as similar predicted class distributions under rephrasings, the same successful outcome across independent attempts, or matching predictions across inference passes. A smaller but recurring usage treats consistency as semantic alignment or coherence between paired items, such as finetuning and target-task data, rationales and gold labels, language and visual plans, ad text and landing pages, generated text and its input source, or all sentences in a text being jointly true in one world; a further minority framing moves inward, defining self-consistency as non-contradictory internal beliefs or, inversely, inconsistency as conflicting concept representations.

**Space of facets.** Papers subdivide the construct into self-consistency, answer consistency, output consistency, prediction consistency, performance consistency, and process consistency. These variants place it at different levels: agreement across paraphrases or logical relations, agreement among sampled reasoning paths, repeatability under identical prompts, stability across fine-tuned variants, reliable success across attempts, and coherence between an agent's stated explanations and its underlying reasoning process. Some papers also blur neighboring labels, treating robustness to prompt variations as part of self-consistency, noting that implication self-consistency is sometimes called just consistency, embedding a consistency condition inside coherence assessment, or arguing that measures called faithfulness are often measuring self-consistency.

**Space of measurement.** Papers link consistency to 1 measurement instrument, Human evaluation, and to 4 behavioral indicators, Hallucination, Information retrieval, Natural language inference, and Text classification. Beyond that linked instrument, operationalizations are mostly repeated-run or agreement analyses, such as pair-wise classifier consistency across prompt rephrasings, repeated identical-prompt trials, matching predictions across two inference passes, multi-trial agent success, and agreement of final answers across sampled reasoning paths; LLM-as-a-judge style evaluations also check whether the same comparison gets the same judgment when response order changes. Other papers score alignment between an output and a reference, such as gold labels, input sources, landing pages, or documents, so operationalization follows the same split seen in the definitions between repeatability and semantic coherence.

**Links.** Single papers make directional claims from and to the construct. One paper claims a causal relationship from Consistency to Generalization, another from Consistency to Information retrieval, and another from Logical reasoning to Consistency; one paper also reports that Consistency correlates with Hallucination. Related links are broader but individually sparse: papers also relate it to Agency, along with several other constructs and behavioral indicators.

## Sources

**Consistency** (18 papers: [BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf), [Generative Judge for Evaluating Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/747dc7c6566c74eb9a663bcd8d057c78-Paper-Conference.pdf), [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf), [Tailoring Self-Rationalizers with Multi-Reward Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf), [Towards Few-Shot Adaptation of Foundation Models via Multitask Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d9a0718883f4a2eecee3c69c7213b05-Paper-Conference.pdf), [PERIA: Perceive, Reason, Imagine, Act via Holistic Language and Vision Planning for Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6af963e891e7efa229c24a1607fa7f-Paper-Conference.pdf), [{$\tau$}-bench: A Benchmark for \underline{T}ool-\underline{A}gent-\underline{U}ser Interaction in Real-World Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b126cc38b8638e07bef37e7b2bb72bf-Paper-Conference.pdf), [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf), [CRMArena: Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks in Realistic Environments](https://aclanthology.org/2025.naacl-long.194.pdf), [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf), [CharacterBox: Evaluating the Role-Playing Capabilities of LLMs in Text-Based Virtual Worlds](https://aclanthology.org/2025.naacl-long.323.pdf), [AdTEC: A Unified Benchmark for Evaluating Text Quality in Search Engine Advertising](https://aclanthology.org/2025.naacl-long.391.pdf), [SylloBio-NLI: Evaluating Large Language Models on Biomedical Syllogistic Reasoning](https://aclanthology.org/2025.naacl-long.371.pdf), [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf), [A Novel Computational Modeling Foundation for Automatic Coherence Assessment](https://aclanthology.org/2025.naacl-long.277.pdf), [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf), [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf), [Think Wider, Detect Sharper: Reinforced Reference Coverage for Document-Level Self-Contradiction Detection](https://aclanthology.org/2025.emnlp-main.67.pdf))
> The similarity between the data distributions of the finetuning tasks and the target task, reflecting how closely the auxiliary tasks align with the objective of the target task in the latent space.

**Self-consistency** (2 papers: [Waste Not, Want Not; Recycled Gumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.292.pdf), [Robust Native Language Identification through Agentic Decomposition](https://aclanthology.org/2025.emnlp-main.423.pdf))
> The ability of a language model to maintain coherent and non-contradictory responses when presented with paraphrased or semantically equivalent prompts.

**Robustness to prompt variations** (1 paper: [Waste Not, Want Not; Recycled Gumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.292.pdf))
> The stability of model responses when the same question is reworded or paraphrased.

**Self-Consistency** (1 paper: [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf))
> The property of the model's internal beliefs not contradicting each other across different prompts or logical relations.

**Answer consistency** (2 papers: [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.247.pdf), [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf))
> The extent to which multiple sampled reasoning paths yield the same final answer, serving as an indicator of confidence in the output.

**Output consistency** (1 paper: [Investigating Value-Reasoning Reliability in Small Large Language Models](https://aclanthology.org/2025.emnlp-main.395.pdf))
> The degree to which a model produces the same output when presented with identical prompts multiple times.

**Prediction consistency** (1 paper: [Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hamman25a/hamman25a.pdf))
> The degree to which a model's prediction for a given input remains stable across multiple fine-tuned variants of the same pre-trained model under minor training variations.

**Conceptual incoherence** (1 paper: [Potemkin Understanding in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mancoridis25a/mancoridis25a.pdf))
> A state where a model holds conflicting or inconsistent internal representations of the same concept, leading it to contradict its own generations or classifications.

**Performance consistency** (1 paper: [Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zainullina25a/zainullina25a.pdf))
> The degree to which an LLM agent maintains reliable success across multiple attempts at complex, multi-step tasks, minimizing variance between average-case and best-case outcomes.

**Process consistency** (1 paper: [Position: Theory of Mind Benchmarks are Broken for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/riemer25a/riemer25a.pdf))
> The degree to which an agent's internal reasoning process remains coherent and aligned across different questions or steps in a task, particularly in how predictions inform actions.

## Relationships

### Consistency →
- **Generalization** (construct): *causes*, 1 paper
  > “Besides small finetuning loss on sufficiently many data, a large diversity parameter ν and a small consistency parameter κ will result in a small target error bound.”
  - [Towards Few-Shot Adaptation of Foundation Models via Multitask Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d9a0718883f4a2eecee3c69c7213b05-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator): *causes*, 1 paper
  > By explicitly modeling both consistency and relevance, our method trains a retriever to retrieve the documents necessary for answering a given question. (Section 3.2)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > Human evaluation results on consistency and coherence among the sentiment of user profiles. (Table 2)
  - [Exploring Persona Sentiment Sensitivity in Personalized Dialogue Generation](https://aclanthology.org/2025.acl-long.900.pdf)
- **Hallucination** (behavioral indicator): *correlates*, 1 paper
  > smaller attentive consistency scores and larger non-attentive consistency scores indicate greater probabilities of hallucinations.
  - [Attention-guided Self-reflection for Zero-shot Hallucination Detection in Large Language Models](https://aclanthology.org/2025.emnlp-main.1063.pdf)

### → Consistency
- **Logical reasoning** (construct): *causes*, 1 paper
  > the deductive reasoning process improves consistency by producing consistent solutions using a given strategy (Introduction).
  - [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)

### Associated with
- **In-context learning** (construct), 1 paper
  > Besides confirming the existence of ICL ability, we are particularly interested in ... determining if our trained models demonstrate consistency, i.e., whether their performance converges in probability to some ceiling.
  - [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf)
- **Robustness** (construct), 1 paper
  > Our hope is that sensitivity and consistency will be helpful to guide prompt engineering and obtain LLMs that balance robustness with performance. (Abstract)
  - [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Persona consistency** (construct), 1 paper
  > Consistency emphasizes the importance of maintaining logical continuity in a character’s behavioral patterns across all interactions... ‚ Behavioral Coherence (BC): Evaluates the logical consistency of character’s actions in relation to previous behaviors and current context.
  - [CharacterBox: Evaluating the Role-Playing Capabilities of LLMs in Text-Based Virtual Worlds](https://aclanthology.org/2025.naacl-long.323.pdf)
- **Relevance** (construct), 1 paper
  > While the answer probability by itself seemed ineffective, its combination with the question probability becomes powerful, as it evaluates the consistency among relevant documents, with irrelevant ones already filtered out due to their low question probabilities. (Section 4.2.2)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
- **Agency** (construct), 1 paper
  > when it comes to tasks requiring heavy reasoning or agentic capabilities, a major challenge persists: while the models occasionally achieve exceptional results, their average performance often falls short of their demonstrated potential. (Section 1)
  - [Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zainullina25a/zainullina25a.pdf)
- **Value-reasoning reliability** (construct), 1 paper
  > We define Value-Reasoning Reliability as comprising: (1) Output consistency under identical prompts...
  - [Investigating Value-Reasoning Reliability in Small Large Language Models](https://aclanthology.org/2025.emnlp-main.395.pdf)
- **Text classification** (behavioral indicator), 1 paper
  > We therefore introduce two metrics for classification tasks, namely sensitivity and consistency, which are complementary to task performance. (Abstract)
  - [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Natural language inference** (behavioral indicator), 1 paper
  > “NLI evaluates NLP models’ ability to capture logical relationships between sentences, serving as a proxy for the consistency condition.”
  - [A Novel Computational Modeling Foundation for Automatic Coherence Assessment](https://aclanthology.org/2025.naacl-long.277.pdf)
- **Stability** (construct), 1 paper
  > Our objective is to define a measure, denoted as S(x, f), for an input x and a given fine-tuned model f, that would preemptively quantify the consistency of the prediction ˆf(x) over a broad class of equally-well-performing fine-tuned models. (Section 3)
  - [Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hamman25a/hamman25a.pdf)
- **Predictive uncertainty** (construct), 1 paper
  > “To evaluate the uncertainty of a model’s responses, a common approach is to calculate the most frequent response from multiple outputs generated by the model across multiple runs. This method quantifies the model’s prediction uncertainty using a metric known as the consistency rate (CR)”
  - [Exploring Response Uncertainty in MLLMs: An Empirical Evaluation under Misleading Scenarios](https://aclanthology.org/2025.emnlp-main.916.pdf)
