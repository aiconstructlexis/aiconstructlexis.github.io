# Text-to-SQL
**Type:** Behavioral indicator  
**Supporting papers:** 56  
**Also known as:** SQL generation, Text-to-SQL generation, SQL query generation, Text-to-SQL conversion, NL2SQL, Database query generation, Incremental SQL generation, Text-to-SQL parsing, SQL UPDATE generation, SQL trigger generation, Database querying  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as translating a natural language question, query, or prompt into a structured SQL statement or program, usually given a database or table schema and sometimes database content or auxiliary documentation. Most definitions stress that the output should be correct or executable against a database and retrieve the desired information, though some papers frame SQL generation as an intermediate step in broader table question answering or as database querying that can also manipulate data.

**Variants.** Papers use several nearby labels, most often SQL generation or text-to-SQL generation, with smaller pockets using NL2SQL, text-to-SQL parsing, and database query generation. Beyond standard single-turn retrieval, variants include multi-turn and dialogue settings with schema and context tracking, open-domain or large-table reasoning over retrieved tables, incremental generation via sub-syntax trees, dialect-specific SQL, and database-action forms such as SQL UPDATE and SQL TRIGGER generation. Several papers also study it in decomposed pipelines, claiming a causal relationship from Schema linking to Text-to-SQL, while another relates Text-to-SQL to Question decomposition through subquestion answering with SQL.

**Space of elicitation and scores.** It is measured by 7 instruments, mostly evaluation datasets and benchmarks. Spider is the prevailing instrument, frequently described as a standard or widely used text-to-SQL dataset, BIRD is the next recurring benchmark, AgentBench, CoSQL, and Spider-DK also appear, and 2 other instruments are linked.

**What it is taken as evidence of.** Rather than tying it to one repeated construct, papers connect it to 7 constructs with mixed relation types. Text-to-SQL is reported to be related to Generalization and Natural language understanding, papers claim causal relationships from In-context learning and Structural understanding to Text-to-SQL, and one paper claims a causal relationship from Text-to-SQL to Instruction understanding by warning that single-task SQL training can diminish it, and 2 other constructs are also linked.

## Sources

**SQL generation** (6 papers: [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf), [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf), [BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/094324f386c836c75d4a26f3499d2ede-Paper-Conference.pdf), [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf), [Track-SQL: Enhancing Generative Language Models with Dual-Extractive Modules for Schema and Context Tracking in Multi-turn Text-to-SQL](https://aclanthology.org/2025.naacl-long.536.pdf), [ALTER: Augmentation for Large-Table-Based Reasoning](https://aclanthology.org/2025.naacl-long.9.pdf))
> The observable behavior of an LLM producing a structured query language (SQL) program in response to a natural language query and a table schema.

**Text-to-SQL generation** (1 paper: [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf))
> The task of converting a natural language question into a structured SQL query that can be executed against a database.

**SQL query generation** (1 paper: [EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/file/a291dad965af9bc2e39ffeb2ca1c6dc0-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of creating a structured query language (SQL) query based on information extracted from natural language text to retrieve data from a database.

**Text-to-SQL conversion** (1 paper: [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of generating correct SQL code from a user's natural language query about a database.

**NL2SQL** (1 paper: [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf))
> The task of translating a natural language question into a corresponding SQL query, given a specific database schema and content.

**Database query generation** (1 paper: [Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf))
> The task of generating correct database queries (e.g., SQL) to retrieve or manipulate data based on a natural language request.

**Incremental SQL generation** (1 paper: [Structure-Guided Large Language Models for Text-to-SQL Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25k/zhang25k.pdf))
> The process of generating a complex SQL query step-by-step, often by decomposing the problem into smaller sub-tasks or syntax components.

**Text-to-SQL parsing** (1 paper: [SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering](https://aclanthology.org/2025.emnlp-main.34.pdf))
> The task of converting a natural language question into a formal SQL query that can be executed against a relational database.

**Text-to-SQL** (1 paper: [SwiftKV: Fast Prefill-Optimized Inference with Knowledge-Preserving Model Transformation](https://aclanthology.org/2025.emnlp-main.1306.pdf))
> Generating SQL queries from natural language prompts.

**SQL UPDATE generation** (1 paper: [Castle: Causal Cascade Updates in Relational Databases with Large Language Models](https://aclanthology.org/2025.emnlp-main.1700.pdf))
> Producing SQL UPDATE statements from natural language instructions and schema information.

**SQL trigger generation** (1 paper: [Castle: Causal Cascade Updates in Relational Databases with Large Language Models](https://aclanthology.org/2025.emnlp-main.1700.pdf))
> The task of automatically creating SQL TRIGGER scripts that maintain data consistency for derived or aggregate metrics in response to data modification events.

**Database querying** (1 paper: [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf))
> The task of generating structured query language (SQL) statements to retrieve information from a database based on a natural language question.

## Relationships

### Text-to-SQL →
- **Spider** (measurement instrument): *measured_by*, 14 papers
  > SELF-DEBUGGING achieves the state-of-the-art performance on several code generation benchmarks, including Spider for text-to-SQL generation, TransCoder for C++-to-Python translation, and MBPP for text-to-Python generation.
  - [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf)
  - [Syntactic and Semantic Control of Large Language Models via Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf)
  - [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf)
  - [Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self-Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ffd05ca3cf3985f4572af015b4cfc1e-Paper-Conference.pdf)
  - [IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d3a9e085540c65dd3e5731361f9320e-Paper-Conference.pdf)
  - [You Only Read Once (YORO): Learning to Internalize Database Knowledge for Text-to-SQL](https://aclanthology.org/2025.naacl-long.94.pdf)
  - [Uncovering the Impact of Chain-of-Thought Reasoning for Direct Preference Optimization: Lessons from Text-to-SQL](https://aclanthology.org/2025.acl-long.1031.pdf)
  - [DCG-SQL: Enhancing In-Context Learning for Text-to-SQL with Deep Contextual Schema Link Graph](https://aclanthology.org/2025.acl-long.748.pdf)
  - [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf)
  - [An Efficient Private GPT Never Autoregressively Decodes](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25q/li25q.pdf)
  - [SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering](https://aclanthology.org/2025.emnlp-main.34.pdf)
  - [Skeletons Matter: Dynamic Data Augmentation for Text-to-Query](https://aclanthology.org/2025.emnlp-main.64.pdf)
- **BIRD** (measurement instrument): *measured_by*, 6 papers
  > For text-to-SQL tasks, the agent has to convert users’ natural language queries into SQL code to meet their data requirements. StreamBench integrates three prominent datasets: Spider [17], CoSQL [18], and BIRD [19]. (Section 3.2)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [From Few to Many: Self-Improving Many-Shot Reasoners Through Iterative Optimization and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f22dfaee68dd71f784a82a684b4404bb-Paper-Conference.pdf)
  - [You Only Read Once (YORO): Learning to Internalize Database Knowledge for Text-to-SQL](https://aclanthology.org/2025.naacl-long.94.pdf)
  - [MSc-SQL: Multi-Sample Critiquing Small Language Models For Text-To-SQL Translation](https://aclanthology.org/2025.naacl-long.107.pdf)
  - [Uncovering the Impact of Chain-of-Thought Reasoning for Direct Preference Optimization: Lessons from Text-to-SQL](https://aclanthology.org/2025.acl-long.1031.pdf)
  - [Skeletons Matter: Dynamic Data Augmentation for Text-to-Query](https://aclanthology.org/2025.emnlp-main.64.pdf)
- **CoSQL** (measurement instrument): *measured_by*, 1 paper
  > For text-to-SQL tasks, the agent has to convert users’ natural language queries into SQL code to meet their data requirements. StreamBench integrates three prominent datasets: Spider [17], CoSQL [18], and BIRD [19]. (Section 3.2)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AgentBench** (measurement instrument): *measured_by*, 1 paper
  > Empirical results from AgentBench indicate that applying CycleQD to LLAMA3-8B-INSTRUCT based models not only enables them to surpass traditional fine-tuning methods in coding, operating systems, and database tasks, but also achieves performance on par with GPT-3.5-TURBO (Section 1).
  - [Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf)
- **Spider-DK** (measurement instrument): *measured_by*, 1 paper
  > In this paper, we evaluate TNT on the task of NL2SQL. We adopt three prevalant datasets, SPIDER (Yu et al., 2018), SPIDER-DK (Gan et al., 2021a), and SPIDER-Realistic (Deng et al., 2021) (Section 6.1).
  - [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf)
- **Spider-Realistic** (measurement instrument): *measured_by*, 1 paper
  > In this paper, we evaluate TNT on the task of NL2SQL. We adopt three prevalant datasets, SPIDER (Yu et al., 2018), SPIDER-DK (Gan et al., 2021a), and SPIDER-Realistic (Deng et al., 2021) (Section 6.1).
  - [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf)
- **Instruction understanding** (construct): *causes*, 1 paper
  > Additionally, training LLMs on a single SQL generation task poses a substantial risk of diminishing performance in understanding instructions... (Section 1)
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
- **WikiSQL** (measurement instrument): *measured_by*, 1 paper
  > "early benchmarks such as WikiSQL (Yavuz et al., 2018) and Spider (Yu et al., 2018) focus on Text-to-SQL parsing over one or more relational tables"
  - [SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering](https://aclanthology.org/2025.emnlp-main.34.pdf)

### → Text-to-SQL
- **Schema linking** (behavioral indicator): *causes*, 3 papers
  > ideal schema linking can effectively achieve accurate SQL generation, which shows that schema linking is still an effective means to solve Text2SQL at this stage and in the future. (Section 4.3)
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
  - [MSc-SQL: Multi-Sample Critiquing Small Language Models For Text-To-SQL Translation](https://aclanthology.org/2025.naacl-long.107.pdf)
  - [LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Text-to-SQL](https://aclanthology.org/2025.emnlp-main.51.pdf)
- **In-context learning** (construct): *causes*, 1 paper
  > With the demonstrations, our method fully leverages in-context learning capability and generate the target SQL correctly. (Section 3)
  - [DCG-SQL: Enhancing In-Context Learning for Text-to-SQL with Deep Contextual Schema Link Graph](https://aclanthology.org/2025.acl-long.748.pdf)
- **Structural understanding** (construct): *causes*, 1 paper
  > “This limitation makes it difficult for the model to handle the complex mapping between natural language queries and diverse database schemas, impeding its ability to accurately interpret schema relationships, construct complex SQL queries”
  - [Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dt/li25dt.pdf)

### Associated with
- **Generalization** (construct), 1 paper
  > In the zero-shot setting, the key challenge is to construct a mapping function f without task-specific labeled data. This requires the model to generalize across unseen SQL queries and databases, relying solely on pre-trained knowledge and the provided database schema. (Section 3.1)
  - [Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dt/li25dt.pdf)
- **Natural language understanding** (construct), 1 paper
  > Text-to-SQL generation provides an ideal middle ground, as SQL’s formal structure makes it more tractable than general language generation while still requiring natural language understanding. (Section 1)
  - [TinySQL: A Progressive Text-to-SQL Dataset for Mechanistic Interpretability Research](https://aclanthology.org/2025.emnlp-main.1489.pdf)
- **Table reasoning** (construct), 1 paper
  > To investigate this, we focus on NL2SQL, a pivotal task in table understanding where LLMs translate natural language queries into SQL, given a specific database (Section 1).
  - [Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf)
- **Question decomposition** (behavioral indicator), 1 paper
  > The Query Agent QAgent generates a SQL query qij and resulting tables Rij (qij(D) = Rij) to answer the subquestions using the database information and schema (Section 4.2)
  - [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf)
- **Syntactic correctness** (construct), 1 paper
  > This ensures that the generated queries maintain both semantic accuracy (correctly capturing user intentions) and syntactic correctness (following proper SQL structure). (Section 1. Introduction)
  - [Structure-Guided Large Language Models for Text-to-SQL Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25k/zhang25k.pdf)
