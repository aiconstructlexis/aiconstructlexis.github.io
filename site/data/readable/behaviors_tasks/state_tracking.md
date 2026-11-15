# State tracking
**Type:** Behavioral indicator  
**Supporting papers:** 9  
**Also known as:** Variable tracking  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage is to treat state tracking as variable tracking in long contexts: keeping track of changing variable values, or monitoring and reporting variable states, when they are updated multiple times through a long context. The formulations largely agree, differing mainly in wording, and one paper makes the target explicit as tracking "the variable assignments provided in the context."

**Variants.** Papers most often name the behavior variable tracking, often abbreviated VT, and study it in synthetic long-context settings. Several descriptions place it in a multi-hop tracing variant with variable tracking, across sequence lengths from 4K to 128K or 131K tokens. A smaller line of work connects state tracking to nearby task settings, especially shortest path finding, multi-hop translation in machine translation, and code generation.

**Space of elicitation and scores.** Papers link state tracking to two measurement instruments. The dominant operationalization is RULER: several papers say state tracking is measured by this synthetic long-context benchmark, which includes variable tracking tasks and a category described as multi-hop tracing with variable tracking. The only other linked instrument is Coin Flip, but there it is only related to state tracking rather than stated to measure it, in a paper that says models can lose track of states as task complexity increases.

**What it is taken as evidence of.** Papers link state tracking to three constructs, and they do not settle on a single construct that it reflects. Some use it as related to long-context understanding, because variable tracking appears in evaluations of long-context capabilities. Another paper relates it to theory of mind, calling basic state tracking a skill underlying theory of mind reasoning, while a separate paper claims a causal relationship from expressive power to state tracking.

## Sources

**Variable tracking** (2 papers: [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf), [xLSTM 7B: A Recurrent LLM for Fast and Efficient Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beck25b/beck25b.pdf))
> The task of keeping track of the changing values of variables that are updated multiple times within a long context.

## Relationships

### State tracking →
- **RULER** (measurement instrument): *measured_by*, 7 papers
  > The RULER benchmark ... encompasses ... tasks involving variable tracking
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
  - [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [Scaling Long Context Training Data by Long-Distance Referrals](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbf49f35b6dd2bef1ad12768c0509daa-Paper-Conference.pdf)
  - [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://aclanthology.org/2025.acl-long.1405.pdf)
  - [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)

### → State tracking
- **Expressive power** (construct): *causes*, 1 paper
  > Transformers, despite their dominance on contemporary language benchmarks, exhibit fundamental limitations in computational expressiveness... they cannot fully recognize regular languages (Bhattamishra et al., 2020) or, equivalently, represent finite state machines (FSMs) (Merrill et al., 2022). This limitation is significant because FSMs form the backbone of many real-world state-tracking problems...
  - [Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf)

### Associated with
- **Coin Flip** (measurement instrument), 1 paper
  > on Coin-Flip and Web-of-Lies, we observe that the model can generate CoT paths that simulate the process step-by-step, but it can easily lose track of the states, especially when the task complexity increases. This reveals model’s intrinsic vulnerability in performing accurate state tracking. (Section 3.2)
  - [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf)
- **Theory of mind** (construct), 1 paper
  > We show that LLMs struggle with basic state tracking, a fundamental skill underlying theory of mind reasoning: tracking mental states necessarily requires being able to track states. (Section 1)
  - [Explore Theory of Mind: program-guided adversarial data generation for theory of mind reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a901d5540789a086ee0881a82211b63d-Paper-Conference.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > In recurrent models, Gated DeltaNet shows consistent advantages, especially in ... Code tasks, demonstrating its superior capabilities in ... state tracking, respectively.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Long-context understanding** (construct), 1 paper
  > To evaluate long-context capabilities, we use the RULER benchmark (Hsieh et al., 2024), which consists of a set of synthetic needle-in-a-haystack, question-answering and variable tracking tasks, with varying context length from 4K to 131K tokens. (Section 5.1)
  - [xLSTM 7B: A Recurrent LLM for Fast and Efficient Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beck25b/beck25b.pdf)
- **Shortest path finding** (behavioral indicator), 1 paper
  > In the Shortest Path task, the model must find the shortest path from a given node to another. Intuitively, to effectively solve the problem, the model should maintain the state of its exploration in the graph
  - [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf)
- **Machine translation** (behavioral indicator), 1 paper
  > A more challenging task, Multi-hop Translation, further requires the model to perform a sequence of translations across multiple languages. ... the model must correctly apply consecutive bilingual dictionaries while keeping track of the translated outputs across the intermediate languages.
  - [SYNC: A Synthetic Long-Context Understanding Benchmark for Controlled Comparisons of Model Capabilities](https://aclanthology.org/2025.emnlp-main.1707.pdf)
