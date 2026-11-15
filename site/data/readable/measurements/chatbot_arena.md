# Chatbot Arena
**Type:** Measurement instrument  
**Supporting papers:** 79  
**Also known as:** ChatBot Arena, CHATBOT ARENA, ChatArena, Chatarena, LLM Arena, LMsys arena, ChatbotArena, LM Arena, LMSYS Chatbot Arena  

## State of the Field

**What it is.** Across papers, Chatbot Arena is most commonly described as a crowdsourced evaluation platform or leaderboard for open-ended conversational tasks, where two anonymous model outputs are compared side by side, users cast pairwise preference votes, and Elo or related rankings are produced from these battles. Some authors instead refer to the underlying evaluation set, datasets, or prompts built from real-world user-assistant interactions and human preference labels, and one paper calls LM Arena, formerly LMSYS Chatbot Arena, a community-driven collection of such head-to-head matchups. A smaller line of work describes it as an evaluation framework or benchmark that uses LLMs to judge responses, and one paper uses the similar name ChatArena for a multi-agent language game framework.

**What it is claimed to measure.** Most measurement claims center on Human preference alignment and Conversational ability, with papers using Chatbot Arena to evaluate human preferences in open-ended, real-time, or multi-turn dialogue. It is linked to 5 constructs, most often Human preference alignment, Conversational ability, Multilingual understanding, Positional bias, and Reasoning, and to 5 behavioral indicators, most often Coding, Dialogue generation, Mathematical problem solving, and Multi-turn dialogue, while one paper relates it to Pairwise comparison. Some papers also say it evaluates models on code, math, multilingual understanding, and broader real-world use cases spanning topics such as reasoning.

**Space of uses.** In use, papers frequently position Chatbot Arena as a reference leaderboard or ground-truth source for relative system quality, and compare new judges, ranking methods, or synthetic evaluations against its human preference rankings. It is linked to 5 other instruments: AlpacaEval 2.0 and Arena-Hard are reported to correlate with Chatbot Arena, and Chatbot Arena is reported to correlate with LiveBench, LiveCodeBench, and WildBench. Some papers also evaluate on Chatbot Arena datasets or prompts, combine it with other evaluation sets, or report live user interactions on the platform.

**Concerns raised.** The clearest explicit concern is evaluation bias. One paper reports positional bias on Chatbot Arena, with some weak LLM judges consistently preferring the first response.

## Sources

**ChatBot Arena** (3 papers: [StackEval: Benchmarking LLMs in Coding Assistance](https://proceedings.neurips.cc/paper_files/paper/2024/file/4126a607bbe2836cb6ca0eb45b75618b-Paper-Datasets_and_Benchmarks_Track.pdf), [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf), [Improving Model Evaluation using SMART Filtering of Benchmark Datasets](https://aclanthology.org/2025.naacl-long.235.pdf))
> An evaluation framework that uses LLMs to judge model responses, often through pairwise comparisons.

**ChatArena** (3 papers: [Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf), [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf), [Learning to Discuss Strategically: A Case Study on One Night Ultimate Werewolf](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cea78701eb986f3ec357eb9b7c6badd-Paper-Conference.pdf))
> An evaluation set of real-world user-assistant interactions used for pairwise preference evaluation.

**Chatbot Arena** (7 papers: [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf), [Decoding Speculative Decoding](https://aclanthology.org/2025.naacl-long.328.pdf), [Language Models can Categorize System Inputs for Performance Analysis](https://aclanthology.org/2025.naacl-long.317.pdf), [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.617.pdf), [JuStRank: Benchmarking LLM Judges for System Ranking](https://aclanthology.org/2025.acl-long.34.pdf), [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf), [From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge](https://aclanthology.org/2025.emnlp-main.138.pdf))
> A crowdsourced evaluation platform where LLMs are evaluated through millions of pairwise comparisons based on human judgments in open-ended conversational tasks.

**CHATBOT ARENA** (1 paper: [RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf))
> A crowdsourcing platform where users compare outputs from two anonymous models side-by-side to vote for the better response, generating a public ELO ranking.

**Chatarena** (1 paper: [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf))
> A diverse, human-labeled dataset encompassing multiple language pairs used for comparative alignment analysis.

**LLM Arena** (1 paper: [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf))
> A public evaluation platform where language models compete in anonymous, randomized battles, with user votes determining the rankings.

**LMsys arena** (1 paper: [MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/461f1fd5f92e5ca95764a88304dc39f7-Paper-Conference.pdf))
> A benchmark platform that uses user voting and Elo-ranking to evaluate multimodal models.

**ChatbotArena** (2 papers: [Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf), [SkillVerse : Assessing and Enhancing LLMs with Tree Evaluation](https://aclanthology.org/2025.acl-long.437.pdf))
> An LLM evaluation platform and leaderboard where models are ranked based on pairwise comparisons from anonymous, crowdsourced human votes.

**LM Arena** (1 paper: [Position: AI Competitions Provide the Gold Standard for Empirical Rigor in GenAI Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sculley25a/sculley25a.pdf))
> A community-driven benchmark, also known as LMSYS Chatbot Arena, that collects a fresh source of novel test questions and human preference votes from users in head-to-head matchups between LLMs.

**LMSYS Chatbot Arena** (2 papers: [BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf), [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf))
> A crowdsourced evaluation platform where users chat with two anonymous language models and vote for the one they prefer, creating a large-scale human preference dataset.

## Relationships

### Chatbot Arena →
- **LiveBench** (measurement instrument): *correlates*, 1 paper
  > LiveBench has a 0.91 and 0.88 correlation with ChatBot Arena and Arena-Hard, respectively.
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **LiveCodeBench** (measurement instrument): *correlates*, 1 paper
  > Even then, our results are well correlated with findings from human evaluations like Chatbot-Arena
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **WildBench** (measurement instrument): *correlates*, 1 paper
  > “WILD-BENCH results demonstrate a strong correlation with the human-voted Elo ratings from Chatbot Arena on hard tasks.”
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)

### → Chatbot Arena
- **Human preference alignment** (construct): *measured_by*, 4 papers
  > The resulting dynamic benchmarks, i.e., MixEval and MixEval-Hard, exhibit significant correlations (0.93 and 0.96) with real-world user preference leaderboard (i.e., Chatbot Arena) and showcase high impartiality and efficiency.
  - [MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f34d7b4a03a3d80be8e72eb430dd81-Paper-Conference.pdf)
  - [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf)
  - [Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf)
  - [Improving Your Model Ranking on Chatbot Arena by Vote Rigging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/min25a/min25a.pdf)
- **Conversational ability** (construct): *measured_by*, 2 papers
  > We then report results from live interactions with users on the Chatbot Arena. (Section 7.3)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf)
- **Dialogue generation** (behavioral indicator): *measured_by*, 1 paper
  > Chatbot Arena is a benchmark platform designed for evaluating LLMs through interactive, randomised battles in a crowd-sourced manner. It allows for the assessment of LLMs in real-time dialogues with human participants. (Section 3.3)
  - [Weak-eval-Strong: Evaluating and Eliciting Lateral Thinking of LLMs with Situation Puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/914b372356d58d9e9357b29332cb8fdc-Paper-Conference.pdf)
- **Multilingual understanding** (construct): *measured_by*, 1 paper
  > The most popular one is the Chatbot Arena (Chiang et al., 2024b), which contains over one million user queries and evaluates models in various tasks such as code, math, and multilingual understanding. (Section 5)
  - [Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf)
- **Multi-turn dialogue** (behavioral indicator): *measured_by*, 1 paper
  > Chatbot Arena has become a cornerstone in LLM evaluation, offering rich datasets for ranking models in open-ended conversational tasks.
  - [A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > "The most popular one is the Chatbot Arena ... which contains over one million user queries and evaluates models in various tasks such as code, math, and multilingual understanding"
  - [Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > In contrast, ChatbotArena offers a broader set of real-world LLM use cases spanning diverse topics including language understanding, creative writing, reasoning, logic, and science. (Section 3.1)
  - [SkillVerse : Assessing and Enhancing LLMs with Tree Evaluation](https://aclanthology.org/2025.acl-long.437.pdf)
- **Positional bias** (construct): *measured_by*, 1 paper
  > We observed positional bias in some weak LLM judges on Chatbot Arena where the first response was consistently preferred, similar to (Zheng et al., 2023).
  - [SkillAggregation: Reference-free LLM-Dependent Aggregation](https://aclanthology.org/2025.acl-long.756.pdf)
- **Arena-Hard** (measurement instrument): *correlates*, 1 paper
  > Arena-Hard-Auto achieves stronger model separability, tighter confidence intervals, and achieve 98.6% correlation with Chatbot Arena rankings, making it a fast, reliable predictor of downstream model performance. (Section 1)
  - [From Crowdsourced Data to High-quality Benchmarks: Arena-Hard and Benchbuilder Pipeline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25h/li25h.pdf)
- **AlpacaEval 2.0** (measurement instrument): *correlates*, 1 paper
  > Here, we test on AlpacaEval 2.0 (Dubois et al., 2024), which has a Spearman correlation of 0.98 with Chatbot Arena while being cost-efficient. (Section 3.2)
  - [Improving Instruct Models for Free: A Study on Partial Adaptation](https://aclanthology.org/2025.emnlp-main.581.pdf)
- **Coding** (behavioral indicator): *measured_by*, 1 paper
  > "The most popular one is the Chatbot Arena ... which contains over one million user queries and evaluates models in various tasks such as code, math, and multilingual understanding"
  - [Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf)

### Associated with
- **Pairwise comparison** (behavioral indicator), 1 paper
  > LMSYS Chatbot Arena leverages (240,000) crowdsourced questions and (90,000) crowdsourced human votes to construct pair-wise win-rates
  - [BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf)
