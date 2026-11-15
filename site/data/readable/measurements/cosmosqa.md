# CosmosQA
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** Cosmos QA  

## State of the Field

**What it is.** Across papers, CosmosQA is most commonly described as a large-scale commonsense-based reading comprehension benchmark or dataset, usually framed as multiple-choice question answering. Definitions consistently say its passages and questions require commonsense reasoning, while some descriptions are more specific, presenting it as common-sense questions about human behaviors, intentions, and social interactions with four answer options each, and another places it among real-world NLP classification datasets.

**What it is claimed to measure.** The prevailing usage is as a measure of commonsense reasoning: papers link it to 1 construct, Commonsense reasoning, and 1 behavioral indicator, Question answering. Most measurement claims treat it as evaluating commonsense reasoning, including work that explicitly labels it a common sense reasoning dataset, while a smaller line of work reports it as measuring question answering by listing it among question answering datasets. Overall, the claims center on a single construct and a single behavioral indicator rather than spreading across many targets.

**Space of uses.** No paper links it to another measurement instrument. Papers usually position it as one dataset within broader evaluation suites, for example alongside BoolQ and SciQ in NLP classification settings, or with Social IQA and QuAIL in question answering setups; other work uses it in mixed reasoning evaluations that also include medical and math datasets. Some papers also describe it as a testbed for weak-to-strong generalization, out-of-distribution generalization, or the impact of fine-tuning on chain-of-thought reasoning.

## Sources

**CosmosQA** (3 papers: [Relating Misfit to Gain in Weak-to-Strong Generalization Beyond the Squared Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mulgund25a/mulgund25a.pdf), [Persona-Augmented Benchmarking: Evaluating LLMs Across Diverse Writing Styles](https://aclanthology.org/2025.emnlp-main.1155.pdf), [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.584.pdf))
> A large-scale dataset of commonsense-based reading comprehension questions, used to evaluate NLP classification performance.

**Cosmos QA** (3 papers: [Representations Shape Weak-to-Strong Generalization: Theoretical Insights and Empirical Predictions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xue25d/xue25d.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf), [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf))
> Reading comprehension dataset involving commonsense reasoning, used to evaluate W2SG in narrative understanding and inference.

## Relationships

### → CosmosQA
- **Commonsense reasoning** (construct): *measured_by*, 2 papers
  > Common sense Q&A (CosmosQA) (Huang et al., 2019): Common sense questions ... to demonstrate how common sense reasoning is affected by writing style.
  - [Persona-Augmented Benchmarking: Evaluating LLMs Across Diverse Writing Styles](https://aclanthology.org/2025.emnlp-main.1155.pdf)
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.584.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > These datasets encompass diverse tasks, covering three Question Answering datasets: Huang et al.’s (2019) Cosmos QA, Sap et al.’s (2019) Social IQA, and Rogers et al.’s (2020) QuAIL; (Section 5.2)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
