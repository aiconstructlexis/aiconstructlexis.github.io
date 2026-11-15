# Pre-training data detection
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Training data detection, Pretraining data detection, Copyrighted book detection  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is a binary detection task over text: papers describe deciding whether a text sample, sentence, or text sequence was part of an LLM's training or pretraining data. Most definitions make success explicit as separating or classifying training versus non-training examples, sometimes through a scoring function over model outputs, and one study says that "the goal is to detect whether a given sentence is in the dataset used for training a Large Language Model" (Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models). A narrower application treats the same behavior as copyrighted book detection, asking whether excerpts from copyrighted books were included in training data.

**Variants.** Papers use closely related names for the behavior, most commonly pre-training or pretraining data detection, with some authors using training data detection. The clearest sub-setting is copyrighted book detection, which focuses on excerpts from copyrighted books. Some papers also connect the task to membership inference attack, describing pre-training data detection as a special case or using membership inference as a related name.

**Space of elicitation and scores.** Papers link the behavior to 6 instruments overall. The recurring measurement benchmarks are WikiMIA, MIMIR, BookMIA, and BookTection; papers describe WikiMIA as a dynamic or temporal benchmark built from data created before and after model training, while MIMIR is presented as a more challenging setting with high n-gram overlap between seen and unseen texts. Some papers also connect the task to membership inference attack rather than a benchmark instrument, and one other linked instrument is reported.

**What it is taken as evidence of.** Papers link it to 3 constructs rather than one shared construct. One paper claims a causal relationship from memorization to pre-training data detection, stating that memory effects on training data are a reason detection algorithms are effective. A separate line relates the behavior to overfitting, describing effectiveness as closely tied to training-data memorization or overfitting, and one paper links training data detection to privacy preservation by saying it is commonly employed to assess privacy risks.

## Sources

**Pre-training data detection** (1 paper: [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf))
> The observable task of determining whether a given text sample was part of a large language model's pre-training corpus by analyzing the model's output statistics.

**Training data detection** (1 paper: [A Statistical Approach for Controlled Training Data Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/c859b99b5d717c9035e79d43dfd69435-Paper-Conference.pdf))
> The observable task of classifying a given text sample as either having been part of the model's training set or not.

**Pretraining data detection** (1 paper: [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf))
> The observable task of classifying whether a given text sequence was included in a language model's pretraining dataset.

**Copyrighted book detection** (2 papers: [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf), [Detecting Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e32ad85fa27be4a9868d55703f01323e-Paper-Conference.pdf))
> The specific application of pretraining data detection to identify excerpts from copyrighted books within the model's training data.

## Relationships

### Pre-training data detection →
- **WikiMIA** (measurement instrument): *measured_by*, 5 papers
  > To facilitate this study, we introduce a dynamic benchmark WIKIMIA that uses data created before and after model training to support gold truth detection. (Abstract)
  - [Detecting Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e32ad85fa27be4a9868d55703f01323e-Paper-Conference.pdf)
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
  - [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)
  - [Identifying Pre-training Data in LLMs: A Neuron Activation-Based Detection Framework](https://aclanthology.org/2025.emnlp-main.946.pdf)
- **MIMIR** (measurement instrument): *measured_by*, 2 papers
  > We focus on two benchmarks (and the only two to our knowledge) for pre-training data detection, WikiMIA (Shi et al., 2024) and MIMIR (Duan et al., 2024).
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
  - [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)
- **BookTection** (measurement instrument): *measured_by*, 1 paper
  > To verify the effectiveness of detection methods, we employ four common benchmark datasets for evaluations, including WikiMIA (Shi et al., 2024), ArXivTection (Duarte et al., 2024), BookTection (Duarte et al., 2024) BookMIA (Shi et al., 2024) and Pile (Maini et al., 2024). (Section 4.1)
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)
- **BookMIA** (measurement instrument): *measured_by*, 1 paper
  > To verify the effectiveness of detection methods, we employ four common benchmark datasets for evaluations, including WikiMIA (Shi et al., 2024), ArXivTection (Duarte et al., 2024), BookTection (Duarte et al., 2024) BookMIA (Shi et al., 2024) and Pile (Maini et al., 2024). (Section 4.1)
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)
- **The Pile** (measurement instrument): *measured_by*, 1 paper
  > To verify the effectiveness of detection methods, we employ four common benchmark datasets for evaluations, including WikiMIA (Shi et al., 2024), ArXivTection (Duarte et al., 2024), BookTection (Duarte et al., 2024) BookMIA (Shi et al., 2024) and Pile (Maini et al., 2024). (Section 4.1)
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)

### → Pre-training data detection
- **Memorization** (construct): *causes*, 1 paper
  > The powerful learning capabilities of LLMs often lead to noticeable memory effects on training data. This characteristic is a key reason why pre-training data detection algorithms are effective (Carlini et al., 2021; Tirumala et al., 2022). (Section 3.5)
  - [Identifying Pre-training Data in LLMs: A Neuron Activation-Based Detection Framework](https://aclanthology.org/2025.emnlp-main.946.pdf)

### Associated with
- **Membership inference attack** (measurement instrument), 3 papers
  > Pre-training data detection can be considered a special case of Membership Inference Attack (MIA) (Shokri et al., 2017): the goal is to infer whether a given input has been used for training a target LLM
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
  - [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)
  - [Identifying Pre-training Data in LLMs: A Neuron Activation-Based Detection Framework](https://aclanthology.org/2025.emnlp-main.946.pdf)
- **Privacy preservation** (construct), 1 paper
  > Training data detection (TDD) is commonly employed to assess privacy risks in machine learning models (Murakonda & Shokri, 2020).
  - [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf)
- **Overfitting** (construct), 1 paper
  > A common view is that the effectiveness of TDD is closely tied to the level of training-data memorization or overfitting exhibited by the target model during training (Yeom et al., 2018; Long et al., 2018).
  - [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf)
