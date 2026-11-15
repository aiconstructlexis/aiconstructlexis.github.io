# Stereotype recognition
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Stereotype identification, Stereotype detection  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is a recognition or detection task for stereotypical content in text. Most commonly, papers describe success as correctly distinguishing stereotypical from anti-stereotypical statements, or as identifying whether a sentence or statement reflects a stereotype; one linked benchmark operationalizes this as three-way classification into "stereotype", "anti-stereotype", or "unrelated". A smaller line of work broadens the behavior to recognizing and critically explaining the presence of stereotypes in prompts.

**Variants.** Papers use nearby labels, including stereotype recognition, stereotype detection, and stereotype identification. The task appears in sentence-level classification, in setups where a model chooses which of multiple sentences expresses a stereotype given context, and in prompt-based probing that asks, "Does the following statement reflect a stereotype?" Some work also adapts existing resources into detection formats, including EspanStereo and multiple-choice StereoSet.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument, StereoSet. It is described as a benchmark or dataset for recognizing stereotypes in sentences, including classifying them as "stereotype", "anti-stereotype", or "unrelated", and one paper notes a multiple-choice adaptation of the dataset. No other measurement instrument is linked.

**What it is taken as evidence of.** The only linked construct is Fairness. One paper presents stereotype recognition as related to Fairness by using the task "to evaluate the alignment of fairness", rather than stating a measured_by, correlates, or causal link to a construct. No other construct link is stated.

## Sources

**Stereotype recognition** (2 papers: [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf), [SHADES: Towards a Multilingual Assessment of Stereotypes in Large Language Models](https://aclanthology.org/2025.naacl-long.600.pdf))
> A task designed to assess fairness by requiring the model to distinguish between stereotypical and anti-stereotypical statements.

**Stereotype identification** (1 paper: [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf))
> The observable ability to recognize and critically explain stereotypical content in input prompts.

**Stereotype detection** (2 papers: [Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLM Collaboration](https://aclanthology.org/2025.emnlp-main.1221.pdf), [Neuron Empirical Gradient: Discovering and Quantifying Neurons' Global Linear Controllability](https://aclanthology.org/2025.acl-long.1041.pdf))
> The task of classifying or identifying which of two or more sentences expresses a stereotype, given a context.

## Relationships

### Stereotype recognition →
- **StereoSet** (measurement instrument): *measured_by*, 1 paper
  > Stereotype Recognition: Utilizing StereoSet [35] to recognize stereotypes in sentences classifying them into one of three classes: “stereotype”, “anti-stereotype”, or “unrelated” categories. (Section 4)
  - [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf)

### Associated with
- **Fairness** (construct), 1 paper
  > To evaluate the alignment of fairness, we perform stereotype recognition task (Sun et al., 2024) (Section 4.1).
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)
