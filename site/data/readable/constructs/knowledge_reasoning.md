# Knowledge reasoning
**Type:** Construct  
**Supporting papers:** 12  
**Also known as:** Knowledge and reasoning, World knowledge reasoning, Fact reasoning, Knowledge-intensive reasoning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats knowledge reasoning as a latent question answering ability that combines factual or world knowledge with inference. Most definitions say it involves answering questions that require factual knowledge plus reasoning over concepts, though they differ on where the knowledge comes from: some describe stored world knowledge or knowledge held in the model’s parameters, while others emphasize external facts, open-book information, or knowledge retrieved from a corpus. A narrower framing treats it as linking textual mentions to external facts in order to infer implicit geographic, cultural, or encyclopedic information needed for relevance.

**Space of facets.** Papers do not use a single label for this construct. Alongside knowledge reasoning, they use nearby names such as knowledge and reasoning, fact reasoning, world knowledge reasoning, and knowledge-intensive reasoning, with the shared core being factual knowledge plus inference. Some usages narrow the scope to world knowledge relations and implicit fact retrieval, while others cast it as open-domain generation or as a broad evaluation category, and papers also separate it from categories such as commonsense reasoning, mathematical reasoning, truthfulness, and conversational ability.

**Space of measurement.** Operationalization is benchmark-based: papers link knowledge reasoning to 10 measurement instruments and 1 behavioral indicator, but the reported measurements themselves are through datasets and benchmarks rather than the behavioral indicator. MMLU is the most frequent instrument, and papers also use ARC, CodeMixBench, CommonsenseQA, and IMPLIRET, plus 5 other instruments. Across these measures, the construct is tested through general knowledge and science question answering, code-mixed evaluation, implicit fact retrieval, open-book question answering, and tasks that ask models to integrate outside knowledge, so the measurements cover both broad factual question answering and narrower formulations centered on external or stored knowledge.

**Links.** Beyond measurement, papers report few non-measurement links. One paper claims a causal relationship from Question decomposition to Knowledge reasoning, describing decomposition of complex questions in knowledge-intensive reasoning tasks for more accurate answer inference. Another paper reports that Knowledge manipulation is related to Knowledge reasoning, with reasoning described alongside knowledge recall and transfer, and no correlational links are reported.

## Sources

**Knowledge reasoning** (2 papers: [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf), [CodeMixBench: Evaluating Code-Mixing Capabilities of LLMs Across 18 Languages](https://aclanthology.org/2025.emnlp-main.109.pdf))
> The latent ability to answer questions by using external or factual knowledge and integrating it into inference.

**Knowledge and reasoning** (1 paper: [Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index](https://aclanthology.org/2025.emnlp-main.1268.pdf))
> The ability to answer questions that require factual knowledge and reasoning over concepts.

**World knowledge reasoning** (1 paper: [ImpliRet: Benchmarking the Implicit Fact Retrieval Challenge](https://aclanthology.org/2025.emnlp-main.1685.pdf))
> The ability to connect textual mentions to external factual knowledge (e.g., that Big Ben is in the UK) to infer implicit geographic, cultural, or encyclopedic facts necessary for determining relevance.

**Fact reasoning** (1 paper: [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf))
> The latent ability to reason based on factual knowledge and open-book information.

**Knowledge-intensive reasoning** (2 papers: [CER: Confidence Enhanced Reasoning in LLMs](https://aclanthology.org/2025.acl-long.390.pdf), [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf))
> The latent ability to answer questions by retrieving and synthesizing information from a broad base of knowledge stored within the model's parameters.

## Relationships

### Knowledge reasoning →
- **MMLU** (measurement instrument): *measured_by*, 4 papers
  > “one knowledge-intensive reasoning benchmark: the mass-multitask language understanding (MMLU) dataset (Hendrycks et al., 2020).”
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf)
  - [Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ax/huang25ax.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 1 paper
  > We employ the ScienceQA [28] dataset for the knowledge reasoning task (Section 5.1.1).
  - [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 1 paper
  > For knowledge reasoning, we utilize Winogrande (Sakaguchi et al., 2019) (abbreviated as Wino) and CommonsenseQA (Talmor et al., 2019) (abbreviated as Comm). (Section 4)
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 1 paper
  > For knowledge reasoning, we utilize Winogrande (Sakaguchi et al., 2019) (abbreviated as Wino) and CommonsenseQA (Talmor et al., 2019) (abbreviated as Comm). (Section 4)
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > OpenBookQA (Mihaylov et al., 2018) for fact reasoning (Section 3.1)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **ARC** (measurement instrument): *measured_by*, 1 paper
  > ARC (Clark et al., 2018), a knowledge reasoning dataset consisting of grad-school level science questions in a multiple-choice format. (Section 4.1).
  - [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > TriviaQA (Joshi et al., 2017): A large-scale dataset containing knowledge-intensive questions sourced from Wikipedia.
  - [CER: Confidence Enhanced Reasoning in LLMs](https://aclanthology.org/2025.acl-long.390.pdf)
- **CodeMixBench** (measurement instrument): *measured_by*, 1 paper
  > we introduce the CodeMixBench, a code-mixing evaluation benchmark including eight tasks–three for evaluating LLMs (knowledge reasoning, mathematical reasoning, and truthfulness) and five for traditional NLP tasks (LID, POS, NER, SA, and MT). (§1)
  - [CodeMixBench: Evaluating Code-Mixing Capabilities of LLMs Across 18 Languages](https://aclanthology.org/2025.emnlp-main.109.pdf)
- **IMPLIRET** (measurement instrument): *measured_by*, 1 paper
  > "IMPLIRET covers three reasoning categories: World Knowledge, Arithmetic, and Temporal."
  - [ImpliRet: Benchmarking the Implicit Fact Retrieval Challenge](https://aclanthology.org/2025.emnlp-main.1685.pdf)
- **OK-VQA** (measurement instrument): *measured_by*, 1 paper
  > OKVQA (Marino et al., 2019), Visual Common Sense Reasoning (VCR) (Zellers et al., 2019) and A-OKVQA (Schwenk et al., 2022) evaluate whether models are able to integrate outside knowledge in order to answer questions, covering a broad base of common-sense and world knowledge. (Section 2.1)
  - [Century: A Framework and Dataset for Evaluating Historical Contextualisation of Sensitive Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/efc549c2d22edf2f244b7013387c6251-Paper-Conference.pdf)

### → Knowledge reasoning
- **Question decomposition** (behavioral indicator): *causes*, 1 paper
  > since questions in knowledge-intensive reasoning tasks can often be a complex composite problems that are challenging to solve directly, a structured knowledge utilizer is used to perform question decomposition... for more accurate answer inference.
  - [StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf)

### Associated with
- **Knowledge manipulation** (construct), 1 paper
  > enhance the knowledge manipulation (e.g., knowledge recall, reasoning, and transfer) ability of LLMs. (Section 1)
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)
