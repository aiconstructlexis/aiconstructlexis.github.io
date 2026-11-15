# ETHICS
**Type:** Measurement instrument  
**Supporting papers:** 11  
**Also known as:** ETHICS dataset, Ethics, Hendrycks Ethics  

## State of the Field

**What it is.** Across definitions, ETHICS is most commonly described as a benchmark dataset for machine ethics or ethical reasoning built from morally charged, scenario-based examples. Papers variously describe first-person descriptions of morally relevant actions with binary labels, tasks where models categorize scenarios as "wrong" or "not wrong," and subsets such as Commonsense, Justice, and Deontology; one description highlights the Commonsense subset as featuring scenario-based moral recognition tasks. A smaller framing treats it more narrowly as a zero-shot benchmark or as a dataset assessing whether described actions are wrong.

**What it is claimed to measure.** Papers link ETHICS to 2 constructs and 2 behavioral indicators, and the prevailing use is as a measure of Moral reasoning. A smaller line of work treats it as measuring Ethical decision-making, while behavioral-indicator links report its use for Binary classification and Zero-shot task performance. Overall, the claims concentrate on moral reasoning, and one relationship explicitly states that ETHICS mainly measures an LLM's moral reasoning ability.

**Space of uses.** No other measurement instrument is linked to it by an explicit relationship. In use, papers place ETHICS alongside benchmarks such as Social Chemistry 101, TruthfulQA, ToxiGen, δ-ROT, and BBQ, and position it within broader evaluations of morality, safety and helpfulness, or values. Several papers also use selected parts rather than the full benchmark, especially Commonsense and Justice.

**Concerns raised.** One paper notes that the common-sense moral scenarios it uses from ETHICS were collected from English-speaking participants in the United States, Canada, and Great Britain, and therefore says the dataset dominantly reflects a Western ethical perspective.

## Sources

**ETHICS dataset** (1 paper: [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf))
> A benchmark dataset consisting of morally charged scenarios used to evaluate a model's ability to perform implicit ethical assessments.

**Ethics** (1 paper: [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf))
> A zero-shot benchmark dataset used to assess model accuracy on ethical reasoning tasks.

**ETHICS** (3 papers: [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf), [Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf), [The discordance between embedded ethics and cultural inference in large language models](https://aclanthology.org/2025.emnlp-main.743.pdf))
> A benchmark for evaluating machine ethics, including a 'Commonsense' subset with scenario-based moral recognition tasks.

**Hendrycks Ethics** (1 paper: [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf))
> Dataset assessing ethical judgment on whether described actions are wrong.

## Relationships

### → ETHICS
- **Moral reasoning** (construct): *measured_by*, 5 papers
  > To verify ALI-Agent’s effectiveness as a general evaluation framework, we conduct experiments on six datasets from three distinct aspects of human values: ...morality (ETHICS [3], Social Chemistry 101 [37])...
  - [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
  - [Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf)
  - [Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework](https://aclanthology.org/2025.emnlp-main.1541.pdf)
- **Ethical decision-making** (construct): *measured_by*, 1 paper
  > "Implicit Ethics: Using the ETHICS dataset [63], we use LLM to categorize morally charged scenarios as “wrong” or “not wrong”."
  - [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf)
- **Zero-shot task performance** (behavioral indicator): *measured_by*, 1 paper
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
- **Binary classification** (behavioral indicator): *measured_by*, 1 paper
  > We use the “Justice” and “Commonsense” datasets from ETHICS (Hendrycks et al., 2020), which involve binary classification based on basic moral concepts. (Section 5.3)
  - [Representations Shape Weak-to-Strong Generalization: Theoretical Insights and Empirical Predictions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xue25d/xue25d.pdf)
