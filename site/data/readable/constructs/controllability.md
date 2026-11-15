# Controllability
**Type:** Construct  
**Supporting papers:** 69  
**Also known as:** Generation control, Controllable generation, Control, Controlled generation, Controllable context sensitivity, Prompt steerability, Behavioral control, Targeted control, Model steering, Multi-attribute control, Steerability  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats controllability as a model's capacity to be steered at inference or generation time so its outputs match task requirements, user intents, desired attributes, or explicit constraints. In this dominant framing, control is exercised through prompts, high-level instructions, or adjustable parameters, and papers describe users as being able to customize behavior at test time or steer it through prompting alone. A smaller line of work narrows the concept to specific targets such as output modality, length or information density, syntactic or semantic constraints, value prioritization, truthfulness, demographic opinions, or the tradeoff between context and prior knowledge. Another minority framing shifts the property from outputs to internal states, defining control as editing or intervening on internal representations while preserving other relevant attributes, or as regulating capabilities during training.

**Space of facets.** Papers subdivide this family of ideas into prompt steerability, controllable context sensitivity, behavioral control, targeted control, model steering, and multi-attribute control. They also use nearby labels, steerability, controllability, controllable generation, controlled generation, generation control, and control, for different targets: prompt-based persona adoption, adaptation to demographic value profiles or truthfulness instructions, compliance with syntax, semantics, length, emotion, dialog-act, CEFR level, or CAD hierarchy constraints, and interventions on latent representations. Across these usages, the recurring overlap is user-directed modulation, but the target of control varies between model behavior, output attributes, processing pipelines, and internal representations.

**Space of measurement.** Operationally, controllability is linked to 4 measurement instruments and 2 behavioral indicators. The named instruments are AlpacaEval and STEER-BENCH, both benchmarks, Human evaluation, where outputs are ranked by how well they reflect intended descriptions, and LLM-as-a-judge, used to rate steered outputs on relevant axes; the linked behavioral indicators are Role-playing and Self-reflection, though they appear through related and causal claims rather than as direct measures. Overall, the linked operationalizations emphasize output-level adherence to prompts, descriptions, or steering goals, which matches the dominant inference-time and constraint-following definitions; no probe-based instrument is named.

**Links.** Papers claim causal relationships from Interpretability and explainability, Self-reflection, and Disentanglement to controllability. One paper says generating reflection tokens makes the language model controllable during inference, and several papers claim a causal relationship from interpretability and explainability to controllability, while some other papers relate the two without making a causal claim. Separately, controllability is related to In-context learning, Role-playing, Generation diversity, and Truthfulness. No correlational link is reported.

## Sources

**Steerability** (8 papers: [Motif: Intrinsic Motivation from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/a8de97fa77a09258b22880c230a83445-Paper-Conference.pdf), [OctoPack: Instruction Tuning Code Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1ec299a5229034141e58aeded0d0b9de-Paper-Conference.pdf), [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf), [DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life](https://proceedings.iclr.cc/paper_files/paper/2025/file/8587069d00a69d0ea498d547fffad6dd-Paper-Conference.pdf), [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf), [Benchmarking Distributional Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.2.pdf), [Text-to-LoRA: Instant Transformer Adaption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/charakorn25a/charakorn25a.pdf), [Value Profiles for Encoding Human Variation](https://aclanthology.org/2025.emnlp-main.106.pdf))
> The extent to which a model can be directed to produce outputs in different modalities (code or natural language) based on the task requirements specified in the input.

**Controllability** (12 papers: [COLLIE: Systematic Construction of Constrained Text Generation Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/a77eadda332b6d4a9ae1e0e4024555f2-Paper-Conference.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf), [Language-Driven Interactive Traffic Trajectory Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/8e63972d4d9d81b31459d787466ce271-Paper-Conference.pdf), [FlexCAD: Unified and Versatile Controllable CAD Generation with Fine-tuned Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/090b23d52bc2722eef2fbf79c5ebf9ec-Paper-Conference.pdf), [Beyond End-to-End VLMs: Leveraging Intermediate Text Representations for Superior Flowchart Understanding](https://aclanthology.org/2025.naacl-long.180.pdf), [Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.497.pdf), [Aligning Sentence Simplification with ESL Learner's Proficiency for Language Acquisition](https://aclanthology.org/2025.naacl-long.21.pdf), [Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts](https://aclanthology.org/2025.naacl-long.18.pdf), [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf), [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf), [JI2S: Joint Influence-Aware Instruction Data Selection for Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.26.pdf))
> The ability to customize a model’s behavior at inference time through adjustable parameters, such as weights on critique signals or retrieval thresholds.

**Generation control** (1 paper: [GameTraversalBenchmark: Evaluating Planning Abilities Of Large Language Models Through Traversing 2D Game Maps](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852c8254bc6d904c09db9921157f59b-Paper-Datasets_and_Benchmarks_Track.pdf))
> The latent capacity to regulate output generation so that produced actions remain valid, syntactically correct, and constraint-compliant.

**Controllable generation** (2 papers: [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf), [SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models](https://aclanthology.org/2025.emnlp-main.112.pdf))
> The ability of a model to modulate its output's characteristics, such as length or information density, based on explicit conditioning.

**Control** (1 paper: [Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/53356aebeea8ffd40a8ac3bb66243162-Paper-Conference.pdf))
> The extent to which internal representations can be edited to change a targeted attribute while leaving other relevant attributes unchanged.

**Controlled generation** (1 paper: [Syntactic and Semantic Control of Large Language Models via Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf))
> The ability of a language model to produce text that is guided by and conforms to a given set of syntactic or semantic constraints.

**Controllable context sensitivity** (1 paper: [Controllable Context Sensitivity and the Knob Behind It](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9d780d1e2d57d4b70e807608a72501b-Paper-Conference.pdf))
> The ability of a language model to deliberately and controllably trade off its reliance on provided context versus its internal prior knowledge when making predictions.

**Prompt steerability** (1 paper: [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf))
> The latent ability of a model to shift its behavioral distribution from its baseline in response to prompting, reflecting how easily it can be shaped to reflect different personas across dimensions and directions.

**Behavioral control** (1 paper: [A Checks-and-Balances Framework for Context-Aware Ethical AI Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25a/chang25a.pdf))
> The latent ability to guide and correct linguistic behaviors in LLM outputs through structured oversight, ensuring compliance with ethical guardrails without compromising knowledge integrity.

**Targeted control** (1 paper: [Targeted control of fast prototyping through domain-specific interface](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25h/shi25h.pdf))
> The latent ability of a model or system to accurately and precisely implement a user's design intention without under- or over-specification, maintaining alignment between high-level intent and low-level execution.

**Model steering** (1 paper: [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf))
> The latent ability to causally influence a language model's output behavior by intervening on its internal representations to incorporate a specific concept.

**Multi-attribute control** (1 paper: [ECO Decoding: Entropy-Based Control for Controllability and Fluency in Controllable Dialogue Generation](https://aclanthology.org/2025.emnlp-main.1437.pdf))
> The model's latent capacity to simultaneously satisfy multiple desired attributes in generated responses without interference or degradation in performance.

## Relationships

### Controllability →
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > To complement this, we conduct a Human Evaluation, where outputs are ranked based on how well they reflect the intended text descriptions. (Section 5.1.3)
  - [BRIDGE: Bootstrapping Text to Control Time-Series Generation via Multi-Agent Iterative Optimization and Diffusion Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ah/li25ah.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > For the latter, we use an LLM judge to rate steered outputs on three relevant axes (see §3.3).
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 1 paper
  > For evaluating steering, we use the instructions from the Alpaca-Eval dataset (Li et al., 2023).
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **STEER-BENCH** (measurement instrument): *measured_by*, 1 paper
  > we introduce STEER-BENCH, a benchmark designed to evaluate population-specific steering in LLMs. (Section 1)
  - [STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models](https://aclanthology.org/2025.emnlp-main.925.pdf)

### → Controllability
- **Interpretability and explainability** (construct): *causes*, 4 papers
  > By embedding interpretability directly into the LLMs, we enable greater transparency, steering, and control over their behavior.
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
  - [SafetyAnalyst: Interpretable, Transparent, and Steerable Safety Moderation for AI Behavior](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bw/li25bw.pdf)
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Self-reflection** (behavioral indicator): *causes*, 1 paper
  > Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements. (ABSTRACT)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
- **Disentanglement** (construct): *causes*, 1 paper
  > attributes relevant to the task are disentangled in a way that allows precise control over model behavior; (Section 1)
  - [Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/53356aebeea8ffd40a8ac3bb66243162-Paper-Conference.pdf)

### Associated with
- **In-context learning** (construct), 1 paper
  > The prompt steerability of a model is related to how well a model can learn from in-context examples (Brown, 2020; Wies et al., 2024). (Section 1.1)
  - [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf)
- **Role-playing** (behavioral indicator), 1 paper
  > Prompt steerability of a model’s persona describes the degree to which a model can be made to adopt different personas by prompting alone. (Section 3)
  - [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf)
- **Generation diversity** (construct), 1 paper
  > Recent advancements in DPO focus on mainly two directions: efficiency i.e., further simplifying the constraints of DPO, and controllability i.e., keeping the balance between alignment and generation diversity. (Section 1. Introduction)
  - [Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf)
- **Truthfulness** (construct), 1 paper
  > GPT-4o shows a 40% increase in truthfulness when prompted, and this pattern is observed across most models, with the stronger models exhibiting more pronounced shifts toward truthfulness. (Section 5.3)
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf)
