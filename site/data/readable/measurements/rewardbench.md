# RewardBench
**Type:** Measurement instrument  
**Supporting papers:** 81  
**Also known as:** Reward Bench, Reward-Bench  

## State of the Field

**What it is.** Across papers, RewardBench is most commonly described as a benchmark for evaluating reward models on preference judgments, often framed as prompt, chosen, rejected triples or binary preference tasks. Definitions repeatedly describe 2,985 tasks drawn from 23 subtasks or datasets, usually organized into Chat, Chat-Hard, Safety, and Reasoning; one paper also describes it as English-only and says the triples are human-validated. Smaller lines of work describe it more specifically as a public benchmark for generative judges on preference-related subtasks, or as an out-of-distribution benchmark for testing generalization.

**What it is claimed to measure.** Papers link RewardBench to 6 constructs and 2 behavioral indicators, so its reported measurement role is spread across several targets rather than confined to one. The prevailing usage is to measure Reasoning and Safety, and some papers also use it for Out-of-distribution generalization; among behavioral indicators, it is used for Pairwise comparison and Preference prediction, with 3 other construct links appearing less often. In these claims, papers describe reasoning through preferences over correct versus incorrect responses, safety through refusal versus compliance on unsafe requests, and some broader judgment or generalization evaluations.

**Space of uses.** Most papers position RewardBench as a main evaluation benchmark for reward models, and several also use it to characterize or rank reward models by empirical performance. It is related to 2 other instruments: JudgeBench is presented as a complement for difficult reasoning tasks, and RM-Bench is described as following RewardBench across domains. Some papers also place it alongside HH-RLHF and other public benchmarks in broader evaluation suites, rather than using it alone.

## Sources

**Reward-Bench** (1 paper: [Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf))
> A public benchmark for evaluating generative judges on preference-related sub-tasks.

**Reward Bench** (1 paper: [RainbowPO: A Unified Framework for Combining Improvements in Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf))
> A benchmark designed to evaluate the performance and quality of reward models used in preference optimization.

**RewardBench** (7 papers: [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf), [PILAF: Optimal Human Preference Sampling for Reward Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25g/feng25g.pdf), [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf), [Preference Learning Algorithms Do Not Learn Preference Rankings](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8ce770a6b25e603fbff4a37f9e31edc-Paper-Conference.pdf), [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf), [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf), [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf))
> A benchmark for evaluating reward models on preference-related judgments and reasoning-oriented reward assessment.

## Relationships

### → RewardBench
- **Reasoning** (construct): *measured_by*, 8 papers
  > RewardBench, which features a variety of prompts from categories such as Chat, Chat Hard, Safety, and Reasoning.
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
  - [Generative Reward Modeling via Synthetic Criteria Preference Learning](https://aclanthology.org/2025.acl-long.1297.pdf)
  - [Improving Model Alignment Through Collective Intelligence of Open-Source Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dr/wang25dr.pdf)
- **Safety** (construct): *measured_by*, 5 papers
  > RewardBench is a new benchmark designed to evaluate the capabilities and safety of reward models (Section 4).
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
  - [Improving Model Alignment Through Collective Intelligence of Open-Source Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dr/wang25dr.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 2 papers
  > We employ the primary dataset from RewardBench to evaluate the out-of-domain generalization capabilities of our reward models. (Section 4.3)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [HAF-RM: A Hybrid Alignment Framework for Reward Model Training](https://aclanthology.org/2025.acl-long.924.pdf)
- **Pairwise comparison** (behavioral indicator): *measured_by*, 1 paper
  > LM-as-a-judge. We benchmark our method on 23 datasets in the RewardBench4 (Lambert et al., 2024b) that can be categorized into four types: Chat, Chat-Hard, Safety, and Reasoning.
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Preference prediction** (behavioral indicator): *measured_by*, 1 paper
  > We use RewardBench (Lambert et al., 2024) as the test benchmark. (Section 4)
  - [MetaMetrics: Calibrating Metrics for Generation Tasks Using Human Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1b248453bca182b6138b8c14a75340d-Paper-Conference.pdf)
- **Coding ability** (construct): *measured_by*, 1 paper
  > RewardBench contains subsets that test RMs in targeted domains, including their coding ability, mathematical ability, and harmlessness. (Section 3.3)
  - [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://aclanthology.org/2025.emnlp-main.167.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > RewardBench contains subsets that test RMs in targeted domains, including their coding ability, mathematical ability, and harmlessness. (Section 3.3)
  - [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://aclanthology.org/2025.emnlp-main.167.pdf)
- **Evaluation ability** (construct): *measured_by*, 1 paper
  > To evaluate the judgment capabilities of our model, we conduct experiments on RewardBench (Lambert et al., 2024). (Section 1)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)

### Associated with
- **RM-Bench** (measurement instrument), 1 paper
  > Following Reward Bench (Lambert et al., 2024), RM-BENCH covers four key domains, namely, Chat, Code, Math, and Safety.
  - [RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style](https://proceedings.iclr.cc/paper_files/paper/2025/file/6da1eec80095dc5937f7716db15aca4b-Paper-Conference.pdf)
- **JudgeBench** (measurement instrument), 1 paper
  > Thus, JudgeBench offers a valuable complement to RewardBench for evaluating reward models on difficult tasks requiring reasoning. (Section 4.3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
