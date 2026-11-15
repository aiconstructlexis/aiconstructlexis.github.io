# LongBench
**Type:** Measurement instrument  
**Supporting papers:** 112  
**Also known as:** Longbench  

## State of the Field

**What it is.** Across the surveyed work, LongBench is most commonly described as a multi-task benchmark or benchmark suite for evaluating long-context understanding in LLMs, usually across question answering, summarization, and code completion. Some papers instead call it a collection of long-context benchmark datasets and describe it as bilingual or multilingual, with real-world and synthetic tasks. Reported length characterizations differ: one definition gives evaluation lengths of 5k to 15k tokens, while other papers describe average context around 18K, a 32K maximum length, or use on sequences longer than 32K.

**What it is claimed to measure.** Papers link LongBench to 6 constructs and 13 behavioral indicators. The prevailing claim is that it measures long-context understanding. Among behavioral indicators, it is most often used to measure text summarization, code completion, few-shot task performance, and question answering, while other papers also use it for additional constructs and task indicators.

**Space of uses.** In use, papers commonly position LongBench as a main downstream evaluation for long-context models and methods, often alongside other long-context benchmarks, and several papers evaluate only selected subsets or tasks from it. The instrument is directly related to 5 other measurement instruments, most often 2WikiMultiHopQA, HotpotQA, MuSiQue, MultiNews, and SAMSum, and some papers also sample LongBench material as context sentences or extended conversations.

**Concerns raised.** A limitation raised in one paper is that current benchmarks such as LongBench "scale only up to 40,000 tokens."

## Sources

**LongBench** (35 papers: [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf), [HyperAttention: Long-context Attention in Near-Linear Time](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5aa940590399350401c57cdf52ce78-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf), [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf), [Advancing MoE Efficiency: A Collaboration-Constrained Routing (C2R) Strategy for Better Expert Parallelism Design](https://aclanthology.org/2025.naacl-long.347.pdf), [LCIRC: A Recurrent Compression Approach for Efficient Long-form Context and Query Dependent Modeling in LLMs](https://aclanthology.org/2025.naacl-long.524.pdf), [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf), [Extending LLM Context Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.28.pdf), [RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/behnam25a/behnam25a.pdf), [A Training-Free Length Extrapolation Approach for LLMs: Greedy Attention Logit Interpolation](https://aclanthology.org/2025.emnlp-main.443.pdf), [AnchorAttention: Difference-Aware Sparse Attention with Stripe Granularity](https://aclanthology.org/2025.emnlp-main.430.pdf), [CAFE: Retrieval Head-based Coarse-to-Fine Information Seeking to Enhance Multi-Document QA Capability](https://aclanthology.org/2025.emnlp-main.655.pdf), [CRITICTOOL: Evaluating Self-Critique Capabilities of Large Language Models in Tool-Calling Error Scenarios](https://aclanthology.org/2025.emnlp-main.1355.pdf), [DCIS: Efficient Length Extrapolation of LLMs via Divide-and-Conquer Scaling Factor Search](https://aclanthology.org/2025.emnlp-main.767.pdf), [DrDiff: Dynamic Routing Diffusion with Hierarchical Attention for Breaking the Efficiency-Quality Trade-off](https://aclanthology.org/2025.emnlp-main.474.pdf), [GATEAU: Selecting Influential Samples for Long Context Alignment](https://aclanthology.org/2025.emnlp-main.375.pdf), [GraphKV: Breaking the Static Selection Paradigm with Graph-Based KV Cache Eviction](https://aclanthology.org/2025.emnlp-main.1112.pdf), [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf), [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf), [Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query](https://aclanthology.org/2025.emnlp-main.1732.pdf), [ToM: Leveraging Tree-oriented MapReduce for Long-Context Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.899.pdf), [TokenSelect: Efficient Long-Context Inference and Length Extrapolation for LLMs via Dynamic Token-Level KV Cache Selection](https://aclanthology.org/2025.emnlp-main.1079.pdf), [TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text](https://aclanthology.org/2025.emnlp-main.334.pdf), [UNComp: Can Matrix Entropy Uncover Sparsity? — A Compressor Design from an Uncertainty-Aware Perspective](https://aclanthology.org/2025.emnlp-main.209.pdf), [XQuant: Achieving Ultra-Low Bit KV Cache Quantization with Cross-Layer Compression](https://aclanthology.org/2025.emnlp-main.494.pdf), [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf), [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf), [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf), [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf), [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf), [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf), [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf), [SlimGPT: Layer-wise Structured Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf), [Stress-Testing Long-Context Language Models with Lifelong ICL and Task Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc8db5884a7474b4771762b6f0c8ee1-Paper-Datasets_and_Benchmarks_Track.pdf))
> Benchmark for evaluating long-context understanding in LLMs across diverse tasks including question answering, summarization, and code completion, with input lengths ranging from 5k to 15k tokens.

**Longbench** (1 paper: [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf))
> A benchmark consisting of various tasks, such as long-document question answering and query-based summarization, to evaluate long-context understanding.

## Relationships

### → LongBench
- **Long-context understanding** (construct): *measured_by*, 37 papers
  > The evaluation is performed on the LongBench benchmark (Bai et al., 2023), where we compare our model with GPT-3.5-turbo and other LLaMA-2-based open-source models designed for handling long context. (Section 4)
  - [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
  - [SlimGPT: Layer-wise Structured Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
  - [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf)
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
  - [Palu: KV-Cache Compression with Low-Rank Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/7da6e0e00702c60607a6ae05c802ef85-Paper-Conference.pdf)
  - [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
  - [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
  - [DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c1ddd2e59df46fd2aa85c833b1b36ed-Paper-Conference.pdf)
  - [ThinK: Thinner Key Cache by Query-Driven Pruning](https://proceedings.iclr.cc/paper_files/paper/2025/file/8edb116d5b288b6a9bba4c16ab647702-Paper-Conference.pdf)
  - [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf)
  - [Training Free Exponential Context Extension via Cascading KV Cache](https://proceedings.iclr.cc/paper_files/paper/2025/file/19a567abaec3990cb40d7a013556fecd-Paper-Conference.pdf)
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
  - [Human-inspired Episodic Memory for Infinite Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c05144b635df16ac9bbf8246bbbd55ca-Paper-Conference.pdf)
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
  - [HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf)
  - [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf)
  - [LCIRC: A Recurrent Compression Approach for Efficient Long-form Context and Query Dependent Modeling in LLMs](https://aclanthology.org/2025.naacl-long.524.pdf)
  - [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf)
  - [Extending LLM Context Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.28.pdf)
  - [Re3Syn: A Dependency-Based Data Synthesis Framework for Long-Context Post-training](https://aclanthology.org/2025.acl-long.1518.pdf)
  - [MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560.pdf)
  - [Scaling up the State Size of RNN LLMs for Long-Context Scenarios](https://aclanthology.org/2025.acl-long.564.pdf)
  - [LongRecipe: Recipe for Efficient Long Context Generalization in Large Language Models](https://aclanthology.org/2025.acl-long.581.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
  - [Core Context Aware Transformers for Long Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cg/chen25cg.pdf)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
  - [Lexico: Extreme KV Cache Compression via Sparse Coding over Universal Dictionaries](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25ae/kim25ae.pdf)
  - [GANQ: GPU-Adaptive Non-Uniform Quantization for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25ae/zhao25ae.pdf)
  - [GATEAU: Selecting Influential Samples for Long Context Alignment](https://aclanthology.org/2025.emnlp-main.375.pdf)
  - [AnchorAttention: Difference-Aware Sparse Attention with Stripe Granularity](https://aclanthology.org/2025.emnlp-main.430.pdf)
- **Text summarization** (behavioral indicator): *measured_by*, 21 papers
  > This benchmark encompasses a broad range of tasks, such as question-answering, summarization, and code completion, where the evaluation length ranges from 5k to 15k. (Section 4.3)
  - [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
  - [Long Context Compression with Activation Beacon](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc797c61eb18f7b3ce9a74af0ef0d876-Paper-Conference.pdf)
  - [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [ThinK: Thinner Key Cache by Query-Driven Pruning](https://proceedings.iclr.cc/paper_files/paper/2025/file/8edb116d5b288b6a9bba4c16ab647702-Paper-Conference.pdf)
  - [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf)
  - [Forgetting Transformer: Softmax Attention with a Forget Gate](https://proceedings.iclr.cc/paper_files/paper/2025/file/add3d389197ad2267f660ad060ef61f4-Paper-Conference.pdf)
  - [FocusLLM: Precise Understanding of Long Context by Dynamic Condensing](https://aclanthology.org/2025.acl-long.1500.pdf)
  - [MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560.pdf)
  - [DAC: A Dynamic Attention-aware Approach for Task-Agnostic Prompt Compression](https://aclanthology.org/2025.acl-long.952.pdf)
  - [ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25b/sun25b.pdf)
  - [CommVQ: Commutative Vector Quantization for KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25du/li25du.pdf)
  - [HashAttention: Semantic Sparsity for Faster Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/desai25a/desai25a.pdf)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
  - [GSM-$∞$: How Do your LLMs Behave over Infinitely Increasing Reasoning Complexity and Context Length?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25m/zhou25m.pdf)
  - [GATEAU: Selecting Influential Samples for Long Context Alignment](https://aclanthology.org/2025.emnlp-main.375.pdf)
- **Code completion** (behavioral indicator): *measured_by*, 12 papers
  > Table 2: Results (%) on LongBench. ∗ indicates results reported by Bai et al. [2023]. CREAM-7B-32k is instruction-tuned for 100 steps using 4K length data on LLaMa2-7B-Chat. Model Single- Doc QA Multi- Doc QA Summari- zation Few-shot Learning Code Completion
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
  - [Long Context Compression with Activation Beacon](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc797c61eb18f7b3ce9a74af0ef0d876-Paper-Conference.pdf)
  - [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
  - [FocusLLM: Precise Understanding of Long Context by Dynamic Condensing](https://aclanthology.org/2025.acl-long.1500.pdf)
  - [MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560.pdf)
  - [Squeezed Attention: Accelerating Long Context Length LLM Inference](https://aclanthology.org/2025.acl-long.1568.pdf)
  - [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf)
  - [ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25b/sun25b.pdf)
  - [CommVQ: Commutative Vector Quantization for KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25du/li25du.pdf)
- **Few-shot task performance** (behavioral indicator): *measured_by*, 11 papers
  > “we further investigate the benefits of long context models for few-shot tasks using two additional datasets (Trec and SAMSum) from LongBench.”
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
  - [Long Context Compression with Activation Beacon](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc797c61eb18f7b3ce9a74af0ef0d876-Paper-Conference.pdf)
  - [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf)
  - [ThinK: Thinner Key Cache by Query-Driven Pruning](https://proceedings.iclr.cc/paper_files/paper/2025/file/8edb116d5b288b6a9bba4c16ab647702-Paper-Conference.pdf)
  - [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf)
  - [FocusLLM: Precise Understanding of Long Context by Dynamic Condensing](https://aclanthology.org/2025.acl-long.1500.pdf)
  - [Squeezed Attention: Accelerating Long Context Length LLM Inference](https://aclanthology.org/2025.acl-long.1568.pdf)
  - [MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560.pdf)
  - [DAC: A Dynamic Attention-aware Approach for Task-Agnostic Prompt Compression](https://aclanthology.org/2025.acl-long.952.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 5 papers
  > This benchmark encompasses a broad range of tasks, such as question-answering, summarization, and code completion, where the evaluation length ranges from 5k to 15k. (Section 4.3)
  - [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [FocusLLM: Precise Understanding of Long Context by Dynamic Condensing](https://aclanthology.org/2025.acl-long.1500.pdf)
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf)
- **General ability** (construct): *measured_by*, 2 papers
  > LongBench (Bai et al., 2024): Focused on medium-context tasks (10K tokens), it assesses summarization, QA, and fact-checking across multiple domains, offering a measure of general capabilities.
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [DCIS: Efficient Length Extrapolation of LLMs via Divide-and-Conquer Scaling Factor Search](https://aclanthology.org/2025.emnlp-main.767.pdf)
- **Document question answering** (behavioral indicator): *measured_by*, 2 papers
  > In this section, we comprehensively evaluate how structurization boosts QA ability on seven datasets from the LongBench benchmark [3] with a variety of LLMs to examine. (Section 4.1)
  - [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf)
  - [TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text](https://aclanthology.org/2025.emnlp-main.334.pdf)
- **Long-context generation** (behavioral indicator): *measured_by*, 2 papers
  > Accuracy comparison between offline searched layer-wise KV cache precision using KVTuner in Table 5 and 6 and uniform KV precision settings of the sensitive Qwen2.5-7B-Instruct on 20 LongBench long context generation benchmarks. (Table 7)
  - [KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dd/li25dd.pdf)
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **Code generation** (behavioral indicator): *measured_by*, 1 paper
  > LongBench This benchmark contains a variety of zero-shot long context tasks, such as: Single/Multi Document QA, Summarization, Coding, etc. (Section 5)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
- **Single-document question answering** (behavioral indicator): *measured_by*, 1 paper
  > LongBench includes nearly 5000 test samples and covers six main task categories, such as single-document question answering (SQA)... (Section 2)
  - [MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560.pdf)
- **Length generalization** (construct): *measured_by*, 1 paper
  > We compare our method with existing length extrapolation approaches... on LongBench (Bai et al., 2023) and InfiniteBench (Zhang et al., 2024)... (Section 5.1)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > EM-LLMS (surprise only) vs. RAG (NV-Embed-v2 retriever) vs. full-context, with LLaMA- 3.1-8B as the base LLM, evaluated on LongBench (Figure 1).
  - [Human-inspired Episodic Memory for Infinite Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c05144b635df16ac9bbf8246bbbd55ca-Paper-Conference.pdf)
- **Contextual reasoning** (construct): *measured_by*, 1 paper
  > For LongBench, we use datasets from the Single-Doc QA and Multi-Doc QA categories to assess contextual reasoning.
  - [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf)
- **Fact checking** (behavioral indicator): *measured_by*, 1 paper
  > LongBench (Bai et al., 2024): Focused on medium-context tasks (10K tokens), it assesses summarization, QA, and fact-checking across multiple domains...
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **Multi-document question answering** (behavioral indicator): *measured_by*, 1 paper
  > "These tasks belong to 6 categories in total: single-doc QA, multi-doc QA, summarization, few-shot learning, synthetic, and code."
  - [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf)
- **Knowledge retrieval** (behavioral indicator): *measured_by*, 1 paper
  > "This benchmark is the most important because it shows both long context generation performance and knowledge retrieval performance"
  - [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf)
- **In-context learning** (construct): *measured_by*, 1 paper
  > “LongBench (in-context learning and code completion)”
  - [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf)
- **Synthetic recall** (behavioral indicator): *measured_by*, 1 paper
  > On LongBench, we evaluate our method with a range of realistic scenarios, including single-/multi-document QA, document summarization, code completion, information retrieval, etc. (Section 5.1)
  - [ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25b/sun25b.pdf)
- **Long-context reasoning** (construct): *measured_by*, 1 paper
  > Long document reasoning performance (%) on Longbench and InfiniteBench (Table 1)
  - [ToM: Leveraging Tree-oriented MapReduce for Long-Context Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.899.pdf)

### Associated with
- **2WikiMultiHopQA** (measurement instrument), 2 papers
  > Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA... (Section 5.1).
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf)
- **MuSiQue** (measurement instrument), 2 papers
  > Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering)... (Section 5.1).
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf)
- **HotpotQA** (measurement instrument), 2 papers
  > We also include HotpotQA (multi-document question answering) from LongBench... (Section 5.1).
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
  - [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf)
- **SAMSum** (measurement instrument), 1 paper
  > Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): ...SAMSum (few-shot instruction following)... (Section 5.1).
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
- **MultiNews** (measurement instrument), 1 paper
  > Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): ...and MultiNews (multi-document summarization) (Section 5.1).
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
