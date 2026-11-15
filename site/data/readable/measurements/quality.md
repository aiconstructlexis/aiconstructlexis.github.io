# QuALITY
**Type:** Measurement instrument  
**Supporting papers:** 16  
**Also known as:** Quality  

## State of the Field

**What it is.** Most papers describe QuALITY as a long-document or long-context question answering benchmark built from stories, articles, or other long passages, usually in a multiple-choice format. Definitions commonly emphasize long inputs, with one description saying passages average about 5,000 tokens and another describing English context passages between 2K and 8K tokens. A smaller line of work recasts the benchmark for different answer formats, including direct answer generation without the four options and a binary-choice extractive reading-comprehension form.

**What it is claimed to measure.** Across papers, QuALITY is linked to 1 construct and 3 behavioral indicators. The prevailing measurement claim is question answering, with papers describing it as a QA dataset over stories and articles; smaller lines of work use it to measure multiple-choice question answering and machine reading comprehension. Papers also report it as evaluating long-context understanding, especially when they frame it as a longer-sequence or long-context ability benchmark.

**Space of uses.** Papers usually use QuALITY as one benchmark inside broader question-answering or long-context evaluation suites, often alongside NarrativeQA and QASPER, and in one case alongside TriviaQA. The common setup keeps it as a multiple-choice task where the model selects among choices, and one paper notes using default validation splits and prompts from prior work for QuALITY.

## Sources

**QuALITY** (7 papers: [From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf), [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf), [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf), [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf), [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf), [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf), [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf))
> A single-document question answering benchmark with long passages and multiple-choice questions, here used in a direct-answer setting to assess document-level reasoning.

**Quality** (1 paper: [E2LLM: Encoder Elongated Large Language Models for Long-Context Understanding and Reasoning](https://aclanthology.org/2025.emnlp-main.970.pdf))
> A dataset used to evaluate performance on the long-context task of question answering.

## Relationships

### → QuALITY
- **Question answering** (behavioral indicator): *measured_by*, 5 papers
  > QuALITY (QLTY) (Pang et al., 2022) is a question answering dataset over stories and articles collected from several resources, such as Project Gutenberg and the Open American National Corpus4.
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
  - [Language Models Learn to Mislead Humans via RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a5a60573637f329b04d1beda4cd404-Paper-Conference.pdf)
  - [Graph Neural Network Enhanced Retrieval for Question Answering of Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
- **Long-context understanding** (construct): *measured_by*, 2 papers
  > Long-context ability evaluation. Following Xiong et al. [94], we evaluated the models on long-sequence tasks, including ... QuALITY [58]... (Table 4, Section 4.2)
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 2 papers
  > Closed-ended tasks primarily focus on the capacity for understanding and reasoning within long contexts, including tasks like multiple-choice questions from QuALITY [5]... (Section 4.2).
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
  - [Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models](https://aclanthology.org/2025.emnlp-main.1656.pdf)
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 1 paper
  > The QuALITY dataset is a reading comprehension task consisting of documents (about 5k tokens long) with a set of multiple choice reading comprehension questions. (Appendix F.1)
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
