# DBPedia
**Type:** Measurement instrument  
**Supporting papers:** 12  
**Also known as:** DBpedia, Dbpedia, DB Pedia  

## State of the Field

**What it is.** Most papers describe DBPedia as a benchmark dataset for topic or ontology classification based on Wikipedia articles. The prevailing description is a 14-way, 14-class task for categorizing text into non-overlapping ontological classes, and some papers frame it more generally as multi-class text classification or text categorization. A smaller line of work describes DBpedia as a hierarchical text classification benchmark, with Wikipedia articles organized in a three-layer taxonomy tree with 9/70/219 classes.

**What it is claimed to measure.** Papers use DBPedia to measure two behavioral indicators, and the dominant link is to text classification. In those papers it is reported as evaluating classification tasks, topic classification, or multi-class classification of Wikipedia articles. A smaller line of work uses it to measure hierarchical text classification. No constructs are linked to it.

**Space of uses.** Papers often present DBPedia as a public evaluation dataset within multi-dataset experiments rather than as a standalone protocol. It appears alongside other classification benchmarks such as AGNews, SST2, Yelp Polarity, and TREC, and one paper also uses it among other publicly available test datasets. No measurement instrument is linked to it.

## Sources

**DBPedia** (4 papers: [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf), [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf), [Plausible Token Amplification for Improving Accuracy of Differentially Private In-Context Learning Based on Implicit Bayesian Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yamasaki25a/yamasaki25a.pdf))
> A benchmark dataset for 14-way topic classification derived from Wikipedia, used to evaluate a model's ability to categorize text into one of fourteen ontological classes.

**Dbpedia** (1 paper: [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf))
> The DBpedia ontology classification dataset, a benchmark for topic classification.

**DBpedia** (3 papers: [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf), [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf), [Ensembling Prompting Strategies for Zero-Shot Hierarchical Text Classification with Large Language Models](https://aclanthology.org/2025.emnlp-main.918.pdf))
> A dataset for ontology classification derived from Wikipedia, used to evaluate text categorization.

**DB Pedia** (1 paper: [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf))
> A topic classification dataset derived from Wikipedia, with 14 classes corresponding to DBpedia ontology types.

## Relationships

### → DBPedia
- **Text classification** (behavioral indicator): *measured_by*, 5 papers
  > ...and 14-way topic classification DBPedia (Zhang et al., 2015) datasets for classification tasks. (Section 5.1)
  - [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
  - [Data-adaptive Differentially Private Prompt Synthesis for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96d00450ed65531ffe2996daed487536-Paper-Conference.pdf)
  - [Plausible Token Amplification for Improving Accuracy of Differentially Private In-Context Learning Based on Implicit Bayesian Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yamasaki25a/yamasaki25a.pdf)
- **Hierarchical text classification** (behavioral indicator): *measured_by*, 1 paper
  > We conduct experiments on the following three public datasets: ... 2) DBpedia consists of Wikipedia articles with a three-layer taxonomy tree...
  - [Ensembling Prompting Strategies for Zero-Shot Hierarchical Text Classification with Large Language Models](https://aclanthology.org/2025.emnlp-main.918.pdf)
