# Explanation generation
**Type:** Behavioral indicator  
**Supporting papers:** 110  
**Also known as:** Text explanation, Fallacy explanation, Plausibility explanation, Analogical explanation, Rule violation explanation, Justification generation, Wordplay generation, Justification production, Rationale generation, Reasoning generation, Classification rationale generation, Alert explanation, Anomaly explanation, Anomaly justification, Free-form explanation, Natural language explanation generation, Analysis generation, High-level justification generation, Tailored explanation generation, Label rationalization, Iterative reasoning, Free-text explanation generation, Prediction explanation  

## State of the Field

**Space of definitions.** Across the definitions, the dominant framing is the production of natural-language text that justifies an answer, label, decision, verdict, or action. Most papers treat it as an accompaniment to prediction, asking models to explain why a selected answer is correct, why other options are incorrect, or why a choice was made, for example why a product is good or bad for a user. Some formulations ask for the explanation before the final answer or score, often as a step-by-step reasoning path, while others ask for a post-hoc, free-form, concise, or otherwise human-readable summary. Success is described in task-specific terms, including whether the explanation is correct, complete and accurate, plausible relative to an alternative, or coherent, factual, and faithful.

**Variants.** The behavior is used in a wide range of settings, including recommendation, image and video reasoning, medical and clinical question answering, misinformation or fact-checking, and language-focused tasks. Papers also rename it in several recurring ways, most often as rationale generation or natural language explanation generation, with feedback, justification, and analysis generation appearing as smaller clusters. More specialized variants ask for explanations of product fit, fallacies, anomalies, rule violations, or a word's meaning in context.

**Space of elicitation and scores.** Papers link explanation generation to 2 measurement instruments. Human evaluation is the more common instrument, used as a human scoring protocol in which annotators rate explanation quality and, in some settings, agreement on generated rationales. VQA-X also measures it, appearing as a benchmark for natural language explanation generation in vision-language tasks.

**What it is taken as evidence of.** Papers most often connect explanation generation to interpretability and explainability and to reasoning. Several papers claim a causal relationship from explanation generation to interpretability and explainability, although another records that link as related rather than causal; the link to reasoning is also usually causal, though some work treats explanation and reasoning as related and even uses the terms interchangeably. Smaller lines of work claim a causal relationship from explanation generation to knowledge manipulation, report it as related to faithfulness, and record a related link from calibration to explanation generation rather than the reverse.

## Sources

**Explanation generation** (15 papers: [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf), [Towards Unified Multi-Modal Personalization: Large Vision-Language Models for Generative Recommendation and Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/297a7a54da76d95f02b04d957a53c7ba-Paper-Conference.pdf), [SocialGPT: Prompting LLMs for Social Relation Reasoning via Greedy Segment Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/047682108c3b053c61ad2da5a6057b4e-Paper-Conference.pdf), [Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf), [Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.182.pdf), [Exploring Large Language Models for Effective Rumor Detection on Social Media](https://aclanthology.org/2025.naacl-long.128.pdf), [LLMs Are Not Intelligent Thinkers: Introducing Mathematical Topic Tree Benchmark for Comprehensive Evaluation of LLMs](https://aclanthology.org/2025.naacl-long.161.pdf), [How Can We Diagnose and Treat Bias in Large Language Models for Clinical Decision-Making?](https://aclanthology.org/2025.naacl-long.114.pdf), [Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding](https://aclanthology.org/2025.emnlp-main.10.pdf), [AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset](https://aclanthology.org/2025.acl-long.96.pdf), [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf), [PCoT: Persuasion-Augmented Chain of Thought for Detecting Fake News and Social Media Disinformation](https://aclanthology.org/2025.acl-long.1215.pdf), [Polishing Every Facet of the GEM: Testing Linguistic Competence of LLMs and Humans in Korean](https://aclanthology.org/2025.acl-long.492.pdf), [Rubrik's Cube: Testing a New Rubric for Evaluating Explanations on the CUBE dataset](https://aclanthology.org/2025.acl-long.1160.pdf), [Which of These Best Describes Multiple Choice Evaluation with LLMs? A) Forced B) Flawed C) Fixable D) All of the Above](https://aclanthology.org/2025.acl-long.169.pdf))
> The observable task of generating natural language text that explains why a particular product is a good or bad match for a user.

**Text explanation** (1 paper: [Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf))
> Expanding a short surgical keystep into a more descriptive explanation of events, anatomy, and instruments.

**Fallacy explanation** (1 paper: [When LLMs Meet Cunning Texts: A Fallacy Understanding Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbfbf1a9adbcc29783475d2767f218e8-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of generating a natural language explanation that clarifies the fallacy, logical error, or humorous aspect within a given cunning text.

**Feedback generation** (3 papers: [Policy Improvement using Language Feedback Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4d4f7cf206bb00f9a38a5b6ae92cf79a-Paper-Conference.pdf), [Generating CAD Code with Vision-Language Models for 3D Designs](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf), [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf))
> The generation of explanatory text that not only classifies a behavior but also provides reasons for the classification.

**Plausibility explanation** (1 paper: [NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf))
> The observable task of generating a free-form text that justifies why a chosen hypothesis image is plausible or more plausible than an alternative.

**Analogical explanation** (1 paper: [A transfer learning framework for weak to strong generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa47ffc7b2033fd32d8b8734686f6ff4-Paper-Conference.pdf))
> The task of explaining complex subjects by generating responses that use analogies.

**Rule violation explanation** (1 paper: [SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49c1879ae366644ce2c17fb39ddea982-Paper-Conference.pdf))
> The task of generating a textual explanation for why a specific action in a video constitutes a rule violation.

**Wordplay generation** (1 paper: [A Reasoning-Based Approach to Cryptic Crossword Clue Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/andrews25a/andrews25a.pdf))
> The task of creating natural language explanations (wordplay) that justify how a candidate answer can be derived from a cryptic clue.

**Justification generation** (2 papers: [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf), [Analyzing values about gendered language reform in LLMs' revisions](https://aclanthology.org/2025.emnlp-main.1277.pdf))
> Producing a concise, readable summary that explains the reasoning and critical evidence behind a verdict.

**Justification production** (1 paper: [The Psychology of Falsehood: A Human-Centric Survey of Misinformation Detection](https://aclanthology.org/2025.emnlp-main.428.pdf))
> The task of generating explanations or justifications for a veracity prediction, often by summarizing or structuring evidence.

**Rationale generation** (5 papers: [Two Heads Are Better Than One: Dual-Model Verbal Reflection at Inference-Time](https://aclanthology.org/2025.emnlp-main.155.pdf), [BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf), [LlavaGuard: An Open VLM-based Framework for Safeguarding Vision Datasets and Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/helff25a/helff25a.pdf), [Sample Efficient Demonstration Selection for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/purohit25a/purohit25a.pdf), [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf))
> Producing free-form explanations or scoring rationales alongside an assessment decision.

**Reasoning generation** (1 paper: [Identification of Multiple Logical Interpretations in Counter-Arguments](https://aclanthology.org/2025.emnlp-main.326.pdf))
> The model's observable behavior of producing natural language justifications for its answers to predicate questions, intended to reflect its internal logical analysis.

**Classification rationale generation** (1 paper: [RD-MCSA: A Multi-Class Sentiment Analysis Approach Integrating In-Context Classification Rationales and Demonstrations](https://aclanthology.org/2025.emnlp-main.1100.pdf))
> Producing detailed, linguistically grounded descriptions of sentiment labels by analyzing representative examples, covering lexical patterns, semantic-pragmatic features, and domain associations.

**Alert explanation** (1 paper: [Primus: A Pioneering Collection of Open-Source Datasets for Cybersecurity LLM Training](https://aclanthology.org/2025.emnlp-main.527.pdf))
> Explaining detected security alerts in response to an instruction.

**Anomaly explanation** (1 paper: [CAVE : Detecting and Explaining Commonsense Anomalies in Visual Environments](https://aclanthology.org/2025.emnlp-main.1379.pdf))
> Providing a rationale for why a described situation is considered anomalous, based on underlying commonsense knowledge.

**Anomaly justification** (1 paper: [CAVE : Detecting and Explaining Commonsense Anomalies in Visual Environments](https://aclanthology.org/2025.emnlp-main.1379.pdf))
> Generating a plausible sequence of events or circumstances that could have led to the observed anomalous situation.

**Free-form explanation** (1 paper: [Do Large Language Models Understand Word Senses?](https://aclanthology.org/2025.emnlp-main.1720.pdf))
> The task of generating an unconstrained, natural language explanation of a target word's meaning in a given context.

**Natural language explanation generation** (4 papers: [Superlatives in Context: Modeling the Implicit Semantics of Superlatives](https://aclanthology.org/2025.naacl-long.160.pdf), [PRACTIQ: A Practical Conversational Text-to-SQL dataset with Ambiguous and Unanswerable Queries](https://aclanthology.org/2025.naacl-long.13.pdf), [Self-Critique and Refinement for Faithful Natural Language Explanations](https://aclanthology.org/2025.emnlp-main.427.pdf), [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf))
> Producing a fluent, natural language summary of SQL execution results to enhance user understanding.

**Analysis generation** (2 papers: [RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf), [SocioDojo: Building Lifelong Analytical Agents with Real-world Text and Time Series](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f7367f5686e6e1592e64209d172b91d-Paper-Conference.pdf))
> The observable act of producing a textual explanation or rationale before providing a final score or judgment.

**High-level justification generation** (1 paper: [SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cm/zhang25cm.pdf))
> Generating a textual explanation for why a particular driving action was chosen.

**Tailored explanation generation** (1 paper: [Agent-to-Agent Theory of Mind: Testing Interlocutor Awareness among Large Language Models](https://aclanthology.org/2025.emnlp-main.1471.pdf))
> Producing structured, adapted explanations (e.g., using bullet points or simplified logic) when the identity of the receiving model is known, especially for weaker solvers.

**Label rationalization** (1 paper: [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf))
> The process where a model is given a video, a question, and the correct label, and is prompted to generate a step-by-step explanation for how to arrive at that label.

**Iterative reasoning** (2 papers: [T-MAD: Target-driven Multimodal Alignment for Stance Detection](https://aclanthology.org/2025.emnlp-main.30.pdf), [Model-based Large Language Model Customization as Service](https://aclanthology.org/2025.emnlp-main.248.pdf))
> A cognitive-like process of progressively refining an internal representation or prediction over multiple steps to capture more nuanced semantic details and cross-modal relationships.

**Free-text explanation generation** (1 paper: [A Necessary Step toward Faithfulness: Measuring and Improving Consistency in Free-Text Explanations](https://aclanthology.org/2025.emnlp-main.797.pdf))
> The observable act of a model producing a natural language text that aims to justify or explain a prior prediction.

**Prediction explanation** (1 paper: [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf))
> Providing a justification for a model's output by referencing acoustic features or contextual cues present in the audio.

## Relationships

### Explanation generation →
- **Interpretability and explainability** (construct): *causes*, 4 papers
  > ...offering interpretable answers, as LLMs can generate language-based explanations for the decisions. (Abstract)
  - [SocialGPT: Prompting LLMs for Social Relation Reasoning via Greedy Segment Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/047682108c3b053c61ad2da5a6057b4e-Paper-Conference.pdf)
  - [RSVP: Reasoning Segmentation via Visual Prompting and Multi-modal Chain-of-Thought](https://aclanthology.org/2025.acl-long.715.pdf)
  - [PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation](https://aclanthology.org/2025.emnlp-main.747.pdf)
  - [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf)
- **Reasoning** (construct): *causes*, 3 papers
  > Large language models (LLMs) can enhance multi-step reasoning abilities by generating intermediate reasoning steps (i.e., rationale) before arriving at an answer (Wei et al., 2022). (Section 1)
  - [Self-Training Meets Consistency: Improving LLMs' Reasoning with Consistency-Driven Rationale Evaluation](https://aclanthology.org/2025.naacl-long.528.pdf)
  - [BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
- **Hallucination** (behavioral indicator): *causes*, 3 papers
  > produces more explanations matching golden explanations but also generates redundant QA pairs, potentially leading to hallucination issues
  - [MEQA: A Benchmark for Multi-hop Event-centric Question Answering with Explanations](https://proceedings.neurips.cc/paper_files/paper/2024/file/e560a0b22e4432003d0dba63ff8dc457-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf)
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 2 papers
  > For the human evaluation of Task 3, we mainly want to verify the effectiveness of the automatic GPT-4 score we use, therefore, we hire 3 evaluation annotators to rate LLMs’ explanations, with scores ranging from {1, 2, 3, 4, 5}. (Section 2.3)
  - [When LLMs Meet Cunning Texts: A Fallacy Understanding Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbfbf1a9adbcc29783475d2767f218e8-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [LlavaGuard: An Open VLM-based Framework for Safeguarding Vision Datasets and Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/helff25a/helff25a.pdf)
- **VQA-X** (measurement instrument): *measured_by*, 1 paper
  > Our Rapper achieves new state-of-the-art performance for both VQA-X (Park et al., 2018) and e-SNLI-VE (Kayser et al., 2021) on NLE generation. (Section 1)
  - [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator): *correlates*, 1 paper
  > models that exhibit superior performance in the Answer Selection task tend to generate more plausible explanations. (Section 3.2)
  - [When LLMs Meet Cunning Texts: A Fallacy Understanding Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbfbf1a9adbcc29783475d2767f218e8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Knowledge manipulation** (construct): *causes*, 1 paper
  > The key idea of KG-SFT is to generate high-quality explanations for each Q&A pair via a structured knowledge graph to enhance the knowledge comprehension and manipulation of LLMs.
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)

### Associated with
- **Label prediction** (behavioral indicator), 2 papers
  > Such domain insensitivity compromises their effectiveness, especially when balancing the dual demands of accurate label prediction and faithful rationale generation, which remains a challenge (Radhakrishnan et al., 2023). (Section 1).
  - [Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference](https://aclanthology.org/2025.acl-long.340.pdf)
  - [QCRD: Quality-guided Contrastive Rationale Distillation for Large Language Models](https://aclanthology.org/2025.emnlp-main.724.pdf)
- **Chain of thought** (behavioral indicator), 1 paper
  > Zelikman et al. (2022) introduced the the Self-Taught Reasoners method, used rationalization to generate chain-of-thought (CoT) reasoning (Sec. 5.2).
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
- **Tool use** (behavioral indicator), 1 paper
  > our proposed Tool-integrated Reasoning format interleaves rationales with program-based tool use. (Figure 2)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **Calibration** (construct), 1 paper
  > We observe that RG leads to more conservative confidence estimates and lower expected calibration error (2.1 with RG vs. 2.9 without RG), which indicate that it enables more accurate identification of knowledge gaps via reasoning (Section 5.2).
  - [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf)
- **Faithfulness** (construct), 1 paper
  > We evaluate the quality of our natural language explanations using two widely recognized metrics in explainable AI: faithfulness and simulatability.
  - [Explaining Differences Between Model Pairs in Natural Language through Sample Learning](https://aclanthology.org/2025.emnlp-main.1462.pdf)
