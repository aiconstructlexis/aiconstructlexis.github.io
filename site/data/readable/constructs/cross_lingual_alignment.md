# Cross-lingual alignment
**Type:** Construct  
**Supporting papers:** 19  
**Also known as:** Multilingual alignment, Multilingual representation alignment, Multilingual semantic alignment, Language-agnostic semantic processing, Cross-lingual semantic alignment, Cross-lingual representation alignment, Representation alignment  

## State of the Field

**Space of definitions.** Across these papers, the prevailing usage treats cross-lingual alignment as a latent multilingual ability to align semantically equivalent content across languages in a shared space, so that knowledge can transfer across languages, often in zero-shot settings. Most definitions phrase this in representational terms, such as producing similar sentence embeddings or hidden states for equivalent texts, while a smaller line of work narrows the construct to specific settings like retrieval or cross-document inference. Another recurring variation is whether authors describe it as an ability of the model, or as the degree, process, or resulting state of bringing multilingual representations closer together.

**Space of facets.** Papers recur to several neighboring labels for closely related framings: multilingual alignment, multilingual representation alignment, multilingual semantic alignment, cross-lingual semantic alignment, cross-lingual representation alignment, representation alignment, and language-agnostic semantic processing. These labels place the emphasis on different objects, sentence embeddings, hidden-state representations, or concepts and meanings, and on different settings, such as retrieval, cross-document inference, or "language-agnostic reasoning" in middle layers. One paper also notes a contrast with monolingual structure, stating that cross-lingual alignment training can distort the optimal monolingual structure of individual languages' semantic spaces.

**Space of measurement.** Operationalization combines 3 linked measurement instruments and 3 linked behavioral indicators. The linked instruments are task benchmarks or datasets: Belebele and MMMLU are explicitly used "to evaluate this alignment," CoVoST 2 is used in work where translation results are said to confirm superior cross-lingual alignment, XNLI appears in evaluation of cross-lingual transfer, and cross-lingual sentence retrieval appears as an accuracy metric at P@1, P@5, and P@10. Papers also operationalize the construct through representational analyses, asking whether semantically equivalent texts have close embeddings or hidden states, or whether source and target language representations are brought closer, which mostly lines up with the shared-space definitions, though some papers also use downstream task performance as evidence.

**Links.** Papers mainly connect cross-lingual alignment to transfer and multilingual performance. Several papers claim causal relationships from cross-lingual alignment to cross-lingual generalization, knowledge transfer, multilingual ability, and machine translation, including one claim that a more coherent, language-agnostic embedding space "drives the observed improvements" in downstream performance and cross-lingual transfer; a separate paper claims a causal relationship from information retrieval to cross-lingual alignment. Other papers describe it as related to 3 additional behaviors or constructs, and no correlational links are reported.

## Sources

**Cross-lingual alignment** (3 papers: [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf), [Modular Sentence Encoders: Separating Language Specialization from Cross-Lingual Alignment](https://aclanthology.org/2025.acl-long.108.pdf), [AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment](https://aclanthology.org/2025.emnlp-main.328.pdf))
> The latent ability of a multilingual model to transfer knowledge across languages, particularly in zero-shot settings.

**Multilingual alignment** (1 paper: [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf))
> The latent ability of a language model to produce similar representations for semantically equivalent texts across different languages, forming the foundation for cross-lingual transfer.

**Multilingual representation alignment** (1 paper: [AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment](https://aclanthology.org/2025.emnlp-main.328.pdf))
> The process and resulting state of making the hidden-state representations of multilingual concepts more similar or geometrically closer within the model's semantic space.

**Multilingual semantic alignment** (1 paper: [Cross-Document Cross-Lingual NLI via RST-Enhanced Graph Fusion and Interpretability Prediction](https://aclanthology.org/2025.emnlp-main.1611.pdf))
> The latent ability to map concepts and meanings across languages using structural and lexical cues to support cross-lingual inference.

**Language-agnostic semantic processing** (1 paper: [The Transfer Neurons Hypothesis: An Underlying Mechanism for Language Latent Space Transitions in Multilingual LLMs](https://aclanthology.org/2025.emnlp-main.1618.pdf))
> The latent ability of a multilingual LLM to process meaning independently of input language by converging representations into a shared semantic latent space where reasoning occurs.

**Cross-lingual semantic alignment** (2 papers: [LexCLiPR: Cross-Lingual Paragraph Retrieval from Legal Judgments](https://aclanthology.org/2025.acl-long.683.pdf), [Mufu: Multilingual Fused Learning for Low-Resource Translation with LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44ae90136013a8d0e2d24f6015b6097-Paper-Conference.pdf))
> The latent ability of a model to align meaning across different languages in a retrieval setting, enabling queries in one language to retrieve relevant content in another.

**Cross-lingual representation alignment** (1 paper: [Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention](https://aclanthology.org/2025.acl-long.270.pdf))
> The latent ability of a model to map semantic representations from one language into the representational space of another, enabling transfer of capabilities across languages.

**Representation alignment** (1 paper: [ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](https://aclanthology.org/2025.acl-long.239.pdf))
> The degree to which internal model representations for different languages with the same meaning are mapped close together in the latent space, facilitating cross-lingual transfer and understanding.

## Relationships

### Cross-lingual alignment →
- **Machine translation** (behavioral indicator): *causes*, 1 paper
  > We present cross-lingual attention alignment of the ﬁnetuned models across Mufu input as a mechanistic explanation of the improvement in translation performance.
  - [Mufu: Multilingual Fused Learning for Low-Resource Translation with LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44ae90136013a8d0e2d24f6015b6097-Paper-Conference.pdf)
- **Cross-lingual generalization** (construct): *causes*, 1 paper
  > These metrics confirm that multi-way pretraining promotes a more coherent, language-agnostic embedding space, which drives the observed improvements in downstream performance and cross-lingual transfer. (Section 4.3)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
- **CoVoST 2** (measurement instrument): *measured_by*, 1 paper
  > These results confirm Audio-Reasoner’s superior cross-lingual alignment and translation performance. (Section 4.2, referring to CoVoST 2 results in Table 5)
  - [Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.1216.pdf)
- **Knowledge transfer** (construct): *causes*, 1 paper
  > A classic assumption in multilingual NLP is that more consistent multilingual representations facilitate easier knowledge transfer (Pan et al., 2021; Tang et al., 2022). (Section 1)
  - [AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment](https://aclanthology.org/2025.emnlp-main.328.pdf)
- **MMMLU** (measurement instrument): *measured_by*, 1 paper
  > To evaluate this alignment, we utilize three benchmarks—Belebele (Bandarkar et al., 2024), m-ARC (Lai et al., 2023), and m-MMLU (Lai et al., 2023)—which collectively encompass a diverse range of high-, medium-, and low-resource languages. (Section 3.4)
  - [From Neurons to Semantics: Evaluating Cross-Linguistic Alignment Capabilities of Large Language Models via Neurons Alignment](https://aclanthology.org/2025.acl-long.1406.pdf)
- **Belebele** (measurement instrument): *measured_by*, 1 paper
  > To evaluate this alignment, we utilize three benchmarks—Belebele (Bandarkar et al., 2024), m-ARC (Lai et al., 2023), and m-MMLU (Lai et al., 2023)—which collectively encompass a diverse range of high-, medium-, and low-resource languages. (Section 3.4)
  - [From Neurons to Semantics: Evaluating Cross-Linguistic Alignment Capabilities of Large Language Models via Neurons Alignment](https://aclanthology.org/2025.acl-long.1406.pdf)
- **Multilingual ability** (construct): *causes*, 1 paper
  > We present ShifCon framework, designed to boost the performance of non-dominant languages by aligning their internal forward process with that of the dominant language.
  - [ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](https://aclanthology.org/2025.acl-long.239.pdf)

### → Cross-lingual alignment
- **Information retrieval** (behavioral indicator): *causes*, 1 paper
  > we propose a cross-lingual retrieval dataset (CLR), which integrates representations across different languages through cross-lingual search, thereby narrowing the representation gap between them. (Section 3.3)
  - [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf)

### Associated with
- **Information retrieval ability** (construct), 1 paper
  > Cross-lingual context retrieval (extracting contextual information in one language based on requests in another) is a fundamental aspect of cross-lingual alignment (Abstract).
  - [Understanding LLMs' Cross-Lingual Context Retrieval: How Good It Is And Where It Comes From](https://aclanthology.org/2025.emnlp-main.1161.pdf)
- **Multilingual reasoning** (construct), 1 paper
  > Our analysis on cross-attention behaviour in Mufu-finetuned models provides evidence that the method extends LLM's capability in multilingual reasoning. That is, given any Mufu-style prompt, the finetuned models are capable of ... aligning the input semantics across languages...
  - [Mufu: Multilingual Fused Learning for Low-Resource Translation with LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44ae90136013a8d0e2d24f6015b6097-Paper-Conference.pdf)
- **Cross-lingual sentence retrieval** (behavioral indicator), 1 paper
  > We further analyze the alignment of internal representations across models. ... we compute the following four metrics: ... Cross-lingual sentence retrieval accuracy at P@1, P@5, and P@10 (Conneau et al., 2017)... (Section 4.3)
  - [From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora](https://aclanthology.org/2025.emnlp-main.374.pdf)
