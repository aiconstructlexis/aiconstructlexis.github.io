# WMT23
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** WMT’23, WMT 2023  

## State of the Field

**What it is.** Most commonly, papers treat WMT23 as the 2023 Workshop or Conference on Machine Translation shared-task test set or benchmark for evaluating machine translation systems and translation quality across multiple language pairs. Some definitions add that it contains human-rated translations across multiple language pairs and systems, and one study specifically uses the WMT'23 MQM ratings for English-German and Chinese-English. Another use frames it as the source of contaminated test examples drawn from ten language pairs.

**What it is claimed to measure.** Papers use it to evaluate machine translation systems or translation quality, including fine-grained machine translation evaluation in one study. They do not explicitly use it to measure any named construct or behavioral indicator.

**Space of uses.** The prevailing usage is as a benchmark or test set in model evaluation. One study evaluates a Specialist method on WMT'23 and compares it with the XCOMET metric, another uses WMT 2023 as the source of contaminated test examples and then decontaminates the set, and another places WMT23 under generative tasks.

**Concerns raised.** Contamination is the only explicit concern raised in the papers here: one study sources contaminated data from WMT 2023 across ten language pairs. The same study reports removing 681 WMT'23 examples during decontamination, leaving 9,491 examples.

## Sources

**WMT’23** (1 paper: [From Jack of All Trades to Master of One: Specializing LLM-based Autoraters to a Test Set](https://raw.githubusercontent.com/mlresearch/v267/main/assets/finkelstein25a/finkelstein25a.pdf))
> Annual Conference on Machine Translation shared task dataset for evaluating machine translation systems, containing human-rated translations across multiple language pairs and systems.

**WMT 2023** (1 paper: [Overestimation in LLM Evaluation: A Controlled Large-Scale Study on Data Contamination’s Impact on Machine Translation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kocyigit25a/kocyigit25a.pdf))
> A machine translation evaluation dataset from the Workshop on Machine Translation 2023, used in this study as the source of contaminated test examples.

**WMT23** (2 papers: [LAuReL: Learned Augmented Residual Layer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/menghani25a/menghani25a.pdf), [Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention](https://aclanthology.org/2025.acl-long.270.pdf))
> Machine translation benchmark evaluating translation quality across multiple language pairs in the 2023 conference evaluation campaign.
