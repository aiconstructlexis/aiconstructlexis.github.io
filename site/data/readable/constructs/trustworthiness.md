# Trustworthiness
**Type:** Construct  
**Supporting papers:** 70  
**Also known as:** Trustfulness, Clinical trustworthiness, Clinical reliability  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats trustworthiness as a broad property of models or their outputs being reliable, dependable, and often safe or accurate enough for people to rely on them, especially in real-world or high-stakes settings. Many definitions place it in outputs, for example reliable, safe, and accurate responses or dependable uncertainty expression, while others frame it as a property of the model itself, such as reliable and consistent understanding and generation evidenced by self-consistency. A smaller line of work states it more explicitly in user terms, as end-user or domain-expert confidence in the system, and a few papers introduce narrower domain variants such as clinical trustworthiness or clinical reliability.

**Space of facets.** Systematizations vary. Some papers divide trustworthiness into robustness and truthfulness, while others treat it as a broader umbrella spanning several reliability and social-risk dimensions. Nearby labels such as trustfulness and clinical trustworthiness appear as narrower variants, and some authors fold transparency into the same broader construct rather than treating it as separate.

**Space of measurement.** Operationalizations span 6 linked measurement instruments and 3 linked behavioral indicators. Common instruments include ASQA, DecodingTrust, FINTRUST, and Human evaluation, while other linked datasets are also used through TRUST-SCORE; DecodingTrust and FINTRUST are presented as comprehensive benchmark or framework-style evaluations, and one paper adds user studies to assess trustworthiness improvements. On the behavioral side, Hallucination is a recurring indicator, so papers often operationalize trustworthiness through benchmark scores and failure-mode evaluation, which matches the recurring emphasis on reliability and dependable outputs.

**Links.** Several papers claim a causal relationship from Hallucination to Trustworthiness, typically in language that hallucinations undermine trustworthy use. Another recurring causal claim runs from Interpretability and explainability to Trustworthiness, and a smaller line makes the same kind of claim from Confidence estimation. Beyond these, papers relate trustworthiness to 20 constructs overall, including Alignment, and one paper says human preference alignment does not automatically guarantee trustworthiness.

## Sources

**Trustworthiness** (14 papers: [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf), [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf), [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf), [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf), [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf), [How to Enable Effective Cooperation Between Humans and NLP Models: A Survey of Principles, Formalizations, and Beyond](https://aclanthology.org/2025.acl-long.22.pdf), [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf), [SafetyQuizzer: Timely and Dynamic Evaluation on the Safety of LLMs](https://aclanthology.org/2025.naacl-long.85.pdf), [CAVE: Controllable Authorship Verification Explanations](https://aclanthology.org/2025.naacl-long.451.pdf), [MICE for CATs: Model-Internal Confidence Estimation for Calibrating Agents with Tools](https://aclanthology.org/2025.naacl-long.615.pdf), [SCIURus: Shared Circuits for Interpretable Uncertainty Representations in Language Models](https://aclanthology.org/2025.naacl-long.618.pdf), [The Impact of Inference Acceleration on Bias of LLMs](https://aclanthology.org/2025.naacl-long.91.pdf), [How to Make LLMs Forget: On Reversing In-Context Knowledge Edits](https://aclanthology.org/2025.naacl-long.630.pdf), [Evaluating Evidence Attribution in Generated Fact Checking Explanations](https://aclanthology.org/2025.naacl-long.282.pdf))
> The quality of a model being reliable and consistent in its understanding and generation, as evidenced by properties like self-consistency.

**Trustfulness** (1 paper: [Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf))
> The reliability and credibility of the model's output results, often compromised by the generation of false or unsupported content.

**Clinical trustworthiness** (1 paper: [From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations](https://aclanthology.org/2025.emnlp-main.548.pdf))
> The degree to which model outputs are reliable and safe for clinical use, especially when intermediate reasoning errors could lead to misjudgments.

**Clinical reliability** (1 paper: [ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment](https://aclanthology.org/2025.emnlp-main.598.pdf))
> The extent to which a generated medical report is trustworthy and valid for use in real-world clinical decision-making.

## Relationships

### Trustworthiness →
- **DecodingTrust** (measurement instrument): *measured_by*, 1 paper
  > DecodingTrust (Wang et al. [2023]) was among the first to aim for a comprehensive assessment of trustworthiness in GPT models from several perspectives. (Section 2.1)
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > Besides the metrics mentioned above, we provide user studies in Appendix H to provide additional insights into the model’s trustworthiness improvements. (Section 4.1.2)
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **ASQA** (measurement instrument): *measured_by*, 1 paper
  > Table 2: LLaMA family evaluated on the ASQA, QAMPARI, and ELI5 datasets. ... TRUST := TRUST-SCORE (Table 2)
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **QAMPARI** (measurement instrument): *measured_by*, 1 paper
  > Table 2: LLaMA family evaluated on the ASQA, QAMPARI, and ELI5 datasets. ... TRUST := TRUST-SCORE (Table 2)
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **ELI5** (measurement instrument): *measured_by*, 1 paper
  > Table 2: LLaMA family evaluated on the ASQA, QAMPARI, and ELI5 datasets. ... TRUST := TRUST-SCORE (Table 2)
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **FINTRUST** (measurement instrument): *measured_by*, 1 paper
  > This paper introduces FINTRUST, a comprehensive benchmark specifically designed for evaluating the trustworthiness of LLMs in finance applications. (Abstract)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf)

### → Trustworthiness
- **Hallucination** (behavioral indicator): *causes*, 6 papers
  > hallucinations — non-factual or non-sensical information generated by the model — have become challenging barriers to trustworthy and reliable artificial intelligence
  - [Stealth edits to large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c8168a8eca2eb23f6b1f5019371043e-Paper-Conference.pdf)
  - [Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf)
  - [WikiContradict: A Benchmark for Evaluating LLMs on Real-World Knowledge Conflicts from Wikipedia](https://proceedings.neurips.cc/paper_files/paper/2024/file/c63819755591ea972f8570beffca6b1b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Selective Generation for Controllable Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a6815122f533193a022cbc41786c1cc-Paper-Conference.pdf)
  - [Where Confabulation Lives: Latent Feature Discovery in LLMs](https://aclanthology.org/2025.emnlp-main.1515.pdf)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
- **Interpretability and explainability** (construct): *causes*, 5 papers
  > one aspect that hinders their deployment is the lack of human-comprehensible understanding of their internal computations. This directly calls into question their reliability and trustworthiness (Introduction).
  - [A Concept-Based Explainability Framework for Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f4fba41b554f9aaa013c4062a1c40518-Paper-Conference.pdf)
  - [Decision Information Meets Large Language Models: The Future of Explainable Operations Research](https://proceedings.iclr.cc/paper_files/paper/2025/file/a48e5877c7bf86a513950ab23b360498-Paper-Conference.pdf)
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
  - [BIRD: A Trustworthy Bayesian Inference Framework for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/19452e14fe6e0a8ac00410f1eebcbded-Paper-Conference.pdf)
  - [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf)
- **Confidence estimation** (behavioral indicator): *causes*, 2 papers
  > In this work, we introduce model-internal confidence estimators (MICE), which improve the trustworthiness and safety of language models as tool-calling agents. (Section 8)
  - [MICE for CATs: Model-Internal Confidence Estimation for Calibrating Agents with Tools](https://aclanthology.org/2025.naacl-long.615.pdf)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Attribution ability** (construct): *causes*, 1 paper
  > Improving the ability of LLMs to both generate relevant summaries and provide accurate attributions has the potential to help improve their usefulness, transparency, and trustworthiness. (Section 2.1)
  - [Unstructured Evidence Attribution for Long Context Query Focused Summarization](https://aclanthology.org/2025.emnlp-main.95.pdf)
- **Honesty** (construct): *causes*, 1 paper
  > honesty—defined as consistently delivering accurate information and refraining from deceiving users—plays a crucial role in ensuring the trustworthy deployment of LLMs in real-world applications. (Section 1)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Semantic uncertainty** (construct): *causes*, 1 paper
  > "uncertainty can be used to improve the trustworthiness of LLMs"
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > our framework leverages the reasoning capabilities of LLMs, enhancing the trustworthiness of clinical predictions. (Abstract)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Multimodal alignment** (construct): *causes*, 1 paper
  > This misalignment undermines trustworthiness, posing challenges for reliable applications of these models in high-stakes medical scenarios (Section 1).
  - [HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models](https://aclanthology.org/2025.acl-long.679.pdf)
- **Formal reasoning** (construct): *causes*, 1 paper
  > Since our answers are formally provable, it conveys a more solid foundation and trustworthiness than direct NL reasoning. (Section 2)
  - [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf)
- **Verbal uncertainty** (construct): *causes*, 1 paper
  > Enabling models to either refuse to answer or explicitly express uncertainty has emerged as a promising direction to reduce hallucinations and enhance trustworthiness (Section 1).
  - [UNCLE: Benchmarking Uncertainty Expressions in Long-Form Generation](https://aclanthology.org/2025.emnlp-main.1543.pdf)

### Associated with
- **Privacy preservation** (construct), 2 papers
  > We assess the trustworthiness of Med-LVLMs across five dimensions, including trustfulness, fairness, safety, privacy, and robustness. (Abstract)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Robustness** (construct), 2 papers
  > We assess the trustworthiness of Med-LVLMs across five dimensions, including trustfulness, fairness, safety, privacy, and robustness. (Abstract)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Truthfulness** (construct), 2 papers
  > Specifically, we divide model trustworthiness into robustness and truthfulness.
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Alignment** (construct), 2 papers
  > identifying units whose outputs meet a user-specified alignment criterion... certifying their corresponding outputs as trustworthy.
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Safety** (construct), 1 paper
  > We assess the trustworthiness of Med-LVLMs across five dimensions, including trustfulness, fairness, safety, privacy, and robustness. (Abstract)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Fairness** (construct), 1 paper
  > We assess the trustworthiness of Med-LVLMs across five dimensions, including trustfulness, fairness, safety, privacy, and robustness. (Abstract)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Toxicity** (construct), 1 paper
  > These components [truthfulness, toxicity, fairness, robustness, privacy, and machine ethics] collectively contribute to a comprehensive framework for assessing and improving LLM trustworthiness. (Section 2)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Stereotyping** (construct), 1 paper
  > this study investigates how models aligned with general-purpose preference data perform across five trustworthiness verticals: toxicity, stereotypical bias, machine ethics, truthfulness, and privacy.
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Moral reasoning** (construct), 1 paper
  > These components [truthfulness, toxicity, fairness, robustness, privacy, and machine ethics] collectively contribute to a comprehensive framework for assessing and improving LLM trustworthiness. (Section 2)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Human preference alignment** (construct), 1 paper
  > Our results demonstrate that RLHF on human preferences doesn’t automatically guarantee trustworthiness, and reverse effects are often observed. (Section 1)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Biased content generation** (behavioral indicator), 1 paper
  > However, MLLMs are proven to exhibit significant drawbacks in trustworthiness, such as hallucination (Rawte et al., 2023; Zhang et al., 2024; Wang et al., 2024a), which results in non-factual information (Ji et al., 2023) and biased generations (Zou et al., 2023). (Section 1)
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
- **Calibration** (construct), 1 paper
  > By improving the trustworthiness of LLMs, IB-EDL facilitates their broader adoption in domains requiring high levels of confidence calibration.
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **Factuality** (construct), 1 paper
  > “The evaluation of trustfulness includes assessments of factuality and uncertainty.”
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
