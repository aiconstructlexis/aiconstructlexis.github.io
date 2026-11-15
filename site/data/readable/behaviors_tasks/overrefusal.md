# Overrefusal
**Type:** Behavioral indicator  
**Supporting papers:** 35  
**Also known as:** Over-refusal, Over-rejection, Over-refusal tendency, Over-sensitivity, Over-defense, False refusal, False rejection, Unwarranted refusal, Exaggerated safety behaviors, Oversafety, Benign query refusal  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing is inappropriate refusal of benign, harmless, safe, legitimate, or answerable queries, usually after they are misread as harmful or risky. Most descriptions cast this either as a latent tendency toward excessive caution, poor calibration, or overgeneralized safety thresholds, or as the observable behavior of refusing a prompt even though a helpful, valid, or safe response is possible. A recurring narrower formulation focuses on benign or borderline prompts that only superficially resemble harmful content, including prompts that merely appear toxic or only seem harmful. Some papers make the success criterion explicit by treating it as overrefusal when an external evaluator deems the content safe, when a valid answer exists, or when refusal probability on benign inputs exceeds a threshold.

**Variants.** Most commonly, papers use overrefusal or over-refusal, while a smaller line of work uses labels such as over-rejection, false refusal, over-defense, over-sensitivity, and oversafety, with other isolated names including false rejection, unwarranted refusal, exaggerated safety behaviors, and benign query refusal. The behavior is studied on benign, borderline, ambiguous, or semantically similar safe prompts, sometimes specifically on sensitive but non-harmful topics, identity-term queries, or benign instructions that appear toxic. Some papers extend the setting to multimodal or audio language models, and one benchmark is explicitly multilingual.

**Space of elicitation and scores.** Papers link overrefusal to 8 measurement instruments. XSTest is the most common and is described as a test suite for false refusal, exaggerated safety, over-rejection, or over-defense on benign prompts or legitimate requests; OR-Bench is another prevalent benchmark, and papers also use OKTest, OR-Bench-Hard-1K, WildChat, and 3 other instruments, typically as benchmarks, test suites, or datasets. Scoring is usually cast as refusal or over-refusal rate on benign queries, false refusal rate or OR rate, or alternatively as compliance ratio on benign prompts.

**What it is taken as evidence of.** Papers link overrefusal to 4 constructs, and they do not converge on a single construct it reflects. The prevailing construct link is a claimed causal relationship from Safety alignment to overrefusal, often described as a side effect of stricter safety alignment or supervised fine-tuning. Other papers claim a causal relationship from overrefusal to Helpfulness and to Utility preservation, using language about diminished helpfulness or limited utility, and one paper reports it as related to Safety.

## Sources

**Over-refusal** (5 papers: [Reimagining Safety Alignment with An Image](https://aclanthology.org/2025.emnlp-main.485.pdf), [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf), [Exploiting LLM Quantization](https://proceedings.neurips.cc/paper_files/paper/2024/file/496720b3c860111b95ac8634349dcc88-Paper-Conference.pdf), [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf), [Improving LLM Safety Alignment with Dual-Objective Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25c/zhao25c.pdf))
> A latent tendency of a model to inappropriately reject benign or borderline queries due to overly strict safety mechanisms, reflecting poor calibration of safety thresholds.

**Over-rejection** (1 paper: [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf))
> The tendency of a model to inappropriately refuse benign queries, often as a side effect of safety training, reflecting a failure to distinguish between harmful and semantically similar but safe inputs.

**Over-refusal tendency** (1 paper: [Governance in Motion: Co-evolution of Constitutions and AI models for Scalable Safety](https://aclanthology.org/2025.emnlp-main.869.pdf))
> The propensity of a model to inappropriately refuse to answer harmless or benign queries, reflecting an imbalance between safety and helpfulness.

**Overrefusal** (3 papers: [Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary](https://aclanthology.org/2025.emnlp-main.1065.pdf), [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf), [Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf))
> The latent tendency of a model to incorrectly refuse to answer legitimate, benign queries by misclassifying them as harmful.

**Over-sensitivity** (1 paper: [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf))
> A safety-related disposition where the model excessively refuses benign or ambiguous queries that only superficially resemble harmful ones, potentially reducing usability.

**Over-defense** (1 paper: [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.384.pdf))
> The behavior of incorrectly refusing to answer benign or harmless queries, often due to overly cautious safety mechanisms.

**False refusal** (2 papers: [Speculative Safety-Aware Decoding](https://aclanthology.org/2025.emnlp-main.648.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf))
> The observable behavior of a model incorrectly refusing to answer a benign query that touches on sensitive but non-harmful topics.

**False rejection** (1 paper: [AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender](https://aclanthology.org/2025.emnlp-main.1248.pdf))
> The observable behavior of a model incorrectly refusing to respond to benign inputs, often due to over-enforcement of safety rules.

**Unwarranted refusal** (1 paper: [Sparse Activation Editing for Reliable Instruction Following in Narratives](https://aclanthology.org/2025.emnlp-main.1311.pdf))
> The behavior of a model refusing to respond to a valid, benign user query, often as a side effect of safety interventions.

**Exaggerated safety behaviors** (1 paper: [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf))
> A latent tendency for models to overgeneralize safety constraints, leading to unwarranted refusals to respond to safe or benign queries, especially those involving identity terms.

**Oversafety** (1 paper: [DREAM: Disentangling Risks to Enhance Safety Alignment in Multimodal Large Language Models](https://aclanthology.org/2025.naacl-long.604.pdf))
> A latent tendency of an MLLM to inappropriately refuse or avoid responding to safe or benign inputs due to overgeneralization of safety rules or misperception of risk.

**Benign query refusal** (1 paper: [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf))
> The observable behavior of incorrectly rejecting safe and legitimate user queries, often as a side effect of safety mechanisms.

## Relationships

### Overrefusal →
- **XSTest** (measurement instrument): *measured_by*, 12 papers
  > We also report the model compliance rate on 100 held-out test examples from XSTest to monitor over refusals. (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf)
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
  - [Safety Reasoning with Guidelines](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cg/wang25cg.pdf)
  - [Improving LLM Safety Alignment with Dual-Objective Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25c/zhao25c.pdf)
  - [The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wollschlager25a/wollschlager25a.pdf)
  - [Sparse Activation Editing for Reliable Instruction Following in Narratives](https://aclanthology.org/2025.emnlp-main.1311.pdf)
  - [SDGO: Self-Discrimination-Guided Optimization for Consistent Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.253.pdf)
  - [Speculative Safety-Aware Decoding](https://aclanthology.org/2025.emnlp-main.648.pdf)
  - [Governance in Motion: Co-evolution of Constitutions and AI models for Scalable Safety](https://aclanthology.org/2025.emnlp-main.869.pdf)
- **OR-Bench** (measurement instrument): *measured_by*, 3 papers
  > Our experiments show that Safe Delta avoids over-defense issues. We evaluate over-refusal using the OR Bench (Cui et al., 2024). (Section 5.7)
  - [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf)
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
  - [Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary](https://aclanthology.org/2025.emnlp-main.1065.pdf)
- **Helpfulness** (construct): *causes*, 3 papers
  > increased model over-rejection, resulting in diminished helpfulness
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)
  - [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf)
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
- **WildChat** (measurement instrument): *measured_by*, 2 papers
  > “we construct an over-refusal evaluation using the WildChat dataset [74].”
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
  - [Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea13534ee239bb3977795b8cc855bacc-Paper-Conference.pdf)
- **OKTest** (measurement instrument): *measured_by*, 2 papers
  > For the false refusal tests, we use one in-distribution dataset Dtest pseudo harmful (ORB-H) and two out-of-distribution datasets: OKTEST (Shi et al., 2024) and XSTEST (Röttger et al., 2024) (Section 4).
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
- **OR-Bench-Hard-1K** (measurement instrument): *measured_by*, 2 papers
  > Over refusal rate vs toxic prompts rejection rate on OR-Bench-Hard-1K and OR-Bench-Toxic. (Figure 1)
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
- **PHTest** (measurement instrument): *measured_by*, 1 paper
  > We evaluate over-refusal using the held-out versions of XSTest (150 samples), SCOPE (593 samples), OR-Bench-Hard-1K (1219 samples), and PHTest (1977 samples) benchmarks... (Section 4.1)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
- **MORBENCH** (measurement instrument): *measured_by*, 1 paper
  > In this section, we introduce our MORBENCH (Multilingual Over-Refusal Benchmark), a large-scale, automatically constructed benchmark designed to evaluate overrefusal behaviors of LLMs across diverse languages and safety categories. (Section 4)
  - [Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary](https://aclanthology.org/2025.emnlp-main.1065.pdf)
- **Utility preservation** (construct): *causes*, 1 paper
  > for benign inputs, such reinforcement of refusal behavior significantly increases the risk of false rejections, limiting the model’s overall utility
  - [AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender](https://aclanthology.org/2025.emnlp-main.1248.pdf)
- **AIAH** (measurement instrument): *measured_by*, 1 paper
  > We adopt AIAH (Yang et al., 2025) as the benchmark ... and [its] provided benign question dataset is used to evaluate over-rejection.
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)

### → Overrefusal
- **Safety alignment** (construct): *causes*, 6 papers
  > Safety alignment is crucial for Large Language Models (LLMs) to resist malicious instructions but often results in over-refusals, where benign prompts are unnecessarily rejected, impairing user experience and model utility. (Abstract)
  - [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf)
  - [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf)
  - [Reimagining Safety Alignment with An Image](https://aclanthology.org/2025.emnlp-main.485.pdf)
  - [Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary](https://aclanthology.org/2025.emnlp-main.1065.pdf)
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)
  - [Safety Layers in Aligned Large Language Models: The Key to LLM Security](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3bfbd65743e60c685a3845bd61ce15f-Paper-Conference.pdf)

### Associated with
- **Safety** (construct), 1 paper
  > Bianchi et al. (2023) highlights that incorporating safety-related examples during finetuning enhances model safety but often results in increased overrefusal. (Section 2.1. Instruction Finetuning)
  - [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf)
