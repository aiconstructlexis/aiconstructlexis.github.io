# Emotion analysis
**Type:** Behavioral indicator  
**Supporting papers:** 46  
**Also known as:** Emotion classification, Emotion recognition in conversations, Emotion detection, Emotion recognition, Emotional state extraction, Emotion label generation, Emotional Tone Interpretation, Emotion recognition in conversation, Text emotion detection, Emotion prediction  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is a label assignment task: papers most commonly describe emotion analysis as identifying or classifying emotions in text or utterances, often with labels such as joy, anger, fear, or sadness. Many formulations assume a predefined label set, with either a single label for a target utterance or multiple labels for the same text or post. A recurrent conversation-specific version predicts the emotion of the current turn from preceding dialogue history, while a smaller line of work frames the task as extracting emotional connotations, identifying the dominant top M emotions in a document, or generating free-text emotion descriptions instead of choosing from a fixed set.

**Variants.** Most papers use nearby names such as emotion classification, emotion detection, and emotion recognition. Common settings are plain text and dialogue, especially emotion recognition in conversations, but papers also study multimodal inputs, audio, physiological signals, narrative sentences, Persian text, and rhetorical language. Smaller variants include emotional state extraction from dialogue history, emotional tone interpretation from instruments or speech, coarse- and fine-grained multimodal classification, and open-vocabulary emotion prediction that allows labels beyond a fixed set.

**Space of elicitation and scores.** Papers link emotion analysis to 5 measurement instruments, most often GoEmotions, then IEMOCAP, SemEval 2018 Task 1 E-c, MELD, and TweetEval. GoEmotions and SemEval 2018 Task 1 E-c are described as multilabel emotion recognition benchmarks, IEMOCAP and MELD are used to assess emotion recognition on utterances, and TweetEval contributes a multiclass emotion recognition task.

**What it is taken as evidence of.** The construct side is narrow: papers link emotion analysis to 1 construct, Emotion understanding, and the recorded claim is that Emotion analysis is related to it rather than measuring or correlating with it, in work that pairs coarse-grained prompting with fine-grained classification. Separate from construct links, papers connect it to 2 other behavioral indicators: one paper claims a causal relationship from Object detection to Emotion analysis, and one paper reports that Emotion analysis is related to Time series classification.

## Sources

**Emotion classification** (3 papers: [ResFormer: All-Time Reservoir Memory for Long Sequence Classification](https://aclanthology.org/2025.emnlp-main.566.pdf), [Implicit In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc034d186280f55370b6aca7a3285a65-Paper-Conference.pdf), [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf))
> Assigning an emotional label (e.g., joy, fear, anger) to a given utterance based on its content and contextual history in a conversation.

**Emotion analysis** (2 papers: [Enhancing Hyperbole and Metaphor Detection with Their Bidirectional Dynamic Interaction and Emotion Knowledge](https://aclanthology.org/2025.acl-long.23.pdf), [A Checks-and-Balances Framework for Context-Aware Ethical AI Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25a/chang25a.pdf))
> Extracting and representing the emotional connotations present in a sentence, particularly those underlying rhetorical expressions.

**Emotion recognition in conversations** (1 paper: [CoE: A Clue of Emotion Framework for Emotion Recognition in Conversations](https://aclanthology.org/2025.acl-long.1148.pdf))
> The task of assigning a predefined emotion label to a specific utterance within a dialogue, given the preceding conversational history.

**Emotion detection** (2 papers: [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486.pdf), [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf))
> Identifying specific emotions expressed in text, such as anger, joy, or fear, often used in social media analysis.

**Emotion recognition** (2 papers: [Large Language Models Do Multi-Label Classification Differently](https://aclanthology.org/2025.emnlp-main.126.pdf), [Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf))
> The task of identifying and classifying human emotions expressed in text.

**Emotional state extraction** (1 paper: [MultiAgentESC: A LLM-based Multi-Agent Collaboration Framework for Emotional Support Conversation](https://aclanthology.org/2025.emnlp-main.232.pdf))
> The observable task of identifying and labeling a user's emotions from their utterances in a dialogue history.

**Emotion label generation** (1 paper: [CR4-NarrEmote: An Open Vocabulary Dataset of Narrative Emotions Derived Using Citizen Science](https://aclanthology.org/2025.emnlp-main.493.pdf))
> Producing free-text descriptions of the emotions a narrative character is feeling based on a given sentence.

**Emotional Tone Interpretation** (1 paper: [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf))
> The task behavior of identifying the emotional atmosphere or tone created by audio elements such as instruments or speech.

**Emotion recognition in conversation** (1 paper: [EmoDynamiX: Emotional Support Dialogue Strategy Prediction by Modelling MiXed Emotions and Discourse Dynamics](https://aclanthology.org/2025.naacl-long.81.pdf))
> The task of identifying and classifying the emotions expressed in utterances within a dialogue context.

**Text emotion detection** (1 paper: [Matina: A Large-Scale 73B Token Persian Text Corpus](https://aclanthology.org/2025.naacl-long.462.pdf))
> Identifying emotional categories (e.g., joy, anger) in Persian text, particularly in social media or informal content.

**Emotion prediction** (1 paper: [OV-MER: Towards Open-Vocabulary Multimodal Emotion Recognition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lian25b/lian25b.pdf))
> The observable task of outputting one or more emotion labels given a multimodal input, particularly with the flexibility to use labels outside a fixed set.

## Relationships

### Emotion analysis →
- **GoEmotions** (measurement instrument): *measured_by*, 3 papers
  > GoEmotions (Demszky et al., 2020): Multilabel emotion recognition benchmark with 27 emotions. (Section 4.1)
  - [Aggregation Artifacts in Subjective Tasks Collapse Large Language Models' Posteriors](https://aclanthology.org/2025.naacl-long.284.pdf)
  - [Large Language Models Do Multi-Label Classification Differently](https://aclanthology.org/2025.emnlp-main.126.pdf)
  - [Humans Hallucinate Too: Language Models Identify and Correct Subjective Annotation Errors With Label-in-a-Haystack Prompts](https://aclanthology.org/2025.emnlp-main.993.pdf)
- **IEMOCAP** (measurement instrument): *measured_by*, 2 papers
  > ER | IEMOCAP Session 5 | Accuracy (Table 2)
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
  - [Distilling an End-to-End Voice Assistant Without Instruction Training Data](https://aclanthology.org/2025.acl-long.388.pdf)
- **SemEval 2018 Task 1 E-c** (measurement instrument): *measured_by*, 2 papers
  > SemEval 2018 Task 1 E-c (Mohammad et al., 2018) Multi-label emotion recognition of 11 emotions. (Section 3)
  - [Large Language Models Do Multi-Label Classification Differently](https://aclanthology.org/2025.emnlp-main.126.pdf)
  - [Humans Hallucinate Too: Language Models Identify and Correct Subjective Annotation Errors With Label-in-a-Haystack Prompts](https://aclanthology.org/2025.emnlp-main.993.pdf)
- **MELD** (measurement instrument): *measured_by*, 1 paper
  > Emotion recognition is assessed on IEMOCAP (Busso et al., 2008) and MELD (Poria et al., 2019), with 1,241 and 2,608 utterances.
  - [Distilling an End-to-End Voice Assistant Without Instruction Training Data](https://aclanthology.org/2025.acl-long.388.pdf)
- **TweetEval** (measurement instrument): *measured_by*, 1 paper
  > Multi-class tasks include emotion recognition (Mohammad et al., 2018) and irony detection (Van Hee et al., 2018) from the TweetEval benchmark (Barbieri et al., 2020)... (Section 4.1)
  - [Inceptive Transformers: Enhancing Contextual Representations through Multi-Scale Feature Learning Across Domains and Languages](https://aclanthology.org/2025.emnlp-main.1312.pdf)

### → Emotion analysis
- **Object detection** (behavioral indicator): *causes*, 1 paper
  > The model's ability to detect faces is crucial for subsequent emotion recognition, as it allows the system to focus on the relevant regions of interest and extract facial features effectively.
  - [Emotion-LLaMA: Multimodal Emotion Recognition and Reasoning with Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/c7f43ada17acc234f568dc66da527418-Paper-Conference.pdf)

### Associated with
- **Emotion understanding** (construct), 1 paper
  > In this paper, we propose Sharpening Emotion Perception in Multimodal Large Language Models (SEPM)... The first stage performs coarse-grained emotion classification, generating textual prompts for the next stage... The second stage then completes fine-grained emotion classification based on this enhanced input. (Section 1, 3.2)
  - [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf)
- **Time series classification** (behavioral indicator), 1 paper
  > Specifically, we focus on various medical time series classification (TSC) tasks based on the physiological signals, including emotion recognition (Li et al., 2024a), sleep stage detection (Supratak et al., 2017; Dong et al., 2017), neurological disorder classification (Yang et al., 2022b; Zhang et al., 2022), etc. (Section 1).
  - [Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ah/wu25ah.pdf)
