# Speech translation
**Type:** Behavioral indicator  
**Supporting papers:** 17  
**Also known as:** Speech-to-text translation, Cascaded speech translation, End-to-end speech translation, Automatic speech translation  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats speech translation as converting spoken content, audio, or utterances in a source language into written text in a target language. Some definitions state this more broadly as translating spoken language into another language, but most make the speech-to-text form explicit and frame the output as target-language text. A smaller line of work separates end-to-end and cascaded formulations: Whisper-UT describes the objective as directly predicting target-language text from speech, while MultiMed-ST contrasts this with a pipeline that first transcribes speech and then translates the transcript.

**Variants.** Papers use several near names for the behavior, including speech translation, speech-to-text translation, automatic speech translation, and direct speech translation. The clearest variant split is between end-to-end speech translation, which omits intermediate transcription, and cascaded speech translation, which combines ASR with machine translation. Some work studies multilingual settings with multiple target languages or language pairs, and one paper specifically highlights terminology translation within speech translation.

**Space of elicitation and scores.** Papers link speech translation to 3 measurement instruments. The most common linked instrument is CoVoST 2, with FLEURS and MuST-C also used to test the task; the evidence describes these as evaluation datasets or data for speech-to-text translation. For scoring, one paper reports using sacreBLEU to compute BLEU scores for ST models.

**What it is taken as evidence of.** Across the papers, no construct is linked to speech translation, so there is no stated agreement about which construct it reflects. Instead, papers relate it to other behaviors: one paper claims a causal relationship from speech recognition to speech translation, stating that ASR performance influences translation quality, and one paper reports it is related to literal translation because speech-to-text systems on idiomatic data often revert to literal translations.

## Sources

**Speech translation** (2 papers: [Dynamic-SUPERB Phase-2: A Collaboratively Expanding Benchmark for Measuring the Capabilities of Spoken Language Models with 180 Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce1a7774429d5c06cc744ff4260a8e9f-Paper-Conference.pdf), [Whisper-UT: A Unified Translation Framework for Speech and Text](https://aclanthology.org/2025.emnlp-main.148.pdf))
> Translating spoken language into another language.

**Speech-to-text translation** (1 paper: [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf))
> The task of transcribing spoken audio from a source language into written text in a different target language.

**Cascaded speech translation** (1 paper: [MultiMed-ST: Large-scale Many-to-many Multilingual Medical Speech Translation](https://aclanthology.org/2025.emnlp-main.599.pdf))
> Translating speech by first transcribing it to text using ASR and then applying machine translation to the transcribed text.

**End-to-end speech translation** (1 paper: [MultiMed-ST: Large-scale Many-to-many Multilingual Medical Speech Translation](https://aclanthology.org/2025.emnlp-main.599.pdf))
> Directly translating speech in one language to text in another without an intermediate transcription step.

**Automatic speech translation** (1 paper: [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf))
> The task of translating spoken language from a source language in an audio input into written text in a target language.

## Relationships

### Speech translation →
- **CoVoST 2** (measurement instrument): *measured_by*, 4 papers
  > “En2Zh CoVoST2-En2Zh ...”
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
  - [Prepending or Cross-Attention for Speech-to-Text? An Empirical Comparison](https://aclanthology.org/2025.naacl-long.153.pdf)
  - [Distilling an End-to-End Voice Assistant Without Instruction Training Data](https://aclanthology.org/2025.acl-long.388.pdf)
  - [Soundwave: Less is More for Speech-Text Alignment in LLMs](https://aclanthology.org/2025.acl-long.917.pdf)
- **MuST-C** (measurement instrument): *measured_by*, 1 paper
  > MuST-C∗(En-Nl|En-It|En-Ro|En-Es) (Table 5).
  - [Soundwave: Less is More for Speech-Text Alignment in LLMs](https://aclanthology.org/2025.acl-long.917.pdf)
- **FLEURS** (measurement instrument): *measured_by*, 1 paper
  > We analyze the output probability distributions of Whisper on the ASR and ST tasks of the Fleurs data (Conneau et al., 2023) on 4 language pairs (Section 3)
  - [Are Generative Models Underconfident? Better Quality Estimation with Boosted Model Probability](https://aclanthology.org/2025.emnlp-main.166.pdf)

### → Speech translation
- **Speech recognition** (behavioral indicator): *causes*, 1 paper
  > In the context of ST, ASR performance influences translation quality; therefore, ASR was additionally assessed using Word Error Rate (WER) and Character Error Rate (CER). (Section 4.2)
  - [MultiMed-ST: Large-scale Many-to-many Multilingual Medical Speech Translation](https://aclanthology.org/2025.emnlp-main.599.pdf)

### Associated with
- **Literal translation** (behavioral indicator), 1 paper
  > SLT systems experience a pronounced performance drop on idiomatic data, often reverting to literal translations even in higher layers. (Section 1)
  - [It's Not a Walk in the Park! Challenges of Idiom Translation in Speech-to-text Systems](https://aclanthology.org/2025.acl-long.1512.pdf)
