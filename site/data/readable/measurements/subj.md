# Subj
**Type:** Measurement instrument  
**Supporting papers:** 9  
**Also known as:** SUBJ  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats Subj or SUBJ as a subjectivity classification dataset or benchmark for distinguishing subjective from objective text. Most definitions describe a binary text classification task, often at the sentence level, and some papers place it under general natural language understanding or text classification evaluation. A smaller line describes it as a binary classification dataset of movie reviews labeled objective or subjective, and definitions also situate it in in-context evaluation of fine-tuned models or in low-data evaluation.

**What it is claimed to measure.** Recorded links focus on behavioral indicators rather than constructs: papers use Subj to measure 2 behavioral indicators, Text classification and Subjectivity classification, and no constructs are linked to it. The dominant linkage is to Text classification, where papers place Subj among datasets that admit classification tasks or use it in text classification evaluation suites. A narrower linkage reports it as measuring Subjectivity classification through the objective versus subjective decision task.

**Space of uses.** Papers typically use Subj alongside other text classification or natural language understanding datasets, with examples including TREC, AG News, MR, SST-2, and Rotten Tomatoes. It is usually one task within a broader evaluation suite, and some definitions specifically frame it for in-context evaluation of fine-tuned models or for low-data natural language understanding evaluation. No measurement instrument is linked to it.

## Sources

**Subj** (4 papers: [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf), [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf), [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/686a3f32067838c8dbb68da6e9e3cf69-Paper-Conference.pdf), [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf))
> A subjectivity classification benchmark used for in-context evaluation of fine-tuned models.

**SUBJ** (3 papers: [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf), [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf), [Large Language Models are Demonstration Pre-Selectors for Themselves](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25i/jin25i.pdf))
> A binary classification dataset of movie reviews, labeled as objective or subjective, used to evaluate natural language understanding in a low-data regime.

## Relationships

### → Subj
- **Text classification** (behavioral indicator): *measured_by*, 2 papers
  > We primarily evaluate our method on AG News (4 classes) [77], SST-2 (2 classes) [57], Rotten Tomatoes (2 classes) [50], and Subj (2 classes) [18] datasets which all admit classification tasks. (Section 5.2)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
- **Subjectivity classification** (behavioral indicator): *measured_by*, 1 paper
  > Task description. SUBJ (Pang & Lee, 2004) is a binary classification dataset for natural language understanding.
  - [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)
