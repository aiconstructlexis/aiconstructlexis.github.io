# CommonsenseQA
**Type:** Measurement instrument  
**Supporting papers:** 141  
**Also known as:** CommonSenseQA, CSQA, Commonsense QA, Commonsense-QA, CommonSense-QA, CommonsenseQA (CSQA), CMSQA, CQA  

## State of the Field

**What it is.** Across papers, the prevailing usage treats CommonsenseQA as a multiple-choice commonsense question-answering benchmark or dataset for everyday or real-world knowledge. Definitions usually say it evaluates commonsense reasoning, and several specify five answer options, or four distractors, with questions that require identifying relevant knowledge and ruling out plausible distractors; some add that the questions are designed to resist superficial cues. A smaller line of work frames it as testing general understanding or general knowledge, one description says it covers social, physical, and psychological domains, some report more than 10,000 or 12,102 questions, and one paper describes CSQA as comprising seven multiple-choice tasks. A few papers also describe it as built on or using ConceptNet, and one uses it as the basis for the ACCORDCSQA benchmark suite.

**What it is claimed to measure.** Papers use CommonsenseQA to measure 14 constructs and 4 behavioral indicators overall, but the dominant link is to Commonsense reasoning. The most frequently listed construct links after that are General ability, General reasoning, Reasoning, and Editing locality. On the behavioral side, papers use it for Multiple-choice question answering, Commonsense question answering, Question answering, and Out-of-distribution detection. The claims converge most strongly on commonsense reasoning, while smaller lines of work also report it as measuring broader capabilities.

**Space of uses.** Many papers include CommonsenseQA as one benchmark in a broader evaluation package, commonly alongside StrategyQA, OpenBookQA, ARC, MMLU, and SocialIQA. It is often positioned as a standard general-domain or downstream check, though some papers use it more specifically for instruction tuning and retriever fine-tuning, multiple-choice answer prediction, zero-shot transfer, or as an out-of-distribution test set. Papers also relate it to three evaluation tools or suites: OLMES, OpenCompass, and lm-evaluation-harness.

**Concerns raised.** An explicit concern papers raise is contamination. In "Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models", the authors apply probes on CommonsenseQA test sets to look for "evidence of contamination". "Improving Model Evaluation using SMART Filtering of Benchmark Datasets" also studies SMART filtering on CommonsenseQA in the classical multiple-choice QA setting.

## Sources

**CommonsenseQA** (25 papers: [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf), [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf), [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf), [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf), [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf), [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf), [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf), [Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://aclanthology.org/2025.naacl-long.99.pdf), [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf), [Improving Model Evaluation using SMART Filtering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.235.pdf), [ACCORD: Closing the Commonsense Measurability Gap](https://aclanthology.org/2025.naacl-long.193.pdf), [Disentangling Memory and Reasoning Ability in Large Language Models](https://aclanthology.org/2025.acl-long.84.pdf), [Emergent Response Planning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25p/dong25p.pdf), [DICE: Structured Reasoning in LLMs through SLM-Guided Chain-of-Thought Correction](https://aclanthology.org/2025.emnlp-main.355.pdf), [Chain of Thoughtlessness? An Analysis of CoT in Planning](https://proceedings.neurips.cc/paper_files/paper/2024/file/3365d974ce309623bd8151082d78206c-Paper-Conference.pdf), [Cost-efficient Knowledge-based Question Answering with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0aafec03d59db29a92fa683bd783374-Paper-Conference.pdf), [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf), [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf), [Instance-adaptive Zero-shot Chain-of-Thought Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/e304e04a6f455dd82f8a85a0a3679493-Paper-Conference.pdf), [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf), [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf), [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf), [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf), [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf))
> A commonsense question answering benchmark used to evaluate commonsense reasoning.

**CommonSenseQA** (4 papers: [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf), [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf), [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf), [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf))
> CommonSenseQA is a commonsense question-answering benchmark used here to evaluate general understanding.

**CSQA** (2 papers: [L4Q: Parameter Efficient Quantization-Aware Fine-Tuning on Large Language Models](https://aclanthology.org/2025.acl-long.99.pdf), [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf))
> A benchmark named Commonsense QA that evaluates a model's commonsense reasoning capabilities through a collection of multiple-choice question-answering tasks.

**Commonsense QA** (3 papers: [Nemotron-CC: Transforming Common Crawl into a Refined Long-Horizon Pretraining Dataset](https://aclanthology.org/2025.acl-long.123.pdf), [LaMDAgent: An Autonomous Framework for Post-Training Pipeline Optimization via LLM Agents](https://aclanthology.org/2025.emnlp-main.1529.pdf), [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf))
> A multiple-choice question answering dataset that requires commonsense knowledge to predict the correct answers.

**Commonsense-QA** (1 paper: [Understanding Overadaptation in Supervised Fine-Tuning: The Role of Ensemble Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25d/hao25d.pdf))
> Question-answering dataset with over 10,000 real-world commonsense questions requiring models to identify relevant knowledge and distinguish plausible distractors.

**CommonSense-QA** (1 paper: [EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf))
> A multiple-choice question answering dataset that requires commonsense knowledge to predict the correct answer, with questions designed to be difficult for models that rely on superficial cues.

**CommonsenseQA (CSQA)** (1 paper: [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf))
> A multiple-choice question answering benchmark designed to evaluate a model's commonsense reasoning and general knowledge.

**CMSQA** (1 paper: [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf))
> CommonsenseQA (CMSQA) is a multiple-choice question answering dataset that targets commonsense knowledge.

**CQA** (1 paper: [QCRD: Quality-guided Contrastive Rationale Distillation for Large Language Models](https://aclanthology.org/2025.emnlp-main.724.pdf))
> Commonsense Question Answering dataset that assesses a model's ability to answer questions requiring general world knowledge and everyday reasoning.

## Relationships

### → CommonsenseQA
- **Commonsense reasoning** (construct): *measured_by*, 33 papers
  > For commonsense reasoning, we consider CSQA for multiple-choice questions (Talmor et al., 2019) and StrategyQA for true or false questions (Geva et al., 2021) (Section 4.1).
  - [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf)
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
  - [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [Instance-adaptive Zero-shot Chain-of-Thought Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/e304e04a6f455dd82f8a85a0a3679493-Paper-Conference.pdf)
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
  - [GraphVis: Boosting LLMs with Visual Knowledge Graph Integration](https://proceedings.neurips.cc/paper_files/paper/2024/file/7cb04f510593c9ba30da398f5e0a7e7b-Paper-Conference.pdf)
  - [Balancing Act: Diversity and Consistency in Large Language Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5554e55d7a21e62d0d7a028ec0ea1c7-Paper-Conference.pdf)
  - [MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/abbbb25cddb2c2cd08714e6bfa2f0634-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
  - [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.157.pdf)
  - [Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling](https://aclanthology.org/2025.naacl-long.184.pdf)
  - [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.309.pdf)
  - [Reverse Thinking Makes LLMs Stronger Reasoners](https://aclanthology.org/2025.naacl-long.434.pdf)
  - [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf)
  - [Forward Knows Efficient Backward Path: Saliency-Guided Memory-Efficient Fine-tuning of Large Language Models](https://aclanthology.org/2025.acl-long.459.pdf)
  - [Tracing and Dissecting How LLMs Recall Factual Knowledge for Real World Questions](https://aclanthology.org/2025.acl-long.1133.pdf)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
  - [GIVE: Structured Reasoning of Large Language Models with Knowledge Graph Inspired Veracity Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25o/he25o.pdf)
  - [Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf)
  - [CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs](https://aclanthology.org/2025.emnlp-main.704.pdf)
  - [Improving Reasoning Capabilities in Small Models through Mixture-of-layers Distillation with Stepwise Attention on Key Information](https://aclanthology.org/2025.emnlp-main.250.pdf)
  - [Reasoning under Uncertainty: Efficient LLM Inference via Unsupervised Confidence Dilution and Convergent Adaptive Sampling](https://aclanthology.org/2025.emnlp-main.1638.pdf)
  - [ThinkSLM: Towards Reasoning in Small Language Models](https://aclanthology.org/2025.emnlp-main.1659.pdf)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-Only LLMs](https://aclanthology.org/2025.emnlp-main.481.pdf)
  - [Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?](https://aclanthology.org/2025.emnlp-main.1516.pdf)
  - [Connecting the Knowledge Dots: Retrieval-augmented Knowledge Connection for Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 7 papers
  > We conduct experiments on MMLU (Hendrycks et al., 2020), ARC-Challenge (Clark et al., 2018), and CommonsenseQA (CSQA) (Talmor et al., 2019), which are all MCQ benchmarks widely used for LLM evaluation.
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
  - [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf)
  - [Taming Overconfidence in LLMs: Reward Calibration in RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/29fb6e1456b3d8b57ede5c45aa2c6537-Paper-Conference.pdf)
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
  - [Improving Model Evaluation using SMART Filtering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.235.pdf)
  - [HARP: Hesitation-Aware Reframing in Transformer Inference Pass](https://aclanthology.org/2025.naacl-long.612.pdf)
- **Commonsense question answering** (behavioral indicator): *measured_by*, 6 papers
  > CommonSenseQA (Talmor et al., 2019): This dataset offers a collection of multi-choice questions that test commonsense reasoning. (Section 3.1)
  - [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf)
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
  - [Beyond Surface Structure: A Causal Assessment of LLMs' Comprehension ability](https://proceedings.iclr.cc/paper_files/paper/2025/file/88139fdcc82fc597090620d77b023282-Paper-Conference.pdf)
  - [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf)
  - [Understanding Overadaptation in Supervised Fine-Tuning: The Role of Ensemble Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25d/hao25d.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 3 papers
  > CommonsenseQA [63] is to test models’ ability to answer questions using only the parameterized knowledge instead of the context knowledge. (Appendix E.2)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
  - [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)
- **General ability** (construct): *measured_by*, 2 papers
  > We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
  - [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 2 papers
  > Our evaluations on standard reasoning datasets (GSM8K, CSQA, and LLC) with various LLMs and prompts show that TREACLE enables cost savings of up to 85% compared to baselines, while maintaining high accuracy. (Abstract)
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
  - [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)
- **General reasoning** (construct): *measured_by*, 2 papers
  > To evaluate the generalization ability of our method and mitigate the risk of catastrophic forgetting, we conduct experiments on commonsense and reasoning datasets, including CSQA (Talmor et al., 2018), Hellaswag (Zellers et al., 2019), and MMLU-pro (Wang et al., 2024). (Section 5.6)
  - [CulFiT: A Fine-grained Cultural-aware LLM Training Paradigm via Multilingual Critique Data Synthesis](https://aclanthology.org/2025.acl-long.1092.pdf)
  - [Enhancing Chain-of-Thought Reasoning via Neuron Activation Differential Analysis](https://aclanthology.org/2025.emnlp-main.817.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > In this section, we investigate whether our method is generally applicable beyond the medical domain. We use two general domain datasets, CommonsenseQA (CSQA) (Talmor et al., 2018) and OpenbookQA (OBQA) (Mihaylov et al., 2018)... (Section 4.5)
  - [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf)
- **Short-context ability** (construct): *measured_by*, 1 paper
  > We select 8 short-context tasks commonly used for evaluating the general capabilities of models. These include... CommonsenseQA (CSQA)... (Section 4.1)
  - [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf)
- **Knowledge reasoning** (construct): *measured_by*, 1 paper
  > For knowledge reasoning, we utilize Winogrande (Sakaguchi et al., 2019) (abbreviated as Wino) and CommonsenseQA (Talmor et al., 2019) (abbreviated as Comm). (Section 4)
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
- **In-context learning** (construct): *measured_by*, 1 paper
  > IP = 1 N g PN g j=1 ˆa T e j N , which is the average in-context performance on N g general evaluation tasks... We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Out-of-distribution detection** (behavioral indicator): *measured_by*, 1 paper
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **Natural language understanding** (construct): *measured_by*, 1 paper
  > To evaluate multitask performance, we test on several NLP benchmarks, including MMLU (Hendrycks et al., 2020), MMLU-Pro (Wang et al., 2024), ARC-Easy, ARC-Challenge (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018), SWAG (Zellers et al., 2018), and CommonsenseQA (Talmor et al., 2018). These benchmarks consist of multiple-choice questions, assessing various aspects of the model's natural language understanding.
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **World knowledge** (construct): *measured_by*, 1 paper
  > We measure general knowledge using the CommonsenseQA (CSQA) (Talmor et al., 2019) dataset... (Section 4.1)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Self-correction ability** (construct): *measured_by*, 1 paper
  > We evaluate self-correction capability on both classification and generation tasks, including domains in mathematics, coding, instruction following, common-sense reasoning, and knowledge. To be specific, the dataset we utilized include ... CommonsenseQA (Talmor et al., 2019). (Section 4.1)
  - [Confidence v.s. Critique: A Decomposition of Self-Correction Capability for LLMs](https://aclanthology.org/2025.acl-long.203.pdf)
- **Zero-shot generalization** (construct): *measured_by*, 1 paper
  > To further evaluate the generalizability of GCR, we conduct zero-shot transfer experiments on three new KGQA datasets: FreebaseQA, CSQA and MedQA (Section 5.1).
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **Inductive reasoning** (construct): *measured_by*, 1 paper
  > “CommonsenseQA, a 5-choice multiple-choice benchmark, peaks in Inductive Reasoning”
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
- **Editing locality** (construct): *measured_by*, 1 paper
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)

### Associated with
- **lm-evaluation-harness** (measurement instrument), 1 paper
  > We use lm-evaluation-harness to report results on ... CommonSenseQA
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **OpenCompass** (measurement instrument), 1 paper
  > "We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA ..., ARC-challenge (ARC-C) ..., ARC-easy (ARC-E) ..., WinoGrande (WG) ..., HellaSwag (HLSG) ..., and CommonSenseQA (CSQA) ..."
  - [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf)
- **OLMES** (measurement instrument), 1 paper
  > "We use the OLMES suite of 10 multiple choice question answering benchmarks (Gu et al., 2024): ... CommonsenseQA (Talmor et al., 2019), SocialIQA ..."
  - [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf)
