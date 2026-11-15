# Ambiguity detection ability
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Ambiguity detection, Ambiguity identification, Ambiguity recognition, Ambiguity awareness  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a latent recognition ability: noticing that a question, claim, statement, instruction, object, or situation admits multiple plausible interpretations. Most definitions stay close to this recognition framing, while some narrow it to visual questions, especially referential ambiguity in images, and others apply it to narrative claims or instructions. A recurring difference is in the response criterion: some papers stop at detecting ambiguity, whereas others require the model to ask for clarification or acknowledge uncertainty before answering.

**Space of facets.** Papers use several near-synonymous labels, ambiguity detection, ambiguity recognition, ambiguity identification, and ambiguity awareness, for closely aligned constructs centered on multiple valid interpretations. The only explicit higher-level placement puts ambiguity awareness under aleatoric uncertainty awareness. Beyond that, the construct is specialized mainly by domain rather than by a shared taxonomy, including visual-question ambiguity, referential ambiguity in images, ambiguity in instructions or statements, and ambiguous wording in summary claims.

**Space of measurement.** Papers link this construct to 1 measurement instrument and 1 behavioral indicator overall. The only named instrument is Ambrosia, presented as a benchmark for systems capable of recognizing and interpreting ambiguous requests. In source descriptions, authors also operationalize the ability by mixing ambiguous with non-ambiguous visual questions, using a binary label for whether a claim contains ambiguity, and tracking whether models ask for clarification, acknowledge ambiguity or uncertainty, or give Explicit responses. These operationalizations mostly match the definitions' focus on recognition, though some extend it to appropriate response behavior.

**Links.** One paper reports that aleatoric uncertainty awareness is related to this construct, specifically by treating ambiguity awareness as a sub-category under aleatoric uncertainty. One paper also reports that ambiguity detection ability correlates with Coreference resolution, describing a persistent tension in which higher Correct-Unamb performance tends to accompany lower Detect-Ambig performance, and vice versa. No causal relationship is recorded.

## Sources

**Ambiguity detection** (2 papers: [Teaching Vision-Language Models to Ask: Resolving Ambiguity in Visual Questions](https://aclanthology.org/2025.acl-long.182.pdf), [Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding](https://aclanthology.org/2025.emnlp-main.10.pdf))
> The latent ability of a model to recognize when a visual question is ambiguous and requires clarification before answering.

**Ambiguity recognition** (1 paper: [RAcQUEt: Unveiling the Dangers of Overlooked Referential Ambiguity in Visual LLMs](https://aclanthology.org/2025.emnlp-main.1206.pdf))
> The latent ability of a model to detect when a question is referentially ambiguous due to multiple possible referents in an image and to respond appropriately by acknowledging uncertainty.

**Ambiguity identification** (1 paper: [Language Models Identify Ambiguities and Exploit Loopholes](https://aclanthology.org/2025.emnlp-main.1677.pdf))
> The latent ability to recognize when a statement or instruction has multiple possible, valid interpretations.

**Ambiguity awareness** (1 paper: [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf))
> The ability to recognize when a question, object, or situation admits multiple plausible interpretations and therefore cannot be answered with certainty.

## Relationships

### Ambiguity detection ability →
- **Ambrosia** (measurement instrument): *measured_by*, 1 paper
  > We introduce a new benchmark, (cid:129)(cid:141)(cid:130)(cid:146)(cid:143)(cid:147)(cid:137)(cid:129), which we hope will inform and inspire the development of text-to-SQL parsers capable of recognizing and interpreting ambiguous requests. (Abstract)
  - [AMBROSIA: A Benchmark for Parsing Ambiguous Questions into Database Queries](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4c942a8405cc910f0a833d28d2573cc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Coreference resolution** (behavioral indicator): *correlates*, 1 paper
  > Across all prompts we observe a persistent tension: high performance in Correct-Unamb tends to be accompanied by lower performance in Detect-Ambig, and vice versa. (Section 6)
  - [Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs](https://aclanthology.org/2025.emnlp-main.1527.pdf)

### Associated with
- **Aleatoric uncertainty awareness** (construct), 1 paper
  > “Similarly, we define 2 sub-categories under aleatoric uncertainty: • Ambiguity awareness involves recognizing situations, objects, or individuals that can be understood, interpreted, or perceived in more than one way.”
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
