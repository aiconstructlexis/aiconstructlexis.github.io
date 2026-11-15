# Coreference resolution
**Type:** Behavioral indicator  
**Supporting papers:** 47  
**Also known as:** Pronoun resolution, Co-reference resolution, Pronoun reference resolution, Reference resolution, Anaphora resolution, Argument alignment, Pronoun disambiguation  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is a reference-linking task: the model determines which noun phrases, pronouns, or other expressions refer to the same real-world entity. Most commonly this appears as pronoun resolution, where the model identifies the correct antecedent from context, often in Winograd or WinoGrande style examples and sometimes explicitly as a 2-choice, commonsense task. A smaller fairness-oriented usage narrows success to linking a gendered pronoun to the correct occupation or profession, including stereotypical and anti-stereotypical cases.

**Variants.** Papers also use nearby names such as pronoun resolution, co-reference resolution, pronoun disambiguation, reference resolution, and anaphora resolution. Beyond sentence-level antecedent choice, some work studies discourse-level resolution in spoken utterances and conversations, translation where the correct pronoun depends on prior context, and multi-document argument alignment that matches arguments across documents to the same referent using semantic compatibility and coreference cues. A smaller line of work places coreference resolution in broader pipelines: papers claim a causal relationship from coreference resolution to text summarization, question answering, and relation extraction, and another paper relates it to textual reasoning.

**Space of elicitation and scores.** Among its 8 linked instruments, papers most often measure it with WinoGrande, described as commonsense coreference resolution, pronoun resolution, or pronoun disambiguation, sometimes as a 2-choice task. WinoBias and WSC are the next most common, with WinoBias focusing on associating gendered pronouns with occupations and WSC evaluating coreference resolution capabilities. The linked instruments are mainly datasets and benchmarks, with OntoNotes and SuperGLUE also appearing, alongside 3 other linked instruments.

**What it is taken as evidence of.** When papers connect this behavior to constructs, they do not converge on a single target, and papers link it to 3 constructs overall. One paper reports a correlation with ambiguity detection ability, observing that higher performance in Correct-Unamb tends to accompany lower performance in Detect-Ambig, and vice versa. Other papers relate coreference resolution to gender bias, saying such biases can be made visible in the task, and to long-context understanding, describing advantages of information extraction and coreference resolution in understanding long contexts.

## Sources

**Coreference resolution** (10 papers: [Are Bert Family Good Instruction Followers? A Study on Their Potential And Limitations](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a13eb0c08247364066e8d86551c3090-Paper-Conference.pdf), [DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/e352b765e625934ce86919995e2371aa-Paper-Conference.pdf), [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf), [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf), [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf), [The Impossibility of Fair LLMs](https://aclanthology.org/2025.acl-long.5.pdf), [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf), [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.208.pdf), [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf), [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf))
> The observable behavior of linking gendered pronouns to their correct antecedent profession in Winograd-style sentences, particularly in stereotypical versus anti-stereotypical contexts.

**Pronoun resolution** (4 papers: [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf), [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf), [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf), [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf))
> The observable task of correctly identifying the antecedent of a pronoun in a sentence, which requires contextual understanding.

**Co-reference resolution** (1 paper: [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf))
> The task of determining which noun phrases or entities in a text refer to the same real-world entity, specifically resolving a pronoun to an occupation.

**Pronoun reference resolution** (1 paper: [COAS2W: A Chinese Older-Adults Spoken-to-Written Transformation Corpus with Context Awareness](https://aclanthology.org/2025.emnlp-main.903.pdf))
> Correctly identifying and resolving ambiguous personal pronouns in spoken utterances by leveraging contextual cues from surrounding sentences.

**Reference resolution** (1 paper: [From Language to Cognition: How LLMs Outgrow the Human Language Network](https://aclanthology.org/2025.emnlp-main.1237.pdf))
> Identifying the correct referent of pronouns or noun phrases within a text.

**Anaphora resolution** (2 papers: [Sheaf Discovery with Joint Computation Graph Pruning and Flexible Granularity](https://aclanthology.org/2025.emnlp-main.446.pdf), [Quantifying the Plausibility of Context Reliance in Neural Machine Translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d3040941a2d57ead4043556a70dd728-Paper-Conference.pdf))
> The general task of determining the referent of an anaphoric expression, such as a pronoun.

**Argument alignment** (1 paper: [Multi-Document Event Extraction Using Large and Small Language Models](https://aclanthology.org/2025.emnlp-main.972.pdf))
> The observable process of matching arguments from different documents to the same underlying referent by evaluating semantic compatibility and coreference cues.

**Pronoun disambiguation** (1 paper: [IG-Pruning: Input-Guided Block Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.537.pdf))
> The task of correctly identifying the antecedent of a pronoun in a sentence, often requiring commonsense understanding.

## Relationships

### Coreference resolution →
- **WinoGrande** (measurement instrument): *measured_by*, 13 papers
  > WinoGrande (Sakaguchi et al., 2019) for conference resolution (Section 4.1).
  - [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf)
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
  - [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf)
  - [Dynamic Fisher-weighted Model Merging via Bayesian Optimization](https://aclanthology.org/2025.naacl-long.254.pdf)
  - [Demystifying Small Language Models for Edge Deployment](https://aclanthology.org/2025.acl-long.718.pdf)
  - [Beyond One-Size-Fits-All: Tailored Benchmarks for Efficient Evaluation](https://aclanthology.org/2025.acl-long.759.pdf)
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
  - [IG-Pruning: Input-Guided Block Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.537.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **WinoBias** (measurement instrument): *measured_by*, 4 papers
  > WinoBias Zhao et al. (2018) present the dataset containing a WinoGrad scheme (Levesque et al., 2011) examples. ... The task is to identify the coreference link between the pronouns and the correct professional. (Section 2.3)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
  - [Prompting Fairness: Integrating Causality to Debias Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f26a2d143a227376dff99a279f93f99-Paper-Conference.pdf)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
  - [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf)
- **WSC** (measurement instrument): *measured_by*, 3 papers
  > “the Winograd Schema Challenge evaluates coreference resolution capabilities (WSC; Levesque et al., 2012)”
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Text summarization** (behavioral indicator): *causes*, 2 papers
  > When addressing tasks involving long-dependency issues, such as summarization... coreference resolution methods demonstrate a clear advantage over other approaches... (Section 5.1)
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
  - [Statistical Deficiency for Task Inclusion Estimation](https://aclanthology.org/2025.acl-long.18.pdf)
- **bAbI** (measurement instrument): *measured_by*, 1 paper
  > The tasks in bAbI vary in the number of facts, question complexity, and the reasoning skills they assess, including spatial and temporal reasoning, deduction, and coreference resolution.
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Question answering** (behavioral indicator): *causes*, 1 paper
  > highlighting the effectiveness of leveraging coreference resolution to bridge context gaps in question answering. (Abstract)
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **SuperGLUE** (measurement instrument): *measured_by*, 1 paper
  > The SuperGLUE benchmark comprises advanced language understanding tasks... coreference resolution (WSC; ())... (Section 4.1)
  - [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf)
- **OntoNotes** (measurement instrument): *measured_by*, 1 paper
  > Evaluation is conducted on five datasets: WikiHop (multi-hop QA), TriviaQA (open QA), OntoNotes (coreference resolution), Hyperpartisan News Detection (long document classification), and HotpotQA (distractor setting, joint F1).
  - [DrDiff: Dynamic Routing Diffusion with Hierarchical Attention for Breaking the Efficiency-Quality Trade-off](https://aclanthology.org/2025.emnlp-main.474.pdf)
- **Relation extraction** (behavioral indicator): *causes*, 1 paper
  > Ablation studies demonstrate that integrating coreference and decomposition increases recall on rare relations by over 20%. (Abstract)
  - [Automated Knowledge Graph Construction using Large Language Models and Sentence Complexity Modelling](https://aclanthology.org/2025.emnlp-main.783.pdf)
- **XWinograd** (measurement instrument): *measured_by*, 1 paper
  > XWinograd (Tikhonov and Ryabinin, 2021): a cross-lingual adaptation of the Winograd Schema challenge5 for coreference resolution evaluation. (Section 4.1)
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf)

### → Coreference resolution
- **Ambiguity detection ability** (construct): *correlates*, 1 paper
  > Across all prompts we observe a persistent tension: high performance in Correct-Unamb tends to be accompanied by lower performance in Detect-Ambig, and vice versa. (Section 6)
  - [Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs](https://aclanthology.org/2025.emnlp-main.1527.pdf)

### Associated with
- **Textual reasoning** (behavioral indicator), 1 paper
  > Natural language reasoning suite consists of 11 benchmarks that involve natural language based reasoning such as Question Answering, natural language inference (NLI), sentence completion, co-reference resolution, and general intelligence.
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **TACT** (measurement instrument), 1 paper
  > Through TACT, the model is implicitly required to address information extraction (IE) challenges such as coreference resolution... (Section 1)
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Long-context understanding** (construct), 1 paper
  > Our method demonstrates the advantages and capabilities of information extraction and coreference resolution in understanding long contexts
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
- **Gender bias** (construct), 1 paper
  > As noted by Davis and van Schijndel (2020), gender biases in neural models can be made visible in coreference resolution. (Section 4)
  - [Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs](https://aclanthology.org/2025.emnlp-main.1527.pdf)
