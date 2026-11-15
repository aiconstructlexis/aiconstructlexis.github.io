# Open LLM Leaderboard
**Type:** Measurement instrument  
**Supporting papers:** 54  
**Also known as:** Huggingface Open Leaderboard, Open LLM Leaderboards, HuggingFace open LLM leaderboard, OpenLLM LeaderBoard, OpenLLM leaderboard, Hugging Face Open LLM Leaderboard, OpenLM leaderboard, HuggingFace Open LLM Leaderboard, Open-LLM, Open LLM leaderboard, LLM Leaderboard, Open-LLM Leaderboard, Open LLM Benchmarks, OPENLLM, OpenLLM Leaderboard  

## State of the Field

**What it is.** Most papers describe the Open LLM Leaderboard as a public HuggingFace leaderboard or evaluation suite for ranking open or open-access LLMs on standardized downstream or academic benchmarks. The prevailing framing is an aggregate suite over reasoning and knowledge tasks, with recurring task lists that include ARC, HellaSwag, MMLU, TruthfulQA, and GSM8K, though other papers describe different subsets or broader versions. Some papers also treat it as an evaluation methodology, including few-shot or zero-shot/few-shot setups, and refer to versions such as v1, v2, and OpenLLM Leaderboard 2.

**What it is claimed to measure.** Papers link it to 9 constructs and 3 behavioral indicators, so its reported measurement role is spread across many targets rather than centered on a single one. The most prominent construct links use it to measure general ability, truthfulness, alignment tax, commonsense reasoning, and instruction following ability, with four other construct links beyond these. Papers also describe the suite as giving a glimpse into model knowledge, reasoning, and truthfulness, and a smaller line of work uses it for three behavioral indicators.

**Space of uses.** In use, papers often position it as a general-purpose benchmark or aggregate proxy of model capabilities, either as a main comparison point or as an auxiliary check beside MT-Bench and AlpacaEval 2, with some pairings to Arena-Hard, LongBench, or Anthropic-HH. It is related to 11 instruments overall. Some papers also use its published scores, correctness data, or sample-wise evaluation files as inputs for separate analyses, and one paper notes adherence to the recommended evaluation harness protocols.

**Concerns raised.** One paper argues that the leaderboard primarily uses accuracy and does not take uncertainty into account. Another paper says models overfit on leaderboards like the OpenLLM Leaderboard.

## Sources

**Huggingface Open Leaderboard** (1 paper: [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf))
> A suite of benchmarks used to evaluate and rank open-source language models on a variety of downstream tasks.

**Open LLM Leaderboards** (1 paper: [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf))
> A public platform that ranks and evaluates the performance of various large language models on a standardized set of benchmarks.

**HuggingFace open LLM leaderboard** (1 paper: [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf))
> A widely recognized evaluation platform that compares LLM performance, primarily utilizing accuracy as the evaluation metric.

**OpenLLM LeaderBoard** (3 papers: [RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf), [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf), [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf))
> An evaluation suite that ranks and tracks the performance of open-source large language models on various benchmarks.

**OpenLLM leaderboard** (1 paper: [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf))
> An evaluation suite that aggregates model performance across a standard set of academic benchmarks to measure general reasoning and knowledge capabilities.

**OpenLLM Leaderboard** (3 papers: [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf), [Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf), [Decoding Speculative Decoding](https://aclanthology.org/2025.naacl-long.328.pdf))
> An evaluation suite comprising several standardized benchmarks used to assess the performance of large language models on various tasks.

**Hugging Face Open LLM Leaderboard** (1 paper: [PhyloLM: Inferring the Phylogeny of Large Language Models and Predicting their Performances in Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e28663712d5a3429a98918c3058f7b-Paper-Conference.pdf))
> An evaluation suite that ranks and tracks the performance of open-access LLMs on a set of standard benchmarks.

**OpenLM leaderboard** (1 paper: [Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f74d79573d71078848973009d0e99bdb-Paper-Conference.pdf))
> A public platform for evaluating and ranking the performance of large language models across a standardized suite of benchmarks.

**HuggingFace Open LLM Leaderboard** (2 papers: [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf), [Correlated Errors in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25e/kim25e.pdf))
> An evaluation framework that measures LLM performance across a standardized suite of diverse academic benchmarks.

**Open-LLM** (1 paper: [Concept-ROT: Poisoning Concepts in Large Language Models with Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb7baa005c239c1c7c4098c2a9e00450-Paper-Conference.pdf))
> Open-LLM benchmark used to assess the impact of poisoning on benign model performance.

**Open LLM Leaderboard** (4 papers: [SimPER: A Minimalist Approach to Preference Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf), [Distributional Preference Alignment of LLMs via Optimal Transport](https://proceedings.neurips.cc/paper_files/paper/2024/file/bce96750dcb64f3257ceabadf0b9c9bf-Paper-Conference.pdf), [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf), [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf))
> A public leaderboard by HuggingFace that evaluates large language models on a suite of standardized benchmarks.

**Open LLM leaderboard** (1 paper: [MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mencattini25a/mencattini25a.pdf))
> A public platform that ranks and evaluates large language models on various benchmarks, used in this paper as a source of model evaluation data for IRT parameter estimation.

**LLM Leaderboard** (1 paper: [CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25x/yang25x.pdf))
> Benchmark suite assessing large language models on six key tasks: AI2 Reasoning Challenge, HellaSwag, MMLU, TruthfulQA, Winogrande, and GSM8K, using the Eleuther AI Language Model Evaluation Harness.

**Open-LLM Leaderboard** (1 paper: [Intuitive Fine-Tuning: Towards Simplifying Alignment into a Single Process](https://aclanthology.org/2025.acl-long.6.pdf))
> An evaluation suite that ranks large language models based on their performance across a collection of standardized benchmarks.

**Open LLM Benchmarks** (1 paper: [JI2S: Joint Influence-Aware Instruction Data Selection for Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.26.pdf))
> A suite of standardized benchmarks used to evaluate the performance of large language models across a range of tasks.

**OPENLLM** (1 paper: [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.336.pdf))
> Benchmark suite for evaluating open-source large language models on a range of tasks including reasoning, knowledge, and instruction following.

## Relationships

### → Open LLM Leaderboard
- **Truthfulness** (construct): *measured_by*, 2 papers
  > These benchmarks give us a glimpse into model knowledge, reasoning, and truthfulness. (Section 4)
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 2 papers
  > Additionally, SPPO exhibits strong generalist abilities across different tasks, including MT-Bench, the Open LLM Leaderboard, and the more recent, more challenging benchmark, Arena-Hard.
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
  - [DCIS: Efficient Length Extrapolation of LLMs via Divide-and-Conquer Scaling Factor Search](https://aclanthology.org/2025.emnlp-main.767.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > Reasoning ability is measured via the Open LLM Leaderboard (Beeching et al., 2023) using the Language Model Evaluation Harness (Gao et al., 2023). (Section 3.2)
  - [MAIN: Mutual Alignment Is Necessary for instruction tuning](https://aclanthology.org/2025.emnlp-main.644.pdf)
- **Catastrophic forgetting** (behavioral indicator): *measured_by*, 1 paper
  > In this section, we show that GEM also helps mitigate forgetting and reduce alignment tax. We evaluate the models across six tasks: ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande, as listed on the OpenLLM leaderboard. (Section 6.2)
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
- **Alignment tax** (construct): *measured_by*, 1 paper
  > In this section, we show that GEM also helps mitigate forgetting and reduce alignment tax. We evaluate the models across six tasks: ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande, as listed on the OpenLLM leaderboard. (Section 6.2)
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > This evaluation suite measures LLM performance across six tasks: commonsense reasoning (Arc (Clark et al., 2018), HellaSwag (Zellers et al., 2019), Winogrande (Sakaguchi et al., 2021)), multi-task language understanding (MMLU (Hendrycks et al., 2020)), mimicking human falsehoods (TruthfulQA (Lin et al., 2021)), and math problem-solving (GSM8K (Cobbe et al., 2021)).
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > This evaluation suite measures LLM performance across six tasks: ... and math problem-solving (GSM8K (Cobbe et al., 2021)).
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Language proficiency** (construct): *measured_by*, 1 paper
  > The average score across the 6 tasks (Average column) is commonly used as an indicator of overall language proficiency. (Table 2)
  - [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > "we also confirm that our safety-tuned model still preserves general instruction-following capabilities: as shown in Table B.2, the performance on the six tasks in the Open LLM Leaderboard changes insignificantly with safety tuning."
  - [Learning Diverse Attacks on Large Language Models for Robust Red-Teaming and Safety Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e128701ceca0ba03658a305faf39deb-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > We started from two LLM leaderboards: (1) HuggingFace’s Open LLM Leaderboard 21; and (2) Stanford’s Holistic Evaluation of Language Models (Helm) (Liang et al., 2023). Both use questions from the Massive Multitask Language Understanding (MMLU) question-answering dataset (Hendrycks et al., 2020), with multiple choice questions and labeled correct answers. (Section 3.1).
  - [Correlated Errors in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25e/kim25e.pdf)
- **Instruction following ability** (construct): *measured_by*, 1 paper
  > To assess the effectiveness of the selected data, we adopt a multifaceted evaluation strategy targeting the instruction-following capabilities of fine-tuned models. First, we measure performance on several widely used benchmarks, including MT-Bench and the Open LLM benchmarks... (Section 5.1)
  - [JI2S: Joint Influence-Aware Instruction Data Selection for Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.26.pdf)

### Associated with
- **MMLU** (measurement instrument), 4 papers
  > We tested the benchmarks available on the hugging face open llm leaderboard which includes MMLU, ARC, Hellaswag, TruthfulQA, Winogrande and GSM8k (HuggingFaceH4) and only included open access models for which the scores are available on the leaderboard. (Section 2.6)
  - [PhyloLM: Inferring the Phylogeny of Large Language Models and Predicting their Performances in Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e28663712d5a3429a98918c3058f7b-Paper-Conference.pdf)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
  - [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GSM8K** (measurement instrument), 3 papers
  > We evaluate these LLMs using prompts of varying length, ambiguity, and context, sourced from the test set of ARC (Clark et al., 2018), GSM8K (Cobbe et al., 2021), HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021), Truthful QA (Lin et al., 2022), and Winogrande (Sakaguchi et al., 2019). These set the performance benchmarks on the HuggingFace Open LLM Leaderboard (Section 4.2)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
  - [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ARC** (measurement instrument), 2 papers
  > Table 2: Evaluation results on various tasks from the Huggingface Open Leaderboard v1 and v2. ... MMLU-PRO, BBH, MUSR, MATH, GSM8K, ARC
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurement instrument), 2 papers
  > Table 2: Evaluation results on various tasks from the Huggingface Open Leaderboard v1 and v2. ... MMLU-PRO, BBH, MUSR, MATH, GSM8K, ARC
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **TruthfulQA** (measurement instrument), 2 papers
  > We evaluate these LLMs using prompts of varying length, ambiguity, and context, sourced from the test set of ARC (Clark et al., 2018), GSM8K (Cobbe et al., 2021), HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021), Truthful QA (Lin et al., 2022), and Winogrande (Sakaguchi et al., 2019). These set the performance benchmarks on the HuggingFace Open LLM Leaderboard (Section 4.2)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
- **Uncertainty** (construct), 1 paper
  > Despite their usefulness, these leaderboards possess a significant limitation: They do not take into account the uncertainty of LLMs.
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLU-Pro** (measurement instrument), 1 paper
  > Table 2: Evaluation results on various tasks from the Huggingface Open Leaderboard v1 and v2. ... MMLU-PRO, BBH, MUSR, MATH, GSM8K, ARC
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
- **MuSR** (measurement instrument), 1 paper
  > Table 2: Evaluation results on various tasks from the Huggingface Open Leaderboard v1 and v2. ... MMLU-PRO, BBH, MUSR, MATH, GSM8K, ARC
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
- **lm-evaluation-harness** (measurement instrument), 1 paper
  > For the Open LLM Leaderboard, we adhere to the recommended Language Model Evaluation Harness (Gao et al., 2021) protocols. (Section 4.1)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **HellaSwag** (measurement instrument), 1 paper
  > We evaluate these LLMs using prompts of varying length, ambiguity, and context, sourced from the test set of ARC (Clark et al., 2018), GSM8K (Cobbe et al., 2021), HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021), Truthful QA (Lin et al., 2022), and Winogrande (Sakaguchi et al., 2019). These set the performance benchmarks on the HuggingFace Open LLM Leaderboard (Section 4.2)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
- **WinoGrande** (measurement instrument), 1 paper
  > We evaluate these LLMs using prompts of varying length, ambiguity, and context, sourced from the test set of ARC (Clark et al., 2018), GSM8K (Cobbe et al., 2021), HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2021), Truthful QA (Lin et al., 2022), and Winogrande (Sakaguchi et al., 2019). These set the performance benchmarks on the HuggingFace Open LLM Leaderboard (Section 4.2)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
- **TyDi QA** (measurement instrument), 1 paper
  > “We adopt ﬁve OpenLLM Leaderboard tasks as our benchmark for evaluation, including MMLU (Hendrycks et al., 2020), TruthfulQA (Lin et al., 2021), GSM (Cobbe et al., 2021), BBH (Suzgun et al., 2022), TydiQA (Clark et al., 2020).”
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
