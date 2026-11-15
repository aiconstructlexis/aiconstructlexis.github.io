# Long-form text generation
**Type:** Behavioral indicator  
**Supporting papers:** 33  
**Also known as:** Long-form generation, Open-ended generation, Wikipedia article generation, Coherent multi-paragraph generation, Open-ended long text generation, Long-text generation, Long-response generation, Ultra-long sequence generation, Long-form response generation, Long-sequence generation, Long-text Generation, Document-level generation, Open-domain text generation, Long sequence generation  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is extended response generation: multi-sentence, multi-paragraph, or document-length text produced from a prompt, often in open-ended and context-specific settings. Many definitions emphasize coherent, detailed outputs that contain multiple factual claims, such as biographies, encyclopedic passages, or answers spanning hundreds or thousands of words, while some papers extend the framing to very long sequences above 10,000 tokens or even 100,000 tokens. Papers differ on what counts as success: most stress coherence, contextual relevance, logical flow, informativeness, or factual consistency across the full output, while one vision-language formulation treats the behavior as the length of the generated sequence before termination.

**Variants.** Papers use several neighboring labels and settings for this behavior. Common variants include open-ended generation, sometimes multilingual and explicitly unstructured; Wikipedia article generation, where models synthesize web-sourced information into sectioned articles; coherent multi-paragraph generation from unordered points; open-domain text generation about an entity using only internal knowledge in an encyclopedic style; and ultra-long sequence generation, framed as continuous coherent text up to 100K tokens. Other papers cast the behavior as complete-document or long-response writing, including essays, code, diaries, floorplans, and multimodal detailed image descriptions or extended free-form responses.

**Space of elicitation and scores.** Papers measure this behavior with six linked instruments. The most common are HelloBench and LongGenBench; papers also use LLM-as-a-judge, LLaVA-Bench-in-the-Wild, and LongFact, plus one other instrument. Across these uses, the instruments include evaluation benchmarks, a synthetic benchmark for following instructions over extended sequences, a prompt set of fact-seeking questions for multi-paragraph responses, a judge-based metric, and a multimodal benchmark for extended inference.

**What it is taken as evidence of.** Papers do not converge on a construct that this behavior directly evidences. The only linked construct is Length generalization, and one paper reports that it is related to long-form text generation by noting that effectiveness can diminish when input length exceeds the training length. Outside construct links, one paper claims a causal relationship from Instruction following to long-form text generation, and one paper reports that Code generation is related to it as another long-response task.

## Sources

**Long-form generation** (7 papers: [LoGU: Long-form Generation with Uncertainty Expressions](https://aclanthology.org/2025.acl-long.928.pdf), [Active Layer-Contrastive Decoding Reduces Hallucination in Large Language Model Generation](https://aclanthology.org/2025.emnlp-main.150.pdf), [Cascade Speculative Drafting for Even Faster LLM Inference](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cb5b083ba4f5ca6bd05dd307a2fb354-Paper-Conference.pdf), [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf), [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf), [NICE Data Selection for Instruction Tuning in LLMs with Non-differentiable Evaluation Metric](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bm/wang25bm.pdf), [Resolving Lexical Bias in Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rizwan25a/rizwan25a.pdf))
> Producing extended, coherent text responses (e.g., biographies) that contain multiple factual claims, often spanning hundreds of words.

**Open-ended generation** (1 paper: [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.939.pdf))
> Producing unstructured, long-form text responses to open-ended prompts in multiple languages.

**Long-form text generation** (3 papers: [Bias in Language Models: Beyond Trick Tests and Towards RUTEd Evaluation](https://aclanthology.org/2025.acl-long.7.pdf), [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf), [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf))
> The observable act of producing extended, context-specific text in response to a prompt, as required for many real-world tasks.

**Wikipedia article generation** (1 paper: [Hierarchical Memory Organization for Wikipedia Generation](https://aclanthology.org/2025.acl-long.1423.pdf))
> Producing full-length, structured Wikipedia-style articles from web-sourced information, including section organization and content synthesis.

**Coherent multi-paragraph generation** (1 paper: [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf))
> The specific task of producing a well-structured and logically flowing text composed of multiple paragraphs from a collection of unordered points.

**Open-ended long text generation** (1 paper: [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.260.pdf))
> Producing lengthy, coherent, and informative responses to complex questions that require synthesis of knowledge across multiple topics or domains.

**Long-text generation** (1 paper: [DrDiff: Dynamic Routing Diffusion with Hierarchical Attention for Breaking the Efficiency-Quality Trade-off](https://aclanthology.org/2025.emnlp-main.474.pdf))
> The task of producing coherent and contextually relevant text sequences that are exceptionally long, such as exceeding 10,000 tokens.

**Long-response generation** (1 paper: [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf))
> The task of generating a substantial number of output tokens from a relatively short input prompt, such as in essay writing or code synthesis.

**Ultra-long sequence generation** (1 paper: [TokenSwift: Lossless Acceleration of Ultra Long Sequence Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25z/wu25z.pdf))
> The observable task of producing a continuous, coherent text sequence of exceptional length, such as 100,000 tokens.

**Long-form response generation** (1 paper: [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf))
> The task of generating multi-paragraph, detailed textual answers in response to open-ended prompts.

**Long-sequence generation** (1 paper: [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf))
> The task of generating coherent and relevant text over an extended context, often requiring the model to maintain consistency and track information over thousands of tokens.

**Long-text Generation** (1 paper: [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf))
> The observable behavior of producing coherent and extended text outputs such as articles or stories.

**Document-level generation** (1 paper: [Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf))
> A specific type of long-form generation that requires producing a response structured as a complete document.

**Open-domain text generation** (1 paper: [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf))
> The observable generation of long-form, encyclopedic-style text about a given entity using only the model's internal knowledge, without external retrieval.

**Long sequence generation** (1 paper: [Inducing High Energy-Latency of Large Vision-Language Models with Verbose Images](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a6a5e2e8a27262501bda3463fcf7b21-Paper-Conference.pdf))
> The observable behavior of a vision-language model producing an extended sequence of tokens, measured by the number of generated tokens before termination.

## Relationships

### Long-form text generation →
- **HelloBench** (measurement instrument): *measured_by*, 2 papers
  > Long-text Generation: WikiText (Merity et al., 2016), and HelloBench (Que et al., 2024).
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
  - [PIC: Unlocking Long-Form Text Generation Capabilities of Large Language Models via Position ID Compression](https://aclanthology.org/2025.acl-long.347.pdf)
- **LongGenBench** (measurement instrument): *measured_by*, 2 papers
  > We introduced LongGenBench, a synthetic benchmark that evaluates long-form generation capabilities of language models by testing their ability to follow instructions over extended sequences. (Section 6)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
- **LongFact** (measurement instrument): *measured_by*, 1 paper
  > “LongFact consists of 2,280 fact-seeking prompts that solicit long-form responses across 38 manually-selected topics.”
  - [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf)
- **WikiText** (measurement instrument): *measured_by*, 1 paper
  > Long-text Generation: WikiText (Merity et al., 2016), and HelloBench (Que et al., 2024).
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 1 paper
  > Long Generation: Evaluates extended inference using LLaVABench (Liu et al., 2024b) and MMDU (Liu et al., 2024e). (Section 4.3).
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > the evaluation metrics of instruction-following tasks, especially those that require long-form generations (e.g., LLM-judge (Dubois et al., 2023) and code generation benchmarks (Chen et al., 2021)).
  - [NICE Data Selection for Instruction Tuning in LLMs with Non-differentiable Evaluation Metric](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bm/wang25bm.pdf)

### → Long-form text generation
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > The ability to follow instructions is essential for long text generation (Reversed NIAH1), just as effective information retrieval is fundamental for processing long-context inputs (NIAH(Kamradt, 2023)). (Section 1)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)

### Associated with
- **Length generalization** (construct), 1 paper
  > While transformer-based models exhibit satisfying performances in tasks of consistent length and distribution, their effectiveness tends to diminish sharply when the input length exceeds the training length, e.g., long document summarization, “needle in a haystack” search, and long text generation. (Section 1)
  - [DAPE: Data-Adaptive Positional Encoding for Length Extrapolation](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f050fa9f0d898e3f265d515f50ae8f9-Paper-Conference.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > In contrast, long-response tasks, such as essay writing and code generation, generate a substantial number of output tokens during the decode phase, requiring sustained attention over growing sequences of self-generated tokens. (Section 1)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
