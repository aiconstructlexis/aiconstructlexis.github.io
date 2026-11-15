# WinoBias
**Type:** Measurement instrument  
**Supporting papers:** 14  
**Also known as:** Winobias  

## State of the Field

**What it is.** Across the papers, WinoBias is most commonly described as a coreference resolution benchmark or dataset for gender bias, built from Winograd-style examples about professions and pronouns. Definitions converge on testing pronoun resolution in stereotypical and anti-stereotypical settings, often around gender-occupation associations. One description says each example contains two gender-neutral profession names and gendered pronouns, and the task is to identify the coreference link to the correct profession, while another describes the items more broadly as gendered sentence pairs.

**What it is claimed to measure.** Papers link WinoBias to two constructs and one behavioral indicator. The prevailing use is to measure gender bias: papers describe it as evaluating whether models assign stereotypical gender pronouns to occupations, and one paper calls it an "ecologically valid probe" for detecting gender biases in pronoun resolution; another formulation says it measures dependency between output words and social groups. Papers also use it to measure coreference resolution, and a smaller line of work uses it to measure social bias.

**Space of uses.** Most descriptions position it as a conventional, popular, or commonly used fairness benchmark, including one that has been applied to LLM-generated text. Papers use it alongside Winogender, and some pair it with StereoSet or BBQ. Some work repurposes it for non-stereotypical evaluation, while another paper treats it as an out-of-distribution bias benchmark for testing generalization.

**Concerns raised.** The main explicit concern is about assessment reliability: one paper states that conventional fairness benchmarks such as WinoBias pose challenges to reliably assessing modern LLMs.

## Sources

**WinoBias** (5 papers: [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf), [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf), [The Impossibility of Fair LLMs](https://aclanthology.org/2025.acl-long.5.pdf), [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf), [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf))
> Coreference resolution benchmark designed to measure gender bias by evaluating model performance on pro- and anti-stereotypical Winograd-style examples involving professions and pronouns.

**Winobias** (2 papers: [Are Models Biased on Text without Gender-related Language?](https://proceedings.iclr.cc/paper_files/paper/2024/file/37771cc0be272368102a37f202bb88d8-Paper-Conference.pdf), [LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations](https://proceedings.iclr.cc/paper_files/paper/2025/file/a712d461e57201efe35d429a6f1731c1-Paper-Conference.pdf))
> A coreference resolution benchmark designed to evaluate gender-occupation bias in language models by testing pronoun resolution in gendered sentence pairs.

## Relationships

### → WinoBias
- **Gender bias** (construct): *measured_by*, 6 papers
  > To answer the first question, we check the LLaMA performance on popular tests for gender bias: WinoBias (Zhao et al., 2018) and StereoSet (Nadeem et al., 2021). (Section 1)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
  - [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf)
  - [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf)
  - [Prompting Fairness: Integrating Causality to Debias Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f26a2d143a227376dff99a279f93f99-Paper-Conference.pdf)
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **Coreference resolution** (behavioral indicator): *measured_by*, 4 papers
  > WinoBias Zhao et al. (2018) present the dataset containing a WinoGrad scheme (Levesque et al., 2011) examples. ... The task is to identify the coreference link between the pronouns and the correct professional. (Section 2.3)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
  - [Prompting Fairness: Integrating Causality to Debias Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f26a2d143a227376dff99a279f93f99-Paper-Conference.pdf)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
  - [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf)
- **Social bias** (construct): *measured_by*, 1 paper
  > ...and evaluated on out-of-distribution bias benchmarks such as WinoBias (Zhao et al., 2018) and Winogender (Rudinger et al., 2018) to test generalization (Section 1).
  - [LLM Bias Detection and Mitigation through the Lens of Desired Distributions](https://aclanthology.org/2025.emnlp-main.76.pdf)
