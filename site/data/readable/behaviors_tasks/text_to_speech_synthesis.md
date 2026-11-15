# Text-to-speech synthesis
**Type:** Behavioral indicator  
**Supporting papers:** 16  
**Also known as:** Conversational speech synthesis, Speech generation, Text-to-speech generation, Text-to-speech, Speech synthesis  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats it as generating human-like or audible speech from text input, a text transcript, or written text. Definitions usually focus on producing spoken audio, and some formulations describe this as translating text into sequences of discrete audio tokens or producing speech from intermediate text responses. A smaller line of work broadens the task to converting textual content plus style instructions into speech, or to generating speech that is contextually appropriate for multi-turn dialogue; in those cases, success is described in terms of fluent, human-like speech with the requested acoustic style, users' needs, or dialogue context.

**Variants.** Several variants appear under nearby names, including conversational speech synthesis, speech generation, text-to-speech generation, and speech synthesis. Papers study context-aware conversational TTS, prompt-based customization with human-like intonation, style-conditioned generation from open-domain instructions, simple text-to-speech, and zero-shot TTS conditioned on a reference audio prompt or unseen speakers' prompts, sometimes described as generating speech in the voice of a target speaker and related to Voice cloning. Other formulations cast the task as audio language modeling, spectrogram reconstruction, or speech decoding from discrete speech tokens.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers elicit the behavior directly through task setups such as text-conditioned speech generation, simple text-to-speech, zero-shot TTS, and speech synthesis from internal representations like discrete tokens or spectrograms, with some work framing it as an audio language modeling problem.

**What it is taken as evidence of.** Construct links are limited and indirect: papers relate it to two constructs, In-context learning and Multimodal reasoning, and these links are recorded as related rather than as measurement, causal, or correlational claims. The framing does not converge on a single construct it indicates, because some work studies text-to-speech in an in-context learning setting, while other work connects generated audio differences to cross-modal reasoning capability. Related behavioral links also connect zero-shot TTS to Voice cloning, and other work says LLM-based TTS systems face Hallucination.

## Sources

**Conversational speech synthesis** (1 paper: [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey](https://aclanthology.org/2025.emnlp-main.40.pdf))
> The task of generating speech that is contextually appropriate for interactive, multi-turn dialogues.

**Text-to-speech synthesis** (3 papers: [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey](https://aclanthology.org/2025.emnlp-main.40.pdf), [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf), [HALL-E: Hierarchical Neural Codec Language Model for Minute-Long Zero-Shot Text-to-Speech Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/e32aefe039c94b95505b243e4cff8aa2-Paper-Conference.pdf))
> The task of generating human-like speech from a given text input.

**Speech generation** (1 paper: [Eliciting Implicit Acoustic Styles from Open-domain Instructions to Facilitate Fine-grained Controllable Generation of Speech](https://aclanthology.org/2025.emnlp-main.182.pdf))
> The observable task of converting textual content and style instructions into an audible speech signal.

**Text-to-speech generation** (2 papers: [Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance](https://aclanthology.org/2025.emnlp-main.1076.pdf), [UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf))
> The observable task of synthesizing audible speech from a given text transcript.

**Text-to-speech** (1 paper: [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf))
> The task of synthesizing audible speech from written text.

**Speech synthesis** (2 papers: [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf), [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf))
> The observable process of generating audible speech waveforms from an internal representation, such as discrete speech tokens.

## Relationships

### Associated with
- **Multimodal reasoning** (construct), 1 paper
  > We also note that the generated audio appears different from all context audio samples, demonstrating the cross-modal reasoning capability of LLMs when using the LLM-Codec as the connector for text and audio. (Section 5.2)
  - [UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf)
- **Voice cloning** (behavioral indicator), 1 paper
  > We apply DiTAR to zero-shot text-to-speech (TTS) that aims to generate speech from unseen speakers’ prompts. (Section 2)
  - [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25a/jia25a.pdf)
- **Hallucination** (behavioral indicator), 1 paper
  > LLM-based TTS systems face challenges, with hallucinations being a prominent issue (Sahoo et al., 2024; Song et al., 2024; Neekhara et al., 2024a; Borsos et al., 2023).
  - [Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance](https://aclanthology.org/2025.emnlp-main.1076.pdf)
- **In-context learning** (construct), 1 paper
  > We conduct experiments to validate the effectiveness of LLM-Codec in an in-context learning setting. ... we evaluate LLM-Codec on various audio understanding and generation tasks, such as speech emotion classification, audio classification, simple text-to-speech, and speech denoising.
  - [UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf)
