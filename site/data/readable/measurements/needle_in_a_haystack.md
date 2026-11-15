# Needle-in-a-Haystack
**Type:** Measurement instrument  
**Supporting papers:** 49  
**Also known as:** Needle-in-the-Haystack, Needle in A Haystack, Needle In A Haystack, Needle in a Haystack, Needle-In-A-Haystack, Needle-in-a-haystack, Needle-in-the-haystack, Needle in A Haystack test, Needle in a haystack test, Needle-in-the-Haystack test, Needle-in-the-haystack test, NIAH, Needle-in-a-Haystack (NIAH), Needle-in-Haystack, Needle-in-a-haystack test, Needle in the Haystack test  

## State of the Field

**What it is.** Across papers, Needle-in-a-Haystack, often abbreviated NIAH, is most commonly described as a synthetic long-context retrieval benchmark or evaluation procedure, and several authors call it a popular or widely used pressure or stress test. The prevailing setup inserts a fact, statement, answer, sentence, or key-value pair, the "needle", at varying depths or positions inside a long irrelevant or distracting document or text, the "haystack", then queries the model to retrieve it. Some definitions emphasize controlled insertion depth, and one reported setup uses a four-needle variant with multiple inserted items.

**What it is claimed to measure.** Papers use it to measure five constructs and three behavioral indicators. The most frequently linked constructs start with long-context understanding and contextual understanding, while the most frequent behavioral links are synthetic recall, context retrieval, and information retrieval; the remaining links cover three other constructs. These claims are spread across several constructs, though the recurring use is to assess retrieval from long contexts, including correct answer rate on the task and whether models can locate inserted facts across varying positions and context lengths.

**Space of uses.** Papers often position it as a retrieval-focused pressure or stress test, sometimes as a preliminary check of long-context capability and sometimes as a downstream evaluation for methods such as context extension, KV cache compression, or context pruning. It is frequently used alongside LongBench, and also appears with RULER and SCBench; papers explicitly relate it to two other instruments, RULER and OpenCompass, and some treat it as a task included within RULER rather than only as a standalone benchmark.

**Concerns raised.** A smaller line of work flags a limitation of the benchmark's synthetic format: one paper notes that synthetic benchmarks such as needle-in-the-haystack may be inadequate for evaluating real long-context RAG scenarios. Another says that many benchmarks built on this test focus on simple retrieval-based experiments.

## Sources

**Needle-in-the-Haystack** (2 papers: [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf), [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf))
> A long-context retrieval benchmark that tests whether a model can find a target item embedded in a long document-style context.

**Needle-in-a-Haystack** (10 papers: [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf), [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf), [SepLLM: Accelerate Large Language Models by Compressing One Segment into One Separator](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bf/chen25bf.pdf), [AnchorAttention: Difference-Aware Sparse Attention with Stripe Granularity](https://aclanthology.org/2025.emnlp-main.430.pdf), [GraphKV: Breaking the Static Selection Paradigm with Graph-Based KV Cache Eviction](https://aclanthology.org/2025.emnlp-main.1112.pdf), [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf), [Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query](https://aclanthology.org/2025.emnlp-main.1732.pdf), [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf), [UNComp: Can Matrix Entropy Uncover Sparsity? — A Compressor Design from an Uncertainty-Aware Perspective](https://aclanthology.org/2025.emnlp-main.209.pdf), [When Long Helps Short: How Context Length in Supervised Fine-tuning Affects Behavior of Large Language Models](https://aclanthology.org/2025.emnlp-main.522.pdf))
> An evaluation test where a specific, irrelevant fact (the "needle") is placed at various depths within a long, distracting text (the "haystack"), and the model is queried to retrieve it.

**Needle-In-A-Haystack** (1 paper: [Differential Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/00b67df24009747e8bbed4c2c6f9c825-Paper-Conference.pdf))
> An evaluation test designed to measure a model's ability to retrieve a specific piece of information (the "needle") embedded within a long, distracting context (the "haystack").

**Needle-in-the-Haystack test** (1 paper: [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf))
> A benchmark that assesses a model's ability to retrieve a specific piece of information ('needle') embedded deep within a long, distracting context ('haystack').

**Needle-in-a-haystack** (1 paper: [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf))
> An evaluation procedure where a specific fact (the "needle") is placed within a long, irrelevant text (the "haystack") to test a model's information retrieval capability.

**Needle in A Haystack** (1 paper: [RazorAttention: Efficient KV Cache Compression Through Retrieval Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/2a98af4fea6a24b73af7b588ca95f755-Paper-Conference.pdf))
> A benchmark designed to evaluate a model's ability to retrieve a specific, targeted piece of information ('the needle') placed at various depths within a long, distracting document ('the haystack').

**Needle in A Haystack test** (1 paper: [NovelQA: Benchmarking Question Answering on Documents Exceeding 200K Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/file/3adb85a348a18cdd74ce99fbbab20301-Paper-Conference.pdf))
> An evaluation procedure that tests information retrieval in long contexts by inserting a distinct, unrelated sentence (the "needle") into a long document (the "haystack") and asking the model to retrieve it.

**Needle-in-the-haystack** (1 paper: [Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf))
> A synthetic benchmark designed to test a model's ability to retrieve a specific piece of information from a long, distracting context, noted as potentially inadequate for evaluating real-world RAG challenges.

**Needle-in-the-haystack test** (1 paper: [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf))
> A controlled experiment designed to evaluate a model's ability to find and use a small piece of relevant information ('needle') placed within a larger, irrelevant context ('haystack').

**Needle In A Haystack** (1 paper: [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf))
> An evaluation task designed to test a model's ability to retrieve a specific piece of information ('needle') embedded within a long, distracting context ('haystack').

**Needle in a haystack test** (1 paper: [Needle Threading: Can LLMs Follow Threads Through Near-Million-Scale Haystacks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/acfcb9e8f066f14cab7368e07cfab5be-Paper-Conference.pdf))
> A general evaluation paradigm for long-context retrieval where a small, relevant piece of information (the 'needle') is placed within a large volume of irrelevant text (the 'haystack') to test if a model can find it.

**Needle in a Haystack** (1 paper: [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf))
> A long-context retrieval benchmark in which a statement is inserted into a long document and the model must retrieve it from context.

**NIAH** (1 paper: [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf))
> Needle in a Haystack, a benchmark designed to test if a model can retrieve a small, specific piece of information ('needle') placed within a long, irrelevant context ('haystack').

**Needle-in-a-Haystack (NIAH)** (1 paper: [RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/behnam25a/behnam25a.pdf))
> An evaluation procedure that tests a model's ability to retrieve a specific piece of information ('needle') embedded within a long, distracting text ('haystack').

**Needle-in-Haystack** (2 papers: [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf))
> An evaluation task that tests a model's ability to retrieve a specific piece of information (the "needle") intentionally placed within a long, distracting context (the "haystack").

**Needle-In-A-Haystack test** (1 paper: [DINT Transformer](https://aclanthology.org/2025.emnlp-main.495.pdf))
> Evaluation protocol that assesses a model's ability to retrieve specific target information (a 'needle') embedded in a long context (a 'haystack'), typically using synthetic data with controlled insertion depth.

**Needle in the Haystack test** (1 paper: [GATEAU: Selecting Influential Samples for Long Context Alignment](https://aclanthology.org/2025.emnlp-main.375.pdf))
> A retrieval-style evaluation that inserts a fact into a long context and asks the model to retrieve it from different depth positions.

## Relationships

### → Needle-in-a-Haystack
- **Synthetic recall** (behavioral indicator): *measured_by*, 11 papers
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
- **Long-context understanding** (construct): *measured_by*, 7 papers
  > Additionally, we assess the CREAM-Chat model with Needle-in-a-Haystack and LongBench[Bai et al., 2023]. (Section 3.1).
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
  - [DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c1ddd2e59df46fd2aa85c833b1b36ed-Paper-Conference.pdf)
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
  - [Hymba: A Hybrid-head Architecture for Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f32def07618040e540e0a6182e290562-Paper-Conference.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Context retrieval** (behavioral indicator): *measured_by*, 3 papers
  > We conduct the Needle-in-a-Haystack test to assess the long-context retrieval ability of different KV cache compression methods.
  - [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf)
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
  - [Long Context Compression with Activation Beacon](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc797c61eb18f7b3ce9a74af0ef0d876-Paper-Conference.pdf)
- **Length generalization** (construct): *measured_by*, 1 paper
  > We measure the extent to which DeBERTa generalizes to longer sequences with the ‘needle in a haystack’ test from RULER (Hsieh et al., 2024). (Section 2.3)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > We design a needle-in-the-haystack experiment which allows us to ... evaluate its robustness w.r.t. the position of the relevant information in the input context. (Section 4.3)
  - [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf)
- **Contextual understanding** (construct): *measured_by*, 1 paper
  > We also conduct Needle-in-a-Haystack tests (gkamradt, 2023) to provide a comprehensive evaluation of both context awareness and extrapolation. (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > To investigate whether the LOGO training strategy affects the information retrieval capabilities of LCMs, we conduct a Needle-in-a-Haystack (NIAH) testing (gkamradt, 2023). (Section 4.2)
  - [LOGO — Long cOntext aliGnment via efficient preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25j/tang25j.pdf)
- **Long-range dependency modeling** (construct): *measured_by*, 1 paper
  > "The Needle-in-the-Haystack test assesses LLMs’ ability to handle long-dependency tasks"
  - [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf)

### Associated with
- **RULER** (measurement instrument), 2 papers
  > Ruler evaluates models across tasks like NIAH and multi-hop tracing. (Section 5)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
  - [Scaling Long Context Training Data by Long-Distance Referrals](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbf49f35b6dd2bef1ad12768c0509daa-Paper-Conference.pdf)
- **OpenCompass** (measurement instrument), 1 paper
  > Needle-In-A-Haystack (Contributors, 2023a) implemented in OpenCompass (Contributors, 2023b). (Figure 2)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
