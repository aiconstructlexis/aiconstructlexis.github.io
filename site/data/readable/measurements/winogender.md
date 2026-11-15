# Winogender
**Type:** Measurement instrument  
**Supporting papers:** 6  
**Also known as:** WinoGender  

## State of the Field

**What it is.** Across the papers, Winogender is most commonly described as a diagnostic or benchmark dataset for gender bias in coreference resolution, especially gender-occupation bias. Definitions describe it as testing whether models resolve pronouns in a gender-stereotyped manner, and one paper specifies sentence templates with gendered pronouns and a Pearson correlation between model probabilities for female pronouns and occupations' female gender statistics. A smaller line of work repurposes the benchmark for non-stereotypical evaluation by filtering out sentences with strong gender co-occurrences, and another paper groups it with WinoGrad Schema based datasets and describes it as similar to WinoBias.

**What it is claimed to measure.** Papers use Winogender to measure 2 constructs and no behavioral indicators: Gender bias and Social bias. The prevailing framing in the definitions is Gender bias in coreference resolution, while one paper also uses it to measure Social bias as an out-of-distribution bias benchmark for testing generalization. Overall, its reported measurement use stays within bias constructs rather than specific behavioral indicators.

**Space of uses.** No paper directly links Winogender to another measurement instrument, but papers frequently use it alongside WinoBias, and some also pair it with CrowS-Pairs, TruthfulQA, BBQ, and WinoBias+. In those settings it is positioned as one of the widely studied or widely used bias benchmarks, sometimes under a human alignment grouping and sometimes as an out-of-distribution benchmark for testing generalization. Another reported use is as a repurposed non-stereotypical evaluation set after filtering sentences with strong gender co-occurrences.

**Concerns raised.** One paper states that WinoGender, together with related WinoGrad Schema based datasets, is "no longer adequate to evaluate recent LLMs." Other papers describe its use and repurposing without stating additional explicit concerns.

## Sources

**Winogender** (1 paper: [Are Models Biased on Text without Gender-related Language?](https://proceedings.iclr.cc/paper_files/paper/2024/file/37771cc0be272368102a37f202bb88d8-Paper-Conference.pdf))
> Winogender (WG), a coreference-resolution gender-occupation bias benchmark repurposed here by filtering out sentences with strong gender co-occurrences.

**WinoGender** (3 papers: [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf), [GenderAlign: An Alignment Dataset for Mitigating Gender Bias in Large Language Models](https://aclanthology.org/2025.acl-long.553.pdf), [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf))
> Diagnostic dataset evaluating gender bias in coreference resolution by testing whether models resolve pronouns in a gender-stereotyped manner.

## Relationships

### → Winogender
- **Social bias** (construct): *measured_by*, 1 paper
  > ...and evaluated on out-of-distribution bias benchmarks such as WinoBias (Zhao et al., 2018) and Winogender (Rudinger et al., 2018) to test generalization (Section 1).
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
- **Gender bias** (construct): *measured_by*, 1 paper
  > We also conduct experiments on BBQ (Parrish et al., 2022) and WinoGender (Zhao et al., 2018), two widely used datasets for evaluating gender bias in LLMs. (Section 1)
  - [GenderAlign: An Alignment Dataset for Mitigating Gender Bias in Large Language Models](https://aclanthology.org/2025.acl-long.553.pdf)
