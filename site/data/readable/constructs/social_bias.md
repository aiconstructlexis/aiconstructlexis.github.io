# Social bias
**Type:** Construct  
**Supporting papers:** 89  
**Also known as:** User name bias, Bias, Diversity bias, Omnivore bias, Demographic bias, Bias and discrimination detection, Societal bias  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats social bias as a model tendency for outputs to differ across social or demographic groups in prejudicial or stereotypical ways. Definitions repeatedly describe disparate treatment between groups, the reflection or amplification of societal stereotypes and prejudices, or different output when inputs reference different social attributes, and several definitions tie these patterns to biases in training data. Smaller lines of work narrow the construct to specific channels such as user name bias, demographic defaulting in annotation, LLM-judge responses to identity mentions, or omnivore bias, while some authors instead define bias as deviation from a desired distribution or as disparate performance across demographic subsets.

**Space of facets.** Where papers break the construct down, one split organizes social bias into two harm types, stereotyping and toxicity, and another paper lists axes such as race, age, socioeconomic status, disability, religion, physical appearance, gender, sexual orientation, and nationality. Papers also use neighboring labels, including societal bias, demographic bias, and simply bias, and some specialize it into narrower forms such as user name bias, diversity bias, and omnivore bias. By contrast, one paper treats social bias as one value issue alongside ethics and toxicity.

**Space of measurement.** Papers operationalize social bias through 10 linked measurement instruments and 4 linked behavioral indicators. The most common instruments are BBQ, CrowS-Pairs, BOLD, StereoSet, and BIG-bench, plus 5 other instruments: BBQ evaluates bias in multiple-choice question answering about protected classes, CrowS-Pairs uses stereotypical versus anti-stereotypical sentence pairs and checks whether the biased variant receives higher probability, BOLD uses open-ended generation prompts, StereoSet measures stereotypes across domains such as gender, profession, race, and religion, and BIG-bench tasks compare probabilities of stereotype-related tokens conditional on identity-related tokens. These operationalizations mostly track differential outputs or preferences across groups, which lines up with the dominant definitions, though some definitions are broader, covering desired-distribution deviations, response shifts from names or demographic cues, or subgroup performance gaps.

**Links.** Most reported links are related links rather than causal claims. Several papers state that fairness is related to social bias, often in discussions of mitigating bias or fairness concerns, and one paper states that social bias is related to toxicity and stereotyping as two harm types. Other work records related links from 3 other constructs and 3 other behavioral indicators to social bias, and one paper reports that preference prediction correlates with social bias through omnivore bias; no causal relationship is claimed.

## Sources

**User name bias** (1 paper: [First-Person Fairness in Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/92af0c8c2664429de2bb44c2692d84ae-Paper-Conference.pdf))
> Differences in chatbot responses that arise from the stored user's name and the demographic information associated with that name.

**Social bias** (5 papers: [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf), [Measuring Social Biases in Masked Language Models by Proxy of Prediction Quality](https://aclanthology.org/2025.acl-long.68.pdf), [Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf), [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.208.pdf), [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.305.pdf))
> Disparate treatments between social groups exhibited by model outputs, often stemming from stereotypes encoded in training data.

**Bias** (8 papers: [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf), [Continuously Updating Digital Twins using Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/amad25a/amad25a.pdf), [Arabic Dataset for LLM Safeguard Evaluation](https://aclanthology.org/2025.naacl-long.285.pdf), [CAVE: Controllable Authorship Verification Explanations](https://aclanthology.org/2025.naacl-long.451.pdf), [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf), [It Is Not Only the Negative that Deserves Attention! Understanding, Generation & Evaluation of (Positive) Moderation](https://aclanthology.org/2025.naacl-long.567.pdf), [Ethical Concern Identification in NLP: A Corpus of ACL Anthology Ethics Statements](https://aclanthology.org/2025.naacl-long.580.pdf), [MAPWise: Evaluating Vision-Language Models for Advanced Map Queries](https://aclanthology.org/2025.naacl-long.473.pdf))
> The tendency of a model to produce outputs that reflect or amplify problematic societal prejudices.

**Diversity bias** (1 paper: [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf))
> A tendency for an LLM judge to respond differently when demographic identity information is introduced into the content.

**Omnivore bias** (1 paper: [What can large language models do for sustainable food?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25a/thomas25a.pdf))
> A systematic tendency for the model to favor non-vegetarian options or model preferences for them more accurately than for vegetarian options.

**Societal bias** (2 papers: [CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases in LLMs](https://aclanthology.org/2025.emnlp-main.84.pdf), [Fine-Tuned LLMs are “Time Capsules” for Tracking Societal Bias Through Books](https://aclanthology.org/2025.naacl-long.118.pdf))
> The latent tendency of an LLM to express or amplify stereotypical, demeaning, or dehumanizing associations about social groups based on attributes such as race, gender, religion, or nationality, even when safety mechanisms are in place.

**Demographic bias** (4 papers: [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf), [Which Demographics do LLMs Default to During Annotation?](https://aclanthology.org/2025.acl-long.848.pdf), [Iterative Multilingual Spectral Attribute Erasure](https://aclanthology.org/2025.emnlp-main.1488.pdf), [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf))
> The latent tendency of a model to reflect societal or data-driven prejudices regarding demographic groups in its outputs.

**Bias and discrimination detection** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> Assessing a model's potential for unfair treatment related to subjective preferences, social stereotypes, race, gender, or religion in judicial decision-making.

## Relationships

### Social bias →
- **CrowS-Pairs** (measurement instrument): *measured_by*, 8 papers
  > Probability-based bias evaluations such as CrowS-Pairs [22] and tasks in the BIG-bench benchmarking suite [48] compare the probabilities of stereotype-related tokens conditional on the presence of identity-related tokens. (Section 2.2)
  - [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf)
  - [Towards Reward Fairness in RLHF: From a Resource Allocation Perspective](https://aclanthology.org/2025.acl-long.163.pdf)
  - [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.208.pdf)
  - [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models](https://aclanthology.org/2025.emnlp-main.774.pdf)
  - [Debiasing Multilingual LLMs in Cross-lingual Latent Space](https://aclanthology.org/2025.emnlp-main.1149.pdf)
  - [TFDP: Token-Efficient Disparity Audits for Autoregressive LLMs via Single-Token Masked Evaluation](https://aclanthology.org/2025.emnlp-main.1250.pdf)
- **BBQ** (measurement instrument): *measured_by*, 8 papers
  > we study the use of self-correction to alleviate societal biases in LLMs on the BBQ (Bias Benchmark for QA) benchmark [55], which evaluates societal biases against individuals belonging to protected classes across nine social dimensions.
  - [A Theoretical Understanding of Self-Correction through In-context Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/a399456a191ca36c7c78dff367887f0a-Paper-Conference.pdf)
  - [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](https://proceedings.neurips.cc/paper_files/paper/2024/file/f5198bc255e1d5f959edd6d1d1a86fab-Paper-Conference.pdf)
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
  - [Prompting Fairness: Integrating Causality to Debias Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f26a2d143a227376dff99a279f93f99-Paper-Conference.pdf)
  - [Instructing Large Language Models for Low-Resource Languages: A Systematic Study for Basque](https://aclanthology.org/2025.emnlp-main.1484.pdf)
  - [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.208.pdf)
  - [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models](https://aclanthology.org/2025.emnlp-main.774.pdf)
- **BOLD** (measurement instrument): *measured_by*, 3 papers
  > BOLD is an open-ended language generation dataset that provides English text generation prompts for bias benchmarking across five domains. (Section 3.2)
  - [Exploring the Impact of Personality Traits on LLM Bias and Toxicity](https://aclanthology.org/2025.emnlp-main.206.pdf)
  - [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models](https://aclanthology.org/2025.emnlp-main.774.pdf)
  - [Building Trust in Clinical LLMs: Bias Analysis and Dataset Transparency](https://aclanthology.org/2025.emnlp-main.1174.pdf)
- **StereoSet** (measurement instrument): *measured_by*, 2 papers
  > We evaluate the efficacy of our debiasing method on the social bias benchmark StereoSet (Nadeem et al., 2021).
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
  - [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.208.pdf)
- **WinoBias** (measurement instrument): *measured_by*, 1 paper
  > ...and evaluated on out-of-distribution bias benchmarks such as WinoBias (Zhao et al., 2018) and Winogender (Rudinger et al., 2018) to test generalization (Section 1).
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
- **BIG-bench** (measurement instrument): *measured_by*, 1 paper
  > Probability-based bias evaluations such as CrowS-Pairs [22] and tasks in the BIG-bench benchmarking suite [48] compare the probabilities of stereotype-related tokens conditional on the presence of identity-related tokens. (Section 2.2)
  - [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GlobalOpinionQA** (measurement instrument): *measured_by*, 1 paper
  > GlobalOpinionQA (Durmus et al., 2024) uses multiple-choice questions to assess the opinions stated by a model relative to aggregated population opinions from different countries. The goal is to identify model bias in representing diverse viewpoints. (Section 3)
  - [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf)
- **Winogender** (measurement instrument): *measured_by*, 1 paper
  > ...and evaluated on out-of-distribution bias benchmarks such as WinoBias (Zhao et al., 2018) and Winogender (Rudinger et al., 2018) to test generalization (Section 1).
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
- **CoBia** (measurement instrument): *measured_by*, 1 paper
  > This lightweight adversarial attack, which we call Co-Bia (Constructed Bias), uses only a single query to expose hidden societal biases in LLMs that could emerge during a conversation. (Section 1)
  - [CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases in LLMs](https://aclanthology.org/2025.emnlp-main.84.pdf)
- **HESEIA** (measurement instrument): *measured_by*, 1 paper
  > We introduce HESEIA, the first dataset for evaluating biases in LLMs organized per school area, including intersectional demographics.
  - [HESEIA: A community-based dataset for evaluating social biases in large language models, co-designed in real school settings in Latin America](https://aclanthology.org/2025.emnlp-main.1275.pdf)

### → Social bias
- **Preference prediction** (behavioral indicator): *correlates*, 1 paper
  > Within the vegetarian vs. non-vegetarian meal comparisons, accuracy is lower when vegetarian options are rated higher, reflecting LLMs’ omnivore bias, as LLMs more frequently prefer non-vegetarian options compared to ground truth human preferences.
  - [What can large language models do for sustainable food?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25a/thomas25a.pdf)

### Associated with
- **Fairness** (construct), 6 papers
  > To mitigate societal biases implicitly encoded in recent successful pretrained language models, a diverse array of approaches have been proposed to encourage model fairness... (Abstract)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
  - [Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf)
  - [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf)
  - [Position: AI’s growing due process problem](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25b/rane25b.pdf)
  - [Iterative Multilingual Spectral Attribute Erasure](https://aclanthology.org/2025.emnlp-main.1488.pdf)
  - [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models](https://aclanthology.org/2025.emnlp-main.774.pdf)
- **Toxicity** (construct), 1 paper
  > Our categorization of social bias types in LLMs is structured around two distinct types of harms: Stereotyping and Toxicity.
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Recommendation** (behavioral indicator), 1 paper
  > Clearly, this has important implications for fairness, bias, and whether recommender systems work for everyone. (Section 4).
  - [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf)
- **Stereotyping** (construct), 1 paper
  > Our categorization of social bias types in LLMs is structured around two distinct types of harms: Stereotyping and Toxicity.
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Opinion summarization** (behavioral indicator), 1 paper
  > The use of AI language systems with inherent biases could shape the way audiences interpret and process information, especially in tasks such as opinion summarisation where biased outputs could significantly influence public opinion. (Section 1)
  - [Less Is More? Examining Fairness in Pruned Large Language Models for Summarising Opinions](https://aclanthology.org/2025.emnlp-main.909.pdf)
- **Factual grounding** (construct), 1 paper
  > Depending on application, we frame bias relative to a desired distribution—equal (for social equity) or real-world (for factual grounding) (Section 6).
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
- **Harmful content generation** (behavioral indicator), 1 paper
  > social attributes such as perceived race, gender, and physical characteristics depicted in images can significantly influence the generation of toxic content (Abstract).
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.305.pdf)
- **Emotion understanding** (construct), 1 paper
  > an analysis of the models’ emotional understanding ability, using EQ-Bench-based metrics, revealed that... (2) performance disparities were confirmed across race, gender, and age group. (Abstract)
  - [Does the Emotional Understanding of LVLMs Vary Under High-Stress Environments and Across Different Demographic Attributes?](https://aclanthology.org/2025.acl-long.1130.pdf)
- **Cultural alignment** (construct), 1 paper
  > AlKhamissi et al. (2024) demonstrate how cultural misalignment can increase bias. (Section 4.2)
  - [Position: LLMs Can be Good Tutors in English Education](https://aclanthology.org/2025.emnlp-main.885.pdf)
