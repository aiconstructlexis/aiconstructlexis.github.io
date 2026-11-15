# lm-evaluation-harness
**Type:** Measurement instrument  
**Supporting papers:** 232  
**Also known as:** lm-eval, LM-Eval, LM-EVAL, Language Model Evaluation Harness, language model evaluation harness, LM Eval Harness, lm-eval-harness, LM-Eval-Harness, LM Evaluation Harness, LM-evaluation harnesses, LM-Evaluation-Harness, LM-evaluation-harness, LM-EVALUATION-HARNESS, LM Harness, lm-harness, lm-eval framework, LM-Eval framework, Harness, llm-evaluation-harness, LLMs Evaluation Harness, Evaluation Harness, EleutherAI LM Harness, Harness-Eval framework, LLM-evaluation suite, Eleuther Harness, Eleuther AI Language Model Evaluation Harness, EleutherAI LM-Eval-Harness, llm-eval-harness, Eleuther AI eval-harness, Open LLM Leaderboard Harness, EleutherAI Language Model Evaluation Harness, HuggingFace Open LLM harness, EleutherAI evaluation harness, Harness framework, eleuther-AI evaluation harness, lm eval framework, Eleuther LM eval harness, eleuther AI eval harness, LLM Evaluation Harness  

## State of the Field

**What it is.** Across papers, the prevailing description is of an open-source, standardized or unified evaluation framework, library, or suite for running language model benchmarks across many downstream tasks. Definitions repeatedly present it as a way to evaluate language-model, reasoning, question answering, and multiple-choice tasks in reproducible settings, most often in zero-shot form, though some papers also use few-shot, 5-shot, or mixed 0-shot to 5-shot setups. Some papers describe narrower slices within the suite, such as text-only task suites or short-context benchmarks including Wikitext, LAMBADA, PIQA, and HellaSwag, while a smaller line of work describes leaderboard-oriented variants or adapted protocols.

**What it is claimed to measure.** Papers link the harness to 10 constructs and 12 behavioral indicators. The prevailing usage is to measure commonsense reasoning, reasoning, and general ability, and to operationalize zero-shot task performance and downstream task performance. Overall, papers report it as evaluating a broad spread of capabilities rather than a single construct, with zero-shot and downstream benchmark performance appearing most often.

**Space of uses.** In use, papers most often treat it as the standard evaluation infrastructure for fair, clean, and reproducible comparison, often under default, recommended, or matched settings. It is linked to 19 other instruments, most often GSM8K, HellaSwag, MMLU, WinoGrande, and PIQA. Several papers use it as the main runner for zero-shot or few-shot evaluations and accuracy reporting, while some use it to validate another benchmark, adapt it for downstream evaluation, or implement a custom task within the harness.

**Concerns raised.** Only a small explicit concern appears: one paper reports that the default harness setting could truncate some models before they completed their full chain-of-thought reasoning, so it used a fork with the maximum generated tokens raised from 256 to 1000.

## Sources

**LM Eval Harness** (1 paper: [Differential Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/00b67df24009747e8bbed4c2c6f9c825-Paper-Conference.pdf))
> A standardized evaluation suite comprising multiple downstream tasks like ARC, BoolQ, and HellaSwag to assess general language model performance.

**lm-evaluation-harness** (12 papers: [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf), [GaussMark: A Practical Approach for Structural Watermarking of Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/block25a/block25a.pdf), [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf), [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf), [DropBP: Accelerating Fine-Tuning of Large Language Models by Dropping Backward Propagation](https://proceedings.neurips.cc/paper_files/paper/2024/file/240225294cdd2c9b692c2519d3278a08-Paper-Conference.pdf), [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf), [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf), [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf), [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf), [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf))
> An open-source framework used to standardize the evaluation of language models on various benchmarks, ensuring reproducible and comparable results.

**LM Evaluation Harness** (1 paper: [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf))
> A standardized evaluation harness used to run language-model benchmarks and multiple-choice tasks.

**LM-Evaluation-Harness** (1 paper: [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf))
> A unified software framework for evaluating language models on a wide range of tasks in a zero-shot setting.

**Language Model Evaluation Harness** (7 papers: [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf), [Latent Preference Coding: Aligning Large Language Models via Discrete Latent Codes](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25a/gong25a.pdf), [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf), [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf), [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf), [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf), [Self-playing Adversarial Language Game Enhances LLM Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4be7e9867ef163563f4a5e90cec478f-Paper-Conference.pdf))
> A unified framework for running standardized evaluations of generative language models on a large number of diverse tasks.

**LM Harness** (2 papers: [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf), [Putnam-AXIOM: A Functional & Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gulati25a/gulati25a.pdf))
> Eleuther's LM Harness, a standardized evaluation framework used to run the paper's text-only task suite.

**lm-harness** (3 papers: [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf), [FISTAPruner: Layer-wise Post-training Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.1498.pdf), [Router-Tuning: A Simple and Effective Approach for Dynamic Depth](https://aclanthology.org/2025.emnlp-main.99.pdf))
> An evaluation framework (lm-evaluation-harness) that provides a standardized way to benchmark language models on a wide range of tasks.

**lm-eval-harness** (6 papers: [RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf), [Persistent Topological Features in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gardinazzi25a/gardinazzi25a.pdf), [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf), [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf), [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf), [SlimGPT: Layer-wise Structured Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf))
> An evaluation framework for language models used to score performance on various downstream tasks.

**language model evaluation harness** (1 paper: [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf))
> An evaluation suite providing a standardized framework for assessing performance on various downstream tasks.

**LM-evaluation-harness** (1 paper: [Forgetting Transformer: Softmax Attention with a Forget Gate](https://proceedings.iclr.cc/paper_files/paper/2025/file/add3d389197ad2267f660ad060ef61f4-Paper-Conference.pdf))
> A standardized evaluation harness used to run zero-shot short-context language-model benchmarks such as Wikitext, LAMBADA, PIQA, HellaSwag, and others.

**LM-evaluation harnesses** (1 paper: [Adaptive Rank Allocation: Speeding Up Modern Transformers with RaNA Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/bdb0596d13cfccf2db6f0cc5280d2a3f-Paper-Conference.pdf))
> A software suite used to run downstream-task performance evaluations in zero-shot or few-shot settings.

**lm-eval** (1 paper: [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf))
> An evaluation harness (lm-evaluation-harness) used to assess model performance on a wide range of zero-shot tasks, in this case to measure helpfulness.

**LM-Eval** (1 paper: [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf))
> LM-Eval is an evaluation benchmark suite used here for generation tasks assessing commonsense and math reasoning.

**LM-Eval-Harness** (1 paper: [STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf))
> A standardized framework for evaluating language models on a wide range of downstream tasks.

**LM-EVALUATION-HARNESS** (1 paper: [Hymba: A Hybrid-head Architecture for Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f32def07618040e540e0a6182e290562-Paper-Conference.pdf))
> LM Evaluation Harness, a standardized evaluation framework used to run language-model benchmarks across multiple tasks and settings.

**LM-EVAL** (2 papers: [Quamba: A Post-Training Quantization Recipe for Selective State Space Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb4b2fb2434f7cce5cb5ab50271296ee-Paper-Conference.pdf), [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chiang25a/chiang25a.pdf))
> LM-EVAL is an evaluation harness used to run zero-shot language-model benchmarks across multiple common-sense tasks.

**Harness** (2 papers: [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf), [Stacking Your Transformers: A Closer Look at Model Growth for Efficient LLM Pre-Training](https://proceedings.neurips.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf))
> An evaluation framework (also known as lm-evaluation-harness) used to assess the generic performance of LLMs across a diverse set of tasks.

**llm-evaluation-harness** (1 paper: [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf))
> The llm-evaluation-harness repository, used to run standardized evaluations on reasoning benchmarks.

**lm-eval framework** (1 paper: [Improving Reasoning Performance in Large Language Models via Representation Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e73c39cc428c7d264d9820319f31e79-Paper-Conference.pdf))
> An evaluation suite for language models, referenced in the paper for its method of benchmarking performance by investigating output logits over a constrained set of potential responses.

**LLMs Evaluation Harness** (1 paper: [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf))
> An evaluation framework used to assess mathematical reasoning performance, which can use tools like sympy to verify the correctness of generated solutions.

**LM-Eval framework** (1 paper: [HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf))
> A software framework used to conduct zero-shot inference evaluations on language models.

**Evaluation Harness** (1 paper: [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf))
> The Evaluation Harness framework, a standardized benchmark evaluation procedure used to run general capability tests.

**EleutherAI LM Harness** (5 papers: [Mixture Compressor for Mixture-of-Experts LLMs Gains More](https://proceedings.iclr.cc/paper_files/paper/2025/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf), [DLP: Dynamic Layerwise Pruning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25l/chen25l.pdf), [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf), [On Pruning State-Space LLMs](https://aclanthology.org/2025.emnlp-main.950.pdf), [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf))
> An evaluation framework used to test language models on a wide range of benchmarks in a standardized way.

**Harness-Eval framework** (1 paper: [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf))
> An evaluation framework used to standardize the assessment of language models, which was used to validate the results on the INCLUDE benchmark.

**LLM-evaluation suite** (1 paper: [Towards Scalable Exact Machine Unlearning Using Parameter-Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/d33b741600f100b31256c70a46f66ec9-Paper-Conference.pdf))
> LLM Evaluation Suite, a standardized evaluation suite used to report zero-shot performance on multiple language-model benchmarks.

**EleutherAI Language Model Evaluation Harness** (2 papers: [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf), [On the Analysis and Distillation of Emergent Outlier Properties in Pre-trained Language Models](https://aclanthology.org/2025.naacl-long.430.pdf))
> A standardized evaluation suite that assesses language models across a variety of zero-shot benchmarks covering reasoning, knowledge, and comprehension tasks.

**Eleuther Harness** (1 paper: [any4: Learned 4-bit Numeric Representation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/elhoushi25a/elhoushi25a.pdf))
> The EleutherAI Language Model Evaluation Harness, a framework for standardized evaluation of language models on a wide range of natural language tasks.

**Eleuther AI Language Model Evaluation Harness** (1 paper: [MoH: Multi-Head Attention as Mixture-of-Head Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25l/jin25l.pdf))
> A unified software framework, also known as lm-evaluation-harness, for standardized evaluation of generative language models across a wide range of benchmarks.

**EleutherAI LM-Eval-Harness** (1 paper: [PROXSPARSE: REGULARIZED LEARNING OF SEMI-STRUCTURED SPARSITY MASKS FOR PRETRAINED LLMS](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bi/liu25bi.pdf))
> EleutherAI LM-Eval-Harness is an evaluation harness used to run standardized zero-shot language reasoning tasks on LLMs.

**llm-eval-harness** (1 paper: [DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf))
> A framework for few-shot language model evaluation used to assess the performance of compressed models on zero-shot tasks.

**Eleuther AI eval-harness** (1 paper: [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf))
> A standardized framework and software library for evaluating language models on a wide range of benchmarks.

**LLM Evaluation Harness** (1 paper: [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf))
> A standardized framework for few-shot evaluation of language models across a diverse set of benchmarks.

**Open LLM Leaderboard Harness** (1 paper: [Beyond Similarity: A Gradient-based Graph Method for Instruction Tuning Data Selection](https://aclanthology.org/2025.acl-long.1189.pdf))
> A standardized framework and software tool used to provide a consistent methodology for evaluating the performance of large language models.

**HuggingFace Open LLM harness** (1 paper: [Re3Syn: A Dependency-Based Data Synthesis Framework for Long-Context Post-training](https://aclanthology.org/2025.acl-long.1518.pdf))
> Standard evaluation suite for assessing foundational language understanding and reasoning abilities of LLMs using a collection of short-text benchmarks such as MMLU, Winogrande, and Hellaswag.

**EleutherAI evaluation harness** (1 paper: [SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bbf38332580c1bed99fa99bc9ee53229-Paper-Conference.pdf))
> A software framework for standardized evaluation of large language models across a wide range of benchmarks.

**Harness framework** (1 paper: [Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements](https://aclanthology.org/2025.emnlp-main.1362.pdf))
> The lm-eval-harness evaluation framework used to run benchmark evaluations under default settings.

**eleuther-AI evaluation harness** (1 paper: [M-Wanda: Improving One-Shot Pruning for Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.1369.pdf))
> Standardized framework for zero-shot evaluation of LLMs across a wide range of benchmarks, used here to ensure consistent scoring across multilingual tasks.

**lm eval framework** (1 paper: [QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models](https://aclanthology.org/2025.emnlp-main.271.pdf))
> The lm-eval framework, a standardized evaluation suite used to run benchmark tasks such as PIQA, ARC, HellaSwag, and WinoGrande.

**Eleuther LM eval harness** (1 paper: [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf))
> The Eleuther LM Eval Harness, a standardized evaluation framework used to run benchmark tasks in the same setting for models not on the leaderboard.

## Relationships

### → lm-evaluation-harness
- **Commonsense reasoning** (construct): *measured_by*, 10 papers
  > For commonsense reasoning we follow the LM Evaluation Harness [16] implementations of these tasks, evaluating on the test sets of ARC and OpenBookQA and the validation sets of HellaSwag, WinoGrande, BoolQ and PIQA, which brings our evaluations in line with other models. (Section 5.1)
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
  - [DropBP: Accelerating Fine-Tuning of Large Language Models by Dropping Backward Propagation](https://proceedings.neurips.cc/paper_files/paper/2024/file/240225294cdd2c9b692c2519d3278a08-Paper-Conference.pdf)
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
  - [HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf)
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
  - [Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf)
- **Zero-shot task performance** (behavioral indicator): *measured_by*, 8 papers
  > For zero-shot evaluation, we use seven tasks from EleutherAI LM Harness (Gao et al., 2021).
  - [A Simple and Effective Pruning Approach for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/14c856c7a41297804de4c4890e846b25-Paper-Conference.pdf)
  - [SliceGPT: Compress Large Language Models by Deleting Rows and Columns](https://proceedings.iclr.cc/paper_files/paper/2024/file/316648eb8b4ffb6010f531b07848c300-Paper-Conference.pdf)
  - [Dynamic Low-Rank Sparse Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/675dc71676eb3bec5326824365a9bac2-Paper-Conference.pdf)
  - [OSTQuant: Refining Large Language Model Quantization with Orthogonal and Scaling Transformations for Better Distribution Fitting](https://proceedings.iclr.cc/paper_files/paper/2025/file/5cebc89b113920dbff7c79854ba765a3-Paper-Conference.pdf)
  - [Bypass Back-propagation: Optimization-based Structural Pruning for Large Language Models via Policy Gradient](https://aclanthology.org/2025.acl-long.1421.pdf)
  - [EvoPress: Accurate Dynamic Model Compression via Evolutionary Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sieberling25a/sieberling25a.pdf)
  - [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chiang25a/chiang25a.pdf)
  - [GANQ: GPU-Adaptive Non-Uniform Quantization for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25ae/zhao25ae.pdf)
- **Reasoning** (construct): *measured_by*, 5 papers
  > For our performance evaluation, we use the few-shot tasks from Language Model Evaluation Harness (Gao et al., 2021). We select these tasks such that they can measure various abilities of the models (e.g., reading comprehension, reasoning, etc.) (Sec. 3.1)
  - [ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6cf669c222ad13f60d503736fb2bd15b-Paper-Conference.pdf)
  - [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 4 papers
  > the LLM’s generic performance A as the evaluation across different tasks using the Harness framework. (Section 2.1)
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
  - [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf)
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 3 papers
  > For our performance evaluation, we use the few-shot tasks from Language Model Evaluation Harness (Gao et al., 2021). We select these tasks such that they can measure various abilities of the models (e.g., reading comprehension, reasoning, etc.) (Sec. 3.1)
  - [ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6cf669c222ad13f60d503736fb2bd15b-Paper-Conference.pdf)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
  - [Neural ODE Transformers: Analyzing Internal Dynamics and Adaptive Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/82e3509393670d9d478c359b4ce6f950-Paper-Conference.pdf)
- **Downstream task performance** (behavioral indicator): *measured_by*, 3 papers
  > ...and on an aggregate of six downstream tasks using the EleutherAI LM Harness (Gao et al., 2023)... (Section 5)
  - [Training-Free Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf)
  - [Domain2Vec: Vectorizing Datasets to Find the Optimal Data Mixture without Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bu/zhang25bu.pdf)
  - [The Sharpness Disparity Principle in Transformers for Accelerating Language Model Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dl/wang25dl.pdf)
- **Zero-shot question answering** (behavioral indicator): *measured_by*, 2 papers
  > To verify the effectiveness and generalizability, we perform extensive evaluation of our models on 7 zero-shot tasks. We employ a set of seven tasks sourced from the EleutherAI LM Harness [50]. (Section 7.1).
  - [Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 2 papers
  > We evaluate the pretrained models on language model tasks and multiple-choice tasks from LM evaluation Harness (Gao et al., 2023). (Section 5.3)
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
  - [MILU: A Multi-task Indic Language Understanding Benchmark](https://aclanthology.org/2025.naacl-long.507.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > Our method is benchmarked across a diverse range of question answering and generation datasets [24, 25, 26, 27, 28, 29, 30, 31] using the lm-eval-harness [32]. (Section 2)
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
  - [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf)
- **In-context learning** (construct): *measured_by*, 2 papers
  > We evaluate APE on three ICL tasks using the LM Evaluation Harness (Gao et al., 2024):: GSM8K (8-shot) (Cobbe et al., 2021a), TriviaQA (5-shot) (Joshi et al., 2017), and MMLU (5-shot) (Hendrycks et al., 2020a). (Section 5.2).
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
  - [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)
- **Natural language understanding** (construct): *measured_by*, 2 papers
  > The results show no significant losses of general ability like natural language understanding after aligning with the embodied environment... Table 2: Zero-shot performance on Language Model Evaluation Harness [56]
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **Language understanding task performance** (behavioral indicator): *measured_by*, 1 paper
  > Then we utilize popular language benchmarks provided in the open-sourced lm-evaluation-harness project [18] for evaluation
  - [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > The evaluation scripts are based on lm-eval for commonsense and mathematical reasoning (Section 4.1).
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 1 paper
  > ...two generation datasets... with the LM-Evaluation-Harness framework (Gao et al., 2023).
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **Zero-shot generalization** (construct): *measured_by*, 1 paper
  > “Zero-shot performance was evaluated using the LM Evaluation Harness (Gao et al., 2021)”
  - [MoDeGPT: Modular Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb7214d2fdfd84165b08539d59c92e07-Paper-Conference.pdf)
- **Knowledge understanding** (construct): *measured_by*, 1 paper
  > We evaluate our models on a total of 9 different zero-shot benchmarks to assess their abilities across various natural language tasks like common sense reasoning, general language understanding and knowledge understanding using the LLM Evaluation Harness [14]. (Section 4.3)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **Helpfulness** (construct): *measured_by*, 1 paper
  > we evaluate the impact of safety heads ablation on helpfulness. We use lm-eval (Gao et al., 2024) to assess model performance after ablating safety heads of Llama-2-7b-chat on zero-shot tasks... (Section 5.3)
  - [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf)
- **Few-shot task performance** (behavioral indicator): *measured_by*, 1 paper
  > We used the Language Model Evaluation Harness framework (Gao et al., 2023) to evaluate accuracy on seven few-shot tasks, and averaged them for performance comparison. (Section 3.1)
  - [Relaxed Recursive Transformers: Effective Parameter Sharing with Layer-wise LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d6a55225cebbdc16fbb0e45c5bdf2b-Paper-Conference.pdf)
- **Classification** (behavioral indicator): *measured_by*, 1 paper
  > ...six classification datasets... with the LM-Evaluation-Harness framework (Gao et al., 2023).
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **Language modeling ability** (construct): *measured_by*, 1 paper
  > To further assess preservation of language modeling capability, we also evaluated on downstream tasks: ... ALMs using the LM Evaluation Harness (Gao et al., 2024) across 5 benchmarks... (Section 3.3).
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
- **Text classification** (behavioral indicator): *measured_by*, 1 paper
  > All the tasks except for MT are classification tasks, where we use the lm-evaluation-harness (Gao et al., 2024) evaluation tool and report accuracy. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)

### Associated with
- **MMLU** (measurement instrument), 4 papers
  > Table 2: Zero-shot performance on Language Model Evaluation Harness [56]... MMLU
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
  - [Training-Free Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
  - [Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1263.pdf)
- **HellaSwag** (measurement instrument), 4 papers
  > Table 2: Zero-shot performance on Language Model Evaluation Harness [56]... HellaSwag
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
  - [Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1263.pdf)
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
- **WinoGrande** (measurement instrument), 4 papers
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
  - [Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1263.pdf)
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
- **GSM8K** (measurement instrument), 4 papers
  > ...using the EleutherAI LM Harness (Gao et al., 2023), including ... 5-shot GSM8K... (Section 5)
  - [Training-Free Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf)
  - [HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf)
  - [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf)
  - [Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning](https://aclanthology.org/2025.naacl-long.519.pdf)
- **PIQA** (measurement instrument), 3 papers
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
  - [Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1263.pdf)
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
- **ARC-Challenge** (measurement instrument), 2 papers
  > Table 2: Zero-shot performance on Language Model Evaluation Harness [56]... ARC_C
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **SciQ** (measurement instrument), 2 papers
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
- **LAMBADA** (measurement instrument), 2 papers
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
  - [Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1263.pdf)
- **BoolQ** (measurement instrument), 2 papers
  > We use lm-evaluation-harness to report results on ... BoolQ
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
  - [Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1263.pdf)
- **BIG-Bench Hard** (measurement instrument), 2 papers
  > We use lm-evaluation-harness to report results on ... BigBench-Hard
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
  - [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf)
- **Open LLM Leaderboard** (measurement instrument), 1 paper
  > For the Open LLM Leaderboard, we adhere to the recommended Language Model Evaluation Harness (Gao et al., 2021) protocols. (Section 4.1)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **ARC-Easy** (measurement instrument), 1 paper
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
- **LogiQA 2.0** (measurement instrument), 1 paper
  > zero-shot downstream performance on 6 common-sense reasoning domains from the language model evaluation harness (Gao et al., 2024): HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2019), PIQA (Bisk et al., 2019), ARC-E (Clark et al., 2018), SciQ (Welbl et al., 2017), LogiQA2 (Liu et al., 2023) and LAMBADA (Paperno et al., 2016). (Section 4)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
- **WikiText-2** (measurement instrument), 1 paper
  > We use lm-evaluation-harness to report results on Wikitext2
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **ARC** (measurement instrument), 1 paper
  > “We use EleutherAI’s LM eval harness (Gao et al., 2024) to evaluate models on ARC (Clark et al., 2018), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), SciQ (Welbl et al., 2017) and Winogrande (Trinh & Le, 2018).”
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
- **CommonsenseQA** (measurement instrument), 1 paper
  > We use lm-evaluation-harness to report results on ... CommonSenseQA
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **CoQA** (measurement instrument), 1 paper
  > We use the LM-Eval framework to conduct zero-shot inference on GSM8K and COQA.
  - [HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument), 1 paper
  > Evaluation is performed on ARC (Clark et al., 2018), BoolQ (BQ) (Clark et al., 2019), OpenbookQA (OBQA) (Mihaylov et al., 2018), PIQA (Bisk et al., 2020a), WinoGrande (WG) (Sakaguchi et al., 2021), LAMBADA (LMBD) (Paperno et al., 2016b), 5-shot MMLU (Hendrycks et al., 2020), and 10-shot HellaSwag (HS) (Zellers et al., 2019a). These evaluations were conducted using the LM-Evaluation-Harness repository (Gao et al., 2024).
  - [Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1263.pdf)
- **Chain of thought** (behavioral indicator), 1 paper
  > We use a fork of EleutherAI's LM Evaluation Harness with minor modiﬁcations. We use the default settings for evaluation, except for increasing the maximum number of allowed generated tokens from 256 to 1000, as we notice that the default setting did not allow some models to complete their full chain-of-thought reasoning before being truncated.
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MATH** (measurement instrument), 1 paper
  > “We perform evaluations using lm-evaluation-harness ... For both GSM8k and MATH, we use 5-shot examples”
  - [Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning](https://aclanthology.org/2025.naacl-long.519.pdf)
