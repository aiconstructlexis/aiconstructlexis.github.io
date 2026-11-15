# Stereotyping
**Type:** Construct  
**Supporting papers:** 23  
**Also known as:** Gender stereotypical bias, Stereotypical association, Occupational gender bias, Stereotypical reasoning, Gender stereotypes, Gender bias, Stereotypes, Gender-occupation bias, Stereotypical bias  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage describes stereotyping as a model tendency to generate, agree with, or otherwise rely on oversimplified, generalized, and often inaccurate beliefs about social groups, especially demographic groups such as gender, ethnicity, religion, or socioeconomic status. Much of the work narrows this broad framing to gender, covering roles, traits, abilities, and occupational associations, and one paper reports models justifying behavior with claims like "men should pay" or "women shouldn't be left alone." A smaller line of work treats it as latent stereotypical reasoning or as systematic task patterns, especially gendered occupation translations, so the main difference is between broad group-level output bias and narrower, often gendered, latent or task-specific formulations.

**Space of facets.** Papers break the construct into recurring subtypes such as gender stereotypical bias, stereotypical association, stereotypical reasoning, and occupational or gender-occupation bias. These labels overlap but are not identical: some refer broadly to reproducing pre-conceived gender roles, characteristics, or abilities, while others focus on associations between occupations and gender, or on prompts about stereotypical personality traits, activities, and preferences. In surrounding taxonomies, stereotyping appears as one component of fairness, as one of two harms under social bias alongside toxicity, and as one trustworthiness vertical.

**Space of measurement.** Operationalization is mostly benchmark-based: papers link stereotyping to 5 measurement instruments, most often CrowS-Pairs and StereoSet, followed by BBQ, DecodingTrust, and LLM-as-a-judge. The benchmarks are described as testing stereotypical associations in paired sentences or context-sentence pairs, with StereoSet covering gender, profession, race, and religion, and CrowS-Pairs assessing stereotypes associated with historically disadvantaged groups; one paper also uses GPT-4 as a judge to score the stereotypical degree of outputs about specific social groups. Papers also connect the construct to 2 behavioral indicators, machine translation and visual question answering, but those are recorded as related settings rather than as measures; overall, the operationalizations line up most directly with definitions framed as output associations and generalized beliefs, and less directly with the minority framing of latent stereotypical reasoning.

**Links.** Papers relate stereotyping to broader taxonomies of fairness, social bias, and trustworthiness: one fairness account breaks fairness into stereotype and bias & preference, one social-bias account organizes harms into stereotyping and toxicity, and one trustworthiness account includes stereotypical bias among its verticals. One paper claims a causal relationship from human preference alignment to stereotyping, reporting that stereotypical bias increases by 150%. It is also related to machine translation, where papers discuss gendered occupation translations, and to one other behavioral setting; no correlation claims are reported.

## Sources

**Stereotyping** (2 papers: [Incorporating Diverse Perspectives in Cultural Alignment: Survey of Evaluation Benchmarks Through A Three-Dimensional Framework](https://aclanthology.org/2025.emnlp-main.862.pdf), [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf))
> The model's tendency to generate oversimplified and often inaccurate generalizations about groups of people, particularly based on demographic indicators like gender, ethnicity, or religion.

**Gender stereotypical bias** (1 paper: [Blind Men and the Elephant: Diverse Perspectives on Gender Stereotypes in Benchmark Datasets](https://aclanthology.org/2025.emnlp-main.1162.pdf))
> The tendency of a language model to associate certain characteristics, roles, or attributes with individuals based on their gender, reflecting and potentially amplifying societal stereotypes.

**Occupational gender bias** (1 paper: [Assumed Identities: Quantifying Gender Bias in Machine Translation of Gender-Ambiguous Occupational Terms](https://aclanthology.org/2025.emnlp-main.1640.pdf))
> A model's systematic predisposition to associate specific occupations with particular genders, revealed through aggregated patterns in translation when the source text is gender-ambiguous.

**Stereotypical association** (1 paper: [Assumed Identities: Quantifying Gender Bias in Machine Translation of Gender-Ambiguous Occupational Terms](https://aclanthology.org/2025.emnlp-main.1640.pdf))
> The tendency to link particular occupations with specific genders in ways that reflect social stereotypes rather than neutral interpretation.

**Stereotypical reasoning** (1 paper: [EuroGEST: Investigating gender stereotypes in multilingual language models](https://aclanthology.org/2025.emnlp-main.1632.pdf))
> The latent cognitive process by which a model preferentially selects responses that align with culturally ingrained stereotypes, particularly in gendered contexts.

**Gender bias** (1 paper: [We Politely Insist: Your LLM Must Learn the Persian Art of Taarof](https://aclanthology.org/2025.emnlp-main.94.pdf))
> The tendency of a model to produce responses influenced by stereotypical gender roles rather than culturally appropriate norms, even when gender is irrelevant to the expected behavior.

**Stereotypes** (1 paper: [GenderAlign: An Alignment Dataset for Mitigating Gender Bias in Large Language Models](https://aclanthology.org/2025.acl-long.553.pdf))
> The latent tendency to reproduce oversimplified and generalized beliefs about gender roles, characteristics, or abilities, such as assuming women are naturally suited for caregiving or men for leadership.

**Gender-occupation bias** (1 paper: [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf))
> A specific form of social bias where a model systematically associates certain occupations with particular genders, often reflecting societal stereotypes.

**Stereotypical bias** (1 paper: [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf))
> The model's tendency to generate or agree with over-generalized, disrespectful, or negative beliefs about particular demographic groups.

## Relationships

### Stereotyping →
- **StereoSet** (measurement instrument): *measured_by*, 3 papers
  > STEREOSET. STEREOSET measures stereotypical biases of models on gender, profession, race, and religion through 4, 229 context-sentence pairs. (Section 4.2)
  - [Reward Model Perspectives: Whose Opinions Do Reward Models Reward?](https://aclanthology.org/2025.emnlp-main.754.pdf)
  - [Blind Men and the Elephant: Diverse Perspectives on Gender Stereotypes in Benchmark Datasets](https://aclanthology.org/2025.emnlp-main.1162.pdf)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **CrowS-Pairs** (measurement instrument): *measured_by*, 3 papers
  > CrowS-Pairs (Nangia et al., 2020) assesses stereotypes associated with historically disadvantaged groups.
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
  - [Blind Men and the Elephant: Diverse Perspectives on Gender Stereotypes in Benchmark Datasets](https://aclanthology.org/2025.emnlp-main.1162.pdf)
  - [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
- **BBQ** (measurement instrument): *measured_by*, 1 paper
  > CrowS-Pairs (Nangia et al., 2020) and BBQ (Parrish et al., 2022) target nine categories of stereotypes, including gender, in paired sentences. (Section 2)
  - [GenderAlign: An Alignment Dataset for Mitigating Gender Bias in Large Language Models](https://aclanthology.org/2025.acl-long.553.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > Particularly, for the bias type of Stereotyping, we use GPT-4 to assess the stereotypical degree of LLM-generated outputs regarding any specific social group.
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **DecodingTrust** (measurement instrument): *measured_by*, 1 paper
  > To verify ALI-Agent’s effectiveness as a general evaluation framework, we conduct experiments on six datasets from three distinct aspects of human values: stereotypes (DecodingTrust [11], CrowS-Pairs [2])...
  - [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)

### → Stereotyping
- **Human preference alignment** (construct): *causes*, 1 paper
  > the effects on other trustworthiness aspects are negative: stereotypical bias increases by 150%... (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)

### Associated with
- **Fairness** (construct), 1 paper
  > We break down this concept [Fairness] into stereotype and bias & preference according to the types of discriminatory outputs [88, 132]. (Sec. 2.2.4)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Trustworthiness** (construct), 1 paper
  > this study investigates how models aligned with general-purpose preference data perform across five trustworthiness verticals: toxicity, stereotypical bias, machine ethics, truthfulness, and privacy.
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Social bias** (construct), 1 paper
  > Our categorization of social bias types in LLMs is structured around two distinct types of harms: Stereotyping and Toxicity.
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Machine translation** (behavioral indicator), 1 paper
  > Machine Translation systems have become indispensable tools for cross-linguistic communication, yet they frequently exhibit gender biases that reinforce societal stereotypes (Blodgett et al., 2020; Menis-Mastromichalakis et al., 2025). (Section 1)
  - [Assumed Identities: Quantifying Gender Bias in Machine Translation of Gender-Ambiguous Occupational Terms](https://aclanthology.org/2025.emnlp-main.1640.pdf)
- **Visual question answering** (behavioral indicator), 1 paper
  > Images, along with prompts, are presented to the VLAs in a visual question answering (VQA) format, and responses are analyzed to discern systematic distributional differences for females and males. (Section 1)
  - [Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf)
