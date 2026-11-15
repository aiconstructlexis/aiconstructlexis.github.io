# Actionability
**Type:** Construct  
**Supporting papers:** 8  
**Also known as:** Actionable insights  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats actionability as how clearly a response tells the recipient what to do next, with emphasis on concrete, practical, specific, and unambiguous guidance. One study asks, "Is it clear from the tutor’s feedback what the student should do next?" and adds that the response should not be "vague, unclear, or a conversation stopper" (Unifying AI Tutor Evaluation: An Evaluation Taxonomy for Pedagogical Ability Assessment of LLM-Powered AI Tutors). Similar wording is used for advice, medical suggestions, and peer review comments, where the response should be practical, contextually relevant, constructive, and easy to translate into specific actions; a smaller line of work uses the term more narrowly as a latent trait of harmful responses that contain clear steps, specific action verbs, and objects that help a user carry out harmful actions.

**Space of facets.** Papers unpack actionability into recurring facets: clear next steps, specificity, practicality, contextual relevance, constructive improvement suggestions, and freedom from vagueness. The label is reused across tutor feedback, advice seeking, medical-response assessment, peer review, and jailbreak outputs, so some papers apply it to practical guidance for the recipient, while others apply it specifically to harmful procedural detail. A nearby label, "actionable insights," is used for reviews that offer specific, constructive suggestions, and one advice framework treats actionability as one of seven values alongside empathy and creativity.

**Space of measurement.** Papers link actionability to one measurement instrument, Human evaluation, and no behavioral indicators. The recorded operationalization is a human rating, on a 5-point scale after each conversation, of whether the response "provides clear steps or instructions"; this uses the same language as the dominant definitions, which center on clear, concrete next actions. No other measurement instruments are linked.

**Links.** Among links to other constructs, one paper claims a causal relationship from actionability to harmlessness. Its evidence states that "actionability and informativeness" are attributes in inducing harm when a jailbroken response is followed by individuals without specialized knowledge (Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions). No correlational or other related links are reported.

## Sources

**Actionability** (5 papers: [Lived Experience Not Found: LLMs Struggle to Align with Experts on Addressing Adverse Drug Reactions from Psychiatric Medication Use](https://aclanthology.org/2025.naacl-long.553.pdf), [Unifying AI Tutor Evaluation: An Evaluation Taxonomy for Pedagogical Ability Assessment of LLM-Powered AI Tutors](https://aclanthology.org/2025.naacl-long.57.pdf), [AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.333.pdf), [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf), [The Good, the Bad and the Constructive: Automatically Measuring Peer Review's Utility for Authors](https://aclanthology.org/2025.emnlp-main.1476.pdf))
> The extent to which a tutor's feedback clearly indicates what the student should do next, avoiding vagueness or ambiguity that could halt progress.

**Actionable insights** (1 paper: [ReviewRL: Towards Automated Scientific Review with RL](https://aclanthology.org/2025.emnlp-main.857.pdf))
> The extent to which a review offers specific, constructive, and practical suggestions for improving the paper.

## Relationships

### Actionability →
- **Harmlessness** (construct): *causes*, 1 paper
  > Through human evaluation, we determine actionability and informativeness as key attributes in inducing harm when the jailbroken response is followed by individuals without specialized knowledge. (Section 1)
  - [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > After each conversation, participants rate the model’s responses on a 5-point scale ... across five criteria ...: (3) Actionability: Response provides clear steps or instructions. (Section 3.2.3)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
