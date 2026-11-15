# Causal reasoning
**Type:** Construct  
**Supporting papers:** 42  
**Also known as:** Causal inference, Cause-and-effect reasoning, Causation understanding, Attribution understanding, Causal consistency, Causal understanding, Causal relationship modeling, Commonsense causal reasoning, Commonsense and causal reasoning  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats causal reasoning as a latent ability to identify or infer cause-and-effect relations between events or variables. Most definitions keep it task-facing, grounding the construct in textual, video, narrative, driving, or everyday contexts, for example determining which object activates a device, explaining an anomalous event, or choosing the most plausible cause, effect, or next event. Several definitions extend it beyond relation identification to distinguishing causation from correlation and reasoning with interventions, counterfactuals, or confounding. A smaller line recasts it as a model-level property, either understanding the underlying causal structure of an environment or maintaining causal consistency between factual and counterfactual answers.

**Space of facets.** Papers organize the construct into overlapping subareas rather than a single fixed taxonomy. Recurring partitions include causal discovery and inference, counterfactual causal reasoning, and commonsense causal reasoning; another formulation lists causal discovery, cause attribution, and causal effect estimation as causal reasoning tasks, and one benchmark places cause-and-effect reasoning within logical reasoning. The literature also uses nearby names for overlapping material, including causal inference, cause-and-effect reasoning, causation understanding, attribution understanding, causal understanding, causal relationship modeling, and commonsense and causal reasoning. Several papers explicitly contrast causal reasoning with correlation-based recall or general reasoning, reserving causal reasoning for interventions, counterfactuals, or underlying causal structure.

**Space of measurement.** Operationalization is benchmark-centered: papers link causal reasoning to 6 measurement instruments and 6 behavioral indicators. The instrument side consists of dataset-style benchmarks, including COPA, ACRE, COPAL-ID, CREPE, and NExT-QA, plus 1 other instrument; in the papers, COPA tests commonsense causal alternatives, ACRE evaluates causal induction through "blicket" detection, COPAL-ID is an Indonesian causal reasoning dataset, and the video QA benchmarks demand causal and temporal reasoning. This generally matches the dominant definitions that cast the construct as identifying cause-effect relations in text, video, or everyday scenarios. Broader definitions that foreground interventions, counterfactuals, confounding, or causal consistency appear alongside these benchmarks, rather than through additional named instruments in the recorded links.

**Links.** Papers link causal reasoning to 6 behavioral indicators and 10 constructs. The most recurrent related link is to counterfactual reasoning, with 12 other related constructs or indicators also reported. Separately, one paper claims a causal relationship from causal reasoning to robustness, and another claims causal relationships from it to coherence and empathetic response generation. No correlational link is recorded.

## Sources

**Causal reasoning** (15 papers: [Can Large Language Models Infer Causation from Correlation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b75a7339dfb256ee4b4bec028a6890b-Paper-Conference.pdf), [Causal Modelling Agents: Causal Graph Discovery through Synergising Metadata- and Data-driven Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe90657b12193c7b52a3418bdc351807-Paper-Conference.pdf), [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf), [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf), [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf), [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf), [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf), [MLLM-Bench: Evaluating Multimodal LLMs with Per-sample Criteria](https://aclanthology.org/2025.naacl-long.256.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf), [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf), [ACCESS : A Benchmark for Abstract Causal Event Discovery and Reasoning](https://aclanthology.org/2025.naacl-long.49.pdf), [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.622.pdf), [Uncertainty in Causality: A New Frontier](https://aclanthology.org/2025.acl-long.396.pdf), [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf), [MovieCORE: COgnitive REasoning in Movies](https://aclanthology.org/2025.emnlp-main.66.pdf))
> The ability to infer cause-and-effect relationships from observing events and object interactions in a video, such as determining which object activates a device.

**Causal inference** (1 paper: [Limits of Transformer Language Models on Learning to Compose Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e797d5139ad94fc2dc2080c09119f29-Paper-Conference.pdf))
> The ability to infer cause-and-effect relationships from data, identified as an area where LLMs exhibit failures.

**Cause-and-effect reasoning** (1 paper: [OlympicArena: Benchmarking Multi-discipline Cognitive Reasoning for Superintelligent AI](https://proceedings.neurips.cc/paper_files/paper/2024/file/222d2eaf24cf8259a35d6c7130d31425-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to identify and establish causal relationships between events, understanding reasons and their consequences.

**Causation understanding** (1 paper: [Advancing Video Anomaly Detection: A Concise Review and a New Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3c5af1f56fc73eef1ba0f442739f5ca-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability to infer cause-and-effect relationships from contextual information, such as identifying the reasons for an anomalous event in a video.

**Attribution understanding** (1 paper: [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf))
> The ability to identify cause-and-effect relations in a video, including causal explanations and counting-related attribution questions.

**Causal consistency** (1 paper: [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf))
> The property that a model's answers to factual and counterfactual questions about the same context are logically coherent and correctly reflect the underlying causal relationships.

**Causal understanding** (1 paper: [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf))
> The latent ability of a system to comprehend the underlying causal structure of an environment, distinct from reflecting mere correlations.

**Causal relationship modeling** (1 paper: [LLM Enhancers for GNNs: An Analysis from the Perspective of Causal Mechanism Identification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25o/gao25o.pdf))
> The latent ability of a model to capture and represent true cause-and-effect dependencies between variables in the data, as defined by a high-level causal model.

**Commonsense causal reasoning** (2 papers: [ACCESS : A Benchmark for Abstract Causal Event Discovery and Reasoning](https://aclanthology.org/2025.naacl-long.49.pdf), [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.622.pdf))
> The ability to reason about causality in everyday situations, playing a vital role in developing a mental model of reality.

**Commonsense and causal reasoning** (1 paper: [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf))
> The ability to infer plausible causes, effects, or next events from everyday situations using common-sense world knowledge.

## Relationships

### Causal reasoning →
- **COPA** (measurement instrument): *measured_by*, 3 papers
  > The Choice of Plausible Alternatives (COPA) dataset is specifically designed to evaluate causal reasoning abilities in natural language processing models.
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.622.pdf)
- **ACRE** (measurement instrument): *measured_by*, 1 paper
  > The ACRE dataset (Zhang et al., 2021) evaluates how well vision systems perform causal induction (Section 4.1).
  - [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf)
- **CREPE** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our LLM cascade approaches on six datasets, covering... (3) causal reasoning, including CREPE (Zhang et al., 2023). (Section 3.1)
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > A better approximation of the underlying causal model generally translates to more robust agents, implying that world models should be causality-aware
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **NExT-QA** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on three popular VideoQA datasets: NExT-QA, STAR, and IntentQA (Xiao et al., 2021; Wu et al., 2021; Li et al., 2023a), which demand both causal and temporal reasoning abilities.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
- **STAR** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on three popular VideoQA datasets: NExT-QA, STAR, and IntentQA (Xiao et al., 2021; Wu et al., 2021; Li et al., 2023a), which demand both causal and temporal reasoning abilities.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
- **Coherence** (construct): *causes*, 1 paper
  > causal reasoning is pivotal for maintaining coherent and specific empathetic interactions (Section 5.2)
  - [ECC: An Emotion-Cause Conversation Dataset for Empathy Response](https://aclanthology.org/2025.emnlp-main.306.pdf)
- **Empathetic response generation** (behavioral indicator): *causes*, 1 paper
  > The ablation study highlights the critical role of cause labels in the CAER model’s performance... the absence of cause labels (w/o C) leads to a more significant decline in both language quality and lexical variety. (Section 5.2)
  - [ECC: An Emotion-Cause Conversation Dataset for Empathy Response](https://aclanthology.org/2025.emnlp-main.306.pdf)
- **COPAL-ID** (measurement instrument): *measured_by*, 1 paper
  > COPAL-ID (Wibowo et al., 2023) is an Indonesian causal reasoning dataset written from scratch by native speakers in both standard and Jakartan Indonesian, a widely spoken dialect. (Section 5.2.1)
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1426.pdf)

### Associated with
- **Causal discovery** (behavioral indicator), 3 papers
  > Causal Reasoning tasks include causal discovery, cause attribution, and causal effect estimation [30, 58, 65]. (Section 2.2)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.622.pdf)
- **Counterfactual reasoning** (construct), 2 papers
  > Counterfactual reasoning is an essential task of causal reasoning. (Section 2.2)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
  - [Language Models as Causal Effect Generators](https://aclanthology.org/2025.emnlp-main.107.pdf)
- **Video question answering** (behavioral indicator), 2 papers
  > Wang et al. (2023b) and Ko et al. (2023) try to leverage LLaMA’s (Touvron et al., 2023) knowledge of temporal and causal reasoning to address the complexities of VideoQA.
  - [ReasVQA: Advancing VideoQA with Imperfect Reasoning Process](https://aclanthology.org/2025.naacl-long.82.pdf)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
- **Visual reasoning** (construct), 1 paper
  > Our task suite encompasses a comprehensive set of perceptual and cognitive tasks, including summarization, perception (recall, tracking), visual reasoning (spatial, temporal, predictive, causal, counterfactual), and navigation (room-to-room, object retrieval) tasks. (Section 2.1)
  - [HourVideo: 1-Hour Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/5f2809607f692d79a01c05c43d702883-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Causal inference** (behavioral indicator), 1 paper
  > Causal Reasoning tasks include causal discovery, cause attribution, and causal effect estimation [30, 58, 65]. (Section 2.2)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
- **Reasoning** (construct), 1 paper
  > Reasoning is a cognitive process that involves drawing conclusions, making judgments, or forming inferences based on facts or premises. This process has been explored from various perspectives. ... Causal reasoning [26] focuses on discerning the relationship between a cause and its effect, aiming to understand how certain events can impact other.
  - [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf)
- **Memorization** (construct), 1 paper
  > we will focus on causal reasoning as it provides us with a clear distinction between recall and reasoning1: the former is limited to inferring statistical correlations, whereas the latter involves working with interventions and counterfactuals (Pearl, 2000).
  - [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf)
- **Counterfactual question answering** (behavioral indicator), 1 paper
  > “causal reasoning through counterfactual question answering is lacking”
  - [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf)
- **Narrative understanding** (construct), 1 paper
  > struggle with causal reasoning derived from aspect, raising concerns about their ability to fully comprehend narratives. (Abstract)
  - [How LLMs Comprehend Temporal Meaning in Narratives: A Case Study in Cognitive Evaluation of LLMs](https://aclanthology.org/2025.acl-long.1415.pdf)
- **Structured reasoning** (construct), 1 paper
  > STRICTA breaks down the assessment into a graph of interconnected reasoning steps drawing on causality theory (Pearl, 1995).
  - [STRICTA: Structured Reasoning in Critical Text Assessment for Peer Review and Beyond](https://aclanthology.org/2025.acl-long.1107.pdf)
- **Scientific question answering** (behavioral indicator), 1 paper
  > Task 1: ScienceQ&A Generation (LLMgen) Generates a synthesized summary response A to a research question Q using abstracts from the top N relevant papers. It must demonstrate (1) domain knowledge, (2) numerical proficiency, (3) long-range context understanding, and (4) cause-and-effect reasoning (Wadden et al., 2020). (Section 2)
  - [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.675.pdf)
- **Physical world understanding** (construct), 1 paper
  > Therefore, we would expect an improvement in causal reasoning to carry with it improvement on intuitive physics as well. (Section 3.4)
  - [Testing the Limits of Fine-Tuning for Improving Visual Cognition in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schulze-buschoff25a/schulze-buschoff25a.pdf)
- **Planning** (construct), 1 paper
  > “LLMs have recently shown great promise in planning and reasoning applications. These tasks demand robust systems, which arguably require a causal understanding of the environment.”
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
