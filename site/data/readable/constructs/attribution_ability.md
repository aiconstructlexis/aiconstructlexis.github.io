# Attribution ability
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Attribution, Evidence attribution  

## State of the Field

**Space of definitions.** Across the definitions, attribution ability is consistently framed as source-grounded support: models are expected to back claims with traceable, source-aligned evidence and to link statements to the evidence that supports them. One study notes that LLMs often have "limited ability to attribute their claims to source material," which matches this emphasis on grounding and traceability. A narrower formulation centers on generated explanations for fact checking, where citations should faithfully reflect the actual content and context of the provided passages, while the broader formulation speaks about model claims and the auditability and verification of reasoning steps.

**Space of facets.** No explicit facet structure or subtype taxonomy is laid out in the papers. The main naming variation is between "attribution" and "evidence attribution": the former is described broadly as supporting claims with traceable evidence, while the latter focuses more specifically on whether statements in explanations are correctly and faithfully linked to supporting source evidence. The clearest difference is scope, broad model claims versus explanation-level citation faithfulness.

**Space of measurement.** No measurement instrument is linked to this construct, and no behavioral indicator is linked to it. Instead, the papers describe operationalization in terms of what should be assessed: whether attribution is faithful to the source evidence, whether citations reflect the source content and context, and whether claims are supported by traceable, source-aligned evidence. In the usage in the papers, assessment is described at the level of these targets rather than through a named instrument.

**Links.** The linked constructs are Trustworthiness and Interpretability and explainability, both through causal claims. One paper claims a causal relationship from attribution ability to Trustworthiness, stating that improving accurate attributions has the potential to help improve trustworthiness, alongside usefulness and transparency. Another paper claims a causal relationship from attribution ability to Interpretability and explainability, describing indexed attribution triplets in generated text as enhancing interpretability; no correlational or generic related links are reported.

## Sources

**Attribution** (1 paper: [Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285.pdf))
> The ability of a model to support its claims with traceable, source-aligned evidence, enabling auditability and verification of reasoning steps.

**Evidence attribution** (1 paper: [Evaluating Evidence Attribution in Generated Fact Checking Explanations](https://aclanthology.org/2025.naacl-long.282.pdf))
> The latent ability of a model to correctly and faithfully link statements in its explanations to the supporting source evidence, ensuring that citations reflect actual content and context from the provided passages.

## Relationships

### Attribution ability →
- **Trustworthiness** (construct): *causes*, 1 paper
  > Improving the ability of LLMs to both generate relevant summaries and provide accurate attributions has the potential to help improve their usefulness, transparency, and trustworthiness. (Section 2.1)
  - [Unstructured Evidence Attribution for Long Context Query Focused Summarization](https://aclanthology.org/2025.emnlp-main.95.pdf)
- **Interpretability and explainability** (construct): *causes*, 1 paper
  > Attribution: attribute triplet indexes in the generated text using sequential numbers to enhance the interpretability of the generated text. (Section 1)
  - [Evaluating and Improving Graph to Text Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.513.pdf)
