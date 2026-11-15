# Contextual understanding
**Type:** Construct  
**Supporting papers:** 91  
**Also known as:** Context understanding, Contextual awareness, Context awareness, Context comprehension, Context-awareness, Contextual comprehension, Context-aware comprehension, Context-aware understanding  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats contextual understanding as a model ability to perceive, process, integrate, and use surrounding information so that responses, predictions, or judgments are coherent and task-appropriate. Most definitions agree on this broad framing, but they differ on what counts as context: ongoing dialogue history, preceding text, retrieved documents or external knowledge, long inputs with distractors, multimodal evidence about an image, scientific narrative structure, or socio-cultural, historical, and situational background. A smaller line of work defines it more narrowly through domain-specific decisions, such as differentiating between groups only when appropriate, judging whether answering a query is safe given context, or solving a puzzle from the supplied context without relying on external knowledge.

**Space of facets.** Papers use several labels for the construct, including context understanding, contextual awareness, context awareness, context comprehension, contextual comprehension, and context-aware understanding or comprehension. The most common distinctions are by source and scale of context, such as multi-turn or historical context, retrieved or external knowledge, long inputs with distractors, multimodal situational context, and culture- or situation-dependent interpretation. Some papers discuss it alongside reasoning or instruction following, and one paper describes it as going beyond superficial patterns or superficial restyling.

**Space of measurement.** Papers link contextual understanding to 13 measurement instruments and 6 behavioral indicators. Measurement is mostly benchmark-based: LAMBADA is explicitly described as evaluating contextual comprehension and long-range dependencies, while MMLU, BIG-Bench Hard, DROP, and GPQA are also among the most frequent instruments, plus 8 other instruments. Operationalizations also include context-sensitive task setups, for example judging a query's safety given context, identifying contextual integrity parameters in multiple-choice questions, or measuring performance with and without surrounding context, so the measurement space ranges from direct context-use tests to broader benchmarks that papers present as assessing context awareness.

**Links.** Several papers claim a causal relationship from contextual understanding to long-context understanding, and one of these also claims a causal relationship from contextual understanding to long-context generation. Single-paper causal claims also connect contextual understanding to reasoning, bias mitigation, schema matching, time series forecasting, proactivity, and legal compliance. Contextual understanding is also reported as related to in-context learning, sign language recognition, and sign language translation.

## Sources

**Context understanding** (6 papers: [Plug-and-Play Policy Planner for Large Language Model Powered Dialogue Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/29e8437db7b549160ce03d336ff66f65-Paper-Conference.pdf), [MKGL: Mastery of a Three-Word Language](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe03053bd2cf5b5c56de1e463bc53e1a-Paper-Conference.pdf), [FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf), [Beyond Sequences: Two-dimensional Representation and Dependency Encoding for Code Generation](https://aclanthology.org/2025.acl-long.308.pdf), [CASE-Bench: Context-Aware SafEty Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25ab/sun25ab.pdf), [Can LLMs Generate and Solve Linguistic Olympiad Puzzles?](https://aclanthology.org/2025.emnlp-main.969.pdf))
> The ability of a model to comprehend and integrate information from the ongoing dialogue history to inform its actions and responses.

**Contextual awareness** (5 papers: [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf), [Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs](https://aclanthology.org/2025.acl-long.341.pdf), [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf), [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf))
> The model's ability to understand and appropriately use the surrounding context, including retrieved information, when generating predictions.

**Contextual understanding** (12 papers: [Compressed Context Memory for Online Language Model Interaction](https://proceedings.iclr.cc/paper_files/paper/2024/file/97dc07f1253ab33ee514f395a82fa7cc-Paper-Conference.pdf), [Large Language Models to Enhance Bayesian Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/84b8d9fcb4e262fcd429544697e1e720-Paper-Conference.pdf), [Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b99d6cc40b05809c3d84b57a165448cd-Paper-Conference.pdf), [WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf), [AIMS.au: A Dataset for the Analysis of Modern Slavery Countermeasures in Corporate Statements](https://proceedings.iclr.cc/paper_files/paper/2025/file/3a33ae4d634b49b0866b4142a1f82a2f-Paper-Conference.pdf), [COVE: COntext and VEracity prediction for out-of-context images](https://aclanthology.org/2025.naacl-long.102.pdf), [Entropy-Based Decoding for Retrieval-Augmented Large Language Models](https://aclanthology.org/2025.naacl-long.236.pdf), [Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding in VLMs](https://aclanthology.org/2025.naacl-long.488.pdf), [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf), [HotelMatch-LLM: Joint Multi-Task Training of Small and Large Language Models for Efficient Multimodal Hotel Retrieval](https://aclanthology.org/2025.acl-long.30.pdf), [A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf), [Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.44.pdf))
> The latent ability of an LLM to process and integrate contextual information—such as problem descriptions, dataset attributes, and optimization history—into coherent and task-appropriate responses.

**Context awareness** (4 papers: [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf), [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf), [Context-Aware Hierarchical Taxonomy Generation for Scientific Papers via LLM-Guided Multi-Aspect Clustering](https://aclanthology.org/2025.emnlp-main.788.pdf), [DeCAP: Context-Adaptive Prompt Generation for Debiasing Zero-shot Question Answering in Large Language Models](https://aclanthology.org/2025.naacl-long.624.pdf))
> The ability of a language model to effectively perceive, process, and utilize information from across its entire input context, especially in long sequences.

**Context comprehension** (2 papers: [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf), [Are Large Language Models Chronically Online Surfers? A Dataset for Chinese Internet Meme Explanation](https://aclanthology.org/2025.emnlp-main.863.pdf))
> The ability to grasp the meaning and structure of long or sophisticated input contexts well enough to answer questions or retrieve relevant information.

**Context-awareness** (2 papers: [From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf), [Parenting: Optimizing Knowledge Selection of Retrieval-Augmented Language Models with Parameter Decoupling and Tailored Tuning](https://aclanthology.org/2025.acl-long.571.pdf))
> The model's ability to understand and utilize the surrounding context, including historical information, to generate relevant and coherent responses.

**Contextual comprehension** (3 papers: [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf), [Browsing Lost Unformed Recollections: A Benchmark for Tip-of-the-Tongue Search and Reasoning](https://aclanthology.org/2025.acl-long.406.pdf), [MUCAR: Benchmarking Multilingual Cross-Modal Ambiguity Resolution for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.760.pdf))
> The latent ability to use surrounding textual context to interpret or complete language accurately.

**Context-aware understanding** (1 paper: [SciEvent: Benchmarking Multi-domain Scientific Event Extraction](https://aclanthology.org/2025.emnlp-main.871.pdf))
> The ability to interpret scientific text by considering the surrounding narrative and structure, enabling the extraction of meaningful and non-conflicting information.

**Context-aware comprehension** (1 paper: [MemeArena: Automating Context-Aware Unbiased Evaluation of Harmfulness Understanding for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.890.pdf))
> The model's capacity to understand and reason about content by taking into account specific socio-cultural, historical, or situational contexts that influence interpretation, particularly in subjective domains like harmfulness.

## Relationships

### Contextual understanding →
- **Long-context understanding** (construct): *causes*, 2 papers
  > These results underscore MoICE's efficacy in enhancing LLMs' ability to understand and generate long contexts, both of which require high context awareness.
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 2 papers
  > These benchmarks assess different aspects of LLM emergent abilities: Lambada evaluates contextual comprehension, testing the model’s ability to understand long-range dependencies in text. (Section 4.2)
  - [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf)
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 2 papers
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > This information with logical relationships enables LLMs to deeply understand the contextual content by clearly perceiving these logical relationships, facilitating the quality and reliability of reasoning (Section 3.2.1).
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Long-context generation** (behavioral indicator): *causes*, 1 paper
  > These results underscore MoICE's efficacy in enhancing LLMs' ability to understand and generate long contexts, both of which require high context awareness.
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **Time series forecasting** (behavioral indicator): *causes*, 1 paper
  > In these scenarios, Context-Alignment paradigm provides a robust contextual prior, enabling accurate logical and structural understanding that enhances the potential of LLMs for cross-domain TS processing. (Section 4.5)
  - [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf)
- **Bias mitigation** (behavioral indicator): *causes*, 1 paper
  > To address these limitations of existing zero-shot debiasing methods, a novel approach is required that enables the LLM to consider the context and minimizes the propagation of bias from internal knowledge into the generated answers.
  - [DeCAP: Context-Adaptive Prompt Generation for Debiasing Zero-shot Question Answering in Large Language Models](https://aclanthology.org/2025.naacl-long.624.pdf)
- **Needle-in-a-Haystack** (measurement instrument): *measured_by*, 1 paper
  > We also conduct Needle-in-a-Haystack tests (gkamradt, 2023) to provide a comprehensive evaluation of both context awareness and extrapolation. (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **MMLU-Pro** (measurement instrument): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **GPQA** (measurement instrument): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **MATH** (measurement instrument): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **DROP** (measurement instrument): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Schema matching** (behavioral indicator): *causes*, 1 paper
  > This contextual understanding enables LLMs to effectively reason about schema hierarchies and identify potential matches. (Section 4)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > Contextual Understanding: the final score from MT-Bench. (Section 4.1).
  - [Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25c/liao25c.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > to demonstrate contextual understanding and general effectiveness of each model variant, we assess their performance using HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2020), and TruthfulQA (Lin et al., 2021b) benchmarks.
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > to demonstrate contextual understanding and general effectiveness of each model variant, we assess their performance using HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2020), and TruthfulQA (Lin et al., 2021b) benchmarks.
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **Proactivity** (construct): *causes*, 1 paper
  > This ability of context awareness (Schilit & Theimer, 1994) enables the proactive agent to interpret signals and proactively propose and execute tasks without explicit human instructions. (Section 1)
  - [Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://proceedings.iclr.cc/paper_files/paper/2025/file/75c37811e830bf029584b1c6fac17726-Paper-Conference.pdf)
- **Legal compliance** (construct): *causes*, 1 paper
  > Consequently, better context-understanding abilities further improve legal compliance, as indicated by the results of Table 2. (Section 5.2)
  - [PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance](https://aclanthology.org/2025.acl-long.518.pdf)

### Associated with
- **In-context learning** (construct), 1 paper
  > constraining their application in tasks demanding extensive contextual awareness, such as in-context learning [28, 46] (Introduction).
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **Sign language recognition** (behavioral indicator), 1 paper
  > All these tasks [ISLR, CSLR, and SLT] impose indispensable demands on the model’s fine-grained comprehension and context awareness capabilities. (Section 1)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
- **Sign language translation** (behavioral indicator), 1 paper
  > All these tasks [ISLR, CSLR, and SLT] impose indispensable demands on the model’s fine-grained comprehension and context awareness capabilities. (Section 1)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
