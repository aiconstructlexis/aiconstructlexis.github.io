# Spider
**Type:** Measurement instrument  
**Supporting papers:** 35  
**Also known as:** SPIDER  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats Spider as a large-scale, complex, cross-domain text-to-SQL benchmark or dataset. Papers commonly describe it as natural-language questions paired with SQL queries over multiple databases or database schemas, sometimes emphasizing executable SQL and syntactic and semantic correctness. A smaller line of work describes it as a benchmark for text-to-SQL semantic parsers or parsing over one or more relational tables, and some papers also refer to train, development, and test splits and a range of difficulty levels.

**What it is claimed to measure.** Papers overwhelmingly use Spider to measure Text-to-SQL, including generating SQL queries from natural-language questions and schemas. Beyond that dominant use, papers link it to two behavioral indicators, Text-to-SQL and Schema linking, and to two constructs, Cross-domain generalization and General ability. The claims are concentrated on Text-to-SQL, while a single paper each reports Spider as measuring schema linking, evaluating cross-domain generalization, or testing general downstream performance.

**Space of uses.** Papers usually position Spider as a standard or prominent benchmark in text-to-SQL evaluation. They often use it alongside other text-to-SQL datasets such as BIRD, KaggleDBQA, and CoSQL, and some papers pair it with Spider-DK, Spider-Realistic, or Spider-Syn. Some evaluations focus on the development split, and one paper explicitly notes that its problem descriptions do not include unit tests.

## Sources

**Spider** (11 papers: [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf), [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf), [IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d3a9e085540c65dd3e5731361f9320e-Paper-Conference.pdf), [You Only Read Once (YORO): Learning to Internalize Database Knowledge for Text-to-SQL](https://aclanthology.org/2025.naacl-long.94.pdf), [PRACTIQ: A Practical Conversational Text-to-SQL dataset with Ambiguous and Unanswerable Queries](https://aclanthology.org/2025.naacl-long.13.pdf), [FLEX: Expert-level False-Less EXecution Metric for Text-to-SQL Benchmark](https://aclanthology.org/2025.naacl-long.228.pdf), [DCG-SQL: Enhancing In-Context Learning for Text-to-SQL with Deep Contextual Schema Link Graph](https://aclanthology.org/2025.acl-long.748.pdf), [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf), [SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering](https://aclanthology.org/2025.emnlp-main.34.pdf), [AMBROSIA: A Benchmark for Parsing Ambiguous Questions into Database Queries](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4c942a8405cc910f0a833d28d2573cc-Paper-Datasets_and_Benchmarks_Track.pdf), [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf))
> Text-to-SQL benchmark evaluating the ability to generate syntactically and semantically correct SQL queries from natural language questions over complex databases, used here without unit tests.

**SPIDER** (1 paper: [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf))
> A widely-used, large-scale, cross-domain benchmark dataset for evaluating Text-to-SQL models, consisting of natural language questions paired with SQL queries across multiple databases.

## Relationships

### → Spider
- **Text-to-SQL** (behavioral indicator): *measured_by*, 14 papers
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
- **General ability** (construct): *measured_by*, 1 paper
  > To validate that MTJD indeed betters output quality, we test MTJD (k=4) and standard multinomial sampling on Spider, MTBench, and HumanEval using the Llama-3 series models. ... For this process, the higher the scores, the better the downstream performance. (Section 5.1)
  - [Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf)
- **Schema linking** (behavioral indicator): *measured_by*, 1 paper
  > We evaluate our method performance of schema linking on the SPIDER, BIRD and AmbiDB datasets
  - [LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Text-to-SQL](https://aclanthology.org/2025.emnlp-main.51.pdf)
- **Cross-domain generalization** (construct): *measured_by*, 1 paper
  > Benchmarks like Spider(Yu et al., 2019) and BIRD(Li et al., 2023b) evaluate cross-domain generalization, where training and test databases are disjoint. (Section 1)
  - [GenLink: Generation-Driven Schema-Linking via Multi-Model Learning for Text-to-SQL](https://aclanthology.org/2025.emnlp-main.1518.pdf)
