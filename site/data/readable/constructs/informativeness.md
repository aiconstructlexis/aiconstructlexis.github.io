# Informativeness
**Type:** Construct  
**Supporting papers:** 28  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats informativeness as the extent to which an output provides relevant, useful, sufficiently detailed information, often with an added expectation of completeness. Many definitions phrase this as adequate or engaging detail in a coherent plot, relevant and complete commentary, or summaries that capture all relevant and key details without omission, and one definition explicitly anchors the judgment in human evaluation. A smaller line of work narrows it to preserving useful non-conflicting content during revision, to reasoning steps that add new and non-redundant information, or to information-dense latent factors, synthetic samples, and even harmful responses; the main variation is the object being judged and whether novelty or non-redundancy is part of the criterion.

**Space of facets.** Papers do not offer a single taxonomy, but a recurring breakdown equates informativeness with relevance and completeness, and sometimes with being insightful. Other papers systematize it through novelty and concision, describing informative steps as adding new, relevant information without repetition, and informative summaries as capturing essential event information while not being overly verbose. Informativeness is also positioned beside fluency and coherence as one of several generation criteria, and beside truthfulness in evaluation settings, rather than using those terms interchangeably.

**Space of measurement.** Papers link informativeness to 4 measurement instruments and no behavioral indicators. The most common operationalizations are Human evaluation and LLM-as-a-judge, followed by the TruthfulQA benchmark and the FreshWiki dataset: papers report manual ratings of informativeness, judge models or GPT-4 informative scores, TruthfulQA's INFO metric, and dataset performance in informativeness and verifiability. These operationalizations mostly score outputs directly, which matches definitions centered on useful, relevant, and complete information, though some evaluations pair informativeness with truthfulness, fluency, coherence, or verifiability.

**Links.** Papers link informativeness to 2 constructs. Several papers report that it is related to Truthfulness, noting both that unassessed informativeness can coincide with misleadingly high truthfulness scores and that a truthful answer may still be not informative, for example "I have no comment." One paper claims a causal relationship from informativeness to Harmlessness; its evidence states that informativeness, together with actionability, is an attribute in inducing harm when a jailbroken response is followed by individuals without specialized knowledge.

## Sources

**Informativeness** (10 papers: [Language Model Decoding as Direct Metrics Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf), [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b0d4b9d3dc41b36cad1d36ddd27858ab-Paper-Conference.pdf), [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf), [MiCEval: Unveiling Multimodal Chain of Thought's Quality via Image Description and Reasoning Steps](https://aclanthology.org/2025.naacl-long.504.pdf), [Latent Factor Models Meets Instructions: Goal-conditioned Latent Factor Discovery without Task Supervision](https://aclanthology.org/2025.naacl-long.554.pdf), [Bridging the Gap between Expert and Language Models: Concept-guided Chess Commentary Generation and Evaluation](https://aclanthology.org/2025.naacl-long.481.pdf), [DTELS: Towards Dynamic Granularity of Timeline Summarization](https://aclanthology.org/2025.naacl-long.136.pdf), [uMedSum: A Unified Framework for Clinical Abstractive Summarization](https://aclanthology.org/2025.acl-long.134.pdf), [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf), [CondenseLM: LLMs-driven Text Dataset Condensation via Reward Matching](https://aclanthology.org/2025.emnlp-main.65.pdf))
> The extent to which generated text provides adequate, engaging detail in a coherent plot according to human judgment.

## Relationships

### Informativeness →
- **TruthfulQA** (measurement instrument): *measured_by*, 2 papers
  > TruthfulQA (Lin et al., 2022) is perhaps the most popular benchmark to evaluate truthfulness in LLMs, a benchmark to assess the truthfulness and informativeness of LLMs by focusing on imitative falsehoods. (Section 1)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 2 papers
  > We perform a manual evaluation of 400 responses for truthfulness and informativeness... (Section 3.2.1)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [Explaining Differences Between Model Pairs in Natural Language through Sample Learning](https://aclanthology.org/2025.emnlp-main.1462.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > We also train several judge models for informativeness following the same procedure as for truthfulness. (Section 3.2.4)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **FreshWiki** (measurement instrument): *measured_by*, 1 paper
  > We conduct extensive experiments on the FreshWiki dataset and our newly constructed WikiStart dataset, demonstrating that MOG achieves state-of-the-art performance in both informativeness and verifiability. (Section 1)
  - [Hierarchical Memory Organization for Wikipedia Generation](https://aclanthology.org/2025.acl-long.1423.pdf)
- **Harmlessness** (construct): *causes*, 1 paper
  > Through human evaluation, we determine actionability and informativeness as key attributes in inducing harm when the jailbroken response is followed by individuals without specialized knowledge. (Section 1)
  - [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf)

### Associated with
- **Truthfulness** (construct), 2 papers
  > This finding highlights the critical importance of assessing informativeness metrics specifically for non-instruction-tuned models, as failing to do so may result in misleadingly high truthfulness scores. (Section 5)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
