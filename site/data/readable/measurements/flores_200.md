# FLORES-200
**Type:** Measurement instrument  
**Supporting papers:** 34  
**Also known as:** Flores-200, Flores200  

## State of the Field

**What it is.** Most definitions treat FLORES-200 as a multilingual machine translation benchmark spanning 200 languages, often emphasizing low-resource coverage. Papers variously use its development, test, and devtest splits; some explicitly describe it as parallel text, and one definition says it contains short paragraphs sampled from Wikimedia and translated by skilled human translators into 204 languages, whereas most others describe 200 languages. A smaller line of work also uses its development and test sets as high-quality parallel training data, and one paper notes that Belebele passages are sourced from FLORES-200.

**What it is claimed to measure.** Across the linked claims, papers use FLORES-200 to measure 1 behavioral indicator, Machine translation, and 1 construct, Generalization. The prevailing usage is machine translation evaluation, including low-resource, multilingual, English-to-X, X-to-English, and many-to-many settings; papers report chrF1, spBLEU, COMET, or BLEU on the benchmark. Only one construct link appears: one paper uses Flores200 for zero-shot evaluation as a measure of generalization in En-Zh and En-De translation.

**Space of uses.** No measurement instrument is linked to it. Papers usually position FLORES-200 as an evaluation benchmark, including 5-shot and 4-shot in-context translation evaluations, though some also use its development and test sets for training or use the test split to identify expert neurons and test cross-lingual retrieval. In the source descriptions it is sometimes used alongside WMT or WMT21 news translation, and one paper uses it together with MAFAND-MT and Lego-MT.

## Sources

**FLORES-200** (10 papers: [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf), [The Reasonableness Behind Unreasonable Translation Capability of Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/61f945d12b07c778801bd169da40762c-Paper-Conference.pdf), [X-ALMA: Plug & Play Modules and Adaptive Rejection for Quality Translation at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec0c9ca85b4ea49c7ebfb503cf55f2ae-Paper-Conference.pdf), [Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study](https://aclanthology.org/2025.naacl-long.280.pdf), [Pula: Training Large Language Models for Setswana](https://aclanthology.org/2025.naacl-long.338.pdf), [MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation](https://aclanthology.org/2025.acl-long.762.pdf), [Improving Cross Lingual Transfer by Pretraining with Active Forgetting](https://aclanthology.org/2025.emnlp-main.120.pdf), [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf), [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf), [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf))
> A multilingual benchmark dataset for evaluating machine translation quality across 200 languages, including many low-resource ones, using the chrF1 metric.

**Flores-200** (2 papers: [A Paradigm Shift in Machine Translation: Boosting Translation Performance of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b9536e186a77feff516893a5f393f7a-Paper-Conference.pdf), [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf))
> Massive multilingual benchmark dataset used for evaluating low-resource and high-resource language translation, including development and test sets used here as high-quality parallel training data.

**Flores200** (2 papers: [Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models](https://aclanthology.org/2025.acl-long.118.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf))
> A machine translation dataset containing parallel text for 204 languages, used for identifying expert neurons and evaluating cross-lingual retrieval.

## Relationships

### → FLORES-200
- **Machine translation** (behavioral indicator): *measured_by*, 11 papers
  > Translating text from a non-English language to English: We carry out these evaluations in a 5-shot in-context learning paradigm on the FLORES-200 (Costa-juss`a et al., 2022) dataset. (Section 4.2)
  - [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf)
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf)
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
  - [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf)
  - [Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages](https://aclanthology.org/2025.acl-long.795.pdf)
  - [DialUp! Modeling the Language Continuum by Adapting Models to Dialects and Dialects to Models](https://aclanthology.org/2025.acl-long.989.pdf)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
  - [Tuning Less, Prompting More: In-Context Preference Learning Pipeline for Natural Language Transformation](https://aclanthology.org/2025.emnlp-main.737.pdf)
  - [It's All About In-Context Learning! Teaching Extremely Low-Resource Languages to LLMs](https://aclanthology.org/2025.emnlp-main.1502.pdf)
  - [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > “For zero-shot evaluation, we adopt Flores200 (NLLB Team, 2022) and evaluate on {Fr, De, Hindi (Hi), Turkish (Tr), Polish (Po)→Zh} and {Fr, Zh, Hi, Tr, Po→De} for En-Zh and En-De translation respectively.”
  - [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf)
