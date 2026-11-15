# Personalization
**Type:** Construct  
**Supporting papers:** 50  
**Also known as:** Personalization capability, Preference following, Preference inference, Adaptive interaction  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats personalization as a latent ability to tailor model outputs, responses, or content to a user's unique needs and preferences, often by drawing on historical interactions, user profiles, or other contextual signals. Most papers stay with this broad response-centered framing, while smaller lines of work define it more narrowly as adapting predictions to author, addressee, or reader attributes, adapting model performance to a client's data and application needs, or conducting multimodal conversations about specific individuals or subjects. A further narrowing appears in definitions of preference inference and preference following, which focus on inferring, memorizing, and adhering to user preferences over long conversations. Across these definitions, the main variation is who the adaptation targets, an individual user, a community, a client, or social groups, and what is adapted, predictions, response style, conversations, or overall performance.

**Space of facets.** Papers often break the construct into narrower capabilities rather than use a single undifferentiated notion. One line distinguishes preference inference from preference following, with the latter defined as generating contextually relevant responses aligned with a known preference, while another uses personalization capability for conversations that correctly identify and reference specific individuals presented in context. Other variants specialize the target of personalization: personalized utterance style through greetings, formality, age sensitivity, and emotional awareness, community-level alignment with norms and values, subject-specific conversations from a few examples, and adaptive interaction framed as personalized results or adjusted conversational tone. As a result, the same name is used for several scopes, from individual preference alignment to community adaptation and client-specific tuning.

**Space of measurement.** Papers link personalization to 5 measurement instruments and 3 behavioral indicators. The most common instrument is LLM-as-a-judge: papers ask a model to rate responses for helpfulness and relevance to user preferences, assess travel plans for preference alignment, or score the similarity between inferred and true preference descriptions on a 5-point Likert scale. Other operationalizations use benchmarks, Caltech101 in visual classification settings that study personalization alongside generalization and privacy, and OpinionQA and GlobalOpinionQA as multiple-choice QA datasets for steerability toward specific users or social groups, plus human evaluation through a user study. These operationalizations mostly track preference alignment or user-specific steerability, though some measure it in broader visual classification settings; the linked behavioral indicators are catastrophic forgetting, synthetic recall, and visual question answering.

**Links.** Papers report no correlational links, but they do describe several causal and related connections. Papers claim causal relationships from in-context learning, expressive power, and synthetic recall to personalization, and one paper also claims a causal relationship from privacy preservation to personalization, with recorded claims that in-context learning allows adaptation to new individuals without additional training, retained expressiveness preserves client-specific learning and improves personalization, retrieval capabilities underlie adherence to user preferences, and stringent privacy measures can hinder personalization. One paper also claims a causal relationship from personalization to visual question answering, stating that after personalization a model can answer visual questions about the subject. Separately, personalization is related to generalization, long-context understanding, catastrophic forgetting, and robustness, usually in discussions of balancing personalized behavior with broader model knowledge or transfer to new individuals.

## Sources

**Personalization** (11 papers: [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf), [Towards Unified Multi-Modal Personalization: Large Vision-Language Models for Generative Recommendation and Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/297a7a54da76d95f02b04d957a53c7ba-Paper-Conference.pdf), [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf), [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf), [PicPersona-TOD : A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.403.pdf), [Hello Again! LLM-powered Personalized Agent for Long-term Dialogue](https://aclanthology.org/2025.naacl-long.272.pdf), [Few-shot Personalization of LLMs with Mis-aligned Responses](https://aclanthology.org/2025.naacl-long.598.pdf), [ComPO: Community Preferences for Language Model Personalization](https://aclanthology.org/2025.naacl-long.419.pdf), [Whose Boat Does it Float? Improving Personalization in Preference Tuning via Inferred User Personas](https://aclanthology.org/2025.acl-long.168.pdf), [On-Device Collaborative Language Modeling via a Mixture of Generalists and Specialists](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25h/fan25h.pdf), [LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60.pdf))
> The ability to tailor responses and content to a user's unique needs and preferences by understanding their historical interactions.

**Personalization capability** (1 paper: [Personalized Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b69dcf999ee89f48d08c6c9881a4c0d-Paper-Conference.pdf))
> The latent ability of a multimodal model to conduct personalized conversations that correctly identify and reference specific individuals presented in context.

**Preference following** (1 paper: [Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/28a46044775d97a4efcbcf14e7f13209-Paper-Conference.pdf))
> The latent ability of a model to infer, memorize, and generate responses that adhere to user preferences expressed over a long-context conversation.

**Preference inference** (1 paper: [Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/28a46044775d97a4efcbcf14e7f13209-Paper-Conference.pdf))
> The latent ability to infer a user's preferences from explicit statements or indirect conversational evidence.

**Adaptive interaction** (1 paper: [Humanizing Machines: Rethinking LLM Anthropomorphism Through a Multi-Level Framework of Design](https://aclanthology.org/2025.emnlp-main.164.pdf))
> The model's ability to modify its responses based on context or user history, such as personalizing results or adjusting conversational tone.

## Relationships

### Personalization →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 3 papers
  > “We further explore whether we can employ language models to automate the evaluation... we ask GPT-4 to rate the responses based on their helpfulness and relevance to users’ preferences.”
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
  - [Personal Travel Solver: A Preference-Driven LLM-Solver System for Travel Planning](https://aclanthology.org/2025.acl-long.1339.pdf)
  - [Aligning LLMs by Predicting Preferences from User Writing Samples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aroca-ouellette25a/aroca-ouellette25a.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > To show that CoS’s personalization aligns with end-users, we conduct a user study with 15 participants. (Sec 3.1)
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
- **Visual question answering** (behavioral indicator): *causes*, 1 paper
  > After being personalized, our method (Yo’LLaVA) can: ... (2) support visual question answering about the subject (e.g., given a new photo, one can ask about <sks>’s location); (Section 3)
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **Caltech101** (measurement instrument): *measured_by*, 1 paper
  > We select four visual classification datasets to investigate the task of balancing personalization, generalization and privacy: Caltech101 (Fei-Fei et al., 2004) (Section 4.1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **OpinionQA** (measurement instrument): *measured_by*, 1 paper
  > For the experiments, we first use two multiple-choice QA datasets proposed to measure the steerability of LLMs for specific users (or social groups): OpinionQA (Santurkar et al., 2023) and GlobalOpinionQA (Durmus et al., 2023). (Section 4.1)
  - [Few-shot Personalization of LLMs with Mis-aligned Responses](https://aclanthology.org/2025.naacl-long.598.pdf)
- **GlobalOpinionQA** (measurement instrument): *measured_by*, 1 paper
  > For the experiments, we first use two multiple-choice QA datasets proposed to measure the steerability of LLMs for specific users (or social groups): OpinionQA (Santurkar et al., 2023) and GlobalOpinionQA (Durmus et al., 2023). (Section 4.1)
  - [Few-shot Personalization of LLMs with Mis-aligned Responses](https://aclanthology.org/2025.naacl-long.598.pdf)

### → Personalization
- **Privacy preservation** (construct): *causes*, 2 papers
  > stringent privacy measures, such as differential privacy, can hinder both personalization and generalization (Abstract).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
  - [Personalized Generation In Large Model Era: A Survey](https://aclanthology.org/2025.acl-long.1201.pdf)
- **Synthetic recall** (behavioral indicator): *causes*, 1 paper
  > RAG consistently performed the best across most models, indicating that adherence to user preferences may hinge on retrieval capabilities.
  - [Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/28a46044775d97a4efcbcf14e7f13209-Paper-Conference.pdf)
- **Expressive power** (construct): *causes*, 1 paper
  > The residual term is crucial for retaining the expressiveness lost during the factorization process, thereby preserving the client-specific learning and improving personalization (Section 1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **In-context learning** (construct): *causes*, 1 paper
  > This approach fully harnesses the in-context learning capabilities of MLLMs, allowing them to adapt to new individuals without additional training. (Section 3)
  - [Personalized Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b69dcf999ee89f48d08c6c9881a4c0d-Paper-Conference.pdf)

### Associated with
- **Generalization** (construct), 2 papers
  > FedPGP (Cui et al., 2024): Incorporate a low-rank adaptation term with an additional contrastive loss to balance generalization and personalization.
  - [Federated Disentangled Tuning with Textual Prior Decoupling and Visual Dynamic Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25k/yang25k.pdf)
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator), 1 paper
  > First, when personalizing an LMM, we want to ensure that its broad pre-trained knowledge is unaffected (i.e., there is no catastrophic forgetting [15, 16]). (Section 1)
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **Robustness** (construct), 1 paper
  > the diversity of names used during training makes the personalization capability more robust and generalizable to new individuals. (Section 6.2.3 IMPACT OF DATA SCALE AND NAME REPETITION)
  - [Personalized Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b69dcf999ee89f48d08c6c9881a4c0d-Paper-Conference.pdf)
- **Long-context understanding** (construct), 1 paper
  > (d) Long-context Modeling Capacity (LC): As more exchanges between the user and the LLM occur, more personal information is gradually revealed, while the limited context length of LLMs makes it increasingly challenging for the LLM to integrate information from past interactions. (Section 3)
  - [Exploring the Potential of LLMs as Personalized Assistants: Dataset, Evaluation, and Analysis](https://aclanthology.org/2025.acl-long.504.pdf)
