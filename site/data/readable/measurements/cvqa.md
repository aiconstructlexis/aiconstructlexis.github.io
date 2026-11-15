# CVQA
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across papers, CVQA is most commonly described as a culturally diverse, multilingual visual question answering benchmark and dataset for culturally specific or culturally diverse images and questions. Definitions describe it as a large-scale resource spanning 31 languages and 30 countries, written in both English and local languages, while one definition instead calls it a cross-lingual VQA dataset. Its questions are described as multiple choice, with one correct answer and three distractors, and the benchmark is also said to be convertible into free-text open-ended QA.

**What it is claimed to measure.** Papers use CVQA to measure three constructs and three behavioral indicators, with claims spread across several targets rather than centered on one alone. The prevailing construct-level uses are for cultural bias, cultural understanding, and multilingual understanding: papers say it can assess the cultural capability and bias of multimodal models, and use it to assess a model's ability to reason about and understand culturally diverse visual content. At the behavioral level, it is reported as measuring visual question answering, and descriptions of its format also link it to additional question-answering modes through its multiple-choice setup and its convertibility to free-text open-ended QA.

**Space of uses.** Papers present CVQA as a benchmark in its own right, and one paper says it can serve as a probing evaluation suite for assessing cultural capability and bias in multimodal models. It also appears alongside other datasets in combined evaluations: one paper uses CVQA with MaRVL to assess reasoning about culturally diverse visual content, and another uses CVQA with A-OKVQA to measure Western bias in question answering.

## Sources

**CVQA** (2 papers: [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf), [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf))
> The Cross-lingual Visual Question Answering (CVQA) dataset, used to assess a model's ability to reason about and understand culturally diverse visual content.

## Relationships

### → CVQA
- **Cultural understanding** (construct): *measured_by*, 2 papers
  > This benchmark can serve as a probing evaluation suite for assessing the cultural capability and bias of multimodal models and hopefully encourage more research efforts toward increasing cultural awareness and linguistic diversity in this field. (Abstract)
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf)
- **Cultural bias** (construct): *measured_by*, 2 papers
  > “To measure Western bias in question answering, we use A-OKVQA and CVQA (Schwenk et al., 2022; Romero et al., 2024).”
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > “We propose CVQA, a large-scale multilingual VQA benchmark”
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > “Each question was accompanied by one correct answer and three distractors that were reasonably plausible, yet incorrect, thus forming a multiple-choice format.”
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Open-ended question answering** (behavioral indicator): *measured_by*, 1 paper
  > “we made sure that CVQA is also convertible into free-text open-ended QA”
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multilingual understanding** (construct): *measured_by*, 1 paper
  > “CVQA is written in both English and local languages, enabling us to benchmark multilingual MLLMs and English-only MLLMs.”
  - [CVQA: Culturally-diverse Multilingual Visual Question Answering Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1568882ba1a50316e87852542523739c-Paper-Datasets_and_Benchmarks_Track.pdf)
