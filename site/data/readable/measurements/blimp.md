# BLiMP
**Type:** Measurement instrument  
**Supporting papers:** 22  

## State of the Field

**What it is.** Across papers, BLiMP is most commonly treated as an English benchmark or corpus of linguistic minimal pairs for grammaticality or acceptability judgments. It is usually described as minimally different pairs of acceptable and unacceptable, or grammatical and ungrammatical, sentences, with evaluation based on identifying the grammatical item or assigning it lower perplexity; several definitions present it as a multi-task benchmark spanning syntax, morphology, and semantics. Most descriptions specify 67 subtasks, datasets, or paradigms with 1,000 pairs each, often grouped into 12 categories or phenomena and sometimes summarized as 67,000 pairs, and some add that the examples are template-generated or built from manually crafted sentence templates, though one paper describes 13 linguistic phenomena. A smaller usage selects an 11-dataset subset that can be used for text generation.

**What it is claimed to measure.** Papers link BLiMP to 5 constructs and no behavioral indicators. The prevailing claim is that it measures syntactic competence, with papers using it for syntactic generalization, grammatical learning, and grammatical competence; some papers also report it as measuring formal linguistic competence. Smaller lines of work use it to measure language proficiency, linguistic knowledge, or plausibility, including plausibility defined as whether model attributions align with human-understood linguistic rationales.

**Space of uses.** BLiMP is often used alongside SyntaxGym, and some papers pair it with CLiMP, GLUE, Brain-Score, or Ewok. In these settings it is typically positioned as a benchmark for linguistic competence or grammaticality within a broader evaluation suite, sometimes as an external targeted evaluation, and one paper states that it 'has become the standard benchmark for English'. Other reported uses include zero-shot evaluation, assessing syntactic agreement, and selecting an 11-dataset subset for generation-based explanation faithfulness.

## Sources

**BLiMP** (18 papers: [Sudden Drops in the Loss: Syntax Acquisition, Phase Transitions, and Simplicity Bias in MLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e8df255a03b383f30abe09203770213-Paper-Conference.pdf), [Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf), [What does the Knowledge Neuron Thesis Have to do with Knowledge?](https://proceedings.iclr.cc/paper_files/paper/2024/file/013d743db3c684957305d32017f13339-Paper-Conference.pdf), [TopoLM: brain-like spatio-functional organization in a topographic language model](https://proceedings.iclr.cc/paper_files/paper/2025/file/4f7f521c08b5e0cd9931e74fa353b59b-Paper-Conference.pdf), [Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.407.pdf), [The LLM Language Network: A Neuroscientific Approach for Identifying Causally Task-Relevant Units](https://aclanthology.org/2025.naacl-long.544.pdf), [How to Make the Most of LLMs' Grammatical Knowledge for Acceptability Judgments](https://aclanthology.org/2025.naacl-long.380.pdf), [Between Circuits and Chomsky: Pre-pretraining on Formal Languages Imparts Linguistic Biases](https://aclanthology.org/2025.acl-long.478.pdf), [Child-Directed Language Does Not Consistently Boost Syntax Learning in Language Models](https://aclanthology.org/2025.emnlp-main.999.pdf), [Convergence and Divergence of Language Models under Different Random Seeds](https://aclanthology.org/2025.emnlp-main.1675.pdf), [From Language to Cognition: How LLMs Outgrow the Human Language Network](https://aclanthology.org/2025.emnlp-main.1237.pdf), [Layer-wise Minimal Pair Probing Reveals Contextual Grammatical-Conceptual Hierarchy in Speech Representations](https://aclanthology.org/2025.emnlp-main.1790.pdf), [Mechanisms vs. Outcomes: Probing for Syntax Fails to Explain Performance on Targeted Syntactic Evaluations](https://aclanthology.org/2025.emnlp-main.1712.pdf), [NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1769.pdf), [QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.6.pdf), [SLlama: Parameter-Efficient Language Model Architecture for Enhanced Linguistic Competence Under Strict Data Constraints](https://aclanthology.org/2025.emnlp-main.1198.pdf), [Sheaf Discovery with Joint Computation Graph Pruning and Flexible Granularity](https://aclanthology.org/2025.emnlp-main.446.pdf), [TurBLiMP: A Turkish Benchmark of Linguistic Minimal Pairs](https://aclanthology.org/2025.emnlp-main.834.pdf))
> Benchmark of Linguistic Minimal Pairs, a corpus of minimal-pair sentence judgments used here to evaluate syntactic phenomena such as agreement.

## Relationships

### → BLiMP
- **Syntactic competence** (construct): *measured_by*, 4 papers
  > We use the BLiMP (Warstadt et al., 2020) and SyntaxGym (SG, Gauthier et al., 2020) test suites to evaluate LMs for syntactic generalization.
  - [Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.407.pdf)
  - [Child-Directed Language Does Not Consistently Boost Syntax Learning in Language Models](https://aclanthology.org/2025.emnlp-main.999.pdf)
  - [Layer-wise Minimal Pair Probing Reveals Contextual Grammatical-Conceptual Hierarchy in Speech Representations](https://aclanthology.org/2025.emnlp-main.1790.pdf)
  - [Mechanisms vs. Outcomes: Probing for Syntax Fails to Explain Performance on Targeted Syntactic Evaluations](https://aclanthology.org/2025.emnlp-main.1712.pdf)
- **Formal linguistic competence** (construct): *measured_by*, 2 papers
  > To assess formal linguistic competence, we use two benchmarks: BLIMP (Warstadt et al., 2019) and SYNTAXGYM (Gauthier et al., 2020). (Section 3.3)
  - [From Language to Cognition: How LLMs Outgrow the Human Language Network](https://aclanthology.org/2025.emnlp-main.1237.pdf)
  - [The LLM Language Network: A Neuroscientific Approach for Identifying Causally Task-Relevant Units](https://aclanthology.org/2025.naacl-long.544.pdf)
- **Language proficiency** (construct): *measured_by*, 1 paper
  > BLiMP provides a fine-grained evaluation of core linguistic competence. (Section 2)
  - [SLlama: Parameter-Efficient Language Model Architecture for Enhanced Linguistic Competence Under Strict Data Constraints](https://aclanthology.org/2025.emnlp-main.1198.pdf)
- **Linguistic knowledge** (construct): *measured_by*, 1 paper
  > we evaluate TopoLM’s performance on linguistic knowledge (BLiMP), downstream task (GLUE), and brain alignment benchmarks (Brain-Score)
  - [TopoLM: brain-like spatio-functional organization in a topographic language model](https://proceedings.iclr.cc/paper_files/paper/2025/file/4f7f521c08b5e0cd9931e74fa353b59b-Paper-Conference.pdf)
- **Plausibility** (construct): *measured_by*, 1 paper
  > ...to examine its plausibility, i.e., the extent to which its attributions align with human-understood linguistic rationales provided by BLiMP... (Section 5)
  - [NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1769.pdf)
