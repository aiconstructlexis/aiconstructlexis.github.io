# Role-playing
**Type:** Behavioral indicator  
**Supporting papers:** 29  
**Also known as:** Human-role dialogue, Inter-role dialogue, Commentary interaction, Role playing, Perspective simulation, Persona adoption, Character portrayal, Survey response generation, Patient response simulation, Classroom simulation, Student simulation, AI persona, Persona-based role-playing, Character simulation, Role-playing dialogue generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is adopting and maintaining a specified persona, character, or role in interaction, most often in conversation. Definitions repeatedly emphasize responses that stay consistent with the assigned persona, and some make that consistency more specific through fidelity to a target persona, adherence to goals, traits, private information, speaking style, or narrative coherence. A smaller line of work extends the behavior beyond named characters to generating text from specified viewpoints or respondent identities, such as lawmakers, news outlets, patients, or survey participants.

**Variants.** Papers study both general role-play and several specialized settings. One recurring multimodal line breaks it into image-centered commentary interaction, human-role dialogue, and inter-role dialogue, differing by whether the exchange is single-turn or multi-turn and whether the partner is a user or another character. Other variants include sequential multi-character prompting for step-by-step instructions, perspective simulation, and domain-specific simulations in social science, drama, surveys, medicine, and education.

**Space of elicitation and scores.** Role-playing is measured by one linked instrument, WildBench. In that benchmark, it appears as one task category within a broader collection of user-facing tasks, described alongside writing assistance, coding, mathematics, data analysis, and planning.

**What it is taken as evidence of.** The only linked construct is Controllability, and the recorded relationship is that role-playing is related to it: one paper defines persona steerability as the degree to which a model can be made to adopt different personas by prompting alone. Separately, one paper claims a causal relationship from Role-playing to Jailbreaking, describing sequential characters as a way to bypass safety guardrails and obtain step-by-step instructions.

## Sources

**Role-playing** (8 papers: [How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions](https://proceedings.iclr.cc/paper_files/paper/2024/file/efe79ae16496a0f5b57287873de072d1-Paper-Conference.pdf), [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf), [SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3075b88e583a0e98d8b24338a613060-Paper-Conference.pdf), [GuideLLM: Exploring LLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.287.pdf), [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf), [AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios](https://aclanthology.org/2025.naacl-long.257.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [EmoAgent: Assessing and Safeguarding Human-AI Interaction for Mental Health Safety](https://aclanthology.org/2025.emnlp-main.594.pdf))
> The behavior of adopting a specified persona or character in a conversational interaction.

**Role playing** (2 papers: [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf), [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf))
> Adopting a specific persona or character in conversation with the user.

**Commentary interaction** (1 paper: [MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf))
> A single-turn dialogue task where an agent, acting as a character, provides comments or reflections about a given image without further interaction.

**Human-role dialogue** (1 paper: [MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf))
> Multi-turn dialogues centered around an image between a human user without a specific identity and a character.

**Inter-role dialogue** (1 paper: [MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf))
> A multi-turn dialogue task where an agent, acting as one character, converses with another character about a given image.

**Perspective simulation** (1 paper: [Linear Representations of Political Perspective Emerge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1557cc3e1a67f985dbdb162db9963dd0-Paper-Conference.pdf))
> The observable action of generating text mimicking the viewpoint of specific entities like lawmakers or news outlets.

**Persona adoption** (2 papers: [A transfer learning framework for weak to strong generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa47ffc7b2033fd32d8b8734686f6ff4-Paper-Conference.pdf), [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf))
> The observable task of generating text that consistently embodies a specified character or style, such as a pirate persona.

**Character portrayal** (1 paper: [CoSER: Coordinating LLM-Based Persona Simulation of Established Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dk/wang25dk.pdf))
> The specific act of a language model generating utterances, actions, and thoughts for a single assigned character within a conversation.

**Survey response generation** (1 paper: [SocioBench: Modeling Human Behavior in Sociological Surveys with Large Language Models](https://aclanthology.org/2025.emnlp-main.1335.pdf))
> Producing answer options to closed-ended sociological survey questions as if the model were a human respondent.

**Patient response simulation** (1 paper: [DDO: Dual-Decision Optimization for LLM-Based Medical Consultation via Multi-Agent Collaboration](https://aclanthology.org/2025.emnlp-main.1340.pdf))
> The observable behavior of simulating patient responses to symptom inquiries, either from recorded data or inferred based on disease-symptom associations when information is missing.

**Student simulation** (1 paper: [Position: LLMs Can be Good Tutors in English Education](https://aclanthology.org/2025.emnlp-main.885.pdf))
> Producing synthetic learner behavior that imitates students with different competency levels and learning trajectories.

**Classroom simulation** (1 paper: [Position: LLMs Can be Good Tutors in English Education](https://aclanthology.org/2025.emnlp-main.885.pdf))
> Using LLM agents to simulate virtual students and tutors in interactive learning environments for pedagogical research and system training.

**AI persona** (1 paper: [Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf))
> A consistent style of response, character, or set of goals that an LLM adopts across different interactions.

**Persona-based role-playing** (1 paper: [SCALE: Towards Collaborative Content Analysis in Social Science with Large Language Model Agents and Human Intervention](https://aclanthology.org/2025.acl-long.416.pdf))
> LLM agents adopting distinct social scientist personas (with defined demographics, values, beliefs) to simulate diverse human perspectives during coding and discussion.

**Character simulation** (1 paper: [Towards Enhanced Immersion and Agency for LLM-based Interactive Drama](https://aclanthology.org/2025.acl-long.546.pdf))
> The observable behavior of LLM agents in role-playing dramatic characters, responding to player input while maintaining narrative coherence and character-specific motivations.

**Role-playing dialogue generation** (1 paper: [Crab: A Novel Configurable Role-Playing LLM with Assessing Benchmark](https://aclanthology.org/2025.acl-long.731.pdf))
> Producing multi-turn conversational responses that reflect a specified character's profile, scenario, and speaking style.

## Relationships

### Role-playing →
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Jailbreaking** (behavioral indicator): *causes*, 1 paper
  > Inspired by previous attempts that exploit role-playing to bypass the safety guardrails of LLMs (DAN, 2023; Li et al., 2024) and research on the distraction phenomenon in LLMs (Shi et al., 2023; Xiao et al., 2024), we apply sequential jailbreak characters within a single user query and ask the target LLMs to act as these characters sequentially to provide step-by-step instructions. (Section 2.1)
  - [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf)

### Associated with
- **Controllability** (construct), 1 paper
  > Prompt steerability of a model’s persona describes the degree to which a model can be made to adopt different personas by prompting alone. (Section 3)
  - [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf)
