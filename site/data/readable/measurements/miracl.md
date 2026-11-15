# MIRACL
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Across the cited definitions, papers describe MIRACL as the Multilingual Information Retrieval Across a Continuum of Languages dataset for multilingual retrieval evaluation across 18 languages. The prevailing description emphasizes native questions and relevance judgements of retrieved passages, while another formulation states more generally that it is used to evaluate retrieval systems across 18 diverse languages.

**What it is claimed to measure.** Papers link MIRACL to one construct and one behavioral indicator. These claims are concentrated rather than spread across many targets: papers use it to measure multilingual ability, with one study saying it helps assess multilingual retrieval capability, and one paper reports it as measuring information retrieval by describing it as a multilingual and cross-lingual IR resource.

**Space of uses.** In use, papers present MIRACL as a retrieval evaluation dataset and, in one case, as the basis for a broader benchmark. One study pairs it with BEIR for main evaluations of dense retrievers and multilingual retrieval capability, while another builds a benchmark on top of MIRACL using native-language questions and generating responses with diverse large language models; no other measurement instrument is explicitly linked to it.

## Sources

**MIRACL** (2 papers: [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf), [MEMERAG: A Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1101.pdf))
> The Multilingual Information Retrieval Across a Continuum of Languages dataset, used for evaluating retrieval systems across 18 diverse languages.

## Relationships

### → MIRACL
- **Multilingual ability** (construct): *measured_by*, 1 paper
  > Our main evaluations are conducted on BEIR (Thakur et al., 2021) and MIRACL (Zhang et al., 2023), to assess the generalization of dense retrievers and multilingual retrieval capability. (Section 4.5).
  - [DRAMA: Diverse Augmentation from Large Language Models to Smaller Dense Retrievers](https://aclanthology.org/2025.acl-long.1457.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > Recent efforts include the development of multilingual and cross-lingual IR resources, such as Mr. TyDi (Zhang et al., 2021), MIRACL (Zhang et al., 2023) and CIRAL (Adeyemi et al., 2024)... (Section 4.3)
  - [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf)
