# Gender bias
**Type:** Construct  
**Supporting papers:** 24  
**Also known as:** Bias against marginalized genders  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage treats gender bias as a latent or systematic tendency in a model's outputs, representations, or reasoning that disadvantages, misrepresents, or unfairly associates people on the basis of gender. Most definitions emphasize stereotyped or spurious associations, such as linking gender-neutral expressions, occupations, or roles to a specific gender, or depicting men with more agentic language than women. Smaller strands narrow the construct to harmful content against marginalized genders, especially within the LGBTQ+ community, or to gendered stereotypes in clinical reasoning independent of clinical relevance. One study also frames it as persisting even in non-stereotypical settings, reporting fair behavior in only 9%-41% of stereotype-free sentences.

**Space of facets.** Papers do not use a single subtype scheme, but they recurrently break the construct into specific manifestations: gender-occupation associations, agency versus communal language, skewed role and attribute representations, biased clinical reasoning, and harms toward marginalized genders. The broad label 'gender bias' often serves as the umbrella term, while 'bias against marginalized genders' is presented as one form within it. The main axis of variation is whether the construct is treated broadly as unfair gendered assumptions in generated content, or more narrowly as a property of outputs, embeddings, or reasoning in a particular domain.

**Space of measurement.** Papers link gender bias to 4 measurement instruments and 1 behavioral indicator. Measurement is centered on benchmark-style datasets and tests: WinoBias is the most frequently linked instrument and is described as probing gender bias through pronoun resolution and occupation associations in coreference settings, followed by BOLD, StereoSet, and Winogender as datasets or tests for analyzing or evaluating gender bias in LLMs. The lone linked behavioral indicator is coreference resolution. These operationalizations line up most directly with definitions centered on stereotyped gender associations, while broader definitions about marginalized genders, clinical reasoning, or representation shifts across roles and attributes are not paired with additional named instruments.

**Links.** Beyond measurement, one paper reports that coreference resolution is related to gender bias, stating that gender biases in neural models can be made visible in coreference resolution. No papers claim a causal or correlational link involving gender bias.

## Sources

**Gender bias** (3 papers: [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf), [Fine-Tuned LLMs are “Time Capsules” for Tracking Societal Bias Through Books](https://aclanthology.org/2025.naacl-long.118.pdf), [How Can We Diagnose and Treat Bias in Large Language Models for Clinical Decision-Making?](https://aclanthology.org/2025.naacl-long.114.pdf))
> A specific form of bias where a model's outputs systematically disadvantage or misrepresent individuals based on their gender.

**Bias against marginalized genders** (1 paper: [GenderAlign: An Alignment Dataset for Mitigating Gender Bias in Large Language Models](https://aclanthology.org/2025.acl-long.553.pdf))
> The latent tendency to generate content that perpetuates disparities or harms against non-dominant gender identities, particularly within the LGBTQ+ community, such as denying their legitimacy or associating them with deviance.

## Relationships

### Gender bias →
- **WinoBias** (measurement instrument): *measured_by*, 6 papers
  > To answer the first question, we check the LLaMA performance on popular tests for gender bias: WinoBias (Zhao et al., 2018) and StereoSet (Nadeem et al., 2021). (Section 1)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
  - [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf)
  - [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf)
  - [Prompting Fairness: Integrating Causality to Debias Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f26a2d143a227376dff99a279f93f99-Paper-Conference.pdf)
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **StereoSet** (measurement instrument): *measured_by*, 1 paper
  > To answer the first question, we check the LLaMA performance on popular tests for gender bias: WinoBias (Zhao et al., 2018) and StereoSet (Nadeem et al., 2021). (Section 1)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **BOLD** (measurement instrument): *measured_by*, 1 paper
  > Additionally, we further conducted an experiment where we use the BOLD dataset to analyze LM gender bias, results are shown in appendix Table 13. (Section 4.4)
  - [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf)
- **Winogender** (measurement instrument): *measured_by*, 1 paper
  > We also conduct experiments on BBQ (Parrish et al., 2022) and WinoGender (Zhao et al., 2018), two widely used datasets for evaluating gender bias in LLMs. (Section 1)
  - [GenderAlign: An Alignment Dataset for Mitigating Gender Bias in Large Language Models](https://aclanthology.org/2025.acl-long.553.pdf)

### Associated with
- **Coreference resolution** (behavioral indicator), 1 paper
  > As noted by Davis and van Schijndel (2020), gender biases in neural models can be made visible in coreference resolution. (Section 4)
  - [Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs](https://aclanthology.org/2025.emnlp-main.1527.pdf)
