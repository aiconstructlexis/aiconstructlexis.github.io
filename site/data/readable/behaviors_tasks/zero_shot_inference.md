# Zero-shot inference
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the definitions, zero-shot inference is described in two task formulations. One describes producing segmentation predictions on an unseen dataset with a supplied vocabulary and no dataset-specific retraining, with the model "trained on Ctrain and directly tested on Ctest"; another describes producing predictions from a human-designed instruction without labeled demonstrations, and characterizes the setup as "zero-shot, inference-only". The papers therefore differ mainly in whether the setting is unseen-dataset segmentation or instruction-conditioned prompting.

**Variants.** Papers study zero-shot inference in at least two settings, open vocabulary semantic segmentation on unseen datasets with customisable vocabulary, and instruction-conditioned prompting. A named related variant is Zero-shot with Chain-of-Thought (CoT), which is described as incorporating reasoning prompts to generate intermediate reasoning steps before the final answer.

**Space of elicitation and scores.** No measurement instrument is linked to it. In the papers, the behavior is elicited either by conditioning on a human-designed instruction without labeled demonstrations, or by directly testing a model on an unseen dataset with a supplied vocabulary and no dataset-specific retraining.

**What it is taken as evidence of.** Papers do not explicitly present zero-shot inference as evidence of a construct through a measurement claim. Only one construct is linked to it, In-context learning, and that link is described as related: one paper reports that an unsupervised ICL method improves upon zero-shot inference by using a few self-generated examples as context labeled by the model itself. The recorded links therefore connect it to a construct by relatedness rather than by an agreed indicator relationship.

## Sources

**Zero-shot inference** (2 papers: [Revisit the Open Nature of Open Vocabulary Semantic Segmentation](https://proceedings.iclr.cc/paper_files/paper/2025/file/17c89f4c14a4aa238616c126f5af19bb-Paper-Conference.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf))
> Producing segmentation predictions on an unseen dataset using a supplied vocabulary without dataset-specific retraining.

## Relationships

### Associated with
- **In-context learning** (construct), 1 paper
  > our unsupervised ICL method improves upon the zero-shot inference by using a few self-generated examples as a context that are labeled by the model itself, thus without requiring any labeled examples. (Section 2)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **Chain of thought** (behavioral indicator), 1 paper
  > “Zero-shot with Chain-of-Thought (CoT) incorporates CoT reasoning prompts to generate intermediate reasoning steps before the final answer”
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
