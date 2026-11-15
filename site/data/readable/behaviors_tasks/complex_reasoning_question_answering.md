# Complex reasoning question answering
**Type:** Behavioral indicator  
**Supporting papers:** 17  
**Also known as:** Reasoning question answering, Complex question answering, Complex reasoning, Multi-step problem solving, Complex reasoning task performance, Complex Reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this behavior as answering questions or solving structured problems that require more than simple recognition or a single memorized fact: papers repeatedly describe multi-step inference, synthesis of multiple pieces of information, comparisons, and detailed analysis. Several definitions keep it squarely in question answering, including multi-hop questions that require chaining facts together, chart questions that require synthesizing information across visual elements, and multimodal questions that go beyond description, while a smaller line of work frames the same behavior as multi-step problem solving, where success includes producing intermediate steps or giving a full answer rather than a simple one-word response.

**Variants.** Papers use several nearby names, most often complex question answering, reasoning question answering, complex reasoning, and multi-step problem solving. The behavior appears in multimodal settings such as image and chart understanding, including one formulation grounded in fMRI-based visual context, and in text settings such as open-domain multi-hop QA, knowledge graph question answering, mathematical word problems, domain-specific or professional queries, and social media analysis that emphasizes evidence selection and justification.

**Space of elicitation and scores.** Papers link this behavior to 6 measurement instruments. The most frequently linked is LLaVA-Bench-in-the-Wild, a multimodal benchmark with conversation, detailed description, and complex reasoning questions; other frequently used instruments are GSM8K, CharXiv, HotpotQA, and MMLU, plus 1 other instrument. Taken together, these instruments operationalize the behavior through image-based QA, chart reasoning, multi-hop question answering, and benchmarked reasoning tasks over subject areas or problem sets.

**What it is taken as evidence of.** Construct links are sparse. Papers link it to 1 construct, Long-context understanding, and the recorded claim is that this behavior is related to that construct rather than explicitly treated as measuring it, so the papers does not show a broader shared construct framing beyond that relation. Separately, one paper claims a causal relationship from Tool use to this behavior, describing tools as enabling complex tasks like multi-step problem-solving and retrieval for complex question answering.

## Sources

**Complex reasoning question answering** (1 paper: [Neuro-Vision to Language: Enhancing Brain Recording-based Visual Reconstruction and Language Interaction](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1c62bdeee97b38c34dcda152c829511-Paper-Conference.pdf))
> The task of answering questions that require inference and deep understanding of a visual scene, based on fMRI data as context.

**Reasoning question answering** (2 papers: [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf), [MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mencattini25a/mencattini25a.pdf))
> The task of answering questions that require complex cognitive operations, such as synthesizing information across different parts of a chart, making comparisons, or performing fine-grained analysis.

**Complex question answering** (6 papers: [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf), [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf), [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf), [From Complex to Atomic: Enhancing Augmented Generation via Knowledge-Aware Dual Rewriting and Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ac/wang25ac.pdf), [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf), [SUNAR: Semantic Uncertainty based Neighborhood Aware Retrieval for Complex QA](https://aclanthology.org/2025.naacl-long.300.pdf))
> The task of answering questions that require more than simple object recognition, often involving reasoning or synthesis of multiple pieces of information.

**Complex reasoning** (3 papers: [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf), [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf), [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf))
> The ability to perform sophisticated logical and inferential thinking to solve complex problems.

**Multi-step problem solving** (2 papers: [Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf), [We-Math: Does Your Large Multimodal Model Achieve Human-like Mathematical Reasoning?](https://aclanthology.org/2025.acl-long.983.pdf))
> The observable behavior of generating a sequence of intermediate steps to arrive at a solution for a complex problem.

**Complex reasoning task performance** (1 paper: [Personality Alignment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/25203d1cc8c58381eab578f4fcf9c4f8-Paper-Conference.pdf))
> The observable behavior of solving structured problems that require multi-step logical, mathematical, or commonsense reasoning, as measured by performance on specific benchmarks.

**Complex Reasoning** (1 paper: [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf))
> The task of solving questions that require multi-step logical inference or detailed analysis.

## Relationships

### Complex reasoning question answering →
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 3 papers
  > LLaVA-Bench serves as a general benchmark for systematic comprehension, encompassing three categories: conversation, detailed description, and complex questions. (Section 4.2)
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 2 papers
  > Furthermore, G2IS demonstrates significant improvements on complex reasoning tasks like GSM8K and BBH, showcasing the advantages of using a gradient-based graph structure to jointly model instruction tuning data, leading to better performance on complex tasks. (Section 4.2)
  - [Beyond Similarity: A Gradient-based Graph Method for Instruction Tuning Data Selection](https://aclanthology.org/2025.acl-long.1189.pdf)
  - [Lexico: Extreme KV Cache Compression via Sparse Coding over Universal Dictionaries](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25ae/kim25ae.pdf)
- **CharXiv** (measurement instrument): *measured_by*, 1 paper
  > CharXiv includes two types of questions: ... 2) reasoning questions that require synthesizing information across complex visual elements
  - [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > MMLU (Hendrycks et al., 2020) complex question answering dataset of multiple choice questions spanning many domains and is used to test LM question-answering across a wide range of subjects. (Section 3)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > HotpotQA (Yang et al., 2018) is a complex question answering dataset of multi-hop reasoning questions which cannot be answered by a single memorized fact, but instead require chaining facts together. (Section 3)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 1 paper
  > Additionally, we evaluate generative performance on complex reasoning tasks, such as GSM8K (Cobbe et al., 2021) with 5-shot prompting and MMLU-Pro Engineering/Law (Wang et al., 2024a) with zero-shot chain-of-thought.
  - [Lexico: Extreme KV Cache Compression via Sparse Coding over Universal Dictionaries](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25ae/kim25ae.pdf)

### → Complex reasoning question answering
- **Tool use** (behavioral indicator): *causes*, 1 paper
  > These tools enable agents to perform complex tasks like multi-step problem-solving and retrieving diverse information, which is essential for complex retrieval and question-answering (QA) (Section 1).
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)

### Associated with
- **Long-context understanding** (construct), 1 paper
  > Large language models (LLMs) have advanced to support long-context tasks such as document understanding (Li et al., 2024a), multi-turn dialogues (Yi et al., 2024), repository-level code completion (Jimenez et al., 2024), and complex reasoning (Zhou et al., 2025).
  - [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf)
