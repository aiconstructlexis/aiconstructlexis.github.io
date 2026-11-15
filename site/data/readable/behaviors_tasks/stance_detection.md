# Stance detection
**Type:** Behavioral indicator  
**Supporting papers:** 16  
**Also known as:** Comment stance classification, Stance classification, Stance annotation  

## State of the Field

**Space of definitions.** Across the surveyed papers, the prevailing usage treats stance detection as assigning a stance label to text with respect to a specific target, topic, issue, or proposition, often described as identifying the attitude or position expressed by the author or speaker. Most papers use three-way label sets, usually favor, against, and neutral, with close alternatives such as support, oppose, and neutral or agree, disagree, and neutral. A smaller line of work uses binary versions, either affirmative versus negative for arguments or favor versus against for online political discussions.

**Variants.** Papers study several relational variants under nearby names, including stance detection, stance classification, comment stance classification, and stance annotation. Beyond generic target-level classification, one strand focuses on social media comment-reply pairs, predicting agree, neutral, or disagree for a reply relative to a parent comment, and another asks whether a top comment supports, denies, or extends an original post based on its semantic and pragmatic relationship to the post. Other settings include arguments labeled affirmative or negative, comments judged with respect to a posed political question, and news headlines labeled as agreeing, neutral, or disagreeing with a target stance about global warming.

**Space of elicitation and scores.** Papers measure it with 2 instruments, most often PStance and VAST. Both are used as datasets in experimental evaluation: linked papers report experiments on VAST and PStance to evaluate methods, and one paper refers to P-Stance as a common stance detection dataset.

**What it is taken as evidence of.** The linked papers do not connect stance detection to any construct, so they do not specify what construct this behavior is taken to indicate.

## Sources

**Stance detection** (5 papers: [MPVStance: Mitigating Hallucinations in Stance Detection with Multi-Perspective Verification](https://aclanthology.org/2025.acl-long.53.pdf), [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.24.pdf), [OpenDebateEvidence: A Massive-Scale Argument Mining and Summarization Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c630d28df1cff44314d5798f82e02ec-Paper-Datasets_and_Benchmarks_Track.pdf), [Faithful Explanations of Black-box NLP Models Using LLM-generated Counterfactuals](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5ee23c149efa1b7fb8d96a3be9908d9-Paper-Conference.pdf), [Mitigating Biases of Large Language Models in Stance Detection with Counterfactual Augmented Calibration](https://aclanthology.org/2025.naacl-long.362.pdf))
> The observable task of identifying and classifying the attitude (e.g., favor, against, neutral) expressed in a text towards a specific target or topic.

**Comment stance classification** (1 paper: [MemeReaCon: Probing Contextual Meme Understanding in Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.176.pdf))
> Determining whether a comment supports, denies, or extends the original post, based on its semantic and pragmatic relationship to the post content.

**Stance classification** (2 papers: [CARE: A Disagreement Detection Framework with Concept Alignment and Reasoning Enhancement](https://aclanthology.org/2025.emnlp-main.671.pdf), [The Power of LLM-Generated Synthetic Data for Stance Detection in Online Political Discussions](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc3ce215c378815ce0be41cb0f65d0b5-Paper-Conference.pdf))
> The observable task of assigning a label (agree, disagree, or neutral) to a reply based on its relationship to a parent comment in a social media context.

**Stance annotation** (1 paper: [Can Unconfident LLM Annotations Be Used for Confident Conclusions?](https://aclanthology.org/2025.naacl-long.179.pdf))
> Classifying whether a text agrees, is neutral, or disagrees with a target stance.

## Relationships

### Stance detection →
- **VAST** (measurement instrument): *measured_by*, 2 papers
  > We validate the effectiveness of our method through extensive experiments on the SemEval-2016, and VAST datasets, showing that MPVStance outperforms state-of-the-art models in zero-shot, few-shot, and challenging scenarios. (Section 1)
  - [MPVStance: Mitigating Hallucinations in Stance Detection with Multi-Perspective Verification](https://aclanthology.org/2025.acl-long.53.pdf)
  - [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.24.pdf)
- **PStance** (measurement instrument): *measured_by*, 2 papers
  > We conduct experiments on the VAST, SEM16, and PStance datasets to evaluate our proposed method.
  - [MPRF: Interpretable Stance Detection through Multi-Path Reasoning Framework](https://aclanthology.org/2025.emnlp-main.24.pdf)
  - [The Power of LLM-Generated Synthetic Data for Stance Detection in Online Political Discussions](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc3ce215c378815ce0be41cb0f65d0b5-Paper-Conference.pdf)
