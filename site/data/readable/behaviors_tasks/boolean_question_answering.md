# Boolean question answering
**Type:** Behavioral indicator  
**Supporting papers:** 21  
**Also known as:** Binary question answering, True/False question answering, Yes/no question answering, True/false question answering, Judgment question answering, Polar question answering, Yes-No question answering  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is a question answering behavior that requires a definitive binary response grounded in some provided context, most often "Yes/No" and sometimes "True/False." Definitions largely agree on the response format, whether framed as answering a question, deciding the truth of a declarative statement, or judging whether a statement is correct or wrong; a smaller line of work also uses an equivalent binary choice such as "A" or "B" in sentence-comprehension prompts.

**Variants.** Papers refer to this behavior with several names, including binary, boolean, true/false, yes/no, judgment, and polar question answering. The settings vary from reading comprehension and passage-based QA to professional qualification exams across vertical domains, map questions, sentence-meaning probes after garden path disambiguation, profiling prompts about persona dimensions, and multimodal counter-commonsense scenarios that test whether a model follows visual input or parametric knowledge.

**Space of elicitation and scores.** Only one measurement instrument is explicitly linked to this behavior: StrategyQA, which papers describe as a yes-no or binary QA dataset where answers are yes or no. In those uses, the behavior is elicited by requiring a direct binary reply to the question.

**What it is taken as evidence of.** Papers link this behavior to three constructs, but not through one shared relationship type. One paper relates it to factual reasoning, another relates it to text-image alignment by converting text into a yes/no question format to assess visual-textual alignment, and one paper claims a causal relationship from positional bias to this behavior, reporting that positional bias can hurt performance even for questions answerable with Yes/No.

## Sources

**Binary question answering** (5 papers: [DIDS: Domain Impact-aware Data Sampling for Large Language Model Training](https://aclanthology.org/2025.emnlp-main.215.pdf), [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf), [MAPWise: Evaluating Vision-Language Models for Advanced Map Queries](https://aclanthology.org/2025.naacl-long.473.pdf), [Incremental Sentence Processing Mechanisms in Autoregressive Transformer Language Models](https://aclanthology.org/2025.naacl-long.164.pdf), [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf))
> The observable task of responding to a question with a definitive 'yes' or 'no' answer based on provided context.

**Boolean question answering** (2 papers: [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.260.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf))
> The task of responding to a question with a binary 'True' or 'False' answer based on a provided context.

**True/False question answering** (3 papers: [QualBench: Benchmarking Chinese LLMs with Localized Professional Qualifications for Vertical Domain Evaluation](https://aclanthology.org/2025.emnlp-main.303.pdf), [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf), [AutoCast++: Enhancing World Event Prediction with Zero-shot Ranking-based Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/93f01c8d9b355d7bbe3f353b44ccde66-Paper-Conference.pdf))
> Determining the truth value of declarative statements drawn from professional qualification exams in various vertical domains.

**Yes/no question answering** (2 papers: [SEFE: Superficial and Essential Forgetting Eliminator for Multimodal Continual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25n/chen25n.pdf), [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf))
> Responding to a question with either 'Yes' or 'No' based on whether a provided statement is correct.

**True/false question answering** (1 paper: [Unveiling the Tapestry of Consistency in Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f094ba0f5ce1720466342f78031bdb-Paper-Conference.pdf))
> A specific question answering task where the model must respond with 'yes' or 'no' or an equivalent binary choice.

**Judgment question answering** (1 paper: [CFinBench: A Comprehensive Chinese Financial Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.40.pdf))
> The observable task of determining whether a given statement is correct or wrong.

**Polar question answering** (1 paper: [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf))
> The model's behavior of responding to yes/no questions about whether it would say a given profiling statement, used to assess alignment with a persona dimension.

**Yes-No question answering** (1 paper: [Insight Over Sight: Exploring the Vision-Knowledge Conflicts in Multimodal LLMs](https://aclanthology.org/2025.acl-long.872.pdf))
> Producing binary (Yes/No) responses to questions that directly present counter-commonsense scenarios, testing whether the model adheres to visual input or parametric knowledge.

## Relationships

### Boolean question answering →
- **StrategyQA** (measurement instrument): *measured_by*, 2 papers
  > StrategyQA is a yes-no QA dataset (Section 3.1.1)
  - [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf)
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)

### → Boolean question answering
- **Positional bias** (construct): *causes*, 1 paper
  > We further find that the positional bias can hurt models’ performance even for questions answerable with Yes/No. (Section 1)
  - [Where is the answer? An empirical study of positional bias for parametric knowledge extraction in language model](https://aclanthology.org/2025.naacl-long.58.pdf)

### Associated with
- **Factual reasoning** (construct), 1 paper
  > This perspective leads to interpreting factual reasoning as a binary question answering (QA) task (Burns et al., 2022; Kassner et al., 2021; Mitchell et al., 2022).
  - [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf)
- **Text-image alignment** (construct), 1 paper
  > "we use a function q(.) that converts a given text t into a question format, which enables the model to assess the visual-textual alignment in a consistent manner. Specifically, q(.) generates a yes/no question"
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)
