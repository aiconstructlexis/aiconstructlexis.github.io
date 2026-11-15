# Primacy bias
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Primacy effect  

## State of the Field

**Space of definitions.** Across the surveyed definitions, the prevailing usage treats primacy bias as a positional bias favoring the beginning of the input sequence. Most commonly, papers describe it as either greater accuracy when retrieving information from the start of the context, for example a model that "can more accurately retrieve information that is at the beginning of the input context," or as disproportionate emphasis on early tokens. A smaller line of work uses the near-synonymous label "primacy effect" and frames it as a latent tendency for early positional salience to influence later outputs, so the main difference is whether the construct is stated as an observable performance pattern or an underlying weighting tendency.

**Space of facets.** Papers usually situate the construct inside broader positional phenomena. Some explicitly call it a form of positional bias, while another places it among serial position effects, "specifically recency and primacy"; in that usage, "primacy effect" and "primacy bias" refer to the same beginning-of-sequence tendency. Another paper describes it as an intrinsic architectural tendency and mentions it alongside induction heads in accounts of positional bias.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to it. In the descriptions, papers operationalize it directly through position-sensitive behavior, such as testing whether retrieval is more accurate when the relevant information appears early in the context, or through empirical studies of positional effects across tasks and models. These operationalizations track the dominant definitions by testing beginning-position advantage or early-token emphasis directly.

**Links.** No papers claim that primacy bias is measured by, causes, correlates with, or is related to another entity.

## Sources

**Primacy bias** (2 papers: [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf), [Where to show Demos in Your Prompt: A Positional Bias of In-Context Learning](https://aclanthology.org/2025.emnlp-main.1503.pdf))
> A form of positional bias where a model is more accurate at retrieving information located at the beginning of the input context.

**Primacy effect** (1 paper: [Emergence of Episodic Memory in Transformers: Characterizing Changes in Temporal Structure of Attention Scores During Training](https://aclanthology.org/2025.naacl-long.448.pdf))
> The latent tendency for a model to give greater weight to tokens presented at the beginning of a sequence, influencing later outputs due to early positional salience.
