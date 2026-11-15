# BOLD
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats BOLD as a benchmark or evaluation dataset for open-ended language generation, with English text prompts used for bias benchmarking. Definitions most often describe prompts spanning five domains, and one definition specifies Wikipedia-derived prompts covering race, gender, profession, religion, and politics. Papers variously frame it as evaluating fairness, social bias, and toxicity, and some describe it as assessing sentiment or the affective properties of model outputs for diverse demographic prompts.

**What it is claimed to measure.** Papers link BOLD to 2 constructs and 1 behavioral indicator. The dominant measurement claim is that it measures social bias, with several papers describing it as a bias evaluation dataset or as designed to evaluate social biases in generative language models. A smaller line of work uses it to measure gender bias, and one paper reports that it measures biased content generation, so the reported links are concentrated on social bias with narrower uses for the other targets.

**Space of uses.** In use, papers place BOLD alongside other generation and fairness benchmarks, most commonly RealToxicityPrompts, and more occasionally AttaQ, BBQ, Holistic Bias, and TREC-Fair. Some papers position it as a primary dataset for text generation or general domain bias assessment, while others use it as an additional benchmark to test the consistency of detoxification ability or to compare bias mitigation results across benchmarks.

## Sources

**BOLD** (5 papers: [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf), [Building Trust in Clinical LLMs: Bias Analysis and Dataset Transparency](https://aclanthology.org/2025.emnlp-main.1174.pdf), [Exploring the Impact of Personality Traits on LLM Bias and Toxicity](https://aclanthology.org/2025.emnlp-main.206.pdf), [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models](https://aclanthology.org/2025.emnlp-main.774.pdf), [Your RAG is Unfair: Exposing Fairness Vulnerabilities in Retrieval-Augmented Generation via Backdoor Attacks](https://aclanthology.org/2025.emnlp-main.804.pdf))
> A benchmark dataset used to evaluate fairness and toxicity in language models, particularly for analyzing biases like gender bias.

## Relationships

### → BOLD
- **Social bias** (construct): *measured_by*, 3 papers
  > BOLD is an open-ended language generation dataset that provides English text generation prompts for bias benchmarking across five domains. (Section 3.2)
  - [Exploring the Impact of Personality Traits on LLM Bias and Toxicity](https://aclanthology.org/2025.emnlp-main.206.pdf)
  - [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models](https://aclanthology.org/2025.emnlp-main.774.pdf)
  - [Building Trust in Clinical LLMs: Bias Analysis and Dataset Transparency](https://aclanthology.org/2025.emnlp-main.1174.pdf)
- **Biased content generation** (behavioral indicator): *measured_by*, 1 paper
  > For text generation, we primarily use the BOLD dataset (Dhamala et al., 2021), and other fairness benchmark datasets Holistic Bias (Smith et al., 2022) and TREC-Fair (Ekstrand et al., 2023). (Section 5.1)
  - [Your RAG is Unfair: Exposing Fairness Vulnerabilities in Retrieval-Augmented Generation via Backdoor Attacks](https://aclanthology.org/2025.emnlp-main.804.pdf)
- **Gender bias** (construct): *measured_by*, 1 paper
  > Additionally, we further conducted an experiment where we use the BOLD dataset to analyze LM gender bias, results are shown in appendix Table 13. (Section 4.4)
  - [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf)
