# Confidence expression
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Expressing uncertainty, Confidence Expression, Confidence score generation, Verbalized confidence, Nuanced uncertainty expression, Linguistic uncertainty expression, Natural language uncertainty expression, Uncertainty expression  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is broad: models communicate certainty or uncertainty in an answer through explicit scores or probabilities, or through linguistic cues such as epistemic markers, hedging, tone, and elaboration. As LACIE: Listener-Aware Finetuning for Calibration in Large Language Models puts it, "LLMs can convey not only an answer to the question, but a level of confidence about the answer being correct." A smaller line of work narrows the behavior to explicit admissions of limited knowledge, for example "I am unsure" or "I don't know," and some papers additionally describe the target behavior as using uncertainty language that faithfully reflects intrinsic uncertainty, or as improving alignment between verbal and semantic uncertainties.

**Variants.** Papers study several variants, most commonly under labels like expressing uncertainty, verbalized confidence, confidence score generation, nuanced uncertainty expression, and linguistic uncertainty expression. The forms range from percentage or probability statements, to class-wise confidence values for each possible class, to hedged answers like "I am not sure but ..." or "maybe," and to direct uncertainty supplements added to answers such as "I am unsure." In one framework, expressing uncertainty is also discussed as a low-level cognitive cue alongside self-correction and adapting responses.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead describe direct elicitation and scoring procedures, including requesting confidence estimates as probability scores or percentages, asking for confidence for each class "between 0.00 and 100.00," and supplementing answers with phrases like "I am unsure" or labeling unfamiliar examples with "I don't know." One scoring approach incorporates model confidence into accuracy by prompting the model to verify its own predicted answer and extracting the probability of the "yes" token.

**What it is taken as evidence of.** Construct links are narrow. The only linked construct is honesty: Alignment for Honesty relates uncertainty expression to honesty and states that "the expression of uncertainty can serve as a valuable indicator of honesty." Papers do not report other construct links for this behavior.

## Sources

**Confidence expression** (1 paper: [LACIE: Listener-Aware Finetuning for Calibration in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8eaf3bcdc105423a972ed90eb07217-Paper-Conference.pdf))
> Communicating certainty or uncertainty in an answer using explicit scores, epistemic markers, tone, or elaboration.

**Expressing uncertainty** (2 papers: [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf), [Humanizing Machines: Rethinking LLM Anthropomorphism Through a Multi-Level Framework of Design](https://aclanthology.org/2025.emnlp-main.164.pdf))
> The observable behavior of a model explicitly stating its lack of confidence or knowledge in its response, such as by outputting phrases like 'I am unsure'.

**Confidence Expression** (1 paper: [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf))
> Providing probability estimates or confidence levels for predictions, often by verifying if a predicted answer is correct via token probability.

**Confidence score generation** (1 paper: [Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8b78c39a262ea563ee51d2f6dba3b04-Paper-Conference.pdf))
> The action of producing numerical confidence values for each potential class in a classification task, expressed within a natural language response.

**Verbalized confidence** (1 paper: [Thinking Out Loud: Do Reasoning Models Know When They're Right?](https://aclanthology.org/2025.emnlp-main.73.pdf))
> The observable expression of a model's certainty in its answer, typically in the form of a percentage or probability statement.

**Nuanced uncertainty expression** (1 paper: [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf))
> The generation of text that qualifies an answer with expressions of doubt or uncertainty, such as "I am not sure but..." or "maybe".

**Linguistic uncertainty expression** (1 paper: [MetaFaith: Faithful Natural Language Uncertainty Expression in LLMs](https://aclanthology.org/2025.emnlp-main.1505.pdf))
> The observable use of words, phrases, and hedging language to convey a degree of confidence or doubt in a generated response.

**Uncertainty expression** (1 paper: [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.183.pdf))
> The observable behavior of a model explicitly stating its lack of knowledge in a response, for example by saying "I don't know".

## Relationships

### Associated with
- **Honesty** (construct), 1 paper
  > the expression of uncertainty can serve as a valuable indicator of honesty, and we view calibration from the perspective of model knowledge as a finer-grained handling of knowns
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
