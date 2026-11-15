# RULER
**Type:** Measurement instrument  
**Supporting papers:** 64  
**Also known as:** Ruler  

## State of the Field

**What it is.** Most papers describe RULER as a synthetic long-context benchmark or dataset for evaluating LLMs, often emphasizing controllable or customizable sequence lengths and task complexity. The prevailing description is a suite of 13 tasks across four categories, with papers variously spelling these out as Needle-in-a-Haystack retrieval, multi-hop tracing or variable tracking, aggregation or common and frequent word extraction, and question answering; some also say it challenges the true context window length or evaluates effective context length. A smaller description treats it more generally as a benchmark suite for long-context capabilities, and one mention refers to five categories.

**What it is claimed to measure.** Papers link RULER to 5 constructs and 9 behavioral indicators. The dominant use is to measure long-context understanding, while smaller lines of work use it for length generalization, long-context reasoning, long-range dependency modeling, and multi-hop reasoning. At the behavioral level, it is most often used for synthetic recall and state tracking, with additional uses for question answering, context retrieval, and document question answering, plus 4 other indicators, so the measurement claims are spread across several closely related long-context abilities rather than a single target.

**Space of uses.** Across experiments, papers usually include RULER as one of a small set of long-context benchmarks, for example alongside LongBench, Needle-in-a-Haystack, InfiniteBench, and LV-Eval. They often report results across various or increasing context lengths, and some studies use selected RULER subtasks, such as variable tracking, common or frequent word extraction, passkey retrieval, or qa-1, rather than the full suite. Papers also relate it to 3 other instruments, most often Needle-in-a-Haystack, with BABILong and one other instrument also noted.

**Concerns raised.** Explicit concerns are limited. A rare critique groups RULER with long-context datasets that primarily assess retrieval and summarization rather than complex reasoning, framing a scope concern about what the benchmark measures.

## Sources

**RULER** (9 papers: [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf), [Untie the Knots: An Efficient Data Augmentation Strategy for Long-Context Pre-Training in Language Models](https://aclanthology.org/2025.acl-long.62.pdf), [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf), [SWAN: An Efficient and Scalable Approach for Long-Context Language Modeling](https://aclanthology.org/2025.emnlp-main.123.pdf), [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf), [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf), [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf), [Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf), [Stress-Testing Long-Context Language Models with Lifelong ICL and Task Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc8db5884a7474b4771762b6f0c8ee1-Paper-Datasets_and_Benchmarks_Track.pdf))
> A synthetic benchmark dataset created to evaluate long-context LLMs with customizable sequence lengths and task complexities, including tasks like needle-in-a-haystack, multi-hop tracing, and aggregation.

**Ruler** (1 paper: [MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/13f972adf12bdf886583d48cd528002f-Paper-Conference.pdf))
> A benchmark suite designed to evaluate the long-context capabilities of language models across various tasks.

## Relationships

### → RULER
- **Long-context understanding** (construct): *measured_by*, 14 papers
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
- **Synthetic recall** (behavioral indicator): *measured_by*, 9 papers
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
- **State tracking** (behavioral indicator): *measured_by*, 7 papers
  > The RULER benchmark ... encompasses ... tasks involving variable tracking
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
  - [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [Scaling Long Context Training Data by Long-Distance Referrals](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbf49f35b6dd2bef1ad12768c0509daa-Paper-Conference.pdf)
  - [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://aclanthology.org/2025.acl-long.1405.pdf)
  - [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > Figure 5 illustrates the trade-off between two representative KV sparsification algorithms, SnapKV and PQCache, and their respective theoretical speedups on three distinct Ruler tasks: needle in a haystack with passkeys 3 (niah-multikeys-3), common word extraction (cwe), and question answering 1 (qa-1). (Section 4.4)
  - [MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/13f972adf12bdf886583d48cd528002f-Paper-Conference.pdf)
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
- **Long-context reasoning** (construct): *measured_by*, 2 papers
  > The latter two [BABILong and RULER] require models to not only retireve multiple pieces of evidence from the long context, but also reason over them... (Section 4.1)
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **Length generalization** (construct): *measured_by*, 2 papers
  > Benchmarks of Long Context Generalization (Section 5.2)
  - [LongRecipe: Recipe for Efficient Long Context Generalization in Large Language Models](https://aclanthology.org/2025.acl-long.581.pdf)
  - [SWAN: An Efficient and Scalable Approach for Long-Context Language Modeling](https://aclanthology.org/2025.emnlp-main.123.pdf)
- **Multi-hop question answering** (behavioral indicator): *measured_by*, 1 paper
  > RULER reports the averaged accuracy on two multi-hop question answering subtasks from RULER. (Table 4)
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
- **Information synthesis** (behavioral indicator): *measured_by*, 1 paper
  > “RULER (Hsieh et al., 2024): a synthetic benchmark with 13 tasks categorized into 4 domains: Needle-in-a-Haystack (Retrieval), Multi-Hop Tracing, Aggregation, and Question Answering.”
  - [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf)
- **Document question answering** (behavioral indicator): *measured_by*, 1 paper
  > "The RULER benchmark (Hsieh et al., 2024) encompasses a variety of synthetic tasks, including eight variants of Needle-in-a-Haystack (NIAH), as well as tasks involving variable tracking, counting, and long-context question answering (QA)."
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
- **Multi-hop reasoning** (construct): *measured_by*, 1 paper
  > "RULER generates synthetic tasks across multiple categories, including multi-hop reasoning and document tracing, and measures the model’s accuracy."
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **Context retrieval** (behavioral indicator): *measured_by*, 1 paper
  > Notably, APB significantly enhances performance in complex context retrieval tasks, such as R.KV in ∞Bench and MK3 in RULER.
  - [APB: Accelerating Distributed Long-Context Inference by Passing Compressed Context Blocks across GPUs](https://aclanthology.org/2025.acl-long.525.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > RULER (Hsieh et al., 2024) is a suite of synthetically created tasks with controllable lengths, which ranges from retrieval, multi-hop tracking, real QA datasets, and context aggregation tasks. (Section 4.5)
  - [Speculative Prefill: Turbocharging TTFT with Lightweight and Training-Free Token Importance Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25g/liu25g.pdf)
- **Long-range dependency modeling** (construct): *measured_by*, 1 paper
  > Extensive experiments on the HELMET(Yen et al., 2024b) and RULER(Hsieh et al., 2024) benchmarks demonstrate that NExtLong significantly improves the model’s ability to capture and utilize long-range dependencies. (Section 1. Introduction)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Text summarization** (behavioral indicator): *measured_by*, 1 paper
  > A significant portion of long-context evaluation datasets, including RULER (Hsieh et al., 2024b), LongBench (Bai et al., 2024), LongBench v2 (Bai et al., 2025), and LOFT (Lee et al., 2024), primarily assess retrieval and summarization rather than complex reasoning. (Section 2)
  - [GSM-$∞$: How Do your LLMs Behave over Infinitely Increasing Reasoning Complexity and Context Length?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25m/zhou25m.pdf)

### Associated with
- **Needle-in-a-Haystack** (measurement instrument), 2 papers
  > Ruler evaluates models across tasks like NIAH and multi-hop tracing. (Section 5)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
  - [Scaling Long Context Training Data by Long-Distance Referrals](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbf49f35b6dd2bef1ad12768c0509daa-Paper-Conference.pdf)
- **BABILong** (measurement instrument), 1 paper
  > RULER, a recently proposed long-context benchmark, shares a similar "needle-in-a-haystack" concept with BABILong.
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **HELMET** (measurement instrument), 1 paper
  > “For this category, we select multiple synthetic recall tasks from RULER (an extended version of NIAH; Hsieh et al., 2024) and also add a JSON KV retrieval task (Liu et al., 2023), which we find more challenging.”
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
