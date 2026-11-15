# HELMET
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across papers, the prevailing usage is as a long-context benchmark for extended text processing tasks. Definitions describe it as application-centric and comprehensive, with a common description noting that it includes portions from RULER and ∞Bench; papers also describe it as covering seven categories of tasks, though one evaluation setup names five task types, synthetic recall, retrieval-augmented generation, many-shot in-context learning, passage re-ranking, and long-document QA, totaling 17 sub-tasks.

**What it is claimed to measure.** Papers link HELMET to 4 constructs and 4 behavioral indicators. The most recurrent measurement claims use it for in-context prediction and synthetic recall, and papers also report it as measuring document question answering and ranking; at the construct level, papers use it to measure length generalization, long-context understanding, long-range dependency modeling, and memory.

**Space of uses.** Papers most often use HELMET alongside RULER: one study presents it as a main benchmark and notes that it includes portions from RULER, while another evaluates models on HELMET and RULER together. A smaller line of work relates HELMET to HotpotQA, Natural Questions, and TriviaQA, with one paper describing those factoid QA tasks as curated by HELMET for long-context benchmarking with 128k input tokens.

## Sources

**HELMET** (3 papers: [A Silver Bullet or a Compromise for Full Attention? A Comprehensive Study of Gist Token-based Context Compression](https://aclanthology.org/2025.acl-long.241.pdf), [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf), [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf))
> A long-context benchmark that includes portions from RULER and ∞Bench, used to assess model performance on extended text processing tasks.

## Relationships

### → HELMET
- **In-context prediction** (behavioral indicator): *measured_by*, 3 papers
  > we present HELMET (How to Evaluate Long-context Models Effectively and Thoroughly). We curate a diverse set of application-centric long-context tasks across seven categories. Beyond widely adopted categories like ... we also add many-shot in-context learning (ICL)
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **Synthetic recall** (behavioral indicator): *measured_by*, 3 papers
  > we present HELMET (How to Evaluate Long-context Models Effectively and Thoroughly). We curate a diverse set of application-centric long-context tasks across seven categories. Beyond widely adopted categories like synthetic recall...
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **Long-context understanding** (construct): *measured_by*, 1 paper
  > In this section, we assess our method AgenticLU using a suite of evaluation tasks drawn from the HELMET long-context benchmark (Yen et al., 2024). (Section 6)
  - [Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.275.pdf)
- **Long-range dependency modeling** (construct): *measured_by*, 1 paper
  > Extensive experiments on the HELMET(Yen et al., 2024b) and RULER(Hsieh et al., 2024) benchmarks demonstrate that NExtLong significantly improves the model’s ability to capture and utilize long-range dependencies. (Section 1. Introduction)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Ranking** (behavioral indicator): *measured_by*, 1 paper
  > The evaluation spans five task types from the HELMET benchmark: synthetic recall, retrieval-augmented generation (RAG), many-shot in-context learning (ICL), passage re-ranking, and long-document QA, covering a total of 17 sub-tasks. (Section 4.1. Evaluation)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Document question answering** (behavioral indicator): *measured_by*, 1 paper
  > The evaluation spans five task types from the HELMET benchmark: synthetic recall, retrieval-augmented generation (RAG), many-shot in-context learning (ICL), passage re-ranking, and long-document QA, covering a total of 17 sub-tasks. (Section 4.1. Evaluation)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Memory** (construct): *measured_by*, 1 paper
  > To assess long-context memory and extrapolation ability, two benchmarks are adopted: ... an application-centric benchmark HELMET (Yen et al., 2024). (Section 1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)
- **Length generalization** (construct): *measured_by*, 1 paper
  > To assess long-context memory and extrapolation ability, two benchmarks are adopted: ... an application-centric benchmark HELMET (Yen et al., 2024). (Section 1)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)

### Associated with
- **HotpotQA** (measurement instrument), 1 paper
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **Natural Questions** (measurement instrument), 1 paper
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **TriviaQA** (measurement instrument), 1 paper
  > For testing on factoid QA tasks, we use HotpotQA (Yang et al., 2018), Natural Questions (NQ) (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017), as curated by HELMET (Yen et al., 2025) for long-context benchmarking with 128k input tokens. (Section 4.1)
  - [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf)
- **RULER** (measurement instrument), 1 paper
  > “For this category, we select multiple synthetic recall tasks from RULER (an extended version of NIAH; Hsieh et al., 2024) and also add a JSON KV retrieval task (Liu et al., 2023), which we find more challenging.”
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
