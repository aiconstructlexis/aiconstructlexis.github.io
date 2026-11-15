# BIG-Bench Hard
**Type:** Measurement instrument  
**Supporting papers:** 160  
**Also known as:** Big Bench Hard, Big-Bench Hard, Big-Bench-Hard, BigBench-Hard, BIG-Bench-Hard, BIG-Bench-Hard (BBH), BIG-Bench Hard (BBH), Big-bench-hard (BBH), BIG-bench Hard, BBH-Hard, BigBench-Hard (BBH), BigBenchHard, BBH, BBH-COT  

## State of the Field

**What it is.** Across papers, the prevailing usage treats BIG-Bench Hard, usually abbreviated BBH, as a challenging subset of BIG-Bench or the Beyond the Imitation Game benchmark, centered on tasks that were difficult for contemporary language models and used for reasoning-focused evaluation. Most descriptions emphasize complex, multi-step, logical, or general reasoning, while some also frame it as covering language understanding, world knowledge, compositionality, and generalization; one paper describes 23 multiple-choice tasks and 4 free-form generation tasks, while others report 21, 23, or 27 tasks, sometimes across 23 task types. Some papers use only selected BBH subtasks, including DATE and Navigate, and one paper refers to BBH-COT as a chain-of-thought variant.

**What it is claimed to measure.** Papers link BBH to 20 constructs and 7 behavioral indicators, so its measurement claims are spread across many targets rather than converging on a single one. The dominant claim is that it measures reasoning, followed by general ability, natural language understanding, chain-of-thought reasoning, and complex reasoning. The remaining links extend to 15 other constructs and the 7 behavioral indicators.

**Space of uses.** In use, BBH is commonly part of broader evaluation suites, often alongside MMLU and GSM8K, and papers position it both as a main reasoning benchmark and as a more general capability check. Authors apply it in 0-shot, 3-shot, 5-shot, 10-shot, Hybrid, chain-of-thought, and many-shot in-context learning settings, sometimes on the full suite and sometimes on selected subtasks. Related links also connect it to Open LLM Leaderboard, lm-evaluation-harness, and LiveBench.

**Concerns raised.** One paper relates BBH to LiveBench, described as containing harder, contamination-limited versions of tasks from previous benchmarks such as BBH. Papers also describe BBH with varying task counts and formats, reporting 21, 23, or 27 tasks and either multiple-choice only or mixes of multiple-choice, short-response, direct-generation, and free-form generation tasks.

## Sources

**Big-Bench Hard** (4 papers: [Knowledge Fusion of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4fd5cfd2e31bebbccfa5ffa354c04bdc-Paper-Conference.pdf), [Large Language Models as Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/3339f19c5fcee3ad74502947a32be9e6-Paper-Conference.pdf), [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf), [BTS: Harmonizing Specialized Experts into a Generalist LLM](https://aclanthology.org/2025.emnlp-main.347.pdf))
> Subset of challenging tasks from the Beyond the Imitation Game Benchmark (BIG-Bench) that require complex reasoning, used to assess advanced language model capabilities.

**BBH** (29 papers: [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf), [CausalLM is not optimal for in-context learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/364071531ff2398e0fb8bae31f615b69-Paper-Conference.pdf), [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [MUFFIN: Curating Multi-Faceted Instructions for Improving Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d1a0188e18c1d74a0f8d6eb5ecede4f-Paper-Conference.pdf), [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf), [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf), [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/127a649ea9ae2df15e903a91352cfd3a-Paper-Conference.pdf), [AdaEdit: Advancing Continuous Knowledge Editing For Large Language Models](https://aclanthology.org/2025.acl-long.208.pdf), [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf), [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf), [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf), [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.336.pdf), [LLMs Are Biased Towards Output Formats! Systematically Evaluating and Mitigating Output Format Bias of LLMs](https://aclanthology.org/2025.naacl-long.15.pdf), [DAWN-ICL: Strategic Planning of Problem-solving Trajectories for Zero-Shot In-Context Learning](https://aclanthology.org/2025.naacl-long.96.pdf), [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf), [MoDification: Mixture of Depths Made Easy](https://aclanthology.org/2025.naacl-long.265.pdf), [CYCLE-INSTRUCT: Fully Seed-Free Instruction Tuning via Dual Self-Training and Cycle Consistency](https://aclanthology.org/2025.emnlp-main.258.pdf), [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf), [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf), [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf), [Instance-adaptive Zero-shot Chain-of-Thought Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/e304e04a6f455dd82f8a85a0a3679493-Paper-Conference.pdf), [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad236edc564f3e3156e1b2feafb99a24-Paper-Datasets_and_Benchmarks_Track.pdf), [Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf), [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf), [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf), [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf), [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf), [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf), [The Art of Saying No: Contextual Noncompliance in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/58e79894267cf72c66202228ad9c6057-Paper-Datasets_and_Benchmarks_Track.pdf))
> The BIG-Bench Hard benchmark, a subset of challenging tasks from BIG-Bench that were identified as difficult for contemporary language models.

**BIG-Bench Hard** (3 papers: [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf), [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf), [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf))
> Subset of the BIG-Bench suite focusing on challenging tasks requiring complex reasoning, including DATE and Navigate for symbolic reasoning.

**Big-Bench-Hard** (2 papers: [Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e1a87dbb7e954b8d9d6c91f6db771eb-Paper-Conference.pdf), [Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf))
> A subset of the Beyond the Imitation Game Benchmark (BIG-Bench) containing challenging tasks, used in this study to evaluate the knowledge and reasoning abilities of LLMs.

**Big Bench Hard** (5 papers: [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf), [Autonomous Evaluation of LLMs for Truth Maintenance and Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf), [Fine-Tuning on Diverse Reasoning Chains Drives Within-Inference CoT Refinement in LLMs](https://aclanthology.org/2025.acl-long.191.pdf), [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf))
> Subset of the Beyond the Imitation Game benchmark focusing on challenging reasoning tasks requiring multi-step logic.

**BigBench-Hard** (3 papers: [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf), [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf), [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf))
> A collection of 27 reasoning tasks where pre-existing LLMs could not outperform human evaluators, covering formats like multiple-choice and short response.

**BIG-Bench-Hard** (1 paper: [On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf))
> A benchmark suite consisting of 23 challenging tasks from the BIG-Bench benchmark that are identified as being difficult for prior language models.

**BIG-Bench-Hard (BBH)** (1 paper: [CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf))
> A benchmark suite comprising 21 challenging tasks designed to assess a model's semantic understanding and logical reasoning capabilities.

**BIG-Bench Hard (BBH)** (1 paper: [Self-playing Adversarial Language Game Enhances LLM Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4be7e9867ef163563f4a5e90cec478f-Paper-Conference.pdf))
> A benchmark consisting of 23 challenging tasks from the BIG-Bench suite that are difficult for current language models.

**Big-bench-hard (BBH)** (1 paper: [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf))
> A suite of challenging benchmark tasks, from which specific symbolic reasoning tasks like Boolean Expression and Dyck Language are drawn.

**BIG-bench Hard** (1 paper: [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf))
> BIG-bench Hard (BBH), a benchmark used to test general language understanding and reasoning.

**BBH-Hard** (3 papers: [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf), [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf), [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf))
> A subset of the BIG-Bench Hard benchmark used to evaluate a model's logical reasoning capabilities on challenging tasks.

**BigBench-Hard (BBH)** (1 paper: [Block-Attention for Efficient Prefilling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf))
> A general domain benchmark suite used to assess model capabilities on difficult tasks.

**BigBenchHard** (1 paper: [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf))
> BigBenchHard is a challenging reasoning benchmark suite used here via boolean expressions and web of lies subsets.

**BBH-COT** (1 paper: [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf))
> A chain-of-thought reasoning benchmark used to assess reasoning performance on Big-Bench Hard-style tasks.

## Relationships

### → BIG-Bench Hard
- **Reasoning** (construct): *measured_by*, 31 papers
  > One such benchmark is Bigbench-hard (Srivastava et al., 2022), which includes multiple reasoning tasks consisting of multiple-choice and direct-generation tasks. (Section 4.3)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e1a87dbb7e954b8d9d6c91f6db771eb-Paper-Conference.pdf)
  - [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Self-playing Adversarial Language Game Enhances LLM Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4be7e9867ef163563f4a5e90cec478f-Paper-Conference.pdf)
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
  - [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
  - [Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f74d79573d71078848973009d0e99bdb-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf)
  - [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/558a100caa93422df215fadb9e9b1dd7-Paper-Conference.pdf)
  - [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
  - [Dynamic Data Mixing Maximizes Instruction Tuning for Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.80.pdf)
  - [From Informal to Formal – Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs](https://aclanthology.org/2025.acl-long.1310.pdf)
  - [TESS 2: A Large-Scale Generalist Diffusion Language Model](https://aclanthology.org/2025.acl-long.1029.pdf)
  - [Towards the Law of Capacity Gap in Distilling Language Models](https://aclanthology.org/2025.acl-long.1097.pdf)
  - [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf)
  - [Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law](https://aclanthology.org/2025.acl-long.1157.pdf)
  - [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
  - [Evaluating Robustness of Large Audio Language Models to Audio Injection: An Empirical Study](https://aclanthology.org/2025.emnlp-main.1303.pdf)
- **General ability** (construct): *measured_by*, 6 papers
  > “we evaluate the 12 models in Table 2 on challenging downstream zero- and few-shot benchmarks focusing on language understanding and reasoning. We include results for 0-shot (0S) and 3-shot (3S) evaluation for BIG-Bench Hard tasks [63, 64]”
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
  - [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf)
  - [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf)
  - [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.naacl-long.321.pdf)
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **Natural language understanding** (construct): *measured_by*, 4 papers
  > BBH tasks cover a diverse range of reasoning problems spanning the following 4 categories according to their authors: 1) Algorithmic and Multi-Step Arithmetic Reasoning, 2) Natural Language Understanding, 3) Use of World Knowledge, and 4) Multilingual Knowledge and Reasoning.
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
- **Logical reasoning** (construct): *measured_by*, 3 papers
  > BBH contains 21 tasks covering both semantic understanding and logical reasoning tasks. (Section 5.2)
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **Symbolic reasoning** (construct): *measured_by*, 3 papers
  > Additionally, we investigate symbolic reasoning tasks from Big-Bench-Hard (bench authors, 2023; Suzgun et al., 2022). (Section 3)
  - [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 3 papers
  > World Knowledge: MMLU [28] (5-shot), BBH [29] (3-shot), with the assessment based on the accuracy of multiple-choice answers. (Section 3.1).
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
  - [LLMs Are Biased Towards Output Formats! Systematically Evaluating and Mitigating Output Format Bias of LLMs](https://aclanthology.org/2025.naacl-long.15.pdf)
  - [DyePack: Provably Flagging Test Set Contamination in LLMs Using Backdoors](https://aclanthology.org/2025.emnlp-main.776.pdf)
- **Generalization** (construct): *measured_by*, 3 papers
  > we access three mainstream benchmarks (MMLU [15], BBH [37], and GSM8K [8]) to evaluate generalization abilities. (Section 3.1)
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
  - [Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf)
  - [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf)
- **Chain-of-thought reasoning** (construct): *measured_by*, 3 papers
  > To validate our methods on diverse tasks, we apply BBH (Suzgun et al., 2022) including a suite of 23 challenging BIG-Bench tasks requiring multi-step reasoning. (Section 4.4)
  - [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
- **Complex reasoning** (construct): *measured_by*, 3 papers
  > BBH (Suzgun et al., 2023) encompasses 27 arduous tasks to assess whether the model can handle complex reasoning situations.
  - [Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf)
  - [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf)
  - [Beyond Similarity: A Gradient-based Graph Method for Instruction Tuning Data Selection](https://aclanthology.org/2025.acl-long.1189.pdf)
- **In-context learning** (construct): *measured_by*, 2 papers
  > evaluate the ICL capability of the finetuned models on two benchmarks: MMLU (Hendrycks et al., 2020) and BBH (Suzgun et al., 2022). (Section 5.3)
  - [CausalLM is not optimal for in-context learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/364071531ff2398e0fb8bae31f615b69-Paper-Conference.pdf)
  - [Block-Attention for Efficient Prefilling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
- **World knowledge** (construct): *measured_by*, 2 papers
  > BBH tasks cover a diverse range of reasoning problems spanning the following 4 categories according to their authors: 1) Algorithmic and Multi-Step Arithmetic Reasoning, 2) Natural Language Understanding, 3) Use of World Knowledge, and 4) Multilingual Knowledge and Reasoning.
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator): *measured_by*, 2 papers
  > In this section, we explore the forgetting of CultureLLM in two general datasets: BIG-Bench-Hard (BBH) [Suzgun et al., 2022] and GSM8K [Cobbe et al., 2021]. (Section 5.2)
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
  - [Controlled Low-Rank Adaptation with Subspace Regularization for Continued Training on Large Language Models](https://aclanthology.org/2025.acl-long.940.pdf)
- **General reasoning** (construct): *measured_by*, 2 papers
  > Finally, to evaluate general reasoning, we test the model on two benchmarks: ...and a more challenging task, 3-shot Chain-of-Thought (CoT) Big Bench Hard (BBH) (Suzgun et al., 2022). (Section 2.3)
  - [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf)
  - [Compute-Constrained Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/5acb720a361eecb34ee62d356859d246-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > We evaluate on tasks selected from BIG-Bench Hard (BBH) [43], a collection of diverse tasks considered to be challenging to LLMs ... the tasks include numerical reasoning, commonsense problem-solving, logical deduction, linguistic manipulation, machine translation, and tabular reasoning, among others. (Section 3.1)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **Machine translation** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate on tasks selected from BIG-Bench Hard (BBH) [43], a collection of diverse tasks considered to be challenging to LLMs ... the tasks include numerical reasoning, commonsense problem-solving, logical deduction, linguistic manipulation, machine translation, and tabular reasoning, among others. (Section 3.1)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **Table reasoning** (construct): *measured_by*, 1 paper
  > We evaluate on tasks selected from BIG-Bench Hard (BBH) [43], a collection of diverse tasks considered to be challenging to LLMs ... the tasks include numerical reasoning, commonsense problem-solving, logical deduction, linguistic manipulation, machine translation, and tabular reasoning, among others. (Section 3.1)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
- **Code generation** (behavioral indicator): *measured_by*, 1 paper
  > In this experiment, we test Trace’s ability in joint prompt optimization and code generation. ... We use the Big-Bench Hard dataset [21] (15 examples for training, 5 for validation, and the rest for testing). (Section 5.3)
  - [Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/83ba7056bce2c3c3c27e17397cf3e1f0-Paper-Conference.pdf)
- **Word sorting** (behavioral indicator): *measured_by*, 1 paper
  > Three BIG-Bench Hard (BBH) [35] tasks: Geometric Shapes, Multi-Step Arithmetic Two, and Word Sorting
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
- **Multilingual reasoning** (construct): *measured_by*, 1 paper
  > BBH tasks cover a diverse range of reasoning problems spanning the following 4 categories according to their authors: 1) Algorithmic and Multi-Step Arithmetic Reasoning, 2) Natural Language Understanding, 3) Use of World Knowledge, and 4) Multilingual Knowledge and Reasoning.
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
- **Algorithmic reasoning** (construct): *measured_by*, 1 paper
  > algorithmic reasoning [BBH, 55] (Introduction).
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **Disambiguation ability** (construct): *measured_by*, 1 paper
  > “These benchmarks are quite diverse and include tasks such as logical deduction, arithmetic, translation error detection, disambiguation, as well as general knowledge”
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > To evaluate the efficacy of ACC-Collab we make use of 5 standard benchmark tasks: ... BBH Suzgun et al. (2022) ∼5k mixed-type questions (Section 5)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > To evaluate the efficacy of our approach, we use GSM8K (Cobbe et al., 2021), Big-Bench-Hard (BBH) (Suzgun et al., 2022), and FOLIO (Han et al., 2022) benchmark datasets for diverse reasoning tasks in mathematics, commonsense, and logical reasoning. (Section 5.1)
  - [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf)
- **Contextual understanding** (construct): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Object counting** (behavioral indicator): *measured_by*, 1 paper
  > For prompt optimization, we use the Big Bench Hard dataset (Suzgun et al., 2022) for Object Counting... (Section 4)
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)
- **Compositionality** (construct): *measured_by*, 1 paper
  > BIG-Bench Hard (BBH; Srivastava et al., 2023; Suzgun et al., 2023) is a benchmark comprising 27 challenging tasks across 23 task types, designed to evaluate large language models on reasoning, compositionality, and generalization. (Section 5.1)
  - [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf)
- **Editing locality** (construct): *measured_by*, 1 paper
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)

### Associated with
- **Open LLM Leaderboard** (measurement instrument), 2 papers
  > Table 2: Evaluation results on various tasks from the Huggingface Open Leaderboard v1 and v2. ... MMLU-PRO, BBH, MUSR, MATH, GSM8K, ARC
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **lm-evaluation-harness** (measurement instrument), 2 papers
  > We use lm-evaluation-harness to report results on ... BigBench-Hard
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
  - [$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf)
- **BIG-Bench Logical Deduction** (measurement instrument), 2 papers
  > We evaluate on tasks selected from BIG-Bench Hard (BBH) [43], a collection of diverse tasks considered to be challenging to LLMs ... the tasks include numerical reasoning, commonsense problem-solving, logical deduction, linguistic manipulation, machine translation, and tabular reasoning, among others. (Section 3.1)
  - [Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/6b031defd145b02bed031093d8797bb3-Paper-Conference.pdf)
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
- **LiveBench** (measurement instrument), 1 paper
  > LiveBench... contains harder, contamination-limited versions of tasks from previous benchmarks such as Big-Bench Hard, AMPS, and IFEval.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
