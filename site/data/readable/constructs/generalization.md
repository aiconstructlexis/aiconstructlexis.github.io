# Generalization
**Type:** Construct  
**Supporting papers:** 1194  
**Also known as:** Generalizability, Generalization ability, Generalization capability, Generalization performance, Generalisation, Generalisability, Task-agnostic generalizability, Domain-generality, Single-task generalization, Sequence generalization  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats generalization as transfer beyond the training setup: maintaining useful performance or learned behavior on new, unseen, or out-of-distribution data, tasks, domains, instructions, tools, users, languages, modalities, or environments. Many definitions also set it against memorization or overfitting, asking whether results reflect "genuine ability or just memorization of the training data" (DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks). Smaller lines narrow it to particular settings, such as preserving performance across model sizes or evaluation settings after quantization, extending edited or abstention behavior to related inputs, or preserving the union of skills in merged models. Papers also vary on whether it is a latent property of a model, method, prompt, or attack, or an observed pattern of test performance or error under distribution shift.

**Space of facets.** Papers use several near-synonymous labels, especially generalizability, generalization ability, generalization capability, and generalization performance. The broad construct is commonly decomposed by what must transfer, across tasks, domains, datasets, languages, modalities, environments, prompt forms, or neighboring edited samples, and some papers make finer distinctions such as unseen instructions, unseen tools in seen categories, and unseen tools in unseen categories. A smaller set introduces narrower variants, including task-agnostic generalizability, domain-generality, sequence generalization, single-task generalization, and generality in merging or editing, where the concern is preserving the union of skills or applying an edit to related inputs. It is repeatedly contrasted with memorization and contamination, and in the abstention line it is explicitly tied to a trade-off with specificity.

**Space of measurement.** Operationalization is mostly benchmark-based. Papers link the construct to 103 measurement instruments and 15 behavioral indicators, with the most frequently linked instruments including MMLU, MT-Bench, ARC-Challenge, TriviaQA, and ALFWorld, and the behavioral indicators most often linked including catastrophic forgetting, code editing, few-shot task performance, abstention, and formal theorem proving. These instruments are usually used as held-out, zero-shot, few-shot, cross-domain, or out-of-distribution tests across tasks, websites, databases, environments, or question styles, while a smaller line uses LLM-as-a-judge, for example GPT-4 judgments on out-of-domain generations. Operationalizations also include explicit generalization error, seen versus unseen split performance, neighboring-sample response after editing, and abstention on descendants, so measurement spans both transfer benchmarks and more targeted probes.

**Links.** The most prevalent linked claim is a causal relationship from In-context learning to Generalization, often described as enabling transfer to new tasks from a few exemplars or contextual information, and some additional papers relate the two without making a causal claim. Several papers also claim causal relationships from Memorization, Overfitting, Reasoning, Knowledge transfer, Inductive reasoning, Inductive bias, Self-improvement, Expert specialization, Model collapse, and the behavioral indicator Catastrophic forgetting to Generalization, while some additional papers only relate several of these pairs; depending on the paper, these links are described as either enabling broader transfer or degrading it. A smaller line reverses the direction, claiming causal relationships from Generalization to In-context learning and Robustness, and one paper also links it causally to formal theorem proving. Generalization is also reported to correlate with Flatness and Instruction understanding, and is related to Specialization, Personalization, Reliability, Specificity, Universality, Abstention, Hallucination, Fairness, text generation, and application behaviors such as harmful content detection and image tasks.

## Sources

**Generalization** (135 papers: [$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf), [A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf), [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf), [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf), [AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7641940c7dd9e5de58c20e39586eb64-Paper-Conference.pdf), [Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e9034dd5420660d86c8c360c35a895e-Paper-Conference.pdf), [Can Large Language Models Infer Causation from Correlation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b75a7339dfb256ee4b4bec028a6890b-Paper-Conference.pdf), [CivRealm: A Learning and Reasoning Odyssey in Civilization for Decision-Making Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/76d2f8e328e1081c22a77ca0fa330ca5-Paper-Conference.pdf), [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf), [Compositional Preference Models for Aligning LMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/8fd10360ac9de462ffd36155d87ee999-Paper-Conference.pdf), [Compressed Context Memory for Online Language Model Interaction](https://proceedings.iclr.cc/paper_files/paper/2024/file/97dc07f1253ab33ee514f395a82fa7cc-Paper-Conference.pdf), [Conversational Drug Editing Using Retrieval and Domain Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/d390199c28b467315b454789b6584f19-Paper-Conference.pdf), [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf), [DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf), [Energy-based Automated Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5ef1df239d6640a27dd6ed9a59f518c9-Paper-Conference.pdf), [Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/5dc6d1c81754c32008c9667339b3fdd3-Paper-Conference.pdf), [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf), [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf), [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf), [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf), [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf), [In-context Autoencoder for Context Compression in a Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b276510ec2d3f6613a8b60c41ff0438-Paper-Conference.pdf), [Ins-DetCLIP: Aligning Detection Model to Follow Human-Language Instruction](https://proceedings.iclr.cc/paper_files/paper/2024/file/accb5f309ec092a6787a1879ad5f2a5f-Paper-Conference.pdf), [It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf), [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf), [LEGO-Prover: Neural Theorem Proving with Growing Libraries](https://proceedings.iclr.cc/paper_files/paper/2024/file/85dca46374dc0f27b4bb5f265b3d17f0-Paper-Conference.pdf), [LILO: Learning Interpretable Libraries by Compressing and Documenting Code](https://proceedings.iclr.cc/paper_files/paper/2024/file/819cebb05f993840e8a52d7564c5c282-Paper-Conference.pdf), [LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/7f70331dbe58ad59d83941dfa7d975aa-Paper-Conference.pdf), [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf), [Language Modeling Is Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/3cbf627fa24fb6cb576e04e689b9428b-Paper-Conference.pdf), [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf), [Large Language Models as Generalizable Policies for Embodied Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/8f9461d11e8ce9b0b28b21bfc645d74e-Paper-Conference.pdf), [Learning Grounded Action Abstractions from Language](https://proceedings.iclr.cc/paper_files/paper/2024/file/99dec5837aae1a7459960c6121b9e3b8-Paper-Conference.pdf), [Learning with Language-Guided State Abstractions](https://proceedings.iclr.cc/paper_files/paper/2024/file/a84de7bd46172264d137b07ae7f00a8a-Paper-Conference.pdf), [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf), [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf), [LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/39ec972afab01e0d8ddc6834a9d12ac1-Paper-Conference.pdf), [MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b063829b922fdeb4fa3472dd3471ff43-Paper-Conference.pdf), [MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf), [MUFFIN: Curating Multi-Faceted Instructions for Improving Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d1a0188e18c1d74a0f8d6eb5ecede4f-Paper-Conference.pdf), [Making Pre-trained Language Models Great on Tabular Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/668563ef18fbfef0b66af491ea334d5f-Paper-Conference.pdf), [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf), [MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/15425f2df99aa1ba52712c9a4afc8536-Paper-Conference.pdf), [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c400474e8a36d0812fdee52739288b12-Paper-Conference.pdf), [Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce806d8b4bf38cd92d483e5a0490d983-Paper-Conference.pdf), [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf), [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf), [OWL: A Large Language Model for IT Operations](https://proceedings.iclr.cc/paper_files/paper/2024/file/6581ff85ba0ca663513d5f65b25f6631-Paper-Conference.pdf), [OctoPack: Instruction Tuning Code Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1ec299a5229034141e58aeded0d0b9de-Paper-Conference.pdf), [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf), [OpenWebMath: An Open Dataset of High-Quality Mathematical Web Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf), [Proving Test Set Contamination in Black-Box Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/46e624c244cff669223d488defd4e835-Paper-Conference.pdf), [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf), [Scaling Laws for Associative Memories](https://proceedings.iclr.cc/paper_files/paper/2024/file/28f734334f9f325b515933e70b6b412c-Paper-Conference.pdf), [SmartPlay : A Benchmark for LLMs as Intelligent Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/063d1fadbde557466bf5bcffe814a64e-Paper-Conference.pdf), [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://proceedings.iclr.cc/paper_files/paper/2024/file/52f050499cf82fa8efb588e263f6f3a7-Paper-Conference.pdf), [TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series](https://proceedings.iclr.cc/paper_files/paper/2024/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf), [Text2Reward: Reward Shaping with Language Models for Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/9941833e8327910ef25daeb9005e4748-Paper-Conference.pdf), [The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”](https://proceedings.iclr.cc/paper_files/paper/2024/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf), [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://proceedings.iclr.cc/paper_files/paper/2024/file/28e50ee5b72e90b50e7196fde8ea260e-Paper-Conference.pdf), [Towards Few-Shot Adaptation of Foundation Models via Multitask Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d9a0718883f4a2eecee3c69c7213b05-Paper-Conference.pdf), [Towards Unified Multi-Modal Personalization: Large Vision-Language Models for Generative Recommendation and Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/297a7a54da76d95f02b04d957a53c7ba-Paper-Conference.pdf), [Training Socially Aligned Language Models on Simulated Social Interactions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d763b4a2dde0ae7b77498516ce9f439e-Paper-Conference.pdf), [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf), [Turning large language models into cognitive models](https://proceedings.iclr.cc/paper_files/paper/2024/file/84b686f7cc7b7751e9aaac0da74f755a-Paper-Conference.pdf), [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf), [Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/9e79aefb538d02a7c0610fa43bdb0d0f-Paper-Conference.pdf), [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf), [Unified Human-Scene Interaction via Prompted Chain-of-Contacts](https://proceedings.iclr.cc/paper_files/paper/2024/file/6a6ecedac816a24f92ad1f444b1edcb0-Paper-Conference.pdf), [Universal Jailbreak Backdoors from Poisoned Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/d1e63f4027efc7c44bfc253eafc15a58-Paper-Conference.pdf), [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf), [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf), [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf), [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf), [Enhancing Language Model Hypernetworks with Restart: A Study on Optimization](https://aclanthology.org/2025.naacl-long.397.pdf), [UniHGKR: Unified Instruction-aware Heterogeneous Knowledge Retrievers](https://aclanthology.org/2025.naacl-long.234.pdf), [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.123.pdf), [LBC: Language-Based-Classifier for Out-Of-Variable Generalization](https://aclanthology.org/2025.naacl-long.583.pdf), [SANDWiCH: Semantical Analysis of Neighbours for Disambiguating Words in Context ad Hoc](https://aclanthology.org/2025.naacl-long.358.pdf), [PicPersona-TOD : A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.403.pdf), [SALAD: Improving Robustness and Generalization through Contrastive Learning with Structure-Aware and LLM-Driven Augmented Data](https://aclanthology.org/2025.naacl-long.634.pdf), [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf), [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.575.pdf), [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf), [Language Models are Crossword Solvers](https://aclanthology.org/2025.naacl-long.104.pdf), [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.353.pdf), [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf), [LRQ: Optimizing Post-Training Quantization for Large Language Models by Learning Low-Rank Weight-Scaling Matrices](https://aclanthology.org/2025.naacl-long.393.pdf), [Exploiting Edited Large Language Models as General Scientific Optimizers](https://aclanthology.org/2025.naacl-long.270.pdf), [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf), [A Systematic Examination of Preference Learning through the Lens of Instruction-Following](https://aclanthology.org/2025.naacl-long.552.pdf), [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.289.pdf), [Little Giants: Synthesizing High-Quality Embedding Data at Scale](https://aclanthology.org/2025.naacl-long.64.pdf), [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf), [Fine-Grained Transfer Learning for Harmful Content Detection through Label-Specific Soft Prompt Tuning](https://aclanthology.org/2025.naacl-long.551.pdf), [Kill two birds with one stone: generalized and robust AI-generated text detection via dynamic perturbations](https://aclanthology.org/2025.naacl-long.446.pdf), [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf), [Matina: A Large-Scale 73B Token Persian Text Corpus](https://aclanthology.org/2025.naacl-long.462.pdf), [Markov Chain of Thought for Efficient Mathematical Reasoning](https://aclanthology.org/2025.naacl-long.365.pdf), [Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation](https://aclanthology.org/2025.naacl-long.28.pdf), [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf), [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.336.pdf), [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.584.pdf), [Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations](https://aclanthology.org/2025.naacl-long.162.pdf), [Assessing the State of the Art in Scene Segmentation](https://aclanthology.org/2025.naacl-long.500.pdf), [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf), [FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models](https://aclanthology.org/2025.naacl-long.534.pdf), [Direct Preference Optimization of Video Large Multimodal Models from Language Model Reward](https://aclanthology.org/2025.naacl-long.30.pdf), [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.416.pdf), [TurtleBench: A Visual Programming Benchmark in Turtle Geometry](https://aclanthology.org/2025.naacl-long.607.pdf), [Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling](https://aclanthology.org/2025.naacl-long.533.pdf), [LLM4DistReconfig: A Fine-tuned Large Language Model for Power Distribution Network Reconfiguration](https://aclanthology.org/2025.naacl-long.208.pdf), [Evaluating and Improving Graph to Text Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.513.pdf), [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.70.pdf), [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.245.pdf), [Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://aclanthology.org/2025.naacl-long.83.pdf), [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf), [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.247.pdf), [The Stochastic Parrot on LLM's Shoulder: A Summative Assessment of Physical Concept Understanding](https://aclanthology.org/2025.naacl-long.569.pdf), [Mutual-pairing Data Augmentation for Fewshot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.205.pdf), [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf), [Bayelemabaga: Creating Resources for Bambara NLP](https://aclanthology.org/2025.naacl-long.602.pdf), [Efficient and Effective Prompt Tuning via Prompt Decomposition and Compressed Outer Product](https://aclanthology.org/2025.naacl-long.225.pdf), [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf), [Sparser Mixture-of-Adapters with Cross-Layer Generalization](https://aclanthology.org/2025.naacl-long.201.pdf), [PromptRefine: Enhancing Few-Shot Performance on Low-Resource Indic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.17.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://aclanthology.org/2025.naacl-long.99.pdf), [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.308.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [A Survey on Foundation Language Models for Single-cell Biology](https://aclanthology.org/2025.acl-long.26.pdf), [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf), [CompKBQA: Component-wise Task Decomposition for Knowledge Base Question Answering](https://aclanthology.org/2025.emnlp-main.16.pdf))
> The ability of a model or fusion method to maintain strong performance across different conditions, datasets, or tasks, such as clean vs. noisy speech or audio-visual settings.

**Generalizability** (15 papers: [An interpretable error correction method for enhancing code-to-code translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e01f4ef7ffeedf3317a44461d18df9d-Paper-Conference.pdf), [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf), [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf), [RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d191ba4c8923ed8fd8935b7c98658b5f-Paper-Conference.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf), [UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/34678d08b36076de986df95c5bbba92f-Paper-Conference.pdf), [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf), [Soft Prompting for Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.204.pdf), [Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLM Communication](https://aclanthology.org/2025.naacl-long.203.pdf), [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf), [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf), [Literature Meets Data: A Synergistic Approach to Hypothesis Generation](https://aclanthology.org/2025.acl-long.12.pdf), [CodeSteer: Symbolic-Augmented Language Models via Code/Text Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25x/chen25x.pdf), [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36.pdf))
> The extent to which a model maintains useful performance across diverse domains, entity types, and evaluation settings beyond the specific data it was trained on.

**Generalization ability** (12 papers: [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf), [MIntRec2.0: A Large-scale Benchmark Dataset for Multimodal Intent Recognition and Out-of-scope Detection in Conversations](https://proceedings.iclr.cc/paper_files/paper/2024/file/ca97c1a8c52889c49e16497912244c3b-Paper-Conference.pdf), [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf), [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf), [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf), [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf), [Unleashing the Power of Pre-trained Language Models for Offline Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c7793beb7f32b559df55d48370f2b8ae-Paper-Conference.pdf), [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf), [OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf), [AndroidGen: Building an Android Language Agent under Data Scarcity](https://aclanthology.org/2025.acl-long.138.pdf), [Advancing Personalized Learning with Neural Collapse for Long-Tail Challenge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25f/hu25f.pdf), [Unveiling Internal Reasoning Modes in LLMs: A Deep Dive into Latent Reasoning vs. Factual Shortcuts with Attribute Rate Ratio](https://aclanthology.org/2025.emnlp-main.111.pdf))
> The model's capacity to perform effectively on new, unseen data and tasks that differ from its training distribution.

**Generalization capability** (7 papers: [AffineQuant: Affine Transformation Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/ddfb58b61e7213dfb9e06c695475b2bd-Paper-Conference.pdf), [RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf), [Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/1e0bfe8bbaa0e70809f0a8ccd9c2ff3e-Paper-Conference.pdf), [Label Drop for Multi-Aspect Relation Modeling in Universal Information Extraction](https://aclanthology.org/2025.naacl-long.259.pdf), [Improving Medical Large Vision-Language Models with Abnormal-Aware Feedback](https://aclanthology.org/2025.acl-long.636.pdf), [Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf), [CARFT: Boosting LLM Reasoning via Contrastive Learning with Annotated Chain-of-Thought-based Reinforced Fine-Tuning](https://aclanthology.org/2025.emnlp-main.302.pdf))
> The ability of the quantized model to preserve performance across different datasets, model sizes, and evaluation settings.

**Generalization performance** (4 papers: [Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf), [Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c63ff34c163bca3055d39490f6d1aaf7-Paper-Conference.pdf), [LASER: Attention with Exponential Transformation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duvvuri25a/duvvuri25a.pdf), [Multilingual Federated Low-Rank Adaptation for Collaborative Content Anomaly Detection across Multilingual Social Media Participants](https://aclanthology.org/2025.emnlp-main.770.pdf))
> The latent tendency of a trained reflector or system to transfer effectively across different actor models or settings.

**Generality** (3 papers: [Model merging with SVD to tie the Knots](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4f8a5109c5083b5307fcd0bddae7a7-Paper-Conference.pdf), [One for All: Update Parameterized Knowledge Across Multiple Models with Once Edit](https://aclanthology.org/2025.acl-long.780.pdf), [BalancEdit: Dynamically Balancing the Generality-Locality Trade-off in Multi-modal Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25e/guo25e.pdf))
> The ability of a merged model to preserve the union of all skills from its base models and correctly classify inputs from any of the source tasks into a unified label space.

**Generalisation** (4 papers: [Procedural Knowledge in Pretraining Drives Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/482847908fd916b5b6b9e82525c773ad-Paper-Conference.pdf), [Less for More: Enhanced Feedback-aligned Mixed LLMs for Molecule Caption Generation and Fine-Grained NLI Evaluation](https://aclanthology.org/2025.acl-long.144.pdf), [X-Transfer Attacks: Towards Super Transferable Adversarial Attacks on CLIP](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25h/huang25h.pdf), [TombRaider: Entering the Vault of History to Jailbreak Large Language Models](https://aclanthology.org/2025.emnlp-main.279.pdf))
> The model's underlying strategy for applying knowledge learned from pretraining data to new, unseen problems.

**Generalisability** (1 paper: [Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions](https://aclanthology.org/2025.acl-long.843.pdf))
> The ability of a reasoning method to transfer effectively across different tasks, models, and problem domains without significant reconfiguration.

**Task-agnostic generalizability** (1 paper: [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf))
> The capacity of a model or method to maintain performance across diverse tasks without requiring task-specific fine-tuning or retraining.

**Domain-generality** (1 paper: [Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf))
> The capacity to apply a cognitive skill across diverse contexts and stimulus types, rather than relying on narrow, task-specific patterns or priors.

**Single-task generalization** (1 paper: [Come Together, But Not Right Now: A Progressive Strategy to Boost Low-Rank Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuang25c/zhuang25c.pdf))
> The ability of a model to perform well on a single, specific downstream task after parameter-efficient fine-tuning.

**Sequence generalization** (1 paper: [Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eedf422d321a20b2bd5e947c57c82e96-Paper-Conference.pdf))
> The ability to handle new sequences within seen topics after learning from many training sequences.

## Relationships

### Generalization →
- **MMLU** (measurement instrument): *measured_by*, 12 papers
  > On MMLU tasks (two rightmost plots in Fig. 4), IO even improves validation performance comparable to or better than EO, but the validation improvement does not generalize to the test set.
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
  - [On Giant's Shoulders: Effortless Weak to Strong by Dynamic Logits Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/34ec1286b2ccd4794c5ca4ad078b7150-Paper-Conference.pdf)
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
  - [NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/db6461eaf0eaeaad1d9c4a70e4818cbd-Paper-Conference.pdf)
  - [MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark](https://aclanthology.org/2025.acl-long.656.pdf)
  - [LoRA-One: One-Step Full Gradient Could Suffice for Fine-Tuning Large Language Models, Provably and Efficiently](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ax/zhang25ax.pdf)
  - [Maximizing Intermediate Checkpoint Value in LLM Pretraining with Bayesian Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bv/liu25bv.pdf)
  - [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chiang25a/chiang25a.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 8 papers
  > for evaluating model performance on out-of-distribution (OOD) preference data, we utilize datasets such as HHH-Alignment [44], MT-Bench Human Judgements [45], and RewardBench [46] (Section 4).
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
  - [BitStack: Any-Size Compression of Large Language Models in Variable Memory Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1842fcfd74f3c2c2a7693994a4a7c37-Paper-Conference.pdf)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
  - [BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ding25d/ding25d.pdf)
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)
  - [Split-Merge: Scalable and Memory-Efficient Merging of Expert LLMs](https://aclanthology.org/2025.emnlp-main.1533.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 4 papers
  > Figure 4 shows the downstream performance on HellaSwag, MMLU Var3, ARC-Challenge, and SciQ. PolyNorm outperforms SwiGLU on all tasks, with notable improvements, demonstrating superior generalization capabilities.
  - [Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/725f5e8036cc08adeba4a7c3bcbc6f2c-Paper-Conference.pdf)
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
  - [Soft Prompting for Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.204.pdf)
  - [Dynamic and Generalizable Process Reward Modeling](https://aclanthology.org/2025.acl-long.212.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 4 papers
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
  - [Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf)
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Robustness** (construct): *causes*, 4 papers
  > We attribute our outstanding robustness to the great generalization ability of our distilled thought-templates
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)
  - [ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25at/chen25at.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 3 papers
  > we access three mainstream benchmarks (MMLU [15], BBH [37], and GSM8K [8]) to evaluate generalization abilities. (Section 3.1)
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
  - [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf)
- **GPQA** (measurement instrument): *measured_by*, 3 papers
  > Additionally, we evaluate the model’s generalization performance across six out-of-domain tasks, including MT-Bench (Zheng et al., 2024), ARC-Challenge (25-shot) (Clark et al., 2018), GSM8K (8-shot) (Cobbe et al., 2021), HellaSwag (8-shot) (Zellers et al., 2019), GPQA (0-shot) (Rein et al., 2023), and MMLU (0-shot) (Hendrycks et al., 2020).
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
  - [T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25e/hou25e.pdf)
- **ALFWorld** (measurement instrument): *measured_by*, 3 papers
  > AlFWorld and ScienceWorld include unseen tasks to evaluate the agent’s generalization ability. (Section 4.1)
  - [Agent Planning with World Knowledge Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf)
  - [Efficient Reinforcement Learning with Large Language Model Priors](https://proceedings.iclr.cc/paper_files/paper/2025/file/797be96e4481c3fe5d675c1ba5352969-Paper-Conference.pdf)
  - [Divide and Conquer: Grounding LLMs as Efficient Decision-Making Agents via Offline Hierarchical Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25q/hu25q.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 3 papers
  > we access three mainstream benchmarks (MMLU [15], BBH [37], and GSM8K [8]) to evaluate generalization abilities. (Section 3.1)
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf)
- **HaluEval** (measurement instrument): *measured_by*, 3 papers
  > The results in Tab. 6 reveal that our annotation model achieves notable accuracies on both HaluEval and HalluQA... underscoring the generalization capability of ANAH-v2. (Section 4.4)
  - [ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e4cdfdd909ea4e34bfc85a12774cba0-Paper-Conference.pdf)
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 2 papers
  > In this section, we investigate whether our method is generally applicable beyond the medical domain. We use two general domain datasets, CommonsenseQA (CSQA) (Talmor et al., 2018) and OpenbookQA (OBQA) (Mihaylov et al., 2018)... (Section 4.5)
  - [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf)
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 2 papers
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
- **GrailQA** (measurement instrument): *measured_by*, 2 papers
  > We experiment on GrailQA to compare the performance on different generalization levels (preliminary in Appendix D). (Section 4.3.3)
  - [TARGA: Targeted Synthetic Data Generation for Practical Reasoning over Structured Data](https://aclanthology.org/2025.acl-long.137.pdf)
  - [Beyond Seen Data: Improving KBQA Generalization Through Schema-Guided Logical Form Generation](https://aclanthology.org/2025.emnlp-main.442.pdf)
- **GAIA** (measurement instrument): *measured_by*, 2 papers
  > Static benchmarks are broken benchmarks in the making, and making GAIA evolve year-by-year through the removal of broken questions and the addition of new ones might be an important component to better assess the generalization and robustness of AI systems. (Section 5)
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **ScienceWorld** (measurement instrument): *measured_by*, 2 papers
  > AlFWorld and ScienceWorld include unseen tasks to evaluate the agent’s generalization ability. (Section 4.1)
  - [Agent Planning with World Knowledge Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf)
  - [Divide and Conquer: Grounding LLMs as Efficient Decision-Making Agents via Offline Hierarchical Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25q/hu25q.pdf)
- **GQA** (measurement instrument): *measured_by*, 2 papers
  > The reason behind selecting GQA, InfoSeek, and A-OKVQA is to evaluate the generalization capability of our framework across datasets that do not necessitate up-to-date knowledge (Section 5.1).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
- **MMBench** (measurement instrument): *measured_by*, 2 papers
  > We empirically analyze the multimodal capacity and generalization ability of MoVA on a wide range of challenging MLLM benchmarks in Table 3. This comprehensive assessment is conducted on MME [82], MMBench [16], QBench [83], MathVista [84], MathVerse [85], and POPE [20]. (Section 4.2)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
  - [Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf)
- **POPE** (measurement instrument): *measured_by*, 2 papers
  > We empirically analyze the multimodal capacity and generalization ability of MoVA on a wide range of challenging MLLM benchmarks in Table 3. This comprehensive assessment is conducted on MME [82], MMBench [16], QBench [83], MathVista [84], MathVerse [85], and POPE [20]. (Section 4.2)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
  - [Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > “We focus on the GPT-4 evaluation since the reward model will not be accurate for the OOD data.”
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
  - [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf)
- **MBPP** (measurement instrument): *measured_by*, 2 papers
  > “We also evaluate the trained router on three out-of-distribution (OOD) tasks: (ii) MBPP [1], which is a code benchmark”
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **Functional MATH** (measurement instrument): *measured_by*, 2 papers
  > To further assess the generalization capabilities of our BoN aware fine-tuned models, we evaluate their performance on two challenging, held-out benchmarks: Functional Math (Srivastava et al., 2024) and MathOdyssey (Fang et al., 2024).
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
  - [Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf)
- **WebArena** (measurement instrument): *measured_by*, 2 papers
  > Furthermore, we evaluate LCoW’s generalization capabilities in WebArena benchmark.
  - [Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c995a913bc20ca39ce2231b8973be90a-Paper-Conference.pdf)
  - [AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2c6e459b95694a24ac69c469a4ee746-Paper-Conference.pdf)
- **miniF2F** (measurement instrument): *measured_by*, 2 papers
  > The FORMALALIGN model exhibits consistent performance across four diverse datasets, demonstrating its ability to generalize its autoformalization evaluation capabilities. Particularly noteworthy are the model's AS scores of 66.39% and 64.61% on the challenging MiniF2F-Valid and MiniF2F-Test datasets, respectively.
  - [FormalAlign: Automated Alignment Evaluation for Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fceedf8c9c0ff51f41b9fe0294ef0070-Paper-Conference.pdf)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **BEIR** (measurement instrument): *measured_by*, 2 papers
  > Our main evaluations are conducted on BEIR (Thakur et al., 2021) and MIRACL (Zhang et al., 2023), to assess the generalization of dense retrievers and multilingual retrieval capability. (Section 4.5).
  - [DRAMA: Diverse Augmentation from Large Language Models to Smaller Dense Retrievers](https://aclanthology.org/2025.acl-long.1457.pdf)
  - [Multi-view-guided Passage Reranking with Large Language Models](https://aclanthology.org/2025.emnlp-main.1459.pdf)
- **OSWorld** (measurement instrument): *measured_by*, 2 papers
  > To further evaluate the generalization capabilities of our model, we tested it on OSWorld, a unified computer environment designed for multimodal agents. (Section 4.3)
  - [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ae/xu25ae.pdf)
  - [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf)
- **OlympiadBench** (measurement instrument): *measured_by*, 2 papers
  > To assess generalizability of our models to out-of-distribution problems, we evaluate on two additional benchmarks: MMLU-Pro Math (Wang et al., 2024b) and Olympiad Bench (He et al., 2024). (Section 4.1).
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
  - [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1087.pdf)
- **MuSiQue** (measurement instrument): *measured_by*, 2 papers
  > For out-of-domain evaluation, we introduce three datasets that differ significantly in question style and information distribution: MuSiQue (Trivedi et al., 2022)... These datasets test the model’s generalization ability beyond the training domain. (Section 4.2.1)
  - [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf)
  - [StepER: Step-wise Knowledge Distillation for Enhancing Reasoning Ability in Multi-Step Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.1500.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 2 papers
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **ARC-AGI** (measurement instrument): *measured_by*, 2 papers
  > The Abstraction and Reasoning Corpus (ARC-AGI), introduced by Chollet (2019) and designed to assess core knowledge and the ability to generalize in AI, exemplifies this difficulty. (Section 1)
  - [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf)
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
- **MATH** (measurement instrument): *measured_by*, 1 paper
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **VirtualHome** (measurement instrument): *measured_by*, 1 paper
  > Table 1: Comparison of generalization performance on eight unseen tasks, with episodic returns averaged over 100 episodes. In these tasks, we replace the pancake in the original Food Preparation task with other foods like cheese, hamburger, apple pie and pizza
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 1 paper
  > In this section, we investigate whether our method is generally applicable beyond the medical domain. We use two general domain datasets, CommonsenseQA (CSQA) (Talmor et al., 2018) and OpenbookQA (OBQA) (Mihaylov et al., 2018)... (Section 4.5)
  - [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf)
- **SVAMP** (measurement instrument): *measured_by*, 1 paper
  > “the SVAMP dataset, containing 1,000 problems, is used solely for evaluation purposes to demonstrate the generalizability of our method.”
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **In-context learning** (construct): *causes*, 1 paper
  > Our theoretical results of population loss reveal that model generalization, tightly with ICL abilities, is influenced by model size, optimization iterations, pre-training data and prompt length. This further demonstrates that ICL emerges from the excellent generalization of sequences and topics (Section 4.1 and Section 4.2).
  - [Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eedf422d321a20b2bd5e947c57c82e96-Paper-Conference.pdf)
- **FLAN** (measurement instrument): *measured_by*, 1 paper
  > To demonstrate the generalizability and robustness of our method, we include FLAN (Chung et al., 2024) (a mix of multiple NLP tasks) as reference datasets .
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the transferability of our approach, we conducted out-of-domain experiments by training the model on one dataset and testing it on another. We use the 2Wiki (2W), HotpotQA (HQ), and MuSiQue (MQ) datasets. (Section 6.6)
  - [StepER: Step-wise Knowledge Distillation for Enhancing Reasoning Ability in Multi-Step Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.1500.pdf)
- **IMDb** (measurement instrument): *measured_by*, 1 paper
  > We investigate the generalization performance of a host of approximate Bayesian methods... we train a CNN-LSTM model... on the IMDB (Maas et al., 2011)...
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
- **GLUE** (measurement instrument): *measured_by*, 1 paper
  > SAFE improves the average GLUE score from 84.66 (LoRA) to 84.99 — this is because SAFE induces a regularization effect on less-important adapters improving generalization performance of the model. (Section 5.2.1)
  - [Not All Adapters Matter: Selective Adapter Freezing for Memory-Efficient Fine-Tuning of Language Models](https://aclanthology.org/2025.naacl-long.480.pdf)
- **HumanEval** (measurement instrument): *measured_by*, 1 paper
  > Among these, AIME-2024, HumanEval, HumanEval+, GPQA, and SciBench are from a totally different distributions compared to training data, serving to verify the generalization capability of MAS-GPT. (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **Minecraft** (measurement instrument): *measured_by*, 1 paper
  > Minecraft offers a unique challenge in 3D spatial reasoning and generalization within a procedurally generated world.
  - [SmartPlay : A Benchmark for LLMs as Intelligent Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/063d1fadbde557466bf5bcffe814a64e-Paper-Conference.pdf)
- **APIBench** (measurement instrument): *measured_by*, 1 paper
  > We further extend ToolLLaMA to an OOD dataset APIBench to validate its generalization ability.
  - [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://proceedings.iclr.cc/paper_files/paper/2024/file/28e50ee5b72e90b50e7196fde8ea260e-Paper-Conference.pdf)
- **CIFAR-10** (measurement instrument): *measured_by*, 1 paper
  > In this section, we evaluate the generalization of discrete prompts generated by Greedy on CIFAR-10, CIFAR-100, ImageNet as well as domain generalization datasets fMoW (Christie et al., 2018) and OfficeHome (Venkateswara et al., 2017) (Section 5)
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **CIFAR-100** (measurement instrument): *measured_by*, 1 paper
  > In this section, we evaluate the generalization of discrete prompts generated by Greedy on CIFAR-10, CIFAR-100, ImageNet as well as domain generalization datasets fMoW (Christie et al., 2018) and OfficeHome (Venkateswara et al., 2017) (Section 5)
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **ImageNet-1k** (measurement instrument): *measured_by*, 1 paper
  > In this section, we evaluate the generalization of discrete prompts generated by Greedy on CIFAR-10, CIFAR-100, ImageNet as well as domain generalization datasets fMoW (Christie et al., 2018) and OfficeHome (Venkateswara et al., 2017) (Section 5)
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **fMoW** (measurement instrument): *measured_by*, 1 paper
  > In this section, we evaluate the generalization of discrete prompts generated by Greedy on CIFAR-10, CIFAR-100, ImageNet as well as domain generalization datasets fMoW (Christie et al., 2018) and OfficeHome (Venkateswara et al., 2017) (Section 5)
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **AGIEval** (measurement instrument): *measured_by*, 1 paper
  > Additionally, to verify generalization, we perform all English tasks in AGIEval (Zhong et al., 2023) using zero-shot settings, which presents a collection of human-centric standardized exams.
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **FLORES-200** (measurement instrument): *measured_by*, 1 paper
  > “For zero-shot evaluation, we adopt Flores200 (NLLB Team, 2022) and evaluate on {Fr, De, Hindi (Hi), Turkish (Tr), Polish (Po)→Zh} and {Fr, Zh, Hi, Tr, Po→De} for En-Zh and En-De translation respectively.”
  - [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf)
- **InfoSeek** (measurement instrument): *measured_by*, 1 paper
  > The reason behind selecting GQA, InfoSeek, and A-OKVQA is to evaluate the generalization capability of our framework across datasets that do not necessitate up-to-date knowledge (Section 5.1).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **A-OKVQA** (measurement instrument): *measured_by*, 1 paper
  > The reason behind selecting GQA, InfoSeek, and A-OKVQA is to evaluate the generalization capability of our framework across datasets that do not necessitate up-to-date knowledge (Section 5.1).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **MME** (measurement instrument): *measured_by*, 1 paper
  > We empirically analyze the multimodal capacity and generalization ability of MoVA on a wide range of challenging MLLM benchmarks in Table 3. This comprehensive assessment is conducted on MME [82], MMBench [16], QBench [83], MathVista [84], MathVerse [85], and POPE [20]. (Section 4.2)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **ASDiv** (measurement instrument): *measured_by*, 1 paper
  > Additionally, we include two mathematical reasoning datasets, i.e., SVAMP [12] and ASDiv [18], to evaluate the out-of-domain generalizability of the models fine-tuned on the data generated from GSM8K and MATH datasets.
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
- **CollegeMath** (measurement instrument): *measured_by*, 1 paper
  > CollegeMath (Tang et al., 2024): This test set contains 2818 college-level mathematical problems extracted from 9 textbooks across 7 domains such as linear algebra and differential equations, testing generalization on complex mathematical reasoning in diverse domains. (Section 4.1)
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
- **TheoremQA** (measurement instrument): *measured_by*, 1 paper
  > TheoremQA (Chen et al., 2023): This benchmark contains 800 problems focused on utilizing mathematical theorems to solve challenging problems in fields such as math, physics and engineering, testing generalization on theoretical reasoning in general STEM. (Section 4.1)
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
- **Clotho** (measurement instrument): *measured_by*, 1 paper
  > Consequently, our model, having been trained solely on AudioSet’s audio excerpts and images, may encounter unfamiliar concepts in Clotho, thereby testing its capacity for generalization. (Section 4)
  - [An eye for an ear: zero-shot audio description leveraging an image captioner with audio-visual token distribution matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/4426af45e987692abf1b80108951ff8a-Paper-Conference.pdf)
- **XSum** (measurement instrument): *measured_by*, 1 paper
  > We conducted additional experiments to further evaluate the robustness and generalizability of our fine-tuning techniques. These experiments included assessments on the xSum dataset
  - [OpenDebateEvidence: A Massive-Scale Argument Mining and Summarization Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c630d28df1cff44314d5798f82e02ec-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LastFM** (measurement instrument): *measured_by*, 1 paper
  > “To validate the generalization ability of iLoRA, we conducted extensive experiments on three datasets derived from real-world recommendation scenarios: LastFM, MovieLens, and Steam”
  - [Customizing Language Models with Instance-wise LoRA for Sequential Recommendation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd476d01692c508ddf1cb43c6279a704-Paper-Conference.pdf)
- **FollowBench** (measurement instrument): *measured_by*, 1 paper
  > FollowBench is a fine-grained constraint-following benchmark with five levels of difficulty. It contains diverse and open-ended instructions requiring evaluation by strong LLMs, such as GPT-4, which can fully examine the generalization of AUTOIF to more general instructions not verifiable by simple code executions. (Section 4).
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
- **MathOdyssey** (measurement instrument): *measured_by*, 1 paper
  > To further assess the generalization capabilities of our BoN aware fine-tuned models, we evaluate their performance on two challenging, held-out benchmarks: Functional Math (Srivastava et al., 2024) and MathOdyssey (Fang et al., 2024).
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
- **Multimodal Mind2Web** (measurement instrument): *measured_by*, 1 paper
  > Second, Multimodal-Mind2Web (Deng et al., 2024; Zheng et al., 2024) extends the Mind2Web benchmark to evaluate generalization across three increasingly challenging settings: cross-task, cross-website, and cross-domain. (Section 3.1)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
- **DynaMath** (measurement instrument): *measured_by*, 1 paper
  > DYNAMATH allows us to evaluate the generalization ability of VLMs, by assessing their performance under varying input conditions of a seed question. (Abstract)
  - [DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/78b248ea6f627431bba5029d92be8a3d-Paper-Conference.pdf)
- **MathVerse** (measurement instrument): *measured_by*, 1 paper
  > To verify the generalization ability of G-LLaVA, we also conduct evaluation on the newly introduced MathVerse benchmark (Zhang et al., 2024b). (Section 5.1)
  - [G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)
- **WebVoyager** (measurement instrument): *measured_by*, 1 paper
  > To further assess AGENTOCCAM’s generalizabilty, we extend experiments to the real-world web environments, evluated with the tasks and golden answers proposed in WebVoyager (He et al., 2024). (Section 2)
  - [AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2c6e459b95694a24ac69c469a4ee746-Paper-Conference.pdf)
- **LogiQA** (measurement instrument): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **LogiQA 2.0** (measurement instrument): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > To test generalization (Section 4.4), we additionally evaluate on MATH (4-shot) (Hendrycks et al., 2021b), MBPP (3-shot) (Austin et al., 2021), NaturalQuestions (5-shot) (Kwiatkowski et al., 2019), TriviaQA (5-shot) (Joshi et al., 2017), Hellaswag (0-shot) (Zellers et al., 2019), PIQA (0-shot) (Bisk et al., 2020), and TruthfulQA (0-shot) (Lin et al., 2022).
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 1 paper
  > For the OOD evaluation, we test each approach’s generalization ability on Deepmind Math (Saxton et al., 2019), MMLU-pro (Wang et al., 2024), strategyQA (Geva et al., 2021), and DROP (Dua et al., 2019). (Section 3.1)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
- **DROP** (measurement instrument): *measured_by*, 1 paper
  > For the OOD evaluation, we test each approach’s generalization ability on Deepmind Math (Saxton et al., 2019), MMLU-pro (Wang et al., 2024), strategyQA (Geva et al., 2021), and DROP (Dua et al., 2019). (Section 3.1)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
- **SNLI** (measurement instrument): *measured_by*, 1 paper
  > We then assessed the performance of the merged LoRA on these in-domain tasks as well as on two additional out-of-domain tasks, SNLI and WNLI, to evaluate its adaptability and generalization capabilities.
  - [Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b54e0146a82945f01e69c2e3309ba925-Paper-Conference.pdf)
- **WNLI** (measurement instrument): *measured_by*, 1 paper
  > We then assessed the performance of the merged LoRA on these in-domain tasks as well as on two additional out-of-domain tasks, SNLI and WNLI, to evaluate its adaptability and generalization capabilities.
  - [Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b54e0146a82945f01e69c2e3309ba925-Paper-Conference.pdf)
- **Formal theorem proving** (behavioral indicator): *causes*, 1 paper
  > “This emphasizes LeanAgent’s continuous generalizability and improvement, explaining its superior theorem-proving performance.”
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 1 paper
  > LLaVA-Bench, a generalized dataset, ... is used to further evaluate the model’s generalization and robustness. (Section 4.1)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **CoLA** (measurement instrument): *measured_by*, 1 paper
  > In Table 3, we observe that ELICIT significantly improves model performance on unseen tasks (GLUE-COLA, BBQ Religion, Deepmind (Saxton et al., 2019), MMLU-Psychology, and BBH-Logical-Deduction-Five-objects) not present in its capability library. (Section 4.4).
  - [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf)
- **Caltech101** (measurement instrument): *measured_by*, 1 paper
  > We select four visual classification datasets to investigate the task of balancing personalization, generalization and privacy: Caltech101 (Fei-Fei et al., 2004) (Section 4.1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **ContextHub** (measurement instrument): *measured_by*, 1 paper
  > TypedThinker generalizes well to the unseen domain. We use a new propositional logic benchmark Contexthub (Hua et al., 2024) for evaluation. (Section 4.5)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **API-Bank** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the generality of MTU-LLaMA, we measure its performance on the OOD test split of MTU-Bench and two other OOD tool-use benchmarks, i.e., API-Bank (Li et al., 2023) and ToolTalk (Farn & Shin, 2023). (Section 3.2)
  - [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf)
- **HarmBench** (measurement instrument): *measured_by*, 1 paper
  > we incorporate a subset of Harmbench dataset from JBB-Behaviors (Chao et al., 2024) to evaluate the generalization capability of the trained prompter. (Section 4)
  - [ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf)
- **Instruction understanding** (construct): *correlates*, 1 paper
  > This is due to the limited capacity of smaller LLMs to understand complex instructions, showing lower generalizability.
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
- **PartNet-Mobility** (measurement instrument): *measured_by*, 1 paper
  > "we validate the performance of Real2Code on the well-established PartNet-Mobility dataset (Mo et al., 2019), using an extensive test set of unseen objects"
  - [Real2Code: Reconstruct Articulated Objects via Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/028fcbcf85435d39a40c4d61b42c99a4-Paper-Conference.pdf)
- **ATIS** (measurement instrument): *measured_by*, 1 paper
  > ATIS has fine-grained intents, and some classes have a low training and test set size (refer to table 4). This imbalance enables us to evaluate the generalizability and reasoning of the deep learning models when dealing with data scarcity.
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **AndroidControl** (measurement instrument): *measured_by*, 1 paper
  > Out of the 833 apps covered by AndroidControl, only 20 have been directly encountered during data synthesis, making this evaluation a test of OS-Genesis ’s out-of-distribution (OOD) performance. (Section 4.3)
  - [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://aclanthology.org/2025.acl-long.277.pdf)
- **LEMON** (measurement instrument): *measured_by*, 1 paper
  > the Lemon dataset serves as a cross-domain dataset for evaluating the generalization capabilities. (Section 5.3)
  - [A Training-free LLM-based Approach to General Chinese Character Error Correction](https://aclanthology.org/2025.acl-long.678.pdf)
- **AIME 2024** (measurement instrument): *measured_by*, 1 paper
  > Among these, AIME-2024, HumanEval, HumanEval+, GPQA, and SciBench are from a totally different distributions compared to training data, serving to verify the generalization capability of MAS-GPT. (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **MMLU-Pro Math** (measurement instrument): *measured_by*, 1 paper
  > To assess generalizability of our models to out-of-distribution problems, we evaluate on two additional benchmarks: MMLU-Pro Math (Wang et al., 2024b) and Olympiad Bench (He et al., 2024). (Section 4.1).
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
- **CMMLU** (measurement instrument): *measured_by*, 1 paper
  > To rigorously assess the generalization capabilities of merged checkpoints to unseen domains, we evaluated the out-of-domain (OOD) performance of various merging methods. Although merging weights were determined using the C-Eval dataset (in-domain, IND), we tested the merged models on three diverse OOD datasets: CMMLU, MMLU, and GSM8K. (Section 4.2)
  - [Maximizing Intermediate Checkpoint Value in LLM Pretraining with Bayesian Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bv/liu25bv.pdf)
- **ConceptARC** (measurement instrument): *measured_by*, 1 paper
  > To make sure we do not overfit on the original ARC data, we further evaluate our method on ConceptARC (Moskvichev et al., 2023) - an ARC-like dataset containing tasks sorted into specific conceptual categories. (Section 5.5)
  - [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf)
- **FreshQA** (measurement instrument): *measured_by*, 1 paper
  > In Table 2, we assess its modularity and generalization by introducing two recent and challenging OOD datasets: FreshQA (FQA) (Vu et al., 2024) and MultiHop-RAG (M-RAG) (Tang & Yang, 2024). (Section 6.3).
  - [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf)
- **MultiHop-RAG** (measurement instrument): *measured_by*, 1 paper
  > In Table 2, we assess its modularity and generalization by introducing two recent and challenging OOD datasets: FreshQA (FQA) (Vu et al., 2024) and MultiHop-RAG (M-RAG) (Tang & Yang, 2024). (Section 6.3).
  - [C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25an/chen25an.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 1 paper
  > To understand the effect of α on model generalization, we measure the AE2 performance of various models with changing α. (Section 4.2. Results)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
- **OK-VQA** (measurement instrument): *measured_by*, 1 paper
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
- **TextVQA** (measurement instrument): *measured_by*, 1 paper
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
- **OCR-VQA** (measurement instrument): *measured_by*, 1 paper
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
- **PKU-SafeRLHF** (measurement instrument): *measured_by*, 1 paper
  > In this section, we will evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU), Reward3, UltraFeedback(UltraF), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
- **UltraFeedback** (measurement instrument): *measured_by*, 1 paper
  > In this section, we will evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU), Reward3, UltraFeedback(UltraF), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
- **FineWeb** (measurement instrument): *measured_by*, 1 paper
  > In this section, we will evaluate our model, previously trained on the C4 dataset, on various other datasets, including Anthropic HH-RLHF (HH), Synthetic instruction2(Instruct), PKU SafeRLHF (PKU), Reward3, UltraFeedback(UltraF), FineWeb (Penedo et al., 2024) and Pile uncopyrighted(Pile)4 datasets. (Section 4.4)
  - [Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf)
- **MineDojo** (measurement instrument): *measured_by*, 1 paper
  > We validate our method in both MineDojo (Fan et al., 2022) and Mineflayer (PrismarineJS., 2013) environments. The experimental results suggest that our method completes diverse challenging tasks with a single model, indicating its promising generalization. (Section 1)
  - [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dj/li25dj.pdf)
- **TopiOCQA** (measurement instrument): *measured_by*, 1 paper
  > For the evaluation of generalization ability, we trained models on the TopiOCQA training set and evaluated them on the QReCC test set, and vice versa.
  - [ConvSearch-R1: Enhancing Query Reformulation for Conversational Search with Reasoning via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1349.pdf)
- **Bamboogle** (measurement instrument): *measured_by*, 1 paper
  > For out-of-domain evaluation, we introduce three datasets that differ significantly in question style and information distribution: MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2022)... These datasets test the model’s generalization ability beyond the training domain. (Section 4.2.1)
  - [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf)
- **GPQA-Diamond** (measurement instrument): *measured_by*, 1 paper
  > we use GSM8K and MATH500, along with an additional dataset to assess how well our transferring-then-finetuning approach generalizes to the unseen task GPQADiamond (Rein et al., 2024). (Section 5.1).
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
- **MME-RealWorld** (measurement instrument): *measured_by*, 1 paper
  > After creating an Error-book based on MME-RealWorld-Lite (Reasoning) subset, we applied it directly to the remaining MME-RealWorld Reasoning subset, excluding the Lite portion to rigorously test generalization (Section 4.1).
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.711.pdf)
- **MTEB** (measurement instrument): *measured_by*, 1 paper
  > To validate the effectiveness and generalization ability of our proposed method, we followed the data selection strategy of e5-mistral-7b-instruct (Wang et al., 2023) and used only a small portion of the MTEB training dataset for zero-shot training. (Section 4.3)
  - [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf)
- **DynamicNER** (measurement instrument): *measured_by*, 1 paper
  > To address these limitations, we propose DynamicNER, the first NER dataset designed for LLM-based methods with dynamic categorization, introducing various entity types and entity type lists for the same entity in different context, leveraging the generalization of LLM-based NER better.
  - [DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.835.pdf)
- **NLGraph** (measurement instrument): *measured_by*, 1 paper
  > The simpler tasks in NLGraph evaluate the generalization and robustness of MA-GTS. (Section 5.1)
  - [MA-GTS: A Multi-Agent Framework for Solving Complex Graph Problems in Real-World Applications](https://aclanthology.org/2025.emnlp-main.973.pdf)
- **MGSM** (measurement instrument): *measured_by*, 1 paper
  > we include (6) MGSM (Shi et al., 2022), a structured math reasoning task where predefined logic may suffice, to evaluate generalization to template-compatible domains. (Section 5.1)
  - [SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence](https://aclanthology.org/2025.emnlp-main.93.pdf)
- **MMMU** (measurement instrument): *measured_by*, 1 paper
  > MODRWKV attains the highest reported score among peers on the MMMU benchmark, highlighting its generalization ability in challenging multi-modal understanding scenarios (Section 4.2).
  - [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf)
- **2WikiMultiHopQA** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the transferability of our approach, we conducted out-of-domain experiments by training the model on one dataset and testing it on another. We use the 2Wiki (2W), HotpotQA (HQ), and MuSiQue (MQ) datasets. (Section 6.6)
  - [StepER: Step-wise Knowledge Distillation for Enhancing Reasoning Ability in Multi-Step Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.1500.pdf)
- **MovieLens** (measurement instrument): *measured_by*, 1 paper
  > “To validate the generalization ability of iLoRA, we conducted extensive experiments on three datasets derived from real-world recommendation scenarios: LastFM, MovieLens, and Steam”
  - [Customizing Language Models with Instance-wise LoRA for Sequential Recommendation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd476d01692c508ddf1cb43c6279a704-Paper-Conference.pdf)

### → Generalization
- **In-context learning** (construct): *causes*, 16 papers
  > In-context learning is a key paradigm in large language models (LLMs) that enables them to generalize to new tasks and domains by simply prompting these models with a few exemplars without explicit parameter updates. (Abstract)
  - [Probing the Decision Boundaries of In-context Learning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb5dd4476448c44e55a759a985b3bbec-Paper-Conference.pdf)
  - [The Closeness of In-Context Learning and Weight Shifting for Softmax Regression](https://proceedings.neurips.cc/paper_files/paper/2024/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf)
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/file/a291dad965af9bc2e39ffeb2ca1c6dc0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Towards Understanding How Transformers Learn In-context Through a Representation Learning Lens](https://proceedings.neurips.cc/paper_files/paper/2024/file/01a8d63f9cb6dcbaa3092ccddd2075ac-Paper-Conference.pdf)
  - [Transformers are Minimax Optimal Nonparametric In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/c11daad0a48ea5f3c5c6390c7b060720-Paper-Conference.pdf)
  - [Fine-grained Analysis of In-context Linear Estimation: Data, Architecture, and Beyond](https://proceedings.neurips.cc/paper_files/paper/2024/file/f9dc462382fef56d58279e75de2438f3-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
  - [LICO: Large Language Models for In-Context Molecular Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/84b16af3773fc5825ddb64996190289a-Paper-Conference.pdf)
  - [Differential learning kinetics govern the transition from memorization to generalization during in-context learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/187f9ba4cd5a59477305ac712282a1cd-Paper-Conference.pdf)
  - [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf)
  - [Faster In-Context Learning for LLMs via N-Gram Trie Speculative Decoding](https://aclanthology.org/2025.emnlp-main.911.pdf)
  - [ALLabel: Three-stage Active Learning for LLM-based Entity Recognition using Demonstration Retrieval](https://aclanthology.org/2025.emnlp-main.1278.pdf)
- **Memorization** (construct): *causes*, 12 papers
  > This raises concerns about whether LLMs are merely memorizing and overfitting these benchmarks instead of learning how to solve the tasks [112], which may lead to poor generalization[67, 13, 9]. (Section 1)
  - [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](https://proceedings.neurips.cc/paper_files/paper/2024/file/f5198bc255e1d5f959edd6d1d1a86fab-Paper-Conference.pdf)
  - [Position: General Intelligence Requires Reward-based Pretraining](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25n/han25n.pdf)
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
  - [Memorization Sinks: Isolating Memorization during LLM Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosal25a/ghosal25a.pdf)
  - [DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf)
  - [Attributing Culture-Conditioned Generations to Pretraining Corpora](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4546b4f9e1a44ed15c253dd43307dd5-Paper-Conference.pdf)
  - [Decision Tree Induction Through LLMs via Semantically-Aware Evolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/08857467641ad82f635023d530605b4c-Paper-Conference.pdf)
  - [Mitigating Memorization in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e50ff94d174465348f15c45760f58f9f-Paper-Conference.pdf)
  - [A Percolation Model of Emergence: Analyzing Transformers Trained on a Formal Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/5cd2b0a6b7423af6369cbdbbb228e8d0-Paper-Conference.pdf)
  - [Less for More: Enhanced Feedback-aligned Mixed LLMs for Molecule Caption Generation and Fine-Grained NLI Evaluation](https://aclanthology.org/2025.acl-long.144.pdf)
  - [Controllable Memorization in LLMs via Weight Pruning](https://aclanthology.org/2025.emnlp-main.765.pdf)
  - [Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision](https://aclanthology.org/2025.emnlp-main.1624.pdf)
- **Overfitting** (construct): *causes*, 8 papers
  > helping to mitigate overfitting, resulting in models that are more robust and generalise better to new data
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
  - [FouRA: Fourier Low-Rank Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/83960718b4d12f799985206f1b1cf00f-Paper-Conference.pdf)
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
  - [In-Context Learning and Occam’s Razor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/elmoznino25b/elmoznino25b.pdf)
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
  - [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf)
- **Reasoning** (construct): *causes*, 7 papers
  > Few-shot reasoning allows LLMs to generalize their understanding to new tasks by leveraging a small set of similar examples. (Sec. 3.3)
  - [Verified Code Transpilation with LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/48bb60a0c0aebb4142bf314bd1a5c6a0-Paper-Conference.pdf)
  - [Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf)
  - [MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d6c53fe062716387ff0df73cc53de60c-Paper-Conference.pdf)
  - [Can We Trust Embodied Agents? Exploring Backdoor Attacks against Embodied LLM-Based Decision-Making Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7af02c8a8e26608199c087f50a21d37-Paper-Conference.pdf)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
  - [Few-Shot Open-Set Classification via Reasoning-Aware Decomposition](https://aclanthology.org/2025.emnlp-main.699.pdf)
- **Catastrophic forgetting** (behavioral indicator): *causes*, 5 papers
  > This in turn damages the ability of the model to generalize to downstream prompts in the target language as measured by perplexity (Section 1)
  - [Emergent Abilities of Large Language Models under Continued Pre-training for Language Adaptation](https://aclanthology.org/2025.acl-long.1547.pdf)
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
  - [Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf)
  - [S$^{2}$FT: Efficient, Scalable and Generalizable LLM Fine-tuning by Structured Sparsity](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e3b9fb0c0c56cf6e1ee61e6a068fca4-Paper-Conference.pdf)
  - [Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf)
- **Knowledge transfer** (construct): *causes*, 3 papers
  > This transfer is crucial as it allows the model to leverage previously acquired knowledge to better generalize to new tasks or domains. (Section 1)
  - [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf)
  - [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf)
  - [Have We Designed Generalizable Structural Knowledge Promptings? Systematic Evaluation and Rethinking](https://aclanthology.org/2025.acl-long.110.pdf)
- **Inductive reasoning** (construct): *causes*, 2 papers
  > The inductive reasoning process enhances generalizability by formulating general problem-solving strategies (Introduction).
  - [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
  - [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf)
- **Code editing** (behavioral indicator): *causes*, 2 papers
  > Reasoning over the differences between the two states admits a more local task (as evidenced by our data efficient learning), and this property can aid in generalization. (Appendix B.1)
  - [Learning to Edit Visual Programs with Self-Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/c585301e1c4b7c50039de5413ef585b5-Paper-Conference.pdf)
  - [EditLord: Learning Code Transformation Rules for Code Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25al/li25al.pdf)
- **Model collapse** (construct): *causes*, 2 papers
  > Consequently, the model’s ability to generalize to real-world data is compromised, as it increasingly relies on the distorted distribution provided by prior AI generations rather than learning accurate representations of the real world. (Section 1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **Self-improvement** (construct): *causes*, 2 papers
  > efﬁcient exploration to discover better strategies and solutions autonomously, i.e., self-improving, which can allow agents to generalize across the various tasks in the digital world.
  - [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Inductive bias** (construct): *causes*, 2 papers
  > This suggests a desirable inductive bias of RAPTR that improves its generalization abilities beyond perplexity. (Section 4)
  - [Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf)
  - [LLMs on the Line: Data Determines Loss-to-Loss Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mayilvahanan25a/mayilvahanan25a.pdf)
- **Expert specialization** (construct): *causes*, 2 papers
  > "improving expert specialization to enhance performance and generalization remains a challenge for MoE"
  - [Mixture-of-Clustered-Experts: Advancing Expert Specialization and Generalization in Instruction Tuning](https://aclanthology.org/2025.emnlp-main.718.pdf)
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **Spatial reasoning** (construct): *causes*, 1 paper
  > state-of-the-art VLMs have exhibited strong spatial reasoning and temporal understanding capabilities across various vision tasks (Nag et al., 2022; Chen et al., 2024; Hong et al., 2023; Gao et al., 2024), allowing them to generalize to novel scenarios. (Section 1)
  - [Vision Language Models are In-Context Value Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/54854cf15a24fff9f5134a8641136fe4-Paper-Conference.pdf)
- **Shortcut learning** (construct): *causes*, 1 paper
  > Statistical evidence that shortcut learning undermines generalization in argument mining. (Section 1)
  - [Limited Generalizability in Argument Mining: State-Of-The-Art Models Learn Datasets, Not Arguments](https://aclanthology.org/2025.acl-long.1164.pdf)
- **Consistency** (construct): *causes*, 1 paper
  > “Besides small finetuning loss on sufficiently many data, a large diversity parameter ν and a small consistency parameter κ will result in a small target error bound.”
  - [Towards Few-Shot Adaptation of Foundation Models via Multitask Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d9a0718883f4a2eecee3c69c7213b05-Paper-Conference.pdf)
- **Commonsense reasoning** (construct): *causes*, 1 paper
  > Theoretically, owing to the commonsense reasoning faculties of MLLMs, our model can be generalized to discover any attributes and interrelations across various real-world objects and scenes.
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **Knowledge retention** (construct): *causes*, 1 paper
  > aligning the fine-tuned model with the pre-trained one is crucial, as it ensures retention of knowledge obtained from large-scale data, preserving generalization (Section 3.3).
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
- **Commonsense knowledge** (construct): *causes*, 1 paper
  > Overall, we show that leveraging detailed keypoint descriptions through comprehensive text, combined with commonsense knowledge from LLMs, effectively enhances generalizable performance in keypoint localization. (Section 4.4)
  - [KptLLM: Unveiling the Power of Large Language Model for Keypoint Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe692980c5d9732cf153ce27947653a7-Paper-Conference.pdf)
- **Disentanglement** (construct): *causes*, 1 paper
  > “DRL is a major goal of artificial intelligence (AI), acclaimed for its enhancement of model robustness, interpretability, and generalizability.”
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **Meta-learning** (construct): *causes*, 1 paper
  > Using Metalic’s unique combination of in-context meta-learning followed by fine-tuning, we enable the generalization of extensive fine-tuning, while also precluding expensive computation. (Section 3.2)
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)
- **Scientific knowledge** (construct): *causes*, 1 paper
  > This alignment demonstrates the better generalizability of equations discovered by LLM-SR to unseen data, likely due to the integration of scientific prior knowledge in the equation discovery process.
  - [LLM-SR: Scientific Equation Discovery via Programming with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/28df8e730c054c5331855fd4d5403ba9-Paper-Conference.pdf)
- **Abstraction** (construct): *causes*, 1 paper
  > The ability to abstract, which is often seen as a human-specific trait, enables reasoning, generalization, and problem-solving in novel contexts
  - [Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf)
- **Recursive stability** (construct): *causes*, 1 paper
  > Moreover, we demonstrate that the generalization error converges under the following conditions: (1) the generative model satisfies recursive stability, and (2) the proportion of real data is maintained at a non-negligible constant level, thus preventing model collapse.
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **World knowledge** (construct): *causes*, 1 paper
  > LLMs are pre-trained on massive datasets, allowing them to accumulate broad world knowledge that enhances their ability to generalize across a wide range of downstream tasks. (Section 2.2)
  - [FakeShield: Explainable Image Forgery Detection and Localization via Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d4e0ab9d8ff180bf5b95c258842d16e-Paper-Conference.pdf)
- **Temporal understanding** (construct): *causes*, 1 paper
  > state-of-the-art VLMs have exhibited strong spatial reasoning and temporal understanding capabilities across various vision tasks (Nag et al., 2022; Chen et al., 2024; Hong et al., 2023; Gao et al., 2024), allowing them to generalize to novel scenarios. (Section 1)
  - [Vision Language Models are In-Context Value Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/54854cf15a24fff9f5134a8641136fe4-Paper-Conference.pdf)
- **Privacy preservation** (construct): *causes*, 1 paper
  > stringent privacy measures, such as differential privacy, can hinder both personalization and generalization (Abstract).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Abstract meta-knowledge** (construct): *causes*, 1 paper
  > "fails to capture the high-level abstract meta-knowledge necessary for generalization across similar problems"
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **Permutation invariance** (construct): *causes*, 1 paper
  > This improvement is primarily attributed to its ability to exploit permutation invariance of code, thereby enhancing the model’s generalization capabilities. (Section 5.2)
  - [Beyond Sequences: Two-dimensional Representation and Dependency Encoding for Code Generation](https://aclanthology.org/2025.acl-long.308.pdf)
- **Compositional generalization** (construct): *causes*, 1 paper
  > identified CG as one of the main drivers of the generalization observed in multi-task training. (Abstract)
  - [Exploring Compositional Generalization of Multimodal LLMs for Medical Imaging](https://aclanthology.org/2025.acl-long.639.pdf)
- **Long chain-of-thought generation** (behavioral indicator): *causes*, 1 paper
  > SFT initialization matters: high-quality, emergent long CoT pattern leads to significantly better generalization and RL gains. (Takeaway 3.3)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Teacher hacking** (construct): *causes*, 1 paper
  > The ultimate outcome of both phenomena is similar: the model fails to generalize to the ground truth, but the reasons differ.
  - [On Teacher Hacking in Language Model Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tiapkin25a/tiapkin25a.pdf)
- **Reward overoptimization** (construct): *causes*, 1 paper
  > high likelihood of preferred responses and big gaps between the likelihood of preferred and dispreferred responses can lead to reward over-optimization - resulting in a better margin but worse generalization. (Section 3.1. Likelihood displacement)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
- **Neural collapse** (construct): *causes*, 1 paper
  > A higher degree of neural collapse (lower ∆TCD) leads to stronger generalizability in text classification tasks. (Section 4.1)
  - [Advancing Personalized Learning with Neural Collapse for Long-Tail Challenge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25f/hu25f.pdf)
- **Pattern matching** (construct): *causes*, 1 paper
  > This illustrates how passive pretraining fails to incentivize the learning of generalizable reasoning skills and, instead, reinforces memorization and pattern matching that have limited generalization beyond the training scenarios. (Section 1)
  - [Position: General Intelligence Requires Reward-based Pretraining](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25n/han25n.pdf)
- **Flatness** (construct): *correlates*, 1 paper
  > We attend to recent studies that have demonstrated that the generalization performance of a model is closely linked to the flatness of the solution landscape (Keskar et al., 2017; Jiang et al., 2020a). (1. Introduction)
  - [SAFE: Finding Sparse and Flat Minima to Improve Pruning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25s/lee25s.pdf)

### Associated with
- **Specialization** (construct), 2 papers
  > These pre-trained TSFMs focus on generalization with a wide domain of time series, where their specialized abilities in medical time series may not be satisfactory. Therefore, we propose a lightweight TSFM personalization scheme to tackle the specialization ability. (Section 2.1).
  - [Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf)
  - [Split-Merge: Scalable and Memory-Efficient Merging of Expert LLMs](https://aclanthology.org/2025.emnlp-main.1533.pdf)
- **Few-shot task performance** (behavioral indicator), 2 papers
  > Humans exhibit remarkable few-shot learning capabilities, rapidly generalizing from a single task demonstration to related conditions by integrating the observed behavior with their internal world model.
  - [VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ac50fd0a4eeeb1f077b17bb7c5353c3-Paper-Conference.pdf)
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
- **Personalization** (construct), 2 papers
  > FedPGP (Cui et al., 2024): Incorporate a low-rank adaptation term with an additional contrastive loss to balance generalization and personalization.
  - [Federated Disentangled Tuning with Textual Prior Decoupling and Visual Dynamic Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25k/yang25k.pdf)
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Adaptability** (construct), 1 paper
  > Overall, our system integrated with MAS-GPT offers the following key advantages: simplicity, cost-efficiency, and adaptability (generality). (Section 3.3)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **Reversal curse** (construct), 1 paper
  > If a model is trained on a sentence of the form “A is B”, it will not automatically generalize to the reverse direction “B is A”. This is the Reversal Curse.
  - [The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”](https://proceedings.iclr.cc/paper_files/paper/2024/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf)
- **Reliability** (construct), 1 paper
  > we find that it seems to be an impossible triangle—reliability, generalization, and locality can not be realized at the same time in the continual editing settings. (Section 1)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Text generation quality** (construct), 1 paper
  > the generation quality of GPT4 decreases as the logical constraints become more complex, while the generation quality of Ctrl-G stays relatively consistent across all settings, demonstrating strong generalization performance. (Sec 5.2)
  - [Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator), 1 paper
  > This lack of proper evaluation can then materialize in persistent issues of deployed systems related to generalization, e.g., hallucination [30], out-of-distribution generalization [39], fairness [6], and generalization to the long-tail [23, 24]. (Section 1).
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Fairness** (construct), 1 paper
  > This lack of proper evaluation can then materialize in persistent issues of deployed systems related to generalization, e.g., hallucination [30], out-of-distribution generalization [39], fairness [6], and generalization to the long-tail [23, 24]. (Section 1).
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Image restoration** (behavioral indicator), 1 paper
  > Image Restoration (IR)... Recently, researchers have increasingly focused on enhancing the generalization ability to diverse degradations in real-world applications
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Factuality** (construct), 1 paper
  > The experimental results in previous sections indicate that after factuality alignment with questions from a group of topics, the LLM will become more factually correct when answering questions from another group of topics (Section 4.2).
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > This trend suggests that lower learning rates enhance the model’s ability to generalize to unseen tasks requiring knowledge, complex reasoning, and instruction following.
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **Specificity** (construct), 1 paper
  > Generalization and specificity are tied together by an inherent trade-off: abstaining from everything achieves perfect generalization but no specificity, and not abstaining at all results in perfect specificity rates but no generalization. (Section 5.1)
  - [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.353.pdf)
- **Abstention** (behavioral indicator), 1 paper
  > generalizability: whether abstention extends to concept’s descendants (Section 1)
  - [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.353.pdf)
- **Universality** (construct), 1 paper
  > This paper aims to evaluate and rethink the generalization capability of the SKP paradigm from four perspectives including Granularity, Transferability, Scalability, and Universality. (Abstract)
  - [Have We Designed Generalizable Structural Knowledge Promptings? Systematic Evaluation and Rethinking](https://aclanthology.org/2025.acl-long.110.pdf)
- **Text-to-SQL** (behavioral indicator), 1 paper
  > In the zero-shot setting, the key challenge is to construct a mapping function f without task-specific labeled data. This requires the model to generalize across unseen SQL queries and databases, relying solely on pre-trained knowledge and the provided database schema. (Section 3.1)
  - [Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dt/li25dt.pdf)
- **Image editing** (behavioral indicator), 1 paper
  > To further demonstrate the generalization and applicability of ELM, we evaluate its ability to generate samples from novel classes and perform image editing tasks, with the results in Appendix A.2. (Section 4.4)
  - [Elucidating the design space of language models for image generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25w/liu25w.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > Two core challenges distinguish open-ended generation from closed-end tasks: (1) Limited generalization across prompt variations... (Introduction)
  - [SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.112.pdf)
- **Image classification** (behavioral indicator), 1 paper
  > Moreover, we extend our experiments to image classification tasks, aiming to evaluate the model's generalizability across diverse domains.
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
- **Harmful content detection** (behavioral indicator), 1 paper
  > The increasing proliferation of harmful content and its evolving nature require effective and generalizable detection methods. (Section 1)
  - [Fine-Grained Transfer Learning for Harmful Content Detection through Label-Specific Soft Prompt Tuning](https://aclanthology.org/2025.naacl-long.551.pdf)
- **Image captioning** (behavioral indicator), 1 paper
  > Meanwhile, image captioning is conducted on the unseen BLIP-2 (OPT-2.7b) (Li et al., 2023), to demonstrate the generalization capacity. (Section 4.1)
  - [Privacy-Shielded Image Compression: Defending Against Exploitation from Vision-Language Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25k/shen25k.pdf)
- **Grokking** (construct), 1 paper
  > “under certain conditions, overparameterized neural networks suddenly transition from pure memorization to near-perfect generalization”
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
