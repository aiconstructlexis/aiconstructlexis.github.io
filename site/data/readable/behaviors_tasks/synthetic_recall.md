# Synthetic recall
**Type:** Behavioral indicator  
**Supporting papers:** 121  
**Also known as:** Passkey retrieval, Needle-in-a-haystack retrieval, Long-context retrieval, Single-needle retrieval, Multi-needle retrieval, Long-dependency retrieval, Prefix-suffix retrieval, Needle question answering, Needle extraction, String retrieval capability, Multimodal retrieval, Information retrieval, Multi-needle reasoning, Synthetic retrieval, Retrieval  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a family of long-context retrieval tasks in which a model must reproduce or extract specific inserted information, the "needle", from a long context or haystack that is often synthetic, irrelevant, or repetitive. A common formulation is passkey retrieval, where the model finds a short five-digit number embedded at some depth in otherwise meaningless text, but other papers frame the target as a statement, fact, string, or other inserted item at varying positions. Success is usually exact recovery of the inserted content, though some settings require all inserted items to be retrieved, and multimodal or audio versions require the response to stay explicitly tied to the located needle.

**Variants.** Most variants stay within text-only needle-in-a-haystack and long-context retrieval, including single-needle and multi-needle versions, with passkey retrieval the most recurring named subtype. Smaller variants add multi-needle reasoning, prefix-suffix dictionary matching, and retrieval of a target item far back in context. Another smaller line extends the setup to multilingual text, mixed text-image documents, and audio Needle QA, where a short segment must be located and reasoned about.

**Space of elicitation and scores.** Papers link synthetic recall to 12 measurement instruments. The most common are Needle-in-a-Haystack, RULER, Passkey retrieval, HELMET, and MM-NIAH: Needle-in-a-Haystack is repeatedly described as inserting a random fact or statement into long text and measuring whether the model retrieves it, RULER as a synthetic benchmark with multiple needle-in-a-haystack variants and other synthetic task types, HELMET as a benchmark category whose synthetic recall tasks are evaluated with SubEM, and MM-NIAH as a multimodal evaluation that detects image or text needles in hybrid long contexts. Additional instruments include NeedleBench and several broader long-context benchmarks.

**What it is taken as evidence of.** Papers link it to 5 constructs, and they do not converge on a single construct it reflects. The prevailing construct-level link is a related one to long-context understanding, with papers describing needle-style retrieval as probing fine-grained contextual understanding or the maximum distance a token can attend to; smaller lines also report it as related to positional bias and temporal perception. Causal claims are sparse and mixed in direction: one paper claims a causal relationship from synthetic recall to personalization, and another claims a causal relationship from recency bias to synthetic recall.

## Sources

**Synthetic recall** (4 papers: [A Silver Bullet or a Compromise for Full Attention? A Comprehensive Study of Gist Token-based Context Compression](https://aclanthology.org/2025.acl-long.241.pdf), [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf), [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf), [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf))
> Reproducing specific, inserted pieces of information (needles) from a long context, testing the fidelity of compressed representations.

**Passkey retrieval** (4 papers: [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf), [Understanding and Improving Length Generalization in Recurrent Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/buitrago25a/buitrago25a.pdf), [A Training-Free Length Extrapolation Approach for LLMs: Greedy Attention Logit Interpolation](https://aclanthology.org/2025.emnlp-main.443.pdf), [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf))
> A "needle in a haystack" task where the model must identify and extract a specific, short piece of information (a passkey) from a long, repetitive document.

**Needle-in-a-haystack retrieval** (3 papers: [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf), [xLSTM 7B: A Recurrent LLM for Fast and Efficient Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beck25b/beck25b.pdf), [Does quantization affect models' performance on long-context tasks?](https://aclanthology.org/2025.emnlp-main.479.pdf))
> The observable task of identifying and extracting a specific piece of information embedded within a large volume of irrelevant text.

**Long-context retrieval** (3 papers: [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf), [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf), [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf))
> Retrieving a target statement or fact from a long input context when it appears at different positions.

**Single-needle retrieval** (1 paper: [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf))
> Finding and recalling a single, specific piece of information ('needle') embedded within a long, distracting context ('haystack').

**Multi-needle retrieval** (1 paper: [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf))
> Finding and recalling multiple, distinct pieces of information ('needles') embedded within a long, distracting context ('haystack').

**Long-dependency retrieval** (1 paper: [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf))
> Recovering a specific target item embedded far back in a long context.

**Prefix-suffix retrieval** (1 paper: [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf))
> Finding a string in a large dictionary that matches both a specified prefix and suffix.

**Needle question answering** (1 paper: [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf))
> Locating and reasoning about a specific short segment (needle) embedded within a longer audio (haystack), requiring precise temporal grounding.

**String retrieval capability** (1 paper: [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf))
> The fundamental ability of a long-context model to retrieve specific, exact-match information from long and potentially noisy input sequences.

**Multimodal retrieval** (1 paper: [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf))
> Answering questions by locating a specific inserted fact, statement, or image within a long multimodal document.

**Information retrieval** (9 papers: [tRAG: Term-level Retrieval-Augmented Generation for Domain-Adaptive Retrieval](https://aclanthology.org/2025.naacl-long.334.pdf), [THREAD: Thinking Deeper with Recursive Spawning](https://aclanthology.org/2025.naacl-long.427.pdf), [FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.597.pdf), [ScreenQA: Large-Scale Question-Answer Pairs Over Mobile App Screenshots](https://aclanthology.org/2025.naacl-long.477.pdf), [AutoEval-ToD: Automated Evaluation of Task-oriented Dialog Systems](https://aclanthology.org/2025.naacl-long.508.pdf), [Multilingual Needle in a Haystack: Investigating Long-Context Behavior of Multilingual Large Language Models](https://aclanthology.org/2025.naacl-long.267.pdf), [AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark](https://aclanthology.org/2025.acl-long.982.pdf), [Dialogue-RAG: Enhancing Retrieval for LLMs via Node-Linking Utterance Rewriting](https://aclanthology.org/2025.acl-long.1191.pdf), [NeuSym-RAG: Hybrid Neural Symbolic Retrieval with Multiview Structuring for PDF Question Answering](https://aclanthology.org/2025.acl-long.311.pdf))
> Locating and extracting a specific piece of information (needle) from a large body of text (haystack), particularly in long and multilingual contexts.

**Multi-needle reasoning** (1 paper: [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf))
> Performing a reasoning task that requires synthesizing information from multiple, distinct facts ('needles') embedded within a long context.

**Synthetic retrieval** (1 paper: [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf))
> The observable behavior of extracting specific, artificially embedded information (e.g., passkeys or key-value pairs) from a long synthetic context.

**Retrieval** (2 papers: [CommVQ: Commutative Vector Quantization for KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25du/li25du.pdf), [Speculative Prefill: Turbocharging TTFT with Lightweight and Training-Free Token Importance Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25g/liu25g.pdf))
> The observable ability of a model to locate and extract specific information from a long input context.

## Relationships

### Synthetic recall →
- **Needle-in-a-Haystack** (measurement instrument): *measured_by*, 11 papers
  > NIAH measures the averaged correct answer rate of the models on the needle-in-a-haystack retrieval task. (Table 4)
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
  - [Forgetting Transformer: Softmax Attention with a Forget Gate](https://proceedings.iclr.cc/paper_files/paper/2025/file/add3d389197ad2267f660ad060ef61f4-Paper-Conference.pdf)
  - [DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c1ddd2e59df46fd2aa85c833b1b36ed-Paper-Conference.pdf)
  - [Hymba: A Hybrid-head Architecture for Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f32def07618040e540e0a6182e290562-Paper-Conference.pdf)
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
  - [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://aclanthology.org/2025.acl-long.1405.pdf)
  - [ClusterAttn: KV Cache Compression under Intrinsic Attention Clustering](https://aclanthology.org/2025.acl-long.703.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)
  - [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf)
- **RULER** (measurement instrument): *measured_by*, 9 papers
  > “RULER includes 8 variants of needle-in-a-haystack retrieval tasks”
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
  - [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
  - [Attention Entropy is a Key Factor: An Analysis of Parallel Context Encoding with Full-attention-based Pre-trained Language Models](https://aclanthology.org/2025.acl-long.485.pdf)
  - [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://aclanthology.org/2025.acl-long.1405.pdf)
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
  - [GSM-$∞$: How Do your LLMs Behave over Infinitely Increasing Reasoning Complexity and Context Length?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25m/zhou25m.pdf)
- **Passkey retrieval** (measurement instrument): *measured_by*, 6 papers
  > The passkey retrieval task as defined in Mohtashami and Jaggi (2023) measures a model’s ability to retrieve a simple passkey (i.e., a five-digit number) from amongst a large amount of otherwise meaningless text. (Section 4.3)
  - [YaRN: Efficient Context Window Extension of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/874a4d89f2d04b4bcf9a2c19545cf040-Paper-Conference.pdf)
  - [Extending LLM Context Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.28.pdf)
  - [Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf)
  - [Rethinking Addressing in Language Models via Contextualized Equivariant Positional Encoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25t/zhu25t.pdf)
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **HELMET** (measurement instrument): *measured_by*, 3 papers
  > we present HELMET (How to Evaluate Long-context Models Effectively and Thoroughly). We curate a diverse set of application-centric long-context tasks across seven categories. Beyond widely adopted categories like synthetic recall...
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **MM-NIAH** (measurement instrument): *measured_by*, 2 papers
  > Our benchmark includes three types of evaluation tasks: multimodal retrieval, counting, and reasoning. (Abstract)
  - [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **NeedleBench** (measurement instrument): *measured_by*, 2 papers
  > NeedleBench (Li et al., 2024a): Tests retrieval and reasoning in complex contexts through three subtasks: Single-Needle Retrieval, Multi-Needle Retrieval, and Multi-Needle Reasoning.
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
- **SWDE** (measurement instrument): *measured_by*, 1 paper
  > Specifically, we assess information retrieval on FDA [93] and SWDE [49], which are designed to evaluate retrieval from in-context passages scraped from HTML/PDFs. (Section 4.1.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Personalization** (construct): *causes*, 1 paper
  > RAG consistently performed the best across most models, indicating that adherence to user preferences may hinge on retrieval capabilities.
  - [Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/28a46044775d97a4efcbcf14e7f13209-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > completely pruning retrieval heads leads to failure in retrieving relevant information and results in hallucination, while pruning random non-retrieval heads does not affect the model’s retrieval ability. (Abstract)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Qasper** (measurement instrument): *measured_by*, 1 paper
  > In long-context retrieval scenario where questions are gathered from Qasper (Dasigi et al., 2021), MoDification-7B-32k yields 10.3 on Qasper, which is competitive with 10.2 from LLaMA-2-7B-32k. (Section 5)
  - [MoDification: Mixture of Depths Made Easy](https://aclanthology.org/2025.naacl-long.265.pdf)
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > On LongBench, we evaluate our method with a range of realistic scenarios, including single-/multi-document QA, document summarization, code completion, information retrieval, etc. (Section 5.1)
  - [ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25b/sun25b.pdf)
- **MileBench** (measurement instrument): *measured_by*, 1 paper
  > The MileBench benchmark also includes needle in haystack tasks for both text and image scenarios. (Section 4.4)
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **LOFT** (measurement instrument): *measured_by*, 1 paper
  > A significant portion of long-context evaluation datasets, including RULER (Hsieh et al., 2024b), LongBench (Bai et al., 2024), LongBench v2 (Bai et al., 2025), and LOFT (Lee et al., 2024), primarily assess retrieval and summarization rather than complex reasoning. (Section 2)
  - [GSM-$∞$: How Do your LLMs Behave over Infinitely Increasing Reasoning Complexity and Context Length?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25m/zhou25m.pdf)
- **LongEval** (measurement instrument): *measured_by*, 1 paper
  > we conduct experiments on LongEval (Li et al., 2023a), a benchmark for long-context retrieval abilities, where we can separate the answer tokens that match the desired answers (e.g., <45129> in Figure 2(a)) from non-answer tokens. (Section 2.1)
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)

### → Synthetic recall
- **Key-value retrieval** (behavioral indicator): *causes*, 2 papers
  > finetuning LLMs on this dataset significantly improves LLMs’ information retrieval and reasoning capabilities in longer-context settings. (ABSTRACT)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
  - [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf)
- **Recency bias** (construct): *causes*, 1 paper
  > “this bias impairs the models’ ability to recall distant information”
  - [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf)

### Associated with
- **Long-context understanding** (construct), 2 papers
  > Passkey retrieval, on the other hand, can effectively measure the maximum distance that a token can attend to during the inference stage. (Section 4.1)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Temporal perception** (construct), 1 paper
  > This task [Retrieval] specifically assesses the model’s capability for temporal perception and understanding across the time dimension. (Section 3.2)
  - [Needle In A Video Haystack: A Scalable Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **Positional bias** (construct), 1 paper
  > In retrieval tasks, PB predominantly manifests as token-shifting... (Section 1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
