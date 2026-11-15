# GrailQA
**Type:** Measurement instrument  
**Supporting papers:** 7  

## State of the Field

**What it is.** Across the papers, the prevailing treatment of GrailQA is as a Freebase-based KBQA or KGQA benchmark and dataset for complex question answering, especially compositional and zero-shot reasoning. Definitions also frame it as a benchmark for evaluating KBQA generalizability and, in one formulation, semantic parsing systems; one description specifies 64,331 questions with target S-expressions and complex questions requiring up to 4-hop reasoning. A recurring description is that it tests three generalization settings: I.I.D., compositional, and zero-shot.

**What it is claimed to measure.** Papers link GrailQA to 4 constructs and 1 behavioral indicator. The reported uses are spread across several targets: papers use it to measure Knowledge graph question answering, and they also report it as evaluating Generalization, Multi-hop reasoning, Robustness, and Zero-shot generalization. This generalization framing is explicit in descriptions that use GrailQA to compare performance across I.I.D., compositional, and zero-shot levels, with one paper stating that validation and test questions are split into 50% unseen KB elements, 25% unseen compositions, and 25% I.I.D.

**Space of uses.** In practice, papers usually place GrailQA inside multi-dataset KGQA evaluations. It is most often used alongside CWQ and WebQSP, and some papers also pair it with WebQuestions and Simple Questions or SimpleQA, describing these collections as representative, standard, or widely used multi-hop KGQA benchmarks. One paper also reports performance under an attack setting on 1,000 randomly sampled GrailQA questions.

## Sources

**GrailQA** (3 papers: [TARGA: Targeted Synthetic Data Generation for Practical Reasoning over Structured Data](https://aclanthology.org/2025.acl-long.137.pdf), [Beyond Seen Data: Improving KBQA Generalization Through Schema-Guided Logical Form Generation](https://aclanthology.org/2025.emnlp-main.442.pdf), [Plan-on-Graph: Self-Correcting Adaptive Planning of Large Language Model on Knowledge Graphs](https://proceedings.neurips.cc/paper_files/paper/2024/file/4254e856d01a5e7b7ea050477c3ef9b9-Paper-Conference.pdf))
> Knowledge base question answering benchmark focusing on complex, compositional, and zero-shot reasoning over Freebase, used to evaluate semantic parsing systems.

## Relationships

### → GrailQA
- **Knowledge graph question answering** (behavioral indicator): *measured_by*, 3 papers
  > To demonstrate the effectiveness of PoG on complex reasoning over knowledge graphs, we adopt three representative multi-hop KGQA datasets: CWQ, WebQSP, and GrailQA. (Section 4.1.1)
  - [Plan-on-Graph: Self-Correcting Adaptive Planning of Large Language Model on Knowledge Graphs](https://proceedings.neurips.cc/paper_files/paper/2024/file/4254e856d01a5e7b7ea050477c3ef9b9-Paper-Conference.pdf)
  - [Digest the Knowledge: Large Language Models empowered Message Passing for Knowledge Graph Question Answering](https://aclanthology.org/2025.acl-long.750.pdf)
  - [SAFE: Schema-Driven Approximate Distance Join for Efficient Knowledge Graph Querying](https://aclanthology.org/2025.emnlp-main.883.pdf)
- **Generalization** (construct): *measured_by*, 2 papers
  > We experiment on GrailQA to compare the performance on different generalization levels (preliminary in Appendix D). (Section 4.3.3)
  - [TARGA: Targeted Synthetic Data Generation for Practical Reasoning over Structured Data](https://aclanthology.org/2025.acl-long.137.pdf)
  - [Beyond Seen Data: Improving KBQA Generalization Through Schema-Guided Logical Form Generation](https://aclanthology.org/2025.emnlp-main.442.pdf)
- **Multi-hop reasoning** (construct): *measured_by*, 2 papers
  > To evaluate the performance of our framework on multi-hop knowledge-intensive reasoning tasks, we conduct tests using four KBQA datasets: CWQ (Talmor & Berant, 2018), WebQSP (Yih et al., 2016), GrailQA (Gu et al., 2021), and SimpleQA (Bordes et al., 2015). (Section 5).
  - [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf)
  - [iQUEST: An Iterative Question-Guided Framework for Knowledge Base Question Answering](https://aclanthology.org/2025.acl-long.760.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > Figure 4: Performance under attack setting on 1,000 randomly sampled GrailQA questions. (Figure 4)
  - [TARGA: Targeted Synthetic Data Generation for Practical Reasoning over Structured Data](https://aclanthology.org/2025.acl-long.137.pdf)
- **Zero-shot generalization** (construct): *measured_by*, 1 paper
  > In the validation and the test sets, 50% of the questions include KB elements that are unseen in the training set (zero-shot generalization tests), 25% consist of unseen compositions of KB elements seen in the training set (compositional generalization tests), and the remaining 25% are randomly sampled from the training set (I.I.D. tests). (Section 5.1)
  - [Beyond Seen Data: Improving KBQA Generalization Through Schema-Guided Logical Form Generation](https://aclanthology.org/2025.emnlp-main.442.pdf)
