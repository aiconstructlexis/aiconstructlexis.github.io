# Context retrieval
**Type:** Behavioral indicator  
**Supporting papers:** 25  
**Also known as:** In-context retrieval, Fact retrieval, Retrieval capability, Retrieval ability, Semantic retrieval capability  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing treats context retrieval as locating and using relevant information from a long context to answer a query, continue from the input, or complete a task. Many definitions narrow this to recovering a specific fact or item when prompted, including needle-style lookups, while others describe retrieving multiple relevant pieces and synthesizing them, or pointing back to relevant paragraphs by index. A smaller strand defines it semantically, as retrieving information by understanding the query's meaning rather than by exact string match, and some papers cast the retrieved material as relevant facts or reasoning steps from a knowledge base or context.

**Variants.** Authors use several nearby names, including in-context retrieval, fact retrieval, retrieval capability, retrieval ability, and semantic retrieval capability. The settings range from long-sequence retrieval tasks to recovery of random numbers assigned to cities or a single needle among multiple needles, to selecting the top-K most relevant facts by similarity, and to multi-document settings where attention from retrieval heads is used to identify relevant documents. Some papers also study retrieval from textual descriptions or long documents, and a smaller line frames success as pointing back to the relevant context.

**Space of elicitation and scores.** Papers link context retrieval to 6 measurement instruments overall. The prevailing operationalization is through benchmarks, datasets, and retrieval tasks, most often Needle-in-a-Haystack, which papers use to assess long-context retrieval ability, including multi-needle settings where inserted six-digit numbers must be recovered; InfiniteBench is also repeatedly used for context retrieval tasks. HotpotQA, Passkey retrieval, and RULER also measure it in the papers, while 1 other linked instrument appears through a related claim rather than a direct measured_by relation.

**What it is taken as evidence of.** Only 1 construct is linked in the papers. One paper claims a causal relationship from context retrieval to Expressive power, stating that enhancing in-context retrieval can improve RNNs' representation power. No alternative construct link is recorded.

## Sources

**Context retrieval** (1 paper: [Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.275.pdf))
> The action of identifying and extracting relevant segments of information from a larger body of text to address a specific query or task.

**In-context retrieval** (1 paper: [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf))
> The ability to locate and use specific information provided within a long context.

**Fact retrieval** (2 papers: [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf), [RTQA : Recursive Thinking for Complex Temporal Knowledge Graph Question Answering with Large Language Models](https://aclanthology.org/2025.emnlp-main.499.pdf))
> Recovering a specific target fact or item from a long context when prompted.

**Retrieval capability** (2 papers: [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf), [CAFE: Retrieval Head-based Coarse-to-Fine Information Seeking to Enhance Multi-Document QA Capability](https://aclanthology.org/2025.emnlp-main.655.pdf))
> The ability to locate and use relevant information from long contexts when answering or continuing from the input.

**Retrieval ability** (2 papers: [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf), [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf))
> The latent capacity to locate and recover relevant information from long contexts when answering a query.

**Semantic retrieval capability** (1 paper: [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf))
> The ability of a long-context model to understand the semantic meaning of a query to retrieve relevant information, rather than relying on exact string matches.

## Relationships

### Context retrieval →
- **Needle-in-a-Haystack** (measurement instrument): *measured_by*, 3 papers
  > We conduct the Needle-in-a-Haystack test to assess the long-context retrieval ability of different KV cache compression methods.
  - [Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf)
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
  - [Long Context Compression with Activation Beacon](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc797c61eb18f7b3ce9a74af0ef0d876-Paper-Conference.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 2 papers
  > "The datasets in ∞-Bench cover diverse tasks including question answering, summarization, context retrieval, and mathematic computing."
  - [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf)
  - [APB: Accelerating Distributed Long-Context Inference by Passing Compressed Context Blocks across GPUs](https://aclanthology.org/2025.acl-long.525.pdf)
- **Passkey retrieval** (measurement instrument): *measured_by*, 1 paper
  > Additionally, evaluations on the passkey retrieval task [33, 29] reveal that SSA substantially enhances the retrieval capabilities of the transformer, shown in Table 4.
  - [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf)
- **Expressive power** (construct): *causes*, 1 paper
  > Our positive results showing that enhancing in-context retrieval can improve RNNs’ representation power hold for vanilla Linear RNNs, and can be easily extended to more complex architectures. (Section 1)
  - [RNNs are not Transformers (Yet): The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > We further conduct experiments on open-source LLMs based on Transformer, Mambda, and a hybrid architecture to show that for tasks that require stronger in-context retrieval capability, RNNs suffer more performance degradation compared to Transformers. ... To test our theory, we use the Hotpot-QA (Yang et al., 2018) dataset. (Section 6.2)
  - [RNNs are not Transformers (Yet): The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **RULER** (measurement instrument): *measured_by*, 1 paper
  > Notably, APB significantly enhances performance in complex context retrieval tasks, such as R.KV in ∞Bench and MK3 in RULER.
  - [APB: Accelerating Distributed Long-Context Inference by Passing Compressed Context Blocks across GPUs](https://aclanthology.org/2025.acl-long.525.pdf)
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > CoT reasoning, which involves decomposing complex tasks into smaller steps, heavily depends on accurately retrieving detailed information from the input. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)

### Associated with
- **Key-value retrieval** (behavioral indicator), 1 paper
  > RNNs with CoT cannot solve a set of fundamental algorithmic problems that directly ask for in-context retrieval, including associative recall. (Section 1)
  - [RNNs are not Transformers (Yet): The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **MMLU** (measurement instrument), 1 paper
  > we find that MMLU performance is primarily governed by retrieval ability (Section 7).
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)
