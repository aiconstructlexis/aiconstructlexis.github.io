# Generality
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Paraphrase execution, Cross-lingual propagation  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage treats generality as post-edit transfer beyond the exact edit prompt: applying newly edited knowledge to rephrased, paraphrased, or semantically equivalent queries. One paper makes this especially concrete as updating "rephrased in-scope examples," and another defines "paraphrase execution" as producing the correct edited output for a paraphrased version of the original prompt. A smaller line of work extends the same idea across languages, defining cross-lingual propagation as whether an edit made in one source language transfers to semantically equivalent queries in other target languages. The main difference across definitions is therefore the scope of transfer, within-language rephrasing versus multilingual propagation.

**Space of facets.** Papers organize the concept around variations of the edited query. The most common distinction is between the original prompt and rephrased or paraphrased in-scope examples, while one survey presents cross-lingual propagation as a multilingual extension of the same concern. The naming is not fully uniform: authors use "generality," "generalization," and "paraphrase execution" for closely related behavior. Generality is also regularly grouped with reliability and locality as a co-target property in editing, and one paper describes reliability, generalization, and locality as an "impossible triangle" in continual editing settings.

**Space of measurement.** Operationalization is tied to editing evaluations. Papers link generality to 2 measurement instruments and 1 behavioral indicator: the named instruments are CounterFact and ZsRE, where one paper evaluates efficacy, generality, and locality with success rates on CounterFact and with accuracy on ZsRE. These operationalizations match the dominant definitions in treating generality as performance beyond the exact edited prompt, while the multilingual definition adds cross-language transfer as another form of the same target behavior.

**Links.** Multiple papers relate generality to knowledge editing, describing it as one of the criteria knowledge editing seeks to satisfy and noting that poor generalization appears when a method can hardly make the model understand edits and generalize to different queries. Another paper relates editing locality to generality, stating that reliability, generalization, and locality cannot all be realized at the same time in continual editing settings. One paper also claims a causal relationship from instruction following ability to generality, attributing stronger generalization performance partly to better instruction-following capability.

## Sources

**Generality** (1 paper: [GeoEdit: Geometric Knowledge Editing for Large Language Models](https://aclanthology.org/2025.emnlp-main.676.pdf))
> The ability of a model to apply newly edited knowledge to rephrased or semantically equivalent prompts, not just the exact one used for editing.

**Paraphrase execution** (1 paper: [Resolving Lexical Bias in Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rizwan25a/rizwan25a.pdf))
> Generating the correct edited output when presented with a paraphrased version of the original edit prompt.

**Cross-lingual propagation** (1 paper: [Editing Across Languages: A Survey of Multilingual Knowledge Editing](https://aclanthology.org/2025.emnlp-main.803.pdf))
> The extent to which a factual edit made in one source language successfully transfers to semantically equivalent queries in other target languages.

## Relationships

### Generality →
- **CounterFact** (measurement instrument): *measured_by*, 1 paper
  > In the Counterfact dataset, we evaluate the models on Efficacy, Generality, and Locality, using success rates as metrics. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)
- **ZsRE** (measurement instrument): *measured_by*, 1 paper
  > Since ZsRE does not measure generative capabilities, we evaluate the models based only on accuracy in terms of Efficacy, Generality, and Locality. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)

### → Generality
- **Instruction following ability** (construct): *causes*, 1 paper
  > For reliability, generalization, and portability evaluations, LLaVA-1.5 outperforms BLIP-2 and MiniGPT-4. This improved performance can be attributed to its larger model size and better instruction-following capability... (Section 5.2.1)
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)

### Associated with
- **Knowledge editing** (behavioral indicator), 2 papers
  > Knowledge editing seeks to maximize the chance of an LLM responding with y given x, while satisfying the following additional criteria at the same time...: (1) Generality: there are different ways to express US president, wherefore the edited model should generalize. (Section 2.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Editing locality** (construct), 1 paper
  > we find that it seems to be an impossible triangle—reliability, generalization, and locality can not be realized at the same time in the continual editing settings. (Section 1)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
