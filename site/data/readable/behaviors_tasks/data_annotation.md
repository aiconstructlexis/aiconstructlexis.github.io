# Data annotation
**Type:** Behavioral indicator  
**Supporting papers:** 16  
**Also known as:** Annotation generation, Label generation, Preference annotation, Source category labeling, Toxicity annotation, Missing event annotation, Text annotation, Bias annotation, Pun annotation, Ingroup annotation, Outgroup annotation, Structured video annotation, Event argument annotation, Facet annotation  

## State of the Field

**Space of definitions.** Across papers, the dominant framing treats data annotation as assigning labels, metadata, or extracted features to examples according to a schema. Most uses ask for explicit outputs such as chosen or rejected preferences, gendered or neutral source labels, toxic content categories, or final truth values of True, False, and Unknown, while some extend the annotation to rationales, pedagogical feedback, textual explanations, or argument spans with roles. A smaller use broadens the term to annotation workflow steps, such as filtering unlabeled sentences for later human annotation, and the annotator itself varies from prompted LLMs and automatic annotators to teachers, students, and ingroup or outgroup raters.

**Variants.** Papers study several task-specific variants, especially preference annotation, toxicity annotation, bias annotation, event-focused annotation, and annotation generation for education. Preference annotation appears both for paired text responses and image assessment with scalar scores, rankings, and explanations, while event-focused work covers missing-event detection and argument-role assignment. Other papers apply the same behavior to source categories, review targets and aspects, and truth-value assignment.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior. Papers instead usually operationalize it directly with prompted LLMs or automatic annotators, sometimes using high-level task instructions, preference judgment principles, and few-shot examples, and the resulting outputs take the form of labels, pairwise preferences, rankings, scalar scores, explanations, or span-role assignments.

**What it is taken as evidence of.** No construct is linked to it, so papers do not explicitly specify what construct this behavior indicates.

## Sources

**Annotation generation** (1 paper: [Position: LLMs Can be Good Tutors in English Education](https://aclanthology.org/2025.emnlp-main.885.pdf))
> Producing structured labels, rationales, or pedagogical feedback for educational data, such as explanations for grammar errors or discourse relations.

**Data annotation** (2 papers: [Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.914.pdf), [SetCSE: Set Operations using Contrastive Learning of Sentence Embeddings](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed863220bf8b6ae698e26d66e86fb97d-Paper-Conference.pdf))
> The observable action of assigning labels or metadata, such as preference information, to data examples.

**Label generation** (1 paper: [MultiLogicNMR(er): A Benchmark and Neural-Symbolic Framework for Non-monotonic Reasoning with Multiple Extensions](https://aclanthology.org/2025.emnlp-main.927.pdf))
> Assigning final truth values (True, False, Unknown) to questions based on the set of computed extensions under a specified reasoning mode.

**Preference annotation** (3 papers: [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf), [Multimodal Large Language Models Make Text-to-Image Generative Models Align Better](https://proceedings.neurips.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf), [RLTHF: Targeted Human Feedback for LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25c/xu25c.pdf))
> The task of automatically labeling pairs of responses as 'chosen' or 'rejected' to create preference data for downstream model training.

**Source category labeling** (1 paper: [Mind the Inclusivity Gap: Multilingual Gender-Neutral Translation Evaluation with mGeNTE](https://aclanthology.org/2025.emnlp-main.692.pdf))
> Outputting a label that classifies the source sentence as either gendered or neutral.

**Toxicity annotation** (1 paper: [Mapping Toxic Comments Across Demographics: A Dataset from German Public Broadcasting](https://aclanthology.org/2025.emnlp-main.948.pdf))
> The observable task of assigning one or more predefined labels from a multi-class, multi-label schema to a given text to categorize its toxic content.

**Missing event annotation** (1 paper: [SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1039.pdf))
> Detecting and labeling additional event mentions in a generated sentence that were not part of the initial generation prompt.

**Text annotation** (1 paper: [Benchmarking Debiasing Methods for LLM-based Parameter Estimates](https://aclanthology.org/2025.emnlp-main.1000.pdf))
> The process of assigning a label or extracting a feature from a piece of text according to a specified schema.

**Bias annotation** (1 paper: [HESEIA: A community-based dataset for evaluating social biases in large language models, co-designed in real school settings in Latin America](https://aclanthology.org/2025.emnlp-main.1275.pdf))
> The process by which teachers and students identify and label social biases in sentences according to demographic axes such as gender, socioeconomic status, and nationality.

**Ingroup annotation** (1 paper: [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1571.pdf))
> Providing toxicity labels by individuals who self-identify with the identity group targeted in a post, reflecting community-specific norms.

**Outgroup annotation** (1 paper: [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1571.pdf))
> Providing toxicity labels by individuals who do not identify with the target group, often reflecting external perceptions of harm.

**Event argument annotation** (1 paper: [Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction](https://aclanthology.org/2025.emnlp-main.1743.pdf))
> Identifying argument spans in text and assigning each span a role for a given event type.

**Facet annotation** (1 paper: [Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews](https://aclanthology.org/2025.emnlp-main.1805.pdf))
> The observable process of assigning predefined category labels (e.g., Method, Validity) to review points to enable structured analysis of review focus.
