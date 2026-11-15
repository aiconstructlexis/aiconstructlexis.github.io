# Uncertainty awareness
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Self-aware uncertainty, Multimodal Uncertainty Awareness  

## State of the Field

**Space of definitions.** Across the surveyed definitions, the prevailing usage treats uncertainty awareness as a latent degree or ability by which a model recognizes its own lack of knowledge, confidence, or inability to provide a definitive answer. Most formulations keep this self-recognition close to internal confidence signals, either by inferring it from inconsistencies in internal states across multiple generations or by defining it as sensitivity to confidence in generated answers and document relevance for self-calibration. A smaller line of work extends the construct to multimodal settings, where the model recognizes cases that cannot be answered definitively because of information limitations or inherent unpredictability.

**Space of facets.** Only one paper explicitly breaks the construct into subtypes, presenting a vision-language taxonomy that distinguishes epistemic uncertainty awareness from aleatoric uncertainty awareness. Across papers, related labels such as self-aware uncertainty, uncertainty awareness, and multimodal uncertainty awareness are used for closely aligned versions of the construct, with the definitions differing mainly by modality and by whether they point to internal states or to self-calibration signals. No other subtype breakdown appears in the definitions.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to this construct. When papers make it concrete, one extracts self-aware uncertainty from feed-forward network states at the last generated token, and another uses uncertainty scores for generated answers and document relevance during inference, iterative prompt rephrasing, and self-calibration training. These operationalizations follow the definitions' focus on internal confidence and knowledge limitations.

**Links.** Links are sparse. One paper reports that epistemic uncertainty awareness is related to uncertainty awareness, and that aleatoric uncertainty awareness is related to uncertainty awareness, as part of a taxonomy that distinguishes the two. No causal relationship or correlation is recorded for this construct.

## Sources

**Self-aware uncertainty** (1 paper: [SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1312.pdf))
> The latent degree to which an LLM recognizes its own lack of knowledge or confidence in generating correct content, inferred from inconsistencies in its internal states across multiple generations.

**Uncertainty awareness** (1 paper: [SGIC: A Self-Guided Iterative Calibration Framework for RAG](https://aclanthology.org/2025.acl-long.1376.pdf))
> The model's sensitivity to its own confidence levels in generated answers and document relevance, allowing it to guide self-calibration processes.

**Multimodal Uncertainty Awareness** (1 paper: [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf))
> The latent ability of a model to recognize situations where a definitive answer cannot be provided due to information limitations or inherent unpredictability in vision-language tasks.

## Relationships

### Associated with
- **Epistemic uncertainty awareness** (construct), 1 paper
  > “we present a taxonomy of uncertainty specific to vision-language AI systems, distinguishing between epistemic uncertainty ... and aleatoric uncertainty ...”
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
- **Aleatoric uncertainty awareness** (construct), 1 paper
  > “we present a taxonomy of uncertainty specific to vision-language AI systems, distinguishing between epistemic uncertainty ... and aleatoric uncertainty ...”
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
