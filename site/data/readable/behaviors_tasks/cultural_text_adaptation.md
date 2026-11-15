# Cultural text adaptation
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Cultural context adaptation, Cultural adaptation  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this behavior as modifying text or dialogue so it aligns with a target culture's linguistic, social, and conceptual norms, entities, and expectations. The most specific formulation describes transforming source-culture text into target-culture text by replacing culturally grounded entities while preserving semantic intent, while a smaller formulation narrows the task to recontextualizing educational materials for the cultural and social norms of different regions. In dialogue work, adapted outputs are framed as culturally adapted slot substitutions similar to those made by human annotators.

**Variants.** Papers use several names for related variants, including cultural context adaptation, cultural text adaptation, and cultural adaptation. The settings range from educational materials and source-to-target adaptation such as American-to-Indian text adaptation, to multilingual dialogue localization that changes names, locations, brands, and references, and to Arabic and English CAMeL-2 contexts where adaptation is examined through preferences for Arab versus Western entities in [MASK] token fillings. One paper reports that cultural text adaptation is related to Text infilling through this [MASK] token filling setup.

**Space of elicitation and scores.** Papers link this behavior to 2 measurement instruments: Human evaluation and LLM-as-a-judge. In the linked evaluation setup, adaptations on a cultural text adaptation task are evaluated with an LLM as Judge and with human evaluations from diverse socio-demographic region.

**What it is taken as evidence of.** No construct is linked to this behavior as evidence of in the papers.

## Sources

**Cultural context adaptation** (1 paper: [Position: LLMs Can be Good Tutors in English Education](https://aclanthology.org/2025.emnlp-main.885.pdf))
> The observable task of recontextualizing educational materials to reflect the cultural and social norms of different regions.

**Cultural text adaptation** (1 paper: [DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context](https://aclanthology.org/2025.emnlp-main.1706.pdf))
> The observable process of modifying a text from a source cultural context (e.g., American) to align with a target cultural context (e.g., Indian) by replacing culturally grounded entities while preserving semantic intent.

**Cultural adaptation** (2 papers: [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.326.pdf), [Multilingual Dialogue Generation and Localization with Dialogue Act Scripting](https://aclanthology.org/2025.emnlp-main.1670.pdf))
> The ability of a language model to appropriately handle and generate text that aligns with specific cultural contexts, norms, and entities.

## Relationships

### Cultural text adaptation →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > To measure the cultural competence of LLMs on a cultural text adaptation task, we evaluate the adaptations using the CSIs created, LLM as Judge, and human evaluations from diverse socio-demographic region. (Abstract)
  - [DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context](https://aclanthology.org/2025.emnlp-main.1706.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > To measure the cultural competence of LLMs on a cultural text adaptation task, we evaluate the adaptations using the CSIs created, LLM as Judge, and human evaluations from diverse socio-demographic region. (Abstract)
  - [DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context](https://aclanthology.org/2025.emnlp-main.1706.pdf)

### Associated with
- **Text infilling** (behavioral indicator), 1 paper
  > We compare the ability of LMs at adapting to cultural contexts in Arabic and English by analyzing their preference for Arab vs. Western entities as [MASK] token fillings of CAMeL-2 contexts. (Section 3.2)
  - [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.326.pdf)
