# Semantic consistency
**Type:** Construct  
**Supporting papers:** 17  
**Also known as:** Visual-semantic consistency  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats semantic consistency as preservation of underlying meaning when something changes, such as input phrasing, symbolic perturbation, modality, prompt form, or repeated generation. Most definitions describe stable meaning across semantically equivalent inputs or outputs, often framed as consistent answers, non-contradictory outputs, or unchanged intent. Smaller lines of work place it at the representation level, as stable semantics across text, fusion, and visible features or as visual representations staying aligned with textual ones, while another line defines it within a single response, as rationale and answer exhibiting consistent semantics. Some authors also fold correctness into the notion, describing it as maintaining the same meaning and correctness across variations of the same question.

**Space of facets.** Papers use the same label for several levels of analysis: cross-modal representation consistency, answer consistency under paraphrase or program perturbation, repeated-generation stability for the same prompt, prompt-rewrite faithfulness, and alignment between different parts of an output. Within these variants, the construct is expressed as semantic similarity, non-contradiction, preservation of meaning and intent, or stable semantic representation, and one paper explicitly names a visual-semantic subtype. One paper also distinguishes it from stylistic consistency by referring to "semantic and stylistic consistency benchmarks."

**Space of measurement.** In the linked measurements, papers connect semantic consistency to one measurement instrument, the Alpaca instruction dataset, used to create semantically equivalent question pairs, and to one behavioral indicator, Informalization. Beyond that explicit instrument link, the operationalizations described in papers are mostly similarity-based analyses rather than additional named instruments: cosine similarity between answer embeddings across question variants, average pairwise semantic similarity across repeated free-text generations, and answer agreement after translation or rotation of symbolic programs that keep the same semantics. Other papers operationalize it through whether outputs become contradictory for equivalent prompts, whether rewritten prompts lose context or narrow focus, or whether rationale and answer remain logically aligned, so the measurements track preservation of meaning across both representation-level and output-level settings.

**Links.** The recorded links are relational rather than causal or correlational. One paper relates Informalization to semantic consistency, describing semantic consistency as preservation of original meaning by informalizing candidates and comparing the embeddings of the original and informalized texts. Another paper relates semantic consistency to one construct, Semantic uncertainty, stating that decreasing semantic entropy reflects enhanced semantic consistency in the model's output space and reduced response uncertainty.

## Sources

**Visual-semantic consistency** (1 paper: [FineCLIP: Self-distilled Region-based CLIP for Better Fine-grained Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/3122aaa22b2fe83f9cead1a696f65ceb-Paper-Conference.pdf))
> The degree to which the model's visual representations maintain a coherent and meaningful alignment with their corresponding semantic (textual) representations across different levels of granularity.

**Semantic consistency** (7 papers: [Empowering Visible-Infrared Person Re-Identification with Large Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d4ee9e805cc90f636c66778225181036-Paper-Conference.pdf), [Can Large Language Models Understand Symbolic Graphics Programs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/41bd71e7bf7f9fe68f1c936940fd06bd-Paper-Conference.pdf), [Waste Not, Want Not; Recycled Gumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.292.pdf), [Analyzing and Improving Coherence of Large Language Models in Question Answering](https://aclanthology.org/2025.naacl-long.588.pdf), [ConMeC: A Dataset for Metonymy Resolution with Common Nouns](https://aclanthology.org/2025.naacl-long.330.pdf), [Self-Instructed Derived Prompt Generation Meets In-Context Learning: Unlocking New Potential of Black-Box LLMs](https://aclanthology.org/2025.acl-long.92.pdf), [Investigating Value-Reasoning Reliability in Small Large Language Models](https://aclanthology.org/2025.emnlp-main.395.pdf))
> The extent to which representations preserve the same underlying meaning across text, fusion, and visible modalities.

## Relationships

### Semantic consistency →
- **Alpaca instruction dataset** (measurement instrument): *measured_by*, 1 paper
  > We create semantically equivalent pairs of questions for evaluation by randomly sampling 300 questions from the Alpaca dataset (Taori et al., 2023) — a popular human-preference dataset - and rephrasing them using gpt-4o mini. (Section 6.1)
  - [Waste Not, Want Not; Recycled Gumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.292.pdf)

### Associated with
- **Informalization** (behavioral indicator), 1 paper
  > semantic consistency evaluates the preservation of the original meaning by informalizing the candidates and computing the similarity between the embeddings of the original and informalized texts. (Abstract)
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
- **Semantic uncertainty** (construct), 1 paper
  > “the semantic entropy of the model gradually decreases, reflecting enhanced semantic consistency in the model’s output space and reduced response uncertainty.” (Section 4.2)
  - [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf)
