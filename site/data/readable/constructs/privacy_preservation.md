# Privacy preservation
**Type:** Construct  
**Supporting papers:** 70  
**Also known as:** Privacy, Secrecy maintenance, Information leakage, Prompt leakage vulnerability, Privacy leakage, Data leakage risk, Privacy risk, Data leakage vulnerability, Information leakage risk, Knowledge file leakage, Privacy protection, Privacy vulnerability  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage centers on limiting disclosure of sensitive information: most papers describe privacy preservation as keeping outputs, prompts, or training procedures from revealing personal data, private exemplars, or individual training points, often with differential privacy guarantees. A smaller but recurring line of work frames the same space negatively, using labels such as privacy leakage, privacy vulnerability, data leakage risk, or prompt leakage vulnerability for susceptibility to disclosure, membership inference, datastore extraction, or system-prompt revelation. Definitions differ mainly on locus and protected object, with some focusing on output behavior during inference, others on training, pruning, or federated processes that avoid sharing client data, and one paper recasting it as secrecy maintenance in social interaction. Some benchmark-style definitions also shift the reference standard from leakage itself to awareness or prompt design, describing privacy as recognizing unauthorized requests, refusing suspicious questions, or writing prompts free of sensitive personal information.

**Space of facets.** When papers divide the construct, the clearest split is between privacy awareness and privacy leakage, with one benchmark stating that it evaluates privacy in terms of awareness and leakage. Other papers organize it by stage, training versus inference, or by leakage channel: one study examines data privacy during both training and inference, and another identifies five knowledge-file leakage vectors, metadata, initialization, retrieval, sandboxed execution, and prompts. Across papers, overlapping labels, privacy, privacy preservation, privacy protection, privacy risk, information leakage, and prompt or knowledge-file leakage, are used for closely related phenomena.

**Space of measurement.** Operationally, papers link privacy preservation to three measurement instruments and three behavioral indicators. The most frequently linked instrument is membership inference attack, used as a test of whether a specific datapoint was used to train the model; the others are human evaluation of whether summaries remain private, and dataset-based evaluation on MIMIC-III for privacy protection under a private-entity setting. The linked behavioral indicators are de-identification, pre-training data detection, and privacy leakage, so the construct is commonly made concrete through training-data detection, privacy-leakage evaluation, and tests of whether identifying information can still be inferred; these operationalizations align most clearly with definitions centered on leakage and disclosure, while the social-interaction and prompt-design framings are represented less directly.

**Links.** Papers connect privacy preservation to seven constructs. Several papers relate it to trustworthiness, and one line of work records a causal relationship from in-context learning to privacy preservation, with in-context learning on private datasets described as posing privacy risks, while another paper treats that pair as related. Other links are more mixed: one paper claims causal relationships from privacy preservation to personalization and to generalization, with stringent privacy measures said to hinder both, another treats privacy and personalization as related, and one paper claims a causal relationship from memorization to privacy preservation; additional papers relate privacy preservation to utility trade-offs and other privacy-oriented notions.

## Sources

**Privacy** (7 papers: [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf), [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf), [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf), [Ethical Concern Identification in NLP: A Corpus of ACL Anthology Ethics Statements](https://aclanthology.org/2025.naacl-long.580.pdf), [What Makes a Good Natural Language Prompt?](https://aclanthology.org/2025.acl-long.292.pdf), [Scaling Laws for Differentially Private Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mckenna25a/mckenna25a.pdf), [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf))
> The degree to which a model's outputs do not reveal sensitive information from its input exemplars, formalized through differential privacy guarantees.

**Secrecy maintenance** (1 paper: [SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3075b88e583a0e98d8b24338a613060-Paper-Conference.pdf))
> The ability to protect private information or intentions from being revealed during social interaction, especially when disclosure would reduce strategic advantage.

**Privacy preservation** (9 papers: [EmojiPrompt: Generative Prompt Obfuscation for Privacy-Preserving Communication with Cloud-based LLMs](https://aclanthology.org/2025.naacl-long.614.pdf), [PAPILLON: Privacy Preservation from Internet-based and Local Language Model Ensembles](https://aclanthology.org/2025.naacl-long.173.pdf), [FedSpaLLM: Federated Pruning of Large Language Models](https://aclanthology.org/2025.naacl-long.424.pdf), [Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e9034dd5420660d86c8c360c35a895e-Paper-Conference.pdf), [DP-OPT: Make Large Language Model Your Privacy-Preserving Prompt Engineer](https://proceedings.iclr.cc/paper_files/paper/2024/file/fffe5a7804c40465ef2432386850c2c7-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf), [Privately Aligning Language Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/477b39bfb9db99f60914dbfed5f23eb2-Paper-Conference.pdf), [IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d3a9e085540c65dd3e5731361f9320e-Paper-Conference.pdf), [Synthetic Text Generation for Training Large Language Models via Gradient Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nguyen25c/nguyen25c.pdf))
> The ability of a system to fulfill user requests without revealing personally identifiable information to untrusted components, such as remote API-based models.

**Information leakage** (1 paper: [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf))
> The unintended access or reuse of task-specific information (e.g., training data, task identifiers) from previously learned tasks during continual learning, posing privacy risks and enabling unfair performance advantages.

**Prompt leakage vulnerability** (1 paper: [“I've Decided to Leak”: Probing Internals Behind Prompt Leakage Intents](https://aclanthology.org/2025.emnlp-main.1082.pdf))
> The susceptibility of a large language model to being manipulated by adversarial queries into revealing its confidential system prompt.

**Privacy leakage** (4 papers: [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf), [Textual Unlearning Gives a False Sense of Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25d/du25d.pdf), [Interpretation Meets Safety: A Survey on Interpretation Methods and Tools for Improving LLM Safety](https://aclanthology.org/2025.emnlp-main.1091.pdf), [Exploiting the Shadows: Unveiling Privacy Leaks through Lower-Ranked Tokens in Large Language Models](https://aclanthology.org/2025.acl-long.410.pdf))
> The tendency to reveal personal or sensitive information when prompted directly or indirectly.

**Privacy vulnerability** (2 papers: [DocMIA: Document-Level Membership Inference Attacks against DocVQA Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/231a8daf4f64935d0c7c6586f290b24f-Paper-Conference.pdf), [Beyond Text: Unveiling Privacy Vulnerabilities in Multi-modal Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1259.pdf))
> The susceptibility of a model to attacks that can reveal sensitive information about its training data.

**Data leakage risk** (1 paper: [Uncovering Latent Memories in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/442443dbe8c4c7e1df7eda140921de36-Paper-Conference.pdf))
> The tendency for a model to reveal sensitive or proprietary training information in its outputs, creating privacy and misuse concerns.

**Privacy risk** (1 paper: [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf))
> The potential for a model to reveal sensitive information about its training data, which can be assessed through training data detection.

**Data leakage vulnerability** (1 paper: [Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf))
> The tendency of a RAG system to expose private datastore content through model outputs.

**Information leakage risk** (1 paper: [Mimicking the Familiar: Dynamic Command Generation for Information Theft Attacks in LLM Tool-Learning System](https://aclanthology.org/2025.acl-long.672.pdf))
> The latent potential for a tool-learning system to unintentionally disclose sensitive user or tool information to unauthorized parties as a result of its design and behavior.

**Knowledge file leakage** (1 paper: [When GPT Spills the Tea: Comprehensive Assessment of Knowledge File Leakage in GPTs](https://aclanthology.org/2025.acl-long.936.pdf))
> The latent propensity of an LLM agent to expose protected knowledge file data—such as titles, content, or original files—through various system vectors, even without direct adversarial prompting.

**Privacy protection** (1 paper: [GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models](https://aclanthology.org/2025.acl-long.255.pdf))
> The degree to which the compressed emulator prevents leakage of sensitive information from either the model or data owner, ensuring that the fine-tuned emulator cannot be used to reconstruct the original model or compromise data confidentiality.

## Relationships

### Privacy preservation →
- **Membership inference attack** (measurement instrument): *measured_by*, 3 papers
  > These fully trained prompts, if not properly protected with privacy mechanism, are vulnerable to MIA which aims to infer if an image sample was used for training or not (Section 3.3).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
  - [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf)
- **Personalization** (construct): *causes*, 2 papers
  > stringent privacy measures, such as differential privacy, can hinder both personalization and generalization (Abstract).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
  - [Personalized Generation In Large Model Era: A Survey](https://aclanthology.org/2025.acl-long.1201.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > stringent privacy measures, such as differential privacy, can hinder both personalization and generalization (Abstract).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **MIMIC-III** (measurement instrument): *measured_by*, 1 paper
  > Table 3: Privacy protection performance under the private entity known setting on the MIMIC-III dataset.
  - [Controlled Generation for Private Synthetic Text](https://aclanthology.org/2025.emnlp-main.1663.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > We further evaluate the LMs capability in generating private summaries by conducting a human evaluation. (Section 4.5)
  - [How Private are Language Models in Abstractive Summarization?](https://aclanthology.org/2025.emnlp-main.1531.pdf)

### → Privacy preservation
- **In-context learning** (construct): *causes*, 2 papers
  > We study the problem of in-context learning (ICL) with large language models (LLMs) on private datasets. This scenario poses privacy risks, as LLMs may leak or regurgitate the private examples demonstrated in the prompt. (Section 1)
  - [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **Memorization** (construct): *causes*, 1 paper
  > This repeated exposure enhances the likelihood of the model memorizing specific details, thereby increasing the potential for data leakage during privacy attacks. (Section 1)
  - [DocMIA: Document-Level Membership Inference Attacks against DocVQA Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/231a8daf4f64935d0c7c6586f290b24f-Paper-Conference.pdf)

### Associated with
- **Trustworthiness** (construct), 2 papers
  > We assess the trustworthiness of Med-LVLMs across five dimensions, including trustfulness, fairness, safety, privacy, and robustness. (Abstract)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Privacy awareness** (construct), 1 paper
  > From the perspectives of consciousness and behaviors [132], we evaluate privacy in terms of awareness and leakage. (Sec. 2.2.5)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Privacy leakage** (behavioral indicator), 1 paper
  > "we evaluate privacy in terms of awareness and leakage"
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Pre-training data detection** (behavioral indicator), 1 paper
  > Training data detection (TDD) is commonly employed to assess privacy risks in machine learning models (Murakonda & Shokri, 2020).
  - [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf)
- **Utility preservation** (construct), 1 paper
  > For DP-based solutions, although they yield better efficiency but faces the trade-off between privacy and utility. (Section 2)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **De-identification** (behavioral indicator), 1 paper
  > “the goal of any text anonymization method is to remove all information that could lead to the inference of a set of pre-specified author attributes while maintaining the utility of the original text.”
  - [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf)
