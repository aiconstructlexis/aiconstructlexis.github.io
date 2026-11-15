# Claim decomposition
**Type:** Behavioral indicator  
**Supporting papers:** 11  
**Also known as:** Claim extraction, Claim simplification, Viewpoint extraction, Statement decomposition, Atomic proposition decomposition  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing is the breakdown of a complex text, claim, statement, or summary into smaller units that can be checked separately, most often as discrete or atomic sub-claims. Most formulations stress verifiability, independent evaluation, or a single factual statement per unit, while smaller variants cast the outputs as sub-questions, decontextualised claim sentences, semantically independent viewpoints, or minimal true or false propositions about an image.

**Variants.** Papers use several near-synonymous names for the behavior, including claim extraction, claim simplification, statement decomposition, viewpoint extraction, and atomic proposition decomposition. The settings vary from multi-faceted claims, passages, and larger documents to reference summaries for content validity and coverage, complex research ideas decomposed into evaluable viewpoints, and detailed image captions broken into atomic units.

**Space of elicitation and scores.** Papers link claim decomposition to two measurement instruments, FActScore and WiCE, but they do so through related links rather than explicit measured_by claims. In those descriptions, FActScore is an LLM-based fact-checking pipeline that verifies claims decomposed from a passage against a trusted reference source, while WiCE appears through the use of its decomposition module in experiments.

**What it is taken as evidence of.** Papers connect the behavior to two constructs, and the link is not uniform. One paper reports it as related to calibration through claim-level extraction, confidence estimation, and calibration analysis, while another paper claims a causal relationship from claim decomposition to interpretability and explainability, saying claim-level decomposition enables finer-grained and more interpretable evaluation.

## Sources

**Claim decomposition** (3 papers: [IMRRF: Integrating Multi-Source Retrieval and Redundancy Filtering for LLM-based Fake News Detection](https://aclanthology.org/2025.naacl-long.461.pdf), [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.320.pdf), [TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain](https://aclanthology.org/2025.emnlp-main.43.pdf))
> Breaking down a complex input text into smaller, verifiable sub-claims, either emphasizing atomicity or verifiability.

**Claim extraction** (2 papers: [RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf), [Improving Zero-shot Sentence Decontextualisation with Content Selection and Planning](https://aclanthology.org/2025.emnlp-main.1258.pdf))
> Decomposing a text into a set of discrete claims for later verification.

**Claim simplification** (1 paper: [The Psychology of Falsehood: A Human-Centric Survey of Misinformation Detection](https://aclanthology.org/2025.emnlp-main.428.pdf))
> The task of breaking down complex assertions into simpler, more easily verifiable components.

**Viewpoint extraction** (1 paper: [GraphEval: A Lightweight Graph-Based LLM Framework for Idea Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5ce40ee957e4f76ef53c09d0bae20f4-Paper-Conference.pdf))
> The task of decomposing a complex research idea into a list of simpler, semantically independent, and evaluable units called viewpoints.

**Statement decomposition** (1 paper: [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf))
> Breaking down a complex statement containing multiple claims into simpler, constituent sub-statements for independent evaluation.

**Atomic proposition decomposition** (1 paper: [Toward Robust Hyper-Detailed Image Captioning: A Multiagent Approach and Dual Evaluation Metrics for Factuality and Coverage](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25aj/lee25aj.pdf))
> Breaking down a detailed caption into minimal true/false claims about the image for individual verification.

## Relationships

### Claim decomposition →
- **Interpretability and explainability** (construct): *causes*, 1 paper
  > Other approaches, including RAGAS (Shahul et al., 2023), RAG-Checker (Ru et al., 2024), and OpenEval (Ispas et al., 2025), introduce claim-level decomposition, enabling LLMs to assess the faithfulness and correctness of each factual statement for finer-grained and more interpretable evaluation.
  - [RAG-Zeval: Enhancing RAG Responses Evaluator through End-to-End Reasoning and Ranking-Based Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1267.pdf)

### Associated with
- **Calibration** (construct), 1 paper
  > This approach involves extracting distinct claims from the generated content, estimating the confidence associated with each claim, and then analyzing the calibration at the claim level. (Section 1)
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
- **WiCE** (measurement instrument), 1 paper
  > “we use the decomposition modules from VeriScore, FactScore, and Wice3 for our experiments”
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.320.pdf)
- **FActScore** (measurement instrument), 1 paper
  > “FACTSCORE is an LLM-based fact-checking pipeline that verifies claims decomposed from a passage against a trusted reference source”
  - [DnDScore: Decontextualization and Decomposition for Factuality Verification in Long-Form Text Generation](https://aclanthology.org/2025.emnlp-main.1205.pdf)
