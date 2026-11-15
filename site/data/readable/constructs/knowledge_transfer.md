# Knowledge transfer
**Type:** Construct  
**Supporting papers:** 94  
**Also known as:** Transferability, Ability transfer, Transfer learning, Skill transfer, Transfer, Task transfer, Cross-task transfer, In-context transferability, Task transferability, Backward transfer, Forward transfer, Prompt transferability, Knowledge transferability, Competence transfer  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is transferability: the degree to which something learned in one setting remains effective in another, usually across models, tasks, datasets, languages, modalities, or training objectives. In this usage, what transfers is often a prompt, jailbreak attack, policy, detector, value network, or learned algorithm rather than the whole model, and papers variously describe cases where transfer is weak, such as continuous prompts not being directly transferable, and cases of broad transfer across unseen models or tasks. A smaller line of work uses knowledge transfer more broadly for a model or multi-expert system reusing previously learned knowledge on downstream tasks, including cross-lingual, cross-domain, and cross-modality application. The main variation is therefore both in scope and locus: some definitions treat it as a latent ability of models or experts, while others treat it as the observed degree of performance carryover of a specific learned artifact.

**Space of facets.** Most papers organize the concept through subtypes tied to setting rather than through a single common taxonomy. In continual learning, some authors explicitly define knowledge transfer as including forward transfer, earlier tasks helping later ones, and backward transfer, later learning helping earlier tasks; benchmark-reduction work further distinguishes task transferability from in-context transferability, where transfer is estimated from how much one task's exemplars help another. Other papers narrow the umbrella to prompt transferability, skill transfer, ability transfer across languages, cross-task transfer across modalities or settings, and competence transfer between semantically related goals. The terminology is correspondingly broad, with knowledge transfer, transferability, knowledge transferability, transfer learning, task transfer, and competence transfer used for overlapping ideas about carrying learned behavior across settings.

**Space of measurement.** Papers link the construct to 2 measurement instruments, GSM8K and TruthfulQA, both used as benchmarks, and to 2 behavioral indicators, Time series forecasting and Catastrophic forgetting, though the latter appear in causal or related claims rather than as direct instruments. Operationalization is usually outcome-based: authors apply a prompt, attack, detector, value network, or other learned component from one model, task, dataset, language, or modality to another and judge transfer by retained or improved performance, sometimes through cross-task evaluation, attack success rates, ablations, or transfer ICL, where performance from task-i exemplars on task-j is taken to reflect transferability. One multilingual paper also says TCd directly measures a model's ability to transfer knowledge across languages through consistent factual answers. These operationalizations mostly match the dominant definition as cross-setting effectiveness, though some broader uses infer knowledge transfer from downstream benchmark gains or from time-series forecasting performance after ablations rather than from a dedicated transfer score.

**Links.** One paper claims a causal relationship from Knowledge transfer to Generalization, saying prior knowledge lets models generalize better to new tasks or domains, while a few other papers relate transferability to prompt or structural prompt generalization. Separate single-paper claims describe a causal relationship from Knowledge transfer to Time series forecasting, and causal relationships from Abstraction and Cross-lingual alignment to Knowledge transfer; one paper also reports that Expressive power correlates with Knowledge transfer, with larger source models showing lower prompt transfer performance. Other papers relate Knowledge transfer to In-context learning, Robustness, Continual learning, Knowledge manipulation, Expert specialization, Parametric knowledge, Rule-based reasoning, and Catastrophic forgetting.

## Sources

**Transferability** (19 papers: [AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f83cb637e159e789f5576ff6848874de-Paper-Conference.pdf), [Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy](https://proceedings.iclr.cc/paper_files/paper/2024/file/e537e071277a2e5fefaa78f87500c7b4-Paper-Conference.pdf), [Making Pre-trained Language Models Great on Tabular Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/668563ef18fbfef0b66af491ea334d5f-Paper-Conference.pdf), [Plug-and-Play Policy Planner for Large Language Model Powered Dialogue Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/29e8437db7b549160ce03d336ff66f65-Paper-Conference.pdf), [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf), [Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/9e79aefb538d02a7c0610fa43bdb0d0f-Paper-Conference.pdf), [Zero-Shot Continuous Prompt Transfer: Generalizing Task Semantics Across Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/05f0734db34deb367fc66f1482528044-Paper-Conference.pdf), [Shadowcast: Stealthy Data Poisoning Attacks Against Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a2e30664b9647f97d7b9275358d083c-Paper-Conference.pdf), [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf), [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf), [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.88.pdf), [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf), [Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning](https://aclanthology.org/2025.naacl-long.519.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [Tricking Retrievers with Influential Tokens: An Efficient Black-Box Corpus Poisoning Attack](https://aclanthology.org/2025.naacl-long.210.pdf), [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf), [Iterative Self-Tuning LLMs for Enhanced Jailbreaking Capabilities](https://aclanthology.org/2025.naacl-long.297.pdf), [Cuckoo: An IE Free Rider Hatched by Massive Nutrition in LLM's Nest](https://aclanthology.org/2025.acl-long.66.pdf), [Learning from Few Samples: A Novel Approach for High-Quality Malcode Generation](https://aclanthology.org/2025.emnlp-main.70.pdf))
> The degree to which continuous prompts learned on one language model can be effectively applied to another, reflecting the generalizability of task semantics across model architectures and embedding spaces.

**Knowledge transfer** (2 papers: [TeamLoRA: Boosting Low-Rank Adaptation with Expert Collaboration and Competition](https://aclanthology.org/2025.acl-long.669.pdf), [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf))
> The latent ability of domain-specific experts to share and apply their learned knowledge to relevant downstream tasks within a multi-expert system.

**Ability transfer** (1 paper: [Extracting and Combining Abilities For Building Multi-lingual Ability-enhanced Large Language Models](https://aclanthology.org/2025.emnlp-main.887.pdf))
> The latent capacity to transfer learned capabilities from one language or domain to another without retraining, preserving the core knowledge while adapting to new linguistic contexts.

**Transfer learning** (1 paper: [Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf))
> The ability of a model to leverage knowledge gained from training on one task or objective to improve its performance on a different but related task or objective.

**Skill transfer** (1 paper: [Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf))
> The degree to which a capability or mechanism learned on one task can be successfully applied or adapted to improve performance on a different task.

**Knowledge transferability** (2 papers: [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf), [Do You Know About My Nation? Investigating Multilingual Language Models' Cultural Literacy Through Factual Knowledge](https://aclanthology.org/2025.emnlp-main.756.pdf))
> The model's ability to effectively transfer learned patterns and knowledge from source domains to improve performance on different target domains.

**Transfer** (1 paper: [Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf))
> The ability to apply learned knowledge, such as abstract variables, from a training context to a new, related context.

**Task transfer** (1 paper: [Task-Adaptive Pretrained Language Models via Clustered-Importance Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/688006b3d1df8be5bb2a2a31a407180c-Paper-Conference.pdf))
> The ability of a model trained for one task to perform well on a different, unevaluated task.

**Cross-task transfer** (1 paper: [LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf))
> The ability to apply knowledge or skills learned from one set of tasks to perform new, untrained tasks, often by composing existing capabilities.

**In-context transferability** (1 paper: [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf))
> A task-level latent property estimated from how much exemplars from one task improve performance on another task when used as in-context examples.

**Task transferability** (1 paper: [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf))
> The degree to which knowledge or skill learned from one task improves performance on another task, reflecting overlap or generalization across tasks.

**Backward transfer** (1 paper: [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf))
> The extent to which learning new tasks improves performance on previously learned tasks.

**Forward transfer** (1 paper: [Adapt-$\infty$: Scalable Continual Multimodal Instruction Tuning via Dynamic Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf))
> The phenomenon where knowledge gained from previous tasks improves the learning of new, subsequent tasks.

**Prompt transferability** (1 paper: [Efficient and Privacy-Preserving Soft Prompt Transfer for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ds/wang25ds.pdf))
> The latent ability of a soft prompt tuned on one language model to maintain high performance when applied to a different, larger language model.

**Competence transfer** (1 paper: [MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gaven25a/gaven25a.pdf))
> The phenomenon where practicing one goal improves performance on other semantically related goals, captured dynamically through learned representations rather than predefined groupings.

## Relationships

### Knowledge transfer →
- **Generalization** (construct): *causes*, 3 papers
  > This transfer is crucial as it allows the model to leverage previously acquired knowledge to better generalize to new tasks or domains. (Section 1)
  - [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf)
  - [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf)
  - [Have We Designed Generalizable Structural Knowledge Promptings? Systematic Evaluation and Rethinking](https://aclanthology.org/2025.acl-long.110.pdf)
- **Time series forecasting** (behavioral indicator): *causes*, 1 paper
  > We attribute the performance gains of TIME-FFM to the valid knowledge transferability across domains. (Section 4.3)
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > Bulilding on this success we further extended DAMO to LLMs, where is also delivered strong results on benchmarks such as TruthfulQA Lin et al. (2021), FACTOR Muhlgay et al. (2023), and GSM8K Cobbe et al. (2021), indicating that DAMO possesses notable transferability across different tasks and model types. (Section 1)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > Bulilding on this success we further extended DAMO to LLMs, where is also delivered strong results on benchmarks such as TruthfulQA Lin et al. (2021), FACTOR Muhlgay et al. (2023), and GSM8K Cobbe et al. (2021), indicating that DAMO possesses notable transferability across different tasks and model types. (Section 1)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)

### → Knowledge transfer
- **Expressive power** (construct): *correlates*, 1 paper
  > We observed in Table 3 that a larger source model (either BERTlarge or RoBERTalarge) has lower transfer performance. This aligns with the intuition in Khashabi et al. (2022) that there could be a large number of similarly performing continuous prompts, residing in a large (and also deep) model’s expressive embedding space... Therefore, the induced prompt may carry model specificity in addition to task semantics, limiting its transferability to other models. (Section 3.3)
  - [Zero-Shot Continuous Prompt Transfer: Generalizing Task Semantics Across Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/05f0734db34deb367fc66f1482528044-Paper-Conference.pdf)
- **Abstraction** (construct): *causes*, 1 paper
  > Higher levels of abstraction implies more flexible transfer
  - [Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf)
- **Cross-lingual alignment** (construct): *causes*, 1 paper
  > A classic assumption in multilingual NLP is that more consistent multilingual representations facilitate easier knowledge transfer (Pan et al., 2021; Tang et al., 2022). (Section 1)
  - [AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment](https://aclanthology.org/2025.emnlp-main.328.pdf)

### Associated with
- **In-context learning** (construct), 2 papers
  > Moreover, the absence of the need to update model parameters also allows a good attribution result for ICL to be transferable across different language models. (Introduction)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)
- **Robustness** (construct), 1 paper
  > In this subsection, we aim to evaluate the robustness, especially the generalizability and transferability of our method MoD to various LLMs. (Section 4.5)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator), 1 paper
  > Cross-domain co-training on a large number of datasets only negatively impacts LLaGA. A similar phenomenon can also be observed when LLMs with cross-modality projectors are applied to CV [49], which may be related to catastrophic forgetting. (Section 4.2.1)
  - [Text-space Graph Foundation Models: Comprehensive Benchmarks and New Insights](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e0b39c69663e9c073739adf547ed778-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Knowledge manipulation** (construct), 1 paper
  > enhance the knowledge manipulation (e.g., knowledge recall, reasoning, and transfer) ability of LLMs. (Section 1)
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)
- **Expert specialization** (construct), 1 paper
  > Thus, there exists a trade-off between the short-term cost savings from knowledge transfer and the long-term convergence efficiency through expert specialization. (Section 1)
  - [Drop-Upcycling: Training Sparse Mixture of Experts with Partial Re-initialization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d24b7366d714b09a977946ef0d9bf3ad-Paper-Conference.pdf)
- **Continual learning** (construct), 1 paper
  > Previous CL research posits that an effective CL method should address two primary challenges: 1) Catastrophic Forgetting (CF) ... and 2) Knowledge Transfer (KT), which includes both forward transfer and backward transfer. (Section 2.1).
  - [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf)
- **Parametric knowledge** (construct), 1 paper
  > Our findings highlight the critical factors contributing to the process of parametric knowledge transfer, underscoring the transferability of model parameters across LLMs of different scales. (Section 1)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
- **Rule-based reasoning** (construct), 1 paper
  > For rule-based reasoning, once a rule is formed through induction, it should be transferable.
  - [MIRAGE: Evaluating and Explaining Inductive Reasoning Process in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b782a3462ee9d566291cff148333ea9b-Paper-Conference.pdf)
