# CoNLL-2003
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** CoNLL2003, CoNLL’03, CoNLL03  

## State of the Field

**What it is.** Across the surveyed work, CoNLL-2003 is most commonly described as a named entity recognition benchmark or dataset. When papers specify its content, they describe news text and four entity types, persons, locations, organizations, and miscellaneous, and one paper further says these are tagged using the IOB scheme, resulting in nine distinct IOB labels. One definition also presents it as an English flat NER dataset for benchmarking sequence labeling models, while another broadens its use to token-level representation learning through tasks such as NER, chunking, and POS tagging.

**What it is claimed to measure.** Across papers, its measurement claims concentrate on 1 behavioral indicator and no constructs: papers use CoNLL-2003 to measure named entity recognition. This framing is consistent across the relationship evidence, which repeatedly presents it as the dataset used for NER experiments. A broader evaluative role for token-level representation learning appears in one definition, but no additional behavioral indicators or constructs are linked to it.

**Space of uses.** Papers use it mainly as an experimental dataset for named entity recognition, and one paper explicitly states that English CoNLL03 is used as train/dev data. No papers explicitly relate it to another measurement instrument, although one paper uses it alongside TREC, MR, Subj, and AG News in a broader evaluation that also includes text classification. Another definition places it in a token-level evaluation setting with chunking and POS tagging.

## Sources

**CoNLL2003** (1 paper: [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf))
> Named entity recognition dataset that evaluates a model’s ability to identify and classify named entities in text into predefined categories such as person, organization, and location.

**CoNLL-2003** (1 paper: [MAGNET: Augmenting Generative Decoders with Representation Learning and Infilling Capabilities](https://aclanthology.org/2025.acl-long.1325.pdf))
> Named entity recognition dataset used to evaluate token-level representation learning through tasks like NER, chunking, and POS tagging.

**CoNLL’03** (1 paper: [Improving Low-Resource Sequence Labeling with Knowledge Fusion and Contextual Label Explanations](https://aclanthology.org/2025.emnlp-main.288.pdf))
> An English flat Named Entity Recognition (NER) dataset widely used for benchmarking sequence labeling models.

**CoNLL03** (1 paper: [LLMs are Better Than You Think: Label-Guided In-Context Learning for Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.1441.pdf))
> A benchmark dataset for named entity recognition derived from news articles, containing entities of four types: persons, locations, organizations, and miscellaneous.

## Relationships

### → CoNLL-2003
- **Named entity recognition** (behavioral indicator): *measured_by*, 5 papers
  > For Named Entity Recognition (NER), we use English CoNLL03 (Tjong Kim Sang, 2002) as train/dev data (Section 4.1)
  - [Constrained Decoding for Cross-lingual Label Projection](https://proceedings.iclr.cc/paper_files/paper/2024/file/67390075fe466276797f489115582cdc-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.172.pdf)
  - [Transplant Then Regenerate: A New Paradigm for Text Data Augmentation](https://aclanthology.org/2025.emnlp-main.702.pdf)
  - [LLMs are Better Than You Think: Label-Guided In-Context Learning for Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.1441.pdf)
