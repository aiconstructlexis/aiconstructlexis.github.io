# Chain-of-thought reasoning
**Type:** Construct  
**Supporting papers:** 243  
**Also known as:** Chain-of-Thought reasoning, Chain-of-reasoning, Thought chain reasoning, Chain-of-Thought ability, Chain-of-thought capability, Internal chain-of-thought, Multistep reasoning, Step-by-step thinking, Procedural reasoning, Thinking, Multi-turn reasoning, Multi-step reasoning, Subtask execution, Sequential inference, Step-wise reasoning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats chain-of-thought reasoning as step-by-step or multi-step problem solving, where a model reaches a final answer through intermediate logical steps. Most definitions stay close to this framing, whether phrased as chain-of-reasoning, multistep reasoning, step-by-step thinking, or procedural reasoning. The main axis of variation is latent capacity versus observable process: some authors define it through explicit intermediate text or structured reasoning traces before the answer, while others describe internal decomposition and planning that may remain unspoken. A smaller line extends the idea to multi-turn settings, and one paper defines it through responsiveness to explicit CoT prompting and reports no evidence of benefit for time series analysis.

**Space of facets.** Papers systematize the concept mostly by grouping together near-synonyms rather than by giving a fixed taxonomy. Common neighboring labels include multi-step, step-wise, sequential, and procedural reasoning, all centered on decomposing a task into intermediate steps, and some work narrows this further to sub-question decomposition or iterative refinement of partial answers. The clearest subtype distinction separates explicit chain generation in token space from internal chain-of-thought, described as layer-wise subtask scheduling even when no intermediate steps are expressed. Another distinction separates single-response chains from multi-turn reasoning, and one paper explicitly frames the construct as task-level reasoning rather than just chains of facts.

**Space of measurement.** Operationalization is dominated by benchmark-style evaluation: papers link the construct to 17 measurement instruments, most often GSM8K, BIG-Bench Hard, and GPQA, plus 14 other benchmarks or task environments. They also link it to 11 behavioral indicators, most often Chain of thought and Code navigation, plus 9 others. In these measurements, the construct is usually assessed indirectly through performance on tasks described as requiring multi-step or complex reasoning, though some papers also operationalize it directly as the production of intermediate reasoning steps, including predefined step-by-step formats or outputs with K reasoning steps before the final answer. This mostly matches the dominant definitions, but it also includes work on internal chain-of-thought where the reasoning is said to remain unexpressed.

**Links.** Papers report causal and related links, but no correlational links. Several papers claim causal relationships from chain-of-thought reasoning to Reasoning, and one paper makes a similar causal claim for Mathematical reasoning; smaller lines make further causal claims to downstream behaviors and capacities. In the opposite direction, one paper claims a causal relationship from Planning to chain-of-thought reasoning, and several papers claim a causal relationship from Chain of thought to chain-of-thought reasoning. Related links connect it with Complex reasoning and a broader set of task-specific phenomena, including errors, decomposition, grounding, and domain-specific reasoning behaviors.

## Sources

**Chain-of-Thought reasoning** (2 papers: [Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf), [Can LLMs Understand Time Series Anomalies?](https://proceedings.iclr.cc/paper_files/paper/2025/file/05774fb74e863308c4b460c9f49f6918-Paper-Conference.pdf))
> The ability of a language model to solve complex problems by generating a sequence of intermediate, logical steps before providing a final answer.

**Chain-of-reasoning** (1 paper: [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf))
> The model's ability to break down a problem into intermediate, sequential steps to arrive at a final solution, often by generating explicit intermediate text.

**Chain-of-thought capability** (1 paper: [Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf))
> The model's ability to benefit from or perform step-by-step reasoning when prompted to explain intermediate inference steps.

**Chain-of-Thought ability** (1 paper: [Training Nonlinear Transformers for Chain-of-Thought Inference: A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf))
> The latent capability of a model to perform multi-step reasoning by generating intermediate steps when prompted with examples.

**Thought chain reasoning** (1 paper: [ThinkBot: Embodied Instruction Following with Thought Chain Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ffa8551239448e07ced48311bf88f6f3-Paper-Conference.pdf))
> The latent ability of a model to infer and articulate a series of intermediate, unstated steps that connect an initial problem to a final solution, particularly for recovering missing actions from sparse instructions.

**Internal chain-of-thought** (1 paper: [Internal Chain-of-Thought: Empirical Evidence for Layer-wise Subtask Scheduling in LLMs](https://aclanthology.org/2025.emnlp-main.1147.pdf))
> The latent capacity of LLMs to internally decompose composite tasks into subtasks and process them sequentially across network layers, even when intermediate steps are not expressed in output.

**Multistep reasoning** (2 papers: [Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf), [Trojsten Benchmark: Evaluating LLM Problem-Solving in Slovak STEM Competition Problems](https://aclanthology.org/2025.emnlp-main.1779.pdf))
> A general cognitive capability to solve problems by breaking them down into a sequence of intermediate steps or operations.

**Step-by-step thinking** (1 paper: [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf))
> The ability to break down a problem into a sequence of smaller, manageable steps and solve them sequentially.

**Procedural reasoning** (1 paper: [RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning](https://aclanthology.org/2025.emnlp-main.1630.pdf))
> The capacity to carry out step-by-step problem solving using methods, inference rules, or solution procedures rather than only retrieving facts.

**Thinking** (1 paper: [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf))
> The latent ability of an LLM to generate internal reasoning or planning processes in natural language before producing a final response, enabling improved performance on complex tasks through implicit computation and self-reflection.

**Multi-turn reasoning** (2 papers: [Building Math Agents with Multi-Turn Iterative Preference Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/40eff1670d6b08bb1bda48b0c5f30110-Paper-Conference.pdf), [MuTIS: Enhancing Reasoning Efficiency through Multi Turn Intervention Sampling in Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.690.pdf))
> The capacity to maintain context and make a sequence of coherent decisions or inferences over multiple interaction turns with an external environment.

**Multi-step reasoning** (3 papers: [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf), [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf), [PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements](https://aclanthology.org/2025.emnlp-main.403.pdf))
> The process of generating a sequence of intermediate reasoning steps to reach a final answer.

**Sequential inference** (1 paper: [seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs](https://aclanthology.org/2025.emnlp-main.1714.pdf))
> The observable process of generating a sequence of conclusions or actions based on a set of facts to solve a problem.

**Step-wise reasoning** (1 paper: [Digest the Knowledge: Large Language Models empowered Message Passing for Knowledge Graph Question Answering](https://aclanthology.org/2025.acl-long.750.pdf))
> The capacity to decompose complex questions into a sequence of sub-questions or inference steps, solving them progressively from shallow to deep levels of knowledge.

## Relationships

### Chain-of-thought reasoning →
- **GSM8K** (measurement instrument): *measured_by*, 4 papers
  > Two mathematical datasets are considered: (4) GSM8k (Cobbe et al., 2021) and (5) AQuA (Ling et al., 2017), since they require comprehensive understanding of complex problems and powerful abilities like bottom-up composition and multi-step reasoning. (Section 4.1)
  - [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf)
  - [Semantic Exploration with Adaptive Gating for Efficient Problem Solving with Language Models](https://aclanthology.org/2025.acl-long.29.pdf)
  - [CommVQ: Commutative Vector Quantization for KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25du/li25du.pdf)
  - [QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.240.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 3 papers
  > To validate our methods on diverse tasks, we apply BBH (Suzgun et al., 2022) including a suite of 23 challenging BIG-Bench tasks requiring multi-step reasoning. (Section 4.4)
  - [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 3 papers
  > Chain-of-Thought (CoT) is an efficient prompting method that enables the reasoning ability of large language models by augmenting the query using multiple examples with multiple intermediate steps. (Abstract)
  - [Training Nonlinear Transformers for Chain-of-Thought Inference: A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf)
  - [Rethinking External Slow-Thinking: From Snowball Errors to Probability of Correct Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gan25a/gan25a.pdf)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **GPQA** (measurement instrument): *measured_by*, 2 papers
  > For instance, models frequently demonstrate high performance on standardized test-style questions yet struggle when faced with complex planning or multi-step reasoning challenges, a limitation highlighted by specialized benchmarks like PlanBench (Valmeekam et al., 2022), GPQA (Rein et al., 2023), and HLE (Phan et al., 2025). (Section 2.4)
  - [In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1208.pdf)
  - [Stepwise Informativeness Search for Improving LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1285.pdf)
- **2WikiMultiHopQA** (measurement instrument): *measured_by*, 1 paper
  > To assess OmniKV’s performance in multi-step reasoning, we utilized 2WikiMQA (Ho et al., 2020) and HotpotQA (Yang et al., 2018) from LongBench. (Section 5)
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
- **Spoken dialogue generation** (behavioral indicator): *causes*, 1 paper
  > "the insertion of the text-related tasks between speech inputs and outputs allows the model to benefit from the pretraining LLM and chained reasoning over the intermediary modality"
  - [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > To assess OmniKV’s performance in multi-step reasoning, we utilized 2WikiMQA (Ho et al., 2020) and HotpotQA (Yang et al., 2018) from LongBench. (Section 5)
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > OBQA (Mihaylov et al., 2018) (multi-step reasoning). (Section 5.1)
  - [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
- **AQuA-RAT** (measurement instrument): *measured_by*, 1 paper
  > Two mathematical datasets are considered: (4) GSM8k (Cobbe et al., 2021) and (5) AQuA (Ling et al., 2017), since they require comprehensive understanding of complex problems and powerful abilities like bottom-up composition and multi-step reasoning. (Section 4.1)
  - [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf)
- **Fact checking** (behavioral indicator): *causes*, 1 paper
  > we extend this by incorporating agent-based LLM, enabling iterative interactions with the knowledge base to resolve ambiguous entities and execute multi-step reasoning for more robust and in-depth claim verification. (Section 2)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
- **Mathematical reasoning** (construct): *causes*, 1 paper
  > Chain of Thought (CoT) of multi-step benefits from the logical structure of the reasoning steps and task-specific actions, significantly enhancing the mathematical reasoning capabilities of large language models.
  - [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf)
- **Reasoning efficiency** (construct): *causes*, 1 paper
  > "Furthermore, multi-step reasoning involving processing long CoT demands greater computational resources, which renders the inference process practically inefficient."
  - [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 1 paper
  > These datasets test a range of commonsense reasoning skills, with StrategyQA requiring more multi-step reasoning.
  - [RARE: Retrieval-Augmented Reasoning Enhancement for Large Language Models](https://aclanthology.org/2025.acl-long.896.pdf)
- **Code navigation** (behavioral indicator): *causes*, 1 paper
  > we equip the localization agent with programming tools based on Abstract Syntax Tree (AST) and Language Server Protocol (LSP) that enable compact code navigation by taking advantage of multi-step reasoning. (Section 1)
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)
- **Iterative refinement** (behavioral indicator): *causes*, 1 paper
  > the Actor refines suboptimal actions via multi-step reasoning and environment validation (Abstract).
  - [Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wan25g/wan25g.pdf)
- **FOLIO** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our framework on four multi-step reasoning datasets: FOLIO (Han et al., 2022), ProofWriter (Tafjord et al., 2020), MMLU-Pro (Wang et al., 2024c) and GPQA (Rein et al., 2023) (Section 4.1).
  - [Stepwise Informativeness Search for Improving LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1285.pdf)
- **ProofWriter** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our framework on four multi-step reasoning datasets: FOLIO (Han et al., 2022), ProofWriter (Tafjord et al., 2020), MMLU-Pro (Wang et al., 2024c) and GPQA (Rein et al., 2023) (Section 4.1).
  - [Stepwise Informativeness Search for Improving LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1285.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our framework on four multi-step reasoning datasets: FOLIO (Han et al., 2022), ProofWriter (Tafjord et al., 2020), MMLU-Pro (Wang et al., 2024c) and GPQA (Rein et al., 2023) (Section 4.1).
  - [Stepwise Informativeness Search for Improving LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1285.pdf)
- **AndroidWorld** (measurement instrument): *measured_by*, 1 paper
  > We evaluate RAG-GUI on AndroidWorld, an online environment requiring multi-step reasoning that mirrors real-world scenarios. (Section 4.2)
  - [Retrieval-augmented GUI Agents with Generative Guidelines](https://aclanthology.org/2025.emnlp-main.902.pdf)
- **MATH** (measurement instrument): *measured_by*, 1 paper
  > challenging multi-step reasoning tasks such as MATH (Hendrycks et al., 2021) (Section 1)
  - [QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.240.pdf)
- **MBPP** (measurement instrument): *measured_by*, 1 paper
  > GSM8K and MBPP involve multi-step reasoning, which remains underexplored in the quantization context despite its great importance. (Section 2.1)
  - [QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.240.pdf)
- **HumanEval** (measurement instrument): *measured_by*, 1 paper
  > challenging multi-step reasoning tasks such as ... HumanEval (All, 0-shot) (Chen et al., 2021). (Section 4.1)
  - [QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.240.pdf)
- **MuSR** (measurement instrument): *measured_by*, 1 paper
  > Given that MUSR is designed to assess multistep reasoning, this suggests that models excelling in structured reasoning tasks also tend to perform well in frame-semantic parsing. (Section 4.7)
  - [Can LLMs Extract Frame-Semantic Arguments?](https://aclanthology.org/2025.emnlp-main.1557.pdf)
- **ARC** (measurement instrument): *measured_by*, 1 paper
  > ARC (AI2 Reasoning Challenge) is a dataset created by the Allen Institute for Artiﬁcial Intelligence (AI2) to evaluate question answering systems’ ability to perform multi-step reasoning.
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
- **Memory** (construct): *causes*, 1 paper
  > Mamba can effectively identify key information from long texts through CoT thinking, thus significantly improving its ability to recall long-context memory. (Section 1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)

### → Chain-of-thought reasoning
- **Chain of thought** (behavioral indicator): *causes*, 4 papers
  > Large language models are capable of solving tasks that require complex multi-step reasoning by generating solutions in a step-by-step chain-of-thought format (Section 1).
  - [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf)
  - [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf)
  - [Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf)
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
- **Planning** (construct): *causes*, 1 paper
  > their planning ability remains a critical bottleneck in tackling complex multi-step reasoning tasks. (ABSTRACT)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > These hallucinations (Maynez et al., 2020) are particularly problematic in domains that require multi-step reasoning, since a single logical error is enough to derail a much larger solution. (Section 1).
  - [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf)
- **Integer addition** (behavioral indicator), 1 paper
  > what architectural design choices, dataset characteristics, and training pipeline variants are required to learn a many-step reasoning process like multi-digit addition? (Section 1)
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
- **Textual reasoning** (behavioral indicator), 1 paper
  > Natural Language Reasoning: we prompt LLMs to perform multi-step reasoning via natural language, and select the following publicly avaibable datasets: GSM8k [34] contains grade school math problems to test the basic arithmetic and reasoning ability. (Appendix C)
  - [JiuZhang3.0: Efficiently Improving Mathematical Reasoning by Training Small Data Synthesis Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0356216f73660e15670510f5e42b5fa6-Paper-Conference.pdf)
- **Mathematical problem solving** (behavioral indicator), 1 paper
  > However, their performance in multi-step reasoning tasks, such as solving complex mathematical or coding problems, remains notably constrained (Section 1).
  - [Step-by-Step Reasoning for Math Problems via Twisted Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4d92f656cc99f60fe1bfc98386aee34-Paper-Conference.pdf)
- **Complex reasoning** (construct), 1 paper
  > The step-by-step long-chain reasoning process is most famously used in Chain-of-Thought (CoT) (Wei et al., 2022).
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
- **Entity disambiguation** (behavioral indicator), 1 paper
  > This challenge is amplified in multi-step reasoning, where entity disambiguation must span the entire verification process. (Section 1)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
- **Table reasoning** (construct), 1 paper
  > Table reasoning presents distinct challenges compared to text-only tasks: it requires interpreting diverse cell contents, aligning data across the table, and performing multi-step reasoning with aggregation and numerical operations (Deng et al., 2024; Wu et al., 2025). (Section 1)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Question decomposition** (behavioral indicator), 1 paper
  > multi-step reasoning methods (Uehara et al., 2022; Wang et al., 2022b; Khan et al., 2023; Yao et al., 2023; Besta et al., 2024) have been proposed that decompose the main question into several sub-question-answer pairs (sub-QAs) and subsequently utilize them to derive the final answer. (Section 1)
  - [Confidence-guided Refinement Reasoning for Zero-shot Question Answering](https://aclanthology.org/2025.emnlp-main.354.pdf)
- **Visual grounding** (construct), 1 paper
  > it is crucial to ground the reasoning process to the visual information and VoCoT is the most suitable format (Section 4.3).
  - [VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models](https://aclanthology.org/2025.naacl-long.192.pdf)
