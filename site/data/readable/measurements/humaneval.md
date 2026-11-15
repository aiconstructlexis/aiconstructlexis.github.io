# HumanEval
**Type:** Measurement instrument  
**Supporting papers:** 309  
**Also known as:** HUMANEVAL, Humaneval, HumanEval-Python, HumanEval-python  

## State of the Field

**What it is.** Across papers, the prevailing description is a Python code generation or code completion benchmark built around functional correctness. Most definitions describe hand-written or hand-crafted programming problems, often 164 in total, with function signatures or docstrings, unit tests, and sometimes reference or canonical Python solutions, evaluated by unit test pass rate, usually pass@1. A smaller line of work refers specifically to HumanEval-Python or HumanEval-python for Python function completion, uses the HumanEvalSynthesize variant, adapts it to a single-line code infilling task, or treats it as the basis for HUMANEVALPACK.

**What it is claimed to measure.** Papers link HumanEval to 12 constructs and 4 behavioral indicators. The prevailing claims are that papers use it to measure code generation and coding ability, with further recurrent uses for reasoning, functional correctness, and code completion. Additional construct and behavioral links are also recorded, so papers do not tie it to only one target concept.

**Space of uses.** Papers explicitly relate it to 2 other instruments, EvalPlus and MultiPL-E, and many evaluations also pair it with MBPP; some additionally mention HumanEval+ or EvalPlus variants. In practice, papers commonly report zero-shot or 0-shot results and pass@1, with some using pass@10, greedy decoding, or the HumanEval automated test harness. Many papers position it as a standard benchmark, and one study says it "has emerged as the standard for this task" (OctoPack: Instruction Tuning Code Large Language Models), though some repurpose it for self-consistency, self-repair, multi-turn interaction, or single-line infilling.

**Concerns raised.** Concern discussion is limited. One paper relates HumanEval to overfitting, stating that its results indicate some level of overfitting to HUMANEVAL.

## Sources

**HumanEval** (35 papers: [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf), [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf), [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf), [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf), [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf), [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf), [L2MAC: Large Language Model Automatic Computer for Extensive Code Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/9e74900c3f6100c56add4bf417547848-Paper-Conference.pdf), [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf), [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a0d3ae989a382ce6e50312bc35bf7e1-Paper-Conference.pdf), [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://proceedings.iclr.cc/paper_files/paper/2024/file/6507b115562bb0a305f1958ccc87355a-Paper-Conference.pdf), [Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/639a9a172c044fbb64175b5fad42e9a5-Paper-Conference.pdf), [OctoPack: Instruction Tuning Code Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1ec299a5229034141e58aeded0d0b9de-Paper-Conference.pdf), [Predicting Emergent Abilities with Infinite Resolution Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e6d14709eae0cbc49a1d19d87fb8b21-Paper-Conference.pdf), [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bbf38332580c1bed99fa99bc9ee53229-Paper-Conference.pdf), [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf), [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf), [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf), [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf), [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf), [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf), [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.336.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf), [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf), [MoDification: Mixture of Depths Made Easy](https://aclanthology.org/2025.naacl-long.265.pdf), [mHumanEval - A Multilingual Benchmark to Evaluate Large Language Models for Code Generation](https://aclanthology.org/2025.naacl-long.570.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf), [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf), [Tree-of-Evolution: Tree-Structured Instruction Evolution for Code Generation in Large Language Models](https://aclanthology.org/2025.acl-long.14.pdf), [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf), [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf))
> A code generation benchmark that evaluates functional correctness of generated code via unit test pass rate, using the Pass@1 metric.

**HUMANEVAL** (1 paper: [Can LLMs Implicitly Learn Numeric Parameter Constraints in Data Science APIs?](https://proceedings.neurips.cc/paper_files/paper/2024/file/617ffb01ea5b57769b0d63d5e9fefd3f-Paper-Conference.pdf))
> A popular benchmark for evaluating the functional correctness of code generated by large language models.

**Humaneval** (1 paper: [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf))
> A benchmark for evaluating the functional correctness of code generated by language models, used here for a single-line code infilling task.

**HumanEval-Python** (1 paper: [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf))
> A benchmark for evaluating code generation models on Python function completion tasks.

**HumanEval-python** (1 paper: [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf))
> A benchmark for evaluating code generation in Python, consisting of handwritten programming problems.

## Relationships

### → HumanEval
- **Code generation** (behavioral indicator): *measured_by*, 131 papers
  > We evaluate SEC in the following tasks and datasets (details in Appendix A.1): ... Code Generation: HumanEval (Chen et al., 2021). (Section 3.1)
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
  - [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://proceedings.iclr.cc/paper_files/paper/2024/file/72eba29737f9c3a5a4ce8cdb7b667145-Paper-Conference.pdf)
  - [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf)
  - [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf)
  - [Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bc4f74e35bcfe8cfe43b0a860786d6a-Paper-Conference.pdf)
  - [Parameter Competition Balancing for Model Merging](https://proceedings.neurips.cc/paper_files/paper/2024/file/99fc8bc48b917c301a80cb74d91c0c06-Paper-Conference.pdf)
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
  - [Can Large Language Models Analyze Graphs like Professionals? A Benchmark, Datasets and Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff417c3993894694e88ffc4d3f53d28b-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Unchosen Experts Can Contribute Too: Unleashing MoE Models’ Power by Self-Contrast](https://proceedings.neurips.cc/paper_files/paper/2024/file/f77012b463892a3f2ac56d3a6086fc5b-Paper-Conference.pdf)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [Judge Decoding: Faster Speculative Sampling Requires Going Beyond Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/656d6174fd5ffb01c843f269649ab5cb-Paper-Conference.pdf)
  - [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf)
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
  - [Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c40bed606c51c8e827c1ba75aa2da054-Paper-Conference.pdf)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
  - [InstructRAG: Instructing Retrieval-Augmented Generation via Self-Synthesized Rationales](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdce0de17dc3cf97019a35baa65aebd0-Paper-Conference.pdf)
  - [Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d022216357816e483433914204aa80ee-Paper-Conference.pdf)
  - [Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
  - [Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf)
  - [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf)
  - [PEARL: Parallel Speculative Decoding with Adaptive Draft Length](https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf)
  - [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [Mixture of Attentions For Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/f31bf160569618084ba9bdc2a8de29d0-Paper-Conference.pdf)
  - [Model Equality Testing: Which Model is this API Serving?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d73234a13815fc1f9779dd17d89be9b4-Paper-Conference.pdf)
  - [AFlow: Automating Agentic Workflow Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5492ecbce4439401798dcd2c90be94cd-Paper-Conference.pdf)
  - [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf)
  - [Learning Harmonized Representations for Speculative Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/575286a73f238b6516ce0467d67eadb2-Paper-Conference.pdf)
  - [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf)
  - [Distributed Speculative Inference (DSI): Speculation Parallelism for Provably Faster Lossless Language Model Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/b36554b97da741b1c48c9de05c73993e-Paper-Conference.pdf)
  - [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbc461518c59a2a8d64e70e2c38c4a0e-Paper-Conference.pdf)
  - [Training Language Models to Self-Correct via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf)
  - [The Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/9aa4e5caaf6d62767787500ee487c7fb-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Leveraging Submodule Linearity Enhances Task Arithmetic Performance in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c983bf84ddbf8c71b2fd19a9d48186b-Paper-Conference.pdf)
  - [Commit0: Library Generation from Scratch](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fcefa894924bb1688041b7a26fb8aea-Paper-Conference.pdf)
  - [MergeME: Model Merging Techniques for Homogeneous and Heterogeneous MoEs](https://aclanthology.org/2025.naacl-long.117.pdf)
  - [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf)
  - [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf)
  - [mHumanEval - A Multilingual Benchmark to Evaluate Large Language Models for Code Generation](https://aclanthology.org/2025.naacl-long.570.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
  - [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf)
  - [Mastering the Craft of Data Synthesis for CodeLLMs](https://aclanthology.org/2025.naacl-long.620.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
  - [Fusing Highly Specialized Language Models for Comprehensive Expertise](https://aclanthology.org/2025.acl-long.42.pdf)
  - [Faster Speculative Decoding via Effective Draft Decoder with Pruned Candidate Tree](https://aclanthology.org/2025.acl-long.486.pdf)
  - [“Give Me BF16 or Give Me Death”? Accuracy-Performance Trade-Offs in LLM Quantization](https://aclanthology.org/2025.acl-long.1304.pdf)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1506.pdf)
  - [Refining Salience-Aware Sparse Fine-Tuning Strategies for Language Models](https://aclanthology.org/2025.acl-long.1541.pdf)
  - [Neural Incompatibility: The Unbridgeable Gap of Cross-Scale Parametric Knowledge Transfer in Large Language Models](https://aclanthology.org/2025.acl-long.1047.pdf)
  - [LESA: Learnable LLM Layer Scaling-Up](https://aclanthology.org/2025.acl-long.1095.pdf)
  - [MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.240.pdf)
  - [WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models](https://aclanthology.org/2025.acl-long.246.pdf)
  - [Learning to Reason from Feedback at Test-Time](https://aclanthology.org/2025.acl-long.262.pdf)
  - [Watermarking Large Language Models: An Unbiased and Low-risk Method](https://aclanthology.org/2025.acl-long.391.pdf)
  - [SPECTRA: Faster Large Language Model Inference with Optimized Internal and External Speculation](https://aclanthology.org/2025.acl-long.685.pdf)
  - [Adapt Once, Thrive with Updates: Transferable Parameter-Efficient Fine-Tuning on Evolving Base Models](https://aclanthology.org/2025.acl-long.719.pdf)
  - [IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory](https://aclanthology.org/2025.acl-long.761.pdf)
  - [LongRecipe: Recipe for Efficient Long Context Generalization in Large Language Models](https://aclanthology.org/2025.acl-long.581.pdf)
  - [BeamLoRA: Beam-Constraint Low-Rank Adaptation](https://aclanthology.org/2025.acl-long.582.pdf)
  - [SAM Decoding: Speculative Decoding via Suffix Automaton](https://aclanthology.org/2025.acl-long.595.pdf)
  - [Planning-Driven Programming: A Large Language Model Programming Workflow](https://aclanthology.org/2025.acl-long.621.pdf)
  - [SCAR: Data Selection via Style Consistency-Aware Response Ranking for Efficient Instruction-Tuning of Large Language Models](https://aclanthology.org/2025.acl-long.625.pdf)
  - [Qwen2.5-xCoder: Multi-Agent Collaboration for Multilingual Code Instruction Tuning](https://aclanthology.org/2025.acl-long.642.pdf)
  - [ImPart: Importance-Aware Delta-Sparsification for Improved Model Compression and Merging in LLMs](https://aclanthology.org/2025.acl-long.921.pdf)
  - [CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/min25b/min25b.pdf)
  - [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf)
  - [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf)
  - [LoRA-One: One-Step Full Gradient Could Suffice for Fine-Tuning Large Language Models, Provably and Efficiently](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ax/zhang25ax.pdf)
  - [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf)
  - [Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf)
  - [Synthesizing Software Engineering Data in a Test-Driven Manner](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cn/zhang25cn.pdf)
  - [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cu/zhang25cu.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
  - [Automated Benchmark Generation for Repository-Level Coding Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vergopoulos25a/vergopoulos25a.pdf)
  - [Gumiho: A Hybrid Architecture to Prioritize Early Tokens in Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dg/li25dg.pdf)
  - [Boosting Multi-Domain Fine-Tuning of Large Language Models through Evolving Interactions between Samples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25q/liang25q.pdf)
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
  - [SeedLoRA: A Fusion Approach to Efficient LLM Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25o/liu25o.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
  - [LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf)
  - [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://raw.githubusercontent.com/mlresearch/v267/main/assets/magnusson25a/magnusson25a.pdf)
  - [Make LoRA Great Again: Boosting LoRA with Adaptive Singular Values and Mixture-of-Experts Optimization Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fan25g/fan25g.pdf)
  - [Fast Large Language Model Collaborative Decoding via Speculation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25c/fu25c.pdf)
  - [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aa/chen25aa.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ay/huang25ay.pdf)
  - [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf)
  - [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ko25a/ko25a.pdf)
  - [EpiCoder: Encompassing Diversity and Complexity in Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bi/wang25bi.pdf)
  - [NICE Data Selection for Instruction Tuning in LLMs with Non-differentiable Evaluation Metric](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bm/wang25bm.pdf)
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
  - [EcoTune: Token-Efficient Multi-Fidelity Hyperparameter Optimization for Large Language Model Inference](https://aclanthology.org/2025.emnlp-main.394.pdf)
  - [Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment](https://aclanthology.org/2025.emnlp-main.406.pdf)
  - [Alignment with Fill-In-the-Middle for Enhancing Code Generation](https://aclanthology.org/2025.emnlp-main.419.pdf)
  - [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://aclanthology.org/2025.emnlp-main.932.pdf)
  - [Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality](https://aclanthology.org/2025.emnlp-main.1138.pdf)
  - [Compound AI Systems Optimization: A Survey of Methods, Challenges, and Future Directions](https://aclanthology.org/2025.emnlp-main.1463.pdf)
  - [CLMTracing: Black-box User-level Watermarking for Code Language Model Tracing](https://aclanthology.org/2025.emnlp-main.1475.pdf)
  - [Not-Just-Scaling Laws: Towards a Better Understanding of the Downstream Impact of Language Model Design Decisions](https://aclanthology.org/2025.emnlp-main.830.pdf)
  - [Dovetail: A CPU/GPU Heterogeneous Speculative Decoding for LLM inference](https://aclanthology.org/2025.emnlp-main.879.pdf)
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [Group-Aware Reinforcement Learning for Output Diversity in Large Language Models](https://aclanthology.org/2025.emnlp-main.1649.pdf)
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
  - [ReSo: A Reward-driven Self-organizing LLM-based Multi-Agent System for Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.808.pdf)
  - [ZERA: Zero-init Instruction Evolving Refinement Agent – From Zero Instructions to Structured Prompts via Principle-based Optimization](https://aclanthology.org/2025.emnlp-main.1190.pdf)
  - [Firewall Routing: Blocking Leads to Better Hybrid Inference for LLMs](https://aclanthology.org/2025.emnlp-main.331.pdf)
  - [Invisible Entropy: Towards Safe and Efficient Low-Entropy LLM Watermarking](https://aclanthology.org/2025.emnlp-main.341.pdf)
  - [Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning](https://aclanthology.org/2025.emnlp-main.350.pdf)
  - [Arena-lite: Efficient and Reliable Large Language Model Evaluation via Tournament-Based Direct Comparisons](https://aclanthology.org/2025.emnlp-main.360.pdf)
  - [AnyMAC: Cascading Flexible Multi-Agent Collaboration via Next-Agent Prediction](https://aclanthology.org/2025.emnlp-main.584.pdf)
  - [Understanding the Information Propagation Effects of Communication Topologies in LLM-based Multi-Agent Systems](https://aclanthology.org/2025.emnlp-main.623.pdf)
  - [Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLMs](https://aclanthology.org/2025.emnlp-main.1754.pdf)
- **Coding ability** (construct): *measured_by*, 14 papers
  > In this ection, we first assess the agents’ coding capabilities using the Humaneval code completion dataset. (Section 3.2)
  - [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
  - [$\texttt{Model-GLUE}$: Democratized LLM Scaling for A Large Model Zoo in the Wild](https://proceedings.neurips.cc/paper_files/paper/2024/file/180a476f22a52b8ef14f42b2b927afcc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf)
  - [Scaling Large Language Model-based Multi-Agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
  - [MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf)
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
  - [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf)
  - [StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf)
  - [From Informal to Formal – Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs](https://aclanthology.org/2025.acl-long.1310.pdf)
  - [Large Language Models to Diffusion Finetuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cetin25a/cetin25a.pdf)
  - [CopySpec: Accelerating LLMs with Speculative Copy-and-Paste](https://aclanthology.org/2025.emnlp-main.1337.pdf)
- **Reasoning** (construct): *measured_by*, 4 papers
  > HumanEval ... a coding task that requires complex reasoning and planning ability.
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
  - [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aa/chen25aa.pdf)
- **Functional correctness** (construct): *measured_by*, 3 papers
  > HumanEval assesses the functional correctness of synthesized code derived from docstrings. (Section 4.2)
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Black-Box Adversarial Attacks on LLM-Based Code Completion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jenko25a/jenko25a.pdf)
  - [SolEval: Benchmarking Large Language Models for Repository-level Solidity Smart Contract Generation](https://aclanthology.org/2025.emnlp-main.218.pdf)
- **Code completion** (behavioral indicator): *measured_by*, 2 papers
  > HumanEval [3] is a code completion benchmark consisting of programming problems assessing language comprehension, algorithms, and simple mathematics (Section 4.1).
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
  - [PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25m/hu25m.pdf)
- **Natural language understanding** (construct): *measured_by*, 2 papers
  > HumanEval [6] is a dataset for evaluating code generation ability, containing 164 manually crafted programming problems covering aspects such as language understanding, reasoning, algorithms, and simple mathematics.
  - [Parameter Competition Balancing for Model Merging](https://proceedings.neurips.cc/paper_files/paper/2024/file/99fc8bc48b917c301a80cb74d91c0c06-Paper-Conference.pdf)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > As shown in Appendix E.2, we assessed each iteration’s performance on general benchmarks, including GSM8k (Cobbe et al., 2021), TriviaQA (Joshi et al., 2017), MMLU (Hendrycks et al., 2020), and HumanEval (Chen et al., 2021). (Section 3.3)
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > Among these, AIME-2024, HumanEval, HumanEval+, GPQA, and SciBench are from a totally different distributions compared to training data, serving to verify the generalization capability of MAS-GPT. (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **Knowledge retention** (construct): *measured_by*, 1 paper
  > Besides, to verify whether HRA can better retain pre-training knowledge, we fine-tune LLaMA-2 7B on the MATHQA dataset by LoRA and HRA, respectively, and check the degradation of model performance on classic NLP tasks, including typical language tasks in ARC [55], HellaSwag [58], MMLU [17], Winogrande [42], and a coding task in HumanEval [6]. (Section 4.2)
  - [Bridging The Gap between Low-rank and Orthogonal Adaptation via Householder Reflection Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator): *measured_by*, 1 paper
  > we evaluated forgetting on coding tasks with HumanEval Chen et al. (2021), observing some degradation. (Section 6)
  - [Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf)
- **Self-correction ability** (construct): *measured_by*, 1 paper
  > We evaluate self-correction capability on both classification and generation tasks, including domains in mathematics, coding, instruction following, common-sense reasoning, and knowledge. To be specific, the dataset we utilized include ... Humaneval (Chen et al., 2021)... (Section 4.1)
  - [Confidence v.s. Critique: A Decomposition of Self-Correction Capability for LLMs](https://aclanthology.org/2025.acl-long.203.pdf)
- **Chain-of-thought reasoning** (construct): *measured_by*, 1 paper
  > challenging multi-step reasoning tasks such as ... HumanEval (All, 0-shot) (Chen et al., 2021). (Section 4.1)
  - [QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.240.pdf)
- **Semantic understanding** (construct): *measured_by*, 1 paper
  > “HumanEval is driven most by Semantic Relationship, aligning with the need to interpret function specifications precisely”
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
- **Text generation quality** (construct): *measured_by*, 1 paper
  > To validate that MTJD indeed betters output quality, we test MTJD (k=4) and standard multinomial sampling on Spider, MTBench, and HumanEval using the Llama-3 series models. ... For this process, the higher the scores, the better the downstream performance. (Section 5.1)
  - [Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf)
- **Code debugging** (behavioral indicator): *measured_by*, 1 paper
  > In this paper, we analyze Code Llama, GPT-3.5 and GPT-4’s ability to perform self-repair on problems taken from HumanEval and APPS.
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)

### Associated with
- **EvalPlus** (measurement instrument), 1 paper
  > Finally, we conduct a detailed evaluation (Sec. 3) against a range of state-of-the-art models known for their strong performance on the EvalPlus [48] benchmark (an improved version of HumanEval). (Introduction)
  - [IaC-Eval: A Code Generation Benchmark for Cloud Infrastructure-as-Code Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26b29298ae8acd94bd7e839688e329b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Overfitting** (construct), 1 paper
  > This indicates some level of overfitting to HUMANEVAL.
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **MultiPL-E** (measurement instrument), 1 paper
  > It extends HumanEval and MBPP (Austin et al., 2021) to support 18 programming languages.
  - [SolEval: Benchmarking Large Language Models for Repository-level Solidity Smart Contract Generation](https://aclanthology.org/2025.emnlp-main.218.pdf)
