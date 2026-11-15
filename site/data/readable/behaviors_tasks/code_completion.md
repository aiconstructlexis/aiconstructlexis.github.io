# Code completion
**Type:** Behavioral indicator  
**Supporting papers:** 25  
**Also known as:** Data science code completion, Fill-in-the-middle code completion, Verilog code completion, Fill in the blank, Next-line prediction, Code auto-completion, Repository-level code completion, Next-line code prediction  

## State of the Field

**Space of definitions.** Across the surveyed work, code completion is most commonly described as generating code continuations from partial code context, often in long-context settings, with the continuation expected to be syntactically and functionally correct. Some papers broaden this to generating or selecting code to finish partially written snippets from requirements, comments, or docstrings, while a smaller line treats it as next-line or next-token prediction; one study also casts structured graph construction as a Python code completion task by asking the model to add relation edges.

**Variants.** Papers study several variants that mainly differ by context scope and domain. Recurring variants include repository-level code completion, which uses whole-repository or cross-file context, fill-in-the-middle, which provides both prefix and suffix, next-line prediction, data science code completion over libraries such as Pandas, NumPy, and PyTorch, and Verilog code completion for partial Verilog snippets; other nearby labels also appear.

**Space of elicitation and scores.** Papers link code completion to 8 measurement instruments. The most frequently linked instrument is LongBench, followed by HumanEval and RepoBench-P, with CrossCodeEval and MBPP also among the most linked instruments; among the linked measures, LongBench treats it as a long-context task category, HumanEval as programming-problem code completion, and RepoBench-P as generating the next line of code from a long code base, and additional instruments are also reported.

**What it is taken as evidence of.** Only one construct is linked to this behavior: Long-context understanding. Papers describe code completion as related to that construct, for example by placing repository-level code completion among long-context tasks, and no other construct link is recorded.

## Sources

**Code completion** (11 papers: [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf), [Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing](https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf), [HyperAttention: Long-context Attention in Near-Linear Time](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5aa940590399350401c57cdf52ce78-Paper-Conference.pdf), [Cascading Large Language Models for Salient Event Graph Generation](https://aclanthology.org/2025.naacl-long.112.pdf), [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf), [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf), [Copilot Arena: A Platform for Code LLM Evaluation in the Wild](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chi25a/chi25a.pdf), [Can You Really Trust Code Copilot? Evaluating Large Language Models from a Code Security Perspective](https://aclanthology.org/2025.acl-long.849.pdf), [FocusLLM: Precise Understanding of Long Context by Dynamic Condensing](https://aclanthology.org/2025.acl-long.1500.pdf), [LADM: Long-context Training Data Selection with Attention-based Dependency Measurement for LLMs](https://aclanthology.org/2025.acl-long.154.pdf), [MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models](https://aclanthology.org/2025.acl-long.560.pdf))
> Generating syntactically and functionally correct code continuations from partial code inputs, particularly under long-context conditions.

**Data science code completion** (1 paper: [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf))
> The task of completing code snippets that use popular data science libraries like Pandas, NumPy, and PyTorch.

**Fill-in-the-middle code completion** (1 paper: [Exact Byte-Level Probabilities from Tokenized Language Models for FIM-Tasks and Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/5ed5c3c846f684a54975ad7a2525199f-Paper-Conference.pdf))
> The task of generating a missing segment of code given the preceding (prefix) and succeeding (suffix) code context.

**Verilog code completion** (1 paper: [CraftRTL: High-quality Synthetic Data Generation for Verilog Code Models with Correct-by-Construction Non-Textual Representations and Targeted Code Repair](https://proceedings.iclr.cc/paper_files/paper/2025/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf))
> The task of completing a partial Verilog code snippet based on the provided context and problem description.

**Fill in the blank** (1 paper: [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf))
> The task of completing missing parts of a code snippet given documentation and context.

**Next-line prediction** (1 paper: [Let the Code LLM Edit Itself When You Edit the Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/9530635032b95cea9585bd800d308300-Paper-Conference.pdf))
> Given code context, the model predicts the next line or next token to complete the snippet.

**Code auto-completion** (1 paper: [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf))
> The task of predicting and generating the next segment of code based on the current context.

**Repository-level code completion** (1 paper: [LV-XAttn: Distributed Cross-Attention for Long Visual Inputs in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25c/chang25c.pdf))
> The task of generating code completions based on the context of an entire software repository.

**Next-line code prediction** (1 paper: [RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d191ba4c8923ed8fd8935b7c98658b5f-Paper-Conference.pdf))
> The observable behavior of generating the next line of code in a file based on both in-file context (preceding lines and imports) and cross-file context (retrieved snippets from other files).

## Relationships

### Code completion →
- **LongBench** (measurement instrument): *measured_by*, 12 papers
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
- **RepoBench-P** (measurement instrument): *measured_by*, 2 papers
  > We pick RepoBench-P [43] which is collected from GitHub repositories, and the model needs to generate the next line of code given the long code base (Section 4.1).
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification](https://aclanthology.org/2025.emnlp-main.343.pdf)
- **HumanEval** (measurement instrument): *measured_by*, 2 papers
  > HumanEval [3] is a code completion benchmark consisting of programming problems assessing language comprehension, algorithms, and simple mathematics (Section 4.1).
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25m/hu25m.pdf)
- **MBPP** (measurement instrument): *measured_by*, 1 paper
  > "a code-generation task that requires the model to complete method bodies from MBPP benchmark [1]"
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
- **TRACE** (measurement instrument): *measured_by*, 1 paper
  > TRACE (Wang et al., 2023b) serves as a challenging continual instruction tuning benchmark comprising 8 diverse tasks, including domain-specific QA, code completion, mathematical reasoning (Section 2).
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **MultiPL-E** (measurement instrument): *measured_by*, 1 paper
  > comparing multilingual code completion averages on Multipl-E (Cassano et al., 2023)
  - [ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding](https://proceedings.iclr.cc/paper_files/paper/2025/file/23ff02034404b65776080cbf7148addd-Paper-Conference.pdf)
- **RepoEval** (measurement instrument): *measured_by*, 1 paper
  > we also evaluate the effectiveness of HLP on repository-level code Fill-in-the-Middle in cross-file scenarios via CrossCodeEval (Ding et al., 2023), CrossCodeLongEval (Wu et al., 2024), and RepoEval (Zhang et al., 2023). (Section 4.2)
  - [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1672.pdf)
- **CrossCodeEval** (measurement instrument): *measured_by*, 1 paper
  > we also evaluate the effectiveness of HLP on repository-level code Fill-in-the-Middle in cross-file scenarios via CrossCodeEval (Ding et al., 2023), CrossCodeLongEval (Wu et al., 2024), and RepoEval (Zhang et al., 2023). (Section 4.2)
  - [Planning-Aware Code Infilling via Horizon-Length Prediction](https://aclanthology.org/2025.emnlp-main.1672.pdf)

### Associated with
- **Long-context understanding** (construct), 1 paper
  > Large language models (LLMs) have advanced to support long-context tasks such as document understanding (Li et al., 2024a), multi-turn dialogues (Yi et al., 2024), repository-level code completion (Jimenez et al., 2024), and complex reasoning (Zhou et al., 2025).
  - [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf)
