# SST-5
**Type:** Measurement instrument  
**Supporting papers:** 23  
**Also known as:** SST5  

## State of the Field

**What it is.** Across the surveyed work, the dominant framing treats SST-5, also written SST5, as the Stanford Sentiment Treebank for fine-grained sentiment classification with five labels. Definitions usually describe the labels as ranging from very negative to very positive, and one source spells out the five classes as "very positive", "positive", "neutral", "negative", and "very negative"; some papers also specify that the texts are movie reviews. Papers alternate between calling it a benchmark, a dataset, and a task, and one definition describes it as a five-class sentiment classification benchmark used to evaluate fine-tuned model performance.

**What it is claimed to measure.** Papers link SST-5 to 3 behavioral indicators and 2 constructs. The prevailing use is to measure Sentiment analysis, with several papers labeling it as a sentiment analysis or sentiment classification dataset. Smaller lines of work report Controlled sentiment generation and Multiple-choice question answering as measured by SST-5, and single papers also use it to measure In-context learning and Reasoning, so the recorded claims spread across several targets rather than centering on only one construct.

**Space of uses.** Most commonly, papers use SST-5 as one element in broader evaluation suites rather than as a standalone instrument. It is most often used alongside SST-2, and papers also place it with SNLI, RTE, MNLI, and GSM-8K, with additional use in larger collections of benchmark tasks. In these papers it appears in fine-tuning evaluations, few-shot and in-context learning experiments, prompt optimization, demonstration selection, and, in one case, sentiment steering.

## Sources

**SST-5** (9 papers: [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf), [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf), [Stable Anisotropic Regularization](https://proceedings.iclr.cc/paper_files/paper/2024/file/6691c5e4a199b72dffd9c90acb63bcd6-Paper-Conference.pdf), [Pareto Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf), [D.Va: Validate Your Demonstration First Before You Use It](https://aclanthology.org/2025.acl-long.129.pdf), [Large Language Models are Demonstration Pre-Selectors for Themselves](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25i/jin25i.pdf), [QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models](https://aclanthology.org/2025.emnlp-main.271.pdf), [LLMs vs Established Text Augmentation Techniques for Classification: When do the Benefits Outweight the Costs?](https://aclanthology.org/2025.naacl-long.526.pdf), [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf))
> A five-class sentiment classification benchmark used to evaluate fine-tuned model performance.

**SST5** (4 papers: [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf), [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf), [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf), [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486.pdf))
> Stanford Sentiment Treebank (SST5) is a benchmark for fine-grained sentiment classification with five labels (from very negative to very positive).

## Relationships

### → SST-5
- **Sentiment analysis** (behavioral indicator): *measured_by*, 3 papers
  > SST-5 [40] Sentiment Analysis (Table 1)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
  - [Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf)
  - [Graceful Forgetting in Generative Language Models](https://aclanthology.org/2025.emnlp-main.666.pdf)
- **In-context learning** (construct): *measured_by*, 1 paper
  > We conduct experiments to investigate the correlation between subset influence and its corresponding in-context learning performance. (Section 4.3.1, Figure 4a on SST-5)
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > For the multiple-choice tasks, we use datasets: COPA (Gordon et al., 2012), StoryCloze (Mostafazadeh et al., 2016), NLI (Bowman et al., 2015), MMLU (Hendrycks et al., 2021), SST2 (Socher et al., 2013), SST5 (Socher et al., 2013), BoolQ (Clark et al., 2019), and Winogrande (Sakaguchi et al., 2020)... (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **Controlled sentiment generation** (behavioral indicator): *measured_by*, 1 paper
  > using Stanford Sentiment Treebank (SST5) (Socher et al., 2013) for sentiment steering (Section 5)
  - [LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](https://aclanthology.org/2025.acl-long.393.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > To further assess the generalizability and effectiveness of RDES beyond simple text classification, we conducted additional experiments on more challenging reasoning benchmarks: BigBenchHard (specifically, boolean expressions and web of lies subsets), SST5 and GSM-8K. (Section 4.5)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
