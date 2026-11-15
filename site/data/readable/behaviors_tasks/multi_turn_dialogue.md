# Multi-turn dialogue
**Type:** Behavioral indicator  
**Supporting papers:** 103  
**Also known as:** Multi-turn conversation, Multi-round dialogue, Multi-turn communication, Multi-turn chat, Interactive communication, Multi-round conversation, Multi-turn dialogue understanding, Open-ended conversation, Extended conversation, Dialogue, Casual conversation, Conversation, Conversational interaction, Multi-turn dialog, Human-like conversation, General chat, Open-ended interaction, Agent chatting, Multi-turn conversational interaction  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is coherent, context-aware conversation over multiple exchanges, where each response depends on the dialogue history and remains relevant across turns. Many papers cast it as back-and-forth user-assistant interaction, sometimes to resolve a request or accomplish a goal, and some extend this to agent-agent or agent-environment episodes with explicit turn taking. A smaller line of work narrows success to higher-quality, guideline-compliant, or progressively clarifying responses over time.

**Variants.** Papers use several near-synonyms, most often multi-turn conversation or multi-round dialogue, alongside multi-turn chat, dialogue, conversational interaction, open-ended conversation, and extended conversation. The studied settings range from open-domain and casual chat to task-oriented dialogue, tool-calling, tutoring, doctor-patient consultation, and collaborative agent communication. Others examine grounded or memory-heavy variants, including GUI, graph, image, and video conversations, code-editing chat, and dialogue understanding where the model retrieves relevant material from prior turns.

**Space of elicitation and scores.** Papers link this behavior to 9 measurement instruments. The prevailing measure is MT-Bench, which papers describe as multi-turn conversational questions or dialogues spanning domains such as writing, reasoning, math, and coding; smaller amounts of work use Chatbot Arena for open-ended conversational ranking, GUI-WORLD and LLaVA-Bench-in-the-Wild for multimodal conversation, and LLM-as-a-judge to score multi-round answers against golden responses. Across these links, the instruments are mostly benchmark-style evaluations or datasets, with a judge methodology also used.

**What it is taken as evidence of.** Papers link it to 4 constructs, and the recorded links are dispersed rather than centered on a single construct. It is reported as related to instruction following ability, robustness to higher dialogue turns, and long-context understanding. Separately, a paper claims a causal relationship from multi-turn dialogue to interpretability and explainability, stating that conversational interfaces for 'chatting with a graph' enhance explainability.

## Sources

**Multi-turn dialogue** (14 papers: [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf), [SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3075b88e583a0e98d8b24338a613060-Paper-Conference.pdf), [AutoEval-ToD: Automated Evaluation of Task-oriented Dialog Systems](https://aclanthology.org/2025.naacl-long.508.pdf), [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf), [LMRL Gym: Benchmarks for Multi-Turn Reinforcement Learning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abdulhai25a/abdulhai25a.pdf), [From Problem-Solving to Teaching Problem-Solving: Aligning LLMs with Pedagogy using Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.15.pdf), [Empowering and Assessing the Utility of Large Language Models in Crop Science](https://proceedings.neurips.cc/paper_files/paper/2024/file/5e5783c673cf05cfd4b3ebf46e96abfc-Paper-Datasets_and_Benchmarks_Track.pdf), [Regressing the Relative Future: Efficient Policy Optimization for Multi-turn RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/186094ef879dcbd5ef6879782916c309-Paper-Conference.pdf), [Dialogue-RAG: Enhancing Retrieval for LLMs via Node-Linking Utterance Rewriting](https://aclanthology.org/2025.acl-long.1191.pdf), [Dynamic Evaluation with Cognitive Reasoning for Multi-turn Safety of Large Language Models](https://aclanthology.org/2025.acl-long.963.pdf), [Faster Speculative Decoding via Effective Draft Decoder with Pruned Candidate Tree](https://aclanthology.org/2025.acl-long.486.pdf), [GUICourse: From General Vision Language Model to Versatile GUI Agent](https://aclanthology.org/2025.acl-long.1065.pdf), [LLMs Can Simulate Standardized Patients via Agent Coevolution](https://aclanthology.org/2025.acl-long.846.pdf))
> The behavior of maintaining a coherent and contextually relevant conversation over multiple exchanges with a user.

**Multi-turn conversation** (13 papers: [#InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/9dae2a90bae49dc874ce1ca8fcc20879-Paper-Conference.pdf), [What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/6091f2bb355e960600f62566ac0e2862-Paper-Conference.pdf), [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf), [Generative Prompt Internalization](https://aclanthology.org/2025.naacl-long.376.pdf), [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf), [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf), [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-Device LLM](https://aclanthology.org/2025.emnlp-main.533.pdf), [Cultural Learning-Based Culture Adaptation of Language Models](https://aclanthology.org/2025.acl-long.156.pdf), [SPECTRA: Faster Large Language Model Inference with Optimized Internal and External Speculation](https://aclanthology.org/2025.acl-long.685.pdf), [Towards the Law of Capacity Gap in Distilling Language Models](https://aclanthology.org/2025.acl-long.1097.pdf))
> Responding coherently across multiple dialogue turns in a conversational benchmark setting.

**Multi-round dialogue** (3 papers: [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf), [PEARL: Parallel Speculative Decoding with Adaptive Draft Length](https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf), [DavIR: Data Selection via Implicit Reward for Large Language Models](https://aclanthology.org/2025.acl-long.452.pdf))
> Engaging in a sequence of conversational turns with a user, maintaining context across multiple rounds of interaction.

**Multi-turn communication** (1 paper: [Autonomous Agents for Collaborative Task under Information Asymmetry](https://proceedings.neurips.cc/paper_files/paper/2024/file/0534abc9e6db91683d82186ef0d68202-Paper-Conference.pdf))
> Exchanging utterances over multiple turns to progressively resolve a task.

**Multi-turn chat** (1 paper: [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf))
> Engaging in a conversation with a user over multiple sequential exchanges of input and output.

**Interactive communication** (1 paper: [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf))
> Engaging in a multi-turn dialogue with a user to exchange information or complete a task.

**Multi-round conversation** (1 paper: [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf))
> Engaging in a sequential, multi-turn dialogue about a GUI, where the model's responses must account for the conversational history.

**Multi-turn dialogue understanding** (1 paper: [From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf))
> Processing and responding to conversational exchanges that span multiple interaction rounds with information retrieval from prior dialogue.

**Open-ended conversation** (2 papers: [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf), [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf))
> Engaging in multi-turn, unconstrained dialogue with a user on a variety of topics.

**Extended conversation** (2 papers: [Circuit Complexity Bounds for RoPE-based Transformer Architecture](https://aclanthology.org/2025.emnlp-main.561.pdf), [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf))
> The observable behavior of maintaining a coherent and contextually appropriate dialogue over many turns.

**Dialogue** (6 papers: [Cache-Efficient Posterior Sampling for Reinforcement Learning with LLM-Derived Priors Across Discrete and Continuous Domains](https://aclanthology.org/2025.emnlp-main.560.pdf), [PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebf8764ecf0688cdd9fe1e5a9c525d0d-Paper-Conference.pdf), [CPPO: Continual Learning for Reinforcement Learning with Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf), [MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cs/zhang25cs.pdf), [ROPO: Robust Preference Optimization for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25d/liang25d.pdf), [LiPO: Listwise Preference Optimization through Learning-to-Rank](https://aclanthology.org/2025.naacl-long.121.pdf))
> Engaging in multi-turn, coherent conversation with a user or another agent.

**Casual conversation** (1 paper: [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-Device LLM](https://aclanthology.org/2025.emnlp-main.533.pdf))
> Engaging in open-domain, non-task-oriented dialogue about everyday topics such as weather, hobbies, or daily life.

**Conversation** (3 papers: [Scalable Data Synthesis through Human-like Cognitive Imitation and Data Recombination](https://aclanthology.org/2025.emnlp-main.236.pdf), [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf), [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf))
> Engaging in interactive, multi-turn dialogue with a user.

**Conversational interaction** (3 papers: [UltraIF: Advancing Instruction Following from the Wild](https://aclanthology.org/2025.emnlp-main.945.pdf), [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf), [Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf))
> The act of participating in a multi-turn dialogue and generating responses that are judged to be of high quality.

**Multi-turn dialog** (1 paper: [Collaborative Rational Speech Act: Pragmatic Reasoning for Multi-Turn Dialog](https://aclanthology.org/2025.emnlp-main.1145.pdf))
> Engaging in a conversation that extends over multiple back-and-forth exchanges between participants.

**Human-like conversation** (1 paper: [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf))
> Engaging in open-ended dialogue that mimics the patterns, coherence, and interactivity of human conversation.

**General chat** (1 paper: [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf))
> The task of engaging in open-domain, multi-turn conversation with a user.

**Open-ended interaction** (1 paper: [Unbounded: A Generative Infinite Game of Character Life Simulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/da2411768acb844b255bb6770e5a71c7-Paper-Conference.pdf))
> The model's participation in unconstrained, free-form interactions with a user, generating responses to a wide variety of natural language inputs without pre-defined rules.

**Agent chatting** (1 paper: [GuideBench: Benchmarking Domain-Oriented Guideline Following for LLM Agents](https://aclanthology.org/2025.acl-long.557.pdf))
> Maintaining coherent and guideline-compliant responses across multiple conversational turns in an agent-user dialogue.

**Multi-turn conversational interaction** (1 paper: [Pixel-Level Reasoning Segmentation via Multi-turn Conversations](https://aclanthology.org/2025.acl-long.864.pdf))
> Engaging in a sequence of dialogue turns with a user, where each response builds on prior context to progressively clarify intent and refine output.

## Relationships

### Multi-turn dialogue →
- **MT-Bench** (measurement instrument): *measured_by*, 18 papers
  > MT-Bench includes a series of open-ended questions that assess LLM capabilities in multi-turn conversations and instruction-following
  - [Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf)
  - [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf)
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
  - [PEARL: Parallel Speculative Decoding with Adaptive Draft Length](https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf)
  - [Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf)
  - [Learning Harmonized Representations for Speculative Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/575286a73f238b6516ce0467d67eadb2-Paper-Conference.pdf)
  - [ALLaM: Large Language Models for Arabic and English](https://proceedings.iclr.cc/paper_files/paper/2025/file/54c15a3033686e7999aecd2740c5a7c4-Paper-Conference.pdf)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
  - [LoCA: Location-Aware Cosine Adaptation for Parameter-Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/d63d7d489a9338afff53d17410ea2c10-Paper-Conference.pdf)
  - [Faster Speculative Decoding via Effective Draft Decoder with Pruned Candidate Tree](https://aclanthology.org/2025.acl-long.486.pdf)
  - [SPECTRA: Faster Large Language Model Inference with Optimized Internal and External Speculation](https://aclanthology.org/2025.acl-long.685.pdf)
  - [Gumiho: A Hybrid Architecture to Prioritize Early Tokens in Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dg/li25dg.pdf)
  - [polybasic Speculative Decoding Through a Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25az/wang25az.pdf)
  - [FuseChat: Knowledge Fusion of Chat Models](https://aclanthology.org/2025.emnlp-main.1096.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 1 paper
  > LLaVA-Bench serves as a general benchmark for systematic comprehension, encompassing three categories: conversation, detailed description, and complex questions. (Section 4.2)
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
- **Vicuna-Bench** (measurement instrument): *measured_by*, 1 paper
  > MT-bench and Vicuna-bench are designed to test the models' competencies in various complex cognitive tasks, including mathematics, reasoning, complex format handling, and writing through both multi-turn and single-turn dialogues.
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **Interpretability and explainability** (construct): *causes*, 1 paper
  > We also enhance explainability, both by returning the retrieved subgraph, and through the use of conversational interfaces for 'chatting with a graph'
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > To assess free-form questions and multiple-round conversations, we utilize the LLM-as-a-Judge methodology, which assigns a similarity score ranging from 1 to 5 between MLLM’s response and a predefined golden answer... (Section 3.1)
  - [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf)
- **Chatbot Arena** (measurement instrument): *measured_by*, 1 paper
  > Chatbot Arena has become a cornerstone in LLM evaluation, offering rich datasets for ranking models in open-ended conversational tasks.
  - [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf)
- **GUI-WORLD** (measurement instrument): *measured_by*, 1 paper
  > “GUI-WORLD features various question types” and “multi-round conversation”
  - [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf)
- **TableEval** (measurement instrument): *measured_by*, 1 paper
  > This approach accommodates various task types within diverse real-world industrial scenarios, including information retrieval, numerical analysis, table reasoning, data analysis, multi-turn dialogue, and understanding of table structures. (Section 3.1)
  - [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf)

### Associated with
- **WildChat** (measurement instrument), 1 paper
  > this paper presents the WILDCHAT dataset, a comprehensive multi-turn, multi-lingual dataset consisting of 1 million timestamped conversations (Section 1).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **HelpSteer2** (measurement instrument), 1 paper
  > To ensure HelpSteer2 is effective for predicting rewards in multi-turn conversations, we included multi-turn prompts, which comprise approximately 29% of the samples.
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Instruction following ability** (construct), 1 paper
  > Can LLMs continuously follow the system message in multi-turn conversations? (Section 3.1)
  - [SysBench: Can LLMs Follow System Message?](https://proceedings.iclr.cc/paper_files/paper/2025/file/b917f916e7eed84ffe8f5e63492b2be8-Paper-Conference.pdf)
- **Robustness** (construct), 1 paper
  > Our MTU-LLaMA exhibits the most gradual decrease in performance, demonstrating its robustness to higher dialogue turns. (Section 3.2)
  - [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf)
- **Long-context understanding** (construct), 1 paper
  > Large language models (LLMs) have advanced to support long-context tasks such as document understanding (Li et al., 2024a), multi-turn dialogues (Yi et al., 2024), repository-level code completion (Jimenez et al., 2024), and complex reasoning (Zhou et al., 2025).
  - [LeanK: Learnable K Cache Channel Pruning for Efficient Decoding](https://aclanthology.org/2025.emnlp-main.1584.pdf)
