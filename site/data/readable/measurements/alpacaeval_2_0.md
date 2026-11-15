# AlpacaEval 2.0
**Type:** Measurement instrument  
**Supporting papers:** 123  
**Also known as:** AlpacaEval2, AlpacaEval2.0, AlpacaEval-2, Alpaca Eval V2, Alpaca Eval 2.0, Alpaca Eval 2, Alpaca-Eval-2, AlpacaEval-V2, AlpacaEvalv2, Alpaca-Eval V2, AlpacaEval v2.0, AlpacaEval 2, Length-controlled AlpacaEval 2.0, AlpacaEval 2.0 Length Controlled, Length-Controlled AlpacaEval, AlpacaEval Leaderboard  

## State of the Field

**What it is.** Across papers, the prevailing usage is as an automatic, LLM-as-a-judge benchmark for instruction-following and open-ended chat evaluation: a model answers 805 instructions or questions, often described as drawn from five datasets or representative real user interactions, and its responses are compared pairwise with a reference or baseline response. Most definitions say the judge is GPT-4, GPT-4 Turbo, or GPT-4o, with outputs reported as win rate and often length-controlled win rate, sometimes against GPT-4 Turbo or Text-davinci-003. Many papers also refer to variants such as AlpacaEval 2.0 Length Controlled or Length-Controlled AlpacaEval, while a smaller set frames it more specifically as question answering, conversation quality, or a text-only human preference alignment benchmark.

**What it is claimed to measure.** Papers use it to measure 9 constructs and 6 behavioral indicators. The prevailing claims are that it measures instruction following and instruction following ability, and many papers also use it to measure human preference alignment, helpfulness, and alignment. Beyond these common framings, papers spread it across several other targets rather than tying it to only one construct.

**Space of uses.** Most papers use it as one of the main benchmarks in multi-benchmark evaluations, usually alongside MT-Bench and Arena-Hard for instruction following, alignment, or chatbot capability; some papers instead use the length-controlled variant as a secondary measure of helpfulness. Papers link it to 3 other instruments: AlpacaEval and human evaluation as related instruments, and Chatbot Arena as a reported correlate. One paper reports a Spearman correlation of 0.98 with Chatbot Arena.

**Concerns raised.** A recurring concern is length or verbosity bias. Many papers describe length-controlled win rates, regression calibration, or a generalized linear model as ways to reduce length-based or stylistic bias, and one paper relates AlpacaEval 2.0 to verbosity bias and says it is not robust to length cheat.

## Sources

**AlpacaEval2** (5 papers: [Online Iterative Reinforcement Learning from Human Feedback with General Preference Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf), [Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf), [Towards Reward Fairness in RLHF: From a Resource Allocation Perspective](https://aclanthology.org/2025.acl-long.163.pdf), [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf), [AIR: Complex Instruction Generation via Automatic Iterative Refinement](https://aclanthology.org/2025.emnlp-main.1628.pdf))
> AlpacaEval2 is an evaluation framework that uses strong LLMs like GPT-4 as judges to assess model performance on a set of prompts, providing a simulated human preference evaluation.

**AlpacaEval 2** (13 papers: [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf), [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf), [Aligning Large Language Models with Implicit Preferences from User-Generated Content](https://aclanthology.org/2025.acl-long.384.pdf), [Principled Data Selection for Alignment: The Hidden Risks of Difficult Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25f/gao25f.pdf), [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf), [Stronger Models are Not Always Stronger Teachers for Instruction Tuning](https://aclanthology.org/2025.naacl-long.224.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf), [Ambiguity Awareness Optimization: Towards Semantic Disambiguation for Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.460.pdf), [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://aclanthology.org/2025.emnlp-main.130.pdf), [Direct Judgement Preference Optimization](https://aclanthology.org/2025.emnlp-main.103.pdf), [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://aclanthology.org/2025.emnlp-main.583.pdf), [Weights-Rotated Preference Optimization for Large Language Models](https://aclanthology.org/2025.emnlp-main.1329.pdf))
> An automatic evaluator of instruction-following models that uses pairwise comparisons to assess chat response quality against a baseline model.

**AlpacaEval2.0** (4 papers: [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf), [DavIR: Data Selection via Implicit Reward for Large Language Models](https://aclanthology.org/2025.acl-long.452.pdf), [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf), [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf))
> An evaluation framework that uses GPT-4 to judge instruction-following responses against a reference model.

**AlpacaEval-2** (1 paper: [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d46574e5baae5121180228223a11836-Paper-Conference.pdf))
> An automatic evaluation suite for assessing the performance of instruction-following language models, which includes a length-controlled win-rate metric.

**AlpacaEval 2.0** (5 papers: [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf), [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf), [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf), [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.51.pdf), [Discriminative Policy Optimization for Token-Level Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ca/chen25ca.pdf))
> An evaluation benchmark that assesses a model's question-answering performance by comparing its responses on a set of instructions against a reference model like GPT-4.

**Alpaca Eval V2** (1 paper: [MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ddab70bf41ffe5d423840644d3357f4-Paper-Conference.pdf))
> An evaluation set used to compare fine-tuned instruction-following models on response quality via GPT-4 judgments.

**Alpaca Eval 2.0** (3 papers: [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf), [From Real to Synthetic: Synthesizing Millions of Diversified and Complicated User Instructions with Attributed Grounding](https://aclanthology.org/2025.acl-long.517.pdf), [Energy-Based Preference Model Offers Better Offline Alignment than the Bradley-Terry Preference Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25i/hong25i.pdf))
> A benchmark used here as an in-domain evaluation of instruction-following, with pairwise head-to-head judgments by GPT-4-turbo.

**Alpaca Eval 2** (1 paper: [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf))
> A benchmark for evaluating a model's ability to follow instructions.

**Alpaca-Eval-2** (1 paper: [Intuitive Fine-Tuning: Towards Simplifying Alignment into a Single Process](https://aclanthology.org/2025.acl-long.6.pdf))
> An updated version of Alpaca-Eval that evaluates model responses using GPT-4 with improved criteria and task coverage, focusing on conversation quality.

**AlpacaEval-V2** (1 paper: [OmniAlign-V: Towards Enhanced Alignment of MLLMs with Human Preference](https://aclanthology.org/2025.acl-long.906.pdf))
> A text-only human preference alignment benchmark used to evaluate language alignment in LLMs and MLLMs.

**AlpacaEvalv2** (1 paper: [Condor: Enhance LLM Alignment with Knowledge-Driven Data Synthesis and Refinement](https://aclanthology.org/2025.acl-long.1091.pdf))
> Human-preference benchmark that evaluates model responses through pairwise comparisons, measuring overall helpfulness and coherence in open-ended dialogue.

**Alpaca-Eval V2** (1 paper: [NILE: Internal Consistency Alignment in Large Language Models](https://aclanthology.org/2025.emnlp-main.412.pdf))
> An automatic evaluation system for instruction-following language models that uses GPT-4-Turbo to judge responses and introduces Length-Controlled Win Rates to reduce length-based biases.

**AlpacaEval v2.0** (1 paper: [Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality](https://aclanthology.org/2025.emnlp-main.1138.pdf))
> An automatic, LLM-based evaluator for assessing the quality of a model's responses to a set of instructions, comparing them against a reference model's outputs.

**Length-controlled AlpacaEval 2.0** (1 paper: [Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf))
> A benchmark for evaluating chat model instruction-following capabilities where response length is controlled to provide a fair comparison.

**AlpacaEval 2.0 Length Controlled** (2 papers: [From Crowdsourced Data to High-quality Benchmarks: Arena-Hard and Benchbuilder Pipeline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25h/li25h.pdf), [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf))
> Human preference-based evaluation benchmark that uses LLM-as-a-judge with length control to reduce stylistic bias, used for comparing alignment and separability.

**Length-Controlled AlpacaEval** (1 paper: [Investigating Non-Transitivity in LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25w/xu25w.pdf))
> A modified version of the AlpacaEval framework that applies a generalized linear model to control for the influence of response length on evaluation scores.

**AlpacaEval Leaderboard** (1 paper: [Time-Reversal Provides Unsupervised Feedback to LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/34aec5ab2f99a8f592e0cca4974013f2-Paper-Conference.pdf))
> A widely used benchmark for evaluating the instruction-following capabilities of language models by comparing their outputs against a reference model like GPT-4.

## Relationships

### AlpacaEval 2.0 →
- **Chatbot Arena** (measurement instrument): *correlates*, 1 paper
  > Here, we test on AlpacaEval 2.0 (Dubois et al., 2024), which has a Spearman correlation of 0.98 with Chatbot Arena while being cost-efficient. (Section 3.2)
  - [Improving Instruct Models for Free: A Study on Partial Adaptation](https://aclanthology.org/2025.emnlp-main.581.pdf)

### → AlpacaEval 2.0
- **Instruction following** (behavioral indicator): *measured_by*, 26 papers
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
- **Instruction following ability** (construct): *measured_by*, 13 papers
  > Instruction-following ability. We further benchmark RoAd using AlpacaEval2.0 [9]. (Section 4.1)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
  - [Better Instruction-Following Through Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/6756c9f0a1a7c6d1d10ab252f16524f2-Paper-Conference.pdf)
  - [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
  - [Stronger Models are Not Always Stronger Teachers for Instruction Tuning](https://aclanthology.org/2025.naacl-long.224.pdf)
  - [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf)
  - [Optimal Transport-Based Token Weighting scheme for Enhanced Preference Optimization](https://aclanthology.org/2025.acl-long.1035.pdf)
  - [R.I.P.: Better Models by Survival of the Fittest Prompts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25u/yu25u.pdf)
  - [Boosting Multi-Domain Fine-Tuning of Large Language Models through Evolving Interactions between Samples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25q/liang25q.pdf)
  - [Discriminative Policy Optimization for Token-Level Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ca/chen25ca.pdf)
  - [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf)
  - [ConfPO: Exploiting Policy Model Confidence for Critical Token Selection in Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoon25b/yoon25b.pdf)
- **Human preference alignment** (construct): *measured_by*, 7 papers
  > AlpacaEval 2.0 approximately evaluates human preference for instruction following. (Section 5.1)
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
  - [Bootstrapping Language Models with DPO Implicit Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4de96b9169aa869cc102afe31055e8-Paper-Conference.pdf)
  - [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
  - [Model Extrapolation Expedites Alignment](https://aclanthology.org/2025.acl-long.51.pdf)
  - [KABB: Knowledge-Aware Bayesian Bandits for Dynamic Expert Coordination in Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aa/zhang25aa.pdf)
  - [Energy-Based Preference Model Offers Better Offline Alignment than the Bradley-Terry Preference Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25i/hong25i.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Helpfulness** (construct): *measured_by*, 6 papers
  > In addition, we also use AlpacaEval 2.0 Length Controlled [37] and Arena Hard [38] as secondary measures of helpfulness, following [33, 39].
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
  - [HelpSteer3: Human-Annotated Feedback and Edit Data to Empower Inference-Time Scaling in Open-Ended General-Domain Tasks](https://aclanthology.org/2025.acl-long.1246.pdf)
  - [AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs](https://aclanthology.org/2025.acl-long.990.pdf)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **Alignment** (construct): *measured_by*, 4 papers
  > "POWER-DL consistently outperforms state-of-the-art methods in alignment benchmarks, achieving improvements of up to 13.0 points on AlpacaEval 2.0"
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
  - [Reward-Guided Tree Search for Inference Time Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
  - [On the Robustness of Reward Models for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25d/hong25d.pdf)
- **Conversational ability** (construct): *measured_by*, 3 papers
  > We conduct GPT-4-based automatic evaluation on AlpacaEval 2.0 (Li et al., 2023b), MT-Bench (Zheng et al., 2023), and Arena-Hard (Li et al., 2024) to measure the chatbot capability of our model.
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf)
  - [DPO Meets PPO: Reinforced Token Optimization for RLHF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25b/zhong25b.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 2 papers
  > Our models are also tested for their open-ended text generation capabilities using model-based evaluations, specifically through MT-Bench [77], AlpacaEval 1.0 and 2.0 [37] (Section 4.1)
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
  - [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d46574e5baae5121180228223a11836-Paper-Conference.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > For question answering, we use AlpacaEval 2.0 (Li et al., 2023b; Dubois et al., 2024a;b) to assess model performance on 805 instructions. (Section 7.1)
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
- **Text generation quality** (construct): *measured_by*, 1 paper
  > We conduct comprehensive evaluations using AlpacaEval 2.0, Arena-Hard, MT-Bench, FLASK benchmarks for assessing the response quality across various dimensions.
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > Remarkably, on AlpacaEval 2 (Li et al., 2023c) and Arena-Hard (Li et al., 2024b), two LLM general problem-solving ability benchmarks, the model trained on 20K our synthetic instruction-response pairs, consistently outperforms models trained on significantly larger datasets... (Section 1)
  - [Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation](https://aclanthology.org/2025.acl-long.1136.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To understand the effect of α on model generalization, we measure the AE2 performance of various models with changing α. (Section 4.2. Results)
  - [AlphaPO: Reward Shape Matters for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25d/gupta25d.pdf)
- **Code generation** (behavioral indicator): *measured_by*, 1 paper
  > To test our hypothesis, we break down the prompts in Alpaca Eval 2.0 (Li et al., 2023) into different categories. ... We select four representative tasks: two are objective tasks that can be verified: mathematical reasoning or calculation (Math) and Coding...
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
- **Creative writing** (behavioral indicator): *measured_by*, 1 paper
  > To test our hypothesis, we break down the prompts in Alpaca Eval 2.0 (Li et al., 2023) into different categories. ... and the other two tasks are tasks that require modeling human open-ended preference: Creative writing and making personal recommendations (Recommendation).
  - [SIMPLEMIX: Frustratingly Simple Mixing of Off- and On-policy Data in Language Model Preference Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25au/li25au.pdf)
- **Open-ended instruction following** (behavioral indicator): *measured_by*, 1 paper
  > We employed three challenging benchmarks to evaluate the open-ended instruction-following task: MT-Bench (Zheng et al., 2023), AlpacaEval 2 (Li et al., 2023), and Arena-Hard (Li et al., 2024). (Section 5.1)
  - [Weights-Rotated Preference Optimization for Large Language Models](https://aclanthology.org/2025.emnlp-main.1329.pdf)

### Associated with
- **Verbosity bias** (construct), 1 paper
  > Additionally, the LC win rates of our cheats are generally higher than the raw win rates because of their short length, which highlights that AlpacaEval 2.0 is also not robust to length cheat.
  - [Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument), 1 paper
  > “We conducted human evaluations on the AlpacaEval2 and Arena-Hard datasets using the Gemma2-9B model.”
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **AlpacaEval** (measurement instrument), 1 paper
  > “AlpacaEval is done with the AlpacaEval2 library”
  - [Ladder-Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference with Communication Overlapping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bg/zhang25bg.pdf)
