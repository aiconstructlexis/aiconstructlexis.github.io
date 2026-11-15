# Robustness
**Type:** Construct  
**Supporting papers:** 657  
**Also known as:** Model robustness, Worst-case performance  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage frames robustness as stability of performance or behavior under changes in prompts, inputs, examples, settings, or environments, including prompt reformulations, in-context example choices, noisy or degraded inputs, typos, option position or symbol changes, distribution shift, adversarial perturbations, changing opponents or environments, and decoding or system-setting changes. Several quoted passages use the term for whether models remain effective under such perturbations, and some describe current systems as "highly brittle in the face of even minor perturbations." Smaller lines of work use robustness for retention of pre-learned capabilities after fine-tuning or editing, for stability of reasoning across similar problems and task conditions, or for worst-case performance on rare shifted inputs. The object whose robustness is discussed also varies across papers, spanning models, agents, jailbreak prompts, watermarks, backdoors, detectors, and evaluation metrics.

**Space of facets.** Papers break the construct into recurring variants such as prompt robustness, out-of-distribution robustness, adversarial robustness, safety or alignment robustness under jailbreaks or decoding changes, multimodal robustness to noisy inputs or typographic attacks, and watermark robustness to editing or spoofing. Some work explicitly treats out-of-distribution and adversarial robustness as separate, while other work places robustness within broader trustworthiness frameworks or discusses it alongside truthfulness, reliability, consistency, and generalization. Across uses, the same label covers both latent properties of model behavior and resilience of artifacts such as prompts, training procedures, evaluation protocols, and embedded watermarks.

**Space of measurement.** Papers link robustness to 33 measurement instruments and 13 behavioral indicators. The most frequently linked instruments are GSM-Hard, MMBench, SVAMP, A-OKVQA, and ALFRED, and the remaining 28 are mostly benchmarks and challenge datasets, with a smaller number of attack-based tests and one LLM-as-a-judge comparison. Operationally, papers usually measure accuracy or task success under controlled perturbations: MMBench uses answer shuffling, A-OKVQA introduces typos, GSM-Hard and SVAMP probe out-of-domain or minimally varied math problems, and ALFRED is used in embodied scenarios. These operationalizations mostly match the dominant stability-under-variation framing, though some papers instead operationalize robustness as retaining abilities after fine-tuning or editing, or as watermark detectability after text modification.

**Links.** Among the 33 construct links, the most recurrent are Generalization, In-context learning, Reasoning, Neural collapse, and Overfitting. Papers variously claim causal relationships from the first four to robustness, while overfitting is discussed as related, and one paper reports a correlation between neural collapse and robustness instead of a causal claim. Beyond these, other papers connect robustness to broader evaluation and safety-oriented constructs, claim causal links from bias-related or planning-related properties to robustness, and record a few outward causal claims from robustness to other constructs. The 13 behavioral-indicator links are sparser, with related links to attack-oriented behaviors and causal claims for some improvement behaviors.

## Sources

**Robustness** (86 papers: [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf), [AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f83cb637e159e789f5576ff6848874de-Paper-Conference.pdf), [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [Beam Enumeration: Probabilistic Explainability For Sample Efficient Self-conditioned Molecular Design](https://proceedings.iclr.cc/paper_files/paper/2024/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf), [Branch-GAN: Improving Text Generation with (not so) Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/02a92b52670752daf17b53f04f1ab405-Paper-Conference.pdf), [CLaM-TTS: Improving Neural Codec Language Model for Zero-Shot Text-to-Speech](https://proceedings.iclr.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf), [Can Large Language Models Infer Causation from Correlation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b75a7339dfb256ee4b4bec028a6890b-Paper-Conference.pdf), [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf), [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf), [Compositional Preference Models for Aligning LMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/8fd10360ac9de462ffd36155d87ee999-Paper-Conference.pdf), [Conformal Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf), [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf), [Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making](https://proceedings.iclr.cc/paper_files/paper/2024/file/fbf1b3765e081251c804da7f508f3b21-Paper-Conference.pdf), [Energy-based Automated Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5ef1df239d6640a27dd6ed9a59f518c9-Paper-Conference.pdf), [Evaluating Language Model Agency Through Negotiations](https://proceedings.iclr.cc/paper_files/paper/2024/file/03876dc6875571c18b3b09a624c77e96-Paper-Conference.pdf), [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf), [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf), [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf), [GeoLLM: Extracting Geospatial Knowledge from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a87f2df7c4ab0213c6ea228e7b7f0a4d-Paper-Conference.pdf), [Grounding Language Plans in Demonstrations Through Counterfactual Perturbations](https://proceedings.iclr.cc/paper_files/paper/2024/file/be62c4a943675195ff5a2a98d5b9724f-Paper-Conference.pdf), [Knowledge Fusion of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4fd5cfd2e31bebbccfa5ffa354c04bdc-Paper-Conference.pdf), [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf), [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf), [Learning with Language-Guided State Abstractions](https://proceedings.iclr.cc/paper_files/paper/2024/file/a84de7bd46172264d137b07ae7f00a8a-Paper-Conference.pdf), [MEND: Meta Demonstration Distillation for Efficient and Effective In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ce1cbededb4b0d6202847ac1b484ee8-Paper-Conference.pdf), [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf), [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf), [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf), [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf), [Provable Robust Watermarking for AI-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/beae9ed5316bcc48e616754c06c11875-Paper-Conference.pdf), [ReFusion: Improving Natural Language Understanding with Computation-Efficient Retrieval Representation Fusion](https://proceedings.iclr.cc/paper_files/paper/2024/file/67b0579a7298d9cf39c59404d867bdd7-Paper-Conference.pdf), [Reward Model Ensembles Help Mitigate Overoptimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda7f9378a210c25e470e19304cce85d-Paper-Conference.pdf), [Towards Robust Multi-Modal Reasoning via Model Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c78ae0c1140902bf3a430b1725bcc4e-Paper-Conference.pdf), [Towards Unified Multi-Modal Personalization: Large Vision-Language Models for Generative Recommendation and Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/297a7a54da76d95f02b04d957a53c7ba-Paper-Conference.pdf), [Training Socially Aligned Language Models on Simulated Social Interactions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d763b4a2dde0ae7b77498516ce9f439e-Paper-Conference.pdf), [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf), [Understanding In-Context Learning in Transformers and LLMs by Learning to Learn Discrete Functions](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7e7fabd73b3df96c54a320862afcb78-Paper-Conference.pdf), [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/4410c0711e9154a7a2d26f9b3816d1ef-Paper-Conference.pdf), [Zero-Shot Robustification of Zero-Shot Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/92ce40962b4098f7bf6eed33128fc606-Paper-Conference.pdf), [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf), [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/01a83bc2f2732a58e6aa731e659e7101-Paper-Conference.pdf), [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf), [Are Multimodal LLMs Robust Against Adversarial Perturbations? RoMMath: A Systematic Evaluation on Multimodal Math Reasoning](https://aclanthology.org/2025.naacl-long.582.pdf), [Arabic Dataset for LLM Safeguard Evaluation](https://aclanthology.org/2025.naacl-long.285.pdf), [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.444.pdf), [SANDWiCH: Semantical Analysis of Neighbours for Disambiguating Words in Context ad Hoc](https://aclanthology.org/2025.naacl-long.358.pdf), [SALAD: Improving Robustness and Generalization through Contrastive Learning with Structure-Aware and LLM-Driven Augmented Data](https://aclanthology.org/2025.naacl-long.634.pdf), [Beyond End-to-End VLMs: Leveraging Intermediate Text Representations for Superior Flowchart Understanding](https://aclanthology.org/2025.naacl-long.180.pdf), [GroundCocoa: A Benchmark for Evaluating Compositional & Conditional Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.420.pdf), [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf), [Knowledge Graph-Guided Retrieval Augmented Generation](https://aclanthology.org/2025.naacl-long.449.pdf), [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf), [Diversify-verify-adapt: Efficient and Robust Retrieval-Augmented Ambiguous Question Answering](https://aclanthology.org/2025.naacl-long.56.pdf), [Kill two birds with one stone: generalized and robust AI-generated text detection via dynamic perturbations](https://aclanthology.org/2025.naacl-long.446.pdf), [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf), [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf), [Guiding Medical Vision-Language Models with Diverse Visual Prompts: Framework Design and Comprehensive Exploration of Prompt Variations](https://aclanthology.org/2025.naacl-long.587.pdf), [SylloBio-NLI: Evaluating Large Language Models on Biomedical Syllogistic Reasoning](https://aclanthology.org/2025.naacl-long.371.pdf), [WaterPool: A Language Model Watermark Mitigating Trade-Offs among Imperceptibility, Efficacy and Robustness](https://aclanthology.org/2025.naacl-long.209.pdf), [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf), [IFIR: A Comprehensive Benchmark for Evaluating Instruction-Following in Expert-Domain Information Retrieval](https://aclanthology.org/2025.naacl-long.511.pdf), [Assessing the State of the Art in Scene Segmentation](https://aclanthology.org/2025.naacl-long.500.pdf), [Beyond the Next Token: Towards Prompt-Robust Zero-Shot Classification via Efficient Multi-Token Prediction](https://aclanthology.org/2025.naacl-long.363.pdf), [FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models](https://aclanthology.org/2025.naacl-long.534.pdf), [NLI under the Microscope: What Atomic Hypothesis Decomposition Reveals](https://aclanthology.org/2025.naacl-long.130.pdf), [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf), [B4: A Black-Box Scrubbing Attack on LLM Watermarks](https://aclanthology.org/2025.naacl-long.460.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf), [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.416.pdf), [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf), [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf), [Eliciting Critical Reasoning in Retrieval-Augmented Generation via Contrastive Explanations](https://aclanthology.org/2025.naacl-long.557.pdf), [MAPWise: Evaluating Vision-Language Models for Advanced Map Queries](https://aclanthology.org/2025.naacl-long.473.pdf), [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.320.pdf), [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf), [Typographic Attacks in a Multi-Image Setting](https://aclanthology.org/2025.naacl-long.626.pdf), [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.247.pdf), [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf), [Mutual-pairing Data Augmentation for Fewshot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.205.pdf), [ImgTrojan: Jailbreaking Vision-Language Models with ONE Image](https://aclanthology.org/2025.naacl-long.360.pdf), [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf), [Is your benchmark truly adversarial? AdvScore: Evaluating Human-Grounded Adversarialness](https://aclanthology.org/2025.naacl-long.27.pdf), [Option Symbol Matters: Investigating and Mitigating Multiple-Choice Option Symbol Bias of Large Language Models](https://aclanthology.org/2025.naacl-long.95.pdf), [Towards Robust and Efficient Federated Low-Rank Adaptation with Heterogeneous Clients](https://aclanthology.org/2025.acl-long.19.pdf), [Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?](https://aclanthology.org/2025.emnlp-main.7.pdf))
> The degree to which a model retains its pre-learned general capabilities, such as code generation and problem-solving, after fine-tuning on a specialized task like code editing.

**Model robustness** (1 paper: [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf))
> The stability of an LLM's reasoning performance across similar problems, tasks, or perturbations in task conditions.

**Worst-case performance** (1 paper: [Estimating the Probabilities of Rare Outputs in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdaac2a02c4fdcae77ba083b110efcc3-Paper-Conference.pdf))
> The extent to which a model avoids highly undesirable outputs on rare or adversarially shifted inputs rather than only performing well on average.

## Relationships

### Robustness →
- **GSM-Hard** (measurement instrument): *measured_by*, 2 papers
  > The drop in performance on GSM-Hard compared to GSM indicates that our models may not be robust to input perturbations, though, they are at par with previous work. (Limitations and Potential Risks)
  - [OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d5aa9a7ce28cdc710fbd044fd3610f3-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36.pdf)
- **MMBench** (measurement instrument): *measured_by*, 2 papers
  > MMBench and the CN version evaluate a model’s answer robustness with all-round shuffling on multiple choice answers. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **SVAMP** (measurement instrument): *measured_by*, 2 papers
  > SVAMP (Patel et al., 2021), a robustness evaluation benchmark. (Section 3.4)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36.pdf)
- **GAIA** (measurement instrument): *measured_by*, 1 paper
  > Static benchmarks are broken benchmarks in the making, and making GAIA evolve year-by-year through the removal of broken questions and the addition of new ones might be an important component to better assess the generalization and robustness of AI systems. (Section 5)
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **OSWorld** (measurement instrument): *measured_by*, 1 paper
  > We find that current agents are not robust to these superficial changes, which lead to performance drops of 60% and even 80%. (Section 5)
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Out-of-distribution generalization** (construct): *causes*, 1 paper
  > The emergent abilities of LLMs, especially in OOD scenarios, largely depends on the robustness of their representations (Section 3.4)
  - [Tri-Level Navigator: LLM-Empowered Tri-Level Learning for Time Series OOD Generalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78d9d035215039ab46e48c281e6a63d-Paper-Conference.pdf)
- **MMBench-CN** (measurement instrument): *measured_by*, 1 paper
  > MMBench and the CN version evaluate a model’s answer robustness with all-round shuffling on multiple choice answers. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **A-OKVQA** (measurement instrument): *measured_by*, 1 paper
  > We introduce typos into A-OKVQA [34] and VQAv2 [12] to test the robustness against text perturbations. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 1 paper
  > We introduce typos into A-OKVQA [34] and VQAv2 [12] to test the robustness against text perturbations. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VirtualHome** (measurement instrument): *measured_by*, 1 paper
  > Finally, we demonstrate superior performance and robustness of ExRAP via intensive experiments with home robots and autonomous driving scenarios in VirtualHome, ALFRED, and CARLA. (Introduction)
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **ALFRED** (measurement instrument): *measured_by*, 1 paper
  > Finally, we demonstrate superior performance and robustness of ExRAP via intensive experiments with home robots and autonomous driving scenarios in VirtualHome, ALFRED, and CARLA. (Introduction)
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > Kangaroo shows consistent high performance across different tasks such as QA, Math, and MT Bench, indicating its robustness and versatility. (Section 5.1)
  - [Kangaroo: Lossless Self-Speculative Decoding for Accelerating LLMs via Double Early Exiting](https://proceedings.neurips.cc/paper_files/paper/2024/file/16336d94a5ffca8de019087ab7fe403f-Paper-Conference.pdf)
- **MS MARCO** (measurement instrument): *measured_by*, 1 paper
  > “To evaluate the model’s robustness in non-Wikipedia scenarios where high-quality text and titles are not available, we conduct experiments on a subset of MS MARCO”
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Needle-in-a-Haystack** (measurement instrument): *measured_by*, 1 paper
  > We design a needle-in-the-haystack experiment which allows us to ... evaluate its robustness w.r.t. the position of the relevant information in the input context. (Section 4.3)
  - [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf)
- **AndroidWorld** (measurement instrument): *measured_by*, 1 paper
  > To understand agent robustness, we analyze M3A’s performance across different random seeds, which generate different task parameters... (Section 5)
  - [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/01a83bc2f2732a58e6aa731e659e7101-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > GPT-4 comparison for robustness (Figure 5 caption).
  - [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf)
- **FLAN** (measurement instrument): *measured_by*, 1 paper
  > To demonstrate the generalizability and robustness of our method, we include FLAN (Chung et al., 2024) (a mix of multiple NLP tasks) as reference datasets .
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 1 paper
  > To assess robustness, we tested on the generalized dataset LLaVA-Bench. (Section 4)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **GSM-Plus** (measurement instrument): *measured_by*, 1 paper
  > GSM-Plus, which tests model robustness. (Section 4.4)
  - [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **AudioBench** (measurement instrument): *measured_by*, 1 paper
  > Consequently, to minimize variability and thoroughly test model robustness, we incorporate at least 20 diverse prompt templates into our evaluation framework for the tasks without diverse prompts originally.
  - [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > We create noised versions of HellaSwag and find that BLT outperforms in terms of robustness the Llama 3 BPE model by a large margin (Table 2).
  - [Byte Latent Transformer: Patches Scale Better Than Tokens](https://aclanthology.org/2025.acl-long.453.pdf)
- **GrailQA** (measurement instrument): *measured_by*, 1 paper
  > Figure 4: Performance under attack setting on 1,000 randomly sampled GrailQA questions. (Figure 4)
  - [TARGA: Targeted Synthetic Data Generation for Practical Reasoning over Structured Data](https://aclanthology.org/2025.acl-long.137.pdf)
- **VoxEval** (measurement instrument): *measured_by*, 1 paper
  > Our benchmark ... 2) evaluates model robustness across diverse input audio conditions (Abstract)
  - [VoxEval: Benchmarking the Knowledge Understanding Capabilities of End-to-End Spoken Language Models](https://aclanthology.org/2025.acl-long.818.pdf)
- **MMLU-Redux** (measurement instrument): *measured_by*, 1 paper
  > To assess the robustness of QuaSAR as an ICL strategy, we evaluated two different phenomena: (i) the order swapping of choices in MMLU-Redux... (Section 4.4)
  - [Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions](https://aclanthology.org/2025.acl-long.843.pdf)
- **Copy-paste attack** (measurement instrument): *measured_by*, 1 paper
  > We assess the robustness of different watermarking methods under various attacks, including the copy-paste attack (Kirchenbauer et al., 2023a), paraphrasing using GPT-3.5, and two configurations of the DIPPER attack (Krishna et al., 2024). (Section 4.4)
  - [Watermarking Large Language Models: An Unbiased and Low-risk Method](https://aclanthology.org/2025.acl-long.391.pdf)
- **SQuAD2.0-Eval** (measurement instrument): *measured_by*, 1 paper
  > Following Li et al. (2023a), we further simulate complex retrieval scenarios using annotation information from SQuAD2.0 to more effectively evaluate the adherence and robustness of RALMs, resulting in the creation of SQuAD2.0-Eval. (Section 5.1)
  - [Parenting: Optimizing Knowledge Selection of Retrieval-Augmented Language Models with Parameter Decoupling and Tailored Tuning](https://aclanthology.org/2025.acl-long.571.pdf)
- **RM-Bench** (measurement instrument): *measured_by*, 1 paper
  > RM-Bench is designed to assess the robustness of reward models, based on their sensitivity and resistance to subtle content differences and style biases. (Section 3)
  - [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > The evaluation on MMLU shows the generalizability and robustness of our framework. (Abstract)
  - [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chiang25a/chiang25a.pdf)
- **PWWS** (measurement instrument): *measured_by*, 1 paper
  > We report the clean accuracy (CA) and the robust accuracy under attack (AUA) with PWWS (PW), TextFooler (TF), and Bert-Attack (BA) (Table 1)
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > we compare the plain BT model and BSR on RLHF training and empirically show that robust RMs better align the policy to the gold preference model. (Abstract).
  - [On the Robustness of Reward Models for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25d/hong25d.pdf)
- **GCG** (measurement instrument): *measured_by*, 1 paper
  > "robustness is assessed via failure rates against the GCG attack"
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)
- **MultiArith** (measurement instrument): *measured_by*, 1 paper
  > For mathematical reasoning, we assess model robustness on three out-of-domain (OOD) benchmarks: ... and (3) MultiArith (Section 4.1).
  - [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36.pdf)
- **FINTRUST** (measurement instrument): *measured_by*, 1 paper
  > we curate 15, 680 instances to evaluate LLM trustworthiness in the financial domain. We ... incorporate seven core dimensions: Truthfulness, Safety, Fairness, Robustness, Privacy, Transparency, and Knowledge Discovery. (Section 2)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **Evol-Instruct** (measurement instrument): *measured_by*, 1 paper
  > When robustness against fine-tuning attacks is evaluated by fine-tuning the watermarked StarCoder2-7B on the code generation dataset Evol-Instruct, the watermark persistence rate improves from 0% to 90% due to adversarial training and the parameter selection algorithm sensitive to the robust watermark. (Introduction)
  - [CLMTracing: Black-box User-level Watermarking for Code Language Model Tracing](https://aclanthology.org/2025.emnlp-main.1475.pdf)
- **ShareGPT** (measurement instrument): *measured_by*, 1 paper
  > This section assesses the robustness of CLMTracing against fine-tuning, wherein the model is fine-tuned on two clean datasets, ShareGPT and Evol-Instruct, with the goal of overwriting embedded watermarks. (Section 4.2.2)
  - [CLMTracing: Black-box User-level Watermarking for Code Language Model Tracing](https://aclanthology.org/2025.emnlp-main.1475.pdf)

### → Robustness
- **Generalization** (construct): *causes*, 4 papers
  > We attribute our outstanding robustness to the great generalization ability of our distilled thought-templates
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)
  - [ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25at/chen25at.pdf)
- **Reasoning** (construct): *causes*, 3 papers
  > A recent advancement in enhancing robustness is ICL with explanations (X-ICL), which improves prediction reliability by guiding LLMs to understand and articulate the reasoning behind correct labels. (Abstract)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
  - [MR. Judge: Multimodal Reasoner as a Judge](https://aclanthology.org/2025.emnlp-main.1021.pdf)
- **In-context learning** (construct): *causes*, 3 papers
  > we believe that utilizing few-shot settings with example demonstrations could potentially enhance model performance and robustness. (Section 5.1)
  - [Are Multimodal LLMs Robust Against Adversarial Perturbations? RoMMath: A Systematic Evaluation on Multimodal Math Reasoning](https://aclanthology.org/2025.naacl-long.582.pdf)
  - [Iterative Vectors: In-Context Gradient Steering without Backpropagation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25j/liu25j.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **Neural collapse** (construct): *causes*, 2 papers
  > In this paper, we are the first to apply neural collapse to address the long-tail problem in data-based personalized learning and improve the robustness of large language models during LoRA fine-tuning in personalized learning scenarios. (Section 2)
  - [Advancing Personalized Learning with Neural Collapse for Long-Tail Challenge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25f/hu25f.pdf)
  - [Linguistic Collapse: Neural Collapse in (Large) Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f88cc8930b47a45ec4733123bf3039b9-Paper-Conference.pdf)
- **Planning** (construct): *causes*, 1 paper
  > Additional experiments on other benchmarks like RM-Bench, JudgeBench, and FollowBenchEval further highlight the utility of both planning and reasoning for building robust LLM-as-a-Judge reasoning models. (Abstract)
  - [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf)
- **Selection bias** (construct): *causes*, 1 paper
  > LLMs’ poor robustness to option position changes results from their biased behavior: they prefer to select speciﬁc option IDs as answers (like “Option A”), which we term as selection bias.
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **Disentanglement** (construct): *causes*, 1 paper
  > “DRL is a major goal of artificial intelligence (AI), acclaimed for its enhancement of model robustness, interpretability, and generalizability.”
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **Recency bias** (construct): *causes*, 1 paper
  > Furthermore, we raise a novel robustness concern regarding SSMs with recency bias: our empirical outcomes show that Mamba is more susceptible to perturbations on local tokens, making it vulnerable to adversarial attack, as these local tokens can be easily manipulated to serve as backdoors. (Section 1)
  - [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > Our analysis shows that self-refinement enables the robustness of agent capability and the diversity of agent environments and thoughts further enhances the performance. (Section 11)
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
- **Positional bias** (construct): *causes*, 1 paper
  > "This bias often leads to unexpected model failures and hurts performance, robustness, and reliability across various applications."
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Causal reasoning** (construct): *causes*, 1 paper
  > A better approximation of the underlying causal model generally translates to more robust agents, implying that world models should be causality-aware
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **Epistemic uncertainty** (construct): *causes*, 1 paper
  > Overall, we find that the uncertainty-aware variant of MBR proposed in this paper leads to better and more robust language generation. (Section 5)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Shortcut learning** (construct): *causes*, 1 paper
  > This association can create a spurious correlation between the filmmaker’s names and sentiment, leading LMs to learn shortcuts that can undermine their robustness. (Section 3.1)
  - [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.416.pdf)
- **Task alignment** (construct): *causes*, 1 paper
  > Our approach, instead, aims to enforce the task alignment, achieving a better robustness-utility tradeoff. (Section 6)
  - [The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents](https://aclanthology.org/2025.acl-long.1435.pdf)
- **Collective intelligence** (construct): *causes*, 1 paper
  > By doing so, DebateCoder effectively leverages the collective intelligence of both models, making the generated code more robust and accurate. (Section 1)
  - [DebateCoder: Towards Collective Intelligence of LLMs via Test Case Driven LLM Debate for Code Generation](https://aclanthology.org/2025.acl-long.589.pdf)
- **Divergent thinking** (construct): *causes*, 1 paper
  > This divergent reasoning is also crucial for machines, enhancing their robustness and enabling them to assist humans in many applications such as scientific discovery. (Abstract)
  - [Flow of Reasoning: Training LLMs for Divergent Reasoning with Minimal Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25k/yu25k.pdf)
- **Multimodal reasoning** (construct): *causes*, 1 paper
  > MVoT demonstrates comparable performance on MAZE (92.95%) and MINIBEHAVIOR (95.14%), while achieving a higher accuracy of 85.60% on FROZENLAKE compared to both Direct and CoT. This demonstrates better stability and robustness of MVoT than CoT.
  - [Imagine While Reasoning in Space: Multimodal Visualization-of-Thought](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cz/li25cz.pdf)
- **Code editing** (behavioral indicator): *causes*, 1 paper
  > With explicit editing rules, EDITLORD significantly improved the baseline in generalization, e.g., by up to 24.87% improvement in length generalization and 58.1% improved robustness against semantics-preserving code transformations. (Section 1)
  - [EditLord: Learning Code Transformation Rules for Code Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25al/li25al.pdf)
- **Critique generation** (behavioral indicator): *causes*, 1 paper
  > This mechanism enhances the model’s robustness in complex and uncertain environments and fosters a dynamic learning phase, facilitating continuous improvement through error identification and rectification. (Section 3.4.1)
  - [CARE: A Disagreement Detection Framework with Concept Alignment and Reasoning Enhancement](https://aclanthology.org/2025.emnlp-main.671.pdf)
- **Backtracking** (behavioral indicator): *causes*, 1 paper
  > Our method’s ability to backtrack helps resolve contradictions, leading to more stable performance in multi-hop scenarios. (Section 5.2)
  - [ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA](https://aclanthology.org/2025.emnlp-main.202.pdf)
- **Counterfactual reasoning** (construct): *causes*, 1 paper
  > we propose DPCI, a novel Dual-Path Counterfactual Integration framework that enhances model robustness by explicitly modeling counterfactual reasoning in multimodal contexts. (Abstract)
  - [Dual-Path Counterfactual Integration for Multimodal Aspect-Based Sentiment Classification](https://aclanthology.org/2025.emnlp-main.1158.pdf)

### Associated with
- **Overfitting** (construct), 2 papers
  > In contrast, mixed-domain models exhibit greater resistance to overfitting, suggesting potential improvements in domain-specific model robustness; (ABSTRACT)
  - [Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making](https://proceedings.iclr.cc/paper_files/paper/2024/file/fbf1b3765e081251c804da7f508f3b21-Paper-Conference.pdf)
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **Trustworthiness** (construct), 2 papers
  > We assess the trustworthiness of Med-LVLMs across five dimensions, including trustfulness, fairness, safety, privacy, and robustness. (Abstract)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Knowledge transfer** (construct), 1 paper
  > In this subsection, we aim to evaluate the robustness, especially the generalizability and transferability of our method MoD to various LLMs. (Section 4.5)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **Safety** (construct), 1 paper
  > We assert that robustness is fundamentally insufficient for ensuring safety goals due to inferential threats from dual-intent queries, with current defenses and evaluations failing to account for these risks. (Section 1)
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **Adversarial robustness** (construct), 1 paper
  > Following the common practice in the field [132, 147], we consider the out-of-distribution (OOD) and adversarial robustness respectively. (Sec. 2.2.3)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **System 2 thinking** (construct), 1 paper
  > A truly intelligent system should exhibit System 2 thinking [Kahneman, 2011], which implies performing tasks consistently regardless of incidental features. (Section 1)
  - [SETLEXSEM CHALLENGE: Using Set Operations to Evaluate the Lexical and Semantic Robustness of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a12909ffd7145c41139ad66ecf20fc0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Truthfulness** (construct), 1 paper
  > Truthfulness involves a dual consideration of hallucination and robustness. (Section 2.1)
  - [MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d9dcd4ebef57f1839d871fe7d891e91-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Stock movement prediction** (behavioral indicator), 1 paper
  > “CausalStock outperforms all baselines on ACC as well as MCC across three datasets demonstrating robustness performance for news-driven multi-stock movement prediction task.”
  - [CausalStock: Deep End-to-end Causal Discovery for News-driven Multi-stock Movement Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/54d689d58fe54c92aee2d732fc49fca8-Paper-Conference.pdf)
- **Personalization** (construct), 1 paper
  > the diversity of names used during training makes the personalization capability more robust and generalizable to new individuals. (Section 6.2.3 IMPACT OF DATA SCALE AND NAME REPETITION)
  - [Personalized Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b69dcf999ee89f48d08c6c9881a4c0d-Paper-Conference.pdf)
- **Multi-turn dialogue** (behavioral indicator), 1 paper
  > Our MTU-LLaMA exhibits the most gradual decrease in performance, demonstrating its robustness to higher dialogue turns. (Section 3.2)
  - [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf)
- **Generation diversity** (construct), 1 paper
  > We posit that a model’s capacity to produce diverse solutions is indicative of its robustness and flexibility in problem-solving. (Section 5.2)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Consistency** (construct), 1 paper
  > Our hope is that sensitivity and consistency will be helpful to guide prompt engineering and obtain LLMs that balance robustness with performance. (Abstract)
  - [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Fact checking** (behavioral indicator), 1 paper
  > fact verification is one area in which assessing the robustness of models developed for this task is crucial. (Section 1)
  - [FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models](https://aclanthology.org/2025.naacl-long.534.pdf)
- **In-context classification** (behavioral indicator), 1 paper
  > in the ‘different norms’ setting, the performance of ‘1-layer’ deteriorates more significantly, while transformers with a more complex structure (’3-layer’) show better robustness under this distribution shift.
  - [On the Training Convergence of Transformers for In-Context Classification of Gaussian Mixtures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25q/shen25q.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > We... demonstrate robustness by showing retention of code generation and general problem-solving abilities post adaptation. (Section 1)
  - [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)
- **Watermark spoofing** (behavioral indicator), 1 paper
  > Following the settings in (Jovanovi´c et al., 2024), we compare the robustness against watermark spoofing attack by setting up LMmo as LLAMA2-7B and LMatt as MISTRAL-7B (Jiang et al., 2023).
  - [StealthInk: A Multi-bit and Stealthy Watermark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25j/jiang25j.pdf)
- **Compositional generalization** (construct), 1 paper
  > our approach considers the interaction between multiple problems, focusing more on the compositional generalization (Xu and Wang, 2024; An et al., 2023; Li et al., 2021) in robustness. (Section 1)
  - [From A and B to A+B: Can Large Language Models Solve Compositional Math Problems?](https://aclanthology.org/2025.emnlp-main.660.pdf)
- **Error propagation** (construct), 1 paper
  > This robustness arises from our balanced topology design, which mitigates error propagation through bottleneck structures while promoting rapid consensus via densely connected reliable agents.
  - [Understanding the Information Propagation Effects of Communication Topologies in LLM-based Multi-Agent Systems](https://aclanthology.org/2025.emnlp-main.623.pdf)
- **Fine-grained visual reasoning** (construct), 1 paper
  > This work offers new insights into the limitations of LVLMs in MCQA and presents a practical approach to improve their robustness in fine-grained visual reasoning. (Abstract)
  - [Benchmarking and Mitigating MCQA Selection Bias of Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1703.pdf)
- **Internal consistency** (construct), 1 paper
  > By linking layer consistency to robustness, CROW provides practical and effective protection against backdoor threats. (Section 1)
  - [CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/min25b/min25b.pdf)
- **Voice cloning** (behavioral indicator), 1 paper
  > In zero-shot speech generation, DiTAR achieves state-of-the-art performance in robustness, speaker similarity, and naturalness.
  - [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25a/jia25a.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > “We systematically compare three widely used value probing methods: token likelihood, sequence perplexity, and text generation. Our results show that all three methods exhibit large variances under non-semantic perturbations” (Abstract).
  - [Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?](https://aclanthology.org/2025.emnlp-main.7.pdf)
- **Adversarial attacks** (behavioral indicator), 1 paper
  > This raises the need to assess the robustness of such solutions, i.e. their ability to deliver correct result even for input manipulated by malicious actors. This is performed by seeking adversarial examples (AEs) (Section 1).
  - [Attacking Misinformation Detection Using Adversarial Examples Generated by Language Models](https://aclanthology.org/2025.emnlp-main.1405.pdf)
