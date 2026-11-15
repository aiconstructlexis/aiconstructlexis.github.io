# Recency bias
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Recency effect  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is a latent preference for recent tokens: attention or retrieval favors tokens closer to the current position over earlier ones, sometimes explicitly only when the compared tokens are otherwise similar. One paper states that "Recency implies that tokens that are more recent in the prompt ... are going to be more important in generating the subsequent token" (Emergence of Episodic Memory in Transformers: Characterizing Changes in Temporal Structure of Attention Scores During Training). Definitions differ mainly in scope: some describe a general weighting in attention, retrieval, or generation, while others narrow it to overemphasis on near, mid-range, or final tokens at the expense of earlier or historical context, and one definition analogizes it to human short-term memory recall patterns.

**Space of facets.** Papers use both "recency effect" and "recency bias" for closely similar phenomena. One paper places it within serial position effects, "specifically recency and primacy," while others describe more specific manifestations such as near-token focus, retrieval favoring recent tokens, or an end-of-input attention sink in which attention is "more strongly concentrated at the tail." One paper also relates it to positional bias by saying an approach can replace lost-in-the-middle with recency bias.

**Space of measurement.** Operationalization is sparse across the papers: no measurement instrument is linked to it, and one behavioral indicator, Synthetic recall, is linked only through a causal claim. Instead of a named benchmark, human evaluation, LLM-as-a-judge, probe, or analysis, papers describe the construct through attention patterns, for example greater weight on nearer positions when token comparisons are matched, heavy focus on near tokens, more balanced coverage of earlier positions in a Transformer, or attention concentrated at the tail. These text descriptions line up with the definitions, since both are framed as stronger weighting of recent positions over earlier ones.

**Links.** The linked claims are mostly causal. One paper claims a causal relationship from recency bias to Synthetic recall, stating that "this bias impairs the models' ability to recall distant information" (Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing), and another claims a causal relationship from recency bias to long-context understanding, arguing that focus on local tokens can be detrimental when information lies far back in the input. A further paper claims a causal relationship from recency bias to robustness, describing greater susceptibility to perturbations on local tokens and vulnerability to adversarial attack, and one paper reports that positional bias is related to recency bias by saying lost-in-the-middle can be replaced by recency bias.

## Sources

**Recency effect** (1 paper: [Emergence of Episodic Memory in Transformers: Characterizing Changes in Temporal Structure of Attention Scores During Training](https://aclanthology.org/2025.naacl-long.448.pdf))
> The latent tendency for a model to give greater weight to recently presented tokens when generating subsequent outputs, analogous to human short-term memory recall patterns.

**Recency bias** (2 papers: [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf), [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf))
> A tendency for attention or retrieval to favor more recent tokens over earlier ones when both are otherwise similar.

## Relationships

### Recency bias →
- **Robustness** (construct): *causes*, 1 paper
  > Furthermore, we raise a novel robustness concern regarding SSMs with recency bias: our empirical outcomes show that Mamba is more susceptible to perturbations on local tokens, making it vulnerable to adversarial attack, as these local tokens can be easily manipulated to serve as backdoors. (Section 1)
  - [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf)
- **Synthetic recall** (behavioral indicator): *causes*, 1 paper
  > “this bias impairs the models’ ability to recall distant information”
  - [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf)
- **Long-context understanding** (construct): *causes*, 1 paper
  > In next-token prediction settings, focusing on local tokens often suffices for short contexts, but can be detrimental when crucial information resides far back in the input.
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)

### Associated with
- **Positional bias** (construct), 1 paper
  > “This approach may appear to improve faithfulness, but it ultimately replaces one positional bias, i.e., lost-in-the-middle, with another, i.e., recency bias.”
  - [On Positional Bias of Faithfulness for Long-form Summarization](https://aclanthology.org/2025.naacl-long.442.pdf)
