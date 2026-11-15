# SCROLLS
**Type:** Measurement instrument  
**Supporting papers:** 7  
**Also known as:** SCROLL, Scrolls, (Zero)SCROLLS  

## State of the Field

**What it is.** Most commonly, papers treat SCROLLS as a benchmark suite for long-text or long-context evaluation, often explicitly as a suite of 7 datasets. Its task mix is described as question answering and summarization, with some descriptions adding classification, and one definition frames SCROLL as evaluating language models' ability to reason over and synthesize information from long texts. A smaller framing discusses Scrolls together with ZeroSCROLLS as realistic long-input tasks from real-world scenarios, and one quoted passage reports average lengths ranging from 1.7k to 49.3k tokens.

**What it is claimed to measure.** Papers use SCROLLS to measure 2 constructs and no behavioral indicators, most often Long-context understanding and Long-context reasoning. These claims are concentrated on long-context capabilities rather than spread across many concepts: one line of work places Scrolls within long-context modeling and QA evaluation, while another describes it as evaluating models' ability to synthesize information over long texts.

**Space of uses.** Across papers, SCROLLS is used as a finetuning and comparison benchmark for long-sequence tasks, including baseline comparisons and long-document decoding tests. It is also related to 3 other instruments, NarrativeQA, QMSum, and Qasper, which papers describe as included in Scrolls open-book QA evaluations. Another usage extracts components from it for a within-32K long-dataset benchmark, noting that QMSum, Qasper, and QuALITY are taken from SCROLLS.

**Concerns raised.** A limited caveat appears in one benchmark setup: NarrativeQA is excluded because it is included in training.

## Sources

**SCROLLS** (2 papers: [Functional Interpolation for Relative Positions improves Long Context Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f55a8b7b1c2c6312eb86557bb9a2bd5-Paper-Conference.pdf), [Accelerating LLM Inference with Lossless Speculative Decoding Algorithms for Heterogeneous Vocabularies](https://raw.githubusercontent.com/mlresearch/v267/main/assets/timor25a/timor25a.pdf))
> Standardized Compendium of Re-evaluated Long Language-modeling Sets (SCROLLS) is a benchmark suite of seven datasets for evaluating models on long-text tasks such as question answering and summarization.

**SCROLL** (1 paper: [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf))
> A benchmark suite for evaluating the ability of language models to reason over and synthesize information from long texts.

**Scrolls** (1 paper: [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark for standardized comparison over long language sequences, consisting of tasks like QA, classification, and summarization.

**(Zero)SCROLLS** (1 paper: [Stress-Testing Long-Context Language Models with Lifelong ICL and Task Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc8db5884a7474b4771762b6f0c8ee1-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark consisting of realistic tasks that require processing long inputs from real-world scenarios, such as summarization and question answering.

## Relationships

### → SCROLLS
- **Long-context understanding** (construct): *measured_by*, 2 papers
  > Evaluation on long-context modeling, including perplexity in various context lengths up to 2M and long-context QA tasks in Scrolls (Parisotto et al., 2020) prove MEGALODON’s ability to model sequences of unlimited length. (Section 1).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
- **Long-context reasoning** (construct): *measured_by*, 1 paper
  > To evaluate the ability of long context reasoning, we compare ICLM with the standard and kNN baselines on the SCROLL benchmark (Shaham et al., 2022) that evaluates LMs’ ability to synthesize information over long texts. (Section 3.3.6)
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)

### Associated with
- **NarrativeQA** (measurement instrument), 1 paper
  > ...we evaluate MEGALODON on long-context open-book question answering (QA) tasks in the Scrolls dataset (Shaham et al., 2022), including NarrativeQA (Koˇcisk´y et al., 2018)... (Section 4.3).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **Qasper** (measurement instrument), 1 paper
  > ...we evaluate MEGALODON on long-context open-book question answering (QA) tasks in the Scrolls dataset (Shaham et al., 2022), including NarrativeQA (Koˇcisk´y et al., 2018), Qasper (Dasigi et al., 2021)... (Section 4.3).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **QMSum** (measurement instrument), 1 paper
  > ...we evaluate MEGALODON on long-context open-book question answering (QA) tasks in the Scrolls dataset (Shaham et al., 2022), including NarrativeQA (Koˇcisk´y et al., 2018), Qasper (Dasigi et al., 2021) and QMSum (Zhong et al., 2021). (Section 4.3).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
