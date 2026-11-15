# Interpretability and explainability
**Type:** Construct  
**Supporting papers:** 282  
**Also known as:** Explainability, Interpretability, Weight-based interpretability, Intrinsic interpretability, Feature interpretability, Model interpretability, Mechanistic interpretability, Human auditability, Transparency and interpretability, Algorithmic understanding, Transparency  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this as a broad umbrella for making a model, feature, reasoning process, or prediction understandable to humans, either by exposing internal computations or by giving rationales for outputs. Most definitions emphasize concise human-understandable explanations of activations, internal states, decision factors, or predictions, and many quoted passages tie that understanding to traceability, such as linking tokens to training data, phrases to source documents, or decisions to concepts and intermediate steps. A smaller line of work narrows the term to interpretable sparse features or monosemantic latents, direct inspection or manipulation of model internals or even weights, and intrinsic interpretability through human-interpretable concepts rather than post-hoc explanation. The main difference across definitions is whether the property belongs to internal mechanisms, learned representations, or output-side justifications and evidence traces.

**Space of facets.** Papers often blur interpretability, explainability, and transparency, and some explicitly treat interpretability and explainability as near-equivalent. Within that umbrella, they introduce narrower labels such as feature interpretability, model interpretability, mechanistic interpretability, weight-based interpretability, intrinsic interpretability, human auditability, and algorithmic understanding. These variants sort the concept by object of analysis, latents and features, inspectable states and circuits, weights, decision rationales, or step-by-step procedures, while transparency usually refers to visible reasoning steps, decision traces, or inspectable lexical dimensions. Some papers also combine transparency and interpretability in step-level scoring of intermediate reasoning.

**Space of measurement.** Papers link this construct to 9 measurement instruments and 14 behavioral indicators. The most often linked instruments are Automated interpretability, LLM-as-a-judge, Human evaluation, SAEBench, and CUB-200-2011, plus 4 others. In practice, authors operationalize it by automatically classifying whether sparse features or latents are human-understandable, asking GPT-4 or GPT-4o to judge the interpretability of outputs or reasoning paths, collecting human ratings of random features and neurons, and using benchmarks or datasets with concept annotations, explanations, criterion-specific scores, or transparency dimensions. These operationalizations cover both internal-feature readability and output-level explanation quality, matching the split seen in the definitions.

**Links.** Most commonly, papers claim causal relationships from reasoning and chain of thought to interpretability and explainability, and similar incoming causal claims also come from several other behaviors and constructs. In the opposite direction, several papers claim a causal relationship from interpretability and explainability to trustworthiness and controllability, with narrower extensions to other outcomes. Related links connect it to medical and evaluation-oriented constructs, and one paper reports that it correlates with chess move prediction.

## Sources

**Interpretability** (25 papers: [An interpretable error correction method for enhancing code-to-code translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e01f4ef7ffeedf3317a44461d18df9d-Paper-Conference.pdf), [Bootstrapping Variational Information Pursuit with Large Language and Vision Models for Interpretable Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/8e12ba543adc673da5b89c9311fcf72c-Paper-Conference.pdf), [Compositional Preference Models for Aligning LMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/8fd10360ac9de462ffd36155d87ee999-Paper-Conference.pdf), [Conversational Drug Editing Using Retrieval and Domain Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/d390199c28b467315b454789b6584f19-Paper-Conference.pdf), [Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making](https://proceedings.iclr.cc/paper_files/paper/2024/file/fbf1b3765e081251c804da7f508f3b21-Paper-Conference.pdf), [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf), [Generative Judge for Evaluating Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/747dc7c6566c74eb9a663bcd8d057c78-Paper-Conference.pdf), [Grounding Language Plans in Demonstrations Through Counterfactual Perturbations](https://proceedings.iclr.cc/paper_files/paper/2024/file/be62c4a943675195ff5a2a98d5b9724f-Paper-Conference.pdf), [LILO: Learning Interpretable Libraries by Compressing and Documenting Code](https://proceedings.iclr.cc/paper_files/paper/2024/file/819cebb05f993840e8a52d7564c5c282-Paper-Conference.pdf), [Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks](https://proceedings.iclr.cc/paper_files/paper/2024/file/72679d76c80e079c70fe5977d21ed1e4-Paper-Conference.pdf), [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf), [Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf), [TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting](https://proceedings.iclr.cc/paper_files/paper/2024/file/5132940b1bced8a7b28e9695d49d435a-Paper-Conference.pdf), [Text2Reward: Reward Shaping with Language Models for Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/9941833e8327910ef25daeb9005e4748-Paper-Conference.pdf), [Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf), [Vision-by-Language for Training-Free Compositional Image Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/48fd58527b29c5c0ef2cae43065636e6-Paper-Conference.pdf), [Reversed Attention: On The Gradient Descent Of Attention Layers In GPT](https://aclanthology.org/2025.naacl-long.52.pdf), [Latent Factor Models Meets Instructions: Goal-conditioned Latent Factor Discovery without Task Supervision](https://aclanthology.org/2025.naacl-long.554.pdf), [Analyzing (In)Abilities of SAEs via Formal Languages](https://aclanthology.org/2025.naacl-long.249.pdf), [Explanation based In-Context Demonstrations Retrieval for Multilingual Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.251.pdf), [Evaluating and Improving Graph to Text Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.513.pdf), [LLM-guided Plan and Retrieval: A Strategic Alignment for Interpretable User Satisfaction Estimation in Dialogue](https://aclanthology.org/2025.naacl-long.523.pdf), [UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26.pdf), [GraphNarrator: Generating Textual Explanations for Graph Neural Networks](https://aclanthology.org/2025.acl-long.2.pdf), [From Problem-Solving to Teaching Problem-Solving: Aligning LLMs with Pedagogy using Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.15.pdf))
> The degree to which a learned feature or representation can be given a concise, human-understandable explanation that predicts its activations.

**Explainability** (11 papers: [Beam Enumeration: Probabilistic Explainability For Sample Efficient Self-conditioned Molecular Design](https://proceedings.iclr.cc/paper_files/paper/2024/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf), [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf), [DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/d4ce6738e84876aa79f13c8bc8b7c5eb-Paper-Conference.pdf), [SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/428ceef2cd8a53add7213e04d1746479-Paper-Conference.pdf), [CAVE: Controllable Authorship Verification Explanations](https://aclanthology.org/2025.naacl-long.451.pdf), [Beyond End-to-End VLMs: Leveraging Intermediate Text Representations for Superior Flowchart Understanding](https://aclanthology.org/2025.naacl-long.180.pdf), [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf), [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf), [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf), [Exploring Large Language Models for Effective Rumor Detection on Social Media](https://aclanthology.org/2025.naacl-long.128.pdf), [Retrieve to Explain: Evidence-driven Predictions for Explainable Drug Target Identification](https://aclanthology.org/2025.acl-long.167.pdf))
> The extent to which the system provides a rationale that helps users understand why a prediction was made.

**Transparency** (3 papers: [Enhancing Lexicon-Based Text Embeddings with Large Language Models](https://aclanthology.org/2025.acl-long.930.pdf), [EmoDynamiX: Emotional Support Dialogue Strategy Prediction by Modelling MiXed Emotions and Discourse Dynamics](https://aclanthology.org/2025.naacl-long.81.pdf), [Has this Fact been Edited? Detecting Knowledge Edits in Language Models](https://aclanthology.org/2025.naacl-long.492.pdf))
> The degree to which the embedding dimensions correspond to human-interpretable lexical units, allowing inspection of model decisions through cluster weights.

**Weight-based interpretability** (1 paper: [Bilinear MLPs enable weight-based mechanistic interpretability](https://proceedings.iclr.cc/paper_files/paper/2025/file/7504142a20a3e1fe9dd7de42f475828c-Paper-Conference.pdf))
> The property of a model where its computational mechanisms can be understood by directly analyzing its weight parameters, rather than relying on activation patterns over a dataset.

**Intrinsic interpretability** (1 paper: [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf))
> The degree to which an LLM’s internal representations and predictions can be directly understood through human-interpretable concepts rather than post-hoc explanations.

**Model interpretability** (2 papers: [NNsight and NDIF: Democratizing Access to Open-Weight Foundation Model Internals](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6c65eb9b56719c1aa45ff73874de317-Paper-Conference.pdf), [Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf))
> The extent to which a model's internal states can be inspected, manipulated, and studied in a transparent way.

**Feature interpretability** (1 paper: [Efficient Dictionary Learning with Switch Sparse Autoencoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc4fbc2c77d2150c4e61e0fca6c2e95a-Paper-Conference.pdf))
> The degree to which the features learned by a sparse autoencoder correspond to distinct, human-understandable concepts.

**Mechanistic interpretability** (2 papers: [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf), [Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25x/he25x.pdf))
> The degree to which a model's internal computations can be dissected and understood in terms of human-interpretable components.

**Human auditability** (1 paper: [DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf))
> The property of a model's decision-making process that allows a human to understand, verify, and trust the rationale behind a given decision.

**Transparency and interpretability** (1 paper: [Free Process Rewards without Process Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25c/yuan25c.pdf))
> The quality of a reward model that allows for a clear understanding of its evaluation process by providing scores for each intermediate reasoning step.

**Algorithmic understanding** (1 paper: [Position: We Need An Algorithmic Understanding of Generative AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eberle25a/eberle25a.pdf))
> The degree to which the internal step-by-step procedures used by a model to solve tasks are known and explainable.

## Relationships

### Interpretability and explainability →
- **Trustworthiness** (construct): *causes*, 5 papers
  > one aspect that hinders their deployment is the lack of human-comprehensible understanding of their internal computations. This directly calls into question their reliability and trustworthiness (Introduction).
  - [A Concept-Based Explainability Framework for Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f4fba41b554f9aaa013c4062a1c40518-Paper-Conference.pdf)
  - [Decision Information Meets Large Language Models: The Future of Explainable Operations Research](https://proceedings.iclr.cc/paper_files/paper/2025/file/a48e5877c7bf86a513950ab23b360498-Paper-Conference.pdf)
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
  - [BIRD: A Trustworthy Bayesian Inference Framework for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/19452e14fe6e0a8ac00410f1eebcbded-Paper-Conference.pdf)
  - [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf)
- **Controllability** (construct): *causes*, 4 papers
  > By embedding interpretability directly into the LLMs, we enable greater transparency, steering, and control over their behavior.
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
  - [SafetyAnalyst: Interpretable, Transparent, and Steerable Safety Moderation for AI Behavior](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bw/li25bw.pdf)
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Automated interpretability** (measurement instrument): *measured_by*, 3 papers
  > “Bricken et al. (2023) evaluate how interpretable sparse autoencoder features using automated interpretability”
  - [Efficient Dictionary Learning with Switch Sparse Autoencoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc4fbc2c77d2150c4e61e0fca6c2e95a-Paper-Conference.pdf)
  - [SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karvonen25a/karvonen25a.pdf)
  - [Compute Optimal Inference and Provable Amortisation Gap in Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/o-neill25a/o-neill25a.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 3 papers
  > We utilize a large multimodal model (GPT-4o) as the ‘judge’ to assign entailment scores given a constructed rule. ... This observation validates the interpretability of the reasoning paths in the concept tree. (Section 4.6)
  - [COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.135.pdf)
  - [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf)
  - [WISE: Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification](https://aclanthology.org/2025.emnlp-main.741.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 2 papers
  > For Pythia SAEs, we asked human crowdworkers to rate the interpretability of random features, random neurons, features from our feature circuits, and neurons from our neuron circuits.
  - [Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ba4d47a83e498c2b1a0868cba20f6de-Paper-Conference.pdf)
  - [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf)
- **SAEBench** (measurement instrument): *measured_by*, 2 papers
  > We include interpretability benchmark results from SAEBench in Appendix A.3.4. (Section 4.1)
  - [Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/leask25a/leask25a.pdf)
  - [Train One Sparse Autoencoder Across Multiple Sparsity Budgets to Preserve Interpretability and Accuracy](https://aclanthology.org/2025.emnlp-main.515.pdf)
- **VQA-X** (measurement instrument): *measured_by*, 1 paper
  > We consider VQA-X (Park et al., 2018), a VQA dataset with human-annotated explanations for each image-question-answer triplets...
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Image editing** (behavioral indicator): *causes*, 1 paper
  > When a prompt closely aligns with the image content and is interpretable by humans, it becomes easier for users to modify the image in the desired direction by making slight edits to the prompt. (Section 4.3)
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **Safety** (construct): *causes*, 1 paper
  > The embedded interpretability empowers users to transparently identify harmful content, steer model behavior, and unlearn undesired concepts – significantly enhancing the safety, reliability, and trustworthiness of LLMs, which are critical capabilities notably absent in existing language models.
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > As a result, developing interpretability methods for MLLMs is crucial for improving alignment quality and efficiency. (Abstract)
  - [SAE-V: Interpreting Multimodal Models for Enhanced Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lou25b/lou25b.pdf)
- **G-Eval** (measurement instrument): *measured_by*, 1 paper
  > G-EVAL generates criterion-specific scores, supporting fine-grained analysis of response quality, explainability, and reasoning. (Section 4.3)
  - [PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **FINTRUST** (measurement instrument): *measured_by*, 1 paper
  > we curate 15, 680 instances to evaluate LLM trustworthiness in the financial domain. We ... incorporate seven core dimensions: Truthfulness, Safety, Fairness, Robustness, Privacy, Transparency, and Knowledge Discovery. (Section 2)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **CUB-200-2011** (measurement instrument): *measured_by*, 1 paper
  > Among these, CUB, SkinCon, and LAD offer image-level concept annotations that enable quantitative evaluation of MCoT interpretability.
  - [WISE: Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification](https://aclanthology.org/2025.emnlp-main.741.pdf)
- **e-SNLI** (measurement instrument): *measured_by*, 1 paper
  > Datasets such as e-SNLI (Camburu et al., 2018) provide human explanations, supporting explicit reasoning and interpretability benchmarks. (Section 2.1)
  - [Cross-Document Cross-Lingual NLI via RST-Enhanced Graph Fusion and Interpretability Prediction](https://aclanthology.org/2025.emnlp-main.1611.pdf)

### → Interpretability and explainability
- **Reasoning** (construct): *causes*, 6 papers
  > Mindmap [74] provides more transparency on LLMs’ decision-making by enabling comprehension and reasoning over structured KG inputs. (Section 1)
  - [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
  - [A Hitchhiker's Guide to Fine-Grained Face Forgery Detection Using Common Sense Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/059d2b9188cdb7ae00f4d78cc9469704-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
  - [REARANK: Reasoning Re-ranking Agent via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.125.pdf)
  - [MR. Judge: Multimodal Reasoner as a Judge](https://aclanthology.org/2025.emnlp-main.1021.pdf)
- **Chain of thought** (behavioral indicator): *causes*, 5 papers
  > We leverage the augmented patient context to enable LLMs to generate step-by-step reasoning chains, enhancing both interpretability and prediction accuracy in clinical tasks. (Section 1)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
  - [MolRAG: Unlocking the Power of Large Language Models for Molecular Property Prediction](https://aclanthology.org/2025.acl-long.755.pdf)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
  - [RTQA : Recursive Thinking for Complex Temporal Knowledge Graph Question Answering with Large Language Models](https://aclanthology.org/2025.emnlp-main.499.pdf)
  - [DSG-MCTS: A Dynamic Strategy-Guided Monte Carlo Tree Search for Diversified Reasoning in Large Language Models](https://aclanthology.org/2025.emnlp-main.532.pdf)
- **Explanation generation** (behavioral indicator): *causes*, 4 papers
  > ...offering interpretable answers, as LLMs can generate language-based explanations for the decisions. (Abstract)
  - [SocialGPT: Prompting LLMs for Social Relation Reasoning via Greedy Segment Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/047682108c3b053c61ad2da5a6057b4e-Paper-Conference.pdf)
  - [RSVP: Reasoning Segmentation via Visual Prompting and Multi-modal Chain-of-Thought](https://aclanthology.org/2025.acl-long.715.pdf)
  - [PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation](https://aclanthology.org/2025.emnlp-main.747.pdf)
  - [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf)
- **Structured reasoning** (construct): *causes*, 2 papers
  > To enhance the accuracy and explainability of natural language reasoning, structured reasoning has been frequently explored as an alternative. (Introduction)
  - [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning](https://aclanthology.org/2025.naacl-long.124.pdf)
  - [RePanda: Pandas-powered Tabular Verification and Reasoning](https://aclanthology.org/2025.acl-long.1549.pdf)
- **Disentanglement** (construct): *causes*, 2 papers
  > “DRL is a major goal of artificial intelligence (AI), acclaimed for its enhancement of model robustness, interpretability, and generalizability.”
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
  - [Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/53356aebeea8ffd40a8ac3bb66243162-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator): *causes*, 1 paper
  > This approach also allows us to enhance explainability by returning the retrieved subgraph. (Section 5)
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **Multi-turn dialogue** (behavioral indicator): *causes*, 1 paper
  > We also enhance explainability, both by returning the retrieved subgraph, and through the use of conversational interfaces for 'chatting with a graph'
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **Monosemanticity** (construct): *causes*, 1 paper
  > Sparse autoencoders (SAEs) have gained a lot of attention as a promising tool to improve the interpretability of large language models (LLMs) by mapping the complex superposition of polysemantic neurons into monosemantic features
  - [Rethinking Evaluation of Sparse Autoencoders through the Representation of Polysemous Words](https://proceedings.iclr.cc/paper_files/paper/2025/file/380a0b16a7e6f8c5010f798c9f2d3c61-Paper-Conference.pdf)
- **Causal discovery** (behavioral indicator): *causes*, 1 paper
  > "ADAM constructs a nearly perfect causal graph from scratch, enabling efficient task decomposition and execution with strong interpretability."
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)
- **Attribution ability** (construct): *causes*, 1 paper
  > Attribution: attribute triplet indexes in the generated text using sequential numbers to enhance the interpretability of the generated text. (Section 1)
  - [Evaluating and Improving Graph to Text Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.513.pdf)
- **Grammatical error correction** (behavioral indicator): *causes*, 1 paper
  > One advantage of example-based GEC systems is that they can enhance system interpretability by providing learners with illustrative examples (Kaneko et al., 2022). (Section 2.1)
  - [Explanation based In-Context Demonstrations Retrieval for Multilingual Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.251.pdf)
- **Chess move prediction** (behavioral indicator): *correlates*, 1 paper
  > Our experiments show that a sufficiently wide-and-sparse MLP in transformer indeed yields more interpretable neurons, leading to a 25% increase in F1 score for chess move prediction, supporting our hypothesis.
  - [Mixture of Experts Made Intrinsically Interpretable](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ag/yang25ag.pdf)
- **Backtracking** (behavioral indicator): *causes*, 1 paper
  > Although incremental improvements have been proposed, the absence of robust backtracking or rollback still limits their reliability and interpretability (Doyle, 1979; Bo et al., 2024). (Section 1)
  - [ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA](https://aclanthology.org/2025.emnlp-main.202.pdf)
- **Claim decomposition** (behavioral indicator): *causes*, 1 paper
  > Other approaches, including RAGAS (Shahul et al., 2023), RAG-Checker (Ru et al., 2024), and OpenEval (Ispas et al., 2025), introduce claim-level decomposition, enabling LLMs to assess the faithfulness and correctness of each factual statement for finer-grained and more interpretable evaluation.
  - [RAG-Zeval: Enhancing RAG Responses Evaluator through End-to-End Reasoning and Ranking-Based Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1267.pdf)

### Associated with
- **Medical reasoning** (construct), 2 papers
  > This observation suggests that both perception, or reading (e.g., finding necessary information in the medical record) and reasoning (determining the disease based on the observations) should be counted when evaluating interpretability in LLM-based medical NLP tasks. (Section 1)
  - [DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/892850bf793e03b5c410dfd9425b94c8-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MEDDxAgent: A Unified Modular Agent Framework for Explainable Automatic Differential Diagnosis](https://aclanthology.org/2025.acl-long.677.pdf)
- **Plausibility** (construct), 2 papers
  > Ideally, the explanation should be both faithful (reflecting the model’s actual behavior) and plausible (aligning with human understanding)
  - [Is the MMI Criterion Necessary for Interpretability? Degenerating Non-causal Features to Plain Noise for Self-Rationalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/d53d51e88d92d3723755f6d425bc513b-Paper-Conference.pdf)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Fact checking** (behavioral indicator), 2 papers
  > Claim verification is a long-standing and challenging task that demands not only high accuracy but also explainability of the verification process. (Abstract)
  - [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf)
  - [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf)
- **Expressive power** (construct), 1 paper
  > The trade-off between expressiveness and interpretability remains a core challenge when building human-centric models for classification and decision-making. (ABSTRACT)
  - [Large Language Models are Interpretable Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/887932131fddf943e8fe3310b62c0147-Paper-Conference.pdf)
- **Symbolic regression** (behavioral indicator), 1 paper
  > This flexibility allows SR to achieve both high accuracy and interpretability, making it especially valuable in fields such as physics (Udrescu et al., 2020), biology (Brunton et al., 2016), and finance (Liu & Guo, 2023), where uncovering transparent, understandable models is crucial for scientific discovery and informed decision-making.
  - [RAG-SR: Retrieval-Augmented Generation for Neural Symbolic Regression](https://proceedings.iclr.cc/paper_files/paper/2025/file/19a8e70828c01059631f913442ae31e6-Paper-Conference.pdf)
- **Polysemanticity** (construct), 1 paper
  > A central obstacle to mechanistic interpretability is polysemanticity, where individual neurons encode multiple, unrelated concepts (Olah et al., 2020).
  - [Mixture of Experts Made Intrinsically Interpretable](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ag/yang25ag.pdf)
- **Hallucination** (behavioral indicator), 1 paper
  > ...problematic due to the opaque nature of LLMs’ parametric knowledge, which leads to poor interpretability and frequent hallucination issues. (Section 1)
  - [MusKGC: A Flexible Multi-source Knowledge Enhancement Framework for Open-World Knowledge Graph Completion](https://aclanthology.org/2025.emnlp-main.508.pdf)
- **Usability** (construct), 1 paper
  > However, we found existing single-turn-based approaches have limitations in user-centricity, especially for novice users: Firstly, interpretability remains a challenge. (Introduction)
  - [Taming Text-to-Image Synthesis for Novices: User-centric Prompt Generation via Multi-turn Guidance](https://aclanthology.org/2025.emnlp-main.444.pdf)
- **Faithfulness** (construct), 1 paper
  > We evaluate the explainability of all the models using plausibility and faithfulness metrics (DeYoung et al., 2019). (Section 6.1)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Medical diagnosis** (behavioral indicator), 1 paper
  > By quantifying the overlap between boxes, our method provides intuitive insights into the relationships between medical concepts, thereby improving the accuracy and interpretability of model predictions. (Section 2.3.2. VOLUME-BASED DIAGNOSIS PREDICTION)
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)
