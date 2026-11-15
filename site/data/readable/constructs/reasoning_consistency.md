# Reasoning consistency
**Type:** Construct  
**Supporting papers:** 7  

## State of the Field

**Space of definitions.** Across the definitions, the shared framing is consistency as alignment or coherence in reasoning, but papers vary in what is being aligned. One recurring use describes coherent and uniform reasoning patterns across diverse problems, with harmonized demonstrations that create a "more coherent set of examples" and can "facilitate more effective reasoning patterns that can be easily followed" (Self-Harmonized Chain of Thought). Other papers define it as alignment between reasoning chains from different modalities or sources, correct and stable reasoning outcomes across languages, or agreement between an intermediate attempt and the model's eventual maximum-budget reasoning outcome. The clearest difference is the reference frame, process-level coherence versus outcome stability, across problems, modalities, languages, or reasoning-budget steps.

**Space of facets.** Rather than a single taxonomy, papers organize the construct by the setting in which reasoning is compared. The same name is used for harmonized Chain-of-Thought demonstrations, cross-modal fusion that aligns textual and visual reasoning processes into a coherent final answer, overlap in reasoning capabilities among languages, and alignment between intermediate reasoning and a final maximum-budget answer. In practice, this means the construct covers both properties of reasoning processes, such as chains or patterns, and properties of resulting answers, such as stable outcomes across languages or across reasoning budgets.

**Space of measurement.** No measurement instrument is linked to this construct, and no behavioral indicator is linked to it. Instead, papers operationalize it inside task-specific procedures: one prompts an LLM to evaluate the consistency between textual and visual reasoning chains during modality fusion, another compares an attempt z_t after t steps with the eventual attempt z_T at the maximum reasoning budget and uses probes to calibrate when generation should terminate, and others treat it through harmonized demonstrations or through reported "improved reasoning consistency across languages" and a "greater degree of overlap in reasoning capabilities among the languages."

## Sources

**Reasoning consistency** (4 papers: [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.577.pdf), [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf), [VisDoM: Multi-Document QA with Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.310.pdf), [Thought calibration: Efficient and confident test-time scaling](https://aclanthology.org/2025.emnlp-main.722.pdf))
> The degree to which a model produces coherent and uniform reasoning patterns across diverse problems, reducing cognitive load through structural harmony.
