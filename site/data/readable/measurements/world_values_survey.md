# World Values Survey
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** World Values Survey (WVS)  

## State of the Field

**What it is.** Across papers, the prevailing usage treats the World Values Survey as a large-scale cross-national survey, or global research project, about beliefs and values worldwide, spanning social, political, religious, cultural, personal, and societal values. Papers commonly use it as seed data or a source of seed questions for culture-specific generation, and some also describe it as a proxy for cultural values in NLP, repurpose it as training data for cultural adaptation, or use it to derive representative personas. Where versions are specified, authors focus on Wave 7, conducted from 2017 to 2020 and covering 57 countries; reported subsets include 260 questions across 13 cultural topics and a filtered set of 206 questions, and one description notes more than 129K human respondents.

**What it is claimed to measure.** Papers link it to 3 constructs and no behavioral indicators. The most common claim is that it measures cultural alignment, with authors using it for assessment and for comparing model responses to human survey data; a smaller line of work uses it to measure value orientation by treating it as ground-truth human value distributions across countries. It is also related to cultural bias, with one paper saying that insights from WVS can help in understanding the cultural and societal norms that underlie biases.

**Space of uses.** No measurement instrument is linked to it. In use, papers position it as a source of seed questions for data generation, as an assessment reference that compares model responses with human survey data, as training data for cultural value adaptation, and as material for deriving personas and adapting questions into local-language multiple-choice evaluations. Some papers mention it alongside Global Attitudes surveys as another question source, and one evaluation places it alongside Hofstede's Cultural Dimensions.

**Concerns raised.** One paper narrows WVS to a 206-question subset by excluding items that are not independent of other questions or that are customized with respondent-specific demographic information.

## Sources

**World Values Survey** (3 papers: [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf), [Self-Pluralising Culture Alignment for Large Language Models](https://aclanthology.org/2025.naacl-long.350.pdf), [Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?](https://aclanthology.org/2025.emnlp-main.7.pdf))
> A cross-national survey used here as seed data for culture-specific question-answer pairs about social, political, religious, and cultural values.

**World Values Survey (WVS)** (3 papers: [CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf), [From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs](https://aclanthology.org/2025.emnlp-main.912.pdf), [NileChat: Towards Linguistically Diverse and Culturally Aware LLMs for Local Communities](https://aclanthology.org/2025.emnlp-main.556.pdf))
> A global research project and survey that explores people’s beliefs and values worldwide, used in this paper as a source of seed questions for data generation.

## Relationships

### → World Values Survey
- **Cultural alignment** (construct): *measured_by*, 3 papers
  > We utilize the World Values Survey (WVS) (Haerpfer et al., 2022) for our assessment. (Section 3.3)
  - [Self-Pluralising Culture Alignment for Large Language Models](https://aclanthology.org/2025.naacl-long.350.pdf)
  - [Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs](https://aclanthology.org/2025.emnlp-main.2.pdf)
  - [From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs](https://aclanthology.org/2025.emnlp-main.912.pdf)
- **Value orientation** (construct): *measured_by*, 1 paper
  > We use the seventh wave of the World Values Survey (Haerpfer et al., 2022), which asks more than 129K human respondents from a wide range of demographic groups for their values. (Section 6)
  - [Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?](https://aclanthology.org/2025.emnlp-main.7.pdf)

### Associated with
- **Cultural bias** (construct), 1 paper
  > Insights from the WVS can help in understanding the cultural and societal norms that underlie biases
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
