# Length generalization
**Type:** Construct  
**Supporting papers:** 66  
**Also known as:** Length generalizability, Length extrapolation, Context Length Generalizability, Generative length extrapolation, Size generalisation, Extrapolation ability, Long-context generalization  

## State of the Field

**Space of definitions.** Most commonly, papers use length generalization for the ability to keep performance when a model trained or pre-trained on shorter sequences is applied to longer ones, often phrased as "training on short, testing on long" and as avoiding performance degradation beyond the training length. A recurring variant treats this as a latent ability to apply a learned algorithm or procedure to longer inputs, and one paper says evaluation on longer and harder problems is used as a proxy for whether the model learned a scalable solution rather than memorizing patterns. Smaller lines of work narrow the construct to longer programs, longer narratives in math word problems, longer speech generation, more input items, or sequence generation beyond the trained duration, and one definition extends it to unseen shorter as well as longer lengths.

**Space of facets.** Papers do not present a single settled taxonomy. One framing separates downward OOD and upward OOD generalization, while another treats adaptation to varying numbers of context examples as one dimension of length generalization. Naming is also loose: length extrapolation, long-context generalization, context length generalizability, size generalisation, and generative length extrapolation are used for closely related short-to-long generalization phenomena, though some usages shift the object from sequence length in general to program length, input-item count, or generation duration. A smaller line of work explicitly says easy-to-hard generalization in its setting is a type of length generalization.

**Space of measurement.** Operationalization is broad but mostly benchmark-based: papers link the construct to 16 measurement instruments and 3 behavioral indicators. The most frequently linked instruments are Books3, InfiniteBench, PG-19, RULER, and Arxiv, with Books3 and PG-19 used in perplexity or held-out-document evaluations, RULER and InfiniteBench used as long-context benchmarks, and Arxiv used as a real-world dataset; other instruments include a needle-in-a-haystack test, packed longer-sequence evaluation, and long-context memory benchmarks. The behavioral settings are arithmetic, counting, and long-form generation, so most measurements mirror the dominant short-to-long definition, while some target long-context memory or application-focused long inputs.

**Links.** Several papers describe length generalization as related to long-context understanding, and another paper frames it as related to reasoning. A smaller line of work explicitly treats easy-to-hard generalization as a type of length generalization. Causal claims are sparse but present: one paper claims a causal relationship from simplicity bias to length generalization, and another claims a causal relationship from effective receptive field to length generalization. Related behavioral contexts include arithmetic, counting, and long-form generation, and other papers also connect the construct to broader generalization and model-property discussions.

## Sources

**Length generalization** (10 papers: [ExeDec: Execution Decomposition for Compositional Generalization in Neural Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/c43b2989b1ba055aa713a4abbe4a8b05-Paper-Conference.pdf), [Functional Interpolation for Relative Positions improves Long Context Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f55a8b7b1c2c6312eb86557bb9a2bd5-Paper-Conference.pdf), [Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks](https://proceedings.iclr.cc/paper_files/paper/2024/file/72679d76c80e079c70fe5977d21ed1e4-Paper-Conference.pdf), [Teaching Arithmetic to Small Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf), [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf), [How Far Can Transformers Reason? The Globality Barrier and Inductive Scratchpad](https://proceedings.neurips.cc/paper_files/paper/2024/file/3107e4bdb658c79053d7ef59cbc804dd-Paper-Conference.pdf), [Rethinking Invariance in In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/01e8ecf628f8d9f62a1fd433d44d34ab-Paper-Conference.pdf), [Principled Understanding of Generalization for Generative Transformer Models in Arithmetic Reasoning Tasks](https://aclanthology.org/2025.acl-long.235.pdf), [Understanding and Improving Length Generalization in Recurrent Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/buitrago25a/buitrago25a.pdf), [Circuit Complexity Bounds for RoPE-based Transformer Architecture](https://aclanthology.org/2025.emnlp-main.561.pdf))
> The ability of a model to be trained on shorter sequences and then be applied to longer sequences without performance degradation.

**Length generalizability** (1 paper: [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf))
> The ability of a large language model to effectively process sequences that are longer than those it was exposed to during its pre-training phase.

**Context Length Generalizability** (1 paper: [Can LLMs Solve Longer Math Word Problems Better?](https://proceedings.iclr.cc/paper_files/paper/2025/file/474ada926b331d78f06d95e8913111cc-Paper-Conference.pdf))
> The ability of a Large Language Model to solve math word problems with extended narratives or lengthy contexts.

**Length extrapolation** (2 papers: [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf), [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf))
> The ability to effectively process sequences that are longer than any seen during the training phase.

**Long-context generalization** (2 papers: [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf), [EpMAN: Episodic Memory AttentioN for Generalizing to Longer Contexts](https://aclanthology.org/2025.acl-long.574.pdf))
> The ability of a model to maintain its performance and effectiveness when processing input sequences that are significantly longer than those it was exposed to during its pre-training phase.

**Generative length extrapolation** (1 paper: [Long-Form Speech Generation with Spoken Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25k/park25k.pdf))
> The ability to maintain high-quality and coherent generation for durations significantly longer than those seen during training.

**Size generalisation** (1 paper: [Softmax is not Enough (for Sharp Size Generalisation)](https://raw.githubusercontent.com/mlresearch/v267/main/assets/velickovic25a/velickovic25a.pdf))
> The ability of a model to maintain performance on tasks when the number of input items exceeds the maximum seen during training, particularly relevant for reasoning tasks over variable-length sequences.

**Extrapolation ability** (1 paper: [BehaviorGPT: Smart Agent Simulation for Autonomous Driving with Next-Patch Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9144c7c014bf4c30e88f650bef8f68dd-Paper-Conference.pdf))
> The model's capability to generate coherent and realistic sequences that are longer than the sequences it was trained on.

## Relationships

### Length generalization →
- **Books3** (measurement instrument): *measured_by*, 2 papers
  > Figure 2: Perplexity of larger bases on Books3 (Presser, 2020) shows better extrapolation.
  - [Scaling Laws of RoPE-based Extrapolation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d33b741600f100b31256c70a46f66ec9-Paper-Conference.pdf)
  - [DAPE: Data-Adaptive Positional Encoding for Length Extrapolation](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f050fa9f0d898e3f265d515f50ae8f9-Paper-Conference.pdf)
- **PG-19** (measurement instrument): *measured_by*, 2 papers
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
  - [SWAN: An Efficient and Scalable Approach for Long-Context Language Modeling](https://aclanthology.org/2025.emnlp-main.123.pdf)
- **RULER** (measurement instrument): *measured_by*, 2 papers
  > Benchmarks of Long Context Generalization (Section 5.2)
  - [LongRecipe: Recipe for Efficient Long Context Generalization in Large Language Models](https://aclanthology.org/2025.acl-long.581.pdf)
  - [SWAN: An Efficient and Scalable Approach for Long-Context Language Modeling](https://aclanthology.org/2025.emnlp-main.123.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 2 papers
  > We compare our method with existing length extrapolation approaches... on LongBench (Bai et al., 2023) and InfiniteBench (Zhang et al., 2024)... (Section 5.1)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
  - [TokenSelect: Efficient Long-Context Inference and Length Extrapolation for LLMs via Dynamic Token-Level KV Cache Selection](https://aclanthology.org/2025.emnlp-main.1079.pdf)
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > We compare our method with existing length extrapolation approaches... on LongBench (Bai et al., 2023) and InfiniteBench (Zhang et al., 2024)... (Section 5.1)
  - [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf)
- **Arxiv** (measurement instrument): *measured_by*, 1 paper
  > Experimental validation on real-world datasets (Arxiv, Books3, and CHE) demonstrates that DAPE enhances model performances in terms of trained length and length generalization, where the improvements are statistically significant. (Abstract)
  - [DAPE: Data-Adaptive Positional Encoding for Length Extrapolation](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f050fa9f0d898e3f265d515f50ae8f9-Paper-Conference.pdf)
- **Needle-in-a-Haystack** (measurement instrument): *measured_by*, 1 paper
  > We measure the extent to which DeBERTa generalizes to longer sequences with the ‘needle in a haystack’ test from RULER (Hsieh et al., 2024). (Section 2.3)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **GovReport** (measurement instrument): *measured_by*, 1 paper
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **QMSum** (measurement instrument): *measured_by*, 1 paper
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **NarrativeQA** (measurement instrument): *measured_by*, 1 paper
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Qasper** (measurement instrument): *measured_by*, 1 paper
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **CodeParrot** (measurement instrument): *measured_by*, 1 paper
  > Figure 2: Length extrapolation on six long benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **DoTA (traffic accident analysis)** (measurement instrument): *measured_by*, 1 paper
  > Long Context... mean testing on the... DoTA long context subset (Table 1).
  - [Single-to-mix Modality Alignment with Multimodal Large Language Model for Document Image Machine Translation](https://aclanthology.org/2025.acl-long.606.pdf)
- **The Pile (deduplicated)** (measurement instrument): *measured_by*, 1 paper
  > To assess their capability for length extrapolation, we evaluated the implicit models on the test split of the D-PILE, which was packed with longer sequences consisting of 4096, 8192, and 16384 tokens. (Section 5)
  - [Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf)
- **LongMemEval** (measurement instrument): *measured_by*, 1 paper
  > To assess long-context memory and extrapolation ability, two benchmarks are adopted: a chat-form benchmark LONGMEMEVAL... (Section 1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **HELMET** (measurement instrument): *measured_by*, 1 paper
  > To assess long-context memory and extrapolation ability, two benchmarks are adopted: ... an application-centric benchmark HELMET (Yen et al., 2024). (Section 1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)

### → Length generalization
- **Simplicity bias** (construct): *causes*, 1 paper
  > Toy Model (RASP Learning). For symbolic tasks, Transformers tend to learn the shortest RASP-L program which fits the training set, if one exists. Thus, if this minimal program exists and correctly length-generalizes, then so will the Transformer. (Section 1)
  - [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf)
- **Effective receptive field** (construct): *causes*, 1 paper
  > Through a series of visualizations, analyses, and empirical measures, recognize that although Mamba can theoretically capture global interactions via the recurrent state, its limited ERF prevents significant length-extrapolation; (Section 1)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)

### Associated with
- **Long-context understanding** (construct), 3 papers
  > Length extrapolation methods, although theoretically capable of extending the context window beyond the training sequence length, often underperform in practical long-context applications. (Section 1)
  - [CLEX: Continuous Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
  - [Long-Short Alignment for Effective Long-Context Modeling in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25a/du25a.pdf)
  - [Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25v/hu25v.pdf)
- **Easy-to-hard generalization** (construct), 2 papers
  > “we investigate whether these models are capable of logical extrapolation—can they solve problems of greater size and difficulty than those that appear in their training set?”
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
  - [Generalizing from SIMPLE to HARD Visual Reasoning: Can We Mitigate Modality Imbalance in VLMs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25j/park25j.pdf)
- **Integer addition** (behavioral indicator), 2 papers
  > Standard Transformers trained from scratch on addition and other arithmetic tasks exhibit little to no length generalization (Section 1)
  - [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf)
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
- **Systematic generalization** (construct), 1 paper
  > While we focus on studying length generalization in this work, we expect the intuitions developed here can apply to systematic generalization more broadly. (Section 1)
  - [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf)
- **Long-form text generation** (behavioral indicator), 1 paper
  > While transformer-based models exhibit satisfying performances in tasks of consistent length and distribution, their effectiveness tends to diminish sharply when the input length exceeds the training length, e.g., long document summarization, “needle in a haystack” search, and long text generation. (Section 1)
  - [DAPE: Data-Adaptive Positional Encoding for Length Extrapolation](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f050fa9f0d898e3f265d515f50ae8f9-Paper-Conference.pdf)
- **Inductive bias** (construct), 1 paper
  > The short validation set reveals an architecture’s inductive bias in the absence of any disambiguating information about how it should generalize to longer lengths, as in the experiments of Del´etang et al. (2023). (Section 4)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
- **Reasoning** (construct), 1 paper
  > Length generalization (LG) is a challenging problem in learning to reason. (ABSTRACT)
  - [Generalizing Reasoning Problems to Longer Lengths](https://proceedings.iclr.cc/paper_files/paper/2025/file/abcbdf504b621b4d1213aa7a5c489f8a-Paper-Conference.pdf)
- **Counting** (behavioral indicator), 1 paper
  > We train a Transformer with learned positional embeddings on count sequences of lengths up to 50, with random a and b points in [0, 155]. This trained model then length-generalizes near perfectly when prompted to count sequences of length 100 (see Figure 1b).
  - [What Algorithms can Transformers Learn? A Study in Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/45ed1a72597594c097152ef9cc187762-Paper-Conference.pdf)
