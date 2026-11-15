# Cultural alignment
**Type:** Construct  
**Supporting papers:** 13  
**Also known as:** Pluralistic culture alignment, Cultural value adaptation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats cultural alignment as correspondence between a model's outputs, responses, judgments, or expressed values and the norms, values, beliefs, and expressions of a specific culture, often contrasted with defaulting to dominant, Western, or Anglospheric perspectives. Papers make this concrete in Arabic social and political settings and in subjective judgments such as hate speech, and one study reports that models "align more closely with annotations from the US than with those from other cultures." A smaller line of work broadens the target to pluralistic culture alignment across diverse human cultures, while another reframes it as cultural value adaptation, a latent ability to align behavior with a specific cultural context beyond mere language use. The main axis of disagreement is therefore specific-culture versus pluralistic scope, and observable outputs or judgments versus a latent behavioral ability.

**Space of facets.** Papers use closely related labels for different slices of the construct. Most commonly, cultural alignment covers responses that respect regional norms and sensitivities, expressed values and preferences inferred from survey answers, and judgments that conform to a group's norms, and some papers also speak of cross-cultural alignment between agents. Alongside this, pluralistic culture alignment names alignment to the shared beliefs, norms, and values of diverse cultures, while cultural value adaptation names a broader ability that should align behavior and "enhance downstream tasks within each culture." Papers also describe it alongside Western, Anglospheric, or US bias.

**Space of measurement.** Papers link cultural alignment to 1 measurement instrument, the World Values Survey, and no behavioral indicator. The most common operationalization is survey-based: papers describe simulating sociological surveys on LLMs and calculating a cultural alignment score from the similarity between model answers and real-world survey answers from a specific culture. Other papers also discuss evaluation with Hofstede's cultural dimensions and with specific cultural proxies, so the measurement space is centered on survey or cultural-dimension frameworks rather than direct behavioral indicators. This largely matches definitions centered on values, beliefs, and norms, though the minority framing of cultural value adaptation as behavior beyond mere language use is broader than the linked instrument.

**Links.** Papers also relate cultural alignment to 2 constructs, cultural bias and social bias. One paper relates it to cultural bias through prior findings that probing for cultural alignment reveals Western bias in encoded world knowledge and values. Another paper relates it to social bias, using the formulation that cultural misalignment can increase bias. No causal or correlational links are recorded.

## Sources

**Cultural alignment** (6 papers: [Arabic Dataset for LLM Safeguard Evaluation](https://aclanthology.org/2025.naacl-long.285.pdf), [Self-Pluralising Culture Alignment for Large Language Models](https://aclanthology.org/2025.naacl-long.350.pdf), [Multi3Hate: Multimodal, Multilingual, and Multicultural Hate Speech Detection with Vision–Language Models](https://aclanthology.org/2025.naacl-long.490.pdf), [The Power of Many: Multi-Agent Multimodal Models for Cultural Image Captioning](https://aclanthology.org/2025.naacl-long.152.pdf), [CulFiT: A Fine-grained Cultural-aware LLM Training Paradigm via Multilingual Critique Data Synthesis](https://aclanthology.org/2025.acl-long.1092.pdf), [Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs](https://aclanthology.org/2025.emnlp-main.2.pdf))
> The extent to which a model's outputs reflect the values, norms, and expressions of a specific cultural context rather than defaulting to dominant (e.g., Western) perspectives.

**Pluralistic culture alignment** (1 paper: [Self-Pluralising Culture Alignment for Large Language Models](https://aclanthology.org/2025.naacl-long.350.pdf))
> The degree to which a model's values and preferences align with the shared beliefs, norms, and values of diverse human cultures.

**Cultural value adaptation** (1 paper: [From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs](https://aclanthology.org/2025.emnlp-main.912.pdf))
> The latent ability of a model to align its behavior with the norms, attitudes, and values of a specific cultural context, beyond mere language use.

## Relationships

### Cultural alignment →
- **World Values Survey** (measurement instrument): *measured_by*, 3 papers
  > We utilize the World Values Survey (WVS) (Haerpfer et al., 2022) for our assessment. (Section 3.3)
  - [Self-Pluralising Culture Alignment for Large Language Models](https://aclanthology.org/2025.naacl-long.350.pdf)
  - [Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs](https://aclanthology.org/2025.emnlp-main.2.pdf)
  - [From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs](https://aclanthology.org/2025.emnlp-main.912.pdf)

### Associated with
- **Cultural bias** (construct), 1 paper
  > “In the language only setting, prior work has probed models for such cultural alignment, finding that they exhibit a Western bias in the world knowledge (Naous et al., 2023) and values (AlKhamissi et al., 2024) they encode.”
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
- **Social bias** (construct), 1 paper
  > AlKhamissi et al. (2024) demonstrate how cultural misalignment can increase bias. (Section 4.2)
  - [Position: LLMs Can be Good Tutors in English Education](https://aclanthology.org/2025.emnlp-main.885.pdf)
