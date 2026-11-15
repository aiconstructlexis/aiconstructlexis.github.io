# Knowledge editing
**Type:** Behavioral indicator  
**Supporting papers:** 28  
**Also known as:** Knowledge erasure, Knowledge update, User-specific editing, Visual entity editing, Visual semantic editing, Model editing, Factual knowledge updating, Hallucination correction, Sequence editing, Sequential editing, Sequential knowledge editing, Fact editing  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is targeted updating of a model's stored factual or commonsense knowledge so that, for a specified prompt or input, the model returns a desired new or corrected answer while unrelated outputs remain unchanged. Most definitions describe this as modifying a small number of parameters, or otherwise making targeted parameter changes, rather than full retraining. A smaller line of work broadens the task to targeted model editing of knowledge and capabilities, or to in-context editing that makes the model answer consistently with a provided fact without changing weights. Other papers use narrower observable outcomes under the same umbrella, including producing an updated fact, ceasing to produce an old fact, changing the object in a subject-relation pair, or correcting hallucinated content.

**Variants.** Variants differ mainly by time, target, and modality. A recurrent variant is sequential editing, where multiple edits are applied to the same model over time and evaluation checks whether earlier edits are retained. Other work separates update and erasure tasks, studies multimodal cases that modify entity-centric visual knowledge, complex visual semantics such as actions or object relationships, and personalized user information, and frames the target either as subject-relation-object factual updates or as hallucination correction. A smaller line also uses broader labels such as model editing and fact editing.

**Space of elicitation and scores.** Knowledge editing is measured by six instruments. The most commonly linked are CounterFact and ZsRE, which papers describe as widely adopted or representative benchmarks for model or factual editing. Papers also use SelfCheckGPT, specifically as a hallucination correction dataset, then WikiData_counterfact and WikiBio, and one other instrument.

**What it is taken as evidence of.** Papers do not converge on a single construct that knowledge editing is taken to indicate. The most recurrent connection is to editing locality: one paper claims a causal relationship from knowledge editing to editing locality, while others describe the two as related and discuss locality as a criterion or aspect of knowledge editing. Papers also relate generality and portability to knowledge editing, and one paper explicitly uses the success rate of knowledge editing to assess context faithfulness. A smaller line claims a causal relationship from knowledge editing to editability, and papers link it to three other constructs as well.

## Sources

**Knowledge editing** (5 papers: [Reasons and Solutions for the Decline in Model Performance after Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f588e59e9ae6138d3ea9e4fdaa7e040-Paper-Conference.pdf), [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf), [ChainEdit: Propagating Ripple Effects in LLM Knowledge Editing through Logical Rule-Guided Chains](https://aclanthology.org/2025.acl-long.665.pdf), [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf), [Dynamic Retriever for In-Context Knowledge Editing via Policy Optimization](https://aclanthology.org/2025.emnlp-main.848.pdf))
> Updating a model's stored factual or commonsense knowledge by modifying a small number of parameters.

**Knowledge erasure** (2 papers: [Knowledge Localization: Mission Not Accomplished? Enter Query Localization!](https://proceedings.iclr.cc/paper_files/paper/2025/file/48adb34f7ee39177c4c23a8e4253a492-Paper-Conference.pdf), [The Knowledge Microscope: Features as Better Analytical Lenses than Neurons](https://aclanthology.org/2025.acl-long.516.pdf))
> The observable outcome of a model ceasing to produce a specific fact in response to relevant queries after its parameters have been modified.

**Knowledge update** (2 papers: [Knowledge Localization: Mission Not Accomplished? Enter Query Localization!](https://proceedings.iclr.cc/paper_files/paper/2025/file/48adb34f7ee39177c4c23a8e4253a492-Paper-Conference.pdf), [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf))
> The observable outcome of a model producing a new, updated fact in response to relevant queries after its parameters have been modified to replace an old fact.

**Visual entity editing** (1 paper: [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf))
> The observable task of modifying a model's knowledge about a specific visual entity, such as updating its attributes or associated facts.

**Visual semantic editing** (1 paper: [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf))
> The observable task of modifying a model's understanding of complex visual semantics, such as actions, body gestures, or object relationships.

**User-specific editing** (1 paper: [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf))
> The observable task of incorporating new, personalized user information into a model, such as details about owned items or personal relationships.

**Model editing** (1 paper: [Efficient Model Editing with Task-Localized Sparse Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96f5de31e8e3d19cbcd3a7397b8dce57-Paper-Conference.pdf))
> The general practice of modifying a pre-trained model's parameters to add, remove, or alter its knowledge and capabilities in a targeted manner.

**Factual knowledge updating** (1 paper: [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.327.pdf))
> The observable process of modifying model parameters to reflect new factual associations in the form of subject-relation-object triples, such as updating "Beats Music is owned by Apple."

**Hallucination correction** (1 paper: [Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.733.pdf))
> Reducing or eliminating factually incorrect statements in model outputs by applying knowledge edits.

**Sequence editing** (1 paper: [Reasons and Solutions for the Decline in Model Performance after Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f588e59e9ae6138d3ea9e4fdaa7e040-Paper-Conference.pdf))
> Repeatedly applying multiple knowledge edits to the same model over a sequence of samples.

**Sequential editing** (2 papers: [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf), [BalancEdit: Dynamically Balancing the Generality-Locality Trade-off in Multi-modal Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25e/guo25e.pdf))
> The task of continuously updating a model with multiple, sequential pieces of knowledge and evaluating its ability to retain earlier edits.

**Sequential knowledge editing** (2 papers: [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf), [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf))
> The observable process of applying a series of targeted updates to a model's parameters to modify its stored knowledge over time.

**Fact editing** (1 paper: [Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching](https://proceedings.iclr.cc/paper_files/paper/2024/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf))
> Model behavior where a stored fact is modified through weight or activation intervention to change the output from one object to another for the same subject-relation pair.

## Relationships

### Knowledge editing →
- **ZsRE** (measurement instrument): *measured_by*, 4 papers
  > we edit different kinds of knowledge: WikiDatarecent, WikiDatacounterfact (Cohen et al., 2024), WikiBio (Hartvigsen et al., 2024), ConvSent (Mitchell et al., 2022), and ZsRE (Yao et al., 2023). (Section 3.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
  - [Dynamic Retriever for In-Context Knowledge Editing via Policy Optimization](https://aclanthology.org/2025.emnlp-main.848.pdf)
  - [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.327.pdf)
- **CounterFact** (measurement instrument): *measured_by*, 4 papers
  > “We evaluate AlphaEdit using two widely adopted benchmarks: the Counterfact dataset (Meng et al., 2022) and the ZsRE dataset (Levy et al., 2017).”
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
  - [Dynamic Retriever for In-Context Knowledge Editing via Policy Optimization](https://aclanthology.org/2025.emnlp-main.848.pdf)
  - [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.327.pdf)
  - [Mechanistic Unlearning: Robust Knowledge Unlearning and Editing via Mechanistic Localization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25k/guo25k.pdf)
- **SelfCheckGPT** (measurement instrument): *measured_by*, 3 papers
  > “we also evaluate its ability to correct Hallucination in SelfCheckGPT [48].”
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
  - [Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.733.pdf)
  - [MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1719.pdf)
- **Editing locality** (construct): *causes*, 3 papers
  > direct editing of long-term memory (ROME, MEMIT, etc.) creates conflicts with prior pretraining knowledge, resulting in poor locality (Section 3.2)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **WikiData_counterfact** (measurement instrument): *measured_by*, 2 papers
  > we edit different kinds of knowledge: WikiDatarecent, WikiDatacounterfact (Cohen et al., 2024), WikiBio (Hartvigsen et al., 2024), ConvSent (Mitchell et al., 2022), and ZsRE (Yao et al., 2023). (Section 3.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
  - [Dynamic Retriever for In-Context Knowledge Editing via Policy Optimization](https://aclanthology.org/2025.emnlp-main.848.pdf)
- **WikiData_recent** (measurement instrument): *measured_by*, 1 paper
  > we edit different kinds of knowledge: WikiDatarecent, WikiDatacounterfact (Cohen et al., 2024), WikiBio (Hartvigsen et al., 2024), ConvSent (Mitchell et al., 2022), and ZsRE (Yao et al., 2023). (Section 3.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **WikiBio** (measurement instrument): *measured_by*, 1 paper
  > we edit different kinds of knowledge: WikiDatarecent, WikiDatacounterfact (Cohen et al., 2024), WikiBio (Hartvigsen et al., 2024), ConvSent (Mitchell et al., 2022), and ZsRE (Yao et al., 2023). (Section 3.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **Editability** (construct): *causes*, 1 paper
  > The sequential updates gradually deviate the model from its initial state, leading to degradation in its editability (Ma et al., 2024; Gupta et al., 2024b). (Section 1)
  - [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf)
- **Catastrophic forgetting** (behavioral indicator): *causes*, 1 paper
  > The model typically encounters catastrophic forgetting during sequential edits, where previously edited examples are forgotten (Wang et al., 2024a; Gupta et al., 2024a). (Section 1)
  - [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf)
- **Knowledge retention** (construct): *causes*, 1 paper
  > the accumulation of preservation loss inevitably erodes model stability during sequential editing operations, ultimately leading to model forgetting and collapse (Section 1).
  - [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.327.pdf)

### Associated with
- **Generality** (construct), 2 papers
  > Knowledge editing seeks to maximize the chance of an LLM responding with y given x, while satisfying the following additional criteria at the same time...: (1) Generality: there are different ways to express US president, wherefore the edited model should generalize. (Section 2.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Portability** (construct), 2 papers
  > Knowledge editing seeks to maximize the chance of an LLM responding with y given x, while satisfying the following additional criteria at the same time...: (2) Portability: relevant knowledge such as the first lady of United States should be updated as well. (Section 2.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **Reliability** (construct), 1 paper
  > i) reliability, the model can remember both current and previous edits after sequential editing
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Linguistic quality** (construct), 1 paper
  > “We analyze ICE across four critical aspects of knowledge editing: accuracy, locality, generalization, and linguistic quality, demonstrating its advantages.”
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **Context faithfulness** (construct), 1 paper
  > this paper uses the success rate of KE to assess the context-faithfulness of LLMs (Section 2.2)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
