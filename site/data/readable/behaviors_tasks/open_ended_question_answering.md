# Open-ended question answering
**Type:** Behavioral indicator  
**Supporting papers:** 36  
**Also known as:** Open-ended answer generation, Free-form question answering, Free-text response generation, Free-form generation, Free-text question answering, Generative question answering  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is free-form answer generation: models produce natural-language responses to questions instead of selecting from fixed options or extracting an answer span. Most definitions also stress detailed or human-like responses, often for questions that do not have a single simple answer, while smaller strands narrow the task to long-form, non-factoid questions that require synthesis and coverage of multiple sub-topics, or to questions where multiple valid answers and perspectives are possible. Where papers spell out success criteria, they variously look for semantic correctness against reference answers, broad coverage in long-form responses, or natural-language answers and explanations.

**Variants.** Authors use several nearby labels for the same family of behavior, especially free-form question answering and free-form generation, with smaller variants called open-ended answer generation, free-text response generation, free-text question answering, and generative question answering. The settings range from long-context passage QA and general factual knowledge to long-form RAG, knowledge-graph QA with explicit reasoning paths and supporting facts, and multimodal cases with video, images, or multi-image dialogue; papers also place it in clinical, cultural, and Arabic open-ended instructional settings.

**Space of elicitation and scores.** Papers link it to 11 measurement instruments. The most frequently linked are Natural Questions, CVQA, EHRNoteQA, FairEval, and GSM8K, with 6 other instruments. These instruments are mostly datasets or benchmarks that elicit or score free-text answers, and they include general QA sets, open-ended evaluation benchmarks, as well as multimodal and domain-specific resources; some explicitly offer both open-ended and multiple-choice formats, and some papers also send the open-style response to an LLM-as-a-judge.

**What it is taken as evidence of.** Papers relate it to 2 constructs rather than converging on a single construct it reflects. One line of work relates it to truthfulness, describing free-form question answering as concentrating on truthfulness in open-ended general factual knowledge. Another paper relates knowledge application to open-ended question answering by using open-ended question-answering, alongside multiple-choice testing, to evaluate knowledge application abilities in real-world scenarios.

## Sources

**Open-ended question answering** (13 papers: [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://proceedings.iclr.cc/paper_files/paper/2024/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf), [MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf), [From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.346.pdf), [Dynamic Data Mixing Maximizes Instruction Tuning for Mixture-of-Experts](https://aclanthology.org/2025.naacl-long.80.pdf), [Do RAG Systems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage](https://aclanthology.org/2025.naacl-long.301.pdf), [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf), [Unlearning vs. Obfuscation: Are We Truly Removing Knowledge?](https://aclanthology.org/2025.emnlp-main.577.pdf), [Can Knowledge Graphs Make Large Language Models More Trustworthy? An Empirical Study Over Open-ended Question Answering](https://aclanthology.org/2025.acl-long.622.pdf), [CulFiT: A Fine-grained Cultural-aware LLM Training Paradigm via Multilingual Critique Data Synthesis](https://aclanthology.org/2025.acl-long.1092.pdf), [Influences on LLM Calibration: A Study of Response Agreement, Loss Functions, and Prompt Styles](https://aclanthology.org/2025.acl-long.188.pdf), [OmniAlign-V: Towards Enhanced Alignment of MLLMs with Human Preference](https://aclanthology.org/2025.acl-long.906.pdf), [Palm: A Culturally Inclusive and Linguistically Diverse Dataset for Arabic LLMs](https://aclanthology.org/2025.acl-long.1579.pdf), [SCAR: Data Selection via Style Consistency-Aware Response Ranking for Efficient Instruction-Tuning of Large Language Models](https://aclanthology.org/2025.acl-long.625.pdf))
> The task of providing comprehensive, detailed, and human-like responses to questions that do not have a predefined or fixed set of possible answers.

**Open-ended answer generation** (1 paper: [CausalChaos! Dataset for Comprehensive Causal Action Question Answering Over Longer Causal Chains Grounded in Dynamic Visual Scenes](https://proceedings.neurips.cc/paper_files/paper/2024/file/a89558069b44ae56ee0daf1f32aae1f6-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of generating a free-form natural language answer to a question based on a video, without being provided a set of options.

**Free-form question answering** (3 papers: [Semantic Density: Uncertainty Quantification for Large Language Models through Confidence Measurement in Semantic Space](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26d4fbaf7dfa115f1d4b3f104e26bce-Paper-Conference.pdf), [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf))
> Generating answers to questions without restricted formats or multiple-choice constraints.

**Free-text response generation** (1 paper: [Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf))
> Generating open-ended textual answers to questions without predefined options, used in LLM-as-a-judge evaluations.

**Free-form generation** (2 papers: [Protecting Privacy in Multimodal Large Language Models with MLLMU-Bench](https://aclanthology.org/2025.naacl-long.207.pdf), [The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models](https://aclanthology.org/2025.naacl-long.303.pdf))
> Generating an open-ended, natural language answer to a question based on provided context or internal knowledge.

**Free-text question answering** (1 paper: [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf))
> A specific form of question answering where the model must generate an open-ended, natural language response.

**Generative question answering** (1 paper: [Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b054fadf1ccd80b37d465f6082629934-Paper-Conference.pdf))
> The task of generating a free-form text answer to a question, rather than extracting an answer span from a provided context.

## Relationships

### Open-ended question answering →
- **Natural Questions** (measurement instrument): *measured_by*, 2 papers
  > Specifically, we consider the open-ended QA task, where the model is prompted to generate the answer in a declarative form given a question. To validate our method and its theoretical guarantee on controlling FDR-E, we create a dataset on textual entailment using the Natural Questions (NQ) dataset [17] for each GLM. (Section A.3.2).
  - [Selective Generation for Controllable Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a6815122f533193a022cbc41786c1cc-Paper-Conference.pdf)
  - [Influences on LLM Calibration: A Study of Response Agreement, Loss Functions, and Prompt Styles](https://aclanthology.org/2025.acl-long.188.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > We cover four open-ended quenstion-answering datasets: TriviaQA (Joshi et al., 2017), Sciq (Welbl et al., 2017), WikiQA (Yang et al., 2015), and NQ (Kwiatkowski et al., 2019). (Section 4.1)
  - [Influences on LLM Calibration: A Study of Response Agreement, Loss Functions, and Prompt Styles](https://aclanthology.org/2025.acl-long.188.pdf)
- **FairEval** (measurement instrument): *measured_by*, 1 paper
  > We evaluate ChatEval on two benchmarks, FairEval and Topical-Chat which represent the categories of open-ended question answer and dialogue response generation, respectively. (Section 3)
  - [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://proceedings.iclr.cc/paper_files/paper/2024/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf)
- **EHRNoteQA** (measurement instrument): *measured_by*, 1 paper
  > We offer EHRNoteQA in two formats: open-ended and multi-choice question answering, and propose a reliable evaluation method for each. (Abstract)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **CVQA** (measurement instrument): *measured_by*, 1 paper
  > “we made sure that CVQA is also convertible into free-text open-ended QA”
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > On the free-form generation tasks (GSM8K, TriviaQA and NQ), we calculate the exact match (EM) accuracy.
  - [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > We also tested open-ended question answering on MT-Bench (Chiang et al., 2023), a special case where Static scheduler is infeasible due to the absence of a validation set. (Section 5)
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)
- **SciQ** (measurement instrument): *measured_by*, 1 paper
  > We cover four open-ended quenstion-answering datasets: TriviaQA (Joshi et al., 2017), Sciq (Welbl et al., 2017), WikiQA (Yang et al., 2015), and NQ (Kwiatkowski et al., 2019). (Section 4.1)
  - [Influences on LLM Calibration: A Study of Response Agreement, Loss Functions, and Prompt Styles](https://aclanthology.org/2025.acl-long.188.pdf)
- **WikiQA** (measurement instrument): *measured_by*, 1 paper
  > We cover four open-ended quenstion-answering datasets: TriviaQA (Joshi et al., 2017), Sciq (Welbl et al., 2017), WikiQA (Yang et al., 2015), and NQ (Kwiatkowski et al., 2019). (Section 4.1)
  - [Influences on LLM Calibration: A Study of Response Agreement, Loss Functions, and Prompt Styles](https://aclanthology.org/2025.acl-long.188.pdf)
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 1 paper
  > we mainly used LLaVA v1.5 (Liu et al., 2024a) and LLaVA NeXT (Liu et al., 2024b) in 7B and 13B sizes and evaluated them on the LLaVA-Bench COCO and LLaVA-Bench Wild (Liu et al., 2023) datasets to assess open-ended generation quality.
  - [Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oh25a/oh25a.pdf)
- **LLaVA-Med** (measurement instrument): *measured_by*, 1 paper
  > we adopt LLaVA-Med instruction dataset (Li et al., 2024) as a domain-specific open-ended benchmark on the medical images and corresponding questions.
  - [Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oh25a/oh25a.pdf)

### Associated with
- **Truthfulness** (construct), 1 paper
  > We examine CRITIC across diverse tasks: free-form question answering concentrates on truthfulness related to open-ended general factual knowledge (Section 4)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Knowledge application** (construct), 1 paper
  > utilizing the two most widely used tasks: open-ended question-answering and multiple-choice testing. We aim to more accurately evaluate LLMs' knowledge application abilities in real-world scenarios
  - [Delving into the Reversal Curse: How Far Can Large Language Models Generalize?](https://proceedings.neurips.cc/paper_files/paper/2024/file/36b6180f3dab4025ba763e853b044814-Paper-Conference.pdf)
