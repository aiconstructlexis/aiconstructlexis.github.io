# MQuAKE
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** MQUAKE  

## State of the Field

**What it is.** Across the papers, MQuAKE is most commonly described as a benchmark or dataset for knowledge editing on multi-hop knowledge questions, especially question-answering tasks that require reasoning over edited facts. Definitions also frame it as testing whether edited knowledge propagates to related facts and as evaluating knowledge editing generalization through multi-hop questions. Another paper describes each case as a multi-hop question built from a chain of single-hop subquestions, while some authors describe variants by hop count, from 2 to 4, by the position of the knowledge used in the questions, and in one definition by temporal knowledge.

**What it is claimed to measure.** Papers link it to one behavioral indicator and three constructs, so its reported measurement role is spread across several targets rather than centered on one. It is used to measure Multi-hop question answering, with papers reporting Multi-hop Accuracy and Hop-wise Answering Accuracy for performance on the benchmark, and it is also reported as measuring Multi-hop reasoning, Context faithfulness, and Portability. In the portability framing, papers describe it as evaluating whether modified knowledge can be applied effectively to related content such as multi-hop reasoning.

**Space of uses.** Papers use it both as a main evaluation benchmark and as an auxiliary dataset in additional experiments. One line of work mainly uses MQuAKE as the multi-hop reasoning knowledge editing dataset, while other papers place it alongside Counterfact, LongformEvaluation, and KnowEdit for extra evaluations. Papers do not link it directly to another measurement instrument.

## Sources

**MQUAKE** (4 papers: [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf), [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf), [Reasons and Solutions for the Decline in Model Performance after Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f588e59e9ae6138d3ea9e4fdaa7e040-Paper-Conference.pdf), [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark for evaluating model editing on multi-hop knowledge questions.

**MQuAKE** (1 paper: [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf))
> Multi-hop knowledge editing benchmark that evaluates models on question-answering tasks requiring reasoning over edited facts, with versions varying in hop count and temporal knowledge.

## Relationships

### → MQuAKE
- **Multi-hop question answering** (behavioral indicator): *measured_by*, 2 papers
  > MQUAKE (Multi-hop Question Answering for Knowledge Editing) is a knowledge editing dataset focusing on the abovementioned multi-hop question answering tasks proposed in Zhong et al. (2023), where every case of MQUAKE is a multi-hop question made by a chain of single-hop subquestions. (Section 2.1)
  - [MQuAKE-Remastered: Multi-Hop Knowledge Editing Can Only Be Advanced with Reliable Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/f782860c2a5d8f675b0066522b8c2cf2-Paper-Conference.pdf)
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **Multi-hop reasoning** (construct): *measured_by*, 1 paper
  > experiments show that CaKE enables more accurate and consistent use of edited knowledge across related reasoning tasks, achieving an average improvement of 20% in multi-hop reasoning accuracy on the MQuAKE dataset (Abstract).
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **Context faithfulness** (construct): *measured_by*, 1 paper
  > "We use LLAMA2-7B-CHAT and LLAMA2-13B-CHAT as baseline models to conduct experiments on MQUAKE ... This verifies whether knowledge has been properly edited and effectively demonstrates LLMs’ context-faithfulness."
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Portability** (construct): *measured_by*, 1 paper
  > MQuAKE (Zhong et al., 2023) is a multi-hop benchmark... Portability evaluates the robustness of the generalization of the edit, evaluating whether the modified knowledge can be applied effectively to related content (e.g. Multi-Hop Reasoning).
  - [REACT: Representation Extraction And Controllable Tuning to Overcome Overfitting in LLM Knowledge Editing](https://aclanthology.org/2025.emnlp-main.860.pdf)
