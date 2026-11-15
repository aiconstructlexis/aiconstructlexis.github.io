# Verbal uncertainty
**Type:** Construct  
**Supporting papers:** 7  
**Also known as:** Uncertainty expression, Output uncertainty, Uncertainty signaling  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats verbal uncertainty as a latent, output-side tendency or ability to communicate doubt through language. Most definitions agree on the core idea of expressing uncertainty in responses, through explicit phrases or implicit cues, but they differ on what that expression is tied to: some connect it to recognizing knowledge gaps or contradictory information and responding with doubt, refusal, or non-commitment, while another defines it as expressed doubt or confidence independent of the model's actual knowledge or internal certainty. A smaller broadening move extends the construct beyond short verbal markers to richer forms such as explanations, verbal qualifiers, and speech prosody.

**Space of facets.** Papers mostly differentiate the construct by the forms of expression they include. Some descriptions separate explicit and implicit cues, for example 'I doubt...' or 'Possibly...', while others widen the space to explanations, verbal qualifiers, prosody, refusals, and other non-committal responses. Papers also use overlapping labels, including uncertainty expression, output uncertainty, and uncertainty signaling, and some contrast the construct with semantic uncertainty or with scalar or numerical uncertainty.

**Space of measurement.** Operationalization centers on 2 measurement instruments and 1 behavioral indicator. The named instruments are LLM-as-a-judge, which one paper uses to measure verbal uncertainty in generated text, and UNCLE, a benchmark introduced to evaluate uncertainty expression in long- and short-form question answering. Both instruments target uncertainty as it is expressed in outputs; the only linked behavioral indicator is hallucination.

**Links.** Papers connect verbal uncertainty to 3 linked constructs and 1 behavioral indicator. One paper reports that semantic uncertainty correlates with verbal uncertainty, and says the correlation is only moderate; another claims a causal relationship from calibration to verbal uncertainty in the context of assigning numerical confidence scores during generation. Separate papers claim a causal relationship from verbal uncertainty to trustworthiness, describing explicit uncertainty or refusal as a way to enhance trustworthiness, and relate hallucination to verbal uncertainty by framing hallucinations as arising from miscalibration between verbal and semantic uncertainty.

## Sources

**Verbal uncertainty** (1 paper: [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf))
> The latent tendency of a model to express doubt or confidence in its outputs through linguistic cues, independent of its actual knowledge or internal certainty.

**Uncertainty expression** (1 paper: [UNCLE: Benchmarking Uncertainty Expressions in Long-Form Generation](https://aclanthology.org/2025.emnlp-main.1543.pdf))
> The latent ability of a model to recognize gaps in its knowledge and explicitly convey that uncertainty through natural language phrases (e.g., 'it is unclear' or 'I am not sure') rather than generating false or overconfident statements.

**Output uncertainty** (1 paper: [Position: Uncertainty Quantification Needs Reassessment for Large Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kirchhof25b/kirchhof25b.pdf))
> The latent capacity of an LLM agent to express uncertainty not as a scalar value but through rich linguistic means such as natural language explanations, verbal qualifiers, or speech prosody to convey ambiguity, competing possibilities, and reasoning.

**Uncertainty signaling** (1 paper: [Conflicting Needles in a Haystack: How LLMs behave when faced with contradictory information](https://aclanthology.org/2025.emnlp-main.1742.pdf))
> The latent ability of a model to recognize ambiguity or inconsistency in its input and express doubt, refusal, or non-commitment in its response.

## Relationships

### Verbal uncertainty →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > We follow recent work in expression decisiveness quantification and employ "LLM-as-a-Judge" to measure VU (Yona et al., 2024; Zheng et al., 2023). (Section 2.2)
  - [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf)
- **Trustworthiness** (construct): *causes*, 1 paper
  > Enabling models to either refuse to answer or explicitly express uncertainty has emerged as a promising direction to reduce hallucinations and enhance trustworthiness (Section 1).
  - [UNCLE: Benchmarking Uncertainty Expressions in Long-Form Generation](https://aclanthology.org/2025.emnlp-main.1543.pdf)
- **UNCLE** (measurement instrument): *measured_by*, 1 paper
  > we first introduce UNCLE, a benchmark designed to evaluate uncertainty expression in both long- and short-form question answering (QA). (Abstract)
  - [UNCLE: Benchmarking Uncertainty Expressions in Long-Form Generation](https://aclanthology.org/2025.emnlp-main.1543.pdf)

### → Verbal uncertainty
- **Semantic uncertainty** (construct): *correlates*, 1 paper
  > We find that “verbal1 uncertainty” is governed by a single linear feature in the representation space of LLMs, and show that this has only moderate correlation with the actual “semantic uncertainty” of the model. (Abstract)
  - [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf)
- **Calibration** (construct): *causes*, 1 paper
  > "Band et al. (2024) introduce linguistic calibration, enabling models to express uncertainty at different levels (e.g., I am 70% sure)."
  - [UNCLE: Benchmarking Uncertainty Expressions in Long-Form Generation](https://aclanthology.org/2025.emnlp-main.1543.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > Hallucinations arise from a miscalibration between VU and SU, where the model fails to express its high uncertainty in its generated output. (Section 4)
  - [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf)
