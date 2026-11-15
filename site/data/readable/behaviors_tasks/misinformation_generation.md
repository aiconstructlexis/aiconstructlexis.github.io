# Misinformation generation
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats this behavior as producing false, misleading, or deceptive text with an LLM. A recurring formulation emphasizes content that is convincing but deceptive, sometimes described as fueling misinformation, supporting deceptive social media campaigns, or obscuring authentic discourse. Some descriptions broaden the scope by explicitly including both intentional and unintentional generation, and by allowing different types, domains, and errors.

**Variants.** Papers vary it mainly by setting and scenario. They mention social media campaigns and broader cross-domain use, and one description explicitly separates intentional generation, framed as malicious users knowingly prompting an LLM, from unintentional generation. A smaller linked framing relates it to Hallucination Generation, named as one type of LLM-based misinformation generation method.

**Space of elicitation and scores.** No measurement instrument is linked to it. In the descriptions, the behavior is specified directly through the generated output, false, misleading, or deceptive text, rather than through a named elicitation or scoring tool.

**What it is taken as evidence of.** Among the papers, only one construct is linked to it, Model collapse. One paper claims a causal relationship from Model collapse to misinformation generation, stating that when synthetic data is used in training, a model can start producing outputs that contain misinformation. No other construct is linked, and one paper separately relates misinformation generation to Hallucination by treating Hallucination Generation as a type within misinformation generation methods.

## Sources

**Misinformation generation** (3 papers: [Large Language Models Threaten Language's Epistemic and Communicative Foundations](https://aclanthology.org/2025.emnlp-main.1457.pdf), [Online Detection of LLM-Generated Texts via Sequential Hypothesis Testing by Betting](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bn/chen25bn.pdf), [Can LLM-Generated Misinformation Be Detected?](https://proceedings.iclr.cc/paper_files/paper/2024/file/94bbcb744bbada8808fda05b9d9290d6-Paper-Conference.pdf))
> The generation of convincing but deceptive content, often for use in social media campaigns or to obscure authentic discourse.

## Relationships

### → Misinformation generation
- **Model collapse** (construct): *causes*, 1 paper
  > If synthetic data is used in training these models, even in small quantities, the model can start producing “gibberish” or nonsensical outputs, contains misinformation, or reflect stereotypes. (Section 1)
  - [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > We propose to categorize the LLM-based misinformation generation methods into three types based on real-world scenarios (Table 1): Hallucination Generation (HG) (Section 3)
  - [Can LLM-Generated Misinformation Be Detected?](https://proceedings.iclr.cc/paper_files/paper/2024/file/94bbcb744bbada8808fda05b9d9290d6-Paper-Conference.pdf)
