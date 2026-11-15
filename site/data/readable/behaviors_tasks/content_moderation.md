# Content moderation
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats content moderation as an observable policy-compliance behavior: filtering, blocking, or altering user-generated or model-generated content, either before or after generation. A smaller formulation narrows it to classifying a given text, such as a user prompt or model response, as safe or unsafe under a defined policy. One paper also notes that generative AI "tends to use invisible content moderation more than social media" and describes models as being built and fine-tuned to avoid providing dangerous information.

**Variants.** Papers study content moderation at multiple points in the interaction, on user prompts, on model responses, and as moderation that can happen before or after content is generated. One paper treats it as a cross-cultural, zero-shot family of tasks, evaluating detection of hate speech, offensive language, spam speech, abusive speech, bias speech, threat speech, and stance of speech across 8 cultures. In the recorded relationships, it is also related to harmful content detection and to hate speech detection.

**Space of elicitation and scores.** Papers link content moderation to 4 measurement instruments, all through measured_by relationships. The most frequently linked are OpenAI Moderation API, OpenAI Moderation dataset, WildGuardMix, and XSTest. The linked instruments include an API that one study uses to "tag all conversations" and instruments used in reporting average harmfulness F1 scores.

**What it is taken as evidence of.** No construct is linked to content moderation, so the papers do not present a shared claim about what construct this behavior indicates.

## Sources

**Content moderation** (2 papers: [Position: Generative AI Regulation Can Learn from Social Media Regulation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/appel25a/appel25a.pdf), [AEGIS2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails](https://aclanthology.org/2025.naacl-long.306.pdf))
> The observable act of filtering, blocking, or altering user or model-generated content to comply with policies, which may occur before or after content is generated.

## Relationships

### Content moderation →
- **OpenAI Moderation API** (measurement instrument): *measured_by*, 1 paper
  > "We utilize the OpenAI moderation API4 (Markov et al., 2023) to tag all conversations."
  - [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf)
- **WildGuardMix** (measurement instrument): *measured_by*, 1 paper
  > Additionally, it performs on par with WILDGUARD (Han et al., 2024) in terms of average harmfulness F1 scores across WILDGUARDTEST (Han et al., 2024), XSTest (Röttger et al., 2023; Han et al., 2024), and the OpenAI Moderation Dataset (Markov et al., 2023). (Section 5)
  - [AEGIS2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails](https://aclanthology.org/2025.naacl-long.306.pdf)
- **XSTest** (measurement instrument): *measured_by*, 1 paper
  > Additionally, it performs on par with WILDGUARD (Han et al., 2024) in terms of average harmfulness F1 scores across WILDGUARDTEST (Han et al., 2024), XSTest (Röttger et al., 2023; Han et al., 2024), and the OpenAI Moderation Dataset (Markov et al., 2023). (Section 5)
  - [AEGIS2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails](https://aclanthology.org/2025.naacl-long.306.pdf)
- **OpenAI Moderation dataset** (measurement instrument): *measured_by*, 1 paper
  > Additionally, it performs on par with WILDGUARD (Han et al., 2024) in terms of average harmfulness F1 scores across WILDGUARDTEST (Han et al., 2024), XSTest (Röttger et al., 2023; Han et al., 2024), and the OpenAI Moderation Dataset (Markov et al., 2023). (Section 5)
  - [AEGIS2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails](https://aclanthology.org/2025.naacl-long.306.pdf)

### Associated with
- **Hate speech detection** (behavioral indicator), 1 paper
  > We evaluate on 7 content moderation tasks for 8 different cultures to detect the following content: hate speech, offensive language, spam speech, abusive speech, bias speech, threat speech, and stance of speech in zero-shot evaluation (Section 4.1)
  - [CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf)
- **Harmful content detection** (behavioral indicator), 1 paper
  > We evaluate on 7 content moderation tasks for 8 different cultures to detect the following content: hate speech, offensive language, spam speech, abusive speech, bias speech, threat speech, and stance of speech in zero-shot evaluation (Section 4.1)
  - [CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf)
