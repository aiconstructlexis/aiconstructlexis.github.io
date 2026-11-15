# Personalized response generation
**Type:** Behavioral indicator  
**Supporting papers:** 9  
**Also known as:** Speaker-specific response generation, Personalized generation, Personalized review generation, Personalized text generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a task of generating user-tailored natural language responses for a specific person, usually by reflecting that person's preferred style, content, tone, background, or prior interactions. FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data describes it as generating "user-tailored responses for unseen contexts" from preferences derived from a shared questionnaire, while other papers treat successful outputs as replies that incorporate profile details, schedules, dialogue history, or a user image, or as speaker-specific replies in multi-party dialogue. A smaller line of work narrows the task to item review generation, or to outputs that maximize expected personalized utility across dimensions such as helpfulness, harmlessness, or humor.

**Variants.** Variants span several settings and names. Papers refer to speaker-specific response generation in multi-party dialogue, personalized response generation for conversational assistants that use dialogue history, profile, schedule, or long-term interactions, personalized text generation in open-ended tasks, personalized review generation for products or items, and personalized system utterances in task-oriented dialogue with image persona; some definitions also allow text or speech outputs rather than text alone.

**Space of elicitation and scores.** It is measured by 3 instruments. The most frequently linked instrument is LLM-as-a-judge, used for a 5-point personalization score and pairwise-comparison win rate in one line of work, and another paper also reports GPT judging alongside human judges; the other linked instruments are Amazon Reviews 2023, used for personalized review generation, and Human evaluation. The linked instruments therefore include judge-based scoring as well as a dataset-based setup.

**What it is taken as evidence of.** No construct is linked to this behavior, so the recorded relationships do not specify what construct papers take it to indicate.

## Sources

**Speaker-specific response generation** (1 paper: [PACHAT: Persona-Aware Speech Assistant for Multi-party Dialogue](https://aclanthology.org/2025.emnlp-main.1492.pdf))
> The observable generation of replies that are explicitly directed at and tailored for a particular speaker in a multi-party conversation.

**Personalized generation** (1 paper: [FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475.pdf))
> The observable task of generating text responses that are tailored to a specific user's preferences for previously unseen contexts or questions.

**Personalized response generation** (5 papers: [FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475.pdf), [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf), [Comparison-based Active Preference Learning for Multi-dimensional Personalization](https://aclanthology.org/2025.acl-long.1590.pdf), [Exploring the Potential of LLMs as Personalized Assistants: Dataset, Evaluation, and Analysis](https://aclanthology.org/2025.acl-long.504.pdf), [PicPersona-TOD : A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.403.pdf))
> Producing natural language responses that reflect a specific user's preferred style, content, or tone, as inferred from their past choices in a questionnaire.

**Personalized review generation** (1 paper: [Latent Inter-User Difference Modeling for LLM Personalization](https://aclanthology.org/2025.emnlp-main.536.pdf))
> The specific task of generating a product or item review that reflects a particular user's writing style, opinions, and preferences.

**Personalized text generation** (1 paper: [Personalized LLM Decoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1723.pdf))
> The observable task of generating text that is tailored to a specific user's style, preferences, and historical data.

## Relationships

### Personalized response generation →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > PAChat achieves the best results across all metrics, demonstrating significant improvements in personalized response generation and particularly winning favor with both GPT and human judges. (Section 5.3.1)
  - [PACHAT: Persona-Aware Speech Assistant for Multi-party Dialogue](https://aclanthology.org/2025.emnlp-main.1492.pdf)
  - [FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475.pdf)
- **Amazon Reviews 2023** (measurement instrument): *measured_by*, 1 paper
  > Building upon prior work, we focus on the representative task of item review generation for LLM personalization (Ni et al., 2019; Peng et al., 2024; Kumar et al., 2024; Au et al., 2025). Specifically, we adopt the Amazon Reviews 2023 dataset (Section 4.1)
  - [Latent Inter-User Difference Modeling for LLM Personalization](https://aclanthology.org/2025.emnlp-main.536.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > PAChat achieves the best results across all metrics, demonstrating significant improvements in personalized response generation and particularly winning favor with both GPT and human judges. (Section 5.3.1)
  - [PACHAT: Persona-Aware Speech Assistant for Multi-party Dialogue](https://aclanthology.org/2025.emnlp-main.1492.pdf)
