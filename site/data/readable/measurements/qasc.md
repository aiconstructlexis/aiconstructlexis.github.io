# QASC
**Type:** Measurement instrument  
**Supporting papers:** 17  

## State of the Field

**What it is.** Across papers, the prevailing description treats QASC as a question-answering benchmark or dataset for science questions that require multi-step or multi-hop reasoning, often by integrating, composing, or reasoning over multiple facts from multiple sentences. Some authors instead place it under commonsense reasoning or multiple-choice comprehension, one definition says it provides questions and associated facts, and another expands the name as "Question Answering via Sentence Composition". A smaller line of work also presents it as an elementary science or scientific reasoning benchmark.

**What it is claimed to measure.** Papers link QASC to 1 construct and 1 behavioral indicator. The prevailing measurement claim is that it measures Question answering, with papers using it for evaluation or fine-tuning under that label; a smaller line of work reports it as measuring Commonsense reasoning by including it among commonsense QA datasets. The reported measurement uses are therefore concentrated on those two targets rather than spread across many constructs or indicators.

**Space of uses.** Papers commonly present QASC as one dataset in broader evaluation suites. It is often used alongside StrategyQA and OpenBookQA or OBQA, and in some cases with CommonsenseQA or CSQA, WikiQA, and QuaRTz, with several other QA datasets appearing in particular studies. Beyond general question answering, papers also place it in scientific reasoning, cross-lingual transfer, model merging, process reward modeling, and forgetting experiments.

## Sources

**QASC** (13 papers: [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf), [Tailoring Self-Rationalizers with Multi-Reward Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf), [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf), [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf), [Dynamic and Generalizable Process Reward Modeling](https://aclanthology.org/2025.acl-long.212.pdf), [Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1203.pdf), [Graceful Forgetting in Generative Language Models](https://aclanthology.org/2025.emnlp-main.666.pdf), [Mitigating Catastrophic Forgetting in Large Language Models with Forgetting-aware Pruning](https://aclanthology.org/2025.emnlp-main.1108.pdf), [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1236.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf), [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf), [Why and How LLMs Benefit from Knowledge Introspection in Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.352.pdf))
> Question-answering dataset requiring multi-step reasoning and integration of scientific facts from multiple sentences.

## Relationships

### → QASC
- **Question answering** (behavioral indicator): *measured_by*, 4 papers
  > In question answering, we adopt the test splits of ECQA (Aggarwal et al., 2021), QASC (Khot et al., 2020), OpenbookQA (Mihaylov et al., 2018), and StrategyQA (Geva et al., 2021) for evaluation. (Section 4)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > we evaluate on eight widely utilized commonsense QA datasets: CommonsenseQA (Talmor et al., 2019), OpenBookQA (Mihaylov et al., 2018), ARC-Easy and ARC-Challenge (Clark et al., 2018), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2020), CommonsenseQA 2.0 (Talmor et al., 2021), and QASC (Khot et al., 2020). (Section 4.2)
  - [Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
