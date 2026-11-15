# Arena-Hard
**Type:** Measurement instrument  
**Supporting papers:** 81  
**Also known as:** Arena Hard, Arena-hard, ArenaHard, Arena Hard v0.1, Arena-Hard v0.1, arena-hard-v0.1, Arena-Hard-Auto, Arena-Hard-Auto-v0.1  

## State of the Field

**What it is.** Across papers, Arena-Hard is most commonly described as a hard benchmark of 500 prompts or queries, often drawn from challenging user queries or live Chatbot Arena data. The prevailing description emphasizes technical problem-solving and open-ended instruction-following, sometimes with pairwise comparisons against a baseline such as GPT-4-0314 using GPT-4 or GPT-4-Turbo as judge, while some authors instead describe it as a real-world chatbot evaluation set, a benchmark concentrated on coding and debugging, or a v0.1 dataset that also includes responses from 63 systems and about 32K instruction-response pairs. A smaller line of work discusses automated variants, Arena-Hard-Auto and Arena-Hard-Auto-v0.1, which use LLM judges, and one definition says they automate LMSYS Chatbot Arena evaluation with 89% agreement with human rankings.

**What it is claimed to measure.** Papers link Arena-Hard to 8 constructs and 6 behavioral indicators. The prevailing usage is to measure instruction following, often phrased as instruction following ability, and papers also use it for human preference alignment, conversational ability, general ability, and helpfulness. Taken together, the reported targets spread across several nearby framings rather than converging on a single construct.

**Space of uses.** Papers most often use Arena-Hard alongside MT-Bench and AlpacaEval 2.0 when reporting open-ended evaluation. They usually position it as a primary or widely adopted benchmark, though some call it a secondary measure of helpfulness or use Arena Hard v0.1 as a source of instructions and system responses for judge ranking. Separate instrument links report that Arena-Hard correlates with Chatbot Arena and LiveBench, and is related to human evaluation.

**Concerns raised.** Where papers raise concerns, they focus on topic skew. One reports an "excessive concentration" on coding and debugging tasks, accounting for over 57% of content, and another says the queries show a pronounced bias toward technical topics.

## Sources

**Arena-Hard** (8 papers: [Taming Overconfidence in LLMs: Reward Calibration in RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/29fb6e1456b3d8b57ede5c45aa2c6537-Paper-Conference.pdf), [Stronger Models are Not Always Stronger Teachers for Instruction Tuning](https://aclanthology.org/2025.naacl-long.224.pdf), [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf), [Binary Classifier Optimization for Large Language Model Alignment](https://aclanthology.org/2025.acl-long.93.pdf), [Principled Data Selection for Alignment: The Hidden Risks of Difficult Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25f/gao25f.pdf), [From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge](https://aclanthology.org/2025.emnlp-main.138.pdf), [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf), [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf))
> A benchmark containing challenging technical problem-solving queries, designed to have strong agreement with human preference rankings for model evaluation.

**Arena-hard** (1 paper: [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf))
> A real-world chatbot evaluation set used to validate instruction-following performance in more open-ended settings.

**Arena Hard** (3 papers: [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf), [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf), [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf))
> A benchmark that uses pairwise comparisons and human voting to evaluate the performance of aligned language models on challenging prompts.

**ArenaHard** (3 papers: [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf), [Quantification of Large Language Model Distillation](https://aclanthology.org/2025.acl-long.248.pdf), [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf))
> A benchmark sampling tasks from Chatbot Arena to evaluate LLMs, often concentrating on coding and debugging.

**Arena Hard v0.1** (1 paper: [JuStRank: Benchmarking LLM Judges for System Ranking](https://aclanthology.org/2025.acl-long.34.pdf))
> Dataset of 500 challenging instructions and responses from 63 systems, used to generate judge scores in the JuStRank benchmark.

**Arena-Hard v0.1** (1 paper: [Iterative Nash Policy Optimization: Aligning LLMs with General Preferences via No-Regret Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/4eef032250ac525903063cd760cb0480-Paper-Conference.pdf))
> A benchmark of 500 technical problem-solving questions used to compare model answers against GPT-4-0314 reference responses with GPT-4 Turbo judging pairwise outcomes.

**arena-hard-v0.1** (1 paper: [Re-evaluating Open-ended Evaluation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/57a009897ab00e2d811a4581ad1f7239-Paper-Conference.pdf))
> A dataset of 500 prompts selected specifically to be difficult and to effectively differentiate the performance of frontier large language models.

**Arena-Hard-Auto** (3 papers: [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf), [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf), [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf))
> A popular LLM-judge benchmark that conducts pairwise comparisons against a baseline model, using a Likert scale and chain-of-thought prompting to score outputs.

**Arena-Hard-Auto-v0.1** (1 paper: [“Give Me BF16 or Give Me Death”? Accuracy-Performance Trade-Offs in LLM Quantization](https://aclanthology.org/2025.acl-long.1304.pdf))
> Automated evaluation that uses an LLM to judge model responses to 500 complex prompts, replicating LMSYS Chatbot Arena with 89% agreement with human rankings, designed to assess chat and instruction-following capabilities.

## Relationships

### Arena-Hard →
- **LiveBench** (measurement instrument): *correlates*, 1 paper
  > LiveBench has a 0.91 and 0.88 correlation with ChatBot Arena and Arena-Hard, respectively.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Chatbot Arena** (measurement instrument): *correlates*, 1 paper
  > Arena-Hard-Auto achieves stronger model separability, tighter confidence intervals, and achieve 98.6% correlation with Chatbot Arena rankings, making it a fast, reliable predictor of downstream model performance. (Section 1)
  - [From Crowdsourced Data to High-quality Benchmarks: Arena-Hard and Benchbuilder Pipeline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25h/li25h.pdf)

### → Arena-Hard
- **Instruction following** (behavioral indicator): *measured_by*, 13 papers
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
- **Instruction following ability** (construct): *measured_by*, 9 papers
  > To explore AUTOIF on more natural Instruction-following scenario, we further introduce the complex instruction-following dataset InfoBench(Qin et al., 2024b), the general natural instruction evaluation set MT-Bench (Zheng et al., 2023) and the real-world chatbot evaluation set Arena-hard (Zheng et al., 2023) as cross domain validation. (Section 4).
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
  - [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
  - [Taming Overconfidence in LLMs: Reward Calibration in RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/29fb6e1456b3d8b57ede5c45aa2c6537-Paper-Conference.pdf)
  - [Stronger Models are Not Always Stronger Teachers for Instruction Tuning](https://aclanthology.org/2025.naacl-long.224.pdf)
  - [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf)
  - [R.I.P.: Better Models by Survival of the Fittest Prompts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25u/yu25u.pdf)
  - [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf)
  - [ConfPO: Exploiting Policy Model Confidence for Critical Token Selection in Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoon25b/yoon25b.pdf)
- **Human preference alignment** (construct): *measured_by*, 4 papers
  > Arena-Hard is a more challenging benchmark that closely aligns with the human preference ranking from Chatbot Arena
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
  - [Self-Boosting Large Language Models with Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf)
  - [ATLANTIS: Weak-to-Strong Learning via Importance Sampling](https://aclanthology.org/2025.acl-long.52.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Technical problem solving** (behavioral indicator): *measured_by*, 4 papers
  > “It spans 250 high-quality topic clusters including 500 well-defined technical problem-solving queries.”
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
  - [Bootstrapping Language Models with DPO Implicit Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4de96b9169aa869cc102afe31055e8-Paper-Conference.pdf)
  - [AMPO: Active Multi Preference Optimization for Self-play Preference Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25c/gupta25c.pdf)
  - [From Crowdsourced Data to High-quality Benchmarks: Arena-Hard and Benchbuilder Pipeline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25h/li25h.pdf)
- **Conversational ability** (construct): *measured_by*, 3 papers
  > In this section we evaluate the Jamba-1.5 models on two chatbot scenarios: Arena-Hard (Li et al., 2024b), a set of 500 challenging user queries that uses GPT4-Turbo as a judge, and WildBench (Lin et al., 2024)... (Section 7.3)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [DPO Meets PPO: Reinforced Token Optimization for RLHF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25b/zhong25b.pdf)
- **Helpfulness** (construct): *measured_by*, 3 papers
  > In addition, we also use AlpacaEval 2.0 Length Controlled [37] and Arena Hard [38] as secondary measures of helpfulness, following [33, 39].
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
  - [HelpSteer3: Human-Annotated Feedback and Edit Data to Empower Inference-Time Scaling in Open-Ended General-Domain Tasks](https://aclanthology.org/2025.acl-long.1246.pdf)
- **General ability** (construct): *measured_by*, 3 papers
  > Additionally, SPPO exhibits strong generalist abilities across different tasks, including MT-Bench, the Open LLM Leaderboard, and the more recent, more challenging benchmark, Arena-Hard.
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [Diverse Preference Learning for Capabilities and Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf)
  - [Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation](https://aclanthology.org/2025.acl-long.1136.pdf)
- **Alignment** (construct): *measured_by*, 2 papers
  > We evaluate alignment effectiveness using three benchmarks: ... (2) Arena-Hard
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
- **Code debugging** (behavioral indicator): *measured_by*, 1 paper
  > Conversely, ArenaHard, sampling 500 tasks from ChatbotArena, displays an excessive concentration on coding and debugging tasks, accounting for over 57% of its content. (Section 1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > We primarily evaluate all the models using two recent proposed instruction-following QA benchmarks: Arena-Hard (Li et al., 2024) and Wild-Bench(Lin et al., 2024).
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Text generation quality** (construct): *measured_by*, 1 paper
  > We conduct comprehensive evaluations using AlpacaEval 2.0, Arena-Hard, MT-Bench, FLASK benchmarks for assessing the response quality across various dimensions.
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Dialogue generation** (behavioral indicator): *measured_by*, 1 paper
  > These benchmarks assess the models’ conversational abilities across a diverse range of queries and are extensively used by the research community.
  - [AlphaDPO: Adaptive Reward Margin for Direct Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25af/wu25af.pdf)
- **Open-ended instruction following** (behavioral indicator): *measured_by*, 1 paper
  > We employed three challenging benchmarks to evaluate the open-ended instruction-following task: MT-Bench (Zheng et al., 2023), AlpacaEval 2 (Li et al., 2023), and Arena-Hard (Li et al., 2024). (Section 5.1)
  - [Weights-Rotated Preference Optimization for Large Language Models](https://aclanthology.org/2025.emnlp-main.1329.pdf)
- **Cross-domain generalization** (construct): *measured_by*, 1 paper
  > "we further introduce the complex instruction-following dataset InfoBench(Qin et al., 2024b), the general natural instruction evaluation set MT-Bench (Zheng et al., 2023) and the real-world chatbot evaluation set Arena-hard (Zheng et al., 2023) as cross domain validation."
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)

### Associated with
- **Human evaluation** (measurement instrument), 1 paper
  > “We conducted human evaluations on the AlpacaEval2 and Arena-Hard datasets using the Gemma2-9B model.”
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
