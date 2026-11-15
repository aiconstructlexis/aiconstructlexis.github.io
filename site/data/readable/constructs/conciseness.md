# Conciseness
**Type:** Construct  
**Supporting papers:** 21  
**Also known as:** Brevity, Succinctness  

## State of the Field

**Space of definitions.** Most commonly, papers treat conciseness, and nearby labels such as brevity and succinctness, as a quality of outputs being brief, to the point, and free of unnecessary repetition, verbosity, or extraneous content. This framing is reused across responses, summaries, code reviews, conversations, explanations, and descriptions, sometimes with the added requirement that the output communicate only the necessary information or fit the reader's needs. A smaller line of work, especially in summarization-oriented formulations, casts conciseness less as shortness alone and more as how much of the generated content aligns with salient, accurate content, while some authors explicitly describe verbosity as its low end.

**Space of facets.** One organizational move places conciseness under User Alignment, alongside Readability and Harmlessness. Across papers, it is also contrasted with verbosity, described as low conciseness or as being too verbose, and nearby labels such as brevity and succinctness are used for much the same idea in explanations and descriptions. Some summarization papers also use the same term for a content-selection notion, describing conciseness as the share of generated material that aligns with salient facts or is both accurate and salient.

**Space of measurement.** In the linked measurement literature, conciseness is measured by 1 instrument, Human evaluation, and no behavioral indicators are linked to it. The prevailing operationalization asks annotators to rate outputs on Likert-style scales for whether they are too verbose, or whether they are clear, complete, and show minimal redundancy, sometimes alongside criteria such as fluency, naturalness, understandability, comprehensiveness, or meaning preservation. These judgments line up closely with the dominant definition of brevity and low redundancy, though some papers elsewhere describe conciseness with ratio-like formulations about on-topic, accurate, or salient content rather than length alone.

**Links.** Beyond measurement, one paper relates conciseness to Human preference alignment by placing it within User Alignment. No causal or correlational claim is recorded.

## Sources

**Conciseness** (9 papers: [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf), [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/be3b0d51a2b86cb4ffe50f13480217e0-Paper-Conference.pdf), [Learning to Summarize from LLM-generated Feedback](https://aclanthology.org/2025.naacl-long.38.pdf), [CRScore: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells](https://aclanthology.org/2025.naacl-long.457.pdf), [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf), [Wizard of Shopping: Target-Oriented E-commerce Dialogue Generation with Decision Tree Branching](https://aclanthology.org/2025.acl-long.641.pdf), [TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain](https://aclanthology.org/2025.emnlp-main.43.pdf), [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf), [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf))
> The ability of a model to produce responses that are brief and to the point, avoiding unnecessary repetition or verbosity.

**Brevity** (1 paper: [GraphNarrator: Generating Textual Explanations for Graph Neural Networks](https://aclanthology.org/2025.acl-long.2.pdf))
> The degree to which the explanation is concise and avoids redundancy, improving human interpretability by minimizing unnecessary content.

**Succinctness** (1 paper: [Sightation Counts: Leveraging Sighted User Feedback in Building a BLV-aligned Dataset of Diagram Descriptions](https://aclanthology.org/2025.acl-long.1338.pdf))
> The quality of a description being brief and to the point without including extraneous or overly long text.

## Relationships

### Conciseness →
- **Human evaluation** (measurement instrument): *measured_by*, 4 papers
  > Using a 1-5 Likert scale, the judges are asked to rate the model output based on five criteria: comprehensiveness, layness, meaning preservation, conciseness, and fluency. (Section 5.3.3).
  - [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf)
  - [Wizard of Shopping: Target-Oriented E-commerce Dialogue Generation with Decision Tree Branching](https://aclanthology.org/2025.acl-long.641.pdf)
  - [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.726.pdf)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)

### Associated with
- **Human preference alignment** (construct), 1 paper
  > We define 4 primary abilities which are divided into 12 fine-grained skills for comprehensive language model evaluation: ... and User Alignment (Conciseness, Readability, Harmlessness). (Section 1)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
