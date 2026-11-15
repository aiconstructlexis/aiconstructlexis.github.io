# Long-context reasoning
**Type:** Construct  
**Supporting papers:** 27  
**Also known as:** Long context reasoning, Long-range reasoning, Long-context problem solving, Long-context inference, Context reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, long-context reasoning is most commonly treated as a latent model ability to process, understand, and use information spread across extended input sequences, often by integrating distant pieces of evidence or dependencies into coherent responses. Closely related definitions call it long-range reasoning or context reasoning, and describe it as reasoning over long inputs, long textual contexts, or long sequences while maintaining coherence and accuracy. A smaller line of work narrows the construct to particular settings, such as extended conversation histories and long queries, full HTML pages, long workflow demonstrations, book-length claim verification, or stable output production as input length grows, so the main variation is between broad latent ability definitions and narrower task- or inference-specific formulations.

**Space of facets.** Papers mainly use several near-synonymous labels, long-range reasoning, context reasoning, long-context problem solving, and long-context inference, for overlapping abilities over extended inputs. One recurring contrast is between reasoning over long sequences and relying only on local context, and other quoted passages connect the construct to multi-step reasoning, exploiting long-range dependencies, and maintaining performance over long conversational history. Papers also apply the label across text, dialogue, workflow demonstrations, web pages, graph tasks, and map-based tasks, sometimes alongside algorithmic planning, API interactions, visual map analysis, lower-level process understanding, and human workflow preference alignment.

**Space of measurement.** Operationally, papers link the construct to 12 measurement instruments and 2 behavioral indicators, and the direct measures are benchmark-style datasets. The most commonly linked instruments are BABILong, RULER, 2WikiMultiHopQA, FLenQA, and HotpotQA, with 7 other instruments also used. These operationalizations instantiate the construct as reasoning across facts in extremely long documents, retrieving multiple pieces of evidence from long context and reasoning over them, synthesizing information over long texts, multi-hop reasoning, or handling extended conversation histories; some papers also use narrower book-length claim verification setups.

**Links.** Beyond measurement, one paper claims a causal relationship from long-context reasoning to hallucination, stating that challenges in long-range multi-step reasoning are major contributors to hallucination in larger graphs. Separate papers claim causal relationships from synthetic key-value retrieval tasks to long-context reasoning, via finetuning that improves long-context reasoning capabilities, and from positional bias to long-context reasoning, describing positional bias as an obstacle in long-context reasoning settings. No correlates or generic related links are reported.

## Sources

**Long context reasoning** (2 papers: [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to synthesize and reason over information distributed across extended input sequences, integrating distant pieces of information to form coherent responses.

**Long-context reasoning** (6 papers: [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf), [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf), [TurkingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.188.pdf), [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf), [Does quantization affect models' performance on long-context tasks?](https://aclanthology.org/2025.emnlp-main.479.pdf), [MapEval: A Map-Based Evaluation of Geo-Spatial Reasoning in Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dihan25a/dihan25a.pdf))
> The cognitive ability of a language model to effectively process, understand, and utilize information presented over extended sequences of text.

**Long-range reasoning** (3 papers: [Theoretical Foundations of Deep Selective State-Space Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6231c5f46598cfd09ff1970524e0436-Paper-Conference.pdf), [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf), [PRISM: Efficient Long-Range Reasoning With Short-Context LLMs](https://aclanthology.org/2025.emnlp-main.517.pdf))
> The ability to model and reason over long sequences of information, capturing dependencies between distant elements.

**Long-context problem solving** (1 paper: [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf))
> The ability to handle extended conversation histories and long queries when generating useful responses.

**Long-context inference** (1 paper: [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf))
> Producing outputs while processing very long input contexts without failing as the context length grows.

**Context reasoning** (1 paper: [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf))
> The latent ability of a model to understand and draw inferences from information distributed across a long textual context.

## Relationships

### Long-context reasoning →
- **BABILong** (measurement instrument): *measured_by*, 2 papers
  > To bridge this gap, we introduce the BABILong benchmark, designed to test language models’ ability to reason across facts distributed in extremely long documents.
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
- **RULER** (measurement instrument): *measured_by*, 2 papers
  > The latter two [BABILong and RULER] require models to not only retireve multiple pieces of evidence from the long context, but also reason over them... (Section 4.1)
  - [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 1 paper
  > Long document reasoning performance (%) on Longbench and InfiniteBench (Table 1)
  - [ToM: Leveraging Tree-oriented MapReduce for Long-Context Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.899.pdf)
- **SCROLLS** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the ability of long context reasoning, we compare ICLM with the standard and kNN baselines on the SCROLL benchmark (Shaham et al., 2022) that evaluates LMs’ ability to synthesize information over long texts. (Section 3.3.6)
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
- **ZeroSCROLLS** (measurement instrument): *measured_by*, 1 paper
  > To comprehensively evaluate the long-context reasoning abilities of LLMs, we choose seven tasks from ZeroSCROLLS [34]
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > Thanks to these realistic user activities, WILDBENCH is a more suitable benchmark for testing the long-context problem solving abilities of LLMs. (Section 2.2)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > This trend underscores that larger graph sizes, and their associated challenges in long-range multi-step reasoning, are major contributors to hallucination.
  - [GraphArena: Evaluating and Exploring Large Language Models on Graph Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf)
- **FLenQA** (measurement instrument): *measured_by*, 1 paper
  > FLenQA benchmark (Levy et al., 2024) that measures LLMs’ long-context reasoning capability. (Section 1)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
- **LongBench v2** (measurement instrument): *measured_by*, 1 paper
  > For long-context reasoning on LongBench v2 (R2 = 70.26%), d_ffn overwhelmingly dominates, indicating that wider FFNs are essential for handling extended contexts effectively.
  - [From Parameters to Performance: A Data-Driven Study on LLM Structure and Development](https://aclanthology.org/2025.emnlp-main.1325.pdf)
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > Long document reasoning performance (%) on Longbench and InfiniteBench (Table 1)
  - [ToM: Leveraging Tree-oriented MapReduce for Long-Context Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.899.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > The evaluation is performed on three long-context multi-hop reasoning datasets: Hotpot QA (Yang et al., 2018), MusiQue (Trivedi et al., 2022) and 2WikiMultiHopQA (Ho et al., 2020). (Section 5.1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **MuSiQue** (measurement instrument): *measured_by*, 1 paper
  > The evaluation is performed on three long-context multi-hop reasoning datasets: Hotpot QA (Yang et al., 2018), MusiQue (Trivedi et al., 2022) and 2WikiMultiHopQA (Ho et al., 2020). (Section 5.1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **2WikiMultiHopQA** (measurement instrument): *measured_by*, 1 paper
  > The evaluation is performed on three long-context multi-hop reasoning datasets: Hotpot QA (Yang et al., 2018), MusiQue (Trivedi et al., 2022) and 2WikiMultiHopQA (Ho et al., 2020). (Section 5.1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)

### → Long-context reasoning
- **Key-value retrieval** (behavioral indicator): *causes*, 1 paper
  > Finetuning LLMs on synthetic key-value retrieval tasks improves LLMs’ long-context reasoning capabilities, even if explicit chain-of-thought reasoning is not allowed. (Finding 3)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
- **Positional bias** (construct): *causes*, 1 paper
  > PB poses significant obstacles in information-rich settings, such as retrieval-augmented generation (Fang et al., 2025; Dong et al., 2025b), long-context reasoning (Li et al., 2024a; Kuratov et al., 2024), and LLM-as-a-judge (Wang et al., 2024b; Li et al., 2024c). (Section 1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
