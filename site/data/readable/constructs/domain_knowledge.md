# Domain knowledge
**Type:** Construct  
**Supporting papers:** 48  
**Also known as:** Professional knowledge, Domain expertise, Specialized knowledge, Topical knowledge, Component type recognition, Expert knowledge application, Domain-specific knowledge, In-domain knowledge, Domain-specific expertise, Localized domain knowledge, Comprehensive knowledge, Expertise, Subject expertise, Professional expertise  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats domain knowledge as a latent understanding or repository of environment-specific or domain-specific concepts, facts, terminology, entities, and procedures that a model can access and apply within a field or task. Many definitions tie it to interpreting observations, constraints, or professional context and choosing appropriate actions or answers, for example having enough knowledge about Minecraft biomes, understanding terms such as "backlogging" and "lot-sizing," or bringing relevant background knowledge to mathematical modeling and multi-domain translation. A smaller line of work broadens the construct to professional or comprehensive knowledge across a wide spectrum of subjects, while other papers narrow it to deep domain expertise, localized Chinese knowledge, in-domain knowledge gained from fine-tuning, or the quality of a response showing expertise; the clearest differences are scope and whether the construct is framed as an internal model property or as demonstrated output quality.

**Space of facets.** Papers use several neighboring labels for similar territory, including domain-specific knowledge, professional knowledge, specialized knowledge, domain expertise, subject expertise, professional expertise, localized domain knowledge, and in-domain knowledge. Some treat it as one capability within larger bundles, appearing alongside numerical proficiency, long-range context understanding, and cause-and-effect reasoning in scientific question answering, alongside emotional intelligence, imagination, and sense of space in one reasoning breakdown, and as professional expertise among five fundamental capabilities. Other papers carve out narrower subforms such as topical knowledge distilled into a set of core factual sentences, component type recognition for circuit elements, and subject expertise that is explicitly contrasted with diagnosing student mistakes and pedagogical technique.

**Space of measurement.** Operationally, papers link domain knowledge to 8 measurement instruments and 2 behavioral indicators, and the dominant approach is performance on benchmarks or datasets for specialized tasks. The most frequently linked instrument is MMLU, used to measure a "knowledge reservoir," specialized knowledge across multiple domains, and comprehensive knowledge; other recurring instruments are DDXPlus for medical diagnosis, DiscoveryBench for tasks where some domains require domain knowledge to derive a hypothesis, MMAU for audio understanding and reasoning with domain-specific knowledge, and MMLU-STEM, plus 3 other instruments. These measures usually operationalize the construct through successful answering, diagnosis, discovery, or reasoning in domain-specific settings, which matches definitions centered on accessing and applying specialized knowledge.

**Links.** Beyond measurement, no correlational links are reported. One paper claims a causal relationship from machine reading comprehension to domain knowledge, stating that reading-comprehension texts provide domain knowledge that enhances domain-specific task performance. Separate papers claim causal relationships from domain knowledge, framed in one paper as professional knowledge, to creativity, and from domain knowledge to disambiguation ability, and another paper reports that domain knowledge is related to scientific question answering, where answers must also demonstrate numerical proficiency, long-range context understanding, and cause-and-effect reasoning.

## Sources

**Domain knowledge** (8 papers: [Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf), [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf), [SmartPlay : A Benchmark for LLMs as Intelligent Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/063d1fadbde557466bf5bcffe814a64e-Paper-Conference.pdf), [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/file/c2f71567cd53464161cab3336e8fc865-Paper-Datasets_and_Benchmarks_Track.pdf), [DiscoveryBench: Towards Data-Driven Discovery with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d70af566e69f1dfb687791ecf955e28-Paper-Conference.pdf), [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.675.pdf), [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf), [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf))
> Knowledge of environment-specific concepts and entities needed to interpret observations and choose appropriate actions.

**Professional knowledge** (2 papers: [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf), [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf))
> The model's encoded repository of information across a wide spectrum of specialized subjects, ranging from elementary to advanced professional levels.

**Domain-specific knowledge** (7 papers: [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf), [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf), [DA-Ada: Learning Domain-Aware Adapter for Domain Adaptive Object Detection](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb71b5567ee985e0a4cee54ade19275c-Paper-Conference.pdf), [ClimaQA: An Automated Evaluation Framework for Climate Question Answering Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3eff068e195daace49955348de9f8398-Paper-Conference.pdf), [TrimLLM: Progressive Layer Dropping for Domain-Specific LLMs](https://aclanthology.org/2025.acl-long.33.pdf), [Agent Reviewers: Domain-specific Multimodal Agents with Shared Memory for Paper Review](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25p/lu25p.pdf), [RewardDS: Privacy-Preserving Fine-Tuning for Large Language Models via Reward Driven Data Synthesis](https://aclanthology.org/2025.emnlp-main.223.pdf))
> The ability to access and apply factual knowledge in specialized domains such as health and science, which require background understanding and quantitative reasoning.

**Domain expertise** (2 papers: [CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf), [QualBench: Benchmarking Chinese LLMs with Localized Professional Qualifications for Vertical Domain Evaluation](https://aclanthology.org/2025.emnlp-main.303.pdf))
> The possession of deep, specialized knowledge in a particular scientific field, enabling comprehension and application of complex concepts.

**Specialized knowledge** (1 paper: [MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/abbbb25cddb2c2cd08714e6bfa2f0634-Paper-Conference.pdf))
> The latent ability to answer questions requiring domain-specific factual or conceptual knowledge across multiple subjects.

**Topical knowledge** (1 paper: [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf))
> The latent, overall understanding or "theory" a language model possesses about a specific subject area, which can be distilled into a set of core factual statements.

**Component type recognition** (1 paper: [LaMAGIC2: Advanced Circuit Formulations for Language Model-Based Analog Topology Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25b/chang25b.pdf))
> The model's ability to understand and differentiate between various types of circuit components (e.g., switches, capacitors, inductors) to correctly learn circuit structures.

**Expert knowledge application** (1 paper: [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability of a model to apply specialized, domain-specific knowledge, such as in making medical diagnoses.

**In-domain knowledge** (1 paper: [UnCo: Uncertainty-Driven Collaborative Framework of Large and Small Models for Grounded Multimodal NER](https://aclanthology.org/2025.emnlp-main.388.pdf))
> The specialized knowledge a model acquires by being fine-tuned on a specific, narrow dataset, allowing it to capture domain-specific conventions and patterns.

**Domain-specific expertise** (1 paper: [AraEval: An Arabic Multi-Task Evaluation Suite for Large Language Models](https://aclanthology.org/2025.emnlp-main.1679.pdf))
> The model's proficiency and specialized knowledge within particular professional or academic fields.

**Localized domain knowledge** (1 paper: [QualBench: Benchmarking Chinese LLMs with Localized Professional Qualifications for Vertical Domain Evaluation](https://aclanthology.org/2025.emnlp-main.303.pdf))
> The latent ability of a model to understand and apply domain-specific knowledge that is grounded in the Chinese sociopolitical, regulatory, and professional context, enabling accurate performance on localized qualification tasks.

**Comprehensive knowledge** (1 paper: [Model Unlearning via Sparse Autoencoder Subspace Guided Projections](https://aclanthology.org/2025.emnlp-main.1348.pdf))
> The breadth and depth of a model's general knowledge across a wide range of academic and professional subjects.

**Expertise** (1 paper: [Multi-Domain Explainability of Preferences](https://aclanthology.org/2025.emnlp-main.736.pdf))
> The quality of a response demonstrating specialized knowledge or skill in a particular field.

**Subject expertise** (1 paper: [MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities of LLM Tutors](https://aclanthology.org/2025.emnlp-main.11.pdf))
> The model's underlying knowledge and mastery of the subject matter being taught, in this case, mathematics.

**Professional expertise** (1 paper: [Probing and Boosting Large Language Models Capabilities via Attention Heads](https://aclanthology.org/2025.emnlp-main.1450.pdf))
> The latent ability to demonstrate domain-specific knowledge and reasoning in specialized fields such as medicine or law.

## Relationships

### Domain knowledge →
- **MMLU** (measurement instrument): *measured_by*, 3 papers
  > We measure this knowledge reservoir using the Massive Multitask Language Understanding dataset (MMLU) (Hendrycks et al., 2021). (Section 4.1)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
  - [MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/abbbb25cddb2c2cd08714e6bfa2f0634-Paper-Conference.pdf)
  - [Model Unlearning via Sparse Autoencoder Subspace Guided Projections](https://aclanthology.org/2025.emnlp-main.1348.pdf)
- **PubHealth** (measurement instrument): *measured_by*, 1 paper
  > To investigate this further [how LLMs possess the capability to access domain-specific factual knowledge], we sample claims from PubHealth (Kotonya & Toni, 2020) in the public health domain and SciFact (Wadden et al., 2022) in the science domain. (Section 2.1)
  - [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **SciFact** (measurement instrument): *measured_by*, 1 paper
  > To investigate this further [how LLMs possess the capability to access domain-specific factual knowledge], we sample claims from PubHealth (Kotonya & Toni, 2020) in the public health domain and SciFact (Wadden et al., 2022) in the science domain. (Section 2.1)
  - [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **Creativity** (construct): *causes*, 1 paper
  > By analyzing these enhanced creation cases with perfect reasoning information, we found that some reasoning tasks involving Professional Knowledge influence the next creation tasks. (Section 5.1).
  - [ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)
- **DDXPlus** (measurement instrument): *measured_by*, 1 paper
  > To assess LLMs’ continuous improvement in applying expert knowledge, we use the DDXPlus [23] dataset, where agents must make a medical diagnosis out of 49 diagnoses based on patient profiles detailing their symptoms. (Section 3.2)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLU-STEM** (measurement instrument): *measured_by*, 1 paper
  > Compared to pretraining just on raw data, a model pretrained on MIND-OWM shows significant boost in mathematical reasoning (GSM8K: +13.42%, MATH: +2.30%), including superior performance in specialized knowledge (MMLU: +4.55%, MMLU-STEM: +4.28%)
  - [MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/abbbb25cddb2c2cd08714e6bfa2f0634-Paper-Conference.pdf)
- **MMAU** (measurement instrument): *measured_by*, 1 paper
  > MMAU emphasizes advanced perception and reasoning with domain-specific knowledge, challenging models to tackle tasks akin to those faced by experts. (ABSTRACT)
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **DiscoveryBench** (measurement instrument): *measured_by*, 1 paper
  > “Some of our tasks, for instance, archaeology, require domain knowledge to derive a particular hypothesis.”
  - [DiscoveryBench: Towards Data-Driven Discovery with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d70af566e69f1dfb687791ecf955e28-Paper-Conference.pdf)
- **MathTutorBench** (measurement instrument): *measured_by*, 1 paper
  > Therefore, MATHTUTORBENCH is divided into three categories: math expertise which evaluates the subject-matter expertise of the tutor... (Section 1)
  - [MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities of LLM Tutors](https://aclanthology.org/2025.emnlp-main.11.pdf)
- **Disambiguation ability** (construct): *causes*, 1 paper
  > This scarcity limits their translation capabilities and prevents them from effectively acquiring cross-domain knowledge, which leads to translation ambiguities. (Section 1)
  - [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf)

### → Domain knowledge
- **Machine reading comprehension** (behavioral indicator): *causes*, 1 paper
  > the utilization of reading comprehension texts provides domain knowledge that enhances performance in domain-specific tasks. (Section 6)
  - [Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf)

### Associated with
- **Scientific question answering** (behavioral indicator), 1 paper
  > Task 1: ScienceQ&A Generation (LLMgen) Generates a synthesized summary response A to a research question Q using abstracts from the top N relevant papers. It must demonstrate (1) domain knowledge, (2) numerical proficiency, (3) long-range context understanding, and (4) cause-and-effect reasoning (Wadden et al., 2020). (Section 2)
  - [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://aclanthology.org/2025.acl-long.675.pdf)
