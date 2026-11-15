# Coherence
**Type:** Construct  
**Supporting papers:** 96  
**Also known as:** Semantic coherence, Coherency, Contextual consistency, Dialogue coherence, Plot quality, Story coherence, Plot coherence, Topic coherence, Text coherence, Argument coherence, Structural consistency, Contextual coherence, Response coherence, Chat consistency  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats coherence as an output-level quality: text, dialogue, summaries, stories, lyrics, or reports should remain logically connected, semantically consistent, well structured, and relevant to prior context, while avoiding contradictions, drift, fragmentation, or nonsensical continuations. Many papers narrow this further to context maintenance, for example topic maintenance with the input prefix, consistency with conversation history, or semantic relevance across long sequences and turns. A smaller line uses the same label differently, defining coherence as agreement between generative and discriminative judgments about correctness, and another defines it as producing semantically equivalent answers for semantically equivalent questions. The main variation is whether coherence is treated as a property of produced outputs, of agreement across query modes, or of answer stability under input variation.

**Space of facets.** Papers use several neighboring labels for closely related ideas, especially semantic coherence, contextual consistency, and chat consistency, all of which focus on staying aligned with earlier context across long sequences or turns. Other task-specific variants narrow the construct to narrative progression, topical unity, or organized argumentative or survey structure, and some authors distinguish local from global coherence. Across these uses, coherence is usually listed alongside, rather than treated as the same thing as, fluency, relevance, factual consistency, naturalness, diversity, or creativity.

**Space of measurement.** Papers link coherence to 8 measurement instruments and 2 behavioral indicators. The most frequently linked instruments are G-Eval and LLM-as-a-judge, both used as LLM-based evaluators, Human evaluation, and the dataset or benchmark based instruments HelpSteer and AlpacaEval, with 3 other instruments also linked. In practice, papers operationalize coherence by rating whether an output is coherent with the prompt, prefix, or dialogue history, by comparing embeddings of prefixes and continuations or of answers to semantically equivalent questions, by casting dialogue coherence as an NLI-style judgment, and sometimes by using proxies such as perplexity or task accuracy. Most of these operationalizations match the dominant output-level framing, though the paraphrase-stability use is measured differently.

**Links.** Papers link coherence to 9 constructs. They claim causal relationships from context retention and causal reasoning to coherence, and from coherence to factuality; another causal account says loss of coherence can arise when a model does not fully understand a request. One paper reports that coherence correlates with helpfulness, describing it as a weaker predictor in one version than another. Other papers describe non-causal links to conversational ability and to broader generation trade-offs or behavior-level semantic fit.

## Sources

**Coherence** (19 papers: [BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf), [Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf), [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf), [Language Model Decoding as Direct Metrics Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf), [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf), [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf), [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf), [Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](https://aclanthology.org/2025.acl-long.210.pdf), [ToneCraft: Cantonese Lyrics Generation with Harmony of Tones and Pitches](https://aclanthology.org/2025.emnlp-main.18.pdf), [Evaluating Small Language Models for News Summarization: Implications and Factors Influencing Performance](https://aclanthology.org/2025.naacl-long.253.pdf), [Unifying AI Tutor Evaluation: An Evaluation Taxonomy for Pedagogical Ability Assessment of LLM-Powered AI Tutors](https://aclanthology.org/2025.naacl-long.57.pdf), [Analyzing and Improving Coherence of Large Language Models in Question Answering](https://aclanthology.org/2025.naacl-long.588.pdf), [RAP: A Metric for Balancing Repetition and Performance in Open-Source Large Language Models](https://aclanthology.org/2025.naacl-long.69.pdf), [Latent Factor Models Meets Instructions: Goal-conditioned Latent Factor Discovery without Task Supervision](https://aclanthology.org/2025.naacl-long.554.pdf), [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf), [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf), [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf), [DTELS: Towards Dynamic Granularity of Timeline Summarization](https://aclanthology.org/2025.naacl-long.136.pdf), [REFFLY: Melody-Constrained Lyrics Editing Model](https://aclanthology.org/2025.naacl-long.564.pdf))
> The degree to which a language model's generative and discriminative judgments align, reflecting a consistent internal assessment of correctness across different query modes.

**Semantic coherence** (4 papers: [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf), [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf), [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf), [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf))
> The latent ability of a model to generate text that is contextually consistent and semantically relevant to the preceding input.

**Coherency** (1 paper: [MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf))
> The extent to which an agent's responses maintain a consistent line of dialogue, avoiding contradictions with previous turns or internal inconsistencies.

**Contextual consistency** (1 paper: [DrDiff: Dynamic Routing Diffusion with Hierarchical Attention for Breaking the Efficiency-Quality Trade-off](https://aclanthology.org/2025.emnlp-main.474.pdf))
> The tendency to keep generated content aligned with earlier context and avoid contradictions or drift as sequence length grows.

**Dialogue coherence** (1 paper: [Memory OS of AI Agent](https://aclanthology.org/2025.emnlp-main.1318.pdf))
> The quality of a conversation where responses are logically connected, consistent, and relevant to the preceding context, especially over long interactions.

**Plot quality** (1 paper: [Agents' Room: Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf))
> The degree to which a story has a recognizable and coherent structure with events that move the narrative forward without logical or conceptual inconsistencies.

**Story coherence** (1 paper: [Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement](https://aclanthology.org/2025.naacl-long.63.pdf))
> The overall quality of a long-form story in which plot development, context, and expression remain consistent and readable.

**Plot coherence** (1 paper: [Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement](https://aclanthology.org/2025.naacl-long.63.pdf))
> The degree to which the sequence of events in a story follows a logical and causally sound progression, resulting in a fluent and understandable plot.

**Topic coherence** (1 paper: [A Unified Supervised and Unsupervised Dialogue Topic Segmentation Framework Based on Utterance Pair Modeling](https://aclanthology.org/2025.naacl-long.252.pdf))
> The latent degree to which utterances within a dialogue segment belong to the same topic, inferred from their semantic and structural relationships.

**Text coherence** (1 paper: [Self-calibration for Language Model Quantization and Pruning](https://aclanthology.org/2025.naacl-long.509.pdf))
> The degree to which generated calibration text is fluent, semantically plausible, and structurally consistent, as an indicator of quality in synthetic data.

**Argument coherence** (1 paper: [CSEval: Towards Automated, Multi-Dimensional, and Reference-Free Counterspeech Evaluation using Auto-Calibrated LLMs](https://aclanthology.org/2025.naacl-long.279.pdf))
> The degree to which a counterspeech response presents specific, logically consistent, and evidence-based arguments that refute the hateful content.

**Structural consistency** (1 paper: [SurveyGen: Quality-Aware Scientific Survey Generation with Large Language Models](https://aclanthology.org/2025.emnlp-main.136.pdf))
> The degree to which the generated survey follows a coherent and logically organized structure with appropriate section divisions and thematic development, matching human-authored conventions.

**Contextual coherence** (1 paper: [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf))
> The latent ability of an LLM to maintain semantic and structural consistency across long sequences of generated text by preserving relevant long-range dependencies.

**Response coherence** (1 paper: [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf))
> The quality of a model's generated responses being logically connected and relevant to the ongoing conversation.

**Chat consistency** (1 paper: [ConsistentChat: Building Skeleton-Guided Consistent Multi-Turn Dialogues for Large Language Models from Scratch](https://aclanthology.org/2025.emnlp-main.424.pdf))
> The latent ability of a dialogue model to maintain semantic coherence across multiple turns, including alignment with initial intent, logical information flow, and contextual relevance of responses.

## Relationships

### Coherence →
- **Human evaluation** (measurement instrument): *measured_by*, 3 papers
  > To address this, we extend human evaluation guidelines from Clark et al. (2023), assessing repetition, fluency, coherence, compatibility (ROCStories/DialogSum), and hallucination (DeliData): (Section 4.2)
  - [Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](https://aclanthology.org/2025.acl-long.210.pdf)
  - [Wizard of Shopping: Target-Oriented E-commerce Dialogue Generation with Decision Tree Branching](https://aclanthology.org/2025.acl-long.641.pdf)
  - [Accelerating Unbiased LLM Evaluation via Synthetic Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25v/zhou25v.pdf)
- **G-Eval** (measurement instrument): *measured_by*, 3 papers
  > For LLM-based evaluation, we employed G-EVAL(Liu et al., 2023), a state-of-the-art metric designed to assess various qualitative aspects of large language model outputs, including Fluency, Coherence, Naturalness, Empathy, and Patient-Centricity, where higher scores indicate better performance. (Section 5.1)
  - [AI Chatbots as Professional Service Agents: Developing a Professional Identity](https://aclanthology.org/2025.emnlp-main.652.pdf)
  - [MemInsight: Autonomous Memory Augmentation for LLM Agents](https://aclanthology.org/2025.emnlp-main.1683.pdf)
  - [Paired by the Teacher: Turning Unpaired Data into High-Fidelity Pairs for Low-Resource Text Generation](https://aclanthology.org/2025.emnlp-main.1030.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > By the prompts, the LLM judge must consider (a) the response’s naturalness, coherence, engagingness and groundedness. (Section 4.3)
  - [SD-Eval: A Benchmark Dataset for Spoken Dialogue Understanding Beyond Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/681fe4ec554beabdc9c84a1780cd5a8a-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
- **HelpSteer** (measurement instrument): *measured_by*, 2 papers
  > For HelpSteer, we use https://huggingface.co/Haoxiang-Wang/ RewardModel-Mistral-7B-for-DPA-v1 for all attributes of rewards, including helpfulness, correctness, coherence, complexity and verbosity.
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
- **Helpfulness** (construct): *correlates*, 1 paper
  > In Table 2, we observe that coherence is a much weaker predictor of helpfulness in HelpSteer2 (Pearson’s R=0.4979) compared to HelpSteer (Pearson’s R=0.6348).
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > MT-Bench, on the other hand, provides a fine-grained evaluation through multi-turn conversational tasks, evaluating not just correctness, but also coherence and fluency. (Section 5.2)
  - [Reflection-Window Decoding: Text Generation with Selective Refinement](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25a/tang25a.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 1 paper
  > “We collect a random subset of 50 tasks ... from the Alpaca-Eval dataset ... An LLM-as-a-Judge then scores the output on how well it followed the instructions and how coherent it was.”
  - [Precise In-Parameter Concept Erasure in Large Language Models](https://aclanthology.org/2025.emnlp-main.960.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > preserving coherence, as measured by accuracy on the GSM8K, MATH, HumanEval and MMLU-Pro datasets.
  - [Group-Aware Reinforcement Learning for Output Diversity in Large Language Models](https://aclanthology.org/2025.emnlp-main.1649.pdf)
- **MATH** (measurement instrument): *measured_by*, 1 paper
  > preserving coherence, as measured by accuracy on the GSM8K, MATH, HumanEval and MMLU-Pro datasets.
  - [Group-Aware Reinforcement Learning for Output Diversity in Large Language Models](https://aclanthology.org/2025.emnlp-main.1649.pdf)
- **Factuality** (construct): *causes*, 1 paper
  > Improved coherence in turn leads to improved accuracy on factual tasks. (Section 1)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)

### → Coherence
- **Context retention** (construct): *causes*, 1 paper
  > This highlights the memory retention issue in long-context models, which often leads to a loss of coherence and adherence to task instructions. (Section 3.2)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **Understanding** (construct): *causes*, 1 paper
  > We conjecture that the instability, or lack of coherence, is a symptom of the model not being able to fully understand a request, i.e., accessing its parametric knowledge necessary for generating a correct answer. (Section 1)
  - [Analyzing and Improving Coherence of Large Language Models in Question Answering](https://aclanthology.org/2025.naacl-long.588.pdf)
- **Causal reasoning** (construct): *causes*, 1 paper
  > causal reasoning is pivotal for maintaining coherent and specific empathetic interactions (Section 5.2)
  - [ECC: An Emotion-Cause Conversation Dataset for Empathy Response](https://aclanthology.org/2025.emnlp-main.306.pdf)

### Associated with
- **Generation diversity** (construct), 1 paper
  > Thus, the best choice of threshold must strike a balance between diversity (i.e., including as many tokens as possible in the set of candidates) and coherence (i.e., avoiding sampling tokens outside the true support). (Section 2)
  - [Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > Coherence evaluates the semantic relatedness between each prompt and its generated response.
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
- **Creativity** (construct), 1 paper
  > A central challenge is managing the trade-off between creativity and coherence, which is influenced by the sampling strategy during text generation. (Section 1)
  - [Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs](https://proceedings.iclr.cc/paper_files/paper/2025/file/afa5f124e36bed5cc2125067005d43f5-Paper-Conference.pdf)
- **Stability** (construct), 1 paper
  > These models, however, often suffer from instability or lack of coherence, that is the ability of the models to generate semantically equivalent outputs when receiving diverse yet semantically equivalent input variations. (Abstract)
  - [Analyzing and Improving Coherence of Large Language Models in Question Answering](https://aclanthology.org/2025.naacl-long.588.pdf)
- **Semantic textual similarity** (behavioral indicator), 1 paper
  > Besides, these works typically measure semantic similarity via token-level embedding distances. Such approach overlooks contextual information, often leading to reduced contextual semantic coherence. (Section 1)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **Conversational ability** (construct), 1 paper
  > "NTPP, significantly improves the conversational abilities of SLMs in terms of turn-taking prediction, response coherence, and naturalness"
  - [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf)
