# Key-value retrieval
**Type:** Behavioral indicator  
**Supporting papers:** 20  
**Also known as:** Multi-subkey dictionary retrieval, Associative recall, In-context recall, Key-Value Retrieval task  

## State of the Field

**Space of definitions.** Across papers, the dominant framing treats it as retrieving the value associated with a specified key from prior context containing many key-value pairs, often organized as a dictionary, long list, random string pairs, or a large JSON object. Success is usually accurate recovery or generation of the value for the queried key. Several papers present it as a synthetic task, and some explicitly use it to evaluate context awareness; some authors use narrower recall formulations under the same umbrella, such as retrieving a stored value for a queried variable or copying the token that followed an earlier trigger token within the same input.

**Variants.** Papers use several nearby names and harder or narrower settings. Associative recall keeps the same basic pattern of generating a value from a key given a string of key-value tuples, and one multi-query version says that successive queries must recall earlier variable assignments. A smaller line of work studies multi-subkey dictionary retrieval, where each key is a tuple of integers and the model must identify the tuple containing specified subkeys, then report the tuple, its value, and its dictionary; another names in-context recall as a token-copying version, and other instantiations use Python-style UUID pairs or large JSON objects.

**Space of elicitation and scores.** Papers link it to 2 measurement instruments, MQAR and InfiniteBench. MQAR measures the behavior by asking models to predict the value associated with the corresponding key at query positions while ignoring non-query positions, whereas InfiniteBench includes key-value retrieval among extended-context tasks such as summarization and question answering.

**What it is taken as evidence of.** Papers connect this behavior to 4 constructs, and the links do not center on a single construct. It is reported as related to in-context learning, context utilization, and in-context reasoning, while one paper claims a causal relationship from key-value retrieval to long-context reasoning by stating that finetuning on synthetic key-value retrieval tasks improves long-context reasoning capabilities.

## Sources

**Key-value retrieval** (4 papers: [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf), [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf), [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf), [Pointwise Mutual Information as a Performance Gauge for Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.78.pdf))
> The task of extracting the correct value corresponding to a given key from a context containing multiple key-value pairs.

**Multi-subkey dictionary retrieval** (1 paper: [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf))
> Given dictionaries whose keys are tuples of integers, the model identifies the tuple containing specified subkeys and reports the tuple, its value, and its dictionary.

**Associative recall** (1 paper: [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf))
> Retrieving the correct stored value for a queried variable from prior context.

**In-context recall** (1 paper: [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf))
> The observable task of copying a token that follows a previous occurrence of a specific trigger token within the same input context.

**Key-Value Retrieval task** (1 paper: [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf))
> An evaluation task that measures a model's context awareness by requiring it to retrieve a specific value for a given key from a long context of randomly generated key-value pairs.

## Relationships

### Key-value retrieval →
- **MQAR** (measurement instrument): *measured_by*, 2 papers
  > Multi-Query Associative Recall (MQAR) Task. (Figure 1)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
  - [Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ab/huang25ab.pdf)
- **Synthetic recall** (behavioral indicator): *causes*, 2 papers
  > finetuning LLMs on this dataset significantly improves LLMs’ information retrieval and reasoning capabilities in longer-context settings. (ABSTRACT)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
  - [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 1 paper
  > InfiniteBench (Zhang et al., 2024): Designed for LLMs on extended contexts, it includes tasks like key-value retrieval, summarization, and QA on data exceeding 100K tokens.
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
- **Long-context reasoning** (construct): *causes*, 1 paper
  > Finetuning LLMs on synthetic key-value retrieval tasks improves LLMs’ long-context reasoning capabilities, even if explicit chain-of-thought reasoning is not allowed. (Finding 3)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)

### Associated with
- **In-context learning** (construct), 2 papers
  > “we evaluate the capacity of various architectures to in-context learn associative recall”
  - [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf)
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
- **Context retrieval** (behavioral indicator), 1 paper
  > RNNs with CoT cannot solve a set of fundamental algorithmic problems that directly ask for in-context retrieval, including associative recall. (Section 1)
  - [RNNs are not Transformers (Yet): The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **In-context reasoning** (construct), 1 paper
  > Under this definition, we list a few simple examples of reasoning that we will consider below: • In-context recall (Section 2.1).
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
- **Context utilization** (construct), 1 paper
  > We assess the context utilization ability of our approaches on two tasks, including multi-document question answering (MDQA) and key-value retrieval (KV retrieval) tasks from [15]. (Section 4.2)
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
