# MultiRC
**Type:** Measurement instrument  
**Supporting papers:** 16  
**Also known as:** MRC, Multi-sentence reading comprehension  

## State of the Field

**What it is.** Across the surveyed work, MultiRC is most commonly described as a multi-sentence reading comprehension dataset or benchmark for question answering. Definitions present it as a multiple choice dataset, sometimes evaluated with exact-match accuracy, and several quoted passages say its questions require reasoning over, or synthesizing information from, multiple sentences in a passage; some also note that a passage question may have multiple correct answers. A smaller line of work phrases it as the task itself, namely answering a question by combining information from multiple sentences, and one definition places it within SuperGLUE.

**What it is claimed to measure.** Papers link MultiRC to one construct and one behavioral indicator. The more common measurement claim is that it measures machine reading comprehension, with papers describing it as a question-answering dataset testing reading comprehension and using it among validation sets that cover reading comprehension. A separate use treats it as measuring general ability by including it in a broader cross-domain evaluation set, so the reported measurement claims span both a behavioral indicator and a construct rather than centering on only one target.

**Space of uses.** Papers usually position MultiRC as part of broader evaluation suites rather than in isolation. Among measurement instruments, it is linked to one other instrument, SuperGLUE, and one paper describes it as one of six NLU tasks from that benchmark; another uses it alongside ARC and OpenBookQA as validation sets for generalization loss estimation. Other quoted passages use it as a task for fine-tuning and efficiency comparisons, including reports of performance gains on MultiRC and reduced memory usage for the task.

## Sources

**MultiRC** (4 papers: [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf), [Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf), [LASER: Attention with Exponential Transformation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duvvuri25a/duvvuri25a.pdf), [QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models](https://aclanthology.org/2025.emnlp-main.271.pdf))
> Multi-Sentence Reading Comprehension, a multiple choice dataset evaluated with exact-match accuracy.

**MRC** (1 paper: [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf))
> Multi-Sentence Reading Comprehension (MultiRC) is a dataset from the SuperGLUE benchmark for a question answering task.

**Multi-sentence reading comprehension** (1 paper: [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://aclanthology.org/2025.naacl-long.230.pdf))
> The task of answering a question that requires synthesizing information from multiple sentences within a passage.

## Relationships

### → MultiRC
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 2 papers
  > Additionally, we use ARC (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018), and MultiRC (Khashabi et al., 2018), covering question answering, commonsense reasoning, and reading comprehension, as validation sets for generalization loss estimation.
  - [Optimizing Pre-Training Data Mixtures with Mixtures of Data Expert Models](https://aclanthology.org/2025.acl-long.1564.pdf)
  - [Regress, Don’t Guess: A Regression-like Loss on Number Tokens for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zausinger25a/zausinger25a.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > "We evaluate the pre-trained base models on 17 tasks across different general domains which include: MMLU (Hendrycks et al., 2020), Arc-Easy, Arc-Challenge (Clark et al., 2018), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), SciQ (Welbl et al., 2017), RTE (Dagan et al., 2005), BBH (Suzgun et al., 2022), LAMBADA (Paperno et al., 2016), OpenBookQA (Mihaylov et al., 2018), RACE-Middle, RACE-High (Lai et al., 2017), MultiRC"
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)

### Associated with
- **SuperGLUE** (measurement instrument), 1 paper
  > “we use six NLU tasks from the SuperGLUE benchmark to evaluate the performance of the language model ... including ... MRC”
  - [MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.823.pdf)
