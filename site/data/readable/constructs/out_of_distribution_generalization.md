# Out-of-distribution generalization
**Type:** Construct  
**Supporting papers:** 55  
**Also known as:** Domain generalization, Out-of-distribution generalisation, Out-of-Distribution Generalization, OOD generalization, Out-of-domain generalization, Domain generalizability, Cross-category generalization, Policy transferability, OOD robustness, OOD Robustness, Out-of-distribution robustness, Distributional robustness  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this construct as a model's ability to maintain or transfer performance from source settings to test data, tasks, domains, or environments not seen during training or fine-tuning. Most formulations use near-equivalent labels such as domain generalization, out-of-domain generalization, or OOD robustness, while a smaller line of work emphasizes dynamic adaptation from context, structural generalization to new combinations, or the transferability of learned policies to new scenarios. Some authors describe it as a latent capacity, others as observable stability of performance, and one robustness-oriented framing narrows it to safety and compliance behavior under shifts in input queries.

**Space of facets.** Papers organize the construct mainly by the kind of shift involved: unseen target domains or datasets, held-out tasks or applications, unseen category splits within a domain, increasing train-test dissimilarity, and, in one robustness framing, input-level versus semantic-level shifts. The terminology overlaps heavily, with domain generalization, domain generalizability, OOD generalization, OOD robustness, out-of-distribution robustness, distributional robustness, cross-category generalization, and policy transferability used for closely related phenomena. One paper places it alongside invariance-based domain generalization, and a recurring contrast is with memorization, as some authors describe OOD cases as requiring structural understanding rather than partial memorization.

**Space of measurement.** Operationally, papers link the construct to 24 measurement instruments and 1 behavioral indicator. The most frequently linked instruments are RewardBench, 42D, ARC-Challenge, ARC-Easy, and AlpacaEval, plus 19 other instruments; these are benchmark-style datasets, and papers typically operationalize the construct as performance on designated OOD splits or held-out datasets, for example by comparing in-distribution and OOD test sets, evaluating unseen tasks, or withholding domains or categories. No human evaluation, LLM-as-a-judge, or probe instrument is linked, and the linked measurements largely match the dominant definition of retained performance under distribution shift.

**Links.** Papers most often connect it to in-context learning, with some claiming a causal relationship from in-context learning to out-of-distribution generalization and others treating the pair as related. One paper also claims a causal relationship from compositionality, and papers report it is related to generation diversity, invariance, and memorization. Three other constructs and one behavioral indicator are also linked, mostly through causal claims, and no correlation links are reported.

## Sources

**Domain generalization** (2 papers: [Nemesis: Normalizing the Soft-prompt Vectors of Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/010c855df402b443e0c16e5b7434e74c-Paper-Conference.pdf), [VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25h/zeng25h.pdf))
> The ability of a vision-language model to maintain or transfer performance from a source domain (e.g., ImageNet) to unseen or shifted target domains (e.g., ImageNet-V2, ImageNet-Sketch).

**Out-of-distribution generalization** (5 papers: [Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf), [Let's Verify Step by Step](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf), [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf), [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf))
> The model's ability to perform well on test data drawn from environments or distributions not seen during training, by leveraging contextual information to adapt dynamically.

**Out-of-distribution generalisation** (2 papers: [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf), [A new framework for evaluating model out-of-distribution generalisation for the biochemical domain](https://proceedings.iclr.cc/paper_files/paper/2025/file/b84adff45775e92a45f0cd87c37f5ce9-Paper-Conference.pdf))
> The ability of a model to maintain performance on inputs drawn from a different distribution than its training data.

**Out-of-Distribution Generalization** (1 paper: [Competition Dynamics Shape Algorithmic Phases of In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a635abfdd007c9a698410c8bbe5ebc33-Paper-Conference.pdf))
> The latent capacity to perform accurately on data distributions not encountered during training.

**OOD generalization** (1 paper: [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf))
> The ability to perform well on formalization problems drawn from distributions different from the training or in-domain benchmark data.

**Out-of-domain generalization** (1 paper: [When is Task Vector Provably Effective for Model Editing? A Generalization Analysis of Nonlinear Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb23cf87a9e04d7677b73c47acd060ef-Paper-Conference.pdf))
> The ability to perform effectively on new tasks or data distributions that were not seen during fine-tuning, achieved by forming a linear combination of existing task vectors.

**Domain generalizability** (1 paper: [Plug-in and Fine-tuning: Bridging the Gap between Small Language Models and Large Language Models](https://aclanthology.org/2025.acl-long.271.pdf))
> The ability of a model to maintain or improve performance when applied to unseen domains or datasets different from its training domain.

**Cross-category generalization** (1 paper: [Towards Robust ESG Analysis Against Greenwashing Risks: Aspect-Action Analysis with Cross-Category Generalization](https://aclanthology.org/2025.acl-long.723.pdf))
> The ability of a model to extract aspect-action pairs in sustainability categories not seen during training, reflecting robustness to intra-domain distribution shifts.

**Policy transferability** (1 paper: [EPO: Explicit Policy Optimization for Strategic Reasoning in LLMs via Reinforcement Learning](https://aclanthology.org/2025.acl-long.747.pdf))
> The extent to which a model's learned strategies can be successfully applied to new, unseen domains or scenarios.

**OOD robustness** (1 paper: [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to maintain performance on unusual or shifted data domains that differ from training distribution.

**OOD Robustness** (1 paper: [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf))
> The degree to which model performance remains stable when queried on samples potentially out-of-distribution relative to the training data.

**Out-of-distribution robustness** (1 paper: [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf))
> A specific facet of robustness concerning the model's ability to handle test data whose distributions significantly differ from the training data, including input-level and semantic-level shifts.

**Distributional robustness** (1 paper: [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf))
> The stability of a model's performance, particularly its safety and compliance behaviors, when the distribution of input queries changes.

## Relationships

### Out-of-distribution generalization →
- **RewardBench** (measurement instrument): *measured_by*, 2 papers
  > We employ the primary dataset from RewardBench to evaluate the out-of-domain generalization capabilities of our reward models. (Section 4.3)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [HAF-RM: A Hybrid Alignment Framework for Reward Model Training](https://aclanthology.org/2025.acl-long.924.pdf)
- **CNN/DailyMail** (measurement instrument): *measured_by*, 1 paper
  > To evaluate out-of-distribution (OOD) generalisation, we specify ... one or more out-of-distribution (OOD) test sets for each task... For summarisation, the ... OOD test set is the CNN/DailyMail test set (Section 5.1).
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 1 paper
  > To evaluate out-of-distribution (OOD) generalisation, we specify ... one or more out-of-distribution (OOD) test sets for each task... For instruction following, the ID test set is a new test set ... For the first OOD test sets, we use the AlpacaEval evaluation test set (Section 5.1).
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **AndroidControl** (measurement instrument): *measured_by*, 1 paper
  > ANDROIDCONTROL is the most diverse UI control dataset to date, including 14,548 unique tasks over 833 Android apps, thus allowing us to conduct in-depth analysis of the model performance in and out of the domain of the training data. (Abstract)
  - [On the Effects of Data Scale on UI Control Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/a79f3ef3b445fd4659f44648f7ea8ffd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **SST-2** (measurement instrument): *measured_by*, 1 paper
  > "we test on the OOD SST-2 [128] from [147], paired with unrelated images and those generated with the text prompts (Task R.3)."
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **CoGS** (measurement instrument): *measured_by*, 1 paper
  > “For the COGS dataset (Kim and Linzen, 2020), we evaluate the model’s in-distribution and out-of-distribution generalization performance”
  - [Initialization is Critical to Whether Transformers Fit Composite Functions by Reasoning or Memorizing](https://proceedings.neurips.cc/paper_files/paper/2024/file/19c145aaad40927c51f4d10eaa339c20-Paper-Conference.pdf)
- **Blocksworld** (measurement instrument): *measured_by*, 1 paper
  > Since all the exemplar candidates are with 3-7 blocks, we denote test examples with 3-7 blocks as in-distribution (ID) and 8-20 blocks as out-of-distribution (OOD). (Figure 6)
  - [Improving Large Language Model Planning with Action Sequence Similarity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b18c6549c77411d92e645027a25838a8-Paper-Conference.pdf)
- **SHP** (measurement instrument): *measured_by*, 1 paper
  > Beyond RewardBench, we also aim to test the out-of-distribution generalization ability of reward models including CrossEval (Zhong et al., 2024), QA Feedback (Wu et al., 2023) and SHP (Ethayarajh et al., 2022).
  - [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **IMDb** (measurement instrument): *measured_by*, 1 paper
  > To test this hypothesis [about generalizability], we conducted an experiment ... under conditions of domain shift. For this experiment, we used three text classification datasets. Specifically, we used IMDB, CR (Ding et al., 2008), and Tweet for sentiment classification. (Section 4.4)
  - [Plug-in and Fine-tuning: Bridging the Gap between Small Language Models and Large Language Models](https://aclanthology.org/2025.acl-long.271.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > To rigorously assess the generalization capabilities of merged checkpoints to unseen domains, we evaluated the out-of-domain (OOD) performance of various merging methods. Although merging weights were determined using the C-Eval dataset (in-domain, IND), we tested the merged models on three diverse OOD datasets: CMMLU, MMLU, and GSM8K. (Section 4.2)
  - [Maximizing Intermediate Checkpoint Value in LLM Pretraining with Bayesian Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bv/liu25bv.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **SVAMP** (measurement instrument): *measured_by*, 1 paper
  > Additionally, we include two mathematical reasoning datasets, i.e., SVAMP [12] and ASDiv [18], to evaluate the out-of-domain generalizability of the models fine-tuned on the data generated from GSM8K and MATH datasets.
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
- **PopQA** (measurement instrument): *measured_by*, 1 paper
  > For out-of-domain evaluation, we introduce three datasets that differ significantly in question style and information distribution: MuSiQue (Trivedi et al., 2022), Bamboogle (Press et al., 2022), and PopQA (Mallen et al., 2022). These datasets test the model’s generalization ability beyond the training domain. (Section 4.2.1)
  - [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 1 paper
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **SciQ** (measurement instrument): *measured_by*, 1 paper
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Reddit TL;DR** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the generalization ability of the aligned models on out-of-distribution data, we fine-tune the models using only posts from the relationship and relationship advice subreddits of the Reddit TL;DR (Stiennon et al., 2020) dataset. (Section 6)
  - [Variational Best-of-N Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/402542c2341e5d2eadc1dd0891275901-Paper-Conference.pdf)
- **HANS** (measurement instrument): *measured_by*, 1 paper
  > We used OOD evaluation datasets for NLI and paraphrase identification... for NLI, we employed HANS (McCoy et al., 2019)... making them suitable benchmarks for evaluating the OOD robustness of ICL. (Section 4.1)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
- **PAWS** (measurement instrument): *measured_by*, 1 paper
  > We used OOD evaluation datasets for NLI and paraphrase identification... for paraphrase identification, we used PAWS (Zhang et al., 1919)... making them suitable benchmarks for evaluating the OOD robustness of ICL. (Section 4.1)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
- **SciBench** (measurement instrument): *measured_by*, 1 paper
  > Among these, AIME-2024, HumanEval, HumanEval+, GPQA, and SciBench are from a totally different distributions compared to training data, serving to verify the generalization capability of MAS-GPT. (Section 4.1)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **ProofNet** (measurement instrument): *measured_by*, 1 paper
  > We also report the performance of the model trained only on LeanWorkbook for 24 iterations, excluding miniF2F-valid and proofnet-valid, demonstrating that the model trained with STP also generalizes to out-of-domain theorems. (Section 4.2)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **42D** (measurement instrument): *measured_by*, 1 paper
  > General-domain test sets: includes 42D and HardEN. These sets are designed to challenge models in diverse, unfamiliar, or out-of-distribution contexts. (Section 4.1)
  - [Towards General-Domain Word Sense Disambiguation: Distilling Large Language Model into Compact Disambiguator](https://aclanthology.org/2025.emnlp-main.45.pdf)
- **HardEN** (measurement instrument): *measured_by*, 1 paper
  > General-domain test sets: includes 42D and HardEN. These sets are designed to challenge models in diverse, unfamiliar, or out-of-distribution contexts. (Section 4.1)
  - [Towards General-Domain Word Sense Disambiguation: Distilling Large Language Model into Compact Disambiguator](https://aclanthology.org/2025.emnlp-main.45.pdf)
- **YAGS** (measurement instrument): *measured_by*, 1 paper
  > To assess generalization beyond the training distribution, we evaluated the FN 1.7 fine-tuned model (§3.2) on the two established out-of-domain datasets. YAGS (Hartmann et al., 2017) is a benchmark annotated with FN 1.5 frames... (Section 4.2)
  - [Do LLMs Encode Frame Semantics? Evidence from Frame Identification](https://aclanthology.org/2025.emnlp-main.1499.pdf)

### → Out-of-distribution generalization
- **In-context learning** (construct): *causes*, 4 papers
  > We argue that context is environment, and posit that in-context learning holds the key to better domain generalization. (Section 1)
  - [Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
  - [When can in-context learning generalize out of task distribution?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goddard25a/goddard25a.pdf)
- **Compositionality** (construct): *causes*, 1 paper
  > Large language models can solve tasks that were not present in the training set. This capability is believed to be due to in-context learning and skill composition. (Abstract)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > The emergent abilities of LLMs, especially in OOD scenarios, largely depends on the robustness of their representations (Section 3.4)
  - [Tri-Level Navigator: LLM-Empowered Tri-Level Learning for Time Series OOD Generalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78d9d035215039ab46e48c281e6a63d-Paper-Conference.pdf)
- **Action grounding** (behavioral indicator): *causes*, 1 paper
  > omitting the pre-training stage significantly degrades performance... These results highlight the critical importance of the data infrastructure for grounding data synthesis; with this infrastructure in place, we can easily improve OOD downstream performance simply by scaling the pre-training corpus. (Section 5.3)
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
- **Shortcut learning** (construct): *causes*, 1 paper
  > ...the model can rely on these ‘shortcuts’ and fail to generalize to out-of-distribution data. (Section 3.1)
  - [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.416.pdf)

### Associated with
- **Invariance** (construct), 1 paper
  > In the first category, domain generalization algorithms based on invariance (Muandet et al., 2013; Ganin et al., 2016; Peters et al., 2016; Arjovsky et al., 2019), illustrated in Figure 1a, regularize predictors h(xe i) to not contain any information about the environment e. (Section 2)
  - [Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)
- **Generation diversity** (construct), 1 paper
  > We demonstrate an inherent tradeoff between generalisation performance and output diversity when choosing between these methods (Section 7).
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Memorization** (construct), 1 paper
  > In fact, the small two-layer model we study has such a low capacity that it entirely skips the in-distribution generalization phase and immediately jumps from pure memorization to out-of-distribution generalization. (Section 4.1)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Reward overoptimization** (construct), 1 paper
  > “There are two prevailing explanations for why this phenomenon occurs. 1. OOD Robustness: In the classical RLHF pipeline, the RL objective (eq. (3)) is optimized using on-policy samples from πθ. This means that the reward function is continuously queried using unseen model samples which are potentially out-of-distribution.”
  - [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf)
