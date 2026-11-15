# Sequential recommendation
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Next-item prediction  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage is predicting the next item a user will interact with from a chronologically ordered or preceding history of interactions. Papers largely agree on this next-item forecasting framing, describing the objective as predicting users’ subsequent choices from historical records, and one formalization states it as selecting the item with the highest probability given the user sequence. As one paper puts it, sequential recommender systems “aim to predict users’ subsequent choices based on their historical interactions” (LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation).

**Variants.** Most papers use the name sequential recommendation, while some use next-item prediction for the same observable behavior. A smaller line of work presents it as a natural language generation task, with prompts such as recommending an item for a user based on purchased items and outputs in the form of an item identifier. Another variant reformulates the task as next-token prediction and then forecasts the next item from the predicted token sequence (RecGPT: A Foundation Model for Sequential Recommendation).

**Space of elicitation and scores.** No measurement instrument is linked to it, so papers do not connect this behavior to a named elicitation or scoring instrument.

**What it is taken as evidence of.** No construct is linked to it, so papers do not explicitly treat this behavior as evidence of a named construct.

## Sources

**Sequential recommendation** (2 papers: [LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f0728449cb3150189d765fc87afc913-Paper-Conference.pdf), [Improving LLMs for Recommendation with Out-Of-Vocabulary Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ar/huang25ar.pdf))
> The task of predicting the next item a user is likely to interact with based on their chronologically ordered history of previous interactions.

**Next-item prediction** (1 paper: [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.513.pdf))
> The observable behavior of forecasting the next item a user will interact with based on their preceding sequence of interactions.
