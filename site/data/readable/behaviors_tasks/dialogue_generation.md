# Dialogue generation
**Type:** Behavioral indicator  
**Supporting papers:** 41  
**Also known as:** Dialogue response generation, Open-domain dialogue generation, Utterance generation, Conversational response generation, Turn-by-turn response generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is generating a natural-language response in dialogue, usually in a multi-turn setting and conditioned on prior conversation. Many formulations cast it as next-utterance prediction, where the model receives a conversation snippet or dialogue history and must predict the next utterance, while some papers broaden it to single-turn human-assistant exchanges or to responses that synthesize retrieved passages with conversational context. Success is most often described in terms such as relevant, coherent, contextually appropriate, or proper responses, though some papers frame the target through human preferences, especially helpfulness and harmlessness.

**Variants.** Papers use nearby labels such as dialogue response generation, open-domain dialogue generation, conversational response generation, utterance generation, and turn-by-turn response generation. These labels mark settings such as persona-conditioned chat, responses built from retrieved passages or external knowledge, task-oriented responses grounded in dialogue history and retrieved or API information, user and system utterance realization from a predefined logic flow, and client simulations conditioned on state, action, and retrieved profile information. Some studies further narrow the domain to shopping, counseling, empathy, personality-conditioned social interaction, multimodal agent interaction, or single-turn gender-related prompts.

**Space of elicitation and scores.** Dialogue generation is measured by 10 instruments. The most frequently linked are HH-RLHF, MT-Bench, DailyDialog, Wizard of Wikipedia, and Arena-Hard. Across papers, these are mostly dialogue datasets and conversational ability benchmarks, from paired conversations with a human-preferred response and everyday conversation corpora to benchmarks for diverse queries. A smaller number of papers also use interactive, crowd-sourced battles with human participants or zero-shot pairwise judgment by a language model judge.

**What it is taken as evidence of.** No paper links dialogue generation to a construct, so the papers do not specify a named construct that this behavior is evidence of.

## Sources

**Dialogue generation** (16 papers: [Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf), [Confronting Reward Model Overoptimization with Constrained RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf), [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf), [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf), [Statistical Rejection Sampling Improves Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/efea6d3821a7ccae74e58892162164c0-Paper-Conference.pdf), [Make LoRA Great Again: Boosting LoRA with Adaptive Singular Values and Mixture-of-Experts Optimization Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25g/fan25g.pdf), [ECC: An Emotion-Cause Conversation Dataset for Empathy Response](https://aclanthology.org/2025.emnlp-main.306.pdf), [WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games](https://proceedings.neurips.cc/paper_files/paper/2024/file/9dd4533e7e4e5ed809344280609c5b05-Paper-Datasets_and_Benchmarks_Track.pdf), [Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf), [A Systematic Study of Compositional Syntactic Transformer Language Models](https://aclanthology.org/2025.acl-long.350.pdf), [BIG5-CHAT: Shaping LLM Personalities Through Training on Human-Grounded Data](https://aclanthology.org/2025.acl-long.999.pdf), [ChatSOP: An SOP-Guided MCTS Planning Framework for Controllable LLM Dialogue Agents](https://aclanthology.org/2025.acl-long.863.pdf), [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf), [GenderAlign: An Alignment Dataset for Mitigating Gender Bias in Large Language Models](https://aclanthology.org/2025.acl-long.553.pdf), [Wizard of Shopping: Target-Oriented E-commerce Dialogue Generation with Decision Tree Branching](https://aclanthology.org/2025.acl-long.641.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf))
> Generating responses in a multi-turn conversational setting.

**Dialogue response generation** (3 papers: [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf), [SQLWOZ: A Realistic Task-Oriented Dialogue Dataset with SQL-Based Dialogue State Representation for Complex User Requirements](https://aclanthology.org/2025.emnlp-main.383.pdf), [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf))
> Producing conversational responses in multi-turn or single-turn dialogue settings that address user queries while balancing helpfulness and harmlessness.

**Open-domain dialogue generation** (1 paper: [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf))
> Generating responses in multi-turn conversations conditioned on persona profiles and dialogue history.

**Utterance generation** (1 paper: [From Schema to State: Zero-Shot Scheme-Only Dialogue State Tracking via Diverse Synthetic Dialogue and Step-by-Step Distillation](https://aclanthology.org/2025.emnlp-main.85.pdf))
> The specific task of generating the natural language text for user and system turns in a dialogue, based on a predefined scenario and logic flow.

**Conversational response generation** (4 papers: [UniConv: Unifying Retrieval and Response Generation for Large Language Models in Conversations](https://aclanthology.org/2025.acl-long.344.pdf), [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf), [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf), [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf))
> The task of synthesizing information from retrieved passages and conversational context to generate a natural language response to a user's query in a multi-turn setting.

**Turn-by-turn response generation** (1 paper: [Consistent Client Simulation for Motivational Interviewing-based Counseling](https://aclanthology.org/2025.acl-long.1021.pdf))
> Generating one client utterance at a time in response to the counselor, conditioned on state, selected action, and retrieved profile information.

## Relationships

### Dialogue generation →
- **HH-RLHF** (measurement instrument): *measured_by*, 9 papers
  > We also evaluate on the validation split of the Anthropic’s Helpful and Harmless (HH) dataset (Ganguli et al., 2022; Bai et al., 2022a), where where each example comprises a pair of conversations between a human and a large language model, with one of the two conversations preferred by a human.
  - [Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
  - [MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ddab70bf41ffe5d423840644d3357f4-Paper-Conference.pdf)
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)
  - [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf)
  - [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf)
  - [BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling](https://proceedings.neurips.cc/paper_files/paper/2024/file/056521a35eacd9d2127b66a7d3c499c5-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 3 papers
  > For the dialogue generation task, we fine-tune the Llama-2-7B (Touvron et al., 2023) model on a 52k subset of the WizardLM dataset (Xu et al., 2024) and evaluate it using the MT-Bench dataset (Zheng et al., 2024a).
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [Make LoRA Great Again: Boosting LoRA with Adaptive Singular Values and Mixture-of-Experts Optimization Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25g/fan25g.pdf)
  - [Flat-LoRA: Low-Rank Adaptation over a Flat Loss Landscape](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25x/li25x.pdf)
- **DailyDialog** (measurement instrument): *measured_by*, 2 papers
  > we focus on a single setting as a case study: dialogue generation with the DailyDialog (Li et al., 2017) dataset
  - [Confronting Reward Model Overoptimization with Constrained RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf)
  - [Compressed Context Memory for Online Language Model Interaction](https://proceedings.iclr.cc/paper_files/paper/2024/file/97dc07f1253ab33ee514f395a82fa7cc-Paper-Conference.pdf)
- **Wizard of Wikipedia** (measurement instrument): *measured_by*, 2 papers
  > Table 2: Accuracy on various long-form NLP tasks. ... Dialogue ... Wow (Table 2)
  - [A Theory for Token-Level Harmonization in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a461bdff86cc07e976bb6c518810398-Paper-Conference.pdf)
  - [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > For the dialogue generation and summarization tasks, we use GPT-4 for zero-shot pairwise evaluation, which is consistent with human judgments (see prompts in Appendix C.2.1). (Section 5.1)
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
- **Chatbot Arena** (measurement instrument): *measured_by*, 1 paper
  > Chatbot Arena is a benchmark platform designed for evaluating LLMs through interactive, randomised battles in a crowd-sourced manner. It allows for the assessment of LLMs in real-time dialogues with human participants. (Section 3.3)
  - [Weak-eval-Strong: Evaluating and Eliciting Lateral Thinking of LLMs with Situation Puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/914b372356d58d9e9357b29332cb8fdc-Paper-Conference.pdf)
- **Databricks Dolly-15k** (measurement instrument): *measured_by*, 1 paper
  > ...and Dolly (Conover et al., 2023) datasets as the dialogue generation task. (Section 3.3)
  - [Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf)
- **UltraFeedback** (measurement instrument): *measured_by*, 1 paper
  > We further conduct experiments on tasks such as conditional generation (IMDB) and dialogue (Anthropic HH, UltraFeedback). (Section 5)
  - [MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ddab70bf41ffe5d423840644d3357f4-Paper-Conference.pdf)
- **ConvAI2** (measurement instrument): *measured_by*, 1 paper
  > Open-domain Dialogue Generation. We use the ConvAI2 dataset (Dinan et al., 2019)... (Section 5.1)
  - [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 1 paper
  > These benchmarks assess the models’ conversational abilities across a diverse range of queries and are extensively used by the research community.
  - [AlphaDPO: Adaptive Reward Margin for Direct Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25af/wu25af.pdf)
