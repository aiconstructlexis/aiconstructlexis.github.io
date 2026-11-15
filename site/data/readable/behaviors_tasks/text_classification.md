# Text classification
**Type:** Behavioral indicator  
**Supporting papers:** 158  
**Also known as:** Topic classification, News headline classification, Hawkish-dovish classification, Argument unit classification, Deal completeness classification, ESG issue identification, Single-sentence classification, Textual classification, Data practice identification, Headline classification, Persuasion strategy classification, Note classification, Topic assignment, Resume classification, Occupation prediction, Question classification, Evergreen question classification, Long document classification, Question type classification, Section classification, Sequential sentence classification, Problem classification, Paper classification, Multi-label classification, Multilabel classification, Sequence classification, Document categorization, Text coding  

## State of the Field

**Space of definitions.** Across papers, the dominant framing treats text classification as assigning a predefined, discrete category to a text input, variously described as a sentence, sequence, document, or piece of text. Success is usually framed as producing the target class label, and one paper describes the common setup as inputting a sentence or paired sentences and outputting a categorical label. A smaller line of work broadens the task to multi-label outputs or other binary classification decisions.

**Variants.** Recurring variants include topic classification, sentiment analysis, question classification, sentence classification, and sequence classification. Other papers adapt the same behavior to specialized domains and alternative settings, including multilingual, long-document, and multi-label formulations.

**Space of elicitation and scores.** Text classification is measured by 27 linked instruments. The most frequently linked are AG News, TREC, GLUE, SST-2, and DBPedia, and papers use them as datasets or benchmark suites for news or topic classification, question classification, sentiment classification, or broader sequence-classification evaluation. Many other instruments also appear, including multilingual and domain-specific benchmarks.

**What it is taken as evidence of.** Papers link text classification to 4 constructs, but the recorded links are all broader related links rather than causal or measurement claims. The prevailing connection is to in-context learning, where papers use text classification tasks to study ICL ability or demonstration selection, while single papers also report related links to consistency, cross-lingual generalization, and semantic understanding. Papers therefore do not present a single agreed construct that this behavior measures.

## Sources

**Text classification** (41 papers: [A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf), [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf), [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf), [DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/e352b765e625934ce86919995e2371aa-Paper-Conference.pdf), [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf), [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf), [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf), [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [Out-of-Distribution Detection by Leveraging Between-Layer Transformation Smoothness](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a2f65c9d2313b71005e600bd23393fe-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf), [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf), [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf), [Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/9e79aefb538d02a7c0610fa43bdb0d0f-Paper-Conference.pdf), [Zero-Shot Robustification of Zero-Shot Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/92ce40962b4098f7bf6eed33128fc606-Paper-Conference.pdf), [Localized Zeroth-Order Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cef1316eaef9bd99da46f63334dc031-Paper-Conference.pdf), [Rethinking Invariance in In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/01e8ecf628f8d9f62a1fd433d44d34ab-Paper-Conference.pdf), [Token-based Decision Criteria Are Suboptimal in In-context Learning](https://aclanthology.org/2025.naacl-long.278.pdf), [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf), [Examining and Adapting Time for Multilingual Classification via Mixture of Temporal Experts](https://aclanthology.org/2025.naacl-long.313.pdf), [Active Few-Shot Learning for Text Classification](https://aclanthology.org/2025.naacl-long.340.pdf), [Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models](https://aclanthology.org/2025.naacl-long.632.pdf), [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.416.pdf), [Logit Separability-Driven Samples and Multiple Class-Related Words Selection for Advancing In-Context Learning](https://aclanthology.org/2025.naacl-long.343.pdf), [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf), [Cooperative or Competitive? Understanding the Interaction between Attention Heads From A Game Theory Perspective](https://aclanthology.org/2025.acl-long.688.pdf), [Direct Prompt Optimization with Continuous Representations](https://aclanthology.org/2025.acl-long.133.pdf), [Efficient Ensemble for Fine-tuning Language Models on Multiple Datasets](https://aclanthology.org/2025.acl-long.1231.pdf), [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf), [Impartial Multi-task Representation Learning via Variance-invariant Probabilistic Decoding](https://aclanthology.org/2025.acl-long.975.pdf), [LSSF: Safety Alignment for Large Language Models through Low-Rank Safety Subspace Fusion](https://aclanthology.org/2025.acl-long.1479.pdf), [LangSAMP: Language-Script Aware Multilingual Pretraining](https://aclanthology.org/2025.acl-long.88.pdf), [LlamaDuo: LLMOps Pipeline for Seamless Migration from Service LLMs to Small-Scale Local LLMs](https://aclanthology.org/2025.acl-long.1592.pdf), [Mitigating Shortcut Learning with InterpoLated Learning](https://aclanthology.org/2025.acl-long.450.pdf), [Multi-task Adversarial Attacks against Black-box Model with Few-shot Queries](https://aclanthology.org/2025.acl-long.684.pdf), [Plug-in and Fine-tuning: Bridging the Gap between Small Language Models and Large Language Models](https://aclanthology.org/2025.acl-long.271.pdf), [Recurrent Knowledge Identification and Fusion for Language Model Continual Learning](https://aclanthology.org/2025.acl-long.1328.pdf), [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf), [Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference](https://aclanthology.org/2025.acl-long.127.pdf), [Vulnerability of LLMs to Vertically Aligned Text Manipulations](https://aclanthology.org/2025.acl-long.978.pdf), [Where Are We? Evaluating LLM Performance on African Languages](https://aclanthology.org/2025.acl-long.1572.pdf))
> Assigning a discrete label to an input text sequence.

**Topic classification** (5 papers: [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf), [Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82cc56a5fa0287c438baa8be65a70-Paper-Conference.pdf), [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf), [D.Va: Validate Your Demonstration First Before You Use It](https://aclanthology.org/2025.acl-long.129.pdf), [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf))
> The task of identifying the main subject or topic of a document from a predefined set of topics.

**News headline classification** (1 paper: [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf))
> Classifying financial headlines according to whether they contain specific market-related information.

**Hawkish-dovish classification** (1 paper: [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf))
> Classifying monetary-policy text by whether it signals tightening, easing, or neutrality.

**Argument unit classification** (1 paper: [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of categorizing sentences in financial texts, such as earnings calls, into argumentative functions like 'claim' or 'premise'.

**Deal completeness classification** (1 paper: [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf))
> Classifying merger-and-acquisition mentions as completed deals or rumors.

**ESG issue identification** (1 paper: [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of detecting and classifying Environmental, Social, and Governance (ESG) related concerns within financial documents.

**Single-sentence classification** (1 paper: [Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf))
> The task of classifying a single sentence into a predefined category, such as determining its grammatical acceptability or sentiment.

**Textual classification** (1 paper: [Large Language Models are Interpretable Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/887932131fddf943e8fe3310b62c0147-Paper-Conference.pdf))
> The task of assigning a label to a text input, especially in scenarios where visual data is converted into descriptive text for evaluation.

**Data practice identification** (1 paper: [Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf))
> The observable task of classifying segments of a privacy policy into predefined categories related to data collection, use, and sharing.

**Persuasion strategy classification** (1 paper: [Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf))
> The observable task of identifying the persuasion techniques used in media content such as advertisements.

**Headline classification** (1 paper: [Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf))
> The task of assigning a news article to one of several predefined categories based on the content of its headline.

**Sentence classification** (2 papers: [Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82cc56a5fa0287c438baa8be65a70-Paper-Conference.pdf), [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf))
> The task of assigning a predefined category or label to a given sentence, such as for sentiment or topic analysis.

**Sequence classification** (3 papers: [ZETA: Leveraging $Z$-order Curves for Efficient Top-$k$ Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/b508c1737d9242e40552699a6e98c87b-Paper-Conference.pdf), [NeuroAda: Activating Each Neuron's Potential for Parameter-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.555.pdf), [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf))
> The observable task of assigning a categorical label to an entire input sequence.

**Note classification** (1 paper: [SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf))
> Categorizing social media notes into predefined topics or taxonomies based on content, in single- or multiple-choice format.

**Topic assignment** (1 paper: [Synthesizing Privacy-Preserving Text Data via Finetuning *without* Finetuning Billion-Scale LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25g/tan25g.pdf))
> Mapping a given document to a predefined topic cluster based on its content, using document embeddings and clustering techniques.

**Resume classification** (1 paper: [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf))
> Determining whether a resume is appropriate for a given job category, used to assess allocational bias in hiring-related decisions.

**Occupation prediction** (2 papers: [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf), [On the Mutual Influence of Gender and Occupation in LLM Representations](https://aclanthology.org/2025.acl-long.83.pdf))
> Predicting a person's job based on biographical information, used to assess whether models rely on gender or other stereotypes.

**Question classification** (1 paper: [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf))
> The task of classifying a question into a category based on the type of answer it expects (e.g., person, location, numeric).

**Evergreen question classification** (1 paper: [Will It Still Be True Tomorrow? Multilingual Evergreen Question Classification to Improve Trustworthy QA](https://aclanthology.org/2025.emnlp-main.434.pdf))
> The observable task of classifying a given question as either 'evergreen' (having a stable answer over time) or 'mutable' (having an answer that changes).

**Long document classification** (1 paper: [DrDiff: Dynamic Routing Diffusion with Hierarchical Attention for Breaking the Efficiency-Quality Trade-off](https://aclanthology.org/2025.emnlp-main.474.pdf))
> Assigning labels to lengthy documents based on their content.

**Question type classification** (1 paper: [LLM-Independent Adaptive RAG: Let the Question Speak for Itself](https://aclanthology.org/2025.emnlp-main.439.pdf))
> Categorizing questions into types such as count, comparative, or multihop based on their structure and reasoning requirements.

**Sequential sentence classification** (1 paper: [Section-Level Simplification of Biomedical Abstracts](https://aclanthology.org/2025.emnlp-main.697.pdf))
> The task of assigning a label to each sentence in a text that indicates its role or category, such as a section header.

**Section classification** (1 paper: [Section-Level Simplification of Biomedical Abstracts](https://aclanthology.org/2025.emnlp-main.697.pdf))
> The process of assigning section labels (e.g., Background, Results) to sentences in a plain language summary based on content and context.

**Problem classification** (1 paper: [MA-GTS: A Multi-Agent Framework for Solving Complex Graph Problems in Real-World Applications](https://aclanthology.org/2025.emnlp-main.973.pdf))
> Determining the type of graph problem (e.g., TSP, Vertex Cover) from natural language descriptions and extracting constraints and optimization objectives.

**Paper classification** (1 paper: [GraphAgent: Agentic Graph Language Assistant](https://aclanthology.org/2025.emnlp-main.1339.pdf))
> The task of assigning a predefined category or label to a scientific paper based on its content.

**Multi-label classification** (1 paper: [ViClaim: A Multilingual Multilabel Dataset for Automatic Claim Detection in Videos](https://aclanthology.org/2025.emnlp-main.21.pdf))
> The task of assigning one or more labels to an input, such as a sentence, from a predefined set of categories.

**Multilabel classification** (1 paper: [MoVa: Towards Generalizable Classification of Human Morals and Values](https://aclanthology.org/2025.emnlp-main.1687.pdf))
> The observable task of assigning zero, one, or multiple labels from a predefined set to a single text example, reflecting the co-occurrence of moral dimensions.

**Document categorization** (1 paper: [Latent Factor Models Meets Instructions: Goal-conditioned Latent Factor Discovery without Task Supervision](https://aclanthology.org/2025.naacl-long.554.pdf))
> Assigning documents to high-level or fine-grained topical labels using learned latent representations.

**Text coding** (1 paper: [SCALE: Towards Collaborative Content Analysis in Social Science with Large Language Model Agents and Human Intervention](https://aclanthology.org/2025.acl-long.416.pdf))
> Converting unstructured text entries into discrete numerical categories based on a codebook of theory-driven rules, analogous to text classification.

## Relationships

### Text classification →
- **AG News** (measurement instrument): *measured_by*, 19 papers
  > SST-2 (Socher et al., 2013) and AGNews (Zhang et al., 2015) are text classification tasks with different class numbers
  - [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
  - [LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect](https://proceedings.neurips.cc/paper_files/paper/2024/file/064f6bcd7d3c72fb187bfca35ba2bfd4-Paper-Conference.pdf)
  - [Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
  - [Can Generative AI Solve Your In-Context Learning Problem? A Martingale Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/d90268f01ef06a55630b0588227adf4f-Paper-Conference.pdf)
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
  - [Data-adaptive Differentially Private Prompt Synthesis for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96d00450ed65531ffe2996daed487536-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
  - [LSSF: Safety Alignment for Large Language Models through Low-Rank Safety Subspace Fusion](https://aclanthology.org/2025.acl-long.1479.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [Plausible Token Amplification for Improving Accuracy of Differentially Private In-Context Learning Based on Implicit Bayesian Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yamasaki25a/yamasaki25a.pdf)
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
  - [Continuous-Time Attention: PDE-Guided Mechanisms for Long-Sequence Transformers](https://aclanthology.org/2025.emnlp-main.1097.pdf)
  - [CondenseLM: LLMs-driven Text Dataset Condensation via Reward Matching](https://aclanthology.org/2025.emnlp-main.65.pdf)
  - [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486.pdf)
  - [SliceMoE: Routing Embedding Slices Instead of Tokens for Fine-Grained and Balanced Transformer Scaling](https://aclanthology.org/2025.emnlp-main.807.pdf)
- **TREC** (measurement instrument): *measured_by*, 8 papers
  > We study 4-way news classification AGNews (Zhang et al., 2015), 6-way question classification TREC (Voorhees & Tice, 2000)... (Section 5.1)
  - [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
  - [DP-OPT: Make Large Language Model Your Privacy-Preserving Prompt Engineer](https://proceedings.iclr.cc/paper_files/paper/2024/file/fffe5a7804c40465ef2432386850c2c7-Paper-Conference.pdf)
  - [Data-adaptive Differentially Private Prompt Synthesis for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96d00450ed65531ffe2996daed487536-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
  - [Plausible Token Amplification for Improving Accuracy of Differentially Private In-Context Learning Based on Implicit Bayesian Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yamasaki25a/yamasaki25a.pdf)
  - [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf)
  - [Transplant Then Regenerate: A New Paradigm for Text Data Augmentation](https://aclanthology.org/2025.emnlp-main.702.pdf)
- **GLUE** (measurement instrument): *measured_by*, 7 papers
  > We evaluate on GLUE [70] for text classification and GSM-8K [9] for mathematical reasoning (Section 4).
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
  - [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf)
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
  - [Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf)
  - [SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3504a4fa45685d668ce92797fbbf1895-Paper-Conference.pdf)
  - [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf)
  - [NeuroAda: Activating Each Neuron's Potential for Parameter-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.555.pdf)
- **SST-2** (measurement instrument): *measured_by*, 7 papers
  > We study text classification using four datasets: sentiment analysis using SST-2 (Socher et al., 2013)... (Section 4.1)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
  - [Mini-batch Coresets for Memory-efficient Language Model Training on Data Mixtures](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd141278c2cf38ae1e4aee909451fb61-Paper-Conference.pdf)
  - [CondenseLM: LLMs-driven Text Dataset Condensation via Reward Matching](https://aclanthology.org/2025.emnlp-main.65.pdf)
- **DBPedia** (measurement instrument): *measured_by*, 5 papers
  > ...and 14-way topic classification DBPedia (Zhang et al., 2015) datasets for classification tasks. (Section 5.1)
  - [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
  - [Data-adaptive Differentially Private Prompt Synthesis for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96d00450ed65531ffe2996daed487536-Paper-Conference.pdf)
  - [Plausible Token Amplification for Improving Accuracy of Differentially Private In-Context Learning Based on Implicit Bayesian Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yamasaki25a/yamasaki25a.pdf)
- **IMDb** (measurement instrument): *measured_by*, 4 papers
  > Table 1: Overview of the tasks, datasets... Task Text Classification Dataset IMDB
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
  - [EMO: Embedding Model Distillation via Intra-Model Relation and Optimal Transport Alignments](https://aclanthology.org/2025.emnlp-main.385.pdf)
  - [CondenseLM: LLMs-driven Text Dataset Condensation via Reward Matching](https://aclanthology.org/2025.emnlp-main.65.pdf)
  - [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486.pdf)
- **Emotion (dair-ai)** (measurement instrument): *measured_by*, 4 papers
  > Following Zhang et al. (2023b), we evaluate on a series of Text Classification datasets: CoLA (2 labels) (Warstadt et al., 2019), Emotion (6 labels) (Saravia et al., 2018)... (Section 3.1)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
  - [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486.pdf)
  - [SliceMoE: Routing Embedding Slices Instead of Tokens for Fine-Grained and Balanced Transformer Scaling](https://aclanthology.org/2025.emnlp-main.807.pdf)
- **SIB-200** (measurement instrument): *measured_by*, 3 papers
  > We evaluate our models on five widely adopted multilingual benchmarks in a zero-shot setting, covering a range of tasks: ... and text classification (SIB-200; Adelani et al., 2024). (Section 3)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
  - [A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages](https://aclanthology.org/2025.emnlp-main.418.pdf)
  - [It's All About In-Context Learning! Teaching Extremely Low-Resource Languages to LLMs](https://aclanthology.org/2025.emnlp-main.1502.pdf)
- **Rotten Tomatoes** (measurement instrument): *measured_by*, 3 papers
  > We primarily evaluate our method on AG News (4 classes) [77], SST-2 (2 classes) [57], Rotten Tomatoes (2 classes) [50], and Subj (2 classes) [18] datasets which all admit classification tasks. (Section 5.2)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
- **Subj** (measurement instrument): *measured_by*, 2 papers
  > We primarily evaluate our method on AG News (4 classes) [77], SST-2 (2 classes) [57], Rotten Tomatoes (2 classes) [50], and Subj (2 classes) [18] datasets which all admit classification tasks. (Section 5.2)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
- **Standard CL Benchmark** (measurement instrument): *measured_by*, 2 papers
  > “This benchmark comprises five text classification datasets: AG News, Amazon Reviews, Yelp Reviews, DBpedia, and Yahoo Answers”
  - [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf)
  - [AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning](https://aclanthology.org/2025.emnlp-main.678.pdf)
- **Financial PhraseBank** (measurement instrument): *measured_by*, 2 papers
  > We assessed our proposed methods by comparing them with standard loss functions across several text classification benchmarks, including Financial Phrasebank (Financial) (Malo et al., 2014), irony detection (Tweet Irony) (Van Hee et al., 2018), and the MRPC dataset from GLUE (Wang et al., 2018).
  - [Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/03dfa2a7755635f756b160e9f4c6b789-Paper-Conference.pdf)
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
- **OpenReview** (measurement instrument): *measured_by*, 2 papers
  > We conduct experiments on two classiﬁcation tasks: Yelp (Yelp, Inc.) and OpenReview (Xie et al., 2024), both of which are 5-way classiﬁcation... (Section 4.1.1)
  - [Synthesizing Privacy-Preserving Text Data via Finetuning *without* Finetuning Billion-Scale LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25g/tan25g.pdf)
  - [Private Federated Learning using Preference-Optimized Synthetic Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25g/hou25g.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > In Table 2, we present the text classification results of different dataset pruning methods on the MMLU benchmark. (Section 4.2.2)
  - [Exploring Learning Complexity for Efficient Downstream Dataset Pruning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7e4aab3786a1f8e39e0f9b8dd9fa105-Paper-Conference.pdf)
- **Jigsaw** (measurement instrument): *measured_by*, 1 paper
  > For the Classification task in Indirect Evaluation, we utilize existing tabular bias evaluation datasets to construct new datasets. Particularly... we utilize the following datasets: Adult (Dua et al., 2017), Credit (Yeh & Lien, 2009), and Jigsaw (Cjadams et al., 2019).
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **20 Newsgroups** (measurement instrument): *measured_by*, 1 paper
  > When conducting domain shift poisoning pre-training, we utilize the IMDB (Maas et al., 2011), Twitter (Founta et al., 2018), and 20 Newsgroups (Lang, 1995) as the proxy dataset for sentiment analysis, toxicity detection, and topic classification task, respectively (Section 5.1).
  - [Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
- **Super-NaturalInstructions** (measurement instrument): *measured_by*, 1 paper
  > The Super-Natural instruction dataset (Wang et al., 2022) contains a collection of 1600+ NLP tasks, including both classiﬁcation and generation tasks.
  - [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf)
- **Yelp** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on two classiﬁcation tasks: Yelp (Yelp, Inc.) and OpenReview (Xie et al., 2024), both of which are 5-way classiﬁcation... (Section 4.1.1)
  - [Synthesizing Privacy-Preserving Text Data via Finetuning *without* Finetuning Billion-Scale LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25g/tan25g.pdf)
- **QNLI** (measurement instrument): *measured_by*, 1 paper
  > QNLI: This is a dataset containing sentence pairs for binary classification (entailment/not entailment). (Section 5)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **BANKING77** (measurement instrument): *measured_by*, 1 paper
  > Text Classification: Requires models to capture the overall semantics of a single text input. We use Patent (Sharma et al., 2019), Imdb and Banking77 (both from MTEB (Muennighoff et al., 2023)). (Section 4.1)
  - [EMO: Embedding Model Distillation via Intra-Model Relation and Optimal Transport Alignments](https://aclanthology.org/2025.emnlp-main.385.pdf)
- **MNLI** (measurement instrument): *measured_by*, 1 paper
  > We experiment on four large-scale text classification datasets: SST-2 (Socher et al., 2013), MNLI (Williams et al., 2018), AG News (Zhang and LeCun, 2015), and IMDB (Maas et al., 2011) (Section 3.1).
  - [CondenseLM: LLMs-driven Text Dataset Condensation via Reward Matching](https://aclanthology.org/2025.emnlp-main.65.pdf)
- **Twitter Financial News Sentiment** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our models on 9 text classification benchmark datasets ... These are: AG News (Zhang et al., 2015), Emotion (Saravia et al., 2018), Stanford Sentiment Treebank (SST2 & SST5) (Socher et al., 2013), Multiclass Sentiment Analysis, Twitter Financial News Sentiment, IMDb (Maas et al., 2011), and Hate Speech Offensive (Davidson et al., 2017).
  - [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486.pdf)
- **Plutus-ben** (measurement instrument): *measured_by*, 1 paper
  > “Plutus-ben addresses six core tasks: numeric/textual named entity recognition, question answering, extractive summarization, abstractive summarization, and topic classification.”
  - [Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance](https://aclanthology.org/2025.emnlp-main.1535.pdf)
- **LaMP** (measurement instrument): *measured_by*, 1 paper
  > "LaMP benchmark consisting of various text classification and generation tasks"
  - [Personalized Language Models via Privacy-Preserving Evolutionary Model Merging](https://aclanthology.org/2025.emnlp-main.1747.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > All the tasks except for MT are classification tasks, where we use the lm-evaluation-harness (Gao et al., 2024) evaluation tool and report accuracy. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **Amazon Polarity** (measurement instrument): *measured_by*, 1 paper
  > We study text classification using four datasets: sentiment analysis using SST-2 (Socher et al., 2013) and Amazon (Zhang et al., 2015)... (Section 4.1)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **CoLA** (measurement instrument): *measured_by*, 1 paper
  > Following Zhang et al. (2023b), we evaluate on a series of Text Classification datasets: CoLA (2 labels) (Warstadt et al., 2019)... (Section 3.1)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)

### Associated with
- **In-context learning** (construct), 3 papers
  > We evaluate the in-context learnig ability of ICLM using 32 demonstration examples. We use seven text classification datasets... (Section 3.3.2)
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
  - [Implicit In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc034d186280f55370b6aca7a3285a65-Paper-Conference.pdf)
- **Semantic understanding** (construct), 1 paper
  > Topic Classification (TC) as a primarily semantic task (Section 1)
  - [Tokenization and Representation Biases in Multilingual Models on Dialectal NLP Tasks](https://aclanthology.org/2025.emnlp-main.1224.pdf)
- **Consistency** (construct), 1 paper
  > We therefore introduce two metrics for classification tasks, namely sensitivity and consistency, which are complementary to task performance. (Abstract)
  - [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Cross-lingual generalization** (construct), 1 paper
  > We conducted continued pre-training of open-source LLMs using corpora obtained through various transliteration methods, analyzed cross-lingual transfer performance across text classification, named entity recognition, machine reading comprehension, knowledge extraction, and machine translation tasks (Section 1).
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)
