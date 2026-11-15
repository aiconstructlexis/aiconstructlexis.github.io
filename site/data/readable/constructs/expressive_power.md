# Expressive power
**Type:** Construct  
**Supporting papers:** 70  
**Also known as:** Representation capability, Representation capacity, Representational capacity, Expressiveness, Expressivity, Representation power, Expressive capacity, Model expressiveness, Computational power, Preference expressiveness, Computational expressivity, Function approximation power  

## State of the Field

**Space of definitions.** Most definitions describe expressive power as the range or complexity of functions, tasks, or signals a model can represent, approximate, or solve. Many papers cast it as an in-principle architectural property, often in formal-language or complexity-class terms, and some explicitly separate it from learnability, the training process, or inductive bias. A recurring secondary usage narrows the construct to parameterization or adaptation capacity under efficiency constraints, especially low-rank, shared-rank, or compact updates. Smaller lines of work place the property in token representations, embeddings, prompts or control mechanisms, or in richer preference and value representations, so the main disagreement is over whether expressive power belongs to the architecture, the parameter space, or the learned representations themselves.

**Space of facets.** Papers use several near-synonyms for the same general construct, most often expressivity, expressiveness, representational capacity, computational power, and function approximation power. Within that cluster, one common strand organizes it through formal languages and complexity classes, asking what automata, languages, or circuit classes a model can realize; another treats it as function approximation or matrix reconstruction capacity; and another treats it as richness of internal or embedded representations, such as global context storage, cross-layer diversity, or feature mapping capacity. Smaller specializations reserve the term for preference relations or value representations. Some papers also contrast expressive power with learnability, emphasizing whether a solution is admitted at all rather than whether training will find it.

**Space of measurement.** No measurement instrument is linked to expressive power, and papers link it to 4 behavioral indicators: Chain of thought, Code generation, Context retrieval, and State tracking. Operationalization is mostly analytic rather than benchmark-based, using formal-language recognition and complexity-class results, Turing-completeness or step-count arguments for prompting and chain of thought, matrix reconstruction tests, and proofs about approximating wavelet projections or discontinuous functions. A smaller empirical strand treats lower cross-layer similarity, anisotropic layer representations, or richer feature mappings from larger vocabularies as evidence of greater expressiveness. These choices largely match the dominant definitions by probing what functions, languages, patterns, or representations a model can encode, though some papers instead study expressiveness through transferability limits of continuous prompts or through whether value representations change with demographic context.

**Links.** Several papers claim a causal relationship from Chain of thought and Reasoning to expressive power, describing intermediate reasoning steps as expanding expressiveness beyond TC0 and restrictive output grammars as reducing it. Other incoming causal claims concern retrieval and representation collapse. In the other direction, papers claim causal relationships from expressive power to Mathematical reasoning and other downstream abilities, as well as to client-specific learning. One paper reports that expressive power correlates with Knowledge transfer, and related links connect it to In-context learning and other model-property constructs.

## Sources

**Representational capacity** (2 papers: [Efficient Learning with Sine-Activated Low-Rank Matrices](https://proceedings.iclr.cc/paper_files/paper/2025/file/112d8e0c7563de6e3408b49a09b4d8a3-Paper-Conference.pdf), [Over-Tokenized Transformer: Vocabulary is Generally Worth Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25bb/huang25bb.pdf))
> The degree to which a model's parameterization can encode complex signals or functions while maintaining compactness.

**Expressive power** (2 papers: [Ask, and it shall be given: On the Turing completeness of prompting](https://proceedings.iclr.cc/paper_files/paper/2025/file/123d3e814e257e0781e5d328232ead9b-Paper-Conference.pdf), [On Expressive Power of Looped Transformers: Theoretical Analysis and Enhancement via Timestep Encoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25x/xu25x.pdf))
> The range and complexity of functions or tasks that a model is capable of performing or representing.

**Representation capability** (1 paper: [Theory, Analysis, and Best Practices for Sigmoid Self-Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/a43b459e9fab3a703148ba0c83b8a442-Paper-Conference.pdf))
> The ability of a model architecture to capture and store information, such as global context, within its token representations.

**Representation capacity** (1 paper: [MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf))
> The model's latent ability to form internal representations sufficient for solving a range of tasks, which can be constrained by parameter sharing or rank.

**Expressivity** (2 papers: [Language Models Need Inductive Biases to Count Inductively](https://proceedings.iclr.cc/paper_files/paper/2025/file/378226e5df7eded3e401de5c9493143c-Paper-Conference.pdf), [CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf))
> The range of functions or computational problems that a model architecture is theoretically capable of representing or solving.

**Representation power** (1 paper: [RandLoRA: Full rank parameter-efficient fine-tuning of large models](https://proceedings.iclr.cc/paper_files/paper/2025/file/382b95a6580cfb0b5ca33c74b4e0e770-Paper-Conference.pdf))
> The inherent capacity of a model's parameterization to capture complex functions and patterns required for downstream tasks.

**Expressiveness** (2 papers: [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf), [Lower Bounds for Chain-of-Thought Reasoning in Hard-Attention Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bavandpour25a/bavandpour25a.pdf))
> The capacity of a model's parameter space, such as a prompt, to represent complex functions and capture fine-grained, client-specific patterns.

**Expressive capacity** (2 papers: [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf), [MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25d/xiao25d.pdf))
> The ability of a model or adaptation method to represent or approximate complex functions, often related to the effective rank of its parameter updates.

**Model expressiveness** (1 paper: [ComLoRA: A Competitive Learning Approach for Enhancing LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/e993102e60e4484686f0bafe7ba8b8f2-Paper-Conference.pdf))
> The degree to which a fine-tuned model can represent complex patterns and tasks with limited adaptation capacity.

**Computational power** (1 paper: [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf))
> The set of problems or formal languages that a given neural network architecture is theoretically capable of solving, defining the upper and lower bounds on its reasoning capabilities.

**Function approximation power** (1 paper: [Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ab/huang25ab.pdf))
> The latent ability of a model to represent complex or discontinuous functions by projecting onto appropriate basis functions, such as wavelets, enabling effective modeling of non-smooth signals.

**Computational expressivity** (1 paper: [Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf))
> The capacity of a model to represent complex computational functions, particularly those beyond the circuit complexity of transformers and linear SSMs, such as non-linear and non-diagonal state transitions.

**Preference expressiveness** (1 paper: [Beyond Bradley-Terry Models: A General Preference Model for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25de/zhang25de.pdf))
> The extent to which a model can represent rich, complex preference relations rather than only simple scalar-ordering assumptions.

## Relationships

### Expressive power →
- **Mathematical reasoning** (construct): *causes*, 2 papers
  > the limited expressive capacity of LoRA, stemming from the low-rank constraint, has been recognized as a bottleneck, particularly in rigorous tasks like code generation and mathematical reasoning.
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
- **Knowledge transfer** (construct): *correlates*, 1 paper
  > We observed in Table 3 that a larger source model (either BERTlarge or RoBERTalarge) has lower transfer performance. This aligns with the intuition in Khashabi et al. (2022) that there could be a large number of similarly performing continuous prompts, residing in a large (and also deep) model’s expressive embedding space... Therefore, the induced prompt may carry model specificity in addition to task semantics, limiting its transferability to other models. (Section 3.3)
  - [Zero-Shot Continuous Prompt Transfer: Generalizing Task Semantics Across Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/05f0734db34deb367fc66f1482528044-Paper-Conference.pdf)
- **Code generation** (behavioral indicator): *causes*, 1 paper
  > the limited expressive capacity of LoRA, stemming from the low-rank constraint, has been recognized as a bottleneck, particularly in rigorous tasks like code generation and mathematical reasoning.
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **Personalization** (construct): *causes*, 1 paper
  > The residual term is crucial for retaining the expressiveness lost during the factorization process, thereby preserving the client-specific learning and improving personalization (Section 1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **State tracking** (behavioral indicator): *causes*, 1 paper
  > Transformers, despite their dominance on contemporary language benchmarks, exhibit fundamental limitations in computational expressiveness... they cannot fully recognize regular languages (Bhattamishra et al., 2020) or, equivalently, represent finite state machines (FSMs) (Merrill et al., 2022). This limitation is significant because FSMs form the backbone of many real-world state-tracking problems...
  - [Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf)

### → Expressive power
- **Chain of thought** (behavioral indicator): *causes*, 2 papers
  > we demonstrate that functions computed by Automata, Turing machines, or sparse circuits can be emulated by an ARDT using these intermediate “chain-of-thought” computations. (Section 3)
  - [On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf)
  - [Lower Bounds for Chain-of-Thought Reasoning in Hard-Attention Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bavandpour25a/bavandpour25a.pdf)
- **Reasoning** (construct): *causes*, 2 papers
  > We theoretically show that the loss of expressivity of LLMs under constrained decoding arises because the output grammar G is too restrictive to accommodate the intermediate reasoning steps required to compute the answer. (Section 1)
  - [CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
- **Context retrieval** (behavioral indicator): *causes*, 1 paper
  > Our positive results showing that enhancing in-context retrieval can improve RNNs’ representation power hold for vanilla Linear RNNs, and can be easily extended to more complex architectures. (Section 1)
  - [RNNs are not Transformers (Yet): The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **Representation collapse** (construct): *causes*, 1 paper
  > This phenomenon, often referred to as the “over-smoothing” problem, substantially reduces the transformers’ ability to represent diverse features (Section 1).
  - [Transformer Meets Twicing: Harnessing Unattended Residual Information](https://proceedings.iclr.cc/paper_files/paper/2025/file/90cdfb6ac8d9f96bdf0ce92f5f05c391-Paper-Conference.pdf)

### Associated with
- **In-context learning** (construct), 1 paper
  > We theoretically prove that ICL with transformer is expressive enough to mimic existing meta-learners. (Section 1)
  - [Why In-Context Learning Models are Good Few-Shot Learners?](https://proceedings.iclr.cc/paper_files/paper/2025/file/6c7ca1889f01a9b767c631686fb5fd24-Paper-Conference.pdf)
- **Interpretability and explainability** (construct), 1 paper
  > The trade-off between expressiveness and interpretability remains a core challenge when building human-centric models for classification and decision-making. (ABSTRACT)
  - [Large Language Models are Interpretable Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/887932131fddf943e8fe3310b62c0147-Paper-Conference.pdf)
- **Uniformity** (construct), 1 paper
  > Both isotropy and uniformity are related to the expressiveness of the embeddings (Gao et al., 2021; Rajaee and Pilehvar, 2021a; Zhang et al., 2022). (Section 1)
  - [On the Relation Between Fine-Tuning, Topological Properties, and Task Performance in Sense-Enhanced Embeddings](https://aclanthology.org/2025.acl-long.1151.pdf)
