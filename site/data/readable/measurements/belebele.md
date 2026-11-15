# Belebele
**Type:** Measurement instrument  
**Supporting papers:** 17  
**Also known as:** BELEBELE  

## State of the Field

**What it is.** Most papers describe Belebele as a multilingual reading comprehension benchmark, usually framed as multiple-choice questions about short passages. Several definitions specify 122 language variants or language-dialect combinations, sometimes with parallel passages and questions, while one paper describes it as translated into over 200 languages and another uses official Moroccan and Egyptian dialect sets. Some papers describe its passages as sourced from FLORES-200, and one refers to it as another benchmark extended from the FLORES family of multilingual evaluation resources.

**What it is claimed to measure.** Papers link Belebele to two behavioral indicators and two constructs. The prevailing usage is to measure machine reading comprehension, and a smaller line of work uses it for multiple-choice question answering; at the construct level, papers also report it as measuring natural language understanding and cross-lingual alignment. Overall, the measurement claims center on reading comprehension, with the broader construct claims spread across those two constructs.

**Space of uses.** Papers usually use Belebele as part of a broader benchmark suite rather than on its own. It appears alongside FLORES for checkpoint selection and evaluation, alongside Multilingual MMLU or m-MMLU for multiple-choice QA and alignment evaluations, and with m-ARC in cross-lingual alignment work; several papers also specify 5-shot prompting or particular dialect subsets such as the official Moroccan and Egyptian sets.

## Sources

**BELEBELE** (2 papers: [Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f9a44cb707ede42a659ad85d940dd55-Paper-Conference.pdf), [LAuReL: Learned Augmented Residual Layer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/menghani25a/menghani25a.pdf))
> A multilingual reading comprehension benchmark used to assess a model's basic language understanding across many languages.

**Belebele** (6 papers: [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf), [Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque](https://aclanthology.org/2025.naacl-long.629.pdf), [FLEURS-ASL: Including American Sign Language in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.314.pdf), [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf), [Less, but Better: Efficient Multilingual Expansion for LLMs via Layer-wise Mixture-of-Experts](https://aclanthology.org/2025.acl-long.878.pdf), [NileChat: Towards Linguistically Diverse and Culturally Aware LLMs for Local Communities](https://aclanthology.org/2025.emnlp-main.556.pdf))
> A multilingual benchmark for evaluating reading comprehension via multiple-choice questions based on short passages.

## Relationships

### → Belebele
- **Machine reading comprehension** (behavioral indicator): *measured_by*, 4 papers
  > Belebele (Bandarkar et al., 2024): Belebele is a multiple-choice machine reading comprehension dataset spanning 122 language variants. (Section 3.3)
  - [Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque](https://aclanthology.org/2025.naacl-long.629.pdf)
  - [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf)
  - [It's All About In-Context Learning! Teaching Extremely Low-Resource Languages to LLMs](https://aclanthology.org/2025.emnlp-main.1502.pdf)
  - [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > For multiple choice QA, we use Belebele (Bandarkar et al., 2024) and Multilingual MMLU (Hendrycks et al., 2021; Lai et al., 2023, MMMLU) with five shot prompting. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **Natural language understanding** (construct): *measured_by*, 1 paper
  > After numerous SFT runs on these “generic” multi-task datasets, the three checkpoints for each language are primarily selected based off their performance on the target language splits on BELEBELE (Bandarkar et al., 2024) and FLORES (NLLB et al., 2022). These simple tasks, reading comprehension and translation, are strong indicators of basic language understanding and generation capabilities. (Section 3.1)
  - [Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f9a44cb707ede42a659ad85d940dd55-Paper-Conference.pdf)
- **Cross-lingual alignment** (construct): *measured_by*, 1 paper
  > To evaluate this alignment, we utilize three benchmarks—Belebele (Bandarkar et al., 2024), m-ARC (Lai et al., 2023), and m-MMLU (Lai et al., 2023)—which collectively encompass a diverse range of high-, medium-, and low-resource languages. (Section 3.4)
  - [From Neurons to Semantics: Evaluating Cross-Linguistic Alignment Capabilities of Large Language Models via Neurons Alignment](https://aclanthology.org/2025.acl-long.1406.pdf)
