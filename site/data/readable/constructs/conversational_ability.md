# Conversational ability
**Type:** Construct  
**Supporting papers:** 28  
**Also known as:** General communication ability, Chatbot capability, Chatbot performance, Conversational capability, Generalist chat capability, Multi-turn dialogue capability, Multi-turn capability, Dialogue capability, Multi-turn conversation ability, Dialogue quality  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats conversational ability as a latent capacity for coherent, context-aware dialogue, usually across multiple turns and sometimes including instruction following in a conversational setting. Many definitions emphasize maintaining prior context across exchanges and producing fluent, helpful, appropriate, or consistent responses. A smaller line of work frames the construct more as overall chatbot performance or capability in open-ended tasks, sometimes inferred from comparative judgments as a latent score, while a few papers narrow it to spoken chat, medical consultation dialogue quality, or dialogue about image authenticity and forgery details.

**Space of facets.** Systematization is light, but one paper explicitly decomposes the construct into fluency, coherency, and consistency, quoting "Flu.: Fluency, Coh.: Coherency, Cons.: Consistency" (OmniCharacter: Towards Immersive Role-Playing Agents with Seamless Speech-Language Personality Interaction). Another paper places a nearby notion, generalist chat capability, under alignment alongside world knowledge and instruction following (WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training). The naming varies across papers, with labels including conversational capability, chatbot capability or performance, dialogue capability, general communication ability, multi-turn capability, multi-turn conversation ability, and dialogue quality; some labels foreground general chat quality, others multi-turn context use, and others a specific application setting.

**Space of measurement.** Papers link the construct to 8 measurement instruments and 2 behavioral indicators. Operationalization is dominated by benchmark-style evaluation, especially MT-Bench, which is described as a multi-turn question-answering benchmark graded by an LLM judge and is repeatedly used to assess conversational or multi-turn ability; AlpacaEval 2.0 and Arena-Hard are the next most common, Chatbot Arena appears through live user interactions and ranking in open-ended conversational tasks, and 3MDBench evaluates diagnostic accuracy and dialogue quality via an Assessor Agent, with 3 other instruments also linked. Most instruments target general or multi-turn chat settings, while 3MDBench targets medical consultation dialogue quality.

**Links.** Reported non-measurement links are all related links. One paper relates conversational ability to visual question answering, treating it as that evaluation dimension in a multimodal setting, and another relates conversational ability to turn-taking prediction. The same line of work also relates coherence to conversational ability and relates conversational ability to naturalness, summarizing conversational abilities in terms of turn-taking prediction, response coherence, and naturalness.

## Sources

**Conversational ability** (5 papers: [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf), [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf), [OmniCharacter: Towards Immersive Role-Playing Agents with Seamless Speech-Language Personality Interaction](https://aclanthology.org/2025.acl-long.1276.pdf), [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf), [Permutative Preference Alignment from Listwise Ranking of Human Judgments](https://aclanthology.org/2025.emnlp-main.17.pdf))
> The latent capacity to engage in multi-turn dialogue and follow instructions in a conversational context.

**General communication ability** (1 paper: [RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5875aca1ef70285a35940afbbce0f9fb-Paper-Datasets_and_Benchmarks_Track.pdf))
> The agent's general proficiency in engaging in coherent and contextually appropriate dialogue, assessed through a question-answer format.

**Chatbot performance** (1 paper: [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf))
> The overall capability of a chatbot in open-ended conversational tasks, as inferred from comparative human judgments and represented by a latent score.

**Conversational capability** (2 papers: [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf), [Condor: Enhance LLM Alignment with Knowledge-Driven Data Synthesis and Refinement](https://aclanthology.org/2025.acl-long.1091.pdf))
> The latent ability to engage in dialogue-like interactions that are judged as helpful and appropriate in chatbot settings.

**Chatbot capability** (1 paper: [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf))
> The model's overall effectiveness and quality in engaging in conversational interactions, encompassing aspects like coherence, helpfulness, and safety.

**Generalist chat capability** (1 paper: [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf))
> The latent ability of a model to engage in high-quality, coherent, and contextually appropriate conversation across a wide range of topics and interaction styles, as judged by human or LLM evaluators.

**Multi-turn capability** (1 paper: [Improving Model Alignment Through Collective Intelligence of Open-Source Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dr/wang25dr.pdf))
> The ability to sustain coherent performance across multiple conversational turns and use prior dialogue context appropriately.

**Multi-turn dialogue capability** (1 paper: [Unlocking the Capabilities of Large Vision-Language Models for Generalizable and Explainable Deepfake Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25d/yu25d.pdf))
> The latent ability of the model to engage in iterative, context-aware conversations with users about image authenticity and forgery details, maintaining coherence across turns.

**Dialogue capability** (1 paper: [VLASCD: A Visual Language Action Model for Simultaneous Chatting and Decision Making](https://aclanthology.org/2025.emnlp-main.468.pdf))
> The model's underlying ability to engage in coherent, context-aware, and fluent conversation.

**Multi-turn conversation ability** (1 paper: [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://aclanthology.org/2025.emnlp-main.583.pdf))
> The capability of a model to maintain context and coherence across multiple exchanges in a dialogue.

**Dialogue quality** (1 paper: [3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark](https://aclanthology.org/2025.emnlp-main.1353.pdf))
> The quality of the model’s consultation dialogue, including how well it communicates and conducts the interaction during a medical consultation.

## Relationships

### Conversational ability →
- **MT-Bench** (measurement instrument): *measured_by*, 10 papers
  > General tasks: like MT-Bench [15, 42] and AlpacaEval [43], encompass categories such as writing, role-playing, and mathematics, highlighting the models’ comprehensive abilities and multi-turn dialogue performance. (Section 2.1)
  - [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf)
  - [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf)
  - [Tamper-Resistant Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc49a629d33bc2461ed7a715ce44da68-Paper-Conference.pdf)
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf)
  - [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf)
  - [Improving Model Alignment Through Collective Intelligence of Open-Source Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dr/wang25dr.pdf)
  - [Permutative Preference Alignment from Listwise Ranking of Human Judgments](https://aclanthology.org/2025.emnlp-main.17.pdf)
  - [FuseChat: Knowledge Fusion of Chat Models](https://aclanthology.org/2025.emnlp-main.1096.pdf)
  - [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://aclanthology.org/2025.emnlp-main.583.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 3 papers
  > We conduct GPT-4-based automatic evaluation on AlpacaEval 2.0 (Li et al., 2023b), MT-Bench (Zheng et al., 2023), and Arena-Hard (Li et al., 2024) to measure the chatbot capability of our model.
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf)
  - [DPO Meets PPO: Reinforced Token Optimization for RLHF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25b/zhong25b.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 3 papers
  > In this section we evaluate the Jamba-1.5 models on two chatbot scenarios: Arena-Hard (Li et al., 2024b), a set of 500 challenging user queries that uses GPT4-Turbo as a judge, and WildBench (Lin et al., 2024)... (Section 7.3)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [DPO Meets PPO: Reinforced Token Optimization for RLHF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25b/zhong25b.pdf)
- **Chatbot Arena** (measurement instrument): *measured_by*, 2 papers
  > We then report results from live interactions with users on the Chatbot Arena. (Section 7.3)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf)
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > In this section we evaluate the Jamba-1.5 models on two chatbot scenarios: Arena-Hard (Li et al., 2024b), a set of 500 challenging user queries that uses GPT4-Turbo as a judge, and WildBench (Lin et al., 2024)... (Section 7.3)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **MixEval** (measurement instrument): *measured_by*, 1 paper
  > For generalist chat capabilities, we use MixEval, AlpacaEval2, and MTBench with GPT-4o-mini as the judge LLM (Ni et al., 2024; Dubois et al., 2024; Zheng et al., 2023). (Section 3.1)
  - [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf)
- **3MDBench** (measurement instrument): *measured_by*, 1 paper
  > 3MDBench ... evaluates diagnostic accuracy and dialogue quality via Assessor Agent.
  - [3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark](https://aclanthology.org/2025.emnlp-main.1353.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 1 paper
  > In the General Benchmark pipeline, we evaluate our models using two widely recognized benchmarks: AlpacaEval (Li et al., 2023) and MT-Bench (Zheng et al., 2023), which assess the model’s comprehensive conversational abilities across various questions. (Section 6)
  - [Permutative Preference Alignment from Listwise Ranking of Human Judgments](https://aclanthology.org/2025.emnlp-main.17.pdf)

### Associated with
- **Visual question answering** (behavioral indicator), 1 paper
  > We evaluate ChatVLA across three dimensions: conversational ability (visual question answering), general multimodal understanding, and general robot control. (Section 1)
  - [ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://aclanthology.org/2025.emnlp-main.273.pdf)
- **Turn-taking prediction** (behavioral indicator), 1 paper
  > "NTPP, significantly improves the conversational abilities of SLMs in terms of turn-taking prediction"
  - [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf)
- **Coherence** (construct), 1 paper
  > "NTPP, significantly improves the conversational abilities of SLMs in terms of turn-taking prediction, response coherence, and naturalness"
  - [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf)
- **Naturalness** (construct), 1 paper
  > "NTPP, significantly improves the conversational abilities of SLMs in terms of turn-taking prediction, response coherence, and naturalness"
  - [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf)
