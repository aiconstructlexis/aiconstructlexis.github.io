# OpenCompass
**Type:** Measurement instrument  
**Supporting papers:** 24  
**Also known as:** Opencompass  

## State of the Field

**What it is.** Most papers describe OpenCompass as an open-source evaluation framework or toolkit for standardized assessment of large language models across multiple benchmarks. Some narrow that description to a suite for several widely used zero-shot benchmarks, while another paper presents it as a platform that includes datasets such as MMBench v1.1, MMStar, MMMU val, MathVista, and OCRBench. One paper further describes using its official scripts, PPL mode, and zero-shot or few-shot prompting to score models across reasoning, language, knowledge, examination, and understanding.

**What it is claimed to measure.** Across papers, OpenCompass is linked to 1 construct, General ability, and no behavioral indicators. Papers use it to measure General ability by evaluating seven distinctive capabilities across 17 representative NLP datasets and by running regression tests on mainstream tasks for models' general capabilities. Claims about what it measures therefore converge on that single construct in the papers.

**Space of uses.** Papers usually position OpenCompass as the platform or framework used to evaluate benchmarks. It is related to 8 instruments, including PIQA, ARC-Challenge, ARC-Easy, CommonsenseQA, and GTA, plus 3 others; papers also describe using it for final-result assessment on zero-shot benchmarks, reporting average benchmark scores, and applying official scripts in zero-shot or few-shot settings.

## Sources

**Opencompass** (2 papers: [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf), [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf))
> An open-source evaluation framework used to systematically assess large language models on various benchmarks.

**OpenCompass** (4 papers: [Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf), [LESA: Learnable LLM Layer Scaling-Up](https://aclanthology.org/2025.acl-long.1095.pdf), [Toward Robust Hyper-Detailed Image Captioning: A Multiagent Approach and Dual Evaluation Metrics for Factuality and Coverage](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25aj/lee25aj.pdf), [UnitCoder: Scalable Code Synthesis from Pre-training Corpora](https://aclanthology.org/2025.emnlp-main.286.pdf))
> An open-source evaluation toolkit for large language models, providing standardized assessment across a wide range of benchmarks.

## Relationships

### → OpenCompass
- **General ability** (construct): *measured_by*, 2 papers
  > We evaluate seven distinctive capabilities of LLMs in a total of 17 representative NLP datasets based on the OpenCompass platform (Contributors, 2023). (Section 3.1).
  - [Mix-CPT: A Domain Adaptation Framework via Decoupling Knowledge Learning and Format Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc721384c26c0bdff3ec31a7de31d8d5-Paper-Conference.pdf)
  - [TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text](https://aclanthology.org/2025.emnlp-main.334.pdf)

### Associated with
- **PIQA** (measurement instrument), 2 papers
  > For the evaluation of Piqa, ARC-c, ARC-e, Hellaswag, MMLU and Winogrande, we use Opencompass (Contributors, 2023) to assess final results, details of prompt templates and evaluation metrics can be found in Appendix A.10. (Section 5.3)
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
  - [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf)
- **Needle-in-a-Haystack** (measurement instrument), 1 paper
  > Needle-In-A-Haystack (Contributors, 2023a) implemented in OpenCompass (Contributors, 2023b). (Figure 2)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **GTA** (measurement instrument), 1 paper
  > "Experiments are conducted using NVIDIA A100 GPU within OpenCompass [7] evaluation platform."
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ARC-Challenge** (measurement instrument), 1 paper
  > "We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA ..., ARC-challenge (ARC-C) ..., ARC-easy (ARC-E) ..., WinoGrande (WG) ..."
  - [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf)
- **ARC-Easy** (measurement instrument), 1 paper
  > "We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA ..., ARC-challenge (ARC-C) ..., ARC-easy (ARC-E) ..., WinoGrande (WG) ..."
  - [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf)
- **WinoGrande** (measurement instrument), 1 paper
  > "We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA ..., ARC-challenge (ARC-C) ..., ARC-easy (ARC-E) ..., WinoGrande (WG) ..."
  - [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf)
- **HellaSwag** (measurement instrument), 1 paper
  > "We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA ..., ARC-challenge (ARC-C) ..., ARC-easy (ARC-E) ..., WinoGrande (WG) ..., HellaSwag (HLSG) ..., and CommonSenseQA (CSQA) ..."
  - [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf)
- **CommonsenseQA** (measurement instrument), 1 paper
  > "We use Opencompass (Contributors, 2023) to test performance on several widely-used zero-shot benchmarks: PIQA ..., ARC-challenge (ARC-C) ..., ARC-easy (ARC-E) ..., WinoGrande (WG) ..., HellaSwag (HLSG) ..., and CommonSenseQA (CSQA) ..."
  - [MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b351608d824a4680344a02b180a947-Paper-Conference.pdf)
