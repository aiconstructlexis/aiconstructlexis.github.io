# Data analysis
**Type:** Behavioral indicator  
**Supporting papers:** 9  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats data analysis as processing data through statistical and logical reasoning to understand the data and answer questions or derive insights. Several descriptions emphasize application-driven queries and answers containing findings and suggestions based on a database, while some operationalizations cast it as inspecting, transforming, and modeling data, sometimes in multiple-choice or fill-in-the-blank formats. A smaller framing presents it as a latent ability for tabular work, including manipulating tables, inferring schema information, and carrying out practical data-wrangling tasks.

**Variants.** Papers study it in several settings, most often as answering questions over tables or CSV files, and sometimes as one of several data science scenarios within automation systems. The variants named in the papers include financial data analysis questions, practical tabular tasks such as table reformatting, predicting which columns can be used to join two tables, and predicting the correct column type annotation. Related links also connect data analysis to question decomposition, data transformation, and schema matching, and one paper claims a causal relationship from code generation to data analysis.

**Space of elicitation and scores.** Papers measure it with 4 instruments: InfiAgent-DABench, LiveBench, TableEval, and WildBench. The common pattern is an instrument that includes data analysis as a named task category or question collection, while InfiAgent-DABench is described through CSV-based analysis questions and the broader instruments place data analysis alongside other task types.

**What it is taken as evidence of.** The construct links do not single out one underlying construct over the others. Instead, papers relate data analysis to 3 constructs, logical reasoning, mathematical reasoning, and strategic reasoning. One paper says that data analysis requires diverse reasoning skills including these three, and these links are stated as related rather than as explicit indicator claims.

## Sources

**Data analysis** (3 papers: [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf), [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50e9ad960ae78b741a6b4fea533f2eaf-Paper-Conference.pdf), [DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation](https://aclanthology.org/2025.emnlp-main.58.pdf))
> The process of systematically applying statistical and logical reasoning to comprehend data and derive insights from a database.

## Relationships

### Data analysis →
- **WildBench** (measurement instrument): *measured_by*, 1 paper
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **LiveBench** (measurement instrument): *measured_by*, 1 paper
  > LiveBench (White et al., 2024) contains 6 problem categories: data analysis, language, reasoning, math, instruction following, and coding. (Section 4.2)
  - [Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation](https://aclanthology.org/2025.naacl-long.404.pdf)
- **InfiAgent-DABench** (measurement instrument): *measured_by*, 1 paper
  > (1) Data Analysis: InfiAgent-DABench (Hu et al., 2024b) contains 257 challenges with CSV inputs and multi-level (easy/medium/hard) analysis questions. (Section 4.1)
  - [DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation](https://aclanthology.org/2025.emnlp-main.58.pdf)
- **TableEval** (measurement instrument): *measured_by*, 1 paper
  > This approach accommodates various task types within diverse real-world industrial scenarios, including information retrieval, numerical analysis, table reasoning, data analysis, multi-turn dialogue, and understanding of table structures. (Section 3.1)
  - [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf)

### → Data analysis
- **Code generation** (behavioral indicator): *causes*, 1 paper
  > we use large language models (LLMs) enhanced by code generation to automatically generate high-quality data analysis, which will later be refined by human annotators. (Abstract)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Mathematical reasoning** (construct), 1 paper
  > the need for data analysis typically arises from specific application scenarios, and requires diverse reasoning skills including mathematical reasoning, logical reasoning, and strategic reasoning. (Abstract)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Logical reasoning** (construct), 1 paper
  > the need for data analysis typically arises from specific application scenarios, and requires diverse reasoning skills including mathematical reasoning, logical reasoning, and strategic reasoning. (Abstract)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Strategic reasoning** (construct), 1 paper
  > the need for data analysis typically arises from specific application scenarios, and requires diverse reasoning skills including mathematical reasoning, logical reasoning, and strategic reasoning. (Abstract)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Question decomposition** (behavioral indicator), 1 paper
  > most existing table QA datasets focus on obtaining specific information, our data analysis queries can be complex and requires query decomposition and reasoning. (Section 6)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Column type annotation** (behavioral indicator), 1 paper
  > “Data Analysis: three tasks using recent datasets from Kaggle and Socrata, specifically, ... and predicting the correct column type annotation”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Schema matching** (behavioral indicator), 1 paper
  > “Data Analysis: three tasks using recent datasets from Kaggle and Socrata, specifically, ... predicting which columns can be used to join two tables”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
- **Data transformation** (behavioral indicator), 1 paper
  > “Data Analysis: three tasks using recent datasets from Kaggle and Socrata, specifically, table reformatting ...”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
