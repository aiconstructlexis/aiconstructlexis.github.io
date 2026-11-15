# Fairness
**Type:** Construct  
**Supporting papers:** 65  
**Also known as:** Algorithmic fairness, Biasness, Equitability, Normative correctness  

## State of the Field

**Space of definitions.** Across the literature, fairness is most commonly described as avoiding biased, stereotypical, or prejudicial outputs and treating social or demographic groups equitably. Several definitions make this more specific as prediction behavior that is independent of sensitive attributes, or as equitable error rates across groups; one paper quantifies it as the share of cases where a model shows no gender preference, saying fair models should prefer neither the masculine nor the feminine version. Smaller lines of work frame fairness as parity between model performance and users' needs across cultures, as adherence to an idealized fairness standard such as gender parity in translation, or as a moral dimension involving justice, reciprocity, and equitable treatment.

**Space of facets.** When papers subdivide fairness, the clearest splits are counterfactual fairness versus performance disparity, and stereotype versus bias and preference. Some authors use nearby labels for overlapping ideas, including equitability for cross-cultural parity, biasness for the presence or absence of unfair prejudice in task-oriented dialogue, and normative correctness for fairness judged against idealized gender parity. Fairness is also treated as one dimension of broader trustworthiness, and one debiasing study measures a tradeoff between fairness and language modeling ability.

**Space of measurement.** Operationally, papers link fairness to 6 measurement instruments and 4 behavioral indicators. The most frequently linked instruments are StereoSet, A-OKVQA, Dictator Game, FINTRUST, and PLLuM-Align, plus 1 other instrument; these operationalize fairness through stereotype benchmarks, questions asked in African-American English, an economic game for fairness in decision-making, a finance trustworthiness benchmark, and human 5-point Likert ratings of response fairness. Most operationalizations align with the prevailing bias-avoidance framing, though some narrow fairness to no gender preference in paired completions, equality differences of false positive and false negative rates, the frequency of gendered terms in generated text, or idealized gender parity in translation.

**Links.** In relationship claims, fairness is most commonly related to social bias: papers describe mitigating societal bias, reducing reliance on demographic patterns, or addressing bias amplification and harm as fairness work. Smaller numbers of papers also relate it to generalization and trustworthiness, along with other related constructs and behaviors. Separately, one paper claims a causal relationship from neural collapse to fairness, and another claims a causal relationship from refusal to fairness; no papers report correlational links.

## Sources

**Fairness** (12 papers: [Are Models Biased on Text without Gender-related Language?](https://proceedings.iclr.cc/paper_files/paper/2024/file/37771cc0be272368102a37f202bb88d8-Paper-Conference.pdf), [Debiasing Attention Mechanism in Transformer without Demographics](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f5337a39b1f6d670aad9d32debc0e5d-Paper-Conference.pdf), [Test-Time Training on Nearest Neighbors for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f02f1185b97518ab5bd7ebde466992d3-Paper-Conference.pdf), [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf), [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf), [FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf), [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf), [Examining and Adapting Time for Multilingual Classification via Mixture of Temporal Experts](https://aclanthology.org/2025.naacl-long.313.pdf), [DeCAP: Context-Adaptive Prompt Generation for Debiasing Zero-shot Question Answering in Large Language Models](https://aclanthology.org/2025.naacl-long.624.pdf), [Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts](https://aclanthology.org/2025.acl-long.185.pdf), [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf), [F²Bench: An Open-ended Fairness Evaluation Benchmark for LLMs with Factuality Considerations](https://aclanthology.org/2025.emnlp-main.105.pdf))
> The degree to which a model avoids producing biased or stereotypical outputs across different social groups, representing an ideal state of equitable treatment.

**Algorithmic fairness** (1 paper: [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf))
> The extent to which a model's outputs are free from systematic prejudice, particularly in sensitive applications like comparing candidates.

**Equitability** (1 paper: [Reading between the Lines: Can LLMs Identify Cross-Cultural Communication Gaps?](https://aclanthology.org/2025.naacl-long.409.pdf))
> The model's capability to maintain parity between its performance and a user's needs across different cultural backgrounds.

**Biasness** (1 paper: [AutoEval-ToD: Automated Evaluation of Task-oriented Dialog Systems](https://aclanthology.org/2025.naacl-long.508.pdf))
> The presence or absence of unfair or prejudiced content in a ToD system's responses, particularly with respect to sensitive attributes.

**Normative correctness** (1 paper: [Assumed Identities: Quantifying Gender Bias in Machine Translation of Gender-Ambiguous Occupational Terms](https://aclanthology.org/2025.emnlp-main.1640.pdf))
> The extent to which a model adheres to an idealized standard of gender fairness, such as equal representation of masculine and feminine forms in translations.

## Relationships

### Fairness →
- **StereoSet** (measurement instrument): *measured_by*, 2 papers
  > As measured by prior metrics from StereoSet, our model achieves a higher degree of fairness while maintaining language modeling ability with low cost12.
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)
- **Dictator Game** (measurement instrument): *measured_by*, 1 paper
  > The Dictator Game is a simple economic experiment where one player (“Dictator“) is given a sum of money to share with another player, with no negotiation or input from the recipient. It examines altruism and fairness in decision-making. (Section 5.1)
  - [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf)
- **A-OKVQA** (measurement instrument): *measured_by*, 1 paper
  > In VHELM, this is assessed by asking questions drawn from A-OKVQA [34] and VQAv2 [12] in African-American English (AAE)... (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 1 paper
  > In VHELM, this is assessed by asking questions drawn from A-OKVQA [34] and VQAv2 [12] in African-American English (AAE)... (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **FINTRUST** (measurement instrument): *measured_by*, 1 paper
  > we curate 15, 680 instances to evaluate LLM trustworthiness in the financial domain. We ... incorporate seven core dimensions: Truthfulness, Safety, Fairness, Robustness, Privacy, Transparency, and Knowledge Discovery. (Section 2)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **PLLuM-Align** (measurement instrument): *measured_by*, 1 paper
  > For scalar multi-attribute rating, annotators evaluated each response on a 5-point Likert scale across seven criteria: i) truthfulness, (ii) linguistic correctness, (iii) safety, (iv) fairness, (v) conciseness, (vi) coherence & reasoning, as well as vii) helpfulness & instruction-following.
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)

### → Fairness
- **Neural collapse** (construct): *causes*, 1 paper
  > This observation further inspires us to explicitly enforce neural collapse to promote fairness in pretrained language models. (Section 1)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **Refusal** (behavioral indicator): *causes*, 1 paper
  > Refusal effectively avoids generating controversial or biased output, ensuring fairness and safety. (Section 3.1)
  - [Position: Political Neutrality in AI Is Impossible — But Here Is How to Approximate It](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fisher25a/fisher25a.pdf)

### Associated with
- **Social bias** (construct), 6 papers
  > To mitigate societal biases implicitly encoded in recent successful pretrained language models, a diverse array of approaches have been proposed to encourage model fairness... (Abstract)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
  - [Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf)
  - [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf)
  - [Position: AI’s growing due process problem](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25b/rane25b.pdf)
  - [Iterative Multilingual Spectral Attribute Erasure](https://aclanthology.org/2025.emnlp-main.1488.pdf)
  - [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models](https://aclanthology.org/2025.emnlp-main.774.pdf)
- **Stereotyping** (construct), 1 paper
  > We break down this concept [Fairness] into stereotype and bias & preference according to the types of discriminatory outputs [88, 132]. (Sec. 2.2.4)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Trustworthiness** (construct), 1 paper
  > We assess the trustworthiness of Med-LVLMs across five dimensions, including trustfulness, fairness, safety, privacy, and robustness. (Abstract)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generalization** (construct), 1 paper
  > This lack of proper evaluation can then materialize in persistent issues of deployed systems related to generalization, e.g., hallucination [30], out-of-distribution generalization [39], fairness [6], and generalization to the long-tail [23, 24]. (Section 1).
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Recommendation** (behavioral indicator), 1 paper
  > Clearly, this has important implications for fairness, bias, and whether recommender systems work for everyone. (Section 4).
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Opinion summarization** (behavioral indicator), 1 paper
  > Our exclusive focus on fairness is not arbitrary, but fundamentally critical in the context of opinion summarisation. (Limitations)
  - [Less Is More? Examining Fairness in Pruned Large Language Models for Summarising Opinions](https://aclanthology.org/2025.emnlp-main.909.pdf)
- **Stereotype recognition** (behavioral indicator), 1 paper
  > To evaluate the alignment of fairness, we perform stereotype recognition task (Sun et al., 2024) (Section 4.1).
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)
