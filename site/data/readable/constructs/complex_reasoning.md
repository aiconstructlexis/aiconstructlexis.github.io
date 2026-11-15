# Complex reasoning
**Type:** Construct  
**Supporting papers:** 21  
**Also known as:** Multi-step inference, Higher-order reasoning, Deep reasoning, Advanced reasoning, Composite reasoning, Long-chain reasoning, Multi-hop deduction  

## State of the Field

**Space of definitions.** Across papers, the prevailing framing treats complex reasoning as a multi-step or multi-hop capacity: solving complex questions or tasks by deriving intermediate conclusions, integrating multiple pieces of knowledge, or satisfying multiple constraints. Definitions often place it beyond basic information retrieval or simple pattern matching, and some sharpen this further as long chains where any single-step error can break the final answer, or as reasoning that must track links across modalities or facts. A smaller line of work treats it more behaviorally, as an observable multi-hop deduction task from a given context rather than only as a latent model capability.

**Space of facets.** Papers use several overlapping labels for nearby variants, including higher-order, deep, long-chain, and advanced reasoning, and these labels are described in terms of multi-step processing rather than simple retrieval. Some papers carve out composite reasoning as questions that combine distinct categories, such as fluent tracking with action executability, while multi-hop deduction appears as a narrower task form, including a 3-hop deduction setting from assumptions. Across these usages, papers distinguish the idea by whether they emphasize multiple constraints, multiple facts or knowledge pieces, multiple modalities, or combinations of reasoning categories.

**Space of measurement.** Operationalization is benchmark-heavy: papers link the construct to 7 measurement instruments and 2 behavioral indicators, with BIG-Bench Hard, MATH, GSM8K, CLEVR, and HotpotQA among the most frequently linked instruments, plus 2 others. The linked instruments are task benchmarks, used for arduous reasoning situations, competition-level or step-by-step math problems, real-user tasks with multiple constraints, agent tasks centered on complex reasoning, and other benchmarked settings. This largely matches the dominant definitions around multi-step inference and multiple constraints, though much of the measurement space instantiates the construct as benchmark performance, especially in mathematical settings.

**Links.** Several papers relate complex reasoning to mathematical reasoning, and one says mathematical ability 'serves as a fundamental measure' of problem-solving and complex reasoning skills; single papers also relate it to commonsense reasoning and to the step-by-step process used in chain-of-thought reasoning. Single papers claim causal relationships from analogical reasoning and multi-step planning to complex reasoning, with one other causal antecedent and 2 related behavioral indicators also reported. No correlational links are reported.

## Sources

**Multi-step inference** (1 paper: [MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf))
> Producing an output that depends on correctly deriving intermediate conclusions from a chain of premises, where each step relies on the previous one.

**Higher-order reasoning** (1 paper: [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf))
> The capacity to engage in complex cognitive processes that go beyond basic information retrieval, involving multiple steps or constraints.

**Deep reasoning** (1 paper: [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf))
> The ability to solve complex questions by integrating multiple pieces of knowledge through multi-step inference.

**Advanced reasoning** (1 paper: [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to perform complex cognitive operations beyond simple pattern matching, which is required for difficult tasks like forecasting and text generation.

**Composite reasoning** (1 paper: [ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf42f133f355e0e07a8957b508b26a1b-Paper-Conference.pdf))
> The ability to solve complex problems by integrating multiple distinct reasoning steps or categories, such as combining fluent tracking with action executability.

**Long-chain reasoning** (1 paper: [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf))
> The capability to perform tasks that require numerous sequential steps, where errors in any single step can lead to an incorrect final outcome.

**Multi-hop deduction** (1 paper: [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf))
> The observable task of solving a problem that requires chaining together multiple steps of inference or information retrieval from a given context.

## Relationships

### Complex reasoning →
- **MATH** (measurement instrument): *measured_by*, 3 papers
  > Experiments are further carried out on the mathematical competition benchmark, MATH (Hendrycks et al., 2021b), achieving a +6.0 improvement with GPT-4, indicating that FUNCODER can also generalize to complex reasoning. (Introduction)
  - [Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bc4f74e35bcfe8cfe43b0a860786d6a-Paper-Conference.pdf)
  - [Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4006ff54a7bbda74c09bad6f7586f5b-Paper-Conference.pdf)
  - [Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning](https://aclanthology.org/2025.naacl-long.515.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 3 papers
  > BBH (Suzgun et al., 2023) encompasses 27 arduous tasks to assess whether the model can handle complex reasoning situations.
  - [Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf)
  - [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf)
  - [Beyond Similarity: A Gradient-based Graph Method for Instruction Tuning Data Selection](https://aclanthology.org/2025.acl-long.1189.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 2 papers
  > For complex reasoning, we use the GSM8K dataset (Cobbe et al., 2021), which contains linguistically diverse grade school math world problems with step-by-step solutions.
  - [Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
  - [CommVQ: Commutative Vector Quantization for KV Cache Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25du/li25du.pdf)
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > Complex real-user tasks usually have multiple constraints and require higher-order reasoning skills, which are well represented in WILDBENCH. (Figure 1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Omni-MATH** (measurement instrument): *measured_by*, 1 paper
  > We introduce Omni-Math, a universal Olympiad-level mathematical benchmark with over 33 sub-domains and diverse difficulty levels, posing new challenges to the problem solving and complex reasoning capability of LLMs. (Section 1)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
- **CLEVR** (measurement instrument): *measured_by*, 1 paper
  > complex reasoning in CLEVR (Johnson et al., 2017) and Winoground (Thrush et al., 2022) (Section 4.1).
  - [VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models](https://aclanthology.org/2025.naacl-long.192.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > “We conduct experiments on three representative agent tasks: Complex Reasoning (HotpotQA (Yang et al., 2018)), Embodied Decision (ALFWorld (Shridhar et al., 2020)), and Interactive Programming (InterCode (Yang et al., 2023))”
  - [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf)

### → Complex reasoning
- **Analogical reasoning** (construct): *causes*, 1 paper
  > we advance the traditional analogical reasoning and propose a novel Thought Propagation (TP) framework to amend existing reasoning-from-scratch methods and enhance the complex reasoning ability of LLMs.
  - [THOUGHT PROPAGATION: AN ANALOGICAL APPROACH TO COMPLEX REASONING WITH LARGE LANGUAGE MODELS](https://proceedings.iclr.cc/paper_files/paper/2024/file/2dae7d1ccf1edf76f8ce7c282bdf4730-Paper-Conference.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > an adaptive self-improvement agentic system that enables LLMs to perform such complex reasoning under limited data by iteratively improving their capability through self-generated experience. (Abstract)
  - [Adaptive Self-improvement LLM Agentic System for ML Library Development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25at/zhang25at.pdf)
- **Multi-step planning** (construct): *causes*, 1 paper
  > Our detailed analysis demonstrates how planning trajectories improves complex reasoning capabilities, showing that PLAN-TUNING is an effective strategy for improving task-specific performance of smaller LLMs. (Abstract)
  - [PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1087.pdf)

### Associated with
- **Mathematical reasoning** (construct), 3 papers
  > Long-chain reasoning task (Wei et al., 2022; Xiong et al., 2024), such as commonsense reasoning and math reasoning, is one of the critical capabilities in large language models (LLMs) (Lai et al., 2024).
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
  - [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf)
- **Commonsense reasoning** (construct), 1 paper
  > Long-chain reasoning task (Wei et al., 2022; Xiong et al., 2024), such as commonsense reasoning and math reasoning, is one of the critical capabilities in large language models (LLMs) (Lai et al., 2024).
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct), 1 paper
  > The step-by-step long-chain reasoning process is most famously used in Chain-of-Thought (CoT) (Wei et al., 2022).
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
- **Document question answering** (behavioral indicator), 1 paper
  > HOMER also improves the prediction accuracy on question answering by 3% (32.7% →35.7%), presenting its capability to perform complex reasoning about the content in the extended context length.
  - [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf)
- **Sudoku solving** (behavioral indicator), 1 paper
  > The Sudoku environment is a highly challenging Constraint Satisfaction Problem (CSP) and determining the value in even a single cell can require highly complex reasoning involving multiple steps. (Section 1)
  - [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf)
