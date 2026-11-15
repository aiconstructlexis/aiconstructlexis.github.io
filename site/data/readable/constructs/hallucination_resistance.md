# Hallucination resistance
**Type:** Construct  
**Supporting papers:** 32  
**Also known as:** Anti-hallucination, Knowledge hallucination, Factuality hallucination, Molecular hallucination, Hallucination tendency, Hallucination mitigation, Hallucination reduction  

## State of the Field

**Space of definitions.** Across the surveyed definitions, the prevailing usage treats this as a latent trait, tendency, ability, or degree by which a model avoids unsupported, false, or factually incorrect outputs. Most descriptions stay at that broad level, while some narrow the scope to specific output types: fabricated or ungrounded knowledge triples, multimodal answers, semantically plausible but factually ungrounded entity relations, citation predictions that do not correspond to real works, unsupported medical information, or molecules that follow structural rules but lack the expected activity or utility. A smaller line of work frames the same family of phenomena from the opposite side, as hallucination tendency, knowledge hallucination, factuality hallucination, or molecular hallucination, including cases where generated content is inconsistent with actual facts even when those facts are provided.

**Space of facets.** Papers organize the concept mainly through domain-specific variants rather than a shared abstract taxonomy. Recurring variants include knowledge hallucination in knowledge creation, factuality hallucination as entity-relation distortions, molecular hallucination as chemically valid yet practically unhelpful molecules, and application-specific forms in citation recommendation, retrieval-augmented generation, and medical consultation. Some descriptions explicitly contrast correctly created knowledge with knowledge hallucinations, and multimodal evaluation distinguishes visual illusion from knowledge hallucination, so the same label is used for both broad failures of factual support and narrower output-specific error types.

**Space of measurement.** Operationalization is benchmark-centered: papers link the construct to 5 measurement instruments and 1 behavioral indicator. The most common instruments are POPE, then AMBER, HallusionBench, Natural Questions, and TriviaQA. In use, papers assess anti-hallucination through POPE, use HallusionBench to diagnose knowledge hallucination alongside visual illusion, use AMBER to evaluate various types of hallucination, and treat degradation on Natural Questions and TriviaQA as evidence of increased hallucination on knowledge-based benchmarks. These measures line up with definitions in multimodal and knowledge-based settings, but the linked instruments do not cover several narrower definitions centered on molecular generation, citation generation, medical consultation, or knowledge-graph triples.

**Links.** Beyond measurement, papers claim a causal relationship from multimodal alignment, the only linked construct, to hallucination resistance, stating that better cross-modal alignment is accompanied by lower degrees of hallucination. Papers also claim a causal relationship from information extraction, the only linked behavioral indicator, to hallucination resistance, with the claim that focusing on relevant table cells provides the right context and reduces hallucinations in reasoning. No correlational or general related links are reported.

## Sources

**Hallucination resistance** (2 papers: [Can LLMs be Good Graph Judge for Knowledge Graph Construction?](https://aclanthology.org/2025.emnlp-main.554.pdf), [MKGL: Mastery of a Three-Word Language](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe03053bd2cf5b5c56de1e463bc53e1a-Paper-Conference.pdf))
> The latent trait of a model to avoid generating or endorsing factually unsupported or fabricated knowledge triples not grounded in the source text.

**Anti-hallucination** (1 paper: [Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cb66be286795d71f89367d596bf78ea7-Paper-Datasets_and_Benchmarks_Track.pdf))
> The latent tendency to avoid generating unsupported or false content in multimodal outputs.

**Knowledge hallucination** (1 paper: [KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf))
> The tendency of a model to generate content that is inconsistent with actual facts, even when those facts are provided, reflecting a failure in knowledge faithfulness.

**Factuality hallucination** (1 paper: [Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.186.pdf))
> The latent tendency of a language model to generate semantically plausible but factually ungrounded relationships between entities, reflecting a failure to align with real-world knowledge.

**Molecular hallucination** (1 paper: [Domain-Agnostic Molecular Generation with Chemical Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed7dd1e32cf9b0abf664bf0e891527e5-Paper-Conference.pdf))
> The model's latent tendency to generate molecules that are structurally and syntactically correct but fail to exhibit the expected chemical activity or practical utility in real-world applications.

**Hallucination tendency** (2 papers: [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf), [CiteBART: Learning to Generate Citations for Local Citation Recommendation](https://aclanthology.org/2025.emnlp-main.89.pdf))
> The latent propensity of the model to generate factually incorrect or unsupported content, potentially encouraged by finetuning data.

**Hallucination mitigation** (2 papers: [Knowledge Graph-Guided Retrieval Augmented Generation](https://aclanthology.org/2025.naacl-long.449.pdf), [From Introspection to Best Practices: Principled Analysis of Demonstrations in Multimodal In-Context Learning](https://aclanthology.org/2025.naacl-long.170.pdf))
> The latent ability of a model to refrain from generating false or unsupported content, particularly in response to ambiguous or unanswerable queries, when guided by appropriate demonstrations.

**Hallucination reduction** (1 paper: [Leveraging Knowledge Graph-Enhanced LLMs for Context-Aware Medical Consultation](https://aclanthology.org/2025.emnlp-main.1549.pdf))
> The degree to which a model avoids generating factually incorrect or unsupported medical information during consultation.

## Relationships

### Hallucination resistance →
- **POPE** (measurement instrument): *measured_by*, 2 papers
  > We assess our models’ ability toward anti-hallucination through POPE [29]. (Section 5)
  - [Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cb66be286795d71f89367d596bf78ea7-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **HallusionBench** (measurement instrument): *measured_by*, 1 paper
  > HallusionBench focuses on diagnosing both the visual illusion and knowledge hallucination of MLLMs.
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > Gekhman et al. (2024) shows that finetuning on factual information encourages hallucinations, something that we verify observing the significant degradation on TriviaQA and NQ-Open, which are knowledge-based benchmarks.
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 1 paper
  > Gekhman et al. (2024) shows that finetuning on factual information encourages hallucinations, something that we verify observing the significant degradation on TriviaQA and NQ-Open, which are knowledge-based benchmarks.
  - [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf)
- **AMBER** (measurement instrument): *measured_by*, 1 paper
  > Hallucination: AMBER (Wang et al., 2023) provides a discriminative way to evaluate various types of hallucination
  - [From Introspection to Best Practices: Principled Analysis of Demonstrations in Multimodal In-Context Learning](https://aclanthology.org/2025.naacl-long.170.pdf)

### → Hallucination resistance
- **Multimodal alignment** (construct): *causes*, 1 paper
  > Due to better cross-modal alignment, our model exhibits lower degrees of hallucination
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **Information extraction** (behavioral indicator): *causes*, 1 paper
  > Focusing on relevant table cells helps LLMs by providing the right context, thus reducing hallucinations in reasoning. (Section 2)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
