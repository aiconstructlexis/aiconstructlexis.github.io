# Context sensitivity
**Type:** Construct  
**Supporting papers:** 9  
**Also known as:** Contextual sensitivity  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats context sensitivity as the extent to which outputs or judgments change with contextual information. Most definitions frame it as adaptation of goals, predictions, rationales, or token choices to the current environment, country, preceding context, or other situational cues, rather than to generic response priors or the current input alone. A smaller line of work casts it more normatively, as producing context-appropriate guidance or interpretation, for example when context helps distinguish sarcasm, critique, or non-toxic language from harmful content. Another recurring framing stresses dependence on situational framing itself, as when causal judgments vary across contexts.

**Space of facets.** The term is applied to several objects: generated goals, survey predictions, rationales, causal judgments, toxicity interpretations, and token-level predictions. The main axis of variation is what counts as context, ranging from agent state, inventory, and environment, to country labels, preceding context, and broader discursive setting. One paper uses the near-synonymous label contextual sensitivity for the same general phenomenon, while the toxicity paper applies the term to annotation or interpretation practice rather than only to model behavior.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to it. Instead, papers operationalize the construct through task-specific context manipulations and contrastive analyses: swapping country names to test whether predictions follow the stated country rather than response priors, removing or changing contextual cues to see whether rationales or causal judgments shift, checking whether generated goals adapt to an agent's state, inventory, and environment, and comparing predictions with and without preceding context to identify context-sensitive tokens. These operationalizations mostly line up with the dominant definition because they vary context and observe whether outputs respond.

## Sources

**Context sensitivity** (5 papers: [World Models with Hints of Large Language Models for Goal Achieving](https://aclanthology.org/2025.naacl-long.3.pdf), [Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations](https://aclanthology.org/2025.naacl-long.162.pdf), [On the Reliability of Large Language Models for Causal Discovery](https://aclanthology.org/2025.acl-long.471.pdf), [Mapping Toxic Comments Across Demographics: A Dataset from German Public Broadcasting](https://aclanthology.org/2025.emnlp-main.948.pdf), [Quantifying the Plausibility of Context Reliance in Neural Machine Translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d3040941a2d57ead4043556a70dd728-Paper-Conference.pdf))
> The degree to which the LLM's generated goals adapt to the agent's current state, inventory, and environment, ensuring relevance and usefulness of the guidance.

**Contextual sensitivity** (1 paper: [Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference](https://aclanthology.org/2025.acl-long.340.pdf))
> The ability of a model to adjust its outputs—especially rationales—in response to meaningful changes in the input context, indicating reliance on domain-specific and semantically important elements.
