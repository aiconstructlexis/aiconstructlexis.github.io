# Machine reading comprehension
**Type:** Behavioral indicator  
**Supporting papers:** 65  
**Also known as:** Paragraph understanding, Reading comprehension  

## State of the Field

**Space of definitions.** Across the surveyed papers, the prevailing usage treats machine reading comprehension as passage-based question answering: reading a passage, paragraph, or other text and answering questions from its content. Several definitions make this explicit as machine reading comprehension, and some narrow it to cross-lingual settings where the question and passage may be in different languages; a smaller line of work uses nearby wording such as paragraph understanding or talks about reading comprehension skills as understanding written scientific content well enough to extract or infer explanations and notes. The common success condition is giving the answer supported by the provided text, often by selecting the correct option in multiple-choice settings, though some papers frame it as yes/no inference from the text itself.

**Variants.** Papers use several nearby names for this behavior, most often reading comprehension and machine reading comprehension, with smaller usages including paragraph understanding and comprehensive reading. The studied settings range from cross-lingual and low-resource variants, including benchmarks used for Tibetan, Chinese, Basque, Indonesian, and multilingual evaluation, to more specialized forms such as conversational or closed-book reading comprehension, multi-hop reasoning, discrete-reasoning reading comprehension, long-document reading comprehension, document-image reading comprehension, and Note-MRC over SNS text.

**Space of elicitation and scores.** Papers measure this behavior with 25 linked instruments. The most frequently linked are BoolQ, RACE, SQuAD 2.0, Belebele, and SQuAD v1.1, and these are mostly benchmark datasets covering yes/no reading comprehension, multiple-choice passage reasoning, question plus context settings, and multilingual machine reading comprehension; papers also use frameworks such as lm-evaluation-harness alongside many other benchmarks. Scoring is usually automatic, with accuracy used in multiple-choice and yes/no settings, exact match from context used in some work, and F1 reported for DROP.

**What it is taken as evidence of.** Papers link machine reading comprehension to 3 constructs, but they do not converge on a single construct that this behavior is taken to reflect. One paper claims a causal relationship from Machine reading comprehension to Domain knowledge, stating that the use of reading comprehension texts provides domain knowledge for domain-specific tasks. Separate papers report a related link from Knowledge conflict resolution to Machine reading comprehension, describing the former as requiring strong reading comprehension skills, and a related link from Machine reading comprehension to Note comprehension through Note-MRC, which is presented as testing reading comprehension in SNS content.

## Sources

**Machine reading comprehension** (3 papers: [Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages](https://aclanthology.org/2025.emnlp-main.1407.pdf), [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf), [Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages](https://aclanthology.org/2025.acl-long.893.pdf))
> The task of answering questions based on a given context passage, where the questions and passage may be in different languages.

**Paragraph understanding** (1 paper: [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf))
> The observable task of reading a paragraph and answering a question based on its content.

**Reading comprehension** (5 papers: [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf), [Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque](https://aclanthology.org/2025.naacl-long.629.pdf), [EmojiPrompt: Generative Prompt Obfuscation for Privacy-Preserving Communication with Cloud-based LLMs](https://aclanthology.org/2025.naacl-long.614.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [JRE-L: Journalist, Reader, and Editor LLMs in the Loop for Science Journalism for the General Audience](https://aclanthology.org/2025.naacl-long.335.pdf))
> The general task of reading a passage of text and answering questions about its content.

## Relationships

### Machine reading comprehension →
- **BoolQ** (measurement instrument): *measured_by*, 10 papers
  > Reading Comprehension (0-shot): BoolQ (Clark et al., 2019). (Section 4.2).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
  - [The Unreasonable Ineffectiveness of the Deeper Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbabc2f70de2dd09f491a8715ec3e80f-Paper-Conference.pdf)
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
  - [LLM Data Selection and Utilization via Dynamic Bi-level Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25g/yu25g.pdf)
  - [From Understanding to Generation: An Efficient Shortcut for Evaluating Language Models](https://aclanthology.org/2025.emnlp-main.1148.pdf)
- **RACE** (measurement instrument): *measured_by*, 7 papers
  > RACE is a reading comprehension benchmark introduced in Lai et al. (2017) collected from English examinations of middle and high school students. (Section 3)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
  - [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [Flexora: Flexible Low-Rank Adaptation for Large Language Models](https://aclanthology.org/2025.acl-long.713.pdf)
  - [MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25d/xiao25d.pdf)
- **SQuAD 2.0** (measurement instrument): *measured_by*, 5 papers
  > “our reading comprehension (RC) fine-tuning datasets include SQuAD 2.0 ...”
  - [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
  - [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf)
  - [From Understanding to Generation: An Efficient Shortcut for Evaluating Language Models](https://aclanthology.org/2025.emnlp-main.1148.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 4 papers
  > Reading Comprehension (RC): SQuAD-3-shots [50], BoolQ-0-shot [12], and CoQA-0-shot [51].
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa27ac7aca4e462da1439b43ceebc04c-Paper-Conference.pdf)
  - [GraphRouter: A Graph-based Router for LLM Selections](https://proceedings.iclr.cc/paper_files/paper/2025/file/41b6674c28a9b93ec8d22a53ca25bc3b-Paper-Conference.pdf)
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)
- **Belebele** (measurement instrument): *measured_by*, 4 papers
  > Belebele (Bandarkar et al., 2024): Belebele is a multiple-choice machine reading comprehension dataset spanning 122 language variants. (Section 3.3)
  - [Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque](https://aclanthology.org/2025.naacl-long.629.pdf)
  - [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf)
  - [It's All About In-Context Learning! Teaching Extremely Low-Resource Languages to LLMs](https://aclanthology.org/2025.emnlp-main.1502.pdf)
  - [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 3 papers
  > For our performance evaluation, we use the few-shot tasks from Language Model Evaluation Harness (Gao et al., 2021). We select these tasks such that they can measure various abilities of the models (e.g., reading comprehension, reasoning, etc.) (Sec. 3.1)
  - [ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6cf669c222ad13f60d503736fb2bd15b-Paper-Conference.pdf)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
  - [Neural ODE Transformers: Analyzing Internal Dynamics and Adaptive Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/82e3509393670d9d478c359b4ce6f950-Paper-Conference.pdf)
- **DROP** (measurement instrument): *measured_by*, 3 papers
  > DROP [50] Task Reading comprehension with discrete reasoning (Table D.1).
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
  - [Automated Design of Agentic Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf)
  - [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 3 papers
  > we use seven commonsense reasoning tasks from the popular framework Harness (Gao et al., 2024), including four reading comprehension tasks (ARC-e, ARC-c (Clark et al., 2018), OBQA (Mihaylov et al., 2018), and BoolQ (Clark et al., 2019))... (Section 4.1)
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **CoQA** (measurement instrument): *measured_by*, 2 papers
  > Reading Comprehension (RC): SQuAD-3-shots [50], BoolQ-0-shot [12], and CoQA-0-shot [51].
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 2 papers
  > For common sense and reading comprehension tasks, we report 0-shot accuracy results for SciQ [22], PIQA [23], WinoGrande (Wino.) [24], ARC Easy(ARC-E.) [25], and HellaSwag (HellaS.) [26], alongside 25-shot accuracy for ARC Challenge (ARC-C.) [27]. (Section 5.1)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **ARC** (measurement instrument): *measured_by*, 2 papers
  > Reading comprehension and commonsense reasoning improves. For ARC and HellaSwag, preference optimization methods generally improve performance compared to the SFT checkpoint.
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
- **MultiRC** (measurement instrument): *measured_by*, 2 papers
  > Additionally, we use ARC (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018), and MultiRC (Khashabi et al., 2018), covering question answering, commonsense reasoning, and reading comprehension, as validation sets for generalization loss estimation.
  - [Optimizing Pre-Training Data Mixtures with Mixtures of Data Expert Models](https://aclanthology.org/2025.acl-long.1564.pdf)
  - [Regress, Don’t Guess: A Regression-like Loss on Number Tokens for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zausinger25a/zausinger25a.pdf)
- **TibetanQA** (measurement instrument): *measured_by*, 2 papers
  > For the machine reading comprehension task, we evaluate the models’ performance by fine-tuning them on the Chinese CMRC dataset (Cui et al., 2019) and English SQuAD dataset (Rajpurkar, 2016), followed by zero-shot testing on the TibetanQA dataset (Sun et al., 2021) to assess their cross-lingual transfer capabilities (Section 4.3).
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)
  - [Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages](https://aclanthology.org/2025.acl-long.893.pdf)
- **Domain knowledge** (construct): *causes*, 1 paper
  > the utilization of reading comprehension texts provides domain knowledge that enhances performance in domain-specific tasks. (Section 6)
  - [Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf)
- **C3** (measurement instrument): *measured_by*, 1 paper
  > a free-form multiple-choice Chinese machine reading comprehension dataset (C3) (Sun et al., 2020) (Section 3.3.5)
  - [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > For common sense and reading comprehension tasks, we report 0-shot accuracy results for SciQ [22], PIQA [23], WinoGrande (Wino.) [24], ARC Easy(ARC-E.) [25], and HellaSwag (HellaS.) [26], alongside 25-shot accuracy for ARC Challenge (ARC-C.) [27]. (Section 5.1)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > For common sense and reading comprehension tasks, we report 0-shot accuracy results for SciQ [22], PIQA [23], WinoGrande (Wino.) [24], ARC Easy(ARC-E.) [25], and HellaSwag (HellaS.) [26], alongside 25-shot accuracy for ARC Challenge (ARC-C.) [27]. (Section 5.1)
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **QuALITY** (measurement instrument): *measured_by*, 1 paper
  > The QuALITY dataset is a reading comprehension task consisting of documents (about 5k tokens long) with a set of multiple choice reading comprehension questions. (Appendix F.1)
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 1 paper
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > we evaluate the models from Figure 3 on five downstream tasks: ARC-easy, lambada, RACE, PIQA, and BoolQ, which collectively test for common sense reasoning, world knowledge, and reading comprehension. (Section 4.3)
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **WikiHop** (measurement instrument): *measured_by*, 1 paper
  > Reading Comprehension ... We primarily consider WIKIHOP [31] in the task, which necessitates multi-hop reasoning to derive the final answer.
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > Reading Comprehension:TriviaQA [42] (0-shot), with the assessment based on the exact match from context. (Section 3.1).
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
- **DocVQA** (measurement instrument): *measured_by*, 1 paper
  > DocVQA (Mathew et al., 2021) focuses on reading comprehension tasks over document images. (Section 4.1)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **SciQA** (measurement instrument): *measured_by*, 1 paper
  > Additionally, the DWM not only enhances the model’s performance on reading comprehension tasks, such as SciQA and BoolQ, but also improves its performance on commonsense reasoning tasks, such as the WinoGrande.
  - [LLM Data Selection and Utilization via Dynamic Bi-level Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25g/yu25g.pdf)
- **FilBench** (measurement instrument): *measured_by*, 1 paper
  > “FILBENCH, a Filipino-centric benchmark designed to evaluate LLMs across a diverse set of tasks and capabilities in Filipino, Tagalog, and Cebuano. We carefully curate the tasks in FILBENCH to reflect the priorities and trends of NLP research in the Philippines such as Cultural Knowledge, Classical NLP, Reading Comprehension, and Generation.”
  - [FilBench: Can LLMs Understand and Generate Filipino?](https://aclanthology.org/2025.emnlp-main.127.pdf)
- **TyDi QA** (measurement instrument): *measured_by*, 1 paper
  > We adopt the Indonesian set from TyDi QA (Clark et al., 2020) for reading comprehension, which is based on Indonesian Wikipedia with human-written questions. (Section 3.3)
  - [LORAXBENCH: A Multitask, Multilingual Benchmark Suite for 20 Indonesian Languages](https://aclanthology.org/2025.emnlp-main.881.pdf)

### Associated with
- **Knowledge conflict resolution** (construct), 1 paper
  > To achieve this, it requires strong reading comprehension skills to interpret and extract accurate information as well as confidence reasoning...
  - [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf)
- **Note comprehension** (construct), 1 paper
  > Note Comprehension. Models must understand and analyze textual content within SNS... The designed tasks are: ... (2) Note-MRC. Tests reading comprehension...
  - [SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf)
