# Natural language inference
**Type:** Behavioral indicator  
**Supporting papers:** 141  
**Also known as:** Semantic inference, Textual entailment prediction, Hypothesis verification, Cross-lingual sentence classification, Textual entailment, NLI, Sentence entailment, Textual entailment task, Entailment prediction, Textual entailment recognition  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is a premise-hypothesis task in which a model judges whether the hypothesis is entailed, contradicted, or neutral/undetermined given the premise. Many definitions paraphrase this as deciding whether the hypothesis is true, false, or possibly true, and one paper even reformats it generatively as "Does \"{SENT1}\" entail \"{SENT2}\"? {Yes/Maybe/No}" (Adapting Large Language Models via Reading Comprehension). A smaller line of work narrows the output to binary entailment judgments, such as entailment versus not entailment or True versus False, and a few formulations broaden the input from a single premise to multi-sentence premises or to facts and rules.

**Variants.** Most variants keep the same inference setup but shift the name, domain, or setting. Papers also call it textual entailment, sentence entailment, textual entailment recognition, entailment prediction, semantic inference, or hypothesis verification, and they study multilingual or cross-lingual classification, biomedical entailment, event reasoning, commonsense NLI based on the most logical continuation of an event, and cases with multi-sentence premises. A smaller variant defines it over facts and rules with labels True, False, or Unknown.

**Space of elicitation and scores.** Papers link this behavior to 17 measurement instruments. The most frequently linked are MNLI, RTE, XNLI, QNLI, and GLUE, and these are used as benchmark datasets or suites for sentence-pair inference, with XNLI described as multilingual and GLUE as a broader benchmark that includes NLI datasets. Other papers use additional NLI benchmarks and related evaluation sets.

**What it is taken as evidence of.** Rather than centering on one construct, the recorded construct links spread across 6 constructs. The most frequently linked are Consistency, General ability, Knowledge, Logical reasoning, and Natural language understanding, and these links are framed as related rather than as direct measurement claims; one paper says NLI serves "as a proxy for the consistency condition" (A Novel Computational Modeling Foundation for Automatic Coherence Assessment), while another says model ability on NLI has been used to evaluate natural language understanding. Beyond construct links, one paper claims a causal relationship from natural language inference to relation extraction, and other papers relate it to grounded response generation and textual reasoning.

## Sources

**Natural language inference** (53 papers: [Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf), [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf), [Are Bert Family Good Instruction Followers? A Study on Their Potential And Limitations](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a13eb0c08247364066e8d86551c3090-Paper-Conference.pdf), [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf), [Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e9034dd5420660d86c8c360c35a895e-Paper-Conference.pdf), [DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/e352b765e625934ce86919995e2371aa-Paper-Conference.pdf), [Debiasing Attention Mechanism in Transformer without Demographics](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f5337a39b1f6d670aad9d32debc0e5d-Paper-Conference.pdf), [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf), [Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce806d8b4bf38cd92d483e5a0490d983-Paper-Conference.pdf), [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf), [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf), [Rethinking Invariance in In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/01e8ecf628f8d9f62a1fd433d44d34ab-Paper-Conference.pdf), [FilBench: Can LLMs Understand and Generate Filipino?](https://aclanthology.org/2025.emnlp-main.127.pdf), [Assessment and manipulation of latent constructs in pre-trained language models using psychometric scales](https://aclanthology.org/2025.acl-long.121.pdf), [CC-Tuning: A Cross-Lingual Connection Mechanism for Improving Joint Multilingual Supervised Fine-Tuning](https://aclanthology.org/2025.acl-long.933.pdf), [Curriculum Debiasing: Toward Robust Parameter-Efficient Fine-Tuning Against Dataset Biases](https://aclanthology.org/2025.acl-long.469.pdf), [D.Va: Validate Your Demonstration First Before You Use It](https://aclanthology.org/2025.acl-long.129.pdf), [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf), [LLäMmlein: Transparent, Compact and Competitive German-Only Language Models from Scratch](https://aclanthology.org/2025.acl-long.111.pdf), [Language Fusion for Parameter-Efficient Cross-lingual Transfer](https://aclanthology.org/2025.acl-long.1255.pdf), [Less Mature is More Adaptable for Sentence-level Language Modeling](https://aclanthology.org/2025.acl-long.573.pdf), [Mitigating Shortcut Learning with InterpoLated Learning](https://aclanthology.org/2025.acl-long.450.pdf), [Neuron Empirical Gradient: Discovering and Quantifying Neurons' Global Linear Controllability](https://aclanthology.org/2025.acl-long.1041.pdf), [PIPER: Benchmarking and Prompting Event Reasoning Boundary of LLMs via Debiasing-Distillation Enhanced Tuning](https://aclanthology.org/2025.acl-long.1389.pdf), [Plug-in and Fine-tuning: Bridging the Gap between Small Language Models and Large Language Models](https://aclanthology.org/2025.acl-long.271.pdf), [Pragmatics in the Era of Large Language Models: A Survey on Datasets, Evaluation, Opportunities and Challenges](https://aclanthology.org/2025.acl-long.425.pdf), [STUN: Structured-Then-Unstructured Pruning for Scalable MoE Pruning](https://aclanthology.org/2025.acl-long.671.pdf), [Your Model is Overconfident, and Other Lies We Tell Ourselves](https://aclanthology.org/2025.acl-long.269.pdf), [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf), [ExLM: Rethinking the Impact of $\texttt[MASK]$ Tokens in Masked Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zheng25q/zheng25q.pdf), [Focus On This, Not That! Steering LLMs with Adaptive Feature Specification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lamb25a/lamb25a.pdf), [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf), [Occult: Optimizing Collaborative Communications across Experts for Accelerated Parallel MoE Training and Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25f/luo25f.pdf), [Resolving Lexical Bias in Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rizwan25a/rizwan25a.pdf), [A Novel Computational Modeling Foundation for Automatic Coherence Assessment](https://aclanthology.org/2025.naacl-long.277.pdf), [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf), [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.122.pdf), [Enhancing Language Model Hypernetworks with Restart: A Study on Optimization](https://aclanthology.org/2025.naacl-long.397.pdf), [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf), [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [Lost in Inference: Rediscovering the Role of Natural Language Inference for Large Language Models](https://aclanthology.org/2025.naacl-long.466.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [NLI under the Microscope: What Atomic Hypothesis Decomposition Reveals](https://aclanthology.org/2025.naacl-long.130.pdf), [Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque](https://aclanthology.org/2025.naacl-long.629.pdf), [SALAD: Improving Robustness and Generalization through Contrastive Learning with Structure-Aware and LLM-Driven Augmented Data](https://aclanthology.org/2025.naacl-long.634.pdf), [SMAB: MAB based word Sensitivity Estimation Framework and its Applications in Adversarial Text Generation](https://aclanthology.org/2025.naacl-long.463.pdf), [Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.407.pdf), [Soft Language Prompts for Language Transfer](https://aclanthology.org/2025.naacl-long.517.pdf))
> The task of determining whether a 'hypothesis' sentence is true (entailment), false (contradiction), or undetermined (neutral) given a 'premise' sentence.

**Textual entailment** (7 papers: [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf), [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf), [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf), [SylloBio-NLI: Evaluating Large Language Models on Biomedical Syllogistic Reasoning](https://aclanthology.org/2025.naacl-long.371.pdf), [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf), [BelarusianGLUE: Towards a Natural Language Understanding Benchmark for Belarusian](https://aclanthology.org/2025.acl-long.25.pdf), [Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f5c76187c28e8d9d3b938d0c504436c-Paper-Conference.pdf))
> Deciding whether a hypothesis is supported by a premise in a sentence-pair classification format.

**Semantic inference** (1 paper: [DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.694.pdf))
> The task of determining the logical relationship between two sentences, such as entailment or contradiction.

**Textual entailment prediction** (1 paper: [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf))
> The task of determining whether a 'hypothesis' sentence can be logically inferred from a 'premise' sentence.

**Hypothesis verification** (1 paper: [LogicTree: Structured Proof Exploration for Coherent and Rigorous Logical Reasoning with Large Language Models](https://aclanthology.org/2025.emnlp-main.1054.pdf))
> Determining whether a hypothesis is true, false, or unknown from a set of facts and rules.

**Cross-lingual sentence classification** (1 paper: [MrT5: Dynamic Token Merging for Efficient Byte-level Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e9dd32cb9f9bff397f1a7ebd07010f2-Paper-Conference.pdf))
> Assigning a natural language inference label to sentences across multiple languages.

**NLI** (1 paper: [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf))
> A natural language inference evaluation used to assess whether the model can infer logical relations between sentence pairs.

**Sentence entailment** (1 paper: [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf))
> The task of determining whether a 'hypothesis' sentence is true, false, or neutral given a 'premise' sentence.

**Textual entailment task** (1 paper: [SylloBio-NLI: Evaluating Large Language Models on Biomedical Syllogistic Reasoning](https://aclanthology.org/2025.naacl-long.371.pdf))
> A binary classification task where models determine whether a conclusion logically follows from a set of premises, focusing on logical validity in a biomedical context.

**Entailment prediction** (1 paper: [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf))
> Determining whether a hypothesis logically follows from a given premise in a natural language inference setup.

**Textual entailment recognition** (1 paper: [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf))
> Assessing whether one sentence logically follows from another, classifying the relationship as entailment, contradiction, or neutrality.

## Relationships

### Natural language inference →
- **MNLI** (measurement instrument): *measured_by*, 15 papers
  > “Natural Language Inference (MNLI”
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
  - [Debiasing Attention Mechanism in Transformer without Demographics](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f5337a39b1f6d670aad9d32debc0e5d-Paper-Conference.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [Beyond correlation: The impact of human uncertainty in measuring the effectiveness of automatic evaluation and LLM-as-a-judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/8798321486948322be2b4d658744ba72-Paper-Conference.pdf)
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
  - [Auto-GDA: Automatic Domain Adaptation for Efficient Grounding Verification in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eb6233e02f7d9efbb84acd839a996fb-Paper-Conference.pdf)
  - [A Novel Computational Modeling Foundation for Automatic Coherence Assessment](https://aclanthology.org/2025.naacl-long.277.pdf)
  - [Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.407.pdf)
  - [Mitigating Shortcut Learning with InterpoLated Learning](https://aclanthology.org/2025.acl-long.450.pdf)
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
  - [Bit-Flip Error Resilience in LLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.528.pdf)
  - [Topic Coverage-based Demonstration Retrieval for In-Context Learning](https://aclanthology.org/2025.emnlp-main.1007.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
- **RTE** (measurement instrument): *measured_by*, 11 papers
  > “Natural Language Inference (MNLI, RTE, QNLI)”
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
  - [Can Generative AI Solve Your In-Context Learning Problem? A Martingale Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/d90268f01ef06a55630b0588227adf4f-Paper-Conference.pdf)
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
  - [Forward Knows Efficient Backward Path: Saliency-Guided Memory-Efficient Fine-tuning of Large Language Models](https://aclanthology.org/2025.acl-long.459.pdf)
  - [Resolving Lexical Bias in Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rizwan25a/rizwan25a.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
  - [Can an Individual Manipulate the Collective Decisions of Multi-Agents?](https://aclanthology.org/2025.emnlp-main.611.pdf)
- **XNLI** (measurement instrument): *measured_by*, 10 papers
  > a language understanding dataset XNLI [Conneau et al., 2018] in natural language inference (NLI) task were used. (Section 4.2)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
  - [AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging](https://aclanthology.org/2025.naacl-long.493.pdf)
  - [CC-Tuning: A Cross-Lingual Connection Mechanism for Improving Joint Multilingual Supervised Fine-Tuning](https://aclanthology.org/2025.acl-long.933.pdf)
  - [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.939.pdf)
  - [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf)
  - [Exploring morphology-aware tokenization: A case study on Spanish language modeling](https://aclanthology.org/2025.emnlp-main.1552.pdf)
  - [Discriminating Form and Meaning in Multilingual Models with Minimal-Pair ABX Tasks](https://aclanthology.org/2025.emnlp-main.1210.pdf)
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf)
- **QNLI** (measurement instrument): *measured_by*, 7 papers
  > “Natural Language Inference (MNLI, RTE, QNLI)”
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
  - [Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b79416c0dc4b09feaa169ed5cdd63d4-Paper-Conference.pdf)
  - [Topic Coverage-based Demonstration Retrieval for In-Context Learning](https://aclanthology.org/2025.emnlp-main.1007.pdf)
  - [TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation](https://aclanthology.org/2025.emnlp-main.1157.pdf)
- **GLUE** (measurement instrument): *measured_by*, 4 papers
  > on the General Language Understanding Evaluation (GLUE) Wang et al. (2018) benchmark, which includes two single-sentence classification, three similarity and paraphrase and four natural language inference datasets.
  - [Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf)
  - [Enhancing Language Model Hypernetworks with Restart: A Study on Optimization](https://aclanthology.org/2025.naacl-long.397.pdf)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf)
- **SNLI** (measurement instrument): *measured_by*, 2 papers
  > SNLI (Bowman et al., 2015) is an NLI inference task dataset with 10K samples and 3 labels – entailment, neutral and contradiction. (Section 3)
  - [Beyond correlation: The impact of human uncertainty in measuring the effectiveness of automatic evaluation and LLM-as-a-judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/8798321486948322be2b4d658744ba72-Paper-Conference.pdf)
  - [NLI under the Microscope: What Atomic Hypothesis Decomposition Reveals](https://aclanthology.org/2025.naacl-long.130.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 2 papers
  > (e) natural language inference (HellaSwag (Zellers et al., 2019)) (Section 4.2)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf)
- **CB** (measurement instrument): *measured_by*, 2 papers
  > Natural language inference: CB (De Marneff et al., 2019) and WiC (Pilehvar & Camacho-Collados, 2018) from superGLUE (Wang et al., 2019) (Section 5.1).
  - [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
- **ANLI** (measurement instrument): *measured_by*, 2 papers
  > MNLI (Multi-Genre Natural Language Inference) and ANLI (Adversarial Natural Language Inference) benchmark a models understanding of entailment, contradiction, and neutrality across genres and adversarially selected examples.
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
  - [QCRD: Quality-guided Contrastive Rationale Distillation for Large Language Models](https://aclanthology.org/2025.emnlp-main.724.pdf)
- **e-SNLI** (measurement instrument): *measured_by*, 2 papers
  > The task of e-SNLI is to determine the logical relationship (contradiction, neutral or entailment) between the premise and hypothesis. (Section 4.1)
  - [Self-Critique and Refinement for Faithful Natural Language Explanations](https://aclanthology.org/2025.emnlp-main.427.pdf)
  - [QCRD: Quality-guided Contrastive Rationale Distillation for Large Language Models](https://aclanthology.org/2025.emnlp-main.724.pdf)
- **WiC** (measurement instrument): *measured_by*, 1 paper
  > Natural language inference: CB (De Marneff et al., 2019) and WiC (Pilehvar & Camacho-Collados, 2018) from superGLUE (Wang et al., 2019) (Section 5.1).
  - [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf)
- **WNLI** (measurement instrument): *measured_by*, 1 paper
  > for inference tasks, the RTE and WNLI (both from GLUE) datasets (Section 4).
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > Natural Language Inference (NLI) using PIQA (Bisk et al., 2020) and WinoGrande (Sakaguchi et al., 2020) (Section 4).
  - [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 1 paper
  > Natural Language Inference (NLI) using PIQA (Bisk et al., 2020) and WinoGrande (Sakaguchi et al., 2020) (Section 4).
  - [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf)
- **Relation extraction** (behavioral indicator): *causes*, 1 paper
  > Recent research efforts have explored the potential of leveraging natural language inference (NLI) techniques to enhance relation extraction (RE). (Abstract)
  - [Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165.pdf)
- **LogicNLI** (measurement instrument): *measured_by*, 1 paper
  > We chose three representative datasets: LogicNLI (Tian et al., 2021) for natural language inference... (Section 5.2.1)
  - [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf)
- **HANS** (measurement instrument): *measured_by*, 1 paper
  > In particular, for NLI, we employed HANS (McCoy et al., 2019), NAN (Truong et al., 2022), PISP (Liu et al., 2020a,b), ST (Naik et al., 2018), and ANLIR1–R3 (Nie et al., 2020a)... (Section 4.1)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
- **PubMedQA** (measurement instrument): *measured_by*, 1 paper
  > For yes/no QA, we select PubMedQA (Jin et al., 2019), an English natural language inference task related to medical research papers. (Section 4.2)
  - [AQuilt: Weaving Logic and Self-Inspection into Low-Cost, High-Relevance Data Synthesis for Specialist LLMs](https://aclanthology.org/2025.emnlp-main.293.pdf)

### Associated with
- **Knowledge** (construct), 1 paper
  > notably NLI tasks, which require integrating knowledge and reasoning. (Section 1)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Textual reasoning** (behavioral indicator), 1 paper
  > Natural language reasoning suite consists of 11 benchmarks that involve natural language based reasoning such as Question Answering, natural language inference (NLI), sentence completion, co-reference resolution, and general intelligence.
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Grounded response generation** (behavioral indicator), 1 paper
  > If a tree Ti shows how H is entailed from a set of corpus texts Li, we say H is grounded in the corpus.
  - [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf)
- **Reasoning** (construct), 1 paper
  > notably NLI tasks, which require integrating knowledge and reasoning. (Section 1)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Logical reasoning** (construct), 1 paper
  > NLI is similar to deductive reasoning in assessing whether a premise supports or contradicts a hypothesis. (Section 6.3)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **General ability** (construct), 1 paper
  > we perform General Capability Tests using six natural language tasks... Specifically, the evaluation tasks include: ... 6. NLI (Natural Language Inference) (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Consistency** (construct), 1 paper
  > “NLI evaluates NLP models’ ability to capture logical relationships between sentences, serving as a proxy for the consistency condition.”
  - [A Novel Computational Modeling Foundation for Automatic Coherence Assessment](https://aclanthology.org/2025.naacl-long.277.pdf)
- **Natural language understanding** (construct), 1 paper
  > In the recent past, a popular way of evaluating natural language understanding (NLU), was to consider a model’s ability to perform natural language inference (NLI) tasks. (Abstract)
  - [Lost in Inference: Rediscovering the Role of Natural Language Inference for Large Language Models](https://aclanthology.org/2025.naacl-long.466.pdf)
