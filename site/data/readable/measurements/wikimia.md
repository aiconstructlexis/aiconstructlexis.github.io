# WikiMIA
**Type:** Measurement instrument  
**Supporting papers:** 7  
**Also known as:** WIKIMIA  

## State of the Field

**What it is.** Across papers, the prevailing description treats WikiMIA as a benchmark or dataset for evaluating training or pretraining data detection on large language models. Definitions commonly describe it as temporal: it uses Wikipedia data or excerpts labeled as seen or unseen, or as training and non-training, based on publication date relative to a model's training cutoff or release timeline. A smaller framing presents the same date-based split as a membership inference benchmark, with member and non-member data separated by publication date.

**What it is claimed to measure.** Papers use WikiMIA to measure one behavioral indicator, Pre-training data detection, and they do not link it to any constructs. The links converge on that single indicator: papers say pre-training data detection is measured by WikiMIA, and describe it as commonly used for evaluating pretraining data detection methods or for verifying the effectiveness of detection methods. One paper also reports that Membership inference attack is related to WikiMIA, rather than presenting it as what WikiMIA measures.

**Space of uses.** In use, papers often position WikiMIA as a benchmark within evaluation suites, most explicitly alongside MIMIR and, in other studies, alongside ArXivTection, BookTection, BookMIA, and Pile. Some authors foreground it as one of the main benchmarks they focus on for pre-training data detection, while others include it among several common benchmarks when testing methods. A separate use applies the benchmark to membership inference on LLM pre-training texts.

**Concerns raised.** Only one concern is explicit in the papers here: one paper says the publication-date split has been criticized for introducing artificial distribution shifts. The same paper notes that a blind baseline, predicting membership solely from text content without any model access, already achieves 98.7% AUC on this setup.

## Sources

**WIKIMIA** (1 paper: [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf))
> A dataset specifically designed to evaluate training data detection algorithms on large language models.

**WikiMIA** (2 papers: [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf), [Context-Aware Membership Inference Attacks against Pre-trained Large Language Models](https://aclanthology.org/2025.emnlp-main.370.pdf))
> A temporal benchmark dataset for evaluating pretraining data detection methods, containing excerpts from Wikipedia articles classified as "seen" or "unseen" based on their publication date relative to a model's training cutoff.

## Relationships

### → WikiMIA
- **Pre-training data detection** (behavioral indicator): *measured_by*, 5 papers
  > To facilitate this study, we introduce a dynamic benchmark WIKIMIA that uses data created before and after model training to support gold truth detection. (Abstract)
  - [Detecting Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e32ad85fa27be4a9868d55703f01323e-Paper-Conference.pdf)
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
  - [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)
  - [Identifying Pre-training Data in LLMs: A Neuron Activation-Based Detection Framework](https://aclanthology.org/2025.emnlp-main.946.pdf)

### Associated with
- **Membership inference attack** (measurement instrument), 1 paper
  > MIA on LLM pre-training texts. We use the WikiMIA benchmark [52], which leverages the Wikipedia timestamp to separate the early Wiki data as the member data, and recent Wiki data as the non-member data (Section 6.3).
  - [Membership Inference Attacks against Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b2c892312af07f8a77afbeed188391f4-Paper-Conference.pdf)
