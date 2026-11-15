# Reasoning
**Type:** Construct  
**Supporting papers:** 804  
**Also known as:** Reasoning ability, Reasoning capability, Inference ability, Reasoning capacity, Inferential capabilities, Inferences, General inference capability, Reasoning capabilities, Reasoning skills, Inference capability, Inferential ability, Thinking, Reasoning performance, Comprehensive reasoning, Few-shot reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats reasoning as a latent model ability for multi-step logical inference: processing information, drawing conclusions, and solving problems, often by decomposing tasks into smaller steps or producing intermediate reasoning. Many definitions explicitly oppose this to pattern matching, memorization, or superficial cues, and anchor it in math, logic, coding, agent decision-making, or evidence aggregation from retrieval. Smaller lines broaden it to multimodal or video understanding, time-series prediction, inferring unseen buzzword meanings, or generating user-tailored reasons in explanations, and one line reframes reasoning as posterior inference over latent chains of thought rather than just stepwise deduction.

**Space of facets.** Papers do not converge on a single taxonomy, but they repeatedly slice the construct by task domain, including mathematical, commonsense, logical, visual or multimodal, and agent or planning-oriented reasoning, with a few papers also naming general, comprehensive, or few-shot reasoning. The literature also uses a broad family of near-synonymous labels, such as reasoning ability, reasoning capability, reasoning capacity, reasoning skills, reasoning performance, inference ability, and inferential ability, usually for the same broader faculty. A smaller distinction separates reasoning from adjacent mechanisms such as thinking or self-generated planning, and some papers explicitly contrast it with memorization.

**Space of measurement.** Operationalization is broad: papers link reasoning to 103 measurement instruments and 41 behavioral indicators. Measurement is dominated by benchmarks rather than probes, most often GSM8K, BIG-Bench Hard, MMLU, PIQA, and ARC-Challenge, with 98 other instruments spanning math, commonsense, agent, multimodal, retrieval, coding, reward-model, and long-context settings; a smaller line uses LLM-based judging or evaluation suites. These operationalizations usually treat reasoning as accuracy or judged quality on multi-step tasks, which mostly matches the dominant definition, though some papers operationalize it through coding, recommendation explanations, tool use, or other domain-specific outputs.

**Links.** Several papers claim a causal relationship from Chain of thought to Reasoning. Several also claim causal relationships from Reasoning to Generalization and to Interpretability and explainability, while Reasoning is related to Commonsense reasoning and is reported to correlate with Mathematical reasoning. Papers also record 40 other behavioral-indicator links and 42 other construct links.

## Sources

**Reasoning** (81 papers: [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf), [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf), [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf), [Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e1a87dbb7e954b8d9d6c91f6db771eb-Paper-Conference.pdf), [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf), [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf), [CivRealm: A Learning and Reasoning Odyssey in Civilization for Decision-Making Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/76d2f8e328e1081c22a77ca0fa330ca5-Paper-Conference.pdf), [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf), [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf), [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf), [DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf), [Evoke: Evoking Critical Thinking Abilities in LLMs via Reviewer-Author Prompt Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf), [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf), [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf), [Knowledge Fusion of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4fd5cfd2e31bebbccfa5ffa354c04bdc-Paper-Conference.pdf), [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf), [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf), [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf), [Large Language Models as Automated Aligners for benchmarking Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf), [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [MIntRec2.0: A Large-scale Benchmark Dataset for Multimodal Intent Recognition and Out-of-scope Detection in Conversations](https://proceedings.iclr.cc/paper_files/paper/2024/file/ca97c1a8c52889c49e16497912244c3b-Paper-Conference.pdf), [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf), [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf), [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf), [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf), [SmartPlay : A Benchmark for LLMs as Intelligent Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/063d1fadbde557466bf5bcffe814a64e-Paper-Conference.pdf), [SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/428ceef2cd8a53add7213e04d1746479-Paper-Conference.pdf), [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf), [Text2Reward: Reward Shaping with Language Models for Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/9941833e8327910ef25daeb9005e4748-Paper-Conference.pdf), [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf), [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf), [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf), [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf), [ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/13250eb13871b3c2c0a0667b54bad165-Paper-Conference.pdf), [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/4410c0711e9154a7a2d26f9b3816d1ef-Paper-Conference.pdf), [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf), [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf), [A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf), [Cascading Large Language Models for Salient Event Graph Generation](https://aclanthology.org/2025.naacl-long.112.pdf), [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf), [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf), [SANDWiCH: Semantical Analysis of Neighbours for Disambiguating Words in Context ad Hoc](https://aclanthology.org/2025.naacl-long.358.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf), [LLM-Based Explicit Models of Opponents for Multi-Agent Games](https://aclanthology.org/2025.naacl-long.41.pdf), [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf), [ALERT: An LLM-powered Benchmark for Automatic Evaluation of Recommendation Explanations](https://aclanthology.org/2025.naacl-long.137.pdf), [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf), [Language Models are Crossword Solvers](https://aclanthology.org/2025.naacl-long.104.pdf), [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf), [Exploiting Edited Large Language Models as General Scientific Optimizers](https://aclanthology.org/2025.naacl-long.270.pdf), [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf), [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.315.pdf), [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf), [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf), [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf), [Assessing the State of the Art in Scene Segmentation](https://aclanthology.org/2025.naacl-long.500.pdf), [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf), [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf), [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf), [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf), [KMMLU: Measuring Massive Multitask Language Understanding in Korean](https://aclanthology.org/2025.naacl-long.206.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [Fine-grained Fallacy Detection with Human Label Variation](https://aclanthology.org/2025.naacl-long.34.pdf), [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf), [MAPWise: Evaluating Vision-Language Models for Advanced Map Queries](https://aclanthology.org/2025.naacl-long.473.pdf), [MASTER: A Multi-Agent System with LLM Specialized MCTS](https://aclanthology.org/2025.naacl-long.476.pdf), [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf), [The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models](https://aclanthology.org/2025.naacl-long.303.pdf), [Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.243.pdf), [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [CoRAC: Integrating Selective API Document Retrieval with Question Semantic Intent for Code Question Answering](https://aclanthology.org/2025.naacl-long.628.pdf), [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf), [LLM The Genius Paradox: A Linguistic and Math Expert's Struggle with Simple Word-based Counting Problems](https://aclanthology.org/2025.naacl-long.172.pdf), [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf), [Intuitive Fine-Tuning: Towards Simplifying Alignment into a Single Process](https://aclanthology.org/2025.acl-long.6.pdf), [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abnar25a/abnar25a.pdf), [A Systematic Analysis of Base Model Choice for Reward Modeling](https://aclanthology.org/2025.emnlp-main.8.pdf))
> The capacity for multi-hop logical inference and deduction about object interactions, action conditions, or dependencies.

**Reasoning capability** (12 papers: [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf), [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf), [GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf), [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf), [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf), [Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1551c01d7a3d0bf21e2518331e9f7074-Paper-Conference.pdf), [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.502.pdf), [Rethinking the Role of LLMs for Document-level Relation Extraction: a Refiner with Task Distribution and Probability Fusion](https://aclanthology.org/2025.naacl-long.319.pdf), [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf), [Addressing Blind Guessing: Calibration of Selection Bias in Multiple-Choice Question Answering by Video Language Models](https://aclanthology.org/2025.acl-long.162.pdf), [CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf), [TokenSkip: Controllable Chain-of-Thought Compression in LLMs](https://aclanthology.org/2025.emnlp-main.165.pdf))
> The ability to infer task structure, constraints, and implementation details needed to generate coherent new simulation tasks.

**Reasoning ability** (15 papers: [Building Cooperative Embodied Agents Modularly with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/54b8b4e0b4ba4aad112e84f32e3b5dbb-Paper-Conference.pdf), [Democratizing Fine-grained Visual Recognition with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/49299a8afda8053932a4cfd62fdfd1b9-Paper-Conference.pdf), [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf), [Let Models Speak Ciphers: Multiagent Debate through Embeddings](https://proceedings.iclr.cc/paper_files/paper/2024/file/e444859b2a22df6b56af9381ad1e9480-Paper-Conference.pdf), [Towards Robust Multi-Modal Reasoning via Model Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c78ae0c1140902bf3a430b1725bcc4e-Paper-Conference.pdf), [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf), [Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf), [Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.429.pdf), [Constrained Decoding with Speculative Lookaheads](https://aclanthology.org/2025.naacl-long.239.pdf), [Latent Factor Models Meets Instructions: Goal-conditioned Latent Factor Discovery without Task Supervision](https://aclanthology.org/2025.naacl-long.554.pdf), [LLM-guided Plan and Retrieval: A Strategic Alignment for Interpretable User Satisfaction Estimation in Dialogue](https://aclanthology.org/2025.naacl-long.523.pdf), [CSR-Bench: Benchmarking LLM Agents in Deployment of Computer Science Research Repositories](https://aclanthology.org/2025.naacl-long.633.pdf), [UniICL: An Efficient ICL Framework Unifying Compression, Selection, and Generation](https://aclanthology.org/2025.acl-long.24.pdf), [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aa/chen25aa.pdf), [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf))
> The emergent capability of a large language model to logically process given information and infer conclusions or generate new insights, particularly when guided by well-structured prompts.

**Inference ability** (1 paper: [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf))
> The capacity of a large language model to reason and draw conclusions based on its existing knowledge.

**Reasoning capacity** (2 papers: [Entity Alignment with Noisy Annotations from Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1b57aaddf85ab01a2445a79c9edc1f4b-Paper-Conference.pdf), [AdamMeme: Adaptively Probe the Reasoning Capacity of Multimodal Large Language Models on Harmfulness](https://aclanthology.org/2025.acl-long.213.pdf))
> The model's latent ability to infer correct outputs through multi-step or probabilistic inference rather than direct pattern matching.

**Inferential capabilities** (1 paper: [MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf))
> The model's underlying ability to make inferences and draw conclusions from given information, which can be enhanced through prompting techniques.

**Inferences** (1 paper: [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to make plausible deductions about the model's present situation from cues in the prompt or context.

**General inference capability** (1 paper: [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf))
> The model's broad ability to perform reasoning and apply knowledge across a wide range of general-purpose tasks, as opposed to specific trustworthiness-related behaviors.

**Reasoning capabilities** (1 paper: [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf))
> The broader latent capacity of an LLM to solve reasoning-oriented tasks across domains such as mathematics and programming.

**Reasoning skills** (1 paper: [DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf))
> The latent capacity to solve problems that require multi-step inference, especially in math-oriented and other reasoning-heavy settings.

**Inference capability** (1 paper: [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf))
> The model's ability to generate accurate outputs by leveraging internalized knowledge of structured linguistic information during task execution.

**Inferential ability** (1 paper: [Can Large Language Models Understand Internet Buzzwords Through User-Generated Content](https://aclanthology.org/2025.acl-long.632.pdf))
> The latent capacity of an LLM to deduce the meaning of a previously unseen buzzword solely from contextual user-generated content, without relying on prior exposure or memorization.

**Thinking** (1 paper: [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf))
> The latent ability of an LLM to generate internal reasoning or planning processes in natural language before producing a final response, enabling improved performance on complex tasks through implicit computation and self-reflection.

**Reasoning performance** (1 paper: [Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes](https://aclanthology.org/2025.emnlp-main.132.pdf))
> The latent capacity of a model to correctly solve complex reasoning tasks, inferred from accuracy across diverse problems and conditions.

**General reasoning** (1 paper: [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf))
> Performing broad reasoning tasks that require inference across diverse domains rather than a single specialized skill.

**Comprehensive reasoning** (1 paper: [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf))
> The general reasoning capacity reflected in performance on hard benchmark tasks requiring multi-step inference.

**Few-shot reasoning** (1 paper: [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf))
> The observable behavior of performing reasoning tasks when provided with only a small number of examples (e.g., 5-shot) in the prompt.

## Relationships

### Reasoning →
- **GSM8K** (measurement instrument): *measured_by*, 49 papers
  > We leverage the Grade School Math dataset (GSM) (Cobbe et al., 2021) to assess the reasoning proficiency of models. (Section 4.1)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
  - [ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/13250eb13871b3c2c0a0667b54bad165-Paper-Conference.pdf)
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf)
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
  - [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)
  - [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
  - [Quantifying Generalization Complexity for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1a65614bf80c4168acc2b6f05f0950c-Paper-Conference.pdf)
  - [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf)
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
  - [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf)
  - [Understanding and Enhancing Safety Mechanisms of LLMs via Safety-Specific Neuron](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d2666e2cf44088cc57204fbc5ef7f34-Paper-Conference.pdf)
  - [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
  - [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf)
  - [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf)
  - [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356.pdf)
  - [TESS 2: A Large-Scale Generalist Diffusion Language Model](https://aclanthology.org/2025.acl-long.1029.pdf)
  - [Towards the Law of Capacity Gap in Distilling Language Models](https://aclanthology.org/2025.acl-long.1097.pdf)
  - [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf)
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
  - [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf)
  - [The Jailbreak Tax: How Useful are Your Jailbreak Outputs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nikolic25a/nikolic25a.pdf)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
  - [Deliberation in Latent Space via Differentiable Cache Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bc/liu25bc.pdf)
  - [Portable Reward Tuning: Towards Reusable Fine-Tuning across Different Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chijiwa25a/chijiwa25a.pdf)
  - [Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf)
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
  - [GANQ: GPU-Adaptive Non-Uniform Quantization for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25ae/zhao25ae.pdf)
  - [What Do Learning Dynamics Reveal About Generalization in LLM Mathematical Reasoning?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kang25f/kang25f.pdf)
  - [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf)
  - [An Empirical Study of LLM Reasoning Ability Under Strict Output Length Constraint](https://aclanthology.org/2025.emnlp-main.389.pdf)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
  - [PruneCD: Contrasting Pruned Self Model to Improve Decoding Factuality](https://aclanthology.org/2025.emnlp-main.1651.pdf)
  - [LoSiA: Efficient High-Rank Fine-Tuning via Subnet Localization and Optimization](https://aclanthology.org/2025.emnlp-main.340.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 31 papers
  > One such benchmark is Bigbench-hard (Srivastava et al., 2022), which includes multiple reasoning tasks consisting of multiple-choice and direct-generation tasks. (Section 4.3)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e1a87dbb7e954b8d9d6c91f6db771eb-Paper-Conference.pdf)
  - [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Self-playing Adversarial Language Game Enhances LLM Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4be7e9867ef163563f4a5e90cec478f-Paper-Conference.pdf)
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
  - [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
  - [Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f74d79573d71078848973009d0e99bdb-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf)
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
  - [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
  - [Dynamic Data Mixing Maximizes Instruction Tuning for Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.80.pdf)
  - [From Informal to Formal – Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs](https://aclanthology.org/2025.acl-long.1310.pdf)
  - [TESS 2: A Large-Scale Generalist Diffusion Language Model](https://aclanthology.org/2025.acl-long.1029.pdf)
  - [Towards the Law of Capacity Gap in Distilling Language Models](https://aclanthology.org/2025.acl-long.1097.pdf)
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
  - [Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law](https://aclanthology.org/2025.acl-long.1157.pdf)
  - [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
  - [Evaluating Robustness of Large Audio Language Models to Audio Injection: An Empirical Study](https://aclanthology.org/2025.emnlp-main.1303.pdf)
- **MMLU** (measurement instrument): *measured_by*, 18 papers
  > We select 24 datasets from MMLU (Hendrycks et al., 2021), Big-Bench-Hard (Suzgun et al., 2022), and MBPP (Austin et al., 2021) to evaluate the knowledge and reasoning abilities of LLMs in diverse domains. (p. 3)
  - [Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e1a87dbb7e954b8d9d6c91f6db771eb-Paper-Conference.pdf)
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Towards Next-Level Post-Training Quantization of Hyper-Scale Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab6eba9a853087993addff937c8cec87-Paper-Conference.pdf)
  - [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
  - [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
  - [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf)
  - [Deliberation in Latent Space via Differentiable Cache Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bc/liu25bc.pdf)
  - [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aa/chen25aa.pdf)
- **PIQA** (measurement instrument): *measured_by*, 14 papers
  > For reasoning abilities, we use ARC-Easy, ARC-Challenge [42], SIQA [43], PIQA [44], WinoGrande [45], and QUAC [46] (all 0-shot).
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf)
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
  - [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf)
  - [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [LoRA-Gen: Specializing Large Language Model via Online LoRA Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25e/xiao25e.pdf)
  - [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf)
- **MATH** (measurement instrument): *measured_by*, 13 papers
  > We test SELF-DISCOVER on 25 challenging reasoning tasks including Big Bench-Hard (BBH) (Suzgun et al., 2022), Thinking for Doing (T4D) (Zhou et al., 2023) and MATH (Hendrycks et al., 2021). (Section 1)
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
  - [Quantifying Generalization Complexity for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1a65614bf80c4168acc2b6f05f0950c-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf)
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
  - [The Jailbreak Tax: How Useful are Your Jailbreak Outputs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nikolic25a/nikolic25a.pdf)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
  - [Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25a/zhao25a.pdf)
  - [ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1453.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 13 papers
  > We evaluate the reasoning performance of quantized models using zero-shot tasks (e.g., ARC [4], HellaSwag [34], and MMLU [8]). (Section 4.2)
  - [Towards Next-Level Post-Training Quantization of Hyper-Scale Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab6eba9a853087993addff937c8cec87-Paper-Conference.pdf)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf)
  - [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [LoRA-Gen: Specializing Large Language Model via Online LoRA Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25e/xiao25e.pdf)
  - [From Parameters to Performance: A Data-Driven Study on LLM Structure and Development](https://aclanthology.org/2025.emnlp-main.1325.pdf)
  - [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 13 papers
  > For reasoning abilities, we use ARC-Easy, ARC-Challenge [42], SIQA [43], PIQA [44], WinoGrande [45], and QUAC [46] (all 0-shot).
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
  - [Speculative Prefill: Turbocharging TTFT with Lightweight and Training-Free Token Importance Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25g/liu25g.pdf)
  - [LoRA-Gen: Specializing Large Language Model via Online LoRA Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25e/xiao25e.pdf)
  - [From Parameters to Performance: A Data-Driven Study on LLM Structure and Development](https://aclanthology.org/2025.emnlp-main.1325.pdf)
  - [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 12 papers
  > For reasoning abilities, we use ARC-Easy, ARC-Challenge [42], SIQA [43], PIQA [44], WinoGrande [45], and QUAC [46] (all 0-shot).
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [LoRA-Gen: Specializing Large Language Model via Online LoRA Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25e/xiao25e.pdf)
  - [From Parameters to Performance: A Data-Driven Study on LLM Structure and Development](https://aclanthology.org/2025.emnlp-main.1325.pdf)
  - [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf)
- **MATH-500** (measurement instrument): *measured_by*, 9 papers
  > We evaluate across 6 reasoning benchmarks used in the original papers of the above prompting strategies, including GSM8K (Cobbe et al., 2021), GSM-Hard (Gao et al., 2023), MATH-500 (Hendrycks et al., 2021b; Lightman et al., 2024), MMLU-high-school-biology, chemistry and physics (Hendrycks et al., 2021a). (Section 2.3)
  - [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356.pdf)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
  - [Enhancing Reasoning Abilities of Small LLMs with Cognitive Alignment](https://aclanthology.org/2025.emnlp-main.377.pdf)
  - [An Empirical Study of LLM Reasoning Ability Under Strict Output Length Constraint](https://aclanthology.org/2025.emnlp-main.389.pdf)
  - [Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.931.pdf)
  - [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf)
  - [The Impact of Language Mixing on Bilingual LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1654.pdf)
  - [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **ARC** (measurement instrument): *measured_by*, 8 papers
  > We evaluate the reasoning performance of quantized models using zero-shot tasks (e.g., ARC [4], HellaSwag [34], and MMLU [8]). (Section 4.2)
  - [Towards Next-Level Post-Training Quantization of Hyper-Scale Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab6eba9a853087993addff937c8cec87-Paper-Conference.pdf)
  - [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
  - [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **RewardBench** (measurement instrument): *measured_by*, 8 papers
  > RewardBench, which features a variety of prompts from categories such as Chat, Chat Hard, Safety, and Reasoning.
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
  - [Generative Reward Modeling via Synthetic Criteria Preference Learning](https://aclanthology.org/2025.acl-long.1297.pdf)
  - [Improving Model Alignment Through Collective Intelligence of Open-Source Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dr/wang25dr.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 7 papers
  > For reasoning abilities, we use ARC-Easy, ARC-Challenge [42], SIQA [43], PIQA [44], WinoGrande [45], and QUAC [46] (all 0-shot).
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [Explaining Modern Gated-Linear RNNs via a Unified Implicit Attention Formulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf)
  - [LoRA-Gen: Specializing Large Language Model via Online LoRA Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25e/xiao25e.pdf)
  - [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf)
- **AIME 2024** (measurement instrument): *measured_by*, 7 papers
  > We focus on four representative reasoning benchmarks: MATH-500, AIME 2024, TheoremQA (Chen et al., 2023), and MMLU-Pro-1k (Wang et al., 2024a). (Section 2.5)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
  - [Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25a/zhao25a.pdf)
  - [Enhancing Reasoning Abilities of Small LLMs with Cognitive Alignment](https://aclanthology.org/2025.emnlp-main.377.pdf)
  - [Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.931.pdf)
  - [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf)
  - [Accelerated Test-Time Scaling with Model-Free Speculative Sampling](https://aclanthology.org/2025.emnlp-main.1558.pdf)
  - [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **GPQA** (measurement instrument): *measured_by*, 7 papers
  > To rigorously assess the capabilities of models in reasoning abilities across different domains, we utilize several widely used datasets, GSM8K [Cobbe et al., 2021], MATH [Hendrycks et al., 2021b], TheoremQA [Chen et al., 2023b], BIG-Bench Hard (BBH) [Suzgun et al., 2022], ARC-C [Clark et al., 2018], GPQA [Rein et al., 2023], MMLU-STEM [Hendrycks et al., 2021a]. (Section 3.2)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356.pdf)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
  - [Speculative Prefill: Turbocharging TTFT with Lightweight and Training-Free Token Importance Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25g/liu25g.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1453.pdf)
  - [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **Generalization** (construct): *causes*, 7 papers
  > Few-shot reasoning allows LLMs to generalize their understanding to new tasks by leveraging a small set of similar examples. (Sec. 3.3)
  - [Verified Code Transpilation with LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/48bb60a0c0aebb4142bf314bd1a5c6a0-Paper-Conference.pdf)
  - [Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf)
  - [MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d6c53fe062716387ff0df73cc53de60c-Paper-Conference.pdf)
  - [Can We Trust Embodied Agents? Exploring Backdoor Attacks against Embodied LLM-Based Decision-Making Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7af02c8a8e26608199c087f50a21d37-Paper-Conference.pdf)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
  - [Few-Shot Open-Set Classification via Reasoning-Aware Decomposition](https://aclanthology.org/2025.emnlp-main.699.pdf)
- **Code generation** (behavioral indicator): *causes*, 7 papers
  > A host of prompting techniques have shown how to leverage the In-Context Learning (ICL) abilities of LLMs to enhance a model's reasoning skills, and, as a result, the quality of generated programs.
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [Are Large Language Models Ready for Multi-Turn Tabular Data Analysis?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25aj/li25aj.pdf)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
  - [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 6 papers
  > MT-bench consists of multi-turn conversations across various domains such as writing, reasoning, math, and coding. (Section 2.2)
  - [What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/6091f2bb355e960600f62566ac0e2862-Paper-Conference.pdf)
  - [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf)
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
  - [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
  - [Select-Then-Decompose: From Empirical Analysis to Adaptive Selection Strategy for Task Decomposition in Large Language Models](https://aclanthology.org/2025.emnlp-main.278.pdf)
- **Interpretability and explainability** (construct): *causes*, 6 papers
  > Mindmap [74] provides more transparency on LLMs’ decision-making by enabling comprehension and reasoning over structured KG inputs. (Section 1)
  - [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
  - [A Hitchhiker's Guide to Fine-Grained Face Forgery Detection Using Common Sense Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/059d2b9188cdb7ae00f4d78cc9469704-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
  - [REARANK: Reasoning Re-ranking Agent via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.125.pdf)
  - [MR. Judge: Multimodal Reasoner as a Judge](https://aclanthology.org/2025.emnlp-main.1021.pdf)
- **GPQA-Diamond** (measurement instrument): *measured_by*, 5 papers
  > Reasoning Models, in which we perform SFT with Qwen-2.5 on s1K dataset (Muennighoff et al., 2025) and evaluated on GPQA Diamond (Rein et al., 2023) (Section 5.1).
  - [LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf)
  - [Enhancing Reasoning Abilities of Small LLMs with Cognitive Alignment](https://aclanthology.org/2025.emnlp-main.377.pdf)
  - [Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.931.pdf)
  - [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf)
  - [Accelerated Test-Time Scaling with Model-Free Speculative Sampling](https://aclanthology.org/2025.emnlp-main.1558.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 5 papers
  > For our performance evaluation, we use the few-shot tasks from Language Model Evaluation Harness (Gao et al., 2021). We select these tasks such that they can measure various abilities of the models (e.g., reading comprehension, reasoning, etc.) (Sec. 3.1)
  - [ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6cf669c222ad13f60d503736fb2bd15b-Paper-Conference.pdf)
  - [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 5 papers
  > HotPotQA [49] features natural, multi-hop questions, which challenge an agent’s ability to perform reasoning and utilize search tools.
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf)
  - [xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **MMMU** (measurement instrument): *measured_by*, 5 papers
  > For general reasoning, benchmarks like MathVista [31] and MMMU [32] assess models on tasks involving multiple-choice and free-form questions, with a focus on multimodal data.
  - [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
  - [TaskGalaxy: Scaling Multi-modal Instruction Fine-tuning with Tens of Thousands Vision Task Types](https://proceedings.iclr.cc/paper_files/paper/2025/file/e885e5bc6e13b9dd8f80bc5482b1fa2f-Paper-Conference.pdf)
  - [Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25at/yang25at.pdf)
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
- **HumanEval** (measurement instrument): *measured_by*, 4 papers
  > HumanEval ... a coding task that requires complex reasoning and planning ability.
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
  - [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aa/chen25aa.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 4 papers
  > We evaluate Spectra Suite models using eight distinct common-sense and reasoning benchmarks consisting of tasks from logical and reasoning questions to grounded and physical commonsense tasks: Arc Easy, Arc Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), HellaSWAG (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), PIQA (Bisk et al., 2019), LAMBADA (Paperno et al., 2016), LogiQA (Liu et al., 2021), all under zero-shot settings. (Section 5)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
  - [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf)
  - [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf)
  - [LoRA-Gen: Specializing Large Language Model via Online LoRA Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25e/xiao25e.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 4 papers
  > Seven reasoning datasets used in the experiments include OpenbookQA (Banerjee et al., 2020), WinoGrande (Sakaguchi et al., 2021) HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019), ARC-e, ARC-c (Clark et al., 2018). (Section 4.1)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
  - [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf)
  - [LoRA-Gen: Specializing Large Language Model via Online LoRA Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25e/xiao25e.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 3 papers
  > We use MMLU Hendrycks et al. (2020), BigBench Hard (BBH) Srivastava et al. (2022), and 4 reasoning benchmarks: GSM8K Cobbe et al. (2021), SVAMP Patel et al. (2021), ASDIV Miao et al. (2020), and StrategyQA Geva et al. (2021) (Section 3.1).
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
- **MathVista** (measurement instrument): *measured_by*, 3 papers
  > For general reasoning, benchmarks like MathVista [31] and MMMU [32] assess models on tasks involving multiple-choice and free-form questions, with a focus on multimodal data.
  - [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **LogiQA** (measurement instrument): *measured_by*, 3 papers
  > We evaluate Spectra Suite models using eight distinct common-sense and reasoning benchmarks consisting of tasks from logical and reasoning questions to grounded and physical commonsense tasks: Arc Easy, Arc Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), HellaSWAG (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), PIQA (Bisk et al., 2019), LAMBADA (Paperno et al., 2016), LogiQA (Liu et al., 2021), all under zero-shot settings. (Section 5)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
  - [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf)
- **Game of 24** (measurement instrument): *measured_by*, 3 papers
  > We study Game of 24 (Yao et al., 2023), a reasoning problem where the transition dynamics and rules are well-defined and readily available.
  - [Learning to Search from Demonstration Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdf80d651420b47da80f789f2631b1b5-Paper-Conference.pdf)
  - [Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf)
  - [On the self-verification limitations of large language models on reasoning and planning tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3c5e56274140e0420baa3916c529210-Paper-Conference.pdf)
- **Robustness** (construct): *causes*, 3 papers
  > A recent advancement in enhancing robustness is ICL with explanations (X-ICL), which improves prediction reliability by guiding LLMs to understand and articulate the reasoning behind correct labels. (Abstract)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
  - [MR. Judge: Multimodal Reasoner as a Judge](https://aclanthology.org/2025.emnlp-main.1021.pdf)
- **ARC-AGI** (measurement instrument): *measured_by*, 3 papers
  > We demonstrate SOAR’s effectiveness on the Abstraction and Reasoning Corpus (ARC), a program synthesis benchmark specifically designed to challenge AI models’ core reasoning capabilities (Chollet, 2019).
  - [Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pourcel25a/pourcel25a.pdf)
  - [RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf)
  - [Test-Time Training Provably Improves Transformers as In-context Learners](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gozeten25a/gozeten25a.pdf)
- **Planning** (construct): *causes*, 3 papers
  > Crucially, the agent needs to perform multi-step reasoning between such information and the current state of the environment to figure out a plan of action
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [ChatCam: Empowering Camera Control through Conversational AI](https://proceedings.neurips.cc/paper_files/paper/2024/file/61dad41cb106aef1154a82965f42df0e-Paper-Conference.pdf)
  - [Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf)
- **MBPP** (measurement instrument): *measured_by*, 2 papers
  > We select 24 datasets from MMLU (Hendrycks et al., 2021), Big-Bench-Hard (Suzgun et al., 2022), and MBPP (Austin et al., 2021) to evaluate the knowledge and reasoning abilities of LLMs in diverse domains. (p. 3)
  - [Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e1a87dbb7e954b8d9d6c91f6db771eb-Paper-Conference.pdf)
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
- **SVAMP** (measurement instrument): *measured_by*, 2 papers
  > We use MMLU Hendrycks et al. (2020), BigBench Hard (BBH) Srivastava et al. (2022), and 4 reasoning benchmarks: GSM8K Cobbe et al. (2021), SVAMP Patel et al. (2021), ASDIV Miao et al. (2020), and StrategyQA Geva et al. (2021) (Section 3.1).
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
- **Action selection** (behavioral indicator): *causes*, 2 papers
  > In the Reasoning module, we utilize the experiences derived from the Memory module and the common-sense knowledge of the LLM to perform decision-making for the current traffic scenario. (Section 3.3)
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
  - [Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf)
- **GSM-Hard** (measurement instrument): *measured_by*, 2 papers
  > Extensive experiments across five SLMs demonstrate rStar can effectively solve diverse reasoning problems, including GSM8K, GSM-Hard, MATH, SVAMP, and StrategyQA.
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
  - [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356.pdf)
- **DROP** (measurement instrument): *measured_by*, 2 papers
  > Moreover, MINIMA achieves superior performance over baselines with respect to ... reasoning (DROP, BBH, GSM8K)...
  - [Towards the Law of Capacity Gap in Distilling Language Models](https://aclanthology.org/2025.acl-long.1097.pdf)
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
- **MMStar** (measurement instrument): *measured_by*, 2 papers
  > MMStar and MMBench (Chen et al., 2024a; Liu et al., 2025) provide comprehensive evaluations by categorizing VLM tasks into two primary domains: perception and reasoning. (Section 5.1)
  - [SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25c/park25c.pdf)
  - [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **GAIA** (measurement instrument): *measured_by*, 2 papers
  > GAIA proposes real-world questions that require a set of fundamental abilities such as reasoning, multi-modality handling, web browsing, and generally tool-use proficiency. (ABSTRACT)
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
  - [Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools](https://aclanthology.org/2025.acl-long.1383.pdf)
- **GQA** (measurement instrument): *measured_by*, 2 papers
  > The GQA dataset does not rely on external knowledge and is used to evaluate the reasoning ability of LVLMs (Section 5.2).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 2 papers
  > In this paper, we introduce MMLU-Pro: a comprehensive benchmark designed for proficient-level multi-discipline language understanding and reasoning. (Section 1).
  - [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad236edc564f3e3156e1b2feafb99a24-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1453.pdf)
- **PrOntoQA** (measurement instrument): *measured_by*, 2 papers
  > Reasoning tasks: PrOntoQA. PrOntoQA (Saparov and He, 2023) is a synthetic multi-step reasoning dataset where each data point assigns hierarchical relationships among objects and requires the model to determine whether a multi-step reasoning chain is correct. (Section 6)
  - [Initialization is Critical to Whether Transformers Fit Composite Functions by Reasoning or Memorizing](https://proceedings.neurips.cc/paper_files/paper/2024/file/19c145aaad40927c51f4d10eaa339c20-Paper-Conference.pdf)
  - [An Analysis for Reasoning Bias of Language Models with Small Initialization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yao25g/yao25g.pdf)
- **MGSM** (measurement instrument): *measured_by*, 2 papers
  > To comprehensively understand how LLMs work with different abilities, we employ four kinds of tasks including MGSM (Shi et al., 2022) for reasoning task... (Section 3.2)
  - [How do Large Language Models Handle Multilingualism?](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bd359b32ab8b2a6bbafa1ed2856cf40-Paper-Conference.pdf)
  - [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 2 papers
  > Our evaluations on standard reasoning datasets (GSM8K, CSQA, and LLC) with various LLMs and prompts show that TREACLE enables cost savings of up to 85% compared to baselines, while maintaining high accuracy. (Abstract)
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
  - [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)
- **TheoremQA** (measurement instrument): *measured_by*, 2 papers
  > To rigorously assess the capabilities of models in reasoning abilities across different domains, we utilize several widely used datasets, GSM8K [Cobbe et al., 2021], MATH [Hendrycks et al., 2021b], TheoremQA [Chen et al., 2023b], BIG-Bench Hard (BBH) [Suzgun et al., 2022], ARC-C [Clark et al., 2018], GPQA [Rein et al., 2023], MMLU-STEM [Hendrycks et al., 2021a]. (Section 3.2)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **MMLU-STEM** (measurement instrument): *measured_by*, 2 papers
  > To rigorously assess the capabilities of models in reasoning abilities across different domains, we utilize several widely used datasets, GSM8K [Cobbe et al., 2021], MATH [Hendrycks et al., 2021b], TheoremQA [Chen et al., 2023b], BIG-Bench Hard (BBH) [Suzgun et al., 2022], ARC-C [Clark et al., 2018], GPQA [Rein et al., 2023], MMLU-STEM [Hendrycks et al., 2021a]. (Section 3.2)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 2 papers
  > We evaluate Spectra Suite models using eight distinct common-sense and reasoning benchmarks consisting of tasks from logical and reasoning questions to grounded and physical commonsense tasks: Arc Easy, Arc Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), HellaSWAG (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), PIQA (Bisk et al., 2019), LAMBADA (Paperno et al., 2016), LogiQA (Liu et al., 2021), all under zero-shot settings. (Section 5)
  - [Surprising Effectiveness of pretraining Ternary Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
  - [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf)
- **LiveBench** (measurement instrument): *measured_by*, 2 papers
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
  - [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 2 papers
  > For standard contexts, we utilize generation tasks from LM-Eval (Gao et al., 2021), assessing model performance across commonsense and math reasoning on CoQA (Exact Match (EM) Accuracy) (Reddy et al., 2019), TruthfulQA (BLEU score) (Lin et al., 2022), and GSM8K (Exact Match (EM) Accuracy) Cobbe et al. (2021b). (Section 5.1)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
  - [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf)
- **MMLU-Redux** (measurement instrument): *measured_by*, 2 papers
  > Furthermore, we also evaluate all the models on four logical reasoning benchmarks to verify the impact of these alignment methods on model’s reasoning abilities, including: MMLU-redux (Gema et al., 2024) (Language)...
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
  - [Representation Shattering in Transformers: A Synthetic Study with Knowledge Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nishi25a/nishi25a.pdf)
- **MathQA** (measurement instrument): *measured_by*, 2 papers
  > Seven reasoning datasets used in the experiments include OpenbookQA (Banerjee et al., 2020), WinoGrande (Sakaguchi et al., 2021) HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), MathQA (Amini et al., 2019), ARC-e, ARC-c (Clark et al., 2018). (Section 4.1)
  - [Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 2 papers
  > To probe the visual understanding and reasoning ability of our LLaVA-1.5-LLaMA3-8B model, we opt for two comprehensive multi-modal evaluation benchmarks, MMMU (Yue et al., 2024) and MM-Vet (Yu et al., 2024).
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
  - [LATTE: Learning to Think with Vision Specialists](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **Tool use** (behavioral indicator): *causes*, 2 papers
  > The LLM must use reasoning to deduce the suitable tools to address the given tasks. (Section 1)
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf)
- **Coding ability** (construct): *causes*, 2 papers
  > This limitation stems from the restricted reasoning abilities of single LLMs... they struggle to tackle more complex coding tasks.
  - [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Expressive power** (construct): *causes*, 2 papers
  > We theoretically show that the loss of expressivity of LLMs under constrained decoding arises because the output grammar G is too restrictive to accommodate the intermediate reasoning steps required to compute the answer. (Section 1)
  - [CRANE: Reasoning with constrained LLM generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/banerjee25a/banerjee25a.pdf)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
- **OlympiadBench** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our method on a diverse set of reasoning tasks, including GSM8K (Cobbe et al., 2021b), MATH500 (Hendrycks et al., 2021), MMLU STEM (Hendrycks et al., 2020), OlympiadBench (He et al., 2024), GaoKao-2023-En (Liao et al., 2024), GPQA (Rein et al., 2023), and Minerva Math (Lewkowycz et al., 2022). (Section 3)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **Open LLM Leaderboard** (measurement instrument): *measured_by*, 1 paper
  > Reasoning ability is measured via the Open LLM Leaderboard (Beeching et al., 2023) using the Language Model Evaluation Harness (Gao et al., 2023). (Section 3.2)
  - [MAIN: Mutual Alignment Is Necessary for instruction tuning](https://aclanthology.org/2025.emnlp-main.644.pdf)
- **AIME** (measurement instrument): *measured_by*, 1 paper
  > We also extend experiments on two more challenging reasoning benchmarks, GPQA (Rein et al., 2024) and AIME (Mathematical Association of America, 2024), further verifying the generality of our findings and methods. (Section 8)
  - [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356.pdf)
- **ASDiv** (measurement instrument): *measured_by*, 1 paper
  > We use MMLU Hendrycks et al. (2020), BigBench Hard (BBH) Srivastava et al. (2022), and 4 reasoning benchmarks: GSM8K Cobbe et al. (2021), SVAMP Patel et al. (2021), ASDIV Miao et al. (2020), and StrategyQA Geva et al. (2021) (Section 3.1).
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **SIQA** (measurement instrument): *measured_by*, 1 paper
  > For reasoning abilities, we use ARC-Easy, ARC-Challenge [42], SIQA [43], PIQA [44], WinoGrande [45], and QUAC [46] (all 0-shot).
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **CMMLU** (measurement instrument): *measured_by*, 1 paper
  > We use zero-shot or few-shot learning to test the reasoning ability across five benchmarks, including MMLU (Hendrycks et al., 2021), CMMLU (Li et al., 2024a), Truthful-QA (Lin et al., 2021), GSM-PLUS (Li et al., 2024b), and GSM8K (Cobbe et al., 2021). (Section 4.3.1)
  - [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > The reasoning tasks include MathQA (Amini et al., 2019), Massive Multitask Language Understanding (MMLU) (Hendrycks et al., 2020), Physical Interaction: Question Answering (PIQA) (Bisk et al., 2020), LogiQA (Liu et al., 2020), TriviaQA (Joshi et al., 2017) and GSM8K (Cobbe et al., 2021). (Section 5.3)
  - [Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.305.pdf)
- **Minerva Math** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our method on a diverse set of reasoning tasks, including GSM8K (Cobbe et al., 2021b), MATH500 (Hendrycks et al., 2021), MMLU STEM (Hendrycks et al., 2020), OlympiadBench (He et al., 2024), GaoKao-2023-En (Liao et al., 2024), GPQA (Rein et al., 2023), and Minerva Math (Lewkowycz et al., 2022). (Section 3)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **AgentBench** (measurement instrument): *measured_by*, 1 paper
  > We present AGENTBENCH, a multi-dimensional benchmark that consists of 8 distinct environments to assess LLM-as-Agent’s reasoning and decision-making abilities.
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **WebQSP** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the reasoning ability of RoG on two benchmark KGQA datasets: WebQuestionSP (WebQSP) (Yih et al., 2016) and Complex WebQuestions (CWQ) (Talmor & Berant, 2018) (Section 5.1)
  - [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf)
- **CWQ** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the reasoning ability of RoG on two benchmark KGQA datasets: WebQuestionSP (WebQSP) (Yih et al., 2016) and Complex WebQuestions (CWQ) (Talmor & Berant, 2018) (Section 5.1)
  - [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf)
- **GTA** (measurement instrument): *measured_by*, 1 paper
  > Fine-grained metrics are designed for tool use, unveiling tool-augmented LLMs’ reasoning and planning capabilities in real-world scenarios. (Section 1)
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **QuAC** (measurement instrument): *measured_by*, 1 paper
  > For reasoning abilities, we use ARC-Easy, ARC-Challenge [42], SIQA [43], PIQA [44], WinoGrande [45], and QUAC [46] (all 0-shot).
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **Multilingual reasoning** (construct): *causes*, 1 paper
  > utilize the built-in reasoning and language understanding capabilities of LLMs... to boost the multilingual reasoning effects.
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **Attribute generation** (behavioral indicator): *causes*, 1 paper
  > To extract these attributes, we employ an LLM to reason about the target object’s characteristics. (Section 3.2)
  - [GAMap: Zero-Shot Object Goal Navigation with Multi-Scale Geometric-Affordance Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/459d93dad139eb084c365d40a57eada3-Paper-Conference.pdf)
- **MedQA** (measurement instrument): *measured_by*, 1 paper
  > both MMLU and MedQA are more oriented toward reasoning rather than pure factual recall, which poses bigger challenges for both the retriever and the LM. (Section 4.2)
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Last letter concatenation** (measurement instrument): *measured_by*, 1 paper
  > Our evaluations on standard reasoning datasets (GSM8K, CSQA, and LLC) with various LLMs and prompts show that TREACLE enables cost savings of up to 85% compared to baselines, while maintaining high accuracy. (Abstract)
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
- **SEED-Bench** (measurement instrument): *measured_by*, 1 paper
  > Reasoning is benchmarked using GQA [15], MathVista [29], Mementos [43], SEED-Bench [22], and RealWorldQA [13] in VHELM. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **RealWorldQA** (measurement instrument): *measured_by*, 1 paper
  > Reasoning is benchmarked using GQA [15], MathVista [29], Mementos [43], SEED-Bench [22], and RealWorldQA [13] in VHELM. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **QNLI** (measurement instrument): *measured_by*, 1 paper
  > For inference ability, we choose six datasets including Hellaswag [48], PIQA [1], WinoGrande [32], QNLI [31], MNLI [44], and WikiText2 [28] for evaluation.
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MNLI** (measurement instrument): *measured_by*, 1 paper
  > For inference ability, we choose six datasets including Hellaswag [48], PIQA [1], WinoGrande [32], QNLI [31], MNLI [44], and WikiText2 [28] for evaluation.
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **WikiText-2** (measurement instrument): *measured_by*, 1 paper
  > For inference ability, we choose six datasets including Hellaswag [48], PIQA [1], WinoGrande [32], QNLI [31], MNLI [44], and WikiText2 [28] for evaluation.
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **2WikiMultiHopQA** (measurement instrument): *measured_by*, 1 paper
  > “Experiments across three complex question-answering datasets reveal that ASSISTRAG exhibits superior reasoning capabilities” and the datasets include “2WikiMultiHopQA [35]”
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > We believe this result indicates that self-improvement requires a minimal level of instruction following and reasoning capabilities, which is not present in these small models. (Section 4.1)
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **Trustworthiness** (construct): *causes*, 1 paper
  > our framework leverages the reasoning capabilities of LLMs, enhancing the trustworthiness of clinical predictions. (Abstract)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **JudgeBench** (measurement instrument): *measured_by*, 1 paper
  > we introduce JudgeBench, a benchmark designed to evaluate LLM-based judges on difficult response pairs that require advanced reasoning abilities. (Section 1)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Disambiguation ability** (construct): *causes*, 1 paper
  > Reasoning and reflection are crucial for the model to correctly understand ambiguous instructions. (Table 5)
  - [Visual-O1: Understanding Ambiguous Instructions via Multi-modal Multi-turn Chain-of-thoughts Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3769fddee1b20552d2490c4ff18b136-Paper-Conference.pdf)
- **Action generation** (behavioral indicator): *causes*, 1 paper
  > For vision-based agents, completing a complex GUI task typically involves several steps, each requiring the model to: (1) Perceive and understand... (2) Reason and plan... (3) Execute: perform the desired action on the target GUI element.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **CoQA** (measurement instrument): *measured_by*, 1 paper
  > For standard contexts, we utilize generation tasks from LM-Eval (Gao et al., 2021), assessing model performance across commonsense and math reasoning on CoQA (Exact Match (EM) Accuracy) (Reddy et al., 2019)... (Section 5.1)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
- **LogiQA 2.0** (measurement instrument): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including... LogiQA 2... (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **SciQ** (measurement instrument): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including... SciQ... (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **MME-RealWorld** (measurement instrument): *measured_by*, 1 paper
  > Our benchmark contains 5 real-world domains, covering 43 perception and reasoning subtasks. (Figure 1)
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **Genetic perturbation experiment design** (behavioral indicator): *causes*, 1 paper
  > BioDiscoveryAgent utilizes its vast biological knowledge along with the ability to reason over insights from previous experimental results to offer an accessible and interpretable method for designing genetic perturbation experiments.
  - [BioDiscoveryAgent: An AI Agent for Designing Genetic Perturbation Experiments](https://proceedings.iclr.cc/paper_files/paper/2025/file/4252dc94531833029000f85dc5fac792-Paper-Conference.pdf)
- **CRUXEval** (measurement instrument): *measured_by*, 1 paper
  > Furthermore, we also evaluate all the models on four logical reasoning benchmarks to verify the impact of these alignment methods on model’s reasoning abilities, including: ... CRUX (Gu et al., 2024) (Code)...
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **FOLIO** (measurement instrument): *measured_by*, 1 paper
  > we use GSM8K (Cobbe et al., 2021), Big-Bench-Hard (BBH) (Suzgun et al., 2022), and FOLIO (Han et al., 2022) benchmark datasets for diverse reasoning tasks (Section 5.1)
  - [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf)
- **ARITHMETIC context-sensitivity dataset** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our method and baselines on three language reasoning tasks. Arithmetic. consists of 1,000 generated arithmetic problems in the form a + b · c + d −e · f. (Section 3.1)
  - [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf)
- **MMAU** (measurement instrument): *measured_by*, 1 paper
  > “It includes information extraction1 and reasoning 2 questions”
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Video question answering** (behavioral indicator): *causes*, 1 paper
  > In this work, we introduce ReasVQA (Reasoning-enhanced Video Question Answering), a novel approach that leverages reasoning processes generated by Multimodal Large Language Models (MLLMs) to improve the performance of VideoQA models.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
- **Video understanding** (construct): *causes*, 1 paper
  > The results above demonstrate the effectiveness of our approach, particularly in leveraging reasoning processes to enhance video understanding.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
- **ToolBench** (measurement instrument): *measured_by*, 1 paper
  > ToolBench (Qin et al., 2024) specifically evaluates multi-turn reasoning and tool-usage abilities
  - [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf)
- **Fact checking** (behavioral indicator): *causes*, 1 paper
  > The model then performs reasoning over this combined information to predict the label Yp of the claim and generates a human-readable explanation Ye. (Section 3.4)
  - [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf)
- **RACE** (measurement instrument): *measured_by*, 1 paper
  > We also select several reasoning benchmarks, i.e., PIQA (Bisk et al., 2020), ARC (Clark et al., 2018), HellaSwag (Zellers et al., 2019), Winogrande (Sakaguchi et al., 2021), Race (Lai et al., 2017) and LAMBADA (Paperno et al., 2016), using the open-sourced toolkit lm-evaluation-harness (Gao et al., 2023). (Section 4.1)
  - [PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](https://aclanthology.org/2025.acl-long.225.pdf)
- **ReDial** (measurement instrument): *measured_by*, 1 paper
  > We introduce ReDial (Reasoning with Dialect Queries), the first high-quality, end-to-end human-annotated SE-AAVE parallel dataset for reasoning tasks (Section 2).
  - [Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks](https://aclanthology.org/2025.acl-long.317.pdf)
- **Chatbot Arena** (measurement instrument): *measured_by*, 1 paper
  > In contrast, ChatbotArena offers a broader set of real-world LLM use cases spanning diverse topics including language understanding, creative writing, reasoning, logic, and science. (Section 3.1)
  - [SkillVerse : Assessing and Enhancing LLMs with Tree Evaluation](https://aclanthology.org/2025.acl-long.437.pdf)
- **MMBench** (measurement instrument): *measured_by*, 1 paper
  > MMStar and MMBench (Chen et al., 2024a; Liu et al., 2025) provide comprehensive evaluations by categorizing VLM tasks into two primary domains: perception and reasoning. (Section 5.1)
  - [SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25c/park25c.pdf)
- **MixEval** (measurement instrument): *measured_by*, 1 paper
  > For our analysis, we look at seven datasets spanning instruction-following, reasoning, mathematics, and coding: MT-Bench (Zheng et al., 2023), AlpacaEval 2.0 (Li et al., 2023), Arena Hard Auto (Li et al., 2024b), MixEval (Ni et al., 2024), MixEval-Hard, MATH (Hendrycks et al., 2021), and CodeContests (Li et al., 2022). (Section 3.2)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **MixEval-Hard** (measurement instrument): *measured_by*, 1 paper
  > For our analysis, we look at seven datasets spanning instruction-following, reasoning, mathematics, and coding: MT-Bench (Zheng et al., 2023), AlpacaEval 2.0 (Li et al., 2023), Arena Hard Auto (Li et al., 2024b), MixEval (Ni et al., 2024), MixEval-Hard, MATH (Hendrycks et al., 2021), and CodeContests (Li et al., 2022). (Section 3.2)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 1 paper
  > To validate the effectiveness of our proposed method, we conduct extensive experiments across multiple reasoning VQA datasets, including ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024), and MathV (Wang et al., 2024a). (Section 1)
  - [Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25at/yang25at.pdf)
- **NExT-QA** (measurement instrument): *measured_by*, 1 paper
  > "video-SALMONN-o1 is also evaluated on Video-MME ... and NExT-QA ... benchmarks with challenging reasoning questions"
  - [video-SALMONN-o1: Reasoning-enhanced Audio-visual Large Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25x/sun25x.pdf)
- **GaoKao 2023 En** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our method on a diverse set of reasoning tasks, including GSM8K (Cobbe et al., 2021b), MATH500 (Hendrycks et al., 2021), MMLU STEM (Hendrycks et al., 2020), OlympiadBench (He et al., 2024), GaoKao-2023-En (Liao et al., 2024), GPQA (Rein et al., 2023), and Minerva Math (Lewkowycz et al., 2022). (Section 3)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **T-Eval** (measurement instrument): *measured_by*, 1 paper
  > We utilize T-Eval (Chen et al., 2023c), which assesses six core competencies: planning, reasoning, retrieval, understanding, instruction following, and reviewing. (Sec. 4.1)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **NLGraph** (measurement instrument): *measured_by*, 1 paper
  > reasoning (GSM8k (Cobbe et al., 2021), Knowledge Crosswords (Ding et al., 2024), NLGraph (Wang et al., 2024a; Zhang et al., 2024a)) (Section 3).
  - [Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf)
- **BANKING77** (measurement instrument): *measured_by*, 1 paper
  > This section presents a comprehensive evaluation of the reasoning accuracy of both closed-source and open-source LLMs using a range of prompt engineering and demonstration selection techniques across four benchmark datasets: BANKING77, CLINC150, HWU64, and LIU54. (Section 4.4)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **CLINC150** (measurement instrument): *measured_by*, 1 paper
  > This section presents a comprehensive evaluation of the reasoning accuracy of both closed-source and open-source LLMs using a range of prompt engineering and demonstration selection techniques across four benchmark datasets: BANKING77, CLINC150, HWU64, and LIU54. (Section 4.4)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **SST-5** (measurement instrument): *measured_by*, 1 paper
  > To further assess the generalizability and effectiveness of RDES beyond simple text classification, we conducted additional experiments on more challenging reasoning benchmarks: BigBenchHard (specifically, boolean expressions and web of lies subsets), SST5 and GSM-8K. (Section 4.5)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **Mystery Blocksworld** (measurement instrument): *measured_by*, 1 paper
  > One aims to develop novel reasoning tasks such as mystery blocksworld (Webb et al., 2024), ARCAGI (Chollet et al., 2025), and others (Zhu et al., 2023).
  - [RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf)
- **FrontierMath** (measurement instrument): *measured_by*, 1 paper
  > Recent advancements in Artificial Intelligence (AI) have sparked increasing interest in the development of reasoning systems. Central to this goal are Large Language Models (LLMs) – models like OpenAI’s o1 (Jaech et al., 2024), o3 (OpenAI, 2024), or DeepSeek-R1 (Team, 2025) show complex problem-solving abilities, and demonstrate unprecedented results on reasoning benchmarks, e.g. FrontierMath (Glazer et al., 2024) and ARC-AGI (Chollet et al., 2024).
  - [RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf)
- **XCOPA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our models on five widely adopted multilingual benchmarks in a zero-shot setting, covering a range of tasks: ... reasoning (XCOPA; Ponti et al., 2020)... (Section 3)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
- **Collaboration** (behavioral indicator): *causes*, 1 paper
  > We find that reasoning models consistently reduce cooperation and norm enforcement, favoring individual rationality. (Abstract)
  - [Spontaneous Giving and Calculated Greed in Language Models](https://aclanthology.org/2025.emnlp-main.267.pdf)
- **Style transfer** (behavioral indicator): *correlates*, 1 paper
  > models with stronger reasoning abilities (e.g., o3-mini, Deepseek) according to the benchmark 1, excel at verification and concealing authorial traits but are less effective at faithfully replicating an author’s distinctive style.
  - [Unraveling Interwoven Roles of Large Language Models in Authorship Privacy: Obfuscation, Mimicking, and Verification](https://aclanthology.org/2025.emnlp-main.753.pdf)
- **Waste-Bench** (measurement instrument): *measured_by*, 1 paper
  > To address these challenges, we propose Waste-Bench, a benchmark designed to evaluate the robustness and reasoning capabilities of VLLMs in the context of waste classification.
  - [Waste-Bench: A Comprehensive Benchmark for Evaluating VLLMs in Cluttered Environments](https://aclanthology.org/2025.emnlp-main.1578.pdf)
- **AGIEval-Math** (measurement instrument): *measured_by*, 1 paper
  > Specifically, we choose several tasks that rely on model reasoning abilities, including GPQA (Rein et al., 2023), MMLU-CF (Zhao et al., 2024), MMLU-Pro (Wang et al., 2024e), MATH (Hendrycks et al., 2021), AGIEval-Math (Zhong et al., 2023), and Med QA (Jin et al., 2021). (Section 4.1)
  - [ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1453.pdf)
- **Linguistic puzzle solving** (behavioral indicator): *causes*, 1 paper
  > Linguistic puzzles used in linguistic competitions typically require multi-step reasoning over the limited data presented in the puzzle.
  - [Can LLMs Generate and Solve Linguistic Olympiad Puzzles?](https://aclanthology.org/2025.emnlp-main.969.pdf)
- **InfiniBench** (measurement instrument): *measured_by*, 1 paper
  > InfiniBench skills: covers eight core skills, grouped into grounding-based (MCQ) and reasoning-based (open-ended) categories.
  - [InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows](https://aclanthology.org/2025.emnlp-main.984.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > Reasoning-based skills are assessed using a GPT-4o mini, assigning a score from 0 to 10.
  - [InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows](https://aclanthology.org/2025.emnlp-main.984.pdf)
- **AraEval** (measurement instrument): *measured_by*, 1 paper
  > In this paper, we present AraEval, a pioneering and comprehensive evaluation suite speciﬁcally developed to assess the advanced knowledge, reasoning, truthfulness, and instruction-following capabilities of foundation models in the Arabic context. (Abstract)
  - [AraEval: An Arabic Multi-Task Evaluation Suite for Large Language Models](https://aclanthology.org/2025.emnlp-main.1679.pdf)
- **LiveCodeBench** (measurement instrument): *measured_by*, 1 paper
  > Extensive evaluations across multiple models and reasoning tasks (AIME-2024, GPQA-Diamond, and LiveCodeBench) demonstrate that STAND reduces inference latency by 60-65% compared to standard autoregressive decoding while maintaining accuracy. (Abstract)
  - [Accelerated Test-Time Scaling with Model-Free Speculative Sampling](https://aclanthology.org/2025.emnlp-main.1558.pdf)
- **BABILong** (measurement instrument): *measured_by*, 1 paper
  > "BABILong includes a diverse set of 20 reasoning tasks"
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)

### → Reasoning
- **Chain of thought** (behavioral indicator): *causes*, 21 papers
  > This suggests that reasoning improvements from PPO may be due to increased chain-of-thought abilities. (Section 3.2).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Iterative Reasoning Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/d37c9ad425fe5b65304d500c6edcba00-Paper-Conference.pdf)
  - [OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/85f1225db986e629289f402c46eff1a4-Paper-Conference.pdf)
  - [Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf)
  - [Reasoning with Latent Thoughts: On the Power of Looped Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/2676109d49d1eb26d6bc584a8f556305-Paper-Conference.pdf)
  - [ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2025/file/9c77f2ce42151b2c2e26d2cf47f99564-Paper-Conference.pdf)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
  - [Automatic Curriculum Expert Iteration for Reliable LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9083c94382509473bdf5fc2672fc72b3-Paper-Conference.pdf)
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.584.pdf)
  - [RATIONALYST: Pre-training Process-Supervision for Improving Reasoning](https://aclanthology.org/2025.acl-long.1288.pdf)
  - [SoftCoT: Soft Chain-of-Thought for Efficient Reasoning with LLMs](https://aclanthology.org/2025.acl-long.1137.pdf)
  - [Nudging: Inference-time Alignment of LLMs via Guided Decoding](https://aclanthology.org/2025.acl-long.623.pdf)
  - [TokenSkip: Controllable Chain-of-Thought Compression in LLMs](https://aclanthology.org/2025.emnlp-main.165.pdf)
  - [DART: Distilling Autoregressive Reasoning to Silent Thought](https://aclanthology.org/2025.emnlp-main.256.pdf)
  - [Taking Notes Brings Focus? Towards Multi-Turn Multimodal Dialogue Learning](https://aclanthology.org/2025.emnlp-main.1690.pdf)
  - [Prior Prompt Engineering for Reinforcement Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1590.pdf)
  - [Steering LLM Reasoning Through Bias-Only Adaptation](https://aclanthology.org/2025.emnlp-main.467.pdf)
  - [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **Mathematical reasoning** (construct): *correlates*, 6 papers
  > We find that unsurprisingly, math, coding, and reasoning all correlate with one another.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2025/file/9c77f2ce42151b2c2e26d2cf47f99564-Paper-Conference.pdf)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
  - [CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs](https://aclanthology.org/2025.emnlp-main.704.pdf)
  - [Expectation Preference Optimization: Reliable Preference Estimation for Improving the Reasoning Capability of Large Language Models](https://aclanthology.org/2025.emnlp-main.1532.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 4 papers
  > ReEvo couples evolutionary search for efficiently exploring heuristic spaces, with self-reflections to boost the reasoning capabilities of LLMs.
  - [ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ced59d480e07d290b6f29fc8798f195-Paper-Conference.pdf)
  - [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf)
  - [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf)
  - [RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **In-context learning** (construct): *causes*, 4 papers
  > All stages utilize the in-context learning method with a few examples to maximize the reasoning ability of large language models (LLMs). (Section 4)
  - [EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/file/a291dad965af9bc2e39ffeb2ca1c6dc0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
- **Chain-of-thought reasoning** (construct): *causes*, 3 papers
  > Chain-of-Thought (CoT) is an efficient prompting method that enables the reasoning ability of large language models by augmenting the query using multiple examples with multiple intermediate steps. (Abstract)
  - [Training Nonlinear Transformers for Chain-of-Thought Inference: A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf)
  - [Rethinking External Slow-Thinking: From Snowball Errors to Probability of Correct Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gan25a/gan25a.pdf)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **Explanation generation** (behavioral indicator): *causes*, 3 papers
  > Large language models (LLMs) can enhance multi-step reasoning abilities by generating intermediate reasoning steps (i.e., rationale) before arriving at an answer (Wei et al., 2022). (Section 1)
  - [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf)
  - [BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
- **Self-correction** (behavioral indicator): *causes*, 2 papers
  > To the best of our knowledge, we are the first to incorporate a reflection mechanism for self-correction and adaptive KG exploration into KG-augmented LLMs, effectively augmenting the LLM’s reasoning ability. (Section 1)
  - [Plan-on-Graph: Self-Correcting Adaptive Planning of Large Language Model on Knowledge Graphs](https://proceedings.neurips.cc/paper_files/paper/2024/file/4254e856d01a5e7b7ea050477c3ef9b9-Paper-Conference.pdf)
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Information extraction** (behavioral indicator): *causes*, 2 papers
  > The tasks of question decomposition, knowledge extraction, and note-taking are interconnected, each contributing towards navigating the reasoning path from a question to its answer.
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Tool use** (behavioral indicator): *causes*, 2 papers
  > Teaching large language models (LLMs) to use tools for solving complex problems can grant them human-like reasoning abilities. (Abstract)
  - [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf)
  - [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf)
- **Strategy generation** (behavioral indicator): *causes*, 2 papers
  > These S+ and S−guide the generation of new strategies to optimize overall performance, enhancing reasoning ability and avoiding redundancy. (Section 3.1.1)
  - [LLM-guided Plan and Retrieval: A Strategic Alignment for Interpretable User Satisfaction Estimation in Dialogue](https://aclanthology.org/2025.naacl-long.523.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
- **Abstraction** (construct): *causes*, 1 paper
  > Grounding on the high-level concepts and principles, LLMs can leverage their intrinsic Reasoning capabilities to derive the solution. (Section 7)
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > These results consistently demonstrate RISE’s effectiveness in enhancing reasoning capabilities for different models. (Section 1)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Contextual understanding** (construct): *causes*, 1 paper
  > This information with logical relationships enables LLMs to deeply understand the contextual content by clearly perceiving these logical relationships, facilitating the quality and reliability of reasoning (Section 3.2.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Inductive bias** (construct): *causes*, 1 paper
  > MIDAS is not only training-efﬁcient but surprisingly also has an inductive bias towards improving downstream tasks, especially tasks that require reasoning abilities like reading comprehension and math problems, despite having similar or slightly worse perplexity compared to baseline training. (Abstract)
  - [On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf)
- **Image captioning** (behavioral indicator): *causes*, 1 paper
  > Much like humans, who often write down their key observations in an image and refer to them while solving complex reasoning tasks, we hypothesize that grounding the LVLM’s responses in a detailed visual description can significantly enhance its reasoning process. (Section 5)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Multimodal alignment** (construct): *causes*, 1 paper
  > As an early model bridging vision and language with an adaptor, LLaVA’s consistent poor performance highlights how such misalignment can impair both perception and reasoning in such tasks. (Section 4.1)
  - [Are Large Vision Language Models Good Game Players?](https://proceedings.iclr.cc/paper_files/paper/2025/file/27881a19f100fdbf57f0ba1c3d499b08-Paper-Conference.pdf)
- **Video question answering** (behavioral indicator): *causes*, 1 paper
  > Video question answering datasets to enhance TRACE’s reasoning capabilities.
  - [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/df027cf11469e746ef94d583f9f5537f-Paper-Conference.pdf)
- **Plausibility** (construct): *causes*, 1 paper
  > We also observe that guiding models to focus on explanation signals from our dataset during training improves the plausibility Token F1 score by 3-4%, improving the model’s reasoning. (Abstract)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Critique generation** (behavioral indicator): *causes*, 1 paper
  > Additionally, these critiques help the policy language model (LM) correct flawed reasoning steps, resulting in improved accuracy in refined responses.
  - [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **Knowledge acquisition** (construct): *causes*, 1 paper
  > In this study, we introduced TinyThinker to enhance reasoning capabilities through effective knowledge internalization. (Section 6)
  - [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf)
- **Selection bias** (construct): *causes*, 1 paper
  > Such bias compromises fairness, reliability, and the true reasoning capabilities of these models. (Section 1).
  - [Addressing Blind Guessing: Calibration of Selection Bias in Multiple-Choice Question Answering by Video Language Models](https://aclanthology.org/2025.acl-long.162.pdf)
- **Critique ability** (construct): *causes*, 1 paper
  > Self-critique mechanisms significantly improve the performance of language models in complex reasoning tasks by giving them the ability to correct errors, conduct induction and deduction, and switch thinking insights. (Abstract)
  - [Fixing Distribution Shifts of LLM Self-Critique via On-Policy Self-Play Training](https://aclanthology.org/2025.acl-long.865.pdf)
- **Planning** (construct): *causes*, 1 paper
  > This paper presents how language models can be trained for internal and external planning to improve reasoning in sequential decision-making, using board games as an experimental domain. (Section 1)
  - [Mastering Board Games by External and Internal Planning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schultz25a/schultz25a.pdf)
- **Authorship attribution** (behavioral indicator): *correlates*, 1 paper
  > models with stronger reasoning abilities (e.g., o3-mini, Deepseek) according to the benchmark 1, excel at verification and concealing authorial traits
  - [Unraveling Interwoven Roles of Large Language Models in Authorship Privacy: Obfuscation, Mimicking, and Verification](https://aclanthology.org/2025.emnlp-main.753.pdf)
- **Code generation** (behavioral indicator): *causes*, 1 paper
  > mixing code-generation data has been suggested to enhance a model’s reasoning and logical abilities (Dong et al., 2024). (Section 2)
  - [Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality](https://aclanthology.org/2025.emnlp-main.1138.pdf)
- **Language mixing** (behavioral indicator): *causes*, 1 paper
  > We demonstrate that bilingual chain-of-thought reasoning with language mixing causally enhances performance: unconstrained bilingual outputs significantly outperforming monolingually constrained ones (p<0.05), and probe-guided yields further gains. (Introduction)
  - [The Impact of Language Mixing on Bilingual LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1654.pdf)
- **Instruction following ability** (construct): *correlates*, 1 paper
  > we are the first to identify the negative correlation between instruction-following ability and model scale in reasoning tasks: while larger models exhibit stronger reasoning capabilities, their adherence to instructions tends to decline.
  - [DICE: Structured Reasoning in LLMs through SLM-Guided Chain-of-Thought Correction](https://aclanthology.org/2025.emnlp-main.355.pdf)
- **Internal consistency** (construct): *causes*, 1 paper
  > we propose a new approach to calibrate reasoning by up-weighting reasoning paths with high internal consistency, resulting in a significant boost in reasoning performance. (Abstract)
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
- **Representation collapse** (construct): *causes*, 1 paper
  > "representation collapse in the model’s intermediate layers as a key factor limiting their reasoning capabilities"
  - [Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)

### Associated with
- **Mathematical problem solving** (behavioral indicator), 6 papers
  > pipelines that reason about math word problems (Abstract)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
  - [VinePPO: Refining Credit Assignment in RL Training of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kazemnejad25a/kazemnejad25a.pdf)
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
  - [Enhancing Efficiency and Exploration in Reinforcement Learning for LLMs](https://aclanthology.org/2025.emnlp-main.75.pdf)
- **Commonsense reasoning** (construct), 6 papers
  > challenging tasks that rely on the reasoning capabilities of LLMs, such as solving arithmetic problems (Hendrycks et al., 2021) and commonsense reasoning (Talmor et al., 2019) (Section 1).
  - [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf)
  - [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
  - [CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs](https://aclanthology.org/2025.emnlp-main.704.pdf)
  - [Expectation Preference Optimization: Reliable Preference Estimation for Improving the Reasoning Capability of Large Language Models](https://aclanthology.org/2025.emnlp-main.1532.pdf)
  - [ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2025/file/9c77f2ce42151b2c2e26d2cf47f99564-Paper-Conference.pdf)
- **Memorization** (construct), 4 papers
  > It may suggest that width is crucial for memorization, while depth is important for reasoning, a similar phenomenon that echos the intuition of [80] (Section 5).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [Reasoning with Latent Thoughts: On the Power of Looped Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/2676109d49d1eb26d6bc584a8f556305-Paper-Conference.pdf)
  - [RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf)
  - [SSA: Semantic Contamination of LLM-Driven Fake News Detection](https://aclanthology.org/2025.emnlp-main.744.pdf)
- **Visual perception** (construct), 2 papers
  > these reasoning benchmarks require a foundational perception capability to accurately identify key elements. (Section A.3)
  - [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Question answering** (behavioral indicator), 2 papers
  > Our two Knowledge Transfer tasks – Question Answering and Demo Validation – assess whether a model can perform higher-level reasoning about the properties and correctness of a workflow. (Section 4.2)
  - [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Logical reasoning** (construct), 2 papers
  > they discuss reasoning tasks including commonsense reasoning, mathematical reasoning, logical reasoning, and causal reasoning. (Section 2.1)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **General ability** (construct), 2 papers
  > Finally, the identification of a single common factor underlying all benchmark scores suggests that a general ability for reasoning and knowledge can be effectively measured through a consolidated, sparse benchmark. (Section 4)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > Gemma-7B-Instruct performs better in structured tasks like reasoning and coding, where precise instruction-following is crucial (Section 3.1)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
- **Intrinsic self-correction** (behavioral indicator), 1 paper
  > Central to our investigation is the notion of intrinsic self-correction, whereby an LLM attempts to correct its initial responses based solely on its inherent capabilities, without the crutch of external feedback. In the context of reasoning, our research indicates that LLMs struggle to self-correct their responses without external feedback (Section 1).
  - [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf)
- **Perception Test** (measurement instrument), 1 paper
  > The Perception test [45] focused on skills (memory, abstraction, physics, semantics) and types of reasoning (descriptive, explanatory, predictive, counterfactual) across video, audio, and text modalities. (Section 2)
  - [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf)
- **Sequential decision-making** (construct), 1 paper
  > ReAct [23]: This LLM-based planning method integrates reasoning and acting to address sequential decision-making tasks. (Section 4.1.2)
  - [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf)
- **Knowledge-based question answering** (behavioral indicator), 1 paper
  > Given a question, the model is required to make inferences based on necessary reasoning background [14]. (Section 1)
  - [Cost-efficient Knowledge-based Question Answering with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0aafec03d59db29a92fa683bd783374-Paper-Conference.pdf)
- **Reasoning segmentation** (behavioral indicator), 1 paper
  > RS has reasoning ability, but only allows single object localization. (Figure 2)
  - [Instruction-Guided Visual Masking](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4165c96702bac5f4962b70f3cf2f136-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator), 1 paper
  > we reveal that the catastrophic forgetting in MLLMs is primarily due to the decline in instruction following rather than reasoning knowledge.
  - [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Causal reasoning** (construct), 1 paper
  > Reasoning is a cognitive process that involves drawing conclusions, making judgments, or forming inferences based on facts or premises. This process has been explored from various perspectives. ... Causal reasoning [26] focuses on discerning the relationship between a cause and its effect, aiming to understand how certain events can impact other.
  - [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf)
- **Counterfactual reasoning** (construct), 1 paper
  > to evaluate the reasoning abilities of the LLM, it is crucial that this consistency is also observed when the queries are framed in a counterfactual manner.
  - [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator), 1 paper
  > The multiple-choice benchmarks we chose is challenging enough in itself and requires strong reasoning ability from the model; (Section 4.1)
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **Length generalization** (construct), 1 paper
  > Length generalization (LG) is a challenging problem in learning to reason. (ABSTRACT)
  - [Generalizing Reasoning Problems to Longer Lengths](https://proceedings.iclr.cc/paper_files/paper/2025/file/abcbdf504b621b4d1213aa7a5c489f8a-Paper-Conference.pdf)
- **Question decomposition** (behavioral indicator), 1 paper
  > WebPlanner first decomposes the user question into sequential or parallel search tasks via reasoning on the graph and determines the next step based on the search feedback (Sec. 2.1).
  - [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://proceedings.iclr.cc/paper_files/paper/2025/file/e01c431bbb83153632c0dcfaf8ccda0a-Paper-Conference.pdf)
- **Human preference alignment** (construct), 1 paper
  > With the bidirectional negative feedback, our proposed BNF can naturally prevent the model from over-fitting to preference data, striking a better balance between human values and reasoning ability while minimizing the alignment tax.
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Alignment tax** (construct), 1 paper
  > Recent studies (Ouyang et al., 2022; Lin et al., 2023) have shown that using preference optimization methods to align LLMs with human values often harms their reasoning ability, referred to as the alignment tax.
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Reasoning error** (behavioral indicator), 1 paper
  > “Reasoning Errors ... account for a significant portion of mistakes... suggesting that even when models correctly perceive the audio, they often fail to apply the necessary complex reasoning.”
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Long-context understanding** (construct), 1 paper
  > The research community increasingly recognizes long-context modeling as a crucial capability for next-generation large language models, driven by diverse real-world applications ranging from in-depth reasoning (DeepSeek-AI, 2025; Zelikman et al., 2022)... (Introduction).
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
- **Abstract reasoning** (construct), 1 paper
  > abstract reasoning involves two core processes: abstraction, the extraction of common features from concrete entities (Murphy, 2004), and reasoning, the derivation of new knowledge from existing information (Holyoak & Morrison, 2012).
  - [Benchmarking Abstract and Reasoning Abilities Through A Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25u/ma25u.pdf)
- **Formal theorem proving** (behavioral indicator), 1 paper
  > Automated theorem proving with formal languages by LLMs stands at the forefront of reasoning research (Yang et al., 2024a), partly because it allows objective and reliable evaluation... Moreover, it arguably encapsulates the essence of advanced reasoning tasks while abstracting away the ambiguity of natural language, enabling meaningful studies on a relatively smaller scale. (Section 1)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **Tool use ability** (construct), 1 paper
  > LLMs must first comprehend the user’s query and perform a reasonable analysis and planning, demonstrating the ability of reasoning. Subsequently, it needs to invoke the correct functions with suitable parameters, reflecting the ability of execution.
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)
- **Social intelligence** (construct), 1 paper
  > However, it remains unclear whether these reasoning capabilities extend to a form of social intelligence: making effective decisions in cooperative contexts. (Abstract)
  - [Spontaneous Giving and Calculated Greed in Language Models](https://aclanthology.org/2025.emnlp-main.267.pdf)
- **Confidence estimation** (behavioral indicator), 1 paper
  > "we propose a set of training-free, graph-based confidence estimation methods tailored to reasoning tasks."
  - [All Roads Lead to Rome: Graph-Based Confidence Estimation for Large Language Model Reasoning](https://aclanthology.org/2025.emnlp-main.1620.pdf)
- **Linguistic puzzle generation** (behavioral indicator), 1 paper
  > the generated puzzles are designed to challenge students’ genuine reasoning and pattern detection, minimizing reliance on external language knowledge.
  - [Can LLMs Generate and Solve Linguistic Olympiad Puzzles?](https://aclanthology.org/2025.emnlp-main.969.pdf)
- **Reasoning faithfulness** (construct), 1 paper
  > This question [Do LRMs actually leverage the reasoning tokens to generate answers?] is closely tied to active research areas including reasoning effectiveness (Ma et al., 2025), reasoning faithfulness (Chen et al., 2025), and model behavior monitoring (Baker et al., 2025). (Section 1)
  - [From Reasoning to Answer: Empirical, Attention-Based and Mechanistic Insights into Distilled DeepSeek R1 Models](https://aclanthology.org/2025.emnlp-main.198.pdf)
- **Natural language inference** (behavioral indicator), 1 paper
  > notably NLI tasks, which require integrating knowledge and reasoning. (Section 1)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Multi-hop question answering** (behavioral indicator), 1 paper
  > we can increase the complexity of a question by making it a multi-hop question [23, 24], which can be used to test whether an LLM can think in multiple steps. (Section 3.3)
  - [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5ef9853a6cdea40ae3e301a6d8dc32b5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Query rewriting** (behavioral indicator), 1 paper
  > We find that utilizing the reasoning ability of large language models (LLMs) to rephrase the search query and extend the aesthetic expectations can make up for this shortcoming. (Abstract)
  - [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf)
- **UltraInteract** (measurement instrument), 1 paper
  > "We consider fine-tuning Mistral-7B and Mistral-8×7B models on UltraInteract [44], a pairwise alignment dataset specifically designed for complex reasoning tasks."
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
- **Knowledge integration** (construct), 1 paper
  > According to Chen et al. (2024), the realization of reasoning ability hinges on two core components: (1) possessing extensive general knowledge of the world, and (2) effectively integrating new information into an existing knowledge base. (Section 2)
  - [KOR-Bench: Benchmarking Language Models on Knowledge-Orthogonal Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/c6f5851a0d9cb435ed8b50e87bd6a257-Paper-Conference.pdf)
- **Multi-operand addition** (behavioral indicator), 1 paper
  > The illustrative reasoning tasks we consider are: n-ary addition, p-hop induction head that tests the model’s ability to track back for p steps, and i-GSM which consists of synthetically constructed grade-school math problems (Section 2).
  - [Reasoning with Latent Thoughts: On the Power of Looped Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/2676109d49d1eb26d6bc584a8f556305-Paper-Conference.pdf)
- **Synthetic data detection** (behavioral indicator), 1 paper
  > the task of distinguishing between real and synthetic data effectively tests the perception, knowledge, and reasoning capabilities of LMMs. (ABSTRACT)
  - [LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afd6374c7f2839cba22f537f15f4f760-Paper-Conference.pdf)
- **Faithfulness** (construct), 1 paper
  > Faithfulness serves as a metric for evaluating the degree to which the model’s provided explanation aligns with its actual reasoning. (Section 6.1)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Natural language understanding** (construct), 1 paper
  > recent studies indicate that the language understanding offered by these models remains limited and far from human-like performance, particularly in grasping the contextual meanings of words—an essential aspect of reasoning. (Abstract)
  - [SANDWiCH: Semantical Analysis of Neighbours for Disambiguating Words in Context ad Hoc](https://aclanthology.org/2025.naacl-long.358.pdf)
- **Transitive reasoning** (construct), 1 paper
  > TI is a fundamental form of reasoning in which, given some premises, a relational conclusion between stimuli can be inferred. For example, if A is greater than B and B is greater than C, then A must, transitively, be greater than C. TI has historically been used to evaluate the reasoning ability of young pre-verbal children (Burt et al., 1911), but has also been well studied throughout the animal kingdom, from rats (Roberts & Phelps, 1994) to wasps (Tibbetts et al., 2019).
  - [Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf)
- **Self-verification** (behavioral indicator), 1 paper
  > “The core idea of ReVISE is to enable LLMs to verify their reasoning processes”
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Calibration** (construct), 1 paper
  > “program-aided reasoning approaches, where LLMs utilize code representation, generally exhibit superior calibration compared to standard text-based reasoning methods that rely on CoT”
  - [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf)
- **Chart question answering** (behavioral indicator), 1 paper
  > "Chart question answering (CQA) has become a critical multimodal task for evaluating the reasoning capabilities of vision-language models."
  - [ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering](https://aclanthology.org/2025.emnlp-main.226.pdf)
