# In-context reasoning
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Knowledge-free reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats in-context reasoning as a model ability or capacity to reason, solve problems, and make judgments from information in the current prompt or context, often as step-by-step logical inference and, in some definitions, with retrieved knowledge and without fine-tuning. A smaller line of work uses the label knowledge-free reasoning for a narrower framing: performing inference by organizing only the knowledge given in context to derive an answer, without relying on internally stored factual knowledge, including arithmetic, symbolic, and logical operations. The main difference across definitions is scope, from broad context-based problem solving to a stricter contrast with stored factual knowledge or factual recall.

**Space of facets.** Papers systematize the construct only lightly. One paper treats it as covering simple reasoning examples such as Key-value retrieval and Indirect object identification, and relates Factual recall to it in the same discussion, while another describes a facet in which predicates are bound in context and structured representations are formed in activations rather than in weights. Naming also varies: most authors use in-context reasoning, while another uses knowledge-free reasoning for a more restrictive formulation centered on context-only inference.

**Space of measurement.** The recorded operationalization is mainly benchmark-based. Papers link it to one measurement instrument, GSM8K, used as a benchmark for reasoning on GSM8K, and to three behavioral indicators, most often Factual recall, Indirect object identification, and Key-value retrieval, though these recorded links are relations rather than explicit measures. The measured usage therefore centers on benchmark reasoning performance, while the definitions themselves are more specific about using prompt-provided information and, in one framing, avoiding internally stored factual knowledge.

**Links.** The reported relational claims are all related links rather than causal or correlational ones. One paper relates in-context reasoning to Key-value retrieval and Indirect object identification as simple reasoning examples, and also relates Factual recall to in-context reasoning. Another paper relates Cross-lingual generalization to in-context reasoning, stating that the knowledge-free reasoning capability can be transferred across source-target language directions.

## Sources

**Knowledge-free reasoning** (1 paper: [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf))
> The latent ability to perform inference using only information provided in the context, without relying on internally stored factual knowledge, encompassing arithmetic, symbolic, and logical operations.

**In-context reasoning** (3 papers: [Privacy Checklist: Privacy Violation Detection Grounding on Contextual Integrity Theory](https://aclanthology.org/2025.naacl-long.86.pdf), [DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation](https://aclanthology.org/2025.emnlp-main.58.pdf), [How do Language Models Bind Entities in Context?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9d1b7fc578c0d2d6431fc26d736ecaf3-Paper-Conference.pdf))
> The model's ability to perform step-by-step logical inference within the prompt context, integrating retrieved knowledge to make judgments without fine-tuning.

## Relationships

### In-context reasoning →
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > we verify whether truncating MLPs improves reasoning on the GSM8K benchmark (Cobbe et al., 2021) (Section 4.2).
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)

### Associated with
- **Key-value retrieval** (behavioral indicator), 1 paper
  > Under this definition, we list a few simple examples of reasoning that we will consider below: • In-context recall (Section 2.1).
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
- **Indirect object identification** (behavioral indicator), 1 paper
  > Under this definition, we list a few simple examples of reasoning that we will consider below: ... • Indirect object identification (IOI) (Section 2.1).
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
- **Factual recall** (behavioral indicator), 1 paper
  > Under this definition, we list a few simple examples of reasoning that we will consider below: ... • Factual recall (Section 2.1).
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
- **Cross-lingual generalization** (construct), 1 paper
  > "the knowledge-free reasoning capability can be nearly perfectly transferred across various source-target language directions"
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
