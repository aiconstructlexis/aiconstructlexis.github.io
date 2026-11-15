# Semantic understanding
**Type:** Construct  
**Supporting papers:** 87  
**Also known as:** Semantic awareness, Semantic comprehension, Semantic capability, Semantic processing, Semantic relationship comprehension, Recommendation-specific semantics, Semantic competence, Semantic generalization, Semantic knowledge  

## State of the Field

**Space of definitions.** Across the surveyed definitions, the prevailing usage treats this construct as a model capability to comprehend meaning and semantic relationships in language or text, often explicitly beyond surface lexical, syntactic, acoustic, phonetic, or co-occurrence cues. Many papers frame it broadly, as understanding meaning in natural language, speech, structured data, or node text, while some definitions narrow it to particular settings such as tool selection, code representations, word sense distinctions, social bias, or user-item matching in recommendation. A smaller line of work shifts the locus from end-to-end ability to representational structure, defining semantic awareness or capability in terms of whether internal embeddings separate meanings, preserve medically meaningful structure, or encode meaning at the word, phrase, and sentence level. Papers also differ on scope, with some centering meaning alone and others explicitly including pragmatic implications, implicit relations, and contextual nuance.

**Space of facets.** Most papers use semantic understanding and semantic comprehension as overlapping labels, and one evaluation paper moves between semantic comprehension and semantic understanding when assessing generated text. Several narrower labels carve out subtypes: semantic relationship comprehension for explicit and implicit entity relations, semantic awareness for clustering representations by distinct meanings, semantic processing for integrating acoustic, syntactic, and semantic information in speech, recommendation-specific semantics for user-item matching, semantic competence for the meaning and pragmatic function of a construction, and semantic knowledge for internal meaning representations. The clearest contrast is with form or syntax: one line of work reports a form-meaning asymmetry, relating semantic understanding to syntactic competence by showing formal constraints can be learned while semantic constraints are not.

**Space of measurement.** Papers operationalize this construct with 5 linked measurement instruments and 8 linked behavioral indicators, mostly through benchmark-style task performance. The named instruments are Fann or Flop, HumanEval, Real-MM-RAG, XNLI, and sBLIMP: these are used to assess poetry understanding, function-specification interpretation through semantic relationship demands, robustness on a rephrased multimodal RAG benchmark, high-level semantics in a cross-lingual benchmark, and speech semantic understanding, respectively. Behaviorally, the construct is most often tied to code summarization, document-level relation extraction, entity matching, information retrieval, and medical diagnosis, alongside other linked indicators. These operationalizations usually line up with the dominant definitions by testing whether models capture meaning rather than surface form, though some target narrower variants such as function-level semantics or semantic relationships.

**Links.** Several papers claim a causal relationship from semantic understanding to schema matching, semantic diversity, information retrieval, document-level relation extraction, medical diagnosis, entity matching, and, in one account, brain alignment. In the opposite direction, papers claim causal relationships from compositionality, world knowledge, preference consistency, and brain alignment to semantic understanding. Other work describes it as related to semantic segmentation, table reasoning, text classification, code summarization, and syntactic competence, with the last relation framed through a form-meaning asymmetry.

## Sources

**Semantic understanding** (9 papers: [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf), [SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations](https://proceedings.neurips.cc/paper_files/paper/2024/file/200661bf8f4993b7828a45a2a90f2ecf-Paper-Datasets_and_Benchmarks_Track.pdf), [SyllableLM: Learning Coarse Semantic Units for Speech Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2844b1bec82dd4be201f68715c03ed1b-Paper-Conference.pdf), [Retrieval, Reasoning, Re-ranking: A Context-Enriched Framework for Knowledge Graph Completion](https://aclanthology.org/2025.naacl-long.221.pdf), [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.122.pdf), [Exploring the Potential of Large Language Models for Heterophilic Graphs](https://aclanthology.org/2025.naacl-long.269.pdf), [Token Prepending: A Training-Free Approach for Eliciting Better Sentence Embeddings from LLMs](https://aclanthology.org/2025.acl-long.159.pdf), [LLM Enhancers for GNNs: An Analysis from the Perspective of Causal Mechanism Identification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25o/gao25o.pdf), [Towards General-Domain Word Sense Disambiguation: Distilling Large Language Model into Compact Disambiguator](https://aclanthology.org/2025.emnlp-main.45.pdf))
> The model's capability to comprehend the meaning and semantic relationships within natural language.

**Semantic comprehension** (7 papers: [MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf), [SetCSE: Set Operations using Contrastive Learning of Sentence Embeddings](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed863220bf8b6ae698e26d66e86fb97d-Paper-Conference.pdf), [HAWK: Learning to Understand Open-World Video Anomalies](https://proceedings.neurips.cc/paper_files/paper/2024/file/fca83589e85cb061631b7ebc5db5d6bd-Paper-Conference.pdf), [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf), [Semantic-Eval : A Semantic Comprehension Evaluation Framework for Large Language Models Generation without Training](https://aclanthology.org/2025.acl-long.477.pdf), [Can Large Language Models Understand Intermediate Representations in Compilers?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25p/jiang25p.pdf), [Drivel-ology: Challenging LLMs with Interpreting Nonsense with Depth](https://aclanthology.org/2025.emnlp-main.1177.pdf))
> The ability to understand the nuanced meaning of tool descriptions and user queries, particularly when distinguishing between functionally similar options.

**Semantic awareness** (1 paper: [SetCSE: Set Operations using Contrastive Learning of Sentence Embeddings](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed863220bf8b6ae698e26d66e86fb97d-Paper-Conference.pdf))
> The degree to which a model's internal representations separate and cluster sentences according to their distinct meanings.

**Semantic capability** (1 paper: [Boltzmann Semantic Score: A Semantic Metric for Evaluating Large Vision Models Using Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc07feae9af49dd3f1a1e049b77f4e17-Paper-Conference.pdf))
> The extent to which a model's representations preserve medically meaningful structure and context rather than superficial cues.

**Semantic processing** (1 paper: [It's Not a Walk in the Park! Challenges of Idiom Translation in Speech-to-text Systems](https://aclanthology.org/2025.acl-long.1512.pdf))
> The model's capacity to process and represent the meaning of language by integrating acoustic, syntactic, and semantic information to form a coherent understanding.

**Semantic relationship comprehension** (1 paper: [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf))
> The latent ability to understand and infer explicit or implicit relationships between entities in a text, such as part-whole or hierarchical roles, beyond mere co-occurrence.

**Recommendation-specific semantics** (1 paper: [EasyRec: Simple yet Effective Language Models for Recommendation](https://aclanthology.org/2025.emnlp-main.894.pdf))
> The latent ability of a language model to encode text in a way that captures nuances relevant specifically to user-item matching and recommendation, beyond general semantic similarity.

**Semantic competence** (1 paper: [Unpacking Let Alone: Human-Scale Models Generalize to a Rare Construction in Form but not Meaning](https://aclanthology.org/2025.emnlp-main.1399.pdf))
> A model's ability to understand and correctly use the meaning, function, and pragmatic implications of a linguistic construction.

**Semantic knowledge** (1 paper: [LinguaLens: Towards Interpreting Linguistic Mechanisms of Large Language Models via Sparse Auto-Encoder](https://aclanthology.org/2025.emnlp-main.1433.pdf))
> The model's internal representation of meaning at the word, phrase, and sentence level.

## Relationships

### Semantic understanding →
- **Schema matching** (behavioral indicator): *causes*, 1 paper
  > Aligning attributes across different MMKGs is challenging due to the variations in the expression of identical attributes. It necessitates more than a basic lexical comparison and requires a profound semantic understanding to ascertain whether attributes with different labels indeed represent the same concept. (Section 4.1)
  - [Tackling Uncertain Correspondences for Multi-Modal Entity Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf)
- **sBLIMP** (measurement instrument): *measured_by*, 1 paper
  > SyllableLM outperforms the 13B parameter TWIST and 7B Moshi on sBLIMP, which best evaluates semantic understanding (Lakhotia et al., 2021).
  - [SyllableLM: Learning Coarse Semantic Units for Speech Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2844b1bec82dd4be201f68715c03ed1b-Paper-Conference.pdf)
- **Semantic diversity** (construct): *causes*, 1 paper
  > We hypothesize that leveraging the semantic knowledge of large language models (LLM) can lead us to improve semantic diversity of resulting behaviors. (Abstract)
  - [Language Guided Skill Discovery](https://proceedings.iclr.cc/paper_files/paper/2025/file/dae30ba63ca043588cdf804bbba295ed-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator): *causes*, 1 paper
  > To build semantic index for files in the LSFS, we leverage an a lightweight embedding model, i.e., all-MiniLM-L6-v2 (Reimers & Gurevych, 2019), commonly used in vector databases, thereby supporting more advanced file operations which requires semantic understanding of file content. (Section 3)
  - [From Commands to Prompts: LLM-based Semantic File System for AIOS](https://proceedings.iclr.cc/paper_files/paper/2025/file/517eb19e99947f60afff0cf93e451825-Paper-Conference.pdf)
- **XNLI** (measurement instrument): *measured_by*, 1 paper
  > The two multilingual tasks evaluate MrT5's ability to understand high-level semantics... specifically, two cross-lingual benchmarks (XNLI and TyDi QA)
  - [MrT5: Dynamic Token Merging for Efficient Byte-level Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e9dd32cb9f9bff397f1a7ebd07010f2-Paper-Conference.pdf)
- **Brain alignment** (construct): *causes*, 1 paper
  > If brain-tuning successfully improves semantic understanding in speech models, we expect that brain-tuned models will align better with semantic language regions in new brain recordings (Section 3.4)
  - [Improving Semantic Understanding in Speech Language Models via Brain-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/95b7a93e60fdfd10cc202f44fd6adf5f-Paper-Conference.pdf)
- **Document-level relation extraction** (behavioral indicator): *causes*, 1 paper
  > The integration of sentence-level semantic RAG enhances the LLM’s ability to accurately extract relations by providing rich and relevant semantic information, which empowers the semantic understanding of LLMs and ultimately improves the performance of document-level RE. (Section 4.3. Sentence-Level Semantic RAG Enhancement)
  - [DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25am/xu25am.pdf)
- **Medical diagnosis** (behavioral indicator): *causes*, 1 paper
  > Language Models (LMs) have advanced diagnosis prediction by leveraging the semantic understanding of medical concepts in Electronic Health Records (EHRs). (Abstract)
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)
- **Real-MM-RAG** (measurement instrument): *measured_by*, 1 paper
  > We also evaluate on the rephrased version of this benchmark, provided by the authors, to assess model robustness and true semantic understanding. (Section 5.1)
  - [DocReRank: Single-Page Hard Negative Query Generation for Training Multi-Modal RAG Rerankers](https://aclanthology.org/2025.emnlp-main.436.pdf)
- **Fann or Flop** (measurement instrument): *measured_by*, 1 paper
  > The benchmark comprises a curated corpus of poems with explanations that assess semantic understanding, metaphor interpretation, prosodic awareness, and cultural context (Abstract).
  - [Fann or Flop: A Multigenre, Multiera Benchmark for Arabic Poetry Understanding in LLMs](https://aclanthology.org/2025.emnlp-main.1023.pdf)
- **HumanEval** (measurement instrument): *measured_by*, 1 paper
  > “HumanEval is driven most by Semantic Relationship, aligning with the need to interpret function specifications precisely”
  - [Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://aclanthology.org/2025.emnlp-main.789.pdf)
- **Entity matching** (behavioral indicator): *causes*, 1 paper
  > “LMs provide advanced semantic understanding to build and refine KGs through tasks like EA.”
  - [How do Language Models Reshape Entity Alignment? A Survey of LM-Driven EA Methods: Advances, Benchmarks, and Future](https://aclanthology.org/2025.emnlp-main.1184.pdf)

### → Semantic understanding
- **Compositionality** (construct): *causes*, 1 paper
  > methods that improve compositionality of CLIP such as NegCLIP and CLIP-SVLC also achieve better performance on SUGARCREPE++ compared to CLIP, underscoring the importance of compositionality as a critical component for understanding semantic and lexical differences. (Section 3.1)
  - [SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations](https://proceedings.neurips.cc/paper_files/paper/2024/file/200661bf8f4993b7828a45a2a90f2ecf-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Brain alignment** (construct): *causes*, 1 paper
  > “incorporating brain signals into the training of language models improves the models’ semantic understanding”
  - [Improving Semantic Understanding in Speech Language Models via Brain-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/95b7a93e60fdfd10cc202f44fd6adf5f-Paper-Conference.pdf)
- **World knowledge** (construct): *causes*, 1 paper
  > As LLMs encompass general open-world knowledge, they can be utilized for the semantic understanding of nodes’ textual content. (Section 1)
  - [Exploring the Potential of Large Language Models for Heterophilic Graphs](https://aclanthology.org/2025.naacl-long.269.pdf)
- **Preference consistency** (construct): *causes*, 1 paper
  > While score consistency drives the PRM to optimize for better complete responses, preference consistency preserves semantic understanding capability, thereby yielding high-quality outputs. (Introduction)
  - [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf)

### Associated with
- **Semantic segmentation** (behavioral indicator), 1 paper
  > Segmentation evaluates the model’s ability to assign semantic labels to each pixel, assessing semantic understanding
  - [Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8c67fc501a50977947c5bebbc39ca8f6-Paper-Conference.pdf)
- **Table reasoning** (construct), 1 paper
  > Our qualitative analysis of model responses reveals that Table-R1-Zero not only acquires multi-step reasoning and reflection abilities like other reasoning models, but also develops essential table-specific reasoning skills such as semantic understanding, information extraction, and arithmetic computation. (Section 1)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Text classification** (behavioral indicator), 1 paper
  > Topic Classification (TC) as a primarily semantic task (Section 1)
  - [Tokenization and Representation Biases in Multilingual Models on Dialectal NLP Tasks](https://aclanthology.org/2025.emnlp-main.1224.pdf)
- **Syntactic competence** (construct), 1 paper
  > Our experiments show strong evidence for a form–meaning asymmetry: Human-scale models learn LET-ALONE’s formal constraints almost perfectly (§4), but fail to learn any semantic constraints (§5).
  - [Unpacking Let Alone: Human-Scale Models Generalize to a Rare Construction in Form but not Meaning](https://aclanthology.org/2025.emnlp-main.1399.pdf)
- **Code summarization** (behavioral indicator), 1 paper
  > This task complements Task 2 by shifting the focus toward semantic understanding. In this setting, LLMs are required to generate concise natural language summaries of IR functions. ... Summarization serves as a proxy to evaluate whether the model can accurately capture functional intent, behavior, and output—ultimately revealing its capacity to reason about function-level semantics. (Section 3.1)
  - [Can Large Language Models Understand Intermediate Representations in Compilers?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25p/jiang25p.pdf)
