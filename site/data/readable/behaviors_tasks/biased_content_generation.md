# Biased content generation
**Type:** Behavioral indicator  
**Supporting papers:** 10  
**Also known as:** Biased generation, Biased output generation, Biased response generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing treats this behavior as observable text or response generation that reflects unfair or systematic prejudice. Most definitions describe outputs with stereotypes, toxicity, discrimination, or other derogatory associations toward groups or ideas, and one paper operationalizes it through an increase in biased words. Some authors state it broadly as biased or unfair output generation, while others narrow it to responses that reinforce gender bias or target a protected group.

**Variants.** Papers use several near-synonymous names, including biased generation, biased output generation, and biased response generation. The behavior is studied in general text generation and prompt response settings, and smaller strands place it in role-playing scenarios or triggered generation tasks where certain identity-related queries are more likely to yield biased content.

**Space of elicitation and scores.** Papers link this behavior to 1 measurement instrument, BOLD, used as a text generation dataset. No other measurement instrument is linked to it.

**What it is taken as evidence of.** Papers link this behavior to 1 construct, Trustworthiness. The recorded claim is that biased generations are related to trustworthiness, with a paper placing them among drawbacks in trustworthiness alongside non-factual information, rather than presenting a measurement or causal link.

## Sources

**Biased content generation** (2 papers: [PoisonBench: Assessing Language Model Vulnerability to Poisoned Preference Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fu25e/fu25e.pdf), [Your RAG is Unfair: Exposing Fairness Vulnerabilities in Retrieval-Augmented Generation via Backdoor Attacks](https://aclanthology.org/2025.emnlp-main.804.pdf))
> The production of text that reflects unfair prejudice or stereotypes towards certain groups or ideas.

**Biased generation** (1 paper: [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf))
> The observable production of outputs that reflect systematic or unfair prejudice.

**Biased output generation** (1 paper: [ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1453.pdf))
> The observable phenomenon of the model producing outputs that are skewed, prejudiced, or unfair, identified as a potential risk in role-playing scenarios.

**Biased response generation** (2 papers: [FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf), [GenderAlign: An Alignment Dataset for Mitigating Gender Bias in Large Language Models](https://aclanthology.org/2025.acl-long.553.pdf))
> The observable production of outputs containing stereotypes, toxicity, or discrimination.

## Relationships

### Biased content generation →
- **BOLD** (measurement instrument): *measured_by*, 1 paper
  > For text generation, we primarily use the BOLD dataset (Dhamala et al., 2021), and other fairness benchmark datasets Holistic Bias (Smith et al., 2022) and TREC-Fair (Ekstrand et al., 2023). (Section 5.1)
  - [Your RAG is Unfair: Exposing Fairness Vulnerabilities in Retrieval-Augmented Generation via Backdoor Attacks](https://aclanthology.org/2025.emnlp-main.804.pdf)

### Associated with
- **Trustworthiness** (construct), 1 paper
  > However, MLLMs are proven to exhibit significant drawbacks in trustworthiness, such as hallucination (Rawte et al., 2023; Zhang et al., 2024; Wang et al., 2024a), which results in non-factual information (Ji et al., 2023) and biased generations (Zou et al., 2023). (Section 1)
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
