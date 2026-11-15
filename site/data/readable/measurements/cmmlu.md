# CMMLU
**Type:** Measurement instrument  
**Supporting papers:** 23  

## State of the Field

**What it is.** Most papers treat CMMLU as a comprehensive benchmark for evaluating knowledge and reasoning in Chinese, often under the name Chinese Massive Multitask Language Understanding. Several descriptions add that it covers 67 subjects from basic to advanced or professional levels, and one definition says it uses multiple-choice questions across diverse academic disciplines. A smaller set of papers frames it more specifically as Chinese language understanding or proficiency, while a few describe it differently, including as multilingual or multimodal, and one quoted passage mentions a 5-shot setting.

**What it is claimed to measure.** Across papers, its measurement claims are spread across 4 constructs and no behavioral indicators, rather than concentrating on a single target. The most frequently linked constructs are Chinese language understanding, general ability, reasoning, and generalization. Papers use it to assess "Chinese language understanding," to check that general capabilities are not compromised, and in one out-of-domain evaluation to test generalization.

**Space of uses.** CMMLU is usually used as one component of a broader evaluation suite, commonly alongside MMLU and also with C-Eval, GSM8K, Xiezhi, and ICLEval. Papers position it as the Chinese benchmark within larger benchmark mixes, and one study says it is used "to ensure that their general capabilities are not compromised after naturalness alignment" (Do Large Language Models have an English Accent? Evaluating and Improving the Naturalness of Multilingual LLMs). A smaller line of work uses it as a high-resource Chinese baseline for comparison with Ti-MMLU, and one paper uses it in 5-shot form.

## Sources

**CMMLU** (14 papers: [Do Large Language Models have an English Accent? Evaluating and Improving the Naturalness of Multilingual LLMs](https://aclanthology.org/2025.acl-long.193.pdf), [Streamlining Redundant Layers to Compress Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4b00a351b41358965613c118e87dc28c-Paper-Conference.pdf), [Data-Efficient Selection via Grammatical Complexity in Continual Pre-training of Domain-Specific LLMs](https://aclanthology.org/2025.emnlp-main.1121.pdf), [GRASP: Replace Redundant Layers with Adaptive Singular Parameters for Efficient Model Compression](https://aclanthology.org/2025.emnlp-main.1338.pdf), [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf), [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf), [TLUE: A Tibetan Language Understanding Evaluation Benchmark](https://aclanthology.org/2025.emnlp-main.1777.pdf), [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf), [Parameter Competition Balancing for Model Merging](https://proceedings.neurips.cc/paper_files/paper/2024/file/99fc8bc48b917c301a80cb74d91c0c06-Paper-Conference.pdf), [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf), [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf), [WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf), [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf), [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf))
> The Chinese Massive Multitask Language Understanding benchmark, used to evaluate a model's general capabilities in Chinese to ensure they are not compromised after alignment.

## Relationships

### → CMMLU
- **General ability** (construct): *measured_by*, 2 papers
  > our approach can largely improve the performance of Llama-3 (8B), including both the general abilities (+8.81 on C-Eval and +6.31 on CMMLU)
  - [Towards Effective and Efficient Continual Pre-training of Large Language Models](https://aclanthology.org/2025.acl-long.289.pdf)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **Chinese language understanding** (construct): *measured_by*, 2 papers
  > Each model’s performance was assessed using domain-specific benchmarks: CMMLU (Li et al., 2023) for Chinese language understanding
  - [Superpose Task-specific Features for Model Merging](https://aclanthology.org/2025.emnlp-main.210.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > We use zero-shot or few-shot learning to test the reasoning ability across five benchmarks, including MMLU (Hendrycks et al., 2021), CMMLU (Li et al., 2024a), Truthful-QA (Lin et al., 2021), GSM-PLUS (Li et al., 2024b), and GSM8K (Cobbe et al., 2021). (Section 4.3.1)
  - [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > To rigorously assess the generalization capabilities of merged checkpoints to unseen domains, we evaluated the out-of-domain (OOD) performance of various merging methods. Although merging weights were determined using the C-Eval dataset (in-domain, IND), we tested the merged models on three diverse OOD datasets: CMMLU, MMLU, and GSM8K. (Section 4.2)
  - [Maximizing Intermediate Checkpoint Value in LLM Pretraining with Bayesian Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bv/liu25bv.pdf)
