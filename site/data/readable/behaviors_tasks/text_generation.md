# Text generation
**Type:** Behavioral indicator  
**Supporting papers:** 596  
**Also known as:** Response generation, Open-ended generation, Writing, Natural language generation, Completion generation, Free-form response generation, Language generation, Sequence generation, Single-turn dialogue generation, Autoregressive generation, Instruction response generation, Single-turn dialogue, Content generation, Movie review generation, Text-to-text generation, Diary writing, Context completion, Single-turn conversation, Book review generation, Draft generation, Free generation, Token generation, Conversation simulation, Blog post writing, Email writing, Culture-conditioned generation, LaTeX document generation, Slogan generation, State description generation, Twitter post generation, Generative language modeling, Surface realization, Inference steering, Email completion, Chat response generation, Open-ended reasoning, Argumentative writing, Cover letter writing, Expository writing, Legal Document Writing, Speech drafting, Fictitious knowledge generation, Long structured output generation, Research paper generation, Arbitrary-length sequence generation, Unconditional generation, Document creation, Cognitive reappraisal generation, Concept-conditioned generation, Development document generation, Editing instruction generation, Random word generation, Token string generation, Verbal response generation, Watermark description generation, Paper writing, Guided generation, Token-by-token generation, Argument composition, Advice generation, Cover letter generation, Culturally appropriate response generation, Reference letter generation, Title generation, Video scriptwriting, Academic writing, Professional writing, Final response generation, Free-text response generation, Model generation, Natural language response generation, Open-ended response generation, Completion, Bidirectional text continuation, Free-text generation, Sentence generation, Human-content continuation, Essay generation, Smart reply generation, Generation, Free-form text completion, Free-form text generation, Free-form Text Generation, Open-ended text generation, Unconditional text generation, Open-response generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is producing coherent, contextually appropriate natural-language sequences or responses from a prompt, instruction, query, prefix, or dialogue history, often through autoregressive, token-by-token decoding. A recurring formulation is continuation, for example taking an initial span of tokens and generating the next segment, or sampling an output string response conditioned on the input. Papers broadly agree on this behavior, but differ on whether they present it as open-ended free-form generation or include constrained cases such as paraphrasing, classification-style outputs, or task-specific completions, and they vary in whether success is tied to reference similarity, fluency and coherence, or usefulness and alignment with preferences.

**Variants.** The most common variant names are response generation, open-ended generation, natural language generation, language generation, and text completion. Many papers also place it in dialogue settings, especially single-turn interaction, and in multimodal settings where interleaved images and text lead to text completions, captions, answers, or descriptions. Smaller lines of work study specialized writing forms, such as emails, reviews, essays, and formal documents, or isolate token-level and prompt-free settings such as token generation, autoregressive generation, unconditional generation, and free generation.

**Space of elicitation and scores.** Papers measure it with 39 instruments. The most frequently linked instruments are WikiText-2, MT-Bench, E2E NLG Challenge, LLM-as-a-judge, and TruthfulQA. Across papers, these instruments include perplexity-based language-modeling benchmarks, open-ended chat and writing benchmarks, task datasets for question answering or data-to-text generation, and judge-based evaluation by larger models or human annotators, with scoring reported through measures such as perplexity, exact match, ROUGE-L or METEOR, win-rate, and model or human judgments.

**What it is taken as evidence of.** Papers link text generation to 15 constructs. The most frequent links are to Text generation quality, Alignment, Coherence, Cultural bias, and Generalization. There is no single agreed construct that it is taken to reflect here: the prevailing pattern is that papers report it as related to several broad qualities, rather than treating it as evidence of one construct alone.

## Sources

**Text generation** (54 papers: [A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf), [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf), [Are Bert Family Good Instruction Followers? A Study on Their Potential And Limitations](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a13eb0c08247364066e8d86551c3090-Paper-Conference.pdf), [BESA: Pruning Large Language Models with Blockwise Parameter-Efficient Sparsity Allocation](https://proceedings.iclr.cc/paper_files/paper/2024/file/21e315d40ac1db66c80c78e86a447ca1-Paper-Conference.pdf), [Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf), [DataInf: Efficiently Estimating Data Influence in LoRA-tuned LLMs and Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e84a0f233611a1dc8fb794dc52415a3-Paper-Conference.pdf), [Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy](https://proceedings.iclr.cc/paper_files/paper/2024/file/e537e071277a2e5fefaa78f87500c7b4-Paper-Conference.pdf), [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf), [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf), [Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf), [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf), [Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing](https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf), [HyperAttention: Long-context Attention in Near-Linear Time](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5aa940590399350401c57cdf52ce78-Paper-Conference.pdf), [Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f5c76187c28e8d9d3b938d0c504436c-Paper-Conference.pdf), [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf), [Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf), [Language Model Detectors Are Easily Optimized Against](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f9f07df0992ce21698d800eaa891bd8-Paper-Conference.pdf), [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf), [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf), [MUFFIN: Curating Multi-Faceted Instructions for Improving Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d1a0188e18c1d74a0f8d6eb5ecede4f-Paper-Conference.pdf), [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf), [MiniLLM: Knowledge Distillation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/8ac015d409635f196f9e3e9dcfb9a94e-Paper-Conference.pdf), [Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/639a9a172c044fbb64175b5fad42e9a5-Paper-Conference.pdf), [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf), [Provable Robust Watermarking for AI-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/beae9ed5316bcc48e616754c06c11875-Paper-Conference.pdf), [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf), [SliceGPT: Compress Large Language Models by Deleting Rows and Columns](https://proceedings.iclr.cc/paper_files/paper/2024/file/316648eb8b4ffb6010f531b07848c300-Paper-Conference.pdf), [Test-Time Training on Nearest Neighbors for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f02f1185b97518ab5bd7ebde466992d3-Paper-Conference.pdf), [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf), [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf), [Towards Codable Watermarking for Injecting Multi-Bits Information to LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/abdc8c031aa6c6917c3b593166e5e340-Paper-Conference.pdf), [Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b054fadf1ccd80b37d465f6082629934-Paper-Conference.pdf), [Unbiased Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c5b00c5bdcc6fe35907dbcca03d27652-Paper-Conference.pdf), [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf), [Vanishing Gradients in Reinforcement Finetuning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b09bb02b90584e2be94ff3ae09289bc-Paper-Conference.pdf), [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf), [PEARL: Parallel Speculative Decoding with Adaptive Draft Length](https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf), [Mamba-Shedder: Post-Transformer Compression for Efficient Selective Structured State Space Models](https://aclanthology.org/2025.naacl-long.195.pdf), [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.113.pdf), [TurkingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.188.pdf), [Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque](https://aclanthology.org/2025.naacl-long.629.pdf), [Waste Not, Want Not; Recycled Gumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.292.pdf), [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf), [Probe-Free Low-Rank Activation Intervention](https://aclanthology.org/2025.naacl-long.143.pdf), [Is Your LLM Outdated? A Deep Look at Temporal Generalization](https://aclanthology.org/2025.naacl-long.381.pdf), [Matina: A Large-Scale 73B Token Persian Text Corpus](https://aclanthology.org/2025.naacl-long.462.pdf), [A Survey of NLP Progress in Sino-Tibetan Low-Resource Languages](https://aclanthology.org/2025.naacl-long.396.pdf), [Bayelemabaga: Creating Resources for Bambara NLP](https://aclanthology.org/2025.naacl-long.602.pdf), [FiNE: Filtering and Improving Noisy Data Elaborately with Large Language Models](https://aclanthology.org/2025.naacl-long.437.pdf), [PromptRefine: Enhancing Few-Shot Performance on Low-Resource Indic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.17.pdf), [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf), [Intuitive Fine-Tuning: Towards Simplifying Alignment into a Single Process](https://aclanthology.org/2025.acl-long.6.pdf), [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abnar25a/abnar25a.pdf), [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf))
> Producing coherent and contextually appropriate text sequences in response to input prompts, including both open-ended and constrained generation.

**Response generation** (11 papers: [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf), [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf), [UniICL: An Efficient ICL Framework Unifying Compression, Selection, and Generation](https://aclanthology.org/2025.acl-long.24.pdf), [PILAF: Optimal Human Preference Sampling for Reward Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25g/feng25g.pdf), [MultiAgentESC: A LLM-based Multi-Agent Collaboration Framework for Emotional Support Conversation](https://aclanthology.org/2025.emnlp-main.232.pdf), [Let Models Speak Ciphers: Multiagent Debate through Embeddings](https://proceedings.iclr.cc/paper_files/paper/2024/file/e444859b2a22df6b56af9381ad1e9480-Paper-Conference.pdf), [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf), [Peering Through Preferences: Unraveling Feedback Acquisition for Aligning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/48a4f41ff000b121eabe7b2491b24aef-Paper-Conference.pdf), [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf), [MADial-Bench: Towards Real-world Evaluation of Memory-Augmented Dialogue Generation](https://aclanthology.org/2025.naacl-long.499.pdf), [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf))
> Producing a natural-language answer or continuation to a user prompt in an assistant setting.

**Open-ended generation** (3 papers: [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf), [Taming Overconfidence in LLMs: Reward Calibration in RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/29fb6e1456b3d8b57ede5c45aa2c6537-Paper-Conference.pdf), [SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.112.pdf))
> Producing free-form text responses to prompts or questions without choosing from fixed answer options.

**Writing** (1 paper: [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf))
> The observable task of generating coherent text content, categorized within MT-Bench.

**Natural language generation** (10 papers: [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf), [RandLoRA: Full rank parameter-efficient fine-tuning of large models](https://proceedings.iclr.cc/paper_files/paper/2025/file/382b95a6580cfb0b5ca33c74b4e0e770-Paper-Conference.pdf), [FedEx-LoRA: Exact Aggregation for Federated and Efficient Fine-Tuning of Large Language Models](https://aclanthology.org/2025.acl-long.67.pdf), [Scalable Model Merging with Progressive Layer-wise Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25r/xu25r.pdf), [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf), [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf), [OctoPack: Instruction Tuning Code Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1ec299a5229034141e58aeded0d0b9de-Paper-Conference.pdf), [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf), [Prototype Conditioned Generative Replay for Continual Learning in NLP](https://aclanthology.org/2025.naacl-long.636.pdf), [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf))
> The general task of producing free-form text in a human language.

**Completion generation** (1 paper: [A Critical Evaluation of AI Feedback for Aligning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/33870b3e099880cd8e705cd07173ac27-Paper-Conference.pdf))
> Producing a sequence of tokens as a response to an input dialogue history or instruction.

**Free-form response generation** (3 papers: [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf), [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf), [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf))
> The observable behavior of generating open-ended, natural language answers to questions, as opposed to selecting from a fixed set of options or producing a single word.

**Text completion** (2 papers: [BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc808cf2d2444b0abcceca366b771389-Paper-Conference.pdf), [Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/18fd48d9cbbf9a20e434c9d3db6973c5-Paper-Conference.pdf))
> Generating the remainder of a text from a provided prefix, optionally conditioned on additional guidance.

**Language generation** (9 papers: [Selective Generation for Controllable Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a6815122f533193a022cbc41786c1cc-Paper-Conference.pdf), [Glauber Generative Model: Discrete Diffusion Models via Binary Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/125be378b39b10676f56e12e6923b902-Paper-Conference.pdf), [SKIM: Any-bit Quantization Pushing The Limits of Post-Training Quantization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25c/bai25c.pdf), [Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.57.pdf), [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf), [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf), [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf), [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf))
> The task of producing a sequence of tokens, such as a sentence or paragraph, in response to an input prompt.

**Free-form generation** (5 papers: [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf), [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf), [Robust Multimodal Large Language Models Against Modality Conflict](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25dq/zhang25dq.pdf), [In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1208.pdf), [Benchmarking and Improving Generator-Validator Consistency of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfcb583d225b1db8d3ca2331f6785774-Paper-Conference.pdf))
> The task of generating an unconstrained natural language response to a prompt or question.

**Sequence generation** (1 paper: [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf))
> The observable behavior of producing a complete sequence of tokens, such as a sentence or paragraph, in an autoregressive manner.

**Single-turn dialogue generation** (2 papers: [BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling](https://proceedings.neurips.cc/paper_files/paper/2024/file/056521a35eacd9d2127b66a7d3c499c5-Paper-Conference.pdf), [EmoCharacter: Evaluating the Emotional Fidelity of Role-Playing Agents in Dialogues](https://aclanthology.org/2025.naacl-long.316.pdf))
> The task of generating a single, coherent, and relevant response to a user's prompt in a conversational context.

**Autoregressive generation** (6 papers: [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf), [Ask, and it shall be given: On the Turing completeness of prompting](https://proceedings.iclr.cc/paper_files/paper/2025/file/123d3e814e257e0781e5d328232ead9b-Paper-Conference.pdf), [IIET: Efficient Numerical Transformer via Implicit Iterative Euler Method](https://aclanthology.org/2025.emnlp-main.453.pdf), [KV-Latent: Dimensional-level KV Cache Reduction with Frequency-aware Rotary Positional Embedding](https://aclanthology.org/2025.acl-long.77.pdf), [Retrofitting Large Language Models with Dynamic Tokenization](https://aclanthology.org/2025.acl-long.1444.pdf), [Language Modeling Is Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/3cbf627fa24fb6cb576e04e689b9428b-Paper-Conference.pdf))
> The process of generating text token by token, where each new token is predicted based on the sequence of previously generated tokens.

**Instruction response generation** (1 paper: [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf))
> Generating responses to user instructions or prompts in an instruction-tuned dialogue setting.

**Single-turn dialogue** (2 papers: [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf), [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf))
> Responding to a single user prompt or question in a self-contained manner without prior conversational context.

**Content generation** (1 paper: [Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf))
> The observable task of producing new text based on a given prompt or context.

**Movie review generation** (1 paper: [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf))
> The specific task of generating text that constitutes a movie review, often with a specified sentiment.

**Diary writing** (1 paper: [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf))
> The specific task of generating a sequence of dated entries that describe events over a period of time.

**Text-to-text generation** (2 papers: [LiFT: Learning to Fine-Tune via Bayesian Parameter Efficient Meta Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/27e5626cabdbb6cd5c56ce4114ff93e4-Paper-Conference.pdf), [Modeling Multi-Task Model Merging as Adaptive Projective Gradient Descent](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25k/wei25k.pdf))
> The task of generating a textual output based on a textual input, encompassing various NLP tasks in a unified format.

**Draft generation** (1 paper: [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf))
> Producing candidate answers from a subset of retrieved documents before verification.

**Conversation simulation** (1 paper: [Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf))
> The act of generating plausible future turns of a conversation to evaluate the potential outcomes of different responses.

**Email writing** (2 papers: [Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf), [Aligning LLMs by Predicting Preferences from User Writing Samples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aroca-ouellette25a/aroca-ouellette25a.pdf))
> The observable task of generating the text for an email based on a given prompt or scenario.

**Blog post writing** (1 paper: [Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf))
> The observable task of generating text in the style and format of a blog post.

**Text continuation** (2 papers: [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf), [Unsupervised Hallucination Detection by Inspecting Reasoning Processes](https://aclanthology.org/2025.emnlp-main.1124.pdf))
> Generating the continuation of a given context, evaluating the model's ability to generate coherent text without introducing bias.

**Token generation** (8 papers: [SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b0a8df568ec496a717566a7f8158aaa-Paper-Conference.pdf), [Attention-Level Speculation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cai25g/cai25g.pdf), [Speculative Safety-Aware Decoding](https://aclanthology.org/2025.emnlp-main.648.pdf), [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://aclanthology.org/2025.acl-long.1369.pdf), [Nudging: Inference-time Alignment of LLMs via Guided Decoding](https://aclanthology.org/2025.acl-long.623.pdf), [Scaling Laws and Efficient Inference for Ternary Language Models](https://aclanthology.org/2025.acl-long.1294.pdf), [Unveiling Environmental Impacts of Large Language Model Serving: A Functional Unit View](https://aclanthology.org/2025.acl-long.519.pdf), [Amphista: Bi-directional Multi-head Decoding for Accelerating LLM Inference](https://aclanthology.org/2025.naacl-long.450.pdf))
> The observable process of producing output tokens sequentially during the decoding phase of inference.

**Single-turn conversation** (3 papers: [Is In-Context Learning Sufficient for Instruction Following in LLMs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/41623b137cd34807f56028aa9f6f84a7-Paper-Conference.pdf), [Energy-Based Preference Model Offers Better Offline Alignment than the Bradley-Terry Preference Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25i/hong25i.pdf), [Navigating the Cultural Kaleidoscope: A Hitchhiker's Guide to Sensitivity in Large Language Models](https://aclanthology.org/2025.naacl-long.388.pdf))
> An observable interaction where the model receives a single user query and generates a single response to complete the task.

**Book review generation** (1 paper: [Generative Monoculture in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf))
> The observable task of producing text reviews for specific book titles, evaluated for sentiment, topic, and wording diversity.

**Context completion** (1 paper: [HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf))
> The observable task of completing a given text prompt or context in a coherent and plausible manner.

**Free generation** (2 papers: [A Percolation Model of Emergence: Analyzing Transformers Trained on a Formal Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/5cd2b0a6b7423af6369cbdbbb228e8d0-Paper-Conference.pdf), [Analyzing (In)Abilities of SAEs via Formal Languages](https://aclanthology.org/2025.naacl-long.249.pdf))
> The task of producing a valid string from the formal language that respects both grammar and type constraints, without any specific input prompt.

**Generative language modeling** (1 paper: [Sparse Learning for State Space Models on Mobile](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf))
> The observable task of producing coherent and contextually relevant text following an initial prompt.

**LaTeX document generation** (1 paper: [Flow: Modularized Agentic Workflow Automation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba84da6921f3040b74ee163aa7451f53-Paper-Conference.pdf))
> The specific task of creating a compilable LaTeX document, such as a Beamer presentation, based on content and formatting requirements.

**Slogan generation** (1 paper: [3D-Properties: Identifying Challenges in DPO and Charting a Path Forward](https://proceedings.iclr.cc/paper_files/paper/2025/file/c080f9fb3658511bc4f063c5794ef706-Paper-Conference.pdf))
> The task of creating a concise and impactful slogan based on a prompt, often with constraints on word count and content.

**Surface realization** (1 paper: [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf))
> The process of translating a high-level plan, such as pseudocode, into a detailed, final natural language response.

**Inference steering** (1 paper: [Uncovering Gaps in How Humans and LLMs Interpret Subjective Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362fbc0d182c6b4b8dadb90177239e4-Paper-Conference.pdf))
> The observable task of generating an output that is shaped by a subjective phrase included directly in the user's prompt.

**Culture-conditioned generation** (1 paper: [Attributing Culture-Conditioned Generations to Pretraining Corpora](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4546b4f9e1a44ed15c253dd43307dd5-Paper-Conference.pdf))
> Producing open-ended text (e.g., narrative, dialogue) conditioned on a specific cultural context.

**Twitter post generation** (1 paper: [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf))
> Writing a social-media style post that describes the content of an image or video.

**State description generation** (1 paper: [Language Guided Skill Discovery](https://proceedings.iclr.cc/paper_files/paper/2025/file/dae30ba63ca043588cdf804bbba295ed-Paper-Conference.pdf))
> The observable action of an LLM producing a natural language description for a given agent state, based on a user-provided prompt.

**Legal Document Writing** (1 paper: [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf))
> The observable behavior of generating formal text adhering to legal standards and logical structures.

**Open-ended reasoning** (1 paper: [KBLaM: Knowledge Base augmented Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf))
> The observable task of responding to a query that requires generating a more elaborate or inferential answer beyond simple fact retrieval.

**Expository writing** (1 paper: [Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf))
> The task of generating text that explains, informs, or describes facts, such as tutorials, encyclopedia entries, or news articles.

**Argumentative writing** (1 paper: [Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf))
> Generating text to compare views, judge, or persuade, such as movie reviews or essays.

**Email completion** (1 paper: [Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf))
> The task of generating coherent and contextually appropriate continuations for a given email prompt, used to measure model utility.

**Cover letter writing** (1 paper: [First-Person Fairness in Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/92af0c8c2664429de2bb44c2692d84ae-Paper-Conference.pdf))
> Generating a cover letter for a user as part of employment-related assistance.

**Chat response generation** (2 papers: [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf), [Beyond Bradley-Terry Models: A General Preference Model for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25de/zhang25de.pdf))
> Producing answers to conversational prompts, often evaluated by sampling multiple candidate replies.

**Speech drafting** (1 paper: [AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf))
> The task of generating the text for a speech, often prompted with an initial sentence from a famous historical speech.

**Fictitious knowledge generation** (1 paper: [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf))
> The task of generating responses based on synthetic, non-factual information about fictional entities.

**Research paper generation** (1 paper: [CycleResearcher: Improving Automated Research via Automated Review](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a48036026dc7946ef6033ae14719cc5-Paper-Conference.pdf))
> The observable task of producing a complete academic paper in a structured format, including sections like abstract, introduction, methods, and results.

**Long structured output generation** (1 paper: [Are Large Vision Language Models Good Game Players?](https://proceedings.iclr.cc/paper_files/paper/2025/file/27881a19f100fdbf57f0ba1c3d499b08-Paper-Conference.pdf))
> Producing extended structured responses such as matrices or move sequences without format breakdowns.

**Arbitrary-length sequence generation** (1 paper: [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf))
> Generating text sequences whose length can continue until an end-of-sequence token or degradation criterion is reached.

**Unconditional generation** (3 papers: [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf), [Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/5dc6d1c81754c32008c9667339b3fdd3-Paper-Conference.pdf), [When Do Prompting and Prefix-Tuning Work? A Theory of Capabilities and Limitations](https://proceedings.iclr.cc/paper_files/paper/2024/file/18a367688479c1b08b001584218a4443-Paper-Conference.pdf))
> Generating text without a conditioning prompt or task-specific input.

**Verbal response generation** (1 paper: [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25d/shi25d.pdf))
> Producing natural language utterances, such as confirmations or clarifications, in response to user prompts or during task execution.

**Watermark description generation** (1 paper: [WMarkGPT: Watermarked Image Understanding via Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25f/tan25f.pdf))
> The observable task of producing a natural language text that describes a watermark's characteristics, such as its location, content, appearance, and its interaction with the main image content.

**Token string generation** (1 paper: [Language Models over Canonical Byte-Pair Encodings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vieira25b/vieira25b.pdf))
> The autoregressive production of sequences of tokens by a language model, which may result in either canonical or noncanonical encodings of character strings.

**Concept-conditioned generation** (1 paper: [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf))
> Generating text that is explicitly guided to include a specified concept or topic.

**Document creation** (1 paper: [CollabLLM: From Passive Responders to Active Collaborators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25i/wu25i.pdf))
> The model helps produce or revise a written document across multiple turns, such as a blog post, creative writing piece, or personal statement.

**Paper writing** (1 paper: [ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf))
> Generating a paper-like research output from researcher and paper context in a structured format.

**Editing instruction generation** (1 paper: [CAD-Editor: A Locate-then-Infill Framework with Automated Training Data Synthesis for Text-Based CAD Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25g/yuan25g.pdf))
> Generating a textual instruction that summarizes the differences between paired CAD models.

**Cognitive reappraisal generation** (1 paper: [SPRI: Aligning Large Language Models with Context-Situated Principles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhan25a/zhan25a.pdf))
> The task of generating text that reframes an emotionally charged situation to alter its emotional impact, a strategy used in psychology.

**Random word generation** (1 paper: [Hardware and Software Platform Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25u/zhang25u.pdf))
> The task of producing a sequence of random words as prompted by a user, used to generate diverse logit distributions for analysis.

**Development document generation** (1 paper: [Synthesizing Software Engineering Data in a Test-Driven Manner](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cn/zhang25cn.pdf))
> Using an LLM to generate detailed task descriptions or requirement documents from unit test content.

**Guided generation** (1 paper: [Large Language Models to Diffusion Finetuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cetin25a/cetin25a.pdf))
> Conditioning output generation on external task-specific signals to improve performance in targeted domains.

**Token-by-token generation** (1 paper: [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf))
> Autoregressive production of text one token at a time, used in standard language modeling evaluation settings.

**Culturally appropriate response generation** (1 paper: [Position: Beyond Assistance – Reimagining LLMs as Ethical and Adaptive Co-Creators in Mental Health Care](https://raw.githubusercontent.com/mlresearch/v267/main/assets/badawi25a/badawi25a.pdf))
> Generating mental health responses that respect and reflect the user's cultural background, avoiding stereotypes and offering relevant, non-biased advice.

**Cover letter generation** (1 paper: [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf))
> Writing a professional cover letter for a job applicant, used to assess whether the quality of writing varies by the applicant's gender.

**Reference letter generation** (2 papers: [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf), [White Men Lead, Black Women Help? Benchmarking and Mitigating Language Agency Social Biases in LLMs](https://aclanthology.org/2025.acl-long.445.pdf))
> Writing a recommendation letter for a student or job candidate, used to evaluate whether the strength of endorsement varies by gender.

**Professional writing** (1 paper: [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf))
> Creating formal documents such as resumes, cover letters, performance reviews, and job descriptions that influence professional evaluation and opportunity allocation.

**Argument composition** (1 paper: [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf))
> Constructing persuasive or critical analyses, such as essay outlines, hypothetical answers, or debate points.

**Academic writing** (1 paper: [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf))
> The task of generating content for educational or research purposes, such as explanations, study plans, literature reviews, and informational articles.

**Advice generation** (1 paper: [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf))
> Producing guidance or recommendations in response to personal or situational queries, such as life advice or problem-solving suggestions.

**Title generation** (1 paper: [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf))
> Producing short, creative textual elements such as product names, hashtags, slogans, or article headings.

**Video scriptwriting** (1 paper: [Position: AI Scaling: From Up to Down and Out](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25fh/wang25fh.pdf))
> Generating narrative or instructional scripts for video content based on creative or contextual prompts.

**Free-text response generation** (1 paper: [ActionStudio: A Lightweight Framework for Data and Training of Large Action Models](https://aclanthology.org/2025.emnlp-main.1090.pdf))
> Producing natural language responses that are contextually appropriate and accurate in agent interactions, particularly in business or CRM settings.

**Final response generation** (1 paper: [Learning to Ask: When LLM Agents Meet Unclear Instruction](https://aclanthology.org/2025.emnlp-main.1104.pdf))
> The act of producing the concluding answer or output for the user after completing all necessary intermediate steps like tool use.

**Model generation** (1 paper: [pFedGPT: Hierarchically Optimizing LoRA Aggregation Weights for Personalized Federated GPT Models](https://aclanthology.org/2025.emnlp-main.239.pdf))
> The observable production of text-based outputs in response to prompts, which is the primary behavior evaluated across various NLP tasks.

**Natural language response generation** (1 paper: [DICE: Structured Reasoning in LLMs through SLM-Guided Chain-of-Thought Correction](https://aclanthology.org/2025.emnlp-main.355.pdf))
> The task of producing unstructured, human-readable text in response to a prompt.

**Open-ended response generation** (3 papers: [STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models](https://aclanthology.org/2025.emnlp-main.925.pdf), [Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models](https://aclanthology.org/2025.acl-long.1529.pdf), [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.617.pdf))
> Generating free-form responses to instructions that reflect a particular community's viewpoint.

**Completion** (1 paper: [The Impact of Negated Text on Hallucination with Large Language Models](https://aclanthology.org/2025.emnlp-main.684.pdf))
> The task of continuing a given text prompt to produce a coherent and contextually relevant extension.

**Bidirectional text continuation** (1 paper: [Transplant Then Regenerate: A New Paradigm for Text Data Augmentation](https://aclanthology.org/2025.emnlp-main.702.pdf))
> The process of generating text both before (backward continuation) and after (forward continuation) a given seed text to create a surrounding context.

**Sentence generation** (1 paper: [SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1039.pdf))
> Producing natural language sentences that include specified event triggers and align with a target domain's linguistic patterns.

**Free-text generation** (1 paper: [LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences in LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1045.pdf))
> The observable behavior of producing open-ended textual outputs without constrained options, used as a task format in reasoning evaluations.

**Essay generation** (2 papers: [OpenTuringBench: An Open-Model-based Benchmark and Framework for Machine-Generated Text Detection and Attribution](https://aclanthology.org/2025.emnlp-main.1354.pdf), [Do Large Language Models have an English Accent? Evaluating and Improving the Naturalness of Multilingual LLMs](https://aclanthology.org/2025.acl-long.193.pdf))
> Producing long-form, coherent essays in a domain different from the training data (news), used to test out-of-domain generalization.

**Human-content continuation** (1 paper: [OpenTuringBench: An Open-Model-based Benchmark and Framework for Machine-Generated Text Detection and Attribution](https://aclanthology.org/2025.emnlp-main.1354.pdf))
> Machine models continuing human-authored text, creating blended content that challenges detection systems.

**Smart reply generation** (1 paper: [HydraOpt: Navigating the Efficiency-Performance Trade-off of Adapter Merging](https://aclanthology.org/2025.emnlp-main.1365.pdf))
> Generating a relevant and concise response to a given textual message.

**Generation** (1 paper: [QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models](https://aclanthology.org/2025.emnlp-main.271.pdf))
> Producing free-form text outputs in response to an input prompt.

**Free-form text completion** (1 paper: [Job Unfair: An Investigation of Gender and Occupational Bias in Free-Form Text Completions by LLMs](https://aclanthology.org/2025.emnlp-main.1159.pdf))
> Generating open-ended continuations of partial sentences, particularly those involving occupational roles and gendered or gender-neutral prompts.

**Free-form text generation** (1 paper: [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf))
> Generating open-ended natural language responses to prompts rather than selecting from fixed options.

**Free-form Text Generation** (1 paper: [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf))
> Generating text responses without fixed options, involving an extensive range of potential responses.

**Open-ended text generation** (14 papers: [Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf), [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf), [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf), [Language Model Decoding as Direct Metrics Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf), [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf), [Differentially Private Steering for Large Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45326c2df19fee16fc1ebc44941fea8e-Paper-Conference.pdf), [Self-calibration for Language Model Quantization and Pruning](https://aclanthology.org/2025.naacl-long.509.pdf), [WaterPool: A Language Model Watermark Mitigating Trade-Offs among Imperceptibility, Efficacy and Robustness](https://aclanthology.org/2025.naacl-long.209.pdf), [Efficient and Privacy-Preserving Soft Prompt Transfer for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ds/wang25ds.pdf), [Instructing Large Language Models for Low-Resource Languages: A Systematic Study for Basque](https://aclanthology.org/2025.emnlp-main.1484.pdf), [Balancing Diversity and Risk in LLM Sampling: How to Select Your Method and Parameter for Open-Ended Text Generation](https://aclanthology.org/2025.acl-long.1278.pdf), [CKnowEdit: A New Chinese Knowledge Editing Dataset for Linguistics, Facts, and Logic Error Correction in LLMs](https://aclanthology.org/2025.acl-long.430.pdf), [MAGNET: Augmenting Generative Decoders with Representation Learning and Infilling Capabilities](https://aclanthology.org/2025.acl-long.1325.pdf), [Odysseus Navigates the Sirens' Song: Dynamic Focus Decoding for Factual and Diverse Open-Ended Text Generation](https://aclanthology.org/2025.acl-long.1320.pdf))
> The task of generating text without a specific, constrained format, often as a continuation of a given prompt.

**Unconditional text generation** (4 papers: [The Belief State Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/01b3dea1871f7cea1e0e6be1f2f085bc-Paper-Conference.pdf), [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf), [Latent Thought Models with Variational Bayes Inference-Time Computation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kong25c/kong25c.pdf), [Tractable Transformers for Flexible Conditional Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ao/liu25ao.pdf))
> Generating a continuation when the goal or suffix is unknown, using only the prefix and internal decoding strategy.

**Open-response generation** (1 paper: [Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf))
> Generating free-form, unconstrained text in response to a prompt, such as describing an image or answering a question without predefined choices.

## Relationships

### Text generation →
- **WikiText-2** (measurement instrument): *measured_by*, 11 papers
  > we evaluate quantized models by reporting the perplexity of language generation experiments, specifically on WikiText2 (Merity et al., 2016), PTB (Marcus et al., 1994)), C4 (Raffel et al., 2020). (Section 4.1)
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
  - [OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f2fc4053a66edfa430bcdf9a6ff3b17-Paper-Conference.pdf)
  - [MoDeGPT: Modular Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb7214d2fdfd84165b08539d59c92e07-Paper-Conference.pdf)
  - [STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking](https://proceedings.iclr.cc/paper_files/paper/2025/file/510e7d39fce008a3e31de54b8f5be9ac-Paper-Conference.pdf)
  - [Probe Pruning: Accelerating LLMs through Dynamic Pruning via Model-Probing](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44efaa3b7a389ea56c7ee9d6589e800-Paper-Conference.pdf)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
  - [La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cj/liu25cj.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
  - [Machine-generated text detection prevents language model collapse](https://aclanthology.org/2025.emnlp-main.1506.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 9 papers
  > In this section, we use MT-Bench (Zheng et al., 2023) to evaluate the quantized models’ free-form text generation capabilities... (Section 6)
  - [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf)
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
  - [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf)
  - [DropBP: Accelerating Fine-Tuning of Large Language Models by Dropping Backward Propagation](https://proceedings.neurips.cc/paper_files/paper/2024/file/240225294cdd2c9b692c2519d3278a08-Paper-Conference.pdf)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
  - [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d46574e5baae5121180228223a11836-Paper-Conference.pdf)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
  - [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.601.pdf)
- **E2E NLG Challenge** (measurement instrument): *measured_by*, 8 papers
  > We compare our approach with LoRA and other parameter-efficient adaptation methods on the natural language understanding (GLUE) and natural language generation (E2E) benchmarks... (Section 1)
  - [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [VB-LoRA: Extreme Parameter Efficient Fine-Tuning with Vector Banks](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e0d38c676d5855bcfab7f6d29d20ad9-Paper-Conference.pdf)
  - [KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf)
  - [On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf)
  - [Logits are All We Need to Adapt Closed Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hiranandani25a/hiranandani25a.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 8 papers
  > As we generate open-ended text from our off-the-shelf models OTSi and our mLLaVA variants for Object Identification, we evaluate this particular task using an LLM-as-a-Judge, specifically Prometheus-2-8x7B (Kim et al., 2024). (Section 4.2)
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
  - [Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
  - [Differentially Private Steering for Large Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45326c2df19fee16fc1ebc44941fea8e-Paper-Conference.pdf)
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
  - [Personality Alignment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/25203d1cc8c58381eab578f4fcf9c4f8-Paper-Conference.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
  - [FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deb25a/deb25a.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 7 papers
  > For open-ended generation tasks, we adopt TruthfulQA [29] and tasks involving chain-of-thought reasoning [52]: StrategyQA [12] and GSM8K [8]. (Section 3.1)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **C4** (measurement instrument): *measured_by*, 6 papers
  > we evaluate quantized models by reporting the perplexity of language generation experiments, specifically on WikiText2 (Merity et al., 2016), PTB (Marcus et al., 1994)), C4 (Raffel et al., 2020). (Section 4.1)
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
  - [STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking](https://proceedings.iclr.cc/paper_files/paper/2025/file/510e7d39fce008a3e31de54b8f5be9ac-Paper-Conference.pdf)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
  - [WaterPool: A Language Model Watermark Mitigating Trade-Offs among Imperceptibility, Efficacy and Robustness](https://aclanthology.org/2025.naacl-long.209.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 4 papers
  > "We conduct experiments on text generation tasks by fine-tuning Phi-3-mini-4k-instruct [1] on the GSM-8K [9] dataset"
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [Selective Aggregation for Low-Rank Adaptation in Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53a37f820d5be5930415d964f4a0187-Paper-Conference.pdf)
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **PTB** (measurement instrument): *measured_by*, 3 papers
  > we evaluate quantized models by reporting the perplexity of language generation experiments, specifically on WikiText2 (Merity et al., 2016), PTB (Marcus et al., 1994)), C4 (Raffel et al., 2020). (Section 4.1)
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
  - [STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **Vicuna-Bench** (measurement instrument): *measured_by*, 3 papers
  > “we employ a broad array of out-of-distribution benchmarks to conduct a more comprehensive evaluation of the model’s capabilities. This includes assessing ... open-ended generation (Vicuna (Chiang et al., 2023) and WizardLM (Xu et al., 2023))”
  - [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf)
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 3 papers
  > We have conducted additional experiments on more realistic open-ended generations datasets, Hot-PotQA [57], Natural Question (NQ) [23], TriviaQA [21]. (Appendix D)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 3 papers
  > We have conducted additional experiments on more realistic open-ended generations datasets, Hot-PotQA [57], Natural Question (NQ) [23], TriviaQA [21]. (Appendix D)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **TinyStories** (measurement instrument): *measured_by*, 3 papers
  > "When trained on the TinyStories dataset ... ARDTs produce coherent and grammatically accurate text"
  - [On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf)
  - [The Belief State Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/01b3dea1871f7cea1e0e6be1f2f085bc-Paper-Conference.pdf)
  - [On Understanding Attention-Based In-Context Learning for Categorical Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25u/wang25u.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 2 papers
  > Our models are also tested for their open-ended text generation capabilities using model-based evaluations, specifically through MT-Bench [77], AlpacaEval 1.0 and 2.0 [37] (Section 4.1)
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
  - [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d46574e5baae5121180228223a11836-Paper-Conference.pdf)
- **WebNLG** (measurement instrument): *measured_by*, 2 papers
  > We utilize the following datasets for our Natural Language Generation (NLG) task: ... WebNLG (Gardent et al., 2017) is a text-to-data dataset... (Section 3.1)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [Logits are All We Need to Adapt Closed Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hiranandani25a/hiranandani25a.pdf)
- **XSum** (measurement instrument): *measured_by*, 2 papers
  > For the NLG task, we finetune the encoder-decoder model BART-large [11] and T5-base [21] on the text summarization datasets XSum [19] and CNN/DailyMail [8]
  - [Unveiling LoRA Intrinsic Ranks via Salience Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9f00cb7dd5fbdc2175d55e2fdf1b05-Paper-Conference.pdf)
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.170.pdf)
- **OpenWebText** (measurement instrument): *measured_by*, 2 papers
  > We first compare the quality of unconditional samples generated by models trained on either WebText (Radford et al., 2019) or OpenWebText (Gokaslan & Cohen, 2019)... (Section 6.1)
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)
  - [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.601.pdf)
- **Super-NaturalInstructions** (measurement instrument): *measured_by*, 2 papers
  > The Super-Natural instruction dataset (Wang et al., 2022) contains a collection of 1600+ NLP tasks, including both classiﬁcation and generation tasks.
  - [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf)
  - [AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning](https://aclanthology.org/2025.emnlp-main.678.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 2 papers
  > To corroborate these G-Eval findings, we conduct human evaluations involving 5 in-house annotators who assessed 50 randomly selected ChatGPT’s generations across the datasets. (Section 4.2)
  - [Flexibly Utilize Memory for Long-Term Conversation via a Fragment-then-Compose Framework](https://aclanthology.org/2025.emnlp-main.1069.pdf)
  - [Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > ...two generation datasets... with the LM-Evaluation-Harness framework (Gao et al., 2023).
  - [SVD-LLM V2: Optimizing Singular Value Truncation for Large Language Model Compression](https://aclanthology.org/2025.naacl-long.217.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > We theorise that as the VLLMs have not been explicitly trained on image-language pairs of manipulated images, a large number of parameters on the language generation leads to more hallucinations [25, 79] for this simple but abstract task. (Section 5.1)
  - [A Hitchhiker's Guide to Fine-Grained Face Forgery Detection Using Common Sense Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/059d2b9188cdb7ae00f4d78cc9469704-Paper-Datasets_and_Benchmarks_Track.pdf)
- **DART** (measurement instrument): *measured_by*, 1 paper
  > We utilize the following datasets for our Natural Language Generation (NLG) task: ... DART (Nan et al., 2020) is yet another significant dataset employed for evaluating text-to-data generation. (Section 3.1)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our models on the LAMBADA dataset and report accuracy and perplexity for zero-shot generation in Figure 4.
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **WizardLM** (measurement instrument): *measured_by*, 1 paper
  > “we employ a broad array of out-of-distribution benchmarks to conduct a more comprehensive evaluation of the model’s capabilities. This includes assessing ... open-ended generation (Vicuna (Chiang et al., 2023) and WizardLM (Xu et al., 2023))”
  - [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > We have conducted additional experiments on more realistic open-ended generations datasets, Hot-PotQA [57], Natural Question (NQ) [23], TriviaQA [21]. (Appendix D)
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **MMBench-Video** (measurement instrument): *measured_by*, 1 paper
  > In response, we present MMBench-Video, a novel dataset tailored for longer videos, challenging models to generate detailed, free-form responses to complex questions. (Section 2.2)
  - [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf)
- **CNN/DailyMail** (measurement instrument): *measured_by*, 1 paper
  > For the NLG task, we finetune the encoder-decoder model BART-large [11] and T5-base [21] on the text summarization datasets XSum [19] and CNN/DailyMail [8]
  - [Unveiling LoRA Intrinsic Ranks via Salience Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9f00cb7dd5fbdc2175d55e2fdf1b05-Paper-Conference.pdf)
- **BioASQ** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our method on the following tasks covering different domains of natural language generation: ... biology and medicine (BioASQ [35]) (Sec. 5)
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 1 paper
  > Table 5: Multimodal reasoning ability on MM-Vet [92]. Rec denotes Recognition; Know denotes knowledge; Gen denotes Language generation; and Spat denotes Spatial awareness.
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 1 paper
  > "For open-ended generation tasks, we adopt TruthfulQA [29] and tasks involving chain-of-thought reasoning [52]: StrategyQA [12] and GSM8K [8]."
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **ToxiGen** (measurement instrument): *measured_by*, 1 paper
  > For the open-ended generation tasks, we apply SADI on TriviaQA (Joshi et al., 2017), TruthfulQA (Lin et al., 2022), ToxiGen (Hartvigsen et al., 2022) datasets. (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 1 paper
  > “We prompt the trained models to answer 805 questions from the AlpacaEval dataset”
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurement instrument): *measured_by*, 1 paper
  > We employ three distinct text generation datasets: Alpaca (Taori et al., 2023), tldr_news (Belvèze, 2022), and MHC (Amod, 2024), to evaluate the effectiveness of our method across various generation tasks.
  - [JoPA: Explaining Large Language Model's Generation via Joint Prompt Attribution](https://aclanthology.org/2025.acl-long.1074.pdf)
- **UltraChat** (measurement instrument): *measured_by*, 1 paper
  > For chat APIs and instruct LLMs, we generate outputs from UltraChat (Ding et al., 2023), a diverse dialogue and instruction dataset.
  - [Idiosyncrasies in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25z/sun25z.pdf)
- **CommonGen** (measurement instrument): *measured_by*, 1 paper
  > We evaluate Plugin on four text generation benchmarks: (a) E2E NLG (Duˇsek et al., 2020), (b) Web NLG (Gardent et al., 2017), (c) CommonGen (Lin et al., 2020), and (d) the Adidas product description dataset (adi, 2023). (Section 7)
  - [Logits are All We Need to Adapt Closed Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hiranandani25a/hiranandani25a.pdf)
- **Response understanding** (construct): *causes*, 1 paper
  > To improve response understanding, we train the LLM to generate responses given the input, as illustrated in Figure 3 (a). (Section 3.2.1)
  - [GRAM: A Generative Foundation Reward Model for Reward Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ad/wang25ad.pdf)
- **WikiText-103** (measurement instrument): *measured_by*, 1 paper
  > "For the latter, we follow (Tong et al., 2023) to use Wikitext-103-v1, a large-scale dataset derived from Wikipedia articles for language modeling tasks."
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **SVAMP** (measurement instrument): *measured_by*, 1 paper
  > Text Generation We use the SVAMP dataset (Patel et al., 2021) which consists of English math word problems with grade level up to 4.
  - [RRInf: Efficient Influence Function Estimation via Ridge Regression for Large Language Models and Text-to-Image Diffusion Models](https://aclanthology.org/2025.emnlp-main.933.pdf)
- **CHAIR** (measurement instrument): *measured_by*, 1 paper
  > Finally, for open-ended generation, we use the CHAIR (Rohrbach et al., 2018). (Section 5.1)
  - [Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens](https://aclanthology.org/2025.emnlp-main.1092.pdf)
- **ESConv** (measurement instrument): *measured_by*, 1 paper
  > we conduct experiments on the ESConv dataset by selectively omitting each of the four distinct aspects when applying the IntentionFrame framework to enhance downstream response generation.
  - [IntentionFrame: A Semi-Structured, Multi-Aspect Framework for Fine-Grained Conversational Intention Understanding](https://aclanthology.org/2025.emnlp-main.1427.pdf)
- **LaMP** (measurement instrument): *measured_by*, 1 paper
  > "LaMP benchmark consisting of various text classification and generation tasks"
  - [Personalized Language Models via Privacy-Preserving Evolutionary Model Merging](https://aclanthology.org/2025.emnlp-main.1747.pdf)

### → Text generation
- **Thought generation** (behavioral indicator): *causes*, 1 paper
  > Through preference optimization the thoughts are then optimized to improve the resulting responses (Section 2.2).
  - [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf)

### Associated with
- **Text generation quality** (construct), 2 papers
  > "we also demonstrate improved generation quality in open-ended text generation"
  - [Retrieval is Accurate Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf)
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **Generation diversity** (construct), 1 paper
  > Diversity: This metric measures the ability to generate texts with a wide range of vocabulary.
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
- **Generative ability** (construct), 1 paper
  > "make progress toward more expressive sampling algorithms that better surface the generative capabilities of large language models."
  - [Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf)
- **Objective mismatch** (construct), 1 paper
  > As pointed out in Section 3.3, this can be attributed to an objective mismatch between text generation and preference modeling. (Section 5.2).
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
- **Judicial analysis generation** (behavioral indicator), 1 paper
  > Tasks at the Generation level require LLMs to generate legal texts with given requirements and formats. We construct four tasks at this level: ...Judicial Analysis Generation (5-2)... (Section C.3.5)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Machine translation** (behavioral indicator), 1 paper
  > Tasks at the Generation level require LLMs to generate legal texts with given requirements and formats. We construct four tasks at this level: ...Legal Translation (5-3)... (Section C.3.5)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Memorization** (construct), 1 paper
  > we observe that LISA is much better than LoRA at memorization-centered tasks, such as Writing or depicting image details, while this gap is much smaller in reasoning-centered tasks like Code or Math (Section 5).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Logical reasoning** (construct), 1 paper
  > When evaluating the Writing Legal Document scenario, logic is identified as the most critical dimension, followed by considerations of harmlessness and clarity, reflecting the distinct requirements of legal writing.
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Coherence** (construct), 1 paper
  > Coherence evaluates the semantic relatedness between each prompt and its generated response.
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
- **Alignment** (construct), 1 paper
  > They did not investigate the more challenging task of language generation, which is closely tied to alignment and involves a significantly more complex output space. (Section 5)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
- **Cultural bias** (construct), 1 paper
  > "In open-ended generative tasks like narrative writing or dialogue, large language models often exhibit cultural biases"
  - [Attributing Culture-Conditioned Generations to Pretraining Corpora](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4546b4f9e1a44ed15c253dd43307dd5-Paper-Conference.pdf)
- **Aspect-based sentiment analysis** (behavioral indicator), 1 paper
  > Alternatively, the ABSA task can be formulated as a text generation problem, where the model predicts a set of sentiment tuples y = {(ai, pi)}T i=1, (Section 3.1)
  - [LACA: Improving Cross-lingual Aspect-Based Sentiment Analysis with LLM Data Augmentation](https://aclanthology.org/2025.acl-long.41.pdf)
- **Peer review generation** (behavioral indicator), 1 paper
  > we split the research simulation process into three critical stages: (1) paper reading, (2) paper writing, and (3) review writing. We believe these stages are crucial in the research community, and each stage relies on the output of the previous stage as input. (Section 5)
  - [ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf)
- **Creative writing** (behavioral indicator), 1 paper
  > Creative composition encompasses generation tasks that require everyday creativity for personal goals... brainstorming solutions to personal problems requires inventive and harmless advice. (Section 1)
  - [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf)
- **Generalization** (construct), 1 paper
  > Two core challenges distinguish open-ended generation from closed-end tasks: (1) Limited generalization across prompt variations... (Introduction)
  - [SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.112.pdf)
- **Natural language understanding** (construct), 1 paper
  > For actions that require natural language understanding, such as composing a text message or querying a search engine, a VLM is invoked to generate the necessary text.
  - [Lightweight Neural App Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/b81266057eb3d96469940d1860a41ad2-Paper-Conference.pdf)
- **FLAN** (measurement instrument), 1 paper
  > FLAN is a dataset with more diverse forms of tasks, including free-form generation tasks like translation and summarization. (Section 5)
  - [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)
- **Human preference alignment** (construct), 1 paper
  > given π∗aligned with human preference, it can both empower response generation, as well as work with its reference model (amateur) to enhance the scoring of HPA for candidate responses. (Section 1)
  - [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf)
- **Utility preservation** (construct), 1 paper
  > As a foundation model, f ′ is expected to retain abilities such as text and code generation, question answering, instruction-following, and basic mathematical reasoning.
  - [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf)
- **Robustness** (construct), 1 paper
  > “We systematically compare three widely used value probing methods: token likelihood, sequence perplexity, and text generation. Our results show that all three methods exhibit large variances under non-semantic perturbations” (Abstract).
  - [Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?](https://aclanthology.org/2025.emnlp-main.7.pdf)
