# IFEval
**Type:** Measurement instrument  
**Supporting papers:** 91  

## State of the Field

**What it is.** Across the surveyed papers, IFEval is most commonly described as a targeted benchmark for instruction following, often framed as evaluating whether a model follows explicit instructions or satisfies verifiable prompt constraints. Several definitions make those constraints concrete as format, style, content, or formatting requirements, and one paper places it in the TÜLU-2 evaluation suite under zero-shot settings. A smaller line of work uses adapted forms, including a synthesized spoken version derived from the original text-based IFEval and single-turn tasks adapted from IFEval data.

**What it is claimed to measure.** Papers use IFEval predominantly to measure instruction following: it is linked to one behavioral indicator, Instruction following, and to five constructs, with Instruction following ability as the prevailing construct-level framing. Smaller lines of work also use it to measure Helpfulness, Self-correction ability, Utility preservation, and World knowledge. The recorded measurement claims converge most clearly on instruction following, while the remaining construct links are distributed across several other framings.

**Space of uses.** In use, papers usually treat IFEval as a main instruction-following evaluation, pairing it with other benchmarks such as AlpacaEval 2.0, FollowBench, MMLU, GSM8K, and MT-Bench, and some authors describe it as a general capability indicator. One paper says it uses the dataset's built-in evaluation methodology for consistency, while others adapt it for spoken evaluation or for single-turn tasks. It has direct links to two other instruments: ComplexBench is reported to correlate with IFEval, and IFEval is related to LiveBench, which one paper presents as containing harder, contamination-limited versions of tasks from earlier benchmarks such as IFEval.

**Concerns raised.** One paper reports that ComplexBench performance is well correlated with IFEval, but model rankings on ComplexBench do not entirely correspond with rankings on the other compared benchmarks. Another paper relates IFEval to LiveBench by describing the latter as containing harder, contamination-limited versions of tasks from earlier benchmarks such as IFEval.

## Sources

**IFEval** (14 papers: [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf), [Self-Pluralising Culture Alignment for Large Language Models](https://aclanthology.org/2025.naacl-long.350.pdf), [IHEval: Evaluating Language Models on Following the Instruction Hierarchy](https://aclanthology.org/2025.naacl-long.425.pdf), [A Systematic Examination of Preference Learning through the Lens of Instruction-Following](https://aclanthology.org/2025.naacl-long.552.pdf), [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf), [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf), [GAPO: Learning Preferential Prompt through Generative Adversarial Policy Optimization](https://aclanthology.org/2025.acl-long.13.pdf), [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf), [A Systematic Analysis of Base Model Choice for Reward Modeling](https://aclanthology.org/2025.emnlp-main.8.pdf), [Benchmarking Complex Instruction-Following with Multiple Constraints Composition](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8c24b08b96a08ec7a7a975feea7777e-Paper-Datasets_and_Benchmarks_Track.pdf), [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf), [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf), [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf))
> A targeted benchmark specifically designed to evaluate an LLM's instruction following capabilities.

## Relationships

### → IFEval
- **Instruction following** (behavioral indicator): *measured_by*, 30 papers
  > “Instruction-Following Evaluation (IFEval): IFEval is a benchmark evaluating a model’s ability to follow explicit instructions”
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ebfb4ec1926fc6409df3bcf7ce957e8-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf)
  - [Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f74d79573d71078848973009d0e99bdb-Paper-Conference.pdf)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
  - [Iterative Nash Policy Optimization: Aligning LLMs with General Preferences via No-Regret Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/4eef032250ac525903063cd760cb0480-Paper-Conference.pdf)
  - [MIA-Bench: Towards Better Instruction Following Evaluation of Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/571082ea18d30060177dfcaf662ff0e5-Paper-Conference.pdf)
  - [Compute-Constrained Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/5acb720a361eecb34ee62d356859d246-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
  - [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf)
  - [Balancing the Budget: Understanding Trade-offs Between Supervised and Preference-Based Finetuning](https://aclanthology.org/2025.acl-long.1248.pdf)
  - [SkillVerse : Assessing and Enhancing LLMs with Tree Evaluation](https://aclanthology.org/2025.acl-long.437.pdf)
  - [IPO: Your Language Model is Secretly a Preference Classifier](https://aclanthology.org/2025.acl-long.954.pdf)
  - [Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf)
  - [Portable Reward Tuning: Towards Reusable Fine-Tuning across Different Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chijiwa25a/chijiwa25a.pdf)
  - [Discriminative Finetuning of Generative Large Language Models without Reward Models and Human Preference Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25d/guo25d.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
  - [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf)
  - [From Parameters to Performance: A Data-Driven Study on LLM Structure and Development](https://aclanthology.org/2025.emnlp-main.1325.pdf)
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf)
  - [LoRACoE: Improving Large Language Model via Composition-based LoRA Expert](https://aclanthology.org/2025.emnlp-main.1594.pdf)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1542.pdf)
  - [Priority on High-Quality: Selecting Instruction Data via Consistency Verification of Noise Injection](https://aclanthology.org/2025.emnlp-main.1048.pdf)
- **Instruction following ability** (construct): *measured_by*, 12 papers
  > evaluate it on various tasks, including instruction-following and roleplay (IFEval and MT-Bench)
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
  - [Do LLMs ``know'' internally when they follow instructions?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca6980a3dba7fb3e4e66925656dba68b-Paper-Conference.pdf)
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
  - [A Systematic Examination of Preference Learning through the Lens of Instruction-Following](https://aclanthology.org/2025.naacl-long.552.pdf)
  - [Self-Pluralising Culture Alignment for Large Language Models](https://aclanthology.org/2025.naacl-long.350.pdf)
  - [Marco-Bench-MIF: On Multilingual Instruction-Following Capability of Large Language](https://aclanthology.org/2025.acl-long.1172.pdf)
  - [GAPO: Learning Preferential Prompt through Generative Adversarial Policy Optimization](https://aclanthology.org/2025.acl-long.13.pdf)
  - [IOPO: Empowering LLMs with Complex Instruction Following via Input-Output Preference Optimization](https://aclanthology.org/2025.acl-long.1079.pdf)
  - [Evaluating Robustness of Large Audio Language Models to Audio Injection: An Empirical Study](https://aclanthology.org/2025.emnlp-main.1303.pdf)
  - [MAIN: Mutual Alignment Is Necessary for instruction tuning](https://aclanthology.org/2025.emnlp-main.644.pdf)
  - [DICE: Structured Reasoning in LLMs through SLM-Guided Chain-of-Thought Correction](https://aclanthology.org/2025.emnlp-main.355.pdf)
- **ComplexBench** (measurement instrument): *correlates*, 1 paper
  > although the performance of various LLMs on ComplexBench is well correlated with their performance on other benchmarks, the rankings of LLMs on ComplexBench do not entirely correspond with those on the other three benchmarks. (Section 5.2.3)
  - [Benchmarking Complex Instruction-Following with Multiple Constraints Composition](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8c24b08b96a08ec7a7a975feea7777e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-correction ability** (construct): *measured_by*, 1 paper
  > We evaluate self-correction capability on both classification and generation tasks, including domains in mathematics, coding, instruction following, common-sense reasoning, and knowledge. To be specific, the dataset we utilized include ... IFEval (Zhou et al., 2023)... (Section 4.1)
  - [Confidence v.s. Critique: A Decomposition of Self-Correction Capability for LLMs](https://aclanthology.org/2025.acl-long.203.pdf)
- **Utility preservation** (construct): *measured_by*, 1 paper
  > The utility performance is evaluated on MT-Bench(Zheng et al., 2023), IFEval(Zhou et al., 2023) and GSM8K(Cobbe et al., 2021), along with the benign part of XSTest(Röttger et al., 2024). (Section 1).
  - [Improve Safety Training of Large Language Models with Safety-Critical Singular Vectors Localization](https://aclanthology.org/2025.acl-long.245.pdf)
- **Helpfulness** (construct): *measured_by*, 1 paper
  > Our experiments focus on Helpfulness (Alpaca Eval 2.0 (Dubois et al., 2024) and IFEval (Zhou et al., 2023)), Harmlessness (Toxigen (Hartvigsen et al., 2022)), and Coding (MBPP (Austin et al., 2021), HumanEval (Chen et al., 2021)). (Section 4)
  - [AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs](https://aclanthology.org/2025.acl-long.990.pdf)
- **World knowledge** (construct): *measured_by*, 1 paper
  > To validate the effectiveness and generalization capabilities of our approach, we assess model capabilities in general knowledge using IFEval (Zhou et al., 2023c) and MMLU (Hendrycks et al., 2021b) (Section 4.1)
  - [Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning](https://aclanthology.org/2025.emnlp-main.350.pdf)

### Associated with
- **LiveBench** (measurement instrument), 1 paper
  > LiveBench... contains harder, contamination-limited versions of tasks from previous benchmarks such as Big-Bench Hard, AMPS, and IFEval.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
