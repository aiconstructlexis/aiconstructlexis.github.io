# Zero-shot classification
**Type:** Behavioral indicator  
**Supporting papers:** 14  
**Also known as:** Zero-shot text classification  

## State of the Field

**Space of definitions.** Across the surveyed papers, the dominant framing treats zero-shot classification as assigning an input to one of several class labels without task-specific training, fine-tuning, or labeled examples, often from a prompt and the model's internal knowledge. Some definitions narrow this to text, where the task is to assign the correct label to a text using semantic alignment between the input and class labels, while others state it more generally as asking for a prediction on any set of classes or, in multimodal form, selecting the most probable label from text descriptions. Reported success is usually phrased as predicting the correct label or achieving zero-shot accuracy.

**Variants.** The task appears in several settings. Papers study zero-shot text classification, prompting GPT-3.5 with paper titles, abstracts, and questions for classification on ogbn-arxiv, common reasoning zero-shot classification datasets, image settings using ImageNet pretrained features with 1-NN evaluation, and multimodal classification where an image is matched to the highest-scoring text label. One paper also relates zero-shot classification to pathology detection in a medical diagnosis setting.

**Space of elicitation and scores.** Papers measure it with 9 linked instruments. The most frequently linked are ARC-Challenge, ARC-Easy, BoolQ, HellaSwag, and ImageNet-1k, and the linked instruments are mostly benchmark datasets used to report zero-shot accuracy; as one study notes, "We also compare the zero-shot accuracy on common reasoning zero-shot classification datasets..." (Search for Efficient Large Language Models). Other papers assess it on ogbn-arxiv or report ImageNet zero-shot classification accuracy.

**What it is taken as evidence of.** Papers do not treat zero-shot classification as evidence of a linked construct, and no construct is linked to it among the reported relationships. Beyond measurement links, the only additional relation is that one paper reports medical diagnosis as related to zero-shot classification through pathology detection via zero-shot and linear probing.

## Sources

**Zero-shot classification** (5 papers: [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf), [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf), [Zero-Shot Robustification of Zero-Shot Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/92ce40962b4098f7bf6eed33128fc606-Paper-Conference.pdf), [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf), [Mitigating Spurious Correlations in Zero-Shot Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2649b1d435f02524812ccbcae0dfe48b-Paper-Conference.pdf))
> The observable act of an LLM assigning class labels to input instances without any task-specific training, based solely on a prompt and its internal knowledge.

**Zero-shot text classification** (1 paper: [Beyond the Next Token: Towards Prompt-Robust Zero-Shot Classification via Efficient Multi-Token Prediction](https://aclanthology.org/2025.naacl-long.363.pdf))
> Assigning a text to one of several predefined categories without any task-specific training, using only the semantic alignment between input and class labels.

## Relationships

### Zero-shot classification →
- **ogbn-arxiv** (measurement instrument): *measured_by*, 1 paper
  > To assess the potential of LLMs in enhancing representation learning for TAGs, we conducted an initial investigation into leveraging GPT-3.5 for zero-shot classification on the ogbn-arxiv dataset. (Section 1)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
- **BoolQ** (measurement instrument): *measured_by*, 1 paper
  > We also compare the zero-shot accuracy on common reasoning zero-shot classiﬁcation datasets including BoolQ [50], PIQA [51], HellaSwag [52], WinoGrande [53], ARC-easy [54], ARC-challenge [54], and OpenbookQA [55]. (Section 4.1)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **PIQA** (measurement instrument): *measured_by*, 1 paper
  > We also compare the zero-shot accuracy on common reasoning zero-shot classiﬁcation datasets including BoolQ [50], PIQA [51], HellaSwag [52], WinoGrande [53], ARC-easy [54], ARC-challenge [54], and OpenbookQA [55]. (Section 4.1)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > We also compare the zero-shot accuracy on common reasoning zero-shot classiﬁcation datasets including BoolQ [50], PIQA [51], HellaSwag [52], WinoGrande [53], ARC-easy [54], ARC-challenge [54], and OpenbookQA [55]. (Section 4.1)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **WinoGrande** (measurement instrument): *measured_by*, 1 paper
  > We also compare the zero-shot accuracy on common reasoning zero-shot classiﬁcation datasets including BoolQ [50], PIQA [51], HellaSwag [52], WinoGrande [53], ARC-easy [54], ARC-challenge [54], and OpenbookQA [55]. (Section 4.1)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **ARC-Easy** (measurement instrument): *measured_by*, 1 paper
  > We also compare the zero-shot accuracy on common reasoning zero-shot classiﬁcation datasets including BoolQ [50], PIQA [51], HellaSwag [52], WinoGrande [53], ARC-easy [54], ARC-challenge [54], and OpenbookQA [55]. (Section 4.1)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **ARC-Challenge** (measurement instrument): *measured_by*, 1 paper
  > We also compare the zero-shot accuracy on common reasoning zero-shot classiﬁcation datasets including BoolQ [50], PIQA [51], HellaSwag [52], WinoGrande [53], ARC-easy [54], ARC-challenge [54], and OpenbookQA [55]. (Section 4.1)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **OpenBookQA** (measurement instrument): *measured_by*, 1 paper
  > We also compare the zero-shot accuracy on common reasoning zero-shot classiﬁcation datasets including BoolQ [50], PIQA [51], HellaSwag [52], WinoGrande [53], ARC-easy [54], ARC-challenge [54], and OpenbookQA [55]. (Section 4.1)
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **ImageNet-1k** (measurement instrument): *measured_by*, 1 paper
  > a lower proportion of SSC results in decreased accuracy in ImageNet zero-shot classification. (Section 4.1)
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)

### Associated with
- **Medical diagnosis** (behavioral indicator), 1 paper
  > Pathology detection via zero-shot (ZS) and linear probing at 1%, 10%, and 100% labeled data of the TUAB training set. (Table 2)
  - [EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gijsen25a/gijsen25a.pdf)
