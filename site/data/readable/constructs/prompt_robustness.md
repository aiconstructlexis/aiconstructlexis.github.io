# Prompt robustness
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Robustness to prompt templates, Robustness to prompt variations  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats prompt robustness as stability when prompts are varied, paraphrased, or reformulated in semantically similar ways. Most descriptions keep the focus on stable performance or consistent responses across prompt wording, including handling a wide range of prompt formulations and producing similar responses for similar inputs. A narrower framing limits the construct to semantically equivalent prompt templates and adds consistency of model rankings across templates, while another broadens it to performance on unseen prompt formulations and generalization beyond surface-level phrasing patterns.

**Space of facets.** Papers use several near-neighbor labels, including prompt robustness, robustness to prompt templates, and robustness to prompt variations, largely for the same family of uses. The main point of variation is scope: some authors center response consistency for the same question under rewording, while others frame it more broadly as stable task performance, ranking stability, or robustness to unseen prompts. Prompt sensitivity is treated as a comparison lens for this construct in one paper, which says sensitivity can be used to compare the robustness of LLMs to prompt variations.

**Space of measurement.** Operationally, papers link the construct to 2 measurement instruments and 1 behavioral indicator. The direct recorded measurement is a dataset-based evaluation with SST-2, selected in one study to focus on models' ability to adapt to manipulated prompts without label accuracy, while LLM-as-a-judge appears as a related evaluation setup because it is reported to lower performance variance and raise the correlation of model rankings across prompts. More broadly, papers operationalize prompt robustness through accuracy and variance on unseen prompts, consistency across paraphrased or semantically similar prompts, and ranking stability across prompt templates; the linked behavioral indicator, instruction following, appears in causal claims rather than as a direct measure.

**Links.** One paper claims a causal relationship from prompt robustness to instruction following, stating that prompt brittleness manifests as poor instruction following when commands deviate from those seen in training. Prompt robustness is also related to prompt sensitivity, which one paper proposes as a guide for comparing robustness to prompt variation, and to cross-domain generalization, where training prompts and novel test prompts are framed as source and target domains. A separate paper relates LLM-as-a-judge to prompt robustness, reporting lower performance variance and higher correlation in model rankings across prompts under that evaluation setup.

## Sources

**Prompt robustness** (3 papers: [Exploiting Edited Large Language Models as General Scientific Optimizers](https://aclanthology.org/2025.naacl-long.270.pdf), [Large Language Models Can Solve Real-World Planning Rigorously with Formal Verification Tools](https://aclanthology.org/2025.naacl-long.176.pdf), [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf))
> The degree to which a system's performance remains stable when faced with varied or paraphrased input prompts.

**Robustness to prompt templates** (1 paper: [Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs](https://aclanthology.org/2025.emnlp-main.1006.pdf))
> The property of an LLM to maintain stable performance and consistent rankings when evaluated across different but semantically equivalent prompt templates.

**Robustness to prompt variations** (1 paper: [Waste Not, Want Not; Recycled Gumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.292.pdf))
> The stability of model responses when the same question is reworded or paraphrased.

## Relationships

### Prompt robustness →
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > This brittleness manifests... as poor instruction following in chatbots and AI agents when commands deviate from those encountered during training (Hong et al., 2024; Sahoo et al., 2025) (Section 1).
  - [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf)
- **SST-2** (measurement instrument): *measured_by*, 1 paper
  > Since labels are not required for this task, we select the SST-2 dataset to focus solely on the models’ ability to adapt to manipulated prompts without being influenced by label accuracy. (Section 4.6)
  - [Direct Prompt Optimization with Continuous Representations](https://aclanthology.org/2025.acl-long.133.pdf)

### Associated with
- **LLM-as-a-judge** (measurement instrument), 1 paper
  > When we adopt LLM-as-a-Judge evaluations, we observe a substantial reduction in performance variance and a consistently higher correlation in model rankings across prompts. Our findings suggest that modern LLMs are more robust to prompt templates than previously believed...
  - [Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs](https://aclanthology.org/2025.emnlp-main.1006.pdf)
- **Prompt sensitivity** (construct), 1 paper
  > The sensitivity should be used, for instance, as a guide to compare the “robustness” of different LLMs to variations of the prompt. (Section 3)
  - [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Cross-domain generalization** (construct), 1 paper
  > The capability of PAFT to generalize effectively to unseen prompt formulations can be rigorously understood through the lens of domain adaptation theory... In this theoretical construct, the collection of training prompts Ptrain along with the task-specific training data Dtrain delineates the source domain. Besdies, the set of novel test prompts Ptest, paired with Dtest, represents the target domain (Section 6).
  - [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf)
