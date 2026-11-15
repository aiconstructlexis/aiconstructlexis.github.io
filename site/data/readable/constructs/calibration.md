# Calibration
**Type:** Construct  
**Supporting papers:** 106  
**Also known as:** Miscalibration, Confidence calibration, QA-calibration, Belief calibration, Verbalized calibration, Linguistic calibration, Probability calibration, Disambiguation reliability, Uncertainty calibration, Faithful calibration  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats calibration as alignment between a model's confidence or predicted probabilities and the observed likelihood that its answer is correct: several definitions say that predictions made with confidence p should be correct about p of the time, or that samples with 80% confidence should have 80% accuracy. A smaller line of work narrows this to settings with contextual or prompt bias in in-context learning, framing calibration as correcting those biases or debiasing predictions with priors. Other papers shift the reference standard from answer correctness to statement truthfulness, agreement with human annotations, or the model's own intrinsic uncertainty; a smaller line also treats calibration as the ability to express graded confidence in natural language. Only a few definitions depart further, treating calibration as matching a draft model's probabilities to a target model's, or as deciding when to answer versus abstain.

**Space of facets.** Most subtype labels keep the same alignment template but change what is conditioned on or what is being aligned. Confidence calibration and probability calibration stay close to the average-case notion, one paper formalizes this as expected correctness at confidence p equaling p, and QA-calibration extends it so the same match must hold within question-answer groups. Other task-specific variants include belief calibration for truthfulness, faithful calibration for intrinsic versus expressed uncertainty, linguistic calibration for numerical confidence in language, uncertainty calibration around known versus unknown information, and disambiguation reliability for self-assessed accuracy in word sense disambiguation. Papers also draw boundaries with neighboring notions: one contrasts calibration with distribution alignment, which compares probabilities over the entire label set rather than only the predicted label, and another uses miscalibration as the converse label for poor alignment.

**Space of measurement.** Operationally, papers link calibration to 12 measurement instruments and 9 behavioral indicators. Measurement is mostly benchmark-based, especially on MMLU, StrategyQA, AG News, ARC-Challenge, and BIG-bench, with several other QA and multimodal benchmarks also used; papers commonly compare confidence or output probabilities to observed accuracy with expected calibration error, and sometimes maximum calibration error, reliability diagrams, or calibrated confidence intervals. Other operationalizations change the unit of analysis rather than the core comparison, using token-level or verbalized probabilities, claim-level or reasoning-step confidence, relevance probabilities for ranking, or a dedicated uncertainty token. These measurements largely match the dominant confidence-accuracy definition, though some instead target group-conditional QA-calibration, statement truthfulness, or alignment between expressed and intrinsic uncertainty.

**Links.** Papers link calibration to 16 constructs and 9 behavioral indicators overall. Overconfidence is the most frequently linked construct: one paper claims a causal relationship from overconfidence to calibration, phrasing overconfidence as producing poor calibration, while other papers treat the pair as related or correlated. Smaller lines of work also connect confidence estimation and in-context learning to calibration, including one causal claim from each alongside related claims. In the other direction, papers claim causal relationships from calibration to hallucination and to reliability, and additional papers connect calibration to other constructs and behaviors through causal, correlational, and related claims.

## Sources

**Calibration** (25 papers: [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf), [Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf), [Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/6733cf15e10e2cd1d59af033c3bb8507-Paper-Conference.pdf), [Energy-based Automated Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5ef1df239d6640a27dd6ed9a59f518c9-Paper-Conference.pdf), [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf), [Learning to Reject with a Fixed Predictor: Application to Decontextualization](https://proceedings.iclr.cc/paper_files/paper/2024/file/c17f3035898a7044194fe45c5df6c6e8-Paper-Conference.pdf), [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf), [Measuring Vision-Language STEM Skills of Neural Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a3a661eb3308d0bb686f6a4bac521032-Paper-Conference.pdf), [MiniLLM: Knowledge Distillation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/8ac015d409635f196f9e3e9dcfb9a94e-Paper-Conference.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [Confidence Regulation Neurons in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e21955c93dede886af1d0d362c756757-Paper-Conference.pdf), [Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/03dfa2a7755635f756b160e9f4c6b789-Paper-Conference.pdf), [Can Unconfident LLM Annotations Be Used for Confident Conclusions?](https://aclanthology.org/2025.naacl-long.179.pdf), [MICE for CATs: Model-Internal Confidence Estimation for Calibrating Agents with Tools](https://aclanthology.org/2025.naacl-long.615.pdf), [From Evidence to Belief: A Bayesian Epistemology Approach to Language Models](https://aclanthology.org/2025.naacl-long.531.pdf), [DIRAS: Efficient LLM Annotation of Document Relevance for Retrieval Augmented Generation](https://aclanthology.org/2025.naacl-long.271.pdf), [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf), [Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations](https://aclanthology.org/2025.naacl-long.162.pdf), [DAWN-ICL: Strategic Planning of Problem-solving Trajectories for Zero-Shot In-Context Learning](https://aclanthology.org/2025.naacl-long.96.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf), [Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion](https://aclanthology.org/2025.naacl-long.601.pdf), [HALoGEN: Fantastic LLM Hallucinations and Where to Find Them](https://aclanthology.org/2025.acl-long.71.pdf), [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf), [Preemptive Detection and Correction of Misaligned Actions in LLM Agents](https://aclanthology.org/2025.emnlp-main.12.pdf))
> The degree to which a model's predicted probabilities reflect true likelihoods of correctness, particularly in the presence of contextual biases from prompts or in-context examples.

**Miscalibration** (1 paper: [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf))
> The degree to which a model's output probabilities are poorly aligned with the true likelihood of correctness, leading to unreliable confidence scores.

**Confidence calibration** (2 papers: [Selective Generation for Controllable Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a6815122f533193a022cbc41786c1cc-Paper-Conference.pdf), [MAC-Tuning: LLM Multi-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.35.pdf))
> The degree to which a model's expressed confidence in its predictions aligns with its actual correctness.

**QA-calibration** (1 paper: [QA-Calibration of Language Model Confidence Scores](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd96cb9a239c37b39dbf34f3f5a4c56f-Paper-Conference.pdf))
> A latent property where a model's confidence scores match its actual accuracy conditional on specific groups of question-and-answer pairs, ensuring reliability across different topics or user contexts.

**Belief calibration** (1 paper: [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf))
> The extent to which the model's expressed confidence in a statement matches the statement's actual truthfulness.

**Linguistic calibration** (1 paper: [UNCLE: Benchmarking Uncertainty Expressions in Long-Form Generation](https://aclanthology.org/2025.emnlp-main.1543.pdf))
> The ability of a model to express graded levels of confidence in its statements, often through numerical scores embedded in natural language.

**Probability calibration** (1 paper: [Not Your Typical Government Tipline: LLM-Assisted Routing of Environmental Protection Agency Citizen Tips](https://aclanthology.org/2025.emnlp-main.1788.pdf))
> The degree to which the model's confidence scores align with actual classification accuracy, enabling reliable threshold-based decision-making in operational settings.

**Disambiguation reliability** (1 paper: [RoDEval: A Robust Word Sense Disambiguation Evaluation Framework for Large Language Models](https://aclanthology.org/2025.emnlp-main.864.pdf))
> The alignment between a model’s self-assessed confidence in its disambiguation ability and its actual accuracy, reflecting cognitive awareness and trustworthiness of outputs.

**Uncertainty calibration** (1 paper: [Alleviating Hallucinations from Knowledge Misalignment in Large Language Models via Selective Abstention Learning](https://aclanthology.org/2025.acl-long.1199.pdf))
> The model's ability to accurately represent its own uncertainty, particularly in distinguishing between known and unknown information, to guide generation.

**Faithful calibration** (1 paper: [MetaFaith: Faithful Natural Language Uncertainty Expression in LLMs](https://aclanthology.org/2025.emnlp-main.1505.pdf))
> The degree to which a model's linguistically expressed uncertainty aligns with its intrinsic uncertainty, reflecting a trustworthy and accurate communication of confidence.

## Relationships

### Calibration →
- **MMLU** (measurement instrument): *measured_by*, 4 papers
  > Table 2 shows the performance of the posthoc calibrators on MMLU and BigBench datasets.
  - [QA-Calibration of Language Model Confidence Scores](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd96cb9a239c37b39dbf34f3f5a4c56f-Paper-Conference.pdf)
  - [Calibrated Language Models and How to Find Them with Label Smoothing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25w/huang25w.pdf)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
  - [Calibration Across Layers: Understanding Calibration Evolution in LLMs](https://aclanthology.org/2025.emnlp-main.742.pdf)
- **Hallucination** (behavioral indicator): *causes*, 3 papers
  > Calibrating language models (LMs) is crucial, as it plays a vital role in detecting and mitigating hallucinations of LMs as well as building more trustworthy models. (ABSTRACT)
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
  - [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf)
  - [Trustworthy Medical Question Answering: An Evaluation-Centric Survey](https://aclanthology.org/2025.emnlp-main.1398.pdf)
- **StrategyQA** (measurement instrument): *measured_by*, 2 papers
  > "We evaluate the quality of confidence estimates across five types of reasoning tasks: 1) Commonsense Reasoning on two benchmarks, Sports Understanding (SportUND) ... StrategyQA (Geva et al., 2021)"
  - [Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/6733cf15e10e2cd1d59af033c3bb8507-Paper-Conference.pdf)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **Reliability** (construct): *causes*, 2 papers
  > Confidence calibration is a critical aspect in developing reliable and trustworthy language models (Nguyen & O’Connor, 2015; Guo et al., 2017; Minderer et al., 2021).
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
  - [COM-BOM: Bayesian Exemplar Search for Efficiently Exploring the Accuracy-Calibration Pareto Frontier](https://aclanthology.org/2025.emnlp-main.1027.pdf)
- **Hedging** (behavioral indicator): *causes*, 1 paper
  > Qualitatively, we find that a LACIE-trained model hedges more when uncertain and adopts implicit cues to signal certainty when it is correct, such as using an authoritative tone or including details. (Abstract)
  - [LACIE: Listener-Aware Finetuning for Calibration in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8eaf3bcdc105423a972ed90eb07217-Paper-Conference.pdf)
- **Abstention** (behavioral indicator): *causes*, 1 paper
  > Finally, finetuning with our listener-aware method leads to an emergent increase in model abstention (e.g. saying “I don’t know”) for answers that are likely to be wrong, trading recall for precision. (Abstract)
  - [LACIE: Listener-Aware Finetuning for Calibration in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8eaf3bcdc105423a972ed90eb07217-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > We then finetune three different LLMs (Mistral-7B, Llama3-8B, Llama3-70B) with LACIE, and show that the models resulting from this multi-agent optimization are better calibrated on TriviaQA with respect to a simulated listener. (Abstract)
  - [LACIE: Listener-Aware Finetuning for Calibration in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8eaf3bcdc105423a972ed90eb07217-Paper-Conference.pdf)
- **Decision-making under uncertainty** (construct): *causes*, 1 paper
  > LLMs, without proper calibration, can be overly confident in their responses... Such pitfalls make them unlikely to make reliable decisions under uncertainty.
  - [DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf)
- **BIG-bench** (measurement instrument): *measured_by*, 1 paper
  > Table 2 shows the performance of the posthoc calibrators on MMLU and BigBench datasets.
  - [QA-Calibration of Language Model Confidence Scores](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd96cb9a239c37b39dbf34f3f5a4c56f-Paper-Conference.pdf)
- **SST-2** (measurement instrument): *measured_by*, 1 paper
  > We first demonstrate that LLama3 is well-calibrated for the SST2, AG-News, and StrategyQA tasks, as illustrated in Table 1 and Figure 3. (Section 5.1)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **AG News** (measurement instrument): *measured_by*, 1 paper
  > We first demonstrate that LLama3 is well-calibrated for the SST2, AG-News, and StrategyQA tasks, as illustrated in Table 1 and Figure 3. (Section 5.1)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **Factuality** (construct): *causes*, 1 paper
  > Numerous studies have explored ways to improve factuality at various stages, such as continual pre-training (Chang et al., 2024), uncertainty calibration (Cohen et al., 2024), factuality alignment (Tian et al., 2024), and contrastive decoding (Section 2).
  - [Alleviating Hallucinations from Knowledge Misalignment in Large Language Models via Selective Abstention Learning](https://aclanthology.org/2025.acl-long.1199.pdf)
- **MedMCQA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the ECE and Accuracy using four diverse datasets: MMLU, MedMCQA, OpenBookQA, Arc-Challenge... (Section 6.1)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the ECE and Accuracy using four diverse datasets: MMLU, MedMCQA, OpenBookQA, Arc-Challenge... (Section 6.1)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the ECE and Accuracy using four diverse datasets: MMLU, MedMCQA, OpenBookQA, Arc-Challenge... (Section 6.1)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **MMMU-Pro** (measurement instrument): *measured_by*, 1 paper
  > We adopt the MMMU-Pro benchmark (Yue et al., 2024) to measure calibration on complex, multidisciplinary image understanding and reasoning problems. (Section 3.1.1)
  - [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf)
- **MathVista** (measurement instrument): *measured_by*, 1 paper
  > To evaluate calibration under visual mathematical reasoning, we employ MathVista (Lu et al., 2024) and MathVision (Wang et al., 2024). (Section 3.1.1)
  - [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf)
- **MathVision** (measurement instrument): *measured_by*, 1 paper
  > To evaluate calibration under visual mathematical reasoning, we employ MathVista (Lu et al., 2024) and MathVision (Wang et al., 2024). (Section 3.1.1)
  - [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf)
- **Verbal uncertainty** (construct): *causes*, 1 paper
  > "Band et al. (2024) introduce linguistic calibration, enabling models to express uncertainty at different levels (e.g., I am 70% sure)."
  - [UNCLE: Benchmarking Uncertainty Expressions in Long-Form Generation](https://aclanthology.org/2025.emnlp-main.1543.pdf)
- **Visual reasoning** (construct): *correlates*, 1 paper
  > "visual reasoning models (i.e., thinking with images) consistently exhibit better calibration"
  - [Seeing is Believing, but How Much? A Comprehensive Analysis of Verbalized Calibration in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.74.pdf)

### → Calibration
- **Overconfidence** (construct): *causes*, 5 papers
  > Fine-tuned large language models (LLMs) often exhibit overconfidence, particularly when trained on small datasets, resulting in poor calibration and inaccurate uncertainty estimates.
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
  - [Calibrated Language Models and How to Find Them with Label Smoothing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25w/huang25w.pdf)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
  - [Reasoning under Uncertainty: Efficient LLM Inference via Unsupervised Confidence Dilution and Convergent Adaptive Sampling](https://aclanthology.org/2025.emnlp-main.1638.pdf)
- **Confidence estimation** (behavioral indicator): *causes*, 3 papers
  > Bayesian methods, with their inherent ability to estimate uncertainty, serve as potent tools to mitigate overconfidence and enhance calibration. (Section ABSTRACT)
  - [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf)
  - [Zero-shot Model-based Reinforcement Learning using Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf)
  - [Calibration Across Layers: Understanding Calibration Evolution in LLMs](https://aclanthology.org/2025.emnlp-main.742.pdf)
- **In-context learning** (construct): *causes*, 2 papers
  > current exemplar selection strategies, by largely ignoring calibration, risk scenarios where gains in accuracy are achieved at the expense of degradation in calibration (Zhang et al., 2024b).
  - [COM-BOM: Bayesian Exemplar Search for Efficiently Exploring the Accuracy-Calibration Pareto Frontier](https://aclanthology.org/2025.emnlp-main.1027.pdf)
  - [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
- **World knowledge** (construct): *causes*, 1 paper
  > Our research reveals that LLMs’ prior knowledge causes potential poor calibration due to the ubiquitous presence of known data in real-world fine-tuning, which appears harmful for calibration. (Abstract)
  - [Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?](https://aclanthology.org/2025.acl-long.722.pdf)

### Associated with
- **Honesty** (construct), 1 paper
  > At its most basic level, the AI should provide accurate information, be well-calibrated, and express appropriate levels of uncertainty rather than misleading users. (Section 2)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Uncertainty** (construct), 1 paper
  > Recent work (Ren et al., 2023) shows that sequence-level confidence scores remain poorly calibrated with output quality, even after applying length normalization. (Section 2)
  - [UNCERTAINTY-LINE: Length-Invariant Estimation of Uncertainty for Large Language Models](https://aclanthology.org/2025.emnlp-main.400.pdf)
- **Claim decomposition** (behavioral indicator), 1 paper
  > This approach involves extracting distinct claims from the generated content, estimating the confidence associated with each claim, and then analyzing the calibration at the claim level. (Section 1)
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
- **Explanation generation** (behavioral indicator), 1 paper
  > We observe that RG leads to more conservative confidence estimates and lower expected calibration error (2.1 with RG vs. 2.9 without RG), which indicate that it enables more accurate identification of knowledge gaps via reasoning (Section 5.2).
  - [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf)
- **Self-verification** (behavioral indicator), 1 paper
  > "prior works have shown self-verification is not particularly effective for reasoning tasks and is often noisy and ill-calibrated"
  - [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf)
- **Future prediction** (behavioral indicator), 1 paper
  > We evaluate components of DeLLMa, including the calibration of its state forecasting approach and a human agreement study to assess its utility elicitation method. (Section 1).
  - [DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf)
- **Metacognition** (construct), 1 paper
  > If a model’s self-predictions are calibrated with respect to its ground-truth behavior, this suggests the model takes into account information about itself that was not in its training data. This would provide further evidence of introspection. (Section 3.3)
  - [Looking Inward: Language Models Can Learn About Themselves by Introspection](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf)
- **Distribution alignment** (construct), 1 paper
  > Our proposed distribution alignment setting differs from calibration in that it compares the probabilities over the entire label set whereas calibration only compares the predicted label probability to the ground truth. (Section 2.3)
  - [Large Language Models Do Multi-Label Classification Differently](https://aclanthology.org/2025.emnlp-main.126.pdf)
- **Trustworthiness** (construct), 1 paper
  > By improving the trustworthiness of LLMs, IB-EDL facilitates their broader adoption in domains requiring high levels of confidence calibration.
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **Internal consistency** (construct), 1 paper
  > This measure offers a straightforward method to gauge the level of internal consistency, serving as a useful indicator of the output’s correctness (i.e., calibration), without requiring additional training. (Section 3.2)
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
- **Visual robustness** (construct), 1 paper
  > By explicitly linking confidence calibration to visual robustness, this method reduces over-reliance on language priors. (Section 1)
  - [Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25r/huang25r.pdf)
- **Multiple-choice question answering** (behavioral indicator), 1 paper
  > The calibration error of an LLM is typically evaluated on a multiple-choice question and its corresponding correct answer, which can be formalized as an input-label pair (x, y)... (Section 3)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **Reasoning** (construct), 1 paper
  > “program-aided reasoning approaches, where LLMs utilize code representation, generally exhibit superior calibration compared to standard text-based reasoning methods that rely on CoT”
  - [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf)
