# BIRD
**Type:** Measurement instrument  
**Supporting papers:** 25  
**Also known as:** BIRD-Bench  

## State of the Field

**What it is.** Across definitions, BIRD is most commonly described as a large-scale, cross-domain, database-grounded benchmark for Text-to-SQL, sometimes written as BIRD-Bench. Papers repeatedly describe it as built from real-world databases and as more challenging than Spider or previous datasets, citing complex databases or schemas, difficult questions, external knowledge, dirty values, varied cell formats, challenging value mappings, and value-based reasoning. The descriptions vary in detail: some give train, development, and test split sizes, some focus on the dev set and a 20240627 BIRD-dev version, and others describe it as containing over 12,751 question-SQL pairs across 95 databases spanning 37 domains.

**What it is claimed to measure.** Papers link BIRD to 2 behavioral indicators and 2 constructs. The prevailing usage is to measure Text-to-SQL: several papers evaluate Text-to-SQL tasks or generation on BIRD, including settings where models generate SQL or SQLite programs from natural language instructions over real-world databases. A smaller line of work uses it to measure schema linking, and individual papers report it as measuring cross-domain generalization and table reasoning.

**Space of uses.** In practice, papers most often use BIRD alongside Spider, and more occasionally alongside CoSQL, KaggleDBQA, AmbiDB, and Text2Cypher. They typically position it as a standard or widely used benchmark, sometimes as a more challenging or more realistic comparison point, and some papers adapt methods to it, sample evaluation data from it, or evaluate specifically on the BIRD-dev set.

## Sources

**BIRD** (8 papers: [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf), [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf), [You Only Read Once (YORO): Learning to Internalize Database Knowledge for Text-to-SQL](https://aclanthology.org/2025.naacl-long.94.pdf), [PRACTIQ: A Practical Conversational Text-to-SQL dataset with Ambiguous and Unanswerable Queries](https://aclanthology.org/2025.naacl-long.13.pdf), [FLEX: Expert-level False-Less EXecution Metric for Text-to-SQL Benchmark](https://aclanthology.org/2025.naacl-long.228.pdf), [MSc-SQL: Multi-Sample Critiquing Small Language Models For Text-To-SQL Translation](https://aclanthology.org/2025.naacl-long.107.pdf), [SHARE: An SLM-based Hierarchical Action CorREction Assistant for Text-to-SQL](https://aclanthology.org/2025.acl-long.552.pdf), [Skeletons Matter: Dynamic Data Augmentation for Text-to-Query](https://aclanthology.org/2025.emnlp-main.64.pdf))
> A large-scale, cross-domain Text-to-SQL benchmark designed to be more challenging than previous datasets, featuring complex databases, difficult questions, and reliance on external knowledge.

**BIRD-Bench** (1 paper: [AMBROSIA: A Benchmark for Parsing Ambiguous Questions into Database Queries](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4c942a8405cc910f0a833d28d2573cc-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark for large-scale database grounded text-to-SQL tasks.

## Relationships

### → BIRD
- **Text-to-SQL** (behavioral indicator): *measured_by*, 6 papers
  > For text-to-SQL tasks, the agent has to convert users’ natural language queries into SQL code to meet their data requirements. StreamBench integrates three prominent datasets: Spider [17], CoSQL [18], and BIRD [19]. (Section 3.2)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [From Few to Many: Self-Improving Many-Shot Reasoners Through Iterative Optimization and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f22dfaee68dd71f784a82a684b4404bb-Paper-Conference.pdf)
  - [You Only Read Once (YORO): Learning to Internalize Database Knowledge for Text-to-SQL](https://aclanthology.org/2025.naacl-long.94.pdf)
  - [MSc-SQL: Multi-Sample Critiquing Small Language Models For Text-To-SQL Translation](https://aclanthology.org/2025.naacl-long.107.pdf)
  - [Uncovering the Impact of Chain-of-Thought Reasoning for Direct Preference Optimization: Lessons from Text-to-SQL](https://aclanthology.org/2025.acl-long.1031.pdf)
  - [Skeletons Matter: Dynamic Data Augmentation for Text-to-Query](https://aclanthology.org/2025.emnlp-main.64.pdf)
- **Schema linking** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate our method performance of schema linking on the SPIDER, BIRD and AmbiDB datasets
  - [LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Text-to-SQL](https://aclanthology.org/2025.emnlp-main.51.pdf)
- **Cross-domain generalization** (construct): *measured_by*, 1 paper
  > Benchmarks like Spider(Yu et al., 2019) and BIRD(Li et al., 2023b) evaluate cross-domain generalization, where training and test databases are disjoint. (Section 1)
  - [GenLink: Generation-Driven Schema-Linking via Multi-Model Learning for Text-to-SQL](https://aclanthology.org/2025.emnlp-main.1518.pdf)
- **Table reasoning** (construct): *measured_by*, 1 paper
  > To verify the scalability of TableRAG for larger tables, we build two new benchmarks sourced from the real-world Arcade [26] and BIRD-SQL [7] datasets.
  - [TableRAG: Million-Token Table Understanding with Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/88dd7aa6979e352fda7c4952ca8eac59-Paper-Conference.pdf)
