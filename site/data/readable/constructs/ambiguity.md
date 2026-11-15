# Ambiguity
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Task ambiguity  

## State of the Field

**Space of definitions.** Across the papers, the term is used in several distinct ways rather than one prevailing sense. One line treats ambiguity as multiplicity of possible interpretations or mappings: task ambiguity is the degree to which a user's intended task specification is underspecified or open to multiple interpretations, and tokenizer ambiguity is the case where more than one token sequence maps to the same text, creating uncertainty in decoding or in the induced language model. A separate, narrower usage describes whether the combination of lyrics and melody creates pronunciation or semantic confusion, so the main disagreement is over whether ambiguity resides in task specification, tokenization, or the lyrics and melody themselves.

**Space of facets.** Papers systematize ambiguity only locally. One paper splits it into pronunciation confusion versus semantic confusion, another treats ambiguity and inconsistency as separate concerns when implementing or using tokenizers, and another singles out task ambiguity as the result of insufficiently clear prompts or example sets. Taken together, the same label is applied to different levels of analysis, and the papers do not present a shared hierarchy or common set of subtypes.

**Space of measurement.** Operationalization is sparse. Papers link ambiguity to 1 measurement instrument, MeetingBank, and 1 behavioral indicator, Task completion. The only instrument named is MeetingBank, used through ambiguity human annotations added to it; no LLM-as-a-judge, probe, or analysis instrument is linked. The behavioral indicator appears in a causal claim rather than as a direct measurement procedure, so the recorded measurement is narrower than the definitions, which also cover tokenization, task specification, and lyrics plus melody.

**Links.** Papers link ambiguity to 1 construct and 1 behavioral indicator. One paper reports that ambiguity is related to Faithfulness, noting that an ambiguous summary can be correctly interpreted in multiple ways given the source document, which can lead to different faithfulness judgments depending on underlying assumptions. Another paper claims a causal relationship from ambiguity to Task completion, framed through the hypothesis that reducing ambiguity should lead to improved code accuracy; no correlational link is reported.

## Sources

**Ambiguity** (2 papers: [ToneCraft: Cantonese Lyrics Generation with Harmony of Tones and Pitches](https://aclanthology.org/2025.emnlp-main.18.pdf), [The Foundations of Tokenization: Statistical and Computational Concerns](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3748cdac932d91f0a51a37db90dec50-Paper-Conference.pdf))
> The tendency for the combination of lyrics and melody to create pronunciation or semantic confusion.

**Task ambiguity** (1 paper: [Eliciting Human Preferences with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9867d5a22653ce98b02595061e40f12-Paper-Conference.pdf))
> The degree to which a user's intended task specification is underspecified or open to multiple interpretations.

## Relationships

### Ambiguity →
- **MeetingBank** (measurement instrument): *measured_by*, 1 paper
  > we extend TofuEval MeetingBank (Tang et al., 2024b) with ambiguity human annotations and present the details in Section 4.2.
  - [Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation](https://aclanthology.org/2025.naacl-long.609.pdf)
- **Task completion** (behavioral indicator): *causes*, 1 paper
  > Based on our definition of ambiguity, we hypothesize that ambiguity reduction should lead to improved code accuracy. (Section 1)
  - [Identifying & Interactively Refining Ambiguous User Goals for Data Visualization Code Generation](https://aclanthology.org/2025.emnlp-main.1283.pdf)

### Associated with
- **Faithfulness** (construct), 1 paper
  > an ambiguous summary can be correctly interpreted in multiple ways given the source document, leading to different faithfulness judgments depending on the underlying assumptions.
  - [Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation](https://aclanthology.org/2025.naacl-long.609.pdf)
