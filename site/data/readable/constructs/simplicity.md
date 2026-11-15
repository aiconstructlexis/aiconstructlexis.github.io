# Simplicity
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Layness  

## State of the Field

**Space of definitions.** Most definitions treat simplicity as the ease or understandability of simplified text, sometimes explicitly for non-experts or general audiences. Another formulation casts it as a model ability to reduce linguistic and conceptual complexity, with one paper describing the goal as reducing the domain knowledge in generated text so general audiences can still understand the core idea. A related label, layness, focuses on whether generated text is suitable and understandable for a general, non-expert audience.

**Space of facets.** One recurring distinction is between raw simplicity of the rewritten text and relative simplicity gain when it is compared with the input complex text. Papers also separate simplicity from neighboring criteria by rating it alongside meaning preservation and fluency, and in one setup alongside comprehensiveness, conciseness, and layness. No construct-level equivalence or nesting is reported.

**Space of measurement.** Papers link simplicity to 3 measurement instruments and no behavioral indicators. Human evaluation operationalizes it with 1-5 Likert ratings of simplicity or layness, LLM-as-a-judge evaluates simplified text along meaning preservation, fluency, and simplicity, and PRMBench includes simplicity as one of several benchmark dimensions. These operationalizations make the construct explicit by scoring simplicity directly, though one paper also measures it comparatively as simplicity gain relative to the input.

**Links.** Beyond measurement, no causal, correlational, or other related links are reported for simplicity.

## Sources

**Simplicity** (3 papers: [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf), [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf), [JUDGEBERT: Assessing Legal Meaning Preservation Between Sentences](https://aclanthology.org/2025.emnlp-main.5.pdf))
> The latent trait reflecting a model's ability to reduce linguistic and conceptual complexity, making text accessible to non-experts without domain knowledge.

**Layness** (1 paper: [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf))
> The degree to which the generated text is suitable and understandable for a general, non-expert audience.

## Relationships

### Simplicity →
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > Using a 1-5 Likert scale, the judges are asked to rate the model output based on five criteria: comprehensiveness, layness, meaning preservation, conciseness, and fluency. (Section 5.3.3).
  - [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > “We use Llama3-8B-Instruct ... to evaluate the generated simplified text along three dimensions: meaning preservation, fluency, and simplicity.”
  - [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf)
- **PRMBench** (measurement instrument): *measured_by*, 1 paper
  > PRMBENCH comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.
  - [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://aclanthology.org/2025.acl-long.1230.pdf)
