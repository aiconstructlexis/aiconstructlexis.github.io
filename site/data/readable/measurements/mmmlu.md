# MMMLU
**Type:** Measurement instrument  
**Supporting papers:** 13  
**Also known as:** M-MMLU  

## State of the Field

**What it is.** Across papers, MMMLU is most commonly described as a multilingual version of MMLU, often specifically a human-translated or professionally translated variant used across multiple languages and subjects. Definitions vary in emphasis, framing it as testing general language understanding, reasoning performance, knowledge comprehension, or world knowledge. One description also notes that answers are extracted from generated outputs rather than token probabilities, and another use draws on its test sets to create "easy" and "hard" evaluation sets.

**What it is claimed to measure.** Papers use MMMLU to measure four constructs and two behavioral indicators. The named targets include cross-lingual alignment, knowledge understanding, multilingual ability, multilingual reasoning, and language mixing, with one additional behavioral indicator also linked to it. Overall, papers distribute its measurement claims across several named targets rather than centering on only one.

**Space of uses.** Several papers place MMMLU inside broader multilingual evaluation suites. It appears with Belebele and m-ARC in cross-lingual alignment evaluations, with Belebele again for multiple-choice question answering, and with MMLU in another multilingual evaluation track. One setup uses five-shot prompting.

## Sources

**MMMLU** (3 papers: [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf), [Cross-Lingual Optimization for Language Transfer in Large Language Models](https://aclanthology.org/2025.acl-long.734.pdf), [P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs](https://aclanthology.org/2025.emnlp-main.242.pdf))
> A human-translated version of the MMLU benchmark, used to test general language understanding across multiple languages and subjects.

**M-MMLU** (1 paper: [MPO: Multilingual Safety Alignment via Reward Gap Optimization](https://aclanthology.org/2025.acl-long.1149.pdf))
> A multilingual benchmark for evaluating a model's world knowledge across a wide range of subjects and languages.

## Relationships

### → MMMLU
- **Multilingual ability** (construct): *measured_by*, 1 paper
  > To evaluate the LLMs’ capability across languages, researchers developed various multilingual benchmarks. Many rely on English translation, including XNLI (Conneau et al., 2018), MMMLU (Hendrycks et al., 2021a)... (Section 2)
  - [NOVA-63: Native Omni-lingual Versatile Assessments of 63 Disciplines](https://aclanthology.org/2025.emnlp-main.364.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > For multiple choice QA, we use Belebele (Bandarkar et al., 2024) and Multilingual MMLU (Hendrycks et al., 2021; Lai et al., 2023, MMMLU) with five shot prompting. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **Language mixing** (behavioral indicator): *measured_by*, 1 paper
  > To evaluate language mixing across broader domains, we also use the multilingual MMLU (m-MMLU) dataset... (Section 3)
  - [Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes](https://aclanthology.org/2025.emnlp-main.132.pdf)
- **Knowledge understanding** (construct): *measured_by*, 1 paper
  > the OpenAI multilingual version of MMLU (MMMLU)1 for knowledge comprehension (Section 2)
  - [P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs](https://aclanthology.org/2025.emnlp-main.242.pdf)
- **Multilingual reasoning** (construct): *measured_by*, 1 paper
  > Beyond English textual reasoning, we include two additional evaluation tracks: a multilingual experiment using MMLU and its professionally translated variant MMMLU (Hendrycks et al., 2021)...
  - [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1236.pdf)
- **Cross-lingual alignment** (construct): *measured_by*, 1 paper
  > To evaluate this alignment, we utilize three benchmarks—Belebele (Bandarkar et al., 2024), m-ARC (Lai et al., 2023), and m-MMLU (Lai et al., 2023)—which collectively encompass a diverse range of high-, medium-, and low-resource languages. (Section 3.4)
  - [From Neurons to Semantics: Evaluating Cross-Linguistic Alignment Capabilities of Large Language Models via Neurons Alignment](https://aclanthology.org/2025.acl-long.1406.pdf)
