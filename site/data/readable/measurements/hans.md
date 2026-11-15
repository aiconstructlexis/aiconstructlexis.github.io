# HANS
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across the surveyed work, HANS is most commonly described as a natural language inference dataset aimed at model sensitivity to lexical overlap and related artifacts. Some descriptions sharpen this by calling it the adversarial dataset Heuristic Analysis for NLI Systems, "generated to contain examples that cannot be solved through heuristics like lexical overlap," and note that it contains 30K examples; others describe it as a stress test set that manipulates lexical overlap, subsequence, and negation. One extracted definition also situates it in a binary classification setting, where it is used to assess length bias.

**What it is claimed to measure.** Measurement claims are concentrated rather than spread across many targets. HANS is linked to one construct, Out-of-distribution generalization, and one behavioral indicator, Natural language inference. One paper reports using it for NLI, and the same paper also presents it as an OOD benchmark, saying that these NLI datasets are "suitable benchmarks for evaluating the OOD robustness of ICL."

**Space of uses.** Papers typically use HANS as part of broader evaluation suites rather than in isolation. One paper places it with NAN, PISP, ST, and ANLIR1-R3 for NLI OOD evaluation, another reports "Results on HANS and PAWS-XEN under finetuning and ICL," and another description positions it within OOD and stress test sets for minority generalization. A separate use places it among seven binary classification datasets spanning natural language inference, sentiment analysis, and paraphrase detection.

## Sources

**HANS** (3 papers: [Lost in Inference: Rediscovering the Role of Natural Language Inference for Large Language Models](https://aclanthology.org/2025.naacl-long.466.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf), [Mitigating Shortcut Learning with InterpoLated Learning](https://aclanthology.org/2025.acl-long.450.pdf))
> Natural Language Inference dataset designed to evaluate models' sensitivity to lexical overlap and other artifacts, used here to assess length bias in binary classification.

## Relationships

### → HANS
- **Natural language inference** (behavioral indicator): *measured_by*, 1 paper
  > In particular, for NLI, we employed HANS (McCoy et al., 2019), NAN (Truong et al., 2022), PISP (Liu et al., 2020a,b), ST (Naik et al., 2018), and ANLIR1–R3 (Nie et al., 2020a)... (Section 4.1)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
- **Out-of-distribution generalization** (construct): *measured_by*, 1 paper
  > We used OOD evaluation datasets for NLI and paraphrase identification... for NLI, we employed HANS (McCoy et al., 2019)... making them suitable benchmarks for evaluating the OOD robustness of ICL. (Section 4.1)
  - [Exploring Explanations Improves the Robustness of In-Context Learning](https://aclanthology.org/2025.acl-long.1155.pdf)
