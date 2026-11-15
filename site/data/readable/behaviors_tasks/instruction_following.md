# Instruction following
**Type:** Behavioral indicator  
**Supporting papers:** 244  
**Also known as:** Instruction adherence, Prompt execution, Following natural language instructions, Requirement satisfaction, Policy violation, Poor instruction-following, Instruction execution, Instruction violation, Instruction non-compliance, Phrase repetition, Natural language instruction following  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is adherence to explicit prompt constraints: producing an output or action sequence that stays on task, matches the requested format, and avoids unsupported, extraneous, or contradictory actions. Success is variously defined as meeting structural and functional requirements, obeying limits on length, format, style, content, or requested steps, and in Evaluating Language Model Agency Through Negotiations this includes staying within maximum word limits and producing valid JSON. A smaller line of work defines the failure case directly, as instruction violation, non-compliance, poor instruction-following, or policy violation, for example answering in the wrong language, revealing forbidden information, or taking an unauthorized action.

**Variants.** Papers use several near-neighbor names, with instruction adherence the most common, alongside prompt execution, following natural language instructions, requirement satisfaction, instruction execution, instruction violation, instruction non-compliance, policy violation, phrase repetition, and natural language instruction following. The settings span text-only prompts, multimodal and audio tasks, GUI interaction, negotiation, role-play, narratives, multilingual generation, and embodied planning. In UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction, failure includes inserting wait() or finish() actions not specified in the prompt, while other papers narrow the task to exact phrase repetition or to staying in character without added explanation.

**Space of elicitation and scores.** Papers measure this behavior with 41 instruments. The most frequently linked are MT-Bench, IFEval, AlpacaEval 2.0, Arena-Hard, and AlpacaEval. The recurring operationalization is benchmark-based evaluation, especially open-ended or explicit-instruction benchmarks; other papers use instruction datasets, automatic evaluators, human studies, and GPT-4 or other LLM-as-judge scoring. The quoted passages describe MT-Bench as GPT-4 graded one-turn and multi-turn instruction-following questions, IFEval as evaluating explicit instructions, and AlpacaEval 2.0 as a length-controlled, reference-free benchmark.

**What it is taken as evidence of.** Papers link instruction following to 17 constructs, most frequently Helpfulness, Human preference alignment, In-context learning, Accuracy, and Alignment. The links are mixed rather than uniform: some papers treat it as related to helpfulness, including one claim that a model is more helpful iff it shows statistically superior performance on measures of instruction following; some claim a causal relationship from instruction following to human preference alignment; and others claim causal relationships from in-context learning or alignment to instruction following. Because the recorded links vary in both type and direction, papers do not converge on a single construct that this behavior reflects.

## Sources

**Instruction adherence** (6 papers: [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nayak25a/nayak25a.pdf), [Evaluating Language Model Agency Through Negotiations](https://proceedings.iclr.cc/paper_files/paper/2024/file/03876dc6875571c18b3b09a624c77e96-Paper-Conference.pdf), [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf), [MIA-Bench: Towards Better Instruction Following Evaluation of Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/571082ea18d30060177dfcaf662ff0e5-Paper-Conference.pdf), [“What do you call a dog that is incontrovertibly true? Dogma”: Testing LLM Generalization through Humor](https://aclanthology.org/2025.acl-long.1117.pdf), [Video2Roleplay: A Multimodal Dataset and Framework for Video-Guided Role-playing Agents](https://aclanthology.org/2025.emnlp-main.1209.pdf))
> The tendency to follow the requested action format and avoid inserting unsupported or extraneous actions.

**Prompt execution** (1 paper: [Ask, and it shall be given: On the Turing completeness of prompting](https://proceedings.iclr.cc/paper_files/paper/2025/file/123d3e814e257e0781e5d328232ead9b-Paper-Conference.pdf))
> The model processing and acting upon a specific input prompt to perform a designated task.

**Following natural language instructions** (1 paper: [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf))
> The observable act of generating a response that adheres to the constraints and commands specified in a natural language prompt.

**Requirement satisfaction** (1 paper: [Agent-as-a-Judge: Evaluate Agents with Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuge25a/zhuge25a.pdf))
> Demonstrating that a generated solution fulfills specified functional and structural conditions defined in a task, including dependency-aware milestones.

**Policy violation** (1 paper: [Effective Red-Teaming of Policy-Adherent Agents](https://aclanthology.org/2025.emnlp-main.114.pdf))
> The observable act of an agent performing an action that contradicts a stated domain-specific rule or constraint, such as canceling a non-refundable ticket.

**Poor instruction-following** (1 paper: [FilBench: Can LLMs Understand and Generate Filipino?](https://aclanthology.org/2025.emnlp-main.127.pdf))
> Failing to adhere to task instructions, such as generating output in the wrong language or format.

**Instruction execution** (1 paper: [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf))
> Following detailed directives by carrying out the requested steps or constraints.

**Instruction violation** (1 paper: [Sparse Activation Editing for Reliable Instruction Following in Narratives](https://aclanthology.org/2025.emnlp-main.1311.pdf))
> The observable behavior where a model generates a response that contradicts or ignores the original instruction, such as revealing forbidden information in a narrative context.

**Instruction non-compliance** (1 paper: [TVQACML: Benchmarking Text-Centric Visual Question Answering in Multilingual Chinese Minority Languages](https://aclanthology.org/2025.emnlp-main.705.pdf))
> The observable failure of a model to adhere to the specified format or constraints of a given task or prompt.

**Phrase repetition** (1 paper: [Improbable Bigrams Expose Vulnerabilities of Incomplete Tokens in Byte-Level Tokenizers](https://aclanthology.org/2025.emnlp-main.919.pdf))
> The observable task of a model accurately reproducing a specific phrase provided in the input prompt when instructed to do so.

**Natural language instruction following** (1 paper: [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf))
> Interpreting and acting upon high-level user commands expressed in natural language to initiate appropriate task planning behavior.

## Relationships

### Instruction following →
- **MT-Bench** (measurement instrument): *measured_by*, 35 papers
  > MT-Bench is a benchmark featuring challenging ONE-TURN or MULTI-TURN reasoning and instruction-following examples, where the model responses are graded by GPT-4 on a scale of 1 (worst) to 10 (best). (Section 6)
  - [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf)
  - [Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf)
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
  - [S$^{2}$FT: Efficient, Scalable and Generalizable LLM Fine-tuning by Structured Sparsity](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e3b9fb0c0c56cf6e1ee61e6a068fca4-Paper-Conference.pdf)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf)
  - [ALLaM: Large Language Models for Arabic and English](https://proceedings.iclr.cc/paper_files/paper/2025/file/54c15a3033686e7999aecd2740c5a7c4-Paper-Conference.pdf)
  - [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf)
  - [KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf)
  - [Is In-Context Learning Sufficient for Instruction Following in LLMs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/41623b137cd34807f56028aa9f6f84a7-Paper-Conference.pdf)
  - [Limits to scalable evaluation at the frontier: LLM as judge won’t beat twice the data](https://proceedings.iclr.cc/paper_files/paper/2025/file/4264ee4376776907c0b87ed70b959585-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
  - [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf)
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
  - [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf)
  - [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf)
  - [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf)
  - [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf)
  - [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf)
  - [Aligning Large Language Models to Follow Instructions and Hallucinate Less via Effective Data Filtering](https://aclanthology.org/2025.acl-long.804.pdf)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
  - [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf)
  - [Understanding Overadaptation in Supervised Fine-Tuning: The Role of Ensemble Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hao25d/hao25d.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
  - [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf)
  - [TGDPO: Harnessing Token-Level Reward Guidance for Enhancing Direct Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25c/zhu25c.pdf)
  - [FuseChat: Knowledge Fusion of Chat Models](https://aclanthology.org/2025.emnlp-main.1096.pdf)
  - [Selective Preference Optimization via Token-Level Reward Function Estimation](https://aclanthology.org/2025.emnlp-main.359.pdf)
- **IFEval** (measurement instrument): *measured_by*, 30 papers
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
- **AlpacaEval 2.0** (measurement instrument): *measured_by*, 26 papers
  > We primarily assess our models using three of the most popular open-ended instruction-following benchmarks: MT-Bench [94], AlpacaEval 2 [51], and Arena-Hard v0.1 [50].
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [Balancing Act: Diversity and Consistency in Large Language Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5554e55d7a21e62d0d7a028ec0ea1c7-Paper-Conference.pdf)
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
  - [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
  - [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf)
  - [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf)
  - [T-REG: Preference Optimization with Token-Level Reward Regularization](https://aclanthology.org/2025.acl-long.1353.pdf)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
  - [Reward-Guided Prompt Evolving in Reinforcement Learning for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25a/ye25a.pdf)
  - [Discriminative Finetuning of Generative Large Language Models without Reward Models and Human Preference Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25d/guo25d.pdf)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [Larger or Smaller Reward Margins to Select Preferences for LLM Alignment?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25al/huang25al.pdf)
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
  - [AlphaDPO: Adaptive Reward Margin for Direct Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25af/wu25af.pdf)
  - [TGDPO: Harnessing Token-Level Reward Guidance for Enhancing Direct Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25c/zhu25c.pdf)
  - [FuseChat: Knowledge Fusion of Chat Models](https://aclanthology.org/2025.emnlp-main.1096.pdf)
  - [Selective Preference Optimization via Token-Level Reward Function Estimation](https://aclanthology.org/2025.emnlp-main.359.pdf)
  - [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://aclanthology.org/2025.emnlp-main.583.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 13 papers
  > We primarily assess our models using three of the most popular open-ended instruction-following benchmarks: MT-Bench [94], AlpacaEval 2 [51], and Arena-Hard v0.1 [50].
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf)
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)
  - [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf)
  - [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf)
  - [T-REG: Preference Optimization with Token-Level Reward Regularization](https://aclanthology.org/2025.acl-long.1353.pdf)
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
  - [AlphaDPO: Adaptive Reward Margin for Direct Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25af/wu25af.pdf)
  - [TGDPO: Harnessing Token-Level Reward Guidance for Enhancing Direct Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25c/zhu25c.pdf)
  - [Selective Preference Optimization via Token-Level Reward Function Estimation](https://aclanthology.org/2025.emnlp-main.359.pdf)
  - [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://aclanthology.org/2025.emnlp-main.583.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 12 papers
  > To evaluate the instruction-following ability, we employ the three most widely recognized benchmarks, including AlpacaEval (Li et al., 2023), MT-bench (Zheng et al., 2023) and Vicuna-bench (Chiang et al., 2023).
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf)
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
  - [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
  - [Learning to Keep a Promise: Scaling Language Model Decoding Parallelism with Learned Asynchronous Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25a/jin25a.pdf)
  - [NICE Data Selection for Instruction Tuning in LLMs with Non-differentiable Evaluation Metric](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bm/wang25bm.pdf)
  - [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf)
  - [Improving Task Diversity in Label Efficient Supervised Finetuning of LLMs](https://aclanthology.org/2025.emnlp-main.1093.pdf)
- **Alpaca instruction dataset** (measurement instrument): *measured_by*, 7 papers
  > "Alpaca contains 52K instruction-following data generated from text-davinci-003 (GPT 3.5)" (Section 4.1)
  - [QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e6c2e85db1f1039177c4495ccd399ac4-Paper-Conference.pdf)
  - [Towards Optimal Multi-draft Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0907335ecf28faf15be54485dbcbe70e-Paper-Conference.pdf)
  - [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf)
  - [Distributed Speculative Inference (DSI): Speculation Parallelism for Provably Faster Lossless Language Model Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/b36554b97da741b1c48c9de05c73993e-Paper-Conference.pdf)
  - [Iterative Label Refinement Matters More than Preference Optimization under Weak Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/240225294cdd2c9b692c2519d3278a08-Paper-Conference.pdf)
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
  - [Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance](https://aclanthology.org/2025.emnlp-main.500.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 3 papers
  > Vicuna QA (Chiang et al., 2023) uses GPT-4 to evaluate the abilities of open-ended chatbots to follow instructions.
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
  - [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **Vicuna-Bench** (measurement instrument): *measured_by*, 3 papers
  > To evaluate the instruction-following ability, we employ the three most widely recognized benchmarks, including AlpacaEval (Li et al., 2023), MT-bench (Zheng et al., 2023) and Vicuna-bench (Chiang et al., 2023).
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
  - [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf)
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
- **UltraFeedback** (measurement instrument): *measured_by*, 3 papers
  > UltraFeedback [7]: a multi-aspect alignment dataset with 64K prompts with preferences obtained from GPT-4, including "Instruction following", "Honest", "Truthful", and "Helpful" objectives (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf)
- **Code generation** (behavioral indicator): *causes*, 3 papers
  > math and code problems are formatted as instructions, enhancing instruction following capabilities enables LLMs to better address these tasks. (Section 4)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
  - [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)
  - [CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.189.pdf)
- **Super-NaturalInstructions** (measurement instrument): *measured_by*, 2 papers
  > This set of tasks evaluates a model’s capability in adhering to instructions. ... Our chosen benchmark for this category is the Super Natural Instructions (Super NI) (Wang et al., 2022)... (Section 4.1)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
- **FollowIR** (measurement instrument): *measured_by*, 2 papers
  > State-of-the-art bi-encoder performance on instruction-following retrieval tasks (+14.3 p-MRR, +3.1 nDCG/MAP on FollowIR (Weller et al., 2024)) with comparable scores to SoTA cross-encoders. (Section 1)
  - [Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2cefdb2c4c3274b78cd450bac35228df-Paper-Conference.pdf)
  - [FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.597.pdf)
- **InfoBench** (measurement instrument): *measured_by*, 2 papers
  > InfoBench (Qin et al., 2024) introduces a new metric called Decomposed Requirements Following Ratio (DRFR) for assessing the instruction-adherence capabilities of LLMs.
  - [MIA-Bench: Towards Better Instruction Following Evaluation of Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/571082ea18d30060177dfcaf662ff0e5-Paper-Conference.pdf)
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf)
- **Human preference alignment** (construct): *causes*, 2 papers
  > the model's ability to follow instructions inherently leads to better alignment with general preferences such as helpfulness and safety
  - [On-the-fly Preference Alignment via Principle-Guided Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcd1d7a599f33c06f06615429793c69b-Paper-Conference.pdf)
  - [OmniAlign-V: Towards Enhanced Alignment of MLLMs with Human Preference](https://aclanthology.org/2025.acl-long.906.pdf)
- **BigCodeBench** (measurement instrument): *measured_by*, 2 papers
  > BigCodeBench (Zhuo et al., 2024) is a more challenging benchmark for code generation that evaluates models’ abilities to follow complex instructions... (Section 4.1)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > we conducted a comprehensive user study ... raters were presented with a set of three audio clips—one from each system—and were asked to rank them according to two key dimensions: Fidelity Quality ... and Instruction Following, which measures how accurately the audio reflects the given prompt. (Section 5.4)
  - [Language Model Based Text-to-Audio Generation: Anti-Causally Aligned Collaborative Residual Transformers](https://aclanthology.org/2025.emnlp-main.1322.pdf)
- **LLMBar** (measurement instrument): *measured_by*, 1 paper
  > LLMBar (Zeng et al., 2023) instead takes a different approach by assessing LLM-based judges’ ability to follow instructions, using response pairs with clear ground truth preference labels based on adherence to instructions rather than subjective preferences. (Section 2)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Zero-shot generalization** (construct): *causes*, 1 paper
  > multimodal instruction tuning has been introduced (Liu et al., 2024), full fine-tuning pre-trained models with diverse multimodal instruction-following datasets, thereby enabling zero-shot generalization to previously unseen multimodal tasks. (Section 1)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
- **FollowBench** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the trained models on several widely-used instruction-following benchmarks, including IFEval (Zhou et al., 2023), Multi-IF (He et al., 2024b), SysBench (Qin et al., 2024), FollowBench (Jiang et al., 2024), and CFBench (Zhang et al., 2024a). (Introduction)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1542.pdf)
- **AgentBench** (measurement instrument): *measured_by*, 1 paper
  > AGENTBENCH thus systematically evaluate an LLM’s core abilities, including following instructions (Ouyang et al., 2022), coding (Chen et al., 2021), knowledge acquisition (Joshi et al., 2017; Talmor et al., 2019), logical reasoning (Srivastava et al., 2023), and commonsense grounding (Shridhar et al., 2020a).
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Harmful content generation** (behavioral indicator): *causes*, 1 paper
  > GPT-4 showed notably more unsafe behavior than Turbo in almost all cases when chatting with ciphers, due to its superior instruction understanding and adherence, thereby interpreting the cipher instruction and generating a relevant response. (Section 4.3)
  - [GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed4c38fe7899d3653acf39b2102af8ba-Paper-Conference.pdf)
- **PandaLM** (measurement instrument): *measured_by*, 1 paper
  > It addresses vital subjective factors such as relative conciseness, clarity, adherence to instructions, comprehensiveness, and formality.
  - [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/be3b0d51a2b86cb4ffe50f13480217e0-Paper-Conference.pdf)
- **GAVIE** (measurement instrument): *measured_by*, 1 paper
  > To improve the robustness and flexibility of the evaluation on visual instruction tuning, we propose GPT4-Assisted Visual Instruction Evaluation (GAVIE) to assess the LMM output in two different aspects: Relevancy to evaluate the instruction-following performance and Accuracy to measure the visual hallucination in the LMM output. (Section 1)
  - [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)
- **MMBench** (measurement instrument): *measured_by*, 1 paper
  > To examine general visual understanding and instruction following of our model, we follow common practices and employ MMBench [77], MME [78], SEEDBench [79], MMMU [30] and MathVista [80] for evaluation. (Section 4.2)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator): *causes*, 1 paper
  > Furthermore, we reveal that the catastrophic forgetting in MLLMs is primarily due to the decline in instruction following rather than reasoning knowledge.
  - [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > We believe this result indicates that self-improvement requires a minimal level of instruction following and reasoning capabilities, which is not present in these small models. (Section 4.1)
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **MT-Bench-101** (measurement instrument): *measured_by*, 1 paper
  > Also, we employed three popular and challenging benchmarks to evaluate the open-ended instruction following task: AlpacaEval (Li et al., 2023), Arena-Hard (Li et al., 2024), MT-Bench 101 (Bai et al., 2024) (Section 5.1).
  - [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf)
- **LiveBench** (measurement instrument): *measured_by*, 1 paper
  > LiveBench... contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **UltraChat** (measurement instrument): *measured_by*, 1 paper
  > ...and instruction task UltraChat (Ding et al., 2023). (§5)
  - [Model Equality Testing: Which Model is this API Serving?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d73234a13815fc1f9779dd17d89be9b4-Paper-Conference.pdf)
- **HelpSteer** (measurement instrument): *measured_by*, 1 paper
  > HelpSteer (Wang et al., 2023) is a QA dataset aimed at evaluating the model’s capability to follow instructions across five dimensions, including informativeness and factuality. (Section 4.1)
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)
- **ArmoRM** (measurement instrument): *measured_by*, 1 paper
  > To address this issue, we selected the instruction-following dimension from ArmoRM-8B (Wang et al., 2024a) as the main evaluation metric for our experiment. (Section 4.1)
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)
- **LongGenBench** (measurement instrument): *measured_by*, 1 paper
  > We introduced LongGenBench, a synthetic benchmark that evaluates long-form generation capabilities of language models by testing their ability to follow instructions over extended sequences. (Section 6)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **Long-form text generation** (behavioral indicator): *causes*, 1 paper
  > The ability to follow instructions is essential for long text generation (Reversed NIAH1), just as effective information retrieval is fundamental for processing long-context inputs (NIAH(Kamradt, 2023)). (Section 1)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **Visual grounding** (construct): *causes*, 1 paper
  > “These results emphasize the superiority of Text4Seg in following instructions, leading to enhanced visual grounding ability.”
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)
- **Open LLM Leaderboard** (measurement instrument): *measured_by*, 1 paper
  > "we also confirm that our safety-tuned model still preserves general instruction-following capabilities: as shown in Table B.2, the performance on the six tasks in the Open LLM Leaderboard changes insignificantly with safety tuning."
  - [Learning Diverse Attacks on Large Language Models for Robust Red-Teaming and Safety Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e128701ceca0ba03658a305faf39deb-Paper-Conference.pdf)
- **AudioBench** (measurement instrument): *measured_by*, 1 paper
  > Despite recent advancements, there lacks a comprehensive benchmark for AudioLLMs on instruction following capabilities conditioned on audio signals. AudioBench addresses this gap by setting up datasets as well as desired evaluation metrics.
  - [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf)
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > "we evaluate the evaluation protocols used in three automatic LLM benchmarks for instruction-following4 – AlpacaEval (Li et al., 2023c), ArenaHard (Li et al., 2024b), and WildBench (Lin et al., 2024)"
  - [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf)
- **BabyAI** (measurement instrument): *measured_by*, 1 paper
  > BabyAI is a grid world platform for instruction following where an agent receives natural language goal instructions such as: “Go to the tile (3,2)” or “Look behind the green locked door”. (Section 5)
  - [The Synergy of LLMs & RL Unlocks Offline Learning of Generalizable Language-Conditioned Policies with Low-fidelity Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pouplin25a/pouplin25a.pdf)
- **TRACE** (measurement instrument): *measured_by*, 1 paper
  > TRACE, another continual instruction tuning benchmark, is designed to evaluate the general ability, instruction following, and safety for LLMs (Wang et al., 2023). (Section 2. Related Work)
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **Natural Instructions** (measurement instrument): *measured_by*, 1 paper
  > Our experiments use three datasets for training and evaluation: the XSum summarization dataset (Narayan et al., 2018), the WMT-14 en-de translation dataset (Bojar et al., 2014), and the instruction-following dataset Natural Instructions (Mishra et al., 2022; Wang et al., 2022).
  - [On Teacher Hacking in Language Model Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tiapkin25a/tiapkin25a.pdf)
- **T-Eval** (measurement instrument): *measured_by*, 1 paper
  > We utilize T-Eval (Chen et al., 2023c), which assesses six core competencies: planning, reasoning, retrieval, understanding, instruction following, and reviewing. (Sec. 4.1)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Self-Instruct** (measurement instrument): *measured_by*, 1 paper
  > Then, we evaluate the trained student models on five instruction-following datasets: Dolly evaluation (Conover et al., 2023), Self-Instruct (Wang et al., 2022a), Super-Natural Instructions (Wang et al., 2022b), Unnatural Instruction(Honovich et al., 2022) and Vicuna evaluation(Chiang et al., 2023). (Section 4.1)
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
- **Mathematical problem solving** (behavioral indicator): *causes*, 1 paper
  > math and code problems are formatted as instructions, enhancing instruction following capabilities enables LLMs to better address these tasks. (Section 4)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
- **FLAN Collection** (measurement instrument): *measured_by*, 1 paper
  > Table 3 also reports target span perplexities on a randomly sampled subset of the FLAN Collection dataset (Longpre et al., 2023), which features data of instructing following, chain-of-thought, in-context few-shot learning, etc. (Section 3.3).
  - [MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25d/xiao25d.pdf)
- **C-Eval** (measurement instrument): *measured_by*, 1 paper
  > Instruction benchmarks evaluate a model’s ability to comprehend and execute detailed directives. ... with C-Eval (Huang et al., 2024) focusing on Chinese instructions.
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.511.pdf)
- **VoiceBench** (measurement instrument): *measured_by*, 1 paper
  > ...VoiceBench (Chen et al., 2024c) synthesizes IFEval (Zhou et al., 2023a), a text-based LLM instruction-following benchmark, into speech...
  - [Towards Holistic Evaluation of Large Audio-Language Models: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **Multi-IF** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the trained models on several widely-used instruction-following benchmarks, including IFEval (Zhou et al., 2023), Multi-IF (He et al., 2024b), SysBench (Qin et al., 2024), FollowBench (Jiang et al., 2024), and CFBench (Zhang et al., 2024a). (Introduction)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1542.pdf)
- **CFBench** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the trained models on several widely-used instruction-following benchmarks, including IFEval (Zhou et al., 2023), Multi-IF (He et al., 2024b), SysBench (Qin et al., 2024), FollowBench (Jiang et al., 2024), and CFBench (Zhang et al., 2024a). (Introduction)
  - [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1542.pdf)

### → Instruction following
- **In-context learning** (construct): *causes*, 2 papers
  > “ICL can marginally help to adapt LMMs to follow instructions.”
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Human preference alignment** (construct): *causes*, 1 paper
  > their magical ability to follow myriad user instructions – the driving force behind their mass adoption – has been attributed to instruction fine-tuning and learning from human feedback. (Section 1)
  - [Privately Aligning Language Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/477b39bfb9db99f60914dbfed5f23eb2-Paper-Conference.pdf)
- **Context retention** (construct): *causes*, 1 paper
  > This highlights the memory retention issue in long-context models, which often leads to a loss of coherence and adherence to task instructions. (Section 3.2)
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > Large language models (LLMs) require alignment to effectively and safely follow user instructions. (Abstract)
  - [Nudging: Inference-time Alignment of LLMs via Guided Decoding](https://aclanthology.org/2025.acl-long.623.pdf)
- **Response ranking** (behavioral indicator): *causes*, 1 paper
  > for tasks like instruction-following and reasoning, techniques such as fusion and ranking are effective for bolstering task performances (Section 2)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Prompt robustness** (construct): *causes*, 1 paper
  > This brittleness manifests... as poor instruction following in chatbots and AI agents when commands deviate from those encountered during training (Hong et al., 2024; Sahoo et al., 2025) (Section 1).
  - [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf)

### Associated with
- **Helpfulness** (construct), 3 papers
  > LMMs must be helpful (e.g., ... follow user instructions)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Reasoning** (construct), 1 paper
  > Gemma-7B-Instruct performs better in structured tasks like reasoning and coding, where precise instruction-following is crucial (Section 3.1)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
- **Task generalization** (construct), 1 paper
  > Instruction Following is often used to evaluate the cross-task generalization of LLMs, and it is dedicated to handling any task described in natural language (Section 2 Related Work).
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **Robotic manipulation** (behavioral indicator), 1 paper
  > "Long-horizon manipulation tasks with general instructions often implicitly encapsulate multiple sub-tasks, posing significant challenges in instruction following"
  - [PERIA: Perceive, Reason, Imagine, Act via Holistic Language and Vision Planning for Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6af963e891e7efa229c24a1607fa7f-Paper-Conference.pdf)
- **Accuracy** (construct), 1 paper
  > “Truth Alignment = Reasoning Capability + Instruction Following”
  - [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generalization** (construct), 1 paper
  > This trend suggests that lower learning rates enhance the model’s ability to generalize to unseen tasks requiring knowledge, complex reasoning, and instruction following.
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **Safety** (construct), 1 paper
  > this balance creates vulnerabilities when the model’s instruction-following objective from u conflicts with the safety goals defined in g.
  - [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf)
- **Coding** (behavioral indicator), 1 paper
  > Gemma-7B-Instruct performs better in structured tasks like reasoning and coding, where precise instruction-following is crucial (Section 3.1)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
- **Text generation quality** (construct), 1 paper
  > achieving an optimal trade-off between instruction adherence and output quality. (Section 1)
  - [Sparse Activation Editing for Reliable Instruction Following in Narratives](https://aclanthology.org/2025.emnlp-main.1311.pdf)
- **Generation diversity** (construct), 1 paper
  > This limitation [in output diversity] hinders their performance in tasks that demand diverse and informative responses, such as open-domain question answering, instruction following, and test-time scaling for reasoning (Zhang et al., 2024a). (Section 1)
  - [G2: Guided Generation for Enhanced Output Diversity in LLMs](https://aclanthology.org/2025.emnlp-main.713.pdf)
- **Cross-lingual generalization** (construct), 1 paper
  > We question whether instruction-following capabilities could be directly transferred to new languages without dedicated instruction data, and whether instruction-tuned models could be adapted through continued pretraining, similar to base models. (Section 1)
  - [Instructing Large Language Models for Low-Resource Languages: A Systematic Study for Basque](https://aclanthology.org/2025.emnlp-main.1484.pdf)
- **Information extraction** (behavioral indicator), 1 paper
  > to identify hallucinations existed in the reference description, we first extract object entities (object nouns and phrases) from it. Here, we leverage the strong instruction following ability of the Large Language Model (LLM). (Sec. 3.2.1)
  - [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Omni-Judge** (measurement instrument), 1 paper
  > Then we treat this task as a similar flow of instruction following, where the extraction of the model answer, judgment, and detailed justification are all required to be generated by Omni-Judge. (Section 2.4)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
- **Paraphrasing** (behavioral indicator), 1 paper
  > Instruction Following: four tasks to paraphrase, simplify, summarize, or generate stories
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Story generation** (behavioral indicator), 1 paper
  > Instruction Following: four tasks to paraphrase, simplify, summarize, or generate stories
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Text summarization** (behavioral indicator), 1 paper
  > Instruction Following: four tasks to paraphrase, simplify, summarize, or generate stories
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **ShareGPT** (measurement instrument), 1 paper
  > “ShareGPT is a dialog dataset collected from sharegpt.com, a website collecting user-shared dialog with ChatGPT. This dataset encompasses a wide range of topics, making it suitable as a general instruction tuning set focusing on the instruction-following ability of models.”
  - [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf)
