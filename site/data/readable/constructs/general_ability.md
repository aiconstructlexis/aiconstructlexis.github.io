# General ability
**Type:** Construct  
**Supporting papers:** 149  
**Also known as:** General capabilities, Downstream Performance, Downstream performance, General abilities, General capability, General performance, Generic performance, Model Capability, Model capability, Model performance, General purpose performance, General-purpose ability, General-purpose capabilities, Model utility, Model Utility, Model competence, Effectiveness, General task performance, Downstream benchmark performance, Foundational capabilities, LLM capability, Benign capabilities, Generalist abilities, General problem-solving, Capability, General model utility, Utility, Skill, Ability, Latent abilities, General language model capability, General model capability, Capabilities set, Capabilities, All-round capability, Intrinsic capacity, Policy performance, Relative performance, Benign utility, Competence, Model usefulness, Downstream task performance, General utility, General task-solving ability, Predictive quality, Model quality, Task solving ability, Performance  

## State of the Field

**Space of definitions.** Most commonly, papers treat general ability as broad model competence across many tasks, domains, or benchmarks, rather than performance on a narrow target task. In this prevailing usage it is the overall proficiency, knowledge, reasoning, question answering, summarization, instruction following, or general-purpose usefulness that papers want to preserve when editing, fine-tuning, unlearning, steering, safeguarding, or compressing a model. A smaller line of work makes the construct more explicitly latent, describing an unobservable ability inferred from scores, sometimes as a unidimensional trait, a capabilities set, or a first-order factor over benchmarks. Another minority usage narrows it to retained or benign performance after intervention, and one paper uses "general abilities" for newly enhanced high-level abilities such as reasoning, coding, and instruction following rather than only pre-existing competence.

**Space of facets.** Papers use several near-overlapping names for this construct, including general capabilities, model capability, model utility, downstream performance, and foundational capabilities, usually for the same broad competence. The facets named most often are reasoning and knowledge, with some papers also invoking comprehension, common sense, dialogue, coding, or multimodal task competence; one paper states that "PC-1 represents the general capability as a weighted average of all metrics," while others model a single latent ability, a capabilities set over tasks, or localizable capability neurons. The main boundary is between broad transferable competence and specialized behaviors, since papers regularly contrast it with narrow edited facts, domain-specific fine-tuning targets, or safety and refusal behavior, and one paper further separates it from composability.

**Space of measurement.** Operationalization is dominated by benchmarking: papers link general ability to 62 measurement instruments, with MMLU used most often, followed by GSM8K, HellaSwag, MT-Bench, and BIG-Bench Hard, plus 57 other instruments. These are mainly benchmarks or benchmark suites, and papers operationalize the construct through accuracy, win rate, or perplexity on general multiple-choice, reasoning, math, chat, coding, long-context, and multimodal tasks, with a smaller number using comparative evaluation frameworks, harness-style analyses, or aggregated retain-set performance. This mostly matches the broad cross-task definitions, although some papers rely on a single proxy such as MMLU alone, or on retained-data and unrelated-question aggregates after editing or unlearning. Papers also connect it to 3 behavioral indicators.

**Links.** Link claims are much sparser than measurement. One paper claims a causal relationship from catastrophic forgetting to general ability, and other papers discuss the pair as related, typically as loss of broad capability after fine-tuning; one paper also claims a causal relationship from general ability to adversarial robustness, with the evidence phrased as "emergent model vulnerabilities." Other isolated causal claims also point into general ability. Related links are more scattered: papers relate general ability to reasoning, safety alignment, composability, and 8 other constructs or indicators.

## Sources

**General capabilities** (5 papers: [Private Attribute Inference from Images with Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb97e9a7c811904c9b01f51fde66edcf-Paper-Conference.pdf), [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf), [Towards Effective and Efficient Continual Pre-training of Large Language Models](https://aclanthology.org/2025.acl-long.289.pdf), [Activation Space Interventions Can Be Transferred Between Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oozeer25a/oozeer25a.pdf), [Continuously Steering LLMs Sensitivity to Contextual Knowledge with Proxy Models](https://aclanthology.org/2025.emnlp-main.233.pdf))
> A model's overall proficiency and performance across a wide range of tasks, which is shown to correlate with its performance on specific, potentially harmful tasks like private attribute inference.

**General ability** (1 paper: [Everything is Editable: Extend Knowledge Editing to Unstructured Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/02763667a5761ff92bb15d8751bcd223-Paper-Conference.pdf))
> The model's broader performance on unrelated tasks or knowledge after editing, reflecting whether edits degrade overall capability.

**General capability** (3 papers: [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf), [YuLan-Mini: Pushing the Limits of Open Data-efficient Language Model](https://aclanthology.org/2025.acl-long.268.pdf), [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf))
> The model's overall performance on a wide range of standard, non-adversarial tasks, such as question answering and instruction following.

**Generic performance** (1 paper: [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf))
> The overall downstream effectiveness of a pre-trained LLM across diverse evaluation tasks rather than a single target domain.

**General abilities** (2 papers: [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf), [HFT: Half Fine-Tuning for Large Language Models](https://aclanthology.org/2025.acl-long.626.pdf))
> The broad set of capabilities of a large language model, such as reasoning and summarization, that are not directly targeted by a specific model edit but can be negatively affected by it.

**General performance** (1 paper: [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf))
> The overall capability of a model across a wide range of tasks and domains, as opposed to performance on a specific, narrow task.

**General-purpose capabilities** (1 paper: [Diverse Preference Learning for Capabilities and Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf))
> Broad task competence of an LLM across heterogeneous chat and reasoning tasks rather than a single narrow domain.

**Downstream Performance** (1 paper: [Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf))
> The latent capability of the model to successfully complete tasks, inferred from accuracy or scores on benchmarks.

**Downstream performance** (1 paper: [RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf))
> The overall capability of a pre-trained model to perform effectively on a wide range of evaluation tasks it was not explicitly trained on.

**Model utility** (7 papers: [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf), [The Jailbreak Tax: How Useful are Your Jailbreak Outputs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nikolic25a/nikolic25a.pdf), [Balancing Forget Quality and Model Utility: A Reverse KL-Divergence Knowledge Distillation Approach for Better Unlearning in LLMs](https://aclanthology.org/2025.naacl-long.60.pdf), [Protecting Privacy in Multimodal Large Language Models with MLLMU-Bench](https://aclanthology.org/2025.naacl-long.207.pdf), [SafeQuant: LLM Safety Analysis via Quantized Gradient Inspection](https://aclanthology.org/2025.naacl-long.127.pdf), [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.415.pdf), [Unlearning as multi-task optimization: A normalized gradient difference approach with an adaptive learning rate](https://aclanthology.org/2025.naacl-long.563.pdf))
> The overall performance and general knowledge of a model on tasks and data that are unaffected by the unlearning process.

**Model Capability** (1 paper: [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf))
> The general ability of the model to perform desired tasks, such as language modeling or question answering, without degradation.

**Model capability** (1 paper: [Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf))
> The overall level of a model's general cognitive abilities, such as reasoning and knowledge, which often correlates with its scale and performance on standard benchmarks.

**General-purpose ability** (1 paper: [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf))
> A model's broad capability across a wide range of tasks and domains, as opposed to specialized performance on a narrow domain.

**Model Utility** (1 paper: [Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf))
> The latent general capability of a model to perform diverse tasks effectively without degradation from interventions.

**Model performance** (2 papers: [Determine-Then-Ensemble: Necessity of Top-k Union for Large Language Model Ensembling](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbb10d319d44f8c3b4720873e4177c65-Paper-Conference.pdf), [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf))
> The overall effectiveness of a model on a given set of tasks, which is a key determinant for successful ensembling.

**General purpose performance** (1 paper: [Scaling Long Context Training Data by Long-Distance Referrals](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbf49f35b6dd2bef1ad12768c0509daa-Paper-Conference.pdf))
> The overall capability of a model across a wide range of domains and tasks, as opposed to specialized performance in a narrow domain.

**General task performance** (1 paper: [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf))
> The overall capability of the model to perform standard NLP tasks without regression when optimized for specific constraints like long context.

**Effectiveness** (1 paper: [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf))
> The overall quality or performance of the model in achieving its objectives, as measured by accuracy on evaluation benchmarks, distinct from its computational cost.

**Model competence** (1 paper: [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf))
> The overall capability and effectiveness of a language model that results from its pretraining regimen, which is crucially impacted by data mixture proportions.

**Downstream benchmark performance** (1 paper: [Improving Pretraining Data Using Perplexity Correlations](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c625366ae28066fcb1827b44517d674-Paper-Conference.pdf))
> The latent capability of a language model that enables it to score highly on a diverse set of evaluation benchmarks.

**LLM capability** (1 paper: [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf))
> The overall latent ability level of a language model across evaluation tasks, inferred from how well it performs and is ranked relative to other models.

**Foundational capabilities** (1 paper: [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf))
> The general, pre-existing knowledge and skills of a large language model, which are evaluated to ensure they are not degraded by specialized fine-tuning.

**General problem-solving** (1 paper: [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf))
> A broad capability to handle a variety of tasks and input formats, acquired through training on a diverse multi-task dataset.

**Generalist abilities** (1 paper: [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf))
> The model's capacity to perform well across a wide and diverse range of tasks and domains without task-specific fine-tuning.

**Benign capabilities** (1 paper: [Tamper-Resistant Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc49a629d33bc2461ed7a715ce44da68-Paper-Conference.pdf))
> The extent to which a safeguarded model retains general-purpose performance on non-target tasks after safety training and tampering.

**Capability** (2 papers: [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf), [Adversaries Can Misuse Combinations of Safe Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jones25a/jones25a.pdf))
> A general, transferable ability of a model, reflected as a commonality across a dataset, that can be localized to a specific set of neurons and enhances performance on related tasks.

**General model utility** (1 paper: [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf))
> The model's broad task performance across general-purpose evaluations, used here as an overall indicator of whether interventions preserve usefulness.

**Utility** (3 papers: [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf), [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf), [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf))
> The overall quality and usefulness of the model's generated output for a given task, considered as a trade-off against safety measures.

**Skill** (1 paper: [Unearthing Skill-level Insights for Understanding Trade-offs of Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5526c73e3ff4f2a34009e13d15f52fcb-Paper-Conference.pdf))
> A latent underlying competency that a model must apply to solve an evaluation instance, often spanning multiple benchmarks and surfacing only through solution steps.

**General language model capability** (1 paper: [Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf))
> The overall proficiency of a model across a wide range of standard language understanding and generation benchmarks.

**General model capability** (1 paper: [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf))
> The overall performance and competence of a model across a wide range of standard tasks, distinct from its specialized safety behaviors.

**Competence** (1 paper: [MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gaven25a/gaven25a.pdf))
> The underlying ability of an agent to successfully achieve a given goal, often operationalized as the probability of success.

**Latent abilities** (1 paper: [MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mencattini25a/mencattini25a.pdf))
> The underlying, unobservable capabilities of a model, such as problem-solving or linguistic skills, which are estimated using statistical methods rather than being directly measured.

**Ability** (1 paper: [Reliable and Efficient Amortized Model-based Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25c/truong25c.pdf))
> The unobservable, unidimensional latent trait of a language model that determines its probability of correctly answering a question, independent of the question's difficulty.

**Capabilities set** (1 paper: [Position: Scaling LLM Agents Requires Asymptotic Analysis with LLM Primitives](https://raw.githubusercontent.com/mlresearch/v267/main/assets/meyerson25a/meyerson25a.pdf))
> The latent trait representing the scope of tasks an LLM can reliably perform, which determines its suitability for specific agent roles within a system.

**Capabilities** (1 paper: [A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf))
> The general ability of a model to perform tasks correctly and generate high-quality, useful, and coherent information.

**All-round capability** (1 paper: [MemoryFormer : Minimize Transformer Computation by Removing Fully-Connected Layers](https://proceedings.neurips.cc/paper_files/paper/2024/file/24143e25a82f856aeed58b2f497d623b-Paper-Conference.pdf))
> Broad general task competence across diverse benchmark types, including knowledge and reasoning tasks.

**Intrinsic capacity** (1 paper: [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf))
> The underlying, general-purpose capabilities of a base model, independent of specific fine-tuning or prompting techniques, which influences its performance on downstream tasks.

**Relative performance** (1 paper: [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf))
> A model's capability or quality assessed through direct comparison with other models, rather than against an absolute standard.

**Policy performance** (1 paper: [Free Process Rewards without Process Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25c/yuan25c.pdf))
> The ability of the model to directly solve downstream tasks when used as a policy model rather than as a reward model.

**Benign utility** (1 paper: [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf))
> The model's ability to maintain its performance and helpfulness on legitimate, non-malicious tasks and prompts.

**Model usefulness** (1 paper: [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.444.pdf))
> The latent capacity of a model to maintain general language understanding and generation quality during and after unlearning procedures.

**Downstream task performance** (1 paper: [Self-calibration for Language Model Quantization and Pruning](https://aclanthology.org/2025.naacl-long.509.pdf))
> The ability of a language model to maintain its effectiveness on a range of evaluation tasks after undergoing compression techniques like quantization or pruning.

**General utility** (1 paper: [SudoLM: Learning Access Control of Parametric Knowledge with Authorization Alignment](https://aclanthology.org/2025.acl-long.1318.pdf))
> The model's ability to maintain high performance on general tasks and benchmarks regardless of the presence or activation of the SUDO key.

**General task-solving ability** (1 paper: [An Empirical Study of Many-to-Many Summarization with Large Language Models](https://aclanthology.org/2025.acl-long.555.pdf))
> The model's preserved competence across diverse domains and tasks beyond the specific one it has been fine-tuned on, reflecting robustness and transferability.

**Predictive quality** (1 paper: [STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf))
> The latent tendency of a language model to produce better next-token predictions and downstream task performance across evaluation settings.

**Model quality** (2 papers: [AMQ: Enabling AutoML for Mixed-precision Weight-Only Quantization of Large Language Models](https://aclanthology.org/2025.emnlp-main.1799.pdf), [SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3504a4fa45685d668ce92797fbbf1895-Paper-Conference.pdf))
> The overall performance and effectiveness of a language model, inferred from its accuracy on various downstream tasks and its ability to maintain the output distribution of the original, unquantized model.

**Task solving ability** (1 paper: [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf))
> The general capacity of a large language model to successfully complete a wide range of instructed tasks.

**Performance** (1 paper: [Quantifying Language Disparities in Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.199.pdf))
> The abstract capability of a language model on a given task, which is measured and represented by numerical scores.

## Relationships

### General ability →
- **MMLU** (measurement instrument): *measured_by*, 40 papers
  > General Ability (Gen): We use MMLU [20], which consists of multiple-choice questions from various branches of knowledge. (Section 3.3.2)
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
  - [Evaluating Copyright Takedown Methods for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/faed4276b52ef762879db4142655c699-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Understanding and Enhancing Safety Mechanisms of LLMs via Safety-Specific Neuron](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d2666e2cf44088cc57204fbc5ef7f34-Paper-Conference.pdf)
  - [Mix-CPT: A Domain Adaptation Framework via Decoupling Knowledge Learning and Format Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc721384c26c0bdff3ec31a7de31d8d5-Paper-Conference.pdf)
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
  - [A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
  - [Everything is Editable: Extend Knowledge Editing to Unstructured Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/02763667a5761ff92bb15d8751bcd223-Paper-Conference.pdf)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Tamper-Resistant Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc49a629d33bc2461ed7a715ce44da68-Paper-Conference.pdf)
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf)
  - [Catastrophic Failure of LLM Unlearning via Quantization](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba79fb5c4fe70050752f20c90c5f07ca-Paper-Conference.pdf)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf)
  - [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf)
  - [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf)
  - [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
  - [SLIM: Let LLM Learn More and Forget Less with Soft LoRA and Identity Mixture](https://aclanthology.org/2025.naacl-long.246.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
  - [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.308.pdf)
  - [An Empirical Study of Many-to-Many Summarization with Large Language Models](https://aclanthology.org/2025.acl-long.555.pdf)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
  - [Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf)
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
  - [OBLIVIATE: Robust and Practical Machine Unlearning for Large Language Models](https://aclanthology.org/2025.emnlp-main.183.pdf)
  - [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf)
  - [Continuously Steering LLMs Sensitivity to Contextual Knowledge with Proxy Models](https://aclanthology.org/2025.emnlp-main.233.pdf)
  - [MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.1080.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 11 papers
  > We evaluated the general capabilities of the models on benchmarks related to general-domain chat (MT-Bench [83] and Alpaca-Eval [37]), general MCQs (MMLU [34] and GPQA [54]), and mathematical tasks (MATH [22] and GSM8k [12]). (Section 4.1)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
  - [Understanding and Enhancing Safety Mechanisms of LLMs via Safety-Specific Neuron](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d2666e2cf44088cc57204fbc5ef7f34-Paper-Conference.pdf)
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
  - [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
  - [SLIM: Let LLM Learn More and Forget Less with Soft LoRA and Identity Mixture](https://aclanthology.org/2025.naacl-long.246.pdf)
  - [MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.1080.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 8 papers
  > To investigate whether up-weighting context-aware neurons impairs the model’s general abilities, we conducted evaluations of IRCAN on six widely-used benchmarks... including ARC [6], HellaSwag [47], MMLU [15], Winogrande [34], GSM8K [7], and TruthfulQA [24]. (Section 5.4)
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
  - [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
  - [Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 7 papers
  > We evaluated the general capabilities of the models on benchmarks related to general-domain chat (MT-Bench [83] and Alpaca-Eval [37]), general MCQs (MMLU [34] and GPQA [54]), and mathematical tasks (MATH [22] and GSM8k [12]). (Section 4.1)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
  - [Evaluating Copyright Takedown Methods for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/faed4276b52ef762879db4142655c699-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf)
  - [MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.1080.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 6 papers
  > “we evaluate the 12 models in Table 2 on challenging downstream zero- and few-shot benchmarks focusing on language understanding and reasoning. We include results for 0-shot (0S) and 3-shot (3S) evaluation for BIG-Bench Hard tasks [63, 64]”
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
  - [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf)
  - [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 4 papers
  > the LLM’s generic performance A as the evaluation across different tasks using the Harness framework. (Section 2.1)
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
  - [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 3 papers
  > Concurrently, we assess the models’ general capabilities using representative NLP tasks including MMLU (Hendrycks et al., 2020), ARC-Challenge (Clark et al., 2018), and GSM8K (Cobbe et al., 2021), ensuring that safety improvements do not come at the cost of overall performance.
  - [Understanding and Enhancing Safety Mechanisms of LLMs via Safety-Specific Neuron](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d2666e2cf44088cc57204fbc5ef7f34-Paper-Conference.pdf)
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 3 papers
  > To investigate whether up-weighting context-aware neurons impairs the model’s general abilities, we conducted evaluations of IRCAN on six widely-used benchmarks... including ARC [6], HellaSwag [47], MMLU [15], Winogrande [34], GSM8K [7], and TruthfulQA [24]. (Section 5.4)
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
  - [STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **WikiText** (measurement instrument): *measured_by*, 3 papers
  > We adopt the Evaluation Harness framework (Gao et al., 2023) for general capability evaluation, including MMLU (5-shot, Hendrycks et al., 2020), ARC-C (Clark et al., 2018) and WIKITEXT (Merity et al., 2016) (Section 4).
  - [Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation](https://proceedings.iclr.cc/paper_files/paper/2025/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf)
  - [Balancing Forget Quality and Model Utility: A Reverse KL-Divergence Knowledge Distillation Approach for Better Unlearning in LLMs](https://aclanthology.org/2025.naacl-long.60.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
- **ARC** (measurement instrument): *measured_by*, 3 papers
  > To investigate whether up-weighting context-aware neurons impairs the model’s general abilities, we conducted evaluations of IRCAN on six widely-used benchmarks... including ARC [6], HellaSwag [47], MMLU [15], Winogrande [34], GSM8K [7], and TruthfulQA [24]. (Section 5.4)
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
- **C-Eval** (measurement instrument): *measured_by*, 3 papers
  > For the general domain evaluation benchmarks, we select MATH, MBPP, MMLU, and CEVAL from the aforementioned experimental settings. (Section 3.3).
  - [Mix-CPT: A Domain Adaptation Framework via Decoupling Knowledge Learning and Format Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc721384c26c0bdff3ec31a7de31d8d5-Paper-Conference.pdf)
  - [Towards Effective and Efficient Continual Pre-training of Large Language Models](https://aclanthology.org/2025.acl-long.289.pdf)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **RTE** (measurement instrument): *measured_by*, 3 papers
  > we perform General Capability Tests using six natural language tasks... Specifically, the evaluation tasks include: ... 4. RTE (Recognizing Textual Entailment) (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 3 papers
  > Additionally, SPPO exhibits strong generalist abilities across different tasks, including MT-Bench, the Open LLM Leaderboard, and the more recent, more challenging benchmark, Arena-Hard.
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [Diverse Preference Learning for Capabilities and Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf)
  - [Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation](https://aclanthology.org/2025.acl-long.1136.pdf)
- **GPQA** (measurement instrument): *measured_by*, 3 papers
  > We evaluated the general capabilities of the models on benchmarks related to general-domain chat (MT-Bench [83] and Alpaca-Eval [37]), general MCQs (MMLU [34] and GPQA [54]), and mathematical tasks (MATH [22] and GSM8k [12]). (Section 4.1)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
  - [MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.1080.pdf)
- **MMBench** (measurement instrument): *measured_by*, 3 papers
  > we selected several common comprehensive benchmarks and VQA datasets, such as ... MMBench ... to evaluate the general capabilities of VLMs (Section 5.1).
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
  - [PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 2 papers
  > The fine-tuned models under MDS are evaluated on the general tasks including MMLU (Hendrycks et al., 2021), GSM8K (Cobbe et al., 2021), and PIQA (Bisk et al., 2020) to measure the catastrophic forgetting of the PEFT approaches.
  - [SLIM: Let LLM Learn More and Forget Less with Soft LoRA and Identity Mixture](https://aclanthology.org/2025.naacl-long.246.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **SIQA** (measurement instrument): *measured_by*, 2 papers
  > Ultimately, we select the following benchmarks as our downstream tasks: Social IQA (Sap et al., 2019), HellaSwag (Zellers et al., 2019), PiQA (Bisk et al., 2020), OpenBookQA (Mihaylov et al., 2018), Lambada (Paperno et al., 2016), SciQ (Welbl et al., 2017), ARC Easy (Clark et al., 2018), COPA (Sarlin et al., 2020), RACE (Lai et al., 2017), LogiQA (Liu et al., 2020), QQP (Wang et al., 2018), WinoGrande (Sakaguchi et al., 2021), and MultiRC (Khashabi et al., 2018). (Section 5)
  - [RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 2 papers
  > We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
  - [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 2 papers
  > To evaluate LLMs’ general capabilities, we select several widely used benchmark, i.e., HellaSwag (Zellers et al., 2019), Race (Lai et al., 2017), MMLU (Hendrycks et al., 2021), GPQA (Rein et al., 2024), OpenBookQA (Mihaylov et al., 2018), BoolQ (Clark et al., 2019), AG News (Zhang et al., 2015), IMDB (Maas et al., 2011), and Perplexity (Chen et al., 1998). (Section 4.1)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **LongBench** (measurement instrument): *measured_by*, 2 papers
  > LongBench (Bai et al., 2024): Focused on medium-context tasks (10K tokens), it assesses summarization, QA, and fact-checking across multiple domains, offering a measure of general capabilities.
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)
  - [DCIS: Efficient Length Extrapolation of LLMs via Divide-and-Conquer Scaling Factor Search](https://aclanthology.org/2025.emnlp-main.767.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 2 papers
  > “These models are trained further and evaluated on downstream tasks: ... ARC-e (Clark et al., 2018)”
  - [STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **MATH** (measurement instrument): *measured_by*, 2 papers
  > We evaluated the general capabilities of the models on benchmarks related to general-domain chat (MT-Bench [83] and Alpaca-Eval [37]), general MCQs (MMLU [34] and GPQA [54]), and mathematical tasks (MATH [22] and GSM8k [12]). (Section 4.1)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Mix-CPT: A Domain Adaptation Framework via Decoupling Knowledge Learning and Format Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc721384c26c0bdff3ec31a7de31d8d5-Paper-Conference.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 2 papers
  > To investigate whether up-weighting context-aware neurons impairs the model’s general abilities, we conducted evaluations of IRCAN on six widely-used benchmarks... including ARC [6], HellaSwag [47], MMLU [15], Winogrande [34], GSM8K [7], and TruthfulQA [24]. (Section 5.4)
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
  - [Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf)
- **TextVQA** (measurement instrument): *measured_by*, 2 papers
  > we further evaluated the performance of our fine-tuned visually-grounded language model (VLM) on additional benchmarks to ensure its robustness across a variety of tasks. In particular, we tested the model on TextVQA [42], POPE [29], and MMVet [51]. (Appendix C.3)
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **OpenCompass** (measurement instrument): *measured_by*, 2 papers
  > We evaluate seven distinctive capabilities of LLMs in a total of 17 representative NLP datasets based on the OpenCompass platform (Contributors, 2023). (Section 3.1).
  - [Mix-CPT: A Domain Adaptation Framework via Decoupling Knowledge Learning and Format Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc721384c26c0bdff3ec31a7de31d8d5-Paper-Conference.pdf)
  - [TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text](https://aclanthology.org/2025.emnlp-main.334.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 2 papers
  > To evaluate the LLM’s general performance in short-text tasks, we measure its WinRate against the text-davinci-003 model using 100 queries from AlpacaEval and 80 queries from VicunaEval. (Section 5.1)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
  - [UniCBE: An Uniformity-driven Comparing Based Evaluation Framework with Unified Multi-Objective Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eafca59fcbabb555fdb5373e2f34385e-Paper-Conference.pdf)
- **MME** (measurement instrument): *measured_by*, 2 papers
  > we selected several common comprehensive benchmarks and VQA datasets, such as ... MME ... to evaluate the general capabilities of VLMs (Section 5.1).
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
- **Open LLM Leaderboard** (measurement instrument): *measured_by*, 2 papers
  > Additionally, SPPO exhibits strong generalist abilities across different tasks, including MT-Bench, the Open LLM Leaderboard, and the more recent, more challenging benchmark, Arena-Hard.
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [DCIS: Efficient Length Extrapolation of LLMs via Divide-and-Conquer Scaling Factor Search](https://aclanthology.org/2025.emnlp-main.767.pdf)
- **GLUE** (measurement instrument): *measured_by*, 2 papers
  > “To further evaluate the intrinsic knowledge of post-edited LLMs, we perform General Capability Tests using six natural language tasks from the General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2019).”
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
  - [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.327.pdf)
- **SciQ** (measurement instrument): *measured_by*, 2 papers
  > “These models are trained further and evaluated on downstream tasks: ... SciQ (Welbl et al., 2017)”
  - [STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **CMMLU** (measurement instrument): *measured_by*, 2 papers
  > our approach can largely improve the performance of Llama-3 (8B), including both the general abilities (+8.81 on C-Eval and +6.31 on CMMLU)
  - [Towards Effective and Efficient Continual Pre-training of Large Language Models](https://aclanthology.org/2025.acl-long.289.pdf)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **TOFU** (measurement instrument): *measured_by*, 2 papers
  > Model utility is assessed using three datasets from the TOFU benchmark related to different types of knowledge. (Section 4.2.3)
  - [Balancing Forget Quality and Model Utility: A Reverse KL-Divergence Knowledge Distillation Approach for Better Unlearning in LLMs](https://aclanthology.org/2025.naacl-long.60.pdf)
  - [A Probabilistic Perspective on Unlearning and Alignment for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b69bc53449ba46bb981951078929a5e-Paper-Conference.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 1 paper
  > "We evaluate the pre-trained base models on 17 tasks across different general domains which include: MMLU (Hendrycks et al., 2020), Arc-Easy, Arc-Challenge (Clark et al., 2018), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), SciQ (Welbl et al., 2017), RTE (Dagan et al., 2005), BBH (Suzgun et al., 2022), LAMBADA"
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **HumanEval** (measurement instrument): *measured_by*, 1 paper
  > As shown in Appendix E.2, we assessed each iteration’s performance on general benchmarks, including GSM8k (Cobbe et al., 2021), TriviaQA (Joshi et al., 2017), MMLU (Hendrycks et al., 2020), and HumanEval (Chen et al., 2021). (Section 3.3)
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **WikiText-2** (measurement instrument): *measured_by*, 1 paper
  > "To ensure the desired model capabilities are not impacted by editing, we measure the perplexity of the model on the dev split of WikiText-2"
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
- **POPE** (measurement instrument): *measured_by*, 1 paper
  > we further evaluated the performance of our fine-tuned visually-grounded language model (VLM) on additional benchmarks to ensure its robustness across a variety of tasks. In particular, we tested the model on TextVQA [42], POPE [29], and MMVet [51]. (Appendix C.3)
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 1 paper
  > we further evaluated the performance of our fine-tuned visually-grounded language model (VLM) on additional benchmarks to ensure its robustness across a variety of tasks. In particular, we tested the model on TextVQA [42], POPE [29], and MMVet [51]. (Appendix C.3)
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
- **StrongREJECT** (measurement instrument): *measured_by*, 1 paper
  > "Therefore, the StrongREJECT evaluator measures both of these dimensions: willingness and capabilities."
  - [A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MBPP** (measurement instrument): *measured_by*, 1 paper
  > For the general domain evaluation benchmarks, we select MATH, MBPP, MMLU, and CEVAL from the aforementioned experimental settings. (Section 3.3).
  - [Mix-CPT: A Domain Adaptation Framework via Decoupling Knowledge Learning and Format Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc721384c26c0bdff3ec31a7de31d8d5-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurement instrument): *measured_by*, 1 paper
  > We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **BBH Object Counting** (measurement instrument): *measured_by*, 1 paper
  > We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > As shown in Appendix E.2, we assessed each iteration’s performance on general benchmarks, including GSM8k (Cobbe et al., 2021), TriviaQA (Joshi et al., 2017), MMLU (Hendrycks et al., 2020), and HumanEval (Chen et al., 2021). (Section 3.3)
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **SST** (measurement instrument): *measured_by*, 1 paper
  > we perform General Capability Tests using six natural language tasks... Specifically, the evaluation tasks include: 1. SST (The Stanford Sentiment Treebank) (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **MRPC** (measurement instrument): *measured_by*, 1 paper
  > we perform General Capability Tests using six natural language tasks... Specifically, the evaluation tasks include: ... 2. MRPC (Microsoft Research Paraphrase Corpus) (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Vicuna-Bench** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the LLM’s general performance in short-text tasks, we measure its WinRate against the text-davinci-003 model using 100 queries from AlpacaEval and 80 queries from VicunaEval. (Section 5.1)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 1 paper
  > we selected several common comprehensive benchmarks and VQA datasets, such as ... VQAv2 ... to evaluate the general capabilities of VLMs (Section 5.1).
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **MMMU-Pro** (measurement instrument): *measured_by*, 1 paper
  > we selected several common comprehensive benchmarks and VQA datasets, such as ... MMMU-Pro to evaluate the general capabilities of VLMs (Section 5.1).
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **MixEval** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the general capabilities of the self-play fine-tuned models, we employ MixEval (Ni et al., 2024) and Open LLM Leaderboard v2 (Fourrier et al., 2024) for benchmark evaluation. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **Open LLM Leaderboard v2** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the general capabilities of the self-play fine-tuned models, we employ MixEval (Ni et al., 2024) and Open LLM Leaderboard v2 (Fourrier et al., 2024) for benchmark evaluation. (Section 4.2)
  - [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf)
- **Adversarial robustness** (construct): *causes*, 1 paper
  > increased model capabilities give rise to distinct emergent model vulnerabilities. (Section 1)
  - [Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf)
- **Spider** (measurement instrument): *measured_by*, 1 paper
  > To validate that MTJD indeed betters output quality, we test MTJD (k=4) and standard multinomial sampling on Spider, MTBench, and HumanEval using the Llama-3 series models. ... For this process, the higher the scores, the better the downstream performance. (Section 5.1)
  - [Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf)
- **SAMSum** (measurement instrument): *measured_by*, 1 paper
  > To explore the side effects of sequential model editing on the general abilities of LLMs, four representative tasks with corresponding datasets were adopted for assessment... including: ... Summarization on the SAMSum (Gliwa et al., 2019)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
- **The Pile** (measurement instrument): *measured_by*, 1 paper
  > maintain the general-purpose ability (losses on the Pile) unchanged.
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)
- **TyDi QA** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the general capabilities, we utilized GSM8K (EM) (Cobbe et al., 2021), BBH (EM) (Cobbe et al., 2021), MMLU (EM) (Hendrycks et al., 2020), TydiQA (F1) (Clark et al., 2020), and WikiText (ppl) (Merity et al., 2016), following Ivison et al. (2023). (Section 4)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 1 paper
  > Remarkably, on AlpacaEval 2 (Li et al., 2023c) and Arena-Hard (Li et al., 2024b), two LLM general problem-solving ability benchmarks, the model trained on 20K our synthetic instruction-response pairs, consistently outperforms models trained on significantly larger datasets... (Section 1)
  - [Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation](https://aclanthology.org/2025.acl-long.1136.pdf)
- **RACE** (measurement instrument): *measured_by*, 1 paper
  > To evaluate LLMs’ general capabilities, we select several widely used benchmark, i.e., HellaSwag (Zellers et al., 2019), Race (Lai et al., 2017), MMLU (Hendrycks et al., 2021), GPQA (Rein et al., 2024), OpenBookQA (Mihaylov et al., 2018), BoolQ (Clark et al., 2019), AG News (Zhang et al., 2015), IMDB (Maas et al., 2011), and Perplexity (Chen et al., 1998). (Section 4.1)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 1 paper
  > To evaluate LLMs’ general capabilities, we select several widely used benchmark, i.e., HellaSwag (Zellers et al., 2019), Race (Lai et al., 2017), MMLU (Hendrycks et al., 2021), GPQA (Rein et al., 2024), OpenBookQA (Mihaylov et al., 2018), BoolQ (Clark et al., 2019), AG News (Zhang et al., 2015), IMDB (Maas et al., 2011), and Perplexity (Chen et al., 1998). (Section 4.1)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
- **AG News** (measurement instrument): *measured_by*, 1 paper
  > To evaluate LLMs’ general capabilities, we select several widely used benchmark, i.e., HellaSwag (Zellers et al., 2019), Race (Lai et al., 2017), MMLU (Hendrycks et al., 2021), GPQA (Rein et al., 2024), OpenBookQA (Mihaylov et al., 2018), BoolQ (Clark et al., 2019), AG News (Zhang et al., 2015), IMDB (Maas et al., 2011), and Perplexity (Chen et al., 1998). (Section 4.1)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
- **IMDb** (measurement instrument): *measured_by*, 1 paper
  > To evaluate LLMs’ general capabilities, we select several widely used benchmark, i.e., HellaSwag (Zellers et al., 2019), Race (Lai et al., 2017), MMLU (Hendrycks et al., 2021), GPQA (Rein et al., 2024), OpenBookQA (Mihaylov et al., 2018), BoolQ (Clark et al., 2019), AG News (Zhang et al., 2015), IMDB (Maas et al., 2011), and Perplexity (Chen et al., 1998). (Section 4.1)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
- **MultiRC** (measurement instrument): *measured_by*, 1 paper
  > "We evaluate the pre-trained base models on 17 tasks across different general domains which include: MMLU (Hendrycks et al., 2020), Arc-Easy, Arc-Challenge (Clark et al., 2018), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), SciQ (Welbl et al., 2017), RTE (Dagan et al., 2005), BBH (Suzgun et al., 2022), LAMBADA (Paperno et al., 2016), OpenBookQA (Mihaylov et al., 2018), RACE-Middle, RACE-High (Lai et al., 2017), MultiRC"
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **CoLA** (measurement instrument): *measured_by*, 1 paper
  > we perform General Capability Tests using six natural language tasks... Specifically, the evaluation tasks include: ... 5. CoLA (Corpus of Linguistic Acceptability) (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **CCBench** (measurement instrument): *measured_by*, 1 paper
  > We assess the models’ general ability on three widely used benchmarks: MMBench (Liu et al., 2023c), CCBench (Liu et al., 2023c), and SEEDImage (Li et al., 2023a), to verify that our model’s general capabilities. (Section 5.2)
  - [PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf)
- **MMStar** (measurement instrument): *measured_by*, 1 paper
  > “We adopt MMStar (Chen et al., 2024c), an advanced benchmark of evaluation the comprehensive capabilities of LVLMs, as the primary evaluation metric.” (Section 4.1)
  - [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf)

### → General ability
- **Catastrophic forgetting** (behavioral indicator): *causes*, 3 papers
  > Furthermore, after fine-tuning the downstream tasks, the LLM may lose the general capability, due to catastrophic forgetting. (Section 1)
  - [SLIM: Let LLM Learn More and Forget Less with Soft LoRA and Identity Mixture](https://aclanthology.org/2025.naacl-long.246.pdf)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
  - [Mitigating Catastrophic Forgetting in Large Language Models with Forgetting-aware Pruning](https://aclanthology.org/2025.emnlp-main.1108.pdf)
- **Generation diversity** (construct): *causes*, 1 paper
  > Diversity loss can harm both capabilities and representation. (Section 3.1)
  - [Diverse Preference Learning for Capabilities and Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf)
- **Image classification** (behavioral indicator): *causes*, 1 paper
  > enhanced classification performance of the VLM transfers to its general capabilities
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
- **Evaluation ability** (construct): *causes*, 1 paper
  > Furthermore, our training method enhances the general capabilities of the model by constructing complicated judge task... (Abstract)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)

### Associated with
- **Reasoning** (construct), 2 papers
  > Finally, the identification of a single common factor underlying all benchmark scores suggests that a general ability for reasoning and knowledge can be effectively measured through a consolidated, sparse benchmark. (Section 4)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Safety alignment** (construct), 1 paper
  > The shape of the LLM capability landscape is drastically different from the one in the LLM safety landscape; these landscapes do not exhibit the same trend, further confirming that the basin shape is indeed unique to the safety of LLM.
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
- **Composability** (construct), 1 paper
  > The disparity between overall utility and composability metrics underscores the need for more nuanced evaluations explicitly targeting composability as a design criterion. (Section 4.4)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)
- **Knowledge** (construct), 1 paper
  > Finally, the identification of a single common factor underlying all benchmark scores suggests that a general ability for reasoning and knowledge can be effectively measured through a consolidated, sparse benchmark. (Section 4)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **Understanding** (construct), 1 paper
  > degradation in foundational LLM capabilities such as comprehension, reasoning, and common sense — an effect known as alignment tax (Section 1)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Commonsense knowledge** (construct), 1 paper
  > degradation in foundational LLM capabilities such as comprehension, reasoning, and common sense — an effect known as alignment tax (Section 1)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Adaptability** (construct), 1 paper
  > How can we preserve and transfer the general capabilities of LLMs while enabling them to adapt to domain-specific knowledge? (Section 1).
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
- **Natural language inference** (behavioral indicator), 1 paper
  > we perform General Capability Tests using six natural language tasks... Specifically, the evaluation tasks include: ... 6. NLI (Natural Language Inference) (Section 4.3).
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
