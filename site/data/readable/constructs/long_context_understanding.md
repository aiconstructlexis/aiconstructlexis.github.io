# Long-context understanding
**Type:** Construct  
**Supporting papers:** 116  
**Also known as:** Long context understanding, Long text understanding, Long-context comprehension, Long-text understanding, Cross-page comprehension, Long Context, Long-context capabilities, Long-context capability, Long-context processing capability, Long-context modeling capability, Long-context modeling, Long-context Modeling Capacity, Recall ability, Long sequence comprehension, Context memory, Long-range ability, Long-range context understanding, Long-range information access, Long-context ability, Long-context performance, Long-range capabilities, Cognition capability, Recall capability, Long-context processing, Long-context processing ability, Long-text comprehension  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this as a latent model ability to process, retain, integrate, and use information across very long inputs, often beyond the original context window, while maintaining coherence, relevance, and task performance. Most definitions are broad and text-centered, covering comprehension, reasoning, and response generation from extended sequences, and some explicitly stress noisy long inputs, extended dialogue histories, or evidence distributed across pages or documents. A smaller line of work narrows the construct to particular demands such as recall of specific facts, context memory across multi-step interactions, or access to distant information, while some papers extend the same framing to multimodal visual-text settings.

**Space of facets.** Papers use several neighboring labels for closely similar meanings, including long-text understanding, long-context comprehension, long-context capability, long-context modeling, long-context processing, long-range ability, and long-context modeling capacity. Within this family, narrower facets are sometimes named separately: recall ability or recall capability focus on retrieving specific information from long contexts, context memory focuses on retaining and correctly using information across long or multi-step tasks, and cross-page comprehension or long-range information access focus on information spread across distant pages or sequence positions. Some papers also place length generalization beside this construct, describing it as a subproblem within long-context modeling rather than the whole construct.

**Space of measurement.** Operationalization is overwhelmingly benchmark-based: papers link the construct to 36 measurement instruments and 15 behavioral indicators, most often LongBench, RULER, InfiniteBench, Needle-in-a-Haystack, and L-Eval. These instruments operationalize the construct through multitask suites, synthetic long-sequence tasks, ultra-long context tests, and retrieval-focused probes; papers also use passkey retrieval, long-context question answering, summarization, variable tracking, and perplexity on long-sequence corpora such as PG-19 or WikiText-2. This measurement space mostly targets the capacities named in definitions, especially retaining, retrieving, and reasoning over extended inputs, though some studies operationalize it more narrowly through recall-style tasks.

**Links.** No correlational links are reported; papers instead use causal or generic relatedness language. Among the recurring links, length generalization is related to long-context understanding, contextual understanding and long-range dependency modeling are presented as causal antecedents, and position-related effects are described as degrading or impairing it as context grows. Papers also claim causal relationships from the construct to downstream tasks, especially text summarization, and relate it more broadly to application settings such as dialogue, document, code, and question-answering work.

## Sources

**Long text understanding** (2 papers: [SmartPlay : A Benchmark for LLMs as Intelligent Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/063d1fadbde557466bf5bcffe814a64e-Paper-Conference.pdf), [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf))
> The latent ability to comprehend and process lengthy or syntactically complex textual inputs, ranging from short lines to documents exceeding one page.

**Long-context understanding** (7 papers: [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf), [LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/211ab571cc9f3802afa6ffff52ae3e5b-Paper-Conference.pdf), [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf), [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf), [RuleArena: A Benchmark for Rule-Guided Reasoning with LLMs in Real-World Scenarios](https://aclanthology.org/2025.acl-long.27.pdf), [GATEAU: Selecting Influential Samples for Long Context Alignment](https://aclanthology.org/2025.emnlp-main.375.pdf), [LCIRC: A Recurrent Compression Approach for Efficient Long-form Context and Query Dependent Modeling in LLMs](https://aclanthology.org/2025.naacl-long.524.pdf))
> The latent ability of a language model to maintain coherence, relevance, and performance when processing input sequences far exceeding its original context window.

**Long context understanding** (4 papers: [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf), [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf))
> The latent ability of a model to effectively process and utilize information across extended input sequences, integrating relevant content despite length and noise.

**Long-context comprehension** (6 papers: [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf), [Dynamic Chunking and Selection for Reading Comprehension of Ultra-Long Context in Large Language Models](https://aclanthology.org/2025.acl-long.1538.pdf), [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf), [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf), [ETHIC: Evaluating Large Language Models on Long-Context Tasks with High Information Coverage](https://aclanthology.org/2025.naacl-long.283.pdf))
> The capacity of a model to process, retain, and utilize information from extended conversational histories or long input sequences.

**Long-text understanding** (2 papers: [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf), [Context-Aware Hierarchical Taxonomy Generation for Scientific Papers via LLM-Guided Multi-Aspect Clustering](https://aclanthology.org/2025.emnlp-main.788.pdf))
> The model's comprehensive ability to read, process, and reason about information presented in extremely long documents or sequences.

**Cross-page comprehension** (1 paper: [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to collect, synthesize, and reason over information and evidence distributed across multiple different pages of a document.

**Long-context capability** (3 papers: [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf), [Untie the Knots: An Efficient Data Augmentation Strategy for Long-Context Pre-Training in Language Models](https://aclanthology.org/2025.acl-long.62.pdf), [Multimodal Needle in a Haystack: Benchmarking Long-Context Capability of Multimodal Large Language Models](https://aclanthology.org/2025.naacl-long.166.pdf))
> The latent ability of a model to effectively process, understand, and perform tasks requiring information from extended textual contexts.

**Long Context** (1 paper: [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf))
> The latent ability to process, comprehend, and synthesize information to generate responses from extensive textual inputs.

**Long-context capabilities** (1 paper: [Forgetting Transformer: Softmax Attention with a Forget Gate](https://proceedings.iclr.cc/paper_files/paper/2025/file/add3d389197ad2267f660ad060ef61f4-Paper-Conference.pdf))
> The model's ability to effectively process, understand, and utilize information from very long sequences of text.

**Long-context processing capability** (1 paper: [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf))
> The ability of a model to effectively process, understand, and utilize information from very long input sequences to perform complex tasks.

**Long-context modeling capability** (2 papers: [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf), [Re3Syn: A Dependency-Based Data Synthesis Framework for Long-Context Post-training](https://aclanthology.org/2025.acl-long.1518.pdf))
> The latent ability of a model to capture long-range dependencies and process extended input sequences effectively.

**Long-context Modeling Capacity** (1 paper: [Exploring the Potential of LLMs as Personalized Assistants: Dataset, Evaluation, and Analysis](https://aclanthology.org/2025.acl-long.504.pdf))
> The ability of an LLM to retain and effectively utilize information from extended dialogue histories, despite the constraints of finite context length.

**Long-context modeling** (2 papers: [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf), [PeerQA: A Scientific Question Answering Dataset from Peer Reviews](https://aclanthology.org/2025.naacl-long.22.pdf))
> The latent ability of a language model to effectively process and retain information across very long input sequences, maintaining coherence and performance over thousands of tokens.

**Recall ability** (1 paper: [Scaling up the State Size of RNN LLMs for Long-Context Scenarios](https://aclanthology.org/2025.acl-long.564.pdf))
> The model's underlying capacity to retrieve specific, relevant information from long input contexts, especially in information-sparse scenarios.

**Long sequence comprehension** (1 paper: [GraphInsight: Unlocking Insights in Large Language Models for Graph Structure Understanding](https://aclanthology.org/2025.acl-long.591.pdf))
> The latent ability of LLMs to maintain understanding and retain information across extended input sequences, particularly challenged by structural complexity and length.

**Context memory** (1 paper: [PlanningArena: A Modular Benchmark for Multidimensional Evaluation of Planning and Tool Learning](https://aclanthology.org/2025.acl-long.1499.pdf))
> The model's ability to retain and correctly use information across long or multi-step planning tasks, particularly in handling user profiles and extended task descriptions without losing critical details.

**Long-range ability** (1 paper: [KV-Latent: Dimensional-level KV Cache Reduction with Frequency-aware Rotary Positional Embedding](https://aclanthology.org/2025.acl-long.77.pdf))
> The latent capacity of a model to maintain coherent and accurate representations over long input sequences, particularly in preserving positional information across distant tokens.

**Long-range context understanding** (1 paper: [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.675.pdf))
> The capacity to synthesize information across multiple documents or abstracts that are distantly related in the input sequence, maintaining coherence and relevance in the output.

**Long-range information access** (1 paper: [Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25v/hu25v.pdf))
> The latent ability to access and utilize information from distant parts of the input sequence, beyond the immediate attention window.

**Long-context performance** (1 paper: [Puzzle: Distillation-Based NAS for Inference-Optimized LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bercovich25a/bercovich25a.pdf))
> The model's ability to maintain accuracy and coherence when processing and generating text with very long input sequences.

**Long-range capabilities** (1 paper: [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf))
> The latent ability of a model to process and maintain dependencies across extensive input contexts.

**Long-context ability** (1 paper: [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ag/xu25ag.pdf))
> The capacity to process and use information across very long input sequences without losing task performance.

**Long-context processing** (2 papers: [Efficient Long Context Fine-tuning with Chunk Flow](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25m/yuan25m.pdf), [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf))
> The model's ability to effectively process and utilize information from extensive input sequences.

**Cognition capability** (1 paper: [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf))
> The model's latent capacity to understand, organize, and use complex long-form context effectively across downstream tasks.

**Recall capability** (1 paper: [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf))
> The model's ability to retrieve specific, factual information from a long context provided as input.

**Long-context processing ability** (1 paper: [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf))
> The model's latent capability to effectively handle, integrate, and utilize information from very long sequences of input text.

**Long-text comprehension** (1 paper: [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf))
> The latent ability of a model to understand and process information across extended input sequences, maintaining coherence and extracting relevant details over long contexts.

## Relationships

### Long-context understanding →
- **LongBench** (measurement instrument): *measured_by*, 37 papers
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
- **RULER** (measurement instrument): *measured_by*, 14 papers
  > We evaluate on the RULER benchmark (Hsieh et al., 2024), a set of 13 synthetic tasks aimed to assess long-context capabilities of language models. (Section 7.1.1)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
  - [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [Scaling Long Context Training Data by Long-Distance Referrals](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbf49f35b6dd2bef1ad12768c0509daa-Paper-Conference.pdf)
  - [“Give Me BF16 or Give Me Death”? Accuracy-Performance Trade-Offs in LLM Quantization](https://aclanthology.org/2025.acl-long.1304.pdf)
  - [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ag/xu25ag.pdf)
  - [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
  - [xLSTM 7B: A Recurrent LLM for Fast and Efficient Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beck25b/beck25b.pdf)
  - [Puzzle: Distillation-Based NAS for Inference-Optimized LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bercovich25a/bercovich25a.pdf)
  - [SwiftKV: Fast Prefill-Optimized Inference with Knowledge-Preserving Model Transformation](https://aclanthology.org/2025.emnlp-main.1306.pdf)
  - [AnchorAttention: Difference-Aware Sparse Attention with Stripe Granularity](https://aclanthology.org/2025.emnlp-main.430.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 12 papers
  > InfiniteBench (Zhang et al., 2024b) is proposed to evaluate the ultra-long context capability of LLMs over 100K sequence length. (Section 4.1)
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
  - [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)
  - [Human-inspired Episodic Memory for Infinite Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c05144b635df16ac9bbf8246bbbd55ca-Paper-Conference.pdf)
  - [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [LCIRC: A Recurrent Compression Approach for Efficient Long-form Context and Query Dependent Modeling in LLMs](https://aclanthology.org/2025.naacl-long.524.pdf)
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
  - [Facilitating Long Context Understanding via Supervised Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.615.pdf)
- **Needle-in-a-Haystack** (measurement instrument): *measured_by*, 7 papers
  > Additionally, we assess the CREAM-Chat model with Needle-in-a-Haystack and LongBench[Bai et al., 2023]. (Section 3.1).
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
  - [DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c1ddd2e59df46fd2aa85c833b1b36ed-Paper-Conference.pdf)
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
  - [Hymba: A Hybrid-head Architecture for Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f32def07618040e540e0a6182e290562-Paper-Conference.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **L-Eval** (measurement instrument): *measured_by*, 5 papers
  > Following the L-Eval benchmark [1], we evaluated the LLM with tasks categorized into two main groups: closed-ended and open-ended tasks. Closed-ended tasks primarily focus on the capacity for understanding and reasoning within long contexts... (Section 4.2).
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
  - [LCIRC: A Recurrent Compression Approach for Efficient Long-form Context and Query Dependent Modeling in LLMs](https://aclanthology.org/2025.naacl-long.524.pdf)
  - [Extending LLM Context Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.28.pdf)
- **Text summarization** (behavioral indicator): *causes*, 5 papers
  > LLMs equipped with longer context lengths excel at handling complex tasks (Caciularu et al., 2023; Bairi et al., 2023; Mazumder & Liu, 2022), especially those with long input, e.g., document summarization. (Section 1)
  - [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf)
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
  - [E2LLM: Encoder Elongated Large Language Models for Long-Context Understanding and Reasoning](https://aclanthology.org/2025.emnlp-main.970.pdf)
  - [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf)
  - [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf)
- **LongBench-E** (measurement instrument): *measured_by*, 4 papers
  > In addition, we evaluate LongMamba on the tasks within LongBench-E (Bai et al., 2023), which are representative of many real-world long-context applications. (Section 6.1)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
  - [Curse of High Dimensionality Issue in Transformer for Long Context Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cr/zhang25cr.pdf)
  - [Long-Short Alignment for Effective Long-Context Modeling in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25a/du25a.pdf)
- **PG-19** (measurement instrument): *measured_by*, 2 papers
  > For long-context understanding, we use the Pile (Gao et al., 2020) and PG-19 (Rae et al., 2019) datasets and assess the performance of the MambaExtend in terms of perplexity scores at various context lengths. (Section 5.1)
  - [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
- **SCROLLS** (measurement instrument): *measured_by*, 2 papers
  > Evaluation on long-context modeling, including perplexity in various context lengths up to 2M and long-context QA tasks in Scrolls (Parisotto et al., 2020) prove MEGALODON’s ability to model sequences of unlimited length. (Section 1).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
- **NarrativeQA** (measurement instrument): *measured_by*, 2 papers
  > Long-context ability evaluation. Following Xiong et al. [94], we evaluated the models on long-sequence tasks, including ... NarrativeQA [44]... (Table 4, Section 4.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
- **QuALITY** (measurement instrument): *measured_by*, 2 papers
  > Long-context ability evaluation. Following Xiong et al. [94], we evaluated the models on long-sequence tasks, including ... QuALITY [58]... (Table 4, Section 4.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **LooGLE** (measurement instrument): *measured_by*, 2 papers
  > The evaluation is based on two benchmarks for long-context understanding: LongBench (Bai et al., 2024) and LooGLE (Li et al., 2024b).
  - [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf)
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **WikiText-2** (measurement instrument): *measured_by*, 1 paper
  > “for long-context modeling, we use Wikitext-2 (Merity, 2016) and PG19 (Rae et al., 2019) datasets for evaluation.”
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
- **ZeroSCROLLS** (measurement instrument): *measured_by*, 1 paper
  > the ZeroSCROLLS benchmark (Shaham et al., 2023) which is specifically designed for LLMs and contains ten diverse natural language tasks that require understanding long input contexts (Section 5.3).
  - [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf)
- **OK-VQA** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the long-context understanding ability, we adopt the few-shot evaluation setting in Flamingo [1]. We report answer accuracy on the OK-VQA [28], TextVQA [29], VizWiz [30], and VQAV2 [31]. (Section 3.1)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **TextVQA** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the long-context understanding ability, we adopt the few-shot evaluation setting in Flamingo [1]. We report answer accuracy on the OK-VQA [28], TextVQA [29], VizWiz [30], and VQAV2 [31]. (Section 3.1)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **VizWiz** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the long-context understanding ability, we adopt the few-shot evaluation setting in Flamingo [1]. We report answer accuracy on the OK-VQA [28], TextVQA [29], VizWiz [30], and VQAV2 [31]. (Section 3.1)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the long-context understanding ability, we adopt the few-shot evaluation setting in Flamingo [1]. We report answer accuracy on the OK-VQA [28], TextVQA [29], VizWiz [30], and VQAV2 [31]. (Section 3.1)
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **DocVQA** (measurement instrument): *measured_by*, 1 paper
  > “To evaluate the long-context understanding ability, we adopt the few-shot evaluation setting in Flamingo [1]. ... In order to illustrate the impact of having long in-context text, we evaluate the model for document understanding on DocVQA [15] and OCR VQA [34].”
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **Qasper** (measurement instrument): *measured_by*, 1 paper
  > Long-context ability evaluation. Following Xiong et al. [94], we evaluated the models on long-sequence tasks, including Qasper [18]... (Table 4, Section 4.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **QMSum** (measurement instrument): *measured_by*, 1 paper
  > Long-context ability evaluation. Following Xiong et al. [94], we evaluated the models on long-sequence tasks, including ... QMSum [105]. (Table 4, Section 4.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **FinanceBench** (measurement instrument): *measured_by*, 1 paper
  > The recent FinanceBench [19] features both extremely long-context documents and practical, scalable cross-page questions. (Section 2)
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Coding ability** (construct): *causes*, 1 paper
  > This limitation stems from the restricted reasoning abilities of single LLMs and their lack of capacity for long-context understanding... they struggle to tackle more complex coding tasks.
  - [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf)
- **Multi-Needle-in-a-Haystack** (measurement instrument): *measured_by*, 1 paper
  > On the mainstream LLaMA3.1-8B-Instruct-128K (Dubey et al., 2024), we achieve a context length of 1M in the multi-NIAH task. (Section 3.3)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **The Pile** (measurement instrument): *measured_by*, 1 paper
  > Long-context understanding on Pile. (Figure 1)
  - [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf)
- **LOFT** (measurement instrument): *measured_by*, 1 paper
  > “We further evaluate our model on a coverage of the LOFT (Lee et al., 2024) dataset collection”
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **RACE** (measurement instrument): *measured_by*, 1 paper
  > "The RACE dataset represents a \"needle-in-a-haystack\" task demanding identification of critical information within lengthy contexts."
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
- **HELMET** (measurement instrument): *measured_by*, 1 paper
  > In this section, we assess our method AgenticLU using a suite of evaluation tasks drawn from the HELMET long-context benchmark (Yen et al., 2024). (Section 6)
  - [Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.275.pdf)
- **LongGenBench** (measurement instrument): *measured_by*, 1 paper
  > (3) Long-Context Understanding: LongBench (Bai et al., 2024), LongGenBench (Liu et al., 2024a), and Needle-in-the-haystack (Kamradt, 2023) (Sec. 2.2)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **BABILong** (measurement instrument): *measured_by*, 1 paper
  > “We evaluate our method on three benchmarks, each testing unique aspects of long context understanding: (ii) BABILong (Kuratov et al., 2024)”
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
- **NovelHopQA** (measurement instrument): *measured_by*, 1 paper
  > However, none of these benchmarks simultaneously test reasoning depth and long-context comprehension in coherent narratives—an issue that NOVELHOPQA addresses. (Section 2)
  - [NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1328.pdf)
- **LongEval** (measurement instrument): *measured_by*, 1 paper
  > we conducted additional experiments on the LongEval benchmark (Li et al., 2023), which is designed to measure long-context performance (Section 5.3).
  - [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf)
- **Passkey retrieval** (measurement instrument): *measured_by*, 1 paper
  > “The task is widely used to evaluate the maximum context length that the model can effectively handle.”
  - [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf)
- **FLenQA** (measurement instrument): *measured_by*, 1 paper
  > Our goal is to investigate whether finetuning LLMs ... improves their long context capabilities on natural language tasks: ... flexible length question answering (FLenQA) (Section 3)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
- **LV-Eval** (measurement instrument): *measured_by*, 1 paper
  > LV-Eval is a long context benchmark with the context length varying between 16k, 32k, 64k, 128k and 256k. (Section 4.2)
  - [EpMAN: Episodic Memory AttentioN for Generalizing to Longer Contexts](https://aclanthology.org/2025.acl-long.574.pdf)

### → Long-context understanding
- **Lost-in-the-middle** (behavioral indicator): *causes*, 3 papers
  > the “lost in the middle” (Liu et al., 2024c; Song et al., 2024) phenomenon degrades performance with increasing context length (Section 1).
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **Contextual understanding** (construct): *causes*, 2 papers
  > These results underscore MoICE's efficacy in enhancing LLMs' ability to understand and generate long contexts, both of which require high context awareness.
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **Positional bias** (construct): *causes*, 2 papers
  > "they tend to favor content at certain positions ... which harms complex reasoning (Chen et al., 2024b), long-context understanding (Liu et al., 2024) and model-based evaluation"
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **Long-range dependency modeling** (construct): *causes*, 2 papers
  > as these models overlook information from distant tokens, they can not capture the long-distance dependencies for long-text understanding. (Section 2)
  - [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf)
  - [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e54e6eef11f87a874bf1e4551fc6d04e-Paper-Conference.pdf)
- **Effective receptive field** (construct): *causes*, 1 paper
  > This approach potentially increases the model’s ERF, enabling better long-context information flow and understanding. (Section 1)
  - [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf)
- **Recency bias** (construct): *causes*, 1 paper
  > In next-token prediction settings, focusing on local tokens often suffices for short contexts, but can be detrimental when crucial information resides far back in the input.
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)

### Associated with
- **Length generalization** (construct), 3 papers
  > Length extrapolation methods, although theoretically capable of extending the context window beyond the training sequence length, often underperform in practical long-context applications. (Section 1)
  - [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
  - [Long-Short Alignment for Effective Long-Context Modeling in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25a/du25a.pdf)
  - [Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25v/hu25v.pdf)
- **Synthetic recall** (behavioral indicator), 2 papers
  > Passkey retrieval, on the other hand, can effectively measure the maximum distance that a token can attend to during the inference stage. (Section 4.1)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **SEED-Bench-2** (measurement instrument), 1 paper
  > existing benchmarks for multi-image comprehensions, such as SEED-Bench-2 [25] and BLINK [26], consist of short contexts, which fail to evaluate the capability for long-context document comprehension. (Introduction)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BLINK** (measurement instrument), 1 paper
  > existing benchmarks for multi-image comprehensions, such as SEED-Bench-2 [25] and BLINK [26], consist of short contexts, which fail to evaluate the capability for long-context document comprehension. (Introduction)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Long video understanding** (construct), 1 paper
  > Long-context capability is critical for multi-modal foundation models, especially for long video understanding. (ABSTRACT)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Multimodal understanding** (construct), 1 paper
  > Integrating multi-modal understanding with long-context capability is important. (Section 1)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Short-context ability** (construct), 1 paper
  > long-context alignment methods grapple with the balance between preserving short-context proficiency and cultivating long-context capabilities (Liu et al., 2024b).
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
- **Information extraction** (behavioral indicator), 1 paper
  > Medical scenarios involve complex case histories, and selecting values from these contexts tests the capacity for long-context processing. (Section 1)
  - [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf)
- **In-context learning** (construct), 1 paper
  > As LLMs have stronger capabilities and wider applications (Yang et al., 2024), its long-context capability becomes a vital bottleneck for various use cases (e.g. in-context learning, retrieval augmented generation, agent workflow etc.) (Agarwal et al., 2024; Xu et al., 2023; Weng, 2023). (Introduction)
  - [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf)
- **Reasoning** (construct), 1 paper
  > The research community increasingly recognizes long-context modeling as a crucial capability for next-generation large language models, driven by diverse real-world applications ranging from in-depth reasoning (DeepSeek-AI, 2025; Zelikman et al., 2022)... (Introduction).
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > The research community increasingly recognizes long-context modeling as a crucial capability for next-generation large language models, driven by diverse real-world applications ranging from... repository-level code generation (Zhang et al., 2023a; Zhang et al.)... (Introduction).
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
- **Scientific question answering** (behavioral indicator), 1 paper
  > Task 1: ScienceQ&A Generation (LLMgen) Generates a synthesized summary response A to a research question Q using abstracts from the top N relevant papers. It must demonstrate (1) domain knowledge, (2) numerical proficiency, (3) long-range context understanding, and (4) cause-and-effect reasoning (Wadden et al., 2020). (Section 2)
  - [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.675.pdf)
- **Graph understanding** (construct), 1 paper
  > At its core, the challenge of LLM understanding graph structures can be viewed as a stringent long sequence comprehension problem (Section 1)
  - [GraphInsight: Unlocking Insights in Large Language Models for Graph Structure Understanding](https://aclanthology.org/2025.acl-long.591.pdf)
- **State tracking** (behavioral indicator), 1 paper
  > To evaluate long-context capabilities, we use the RULER benchmark (Hsieh et al., 2024), which consists of a set of synthetic needle-in-a-haystack, question-answering and variable tracking tasks, with varying context length from 4K to 131K tokens. (Section 5.1)
  - [xLSTM 7B: A Recurrent LLM for Fast and Efficient Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beck25b/beck25b.pdf)
- **Multi-hop reasoning** (construct), 1 paper
  > These results affirm that long-context capacity alone is not enough—multi-hop reasoning remains an open challenge. (Section 5)
  - [NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1328.pdf)
- **Document understanding** (construct), 1 paper
  > Large language models (LLMs) have advanced to support long-context tasks such as document understanding (Li et al., 2024a), multi-turn dialogues (Yi et al., 2024), repository-level code completion (Jimenez et al., 2024), and complex reasoning (Zhou et al., 2025).
  - [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf)
- **Multi-turn dialogue** (behavioral indicator), 1 paper
  > Large language models (LLMs) have advanced to support long-context tasks such as document understanding (Li et al., 2024a), multi-turn dialogues (Yi et al., 2024), repository-level code completion (Jimenez et al., 2024), and complex reasoning (Zhou et al., 2025).
  - [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf)
- **Code completion** (behavioral indicator), 1 paper
  > Large language models (LLMs) have advanced to support long-context tasks such as document understanding (Li et al., 2024a), multi-turn dialogues (Yi et al., 2024), repository-level code completion (Jimenez et al., 2024), and complex reasoning (Zhou et al., 2025).
  - [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf)
- **Complex reasoning question answering** (behavioral indicator), 1 paper
  > Large language models (LLMs) have advanced to support long-context tasks such as document understanding (Li et al., 2024a), multi-turn dialogues (Yi et al., 2024), repository-level code completion (Jimenez et al., 2024), and complex reasoning (Zhou et al., 2025).
  - [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf)
- **ArgKP21** (measurement instrument), 1 paper
  > Relatedly, we find that ArgKP21 does not fully test the long-context understanding of models. (Section 1)
  - [ArgCMV: An Argument Summarization Benchmark for the LLM-era](https://aclanthology.org/2025.emnlp-main.1110.pdf)
- **Cross-modal retrieval** (behavioral indicator), 1 paper
  > The long-text-image retrieval task necessitates the alignment of text features from long texts with the image features from the corresponding images, which thereby evaluates the model’s ability to comprehend long texts. (Section 4.1)
  - [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf)
- **In-context prediction** (behavioral indicator), 1 paper
  > Handling long-context inputs is crucial for large language models (LLMs) in tasks such as extended conversations, document summarization, and many-shot in-context learning. (Section ABSTRACT)
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
- **Coreference resolution** (behavioral indicator), 1 paper
  > Our method demonstrates the advantages and capabilities of information extraction and coreference resolution in understanding long contexts
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **Personalization** (construct), 1 paper
  > (d) Long-context Modeling Capacity (LC): As more exchanges between the user and the LLM occur, more personal information is gradually revealed, while the limited context length of LLMs makes it increasingly challenging for the LLM to integrate information from past interactions. (Section 3)
  - [Exploring the Potential of LLMs as Personalized Assistants: Dataset, Evaluation, and Analysis](https://aclanthology.org/2025.acl-long.504.pdf)
- **Memory** (construct), 1 paper
  > Despite these improvements, the state sizes of RNNs remain much smaller than those of Transformers with a 2k context length, making state size a critical bottleneck for long-context understanding.
  - [Scaling up the State Size of RNN LLMs for Long-Context Scenarios](https://aclanthology.org/2025.acl-long.564.pdf)
- **Code understanding** (construct), 1 paper
  > We evaluate our DSLA model on tasks requiring careful long-range interactions (Bai et al., 2024), including: ... (ii) Code Understanding, which require reasoning across multiple code files to answer complex questions
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **Few-shot task performance** (behavioral indicator), 1 paper
  > We evaluate our DSLA model on tasks requiring careful long-range interactions (Bai et al., 2024), including: ... (iii) Few-shot learning requires the model to comprehend a limited number of examples and effectively perform various tasks, including classification, summarization, and reading comprehension.
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **Question answering** (behavioral indicator), 1 paper
  > ...achieving substantial progress on tasks such as summarization and question answering that emphasize the effective utilization and understanding of long inputs.
  - [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf)
