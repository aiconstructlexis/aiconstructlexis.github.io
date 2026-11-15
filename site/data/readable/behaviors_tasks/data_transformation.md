# Data transformation
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Data wrangling, Table reformatting  

## State of the Field

**Space of definitions.** Most definitions describe it as converting data from one format or structure to another, often to restructure or enhance the data. In task form, one benchmark asks for a table in one format to be reformatted into a specified target format. A smaller line of work describes the behavior as generating executable code to transform tabular data from natural language instructions or input-output examples, while a related framing uses the nearby label data wrangling for database operations that clean, organize, or reshape data for later analysis.

**Variants.** Papers study it under several names, most commonly data transformation, with smaller variants including data wrangling, table reformatting, and data transformation by-example. The settings are mainly tabular or database-centered: examples include project-level transformation workflows built on DBT, reformatting tables from JSON or CSV into Markdown or HTML, and generating SQL, R, or Pandas code from input-output examples.

**Space of elicitation and scores.** No measurement instrument is linked to it. The recorded links instead connect it to two behavioral indicators, Code generation and Data analysis, both as related links rather than measurement links.

**What it is taken as evidence of.** No construct is linked to it. Instead, the only recorded connections are related links: one paper relates Code generation to Data transformation, describing it as "a general paradigm for structured reasoning and data transformation tasks," and another relates Data analysis to Data transformation through table reformatting.

## Sources

**Data wrangling** (1 paper: [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://proceedings.iclr.cc/paper_files/paper/2025/file/46c10f6c8ea5aa6f267bcdabcb123f97-Paper-Conference.pdf))
> Performing database operations that clean, organize, or reshape data for later analysis.

**Data transformation** (2 papers: [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://proceedings.iclr.cc/paper_files/paper/2025/file/46c10f6c8ea5aa6f267bcdabcb123f97-Paper-Conference.pdf), [Table-LLM-Specialist: Language Model Specialists for Tables using Iterative Fine-tuning](https://aclanthology.org/2025.emnlp-main.1795.pdf))
> The observable task of converting data from one format or structure to another, often involving restructuring or enhancing the data.

**Table reformatting** (1 paper: [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf))
> The task of converting a table from a source format (e.g., JSON, CSV) to a specified target format (e.g., Markdown, HTML).

## Relationships

### Associated with
- **Code generation** (behavioral indicator), 1 paper
  > Beyond grid puzzles, PBE is a general paradigm for structured reasoning and data transformation tasks
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
- **Data analysis** (behavioral indicator), 1 paper
  > “Data Analysis: three tasks using recent datasets from Kaggle and Socrata, specifically, table reformatting ...”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)
