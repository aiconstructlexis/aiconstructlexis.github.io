# Speech recognition
**Type:** Behavioral indicator  
**Supporting papers:** 33  
**Also known as:** Automatic speech recognition, Speech-to-text transcription  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is the conversion of spoken language, a speech signal, or spoken audio into written text or a textual transcription. Papers use the names automatic speech recognition, speech recognition, and speech-to-text transcription, and some explicitly restrict the output to text in the same language or the source-language transcript. Success is usually framed as accurate speech-to-text conversion, often scored with word error rate, and one study notes that ASR "requires learning precisely frame-level alignment instead of utterance-level understanding" (It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition).

**Variants.** Variation across papers is mainly in the names and settings used: beyond the common ASR label, some work studies speech-to-text transcription as intermediate text transcript generation from speech tokens, while other work trains transcription directly from spectrograms. Papers examine clean read speech, conversational and accented speech, low-resource ASR, and audio-visual settings, and some evaluate speech-to-text recognition alongside speech translation. The only linked behavioral indicator is speech translation, and one paper claims a causal relationship from speech recognition to speech translation quality by stating that ASR performance influences translation quality.

**Space of elicitation and scores.** Papers link speech recognition to 5 measurement instruments. The prevailing instrument is LibriSpeech, described as an automatic speech recognition benchmark, a Speech-to-Text dataset, and a clean read speech benchmark; FLEURS also appears as an ASR benchmark, including out-of-distribution evaluation with WER. ATIS and CoVoST 2 appear in narrower evaluation setups, and SUPERB is linked as a related benchmark configuration rather than a direct measure. Across these instruments, scoring is commonly reported with WER, with some papers also using CER or reporting (1-WER) as accuracy.

**What it is taken as evidence of.** Only one construct is linked to speech recognition, speech understanding, so papers do not present alternative construct links here. The recorded connection is not uniform in type, appearing both as a causal relationship from speech understanding to speech recognition and as a broader related link, while one paper also states that "ASR and AST are foundational tasks that enable the model to understand speech" (VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning).

## Sources

**Automatic speech recognition** (10 papers: [It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf), [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf), [Improving Semantic Understanding in Speech Language Models via Brain-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/95b7a93e60fdfd10cc202f44fd6adf5f-Paper-Conference.pdf), [Ihquin tlahtouah in Tetelahtzincocah: An annotated, multi-purpose audio and text corpus of Western Sierra Puebla Nahuatl](https://aclanthology.org/2025.naacl-long.181.pdf), [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf), [Wav2Prompt: End-to-End Speech Prompt Learning and Task-based Fine-tuning for Text-based LLMs](https://aclanthology.org/2025.naacl-long.354.pdf), [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf), [Prepending or Cross-Attention for Speech-to-Text? An Empirical Comparison](https://aclanthology.org/2025.naacl-long.153.pdf), [Whisper-UT: A Unified Translation Framework for Speech and Text](https://aclanthology.org/2025.emnlp-main.148.pdf), [Looking Beyond the Top-1: Transformers Determine Top Tokens in Order](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lioubashevski25a/lioubashevski25a.pdf))
> The task of converting a spoken language utterance (speech signal) into its corresponding textual transcription.

**Speech recognition** (6 papers: [SD-Eval: A Benchmark Dataset for Spoken Dialogue Understanding Beyond Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/681fe4ec554beabdc9c84a1780cd5a8a-Paper-Datasets_and_Benchmarks_Track.pdf), [Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf), [Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.291.pdf), [Afrispeech-Dialog: A Benchmark Dataset for Spontaneous English Conversations in Healthcare and Beyond](https://aclanthology.org/2025.naacl-long.426.pdf), [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf), [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf))
> The observable task of transcribing spoken language from an audio signal into written text.

**Speech-to-text transcription** (2 papers: [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf), [LASER: Attention with Exponential Transformation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duvvuri25a/duvvuri25a.pdf))
> Converting input speech tokens into intermediate text transcripts.

## Relationships

### Speech recognition →
- **LibriSpeech** (measurement instrument): *measured_by*, 8 papers
  > ASR | LibriSpeech test-clean/-other, GigaSpeech test | %WER (Table 2)
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
  - [VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf)
  - [Theory, Analysis, and Best Practices for Sigmoid Self-Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/a43b459e9fab3a703148ba0c83b8a442-Paper-Conference.pdf)
  - [Wav2Prompt: End-to-End Speech Prompt Learning and Task-based Fine-tuning for Text-based LLMs](https://aclanthology.org/2025.naacl-long.354.pdf)
  - [LASER: Attention with Exponential Transformation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duvvuri25a/duvvuri25a.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
  - [Enhancing Speech Large Language Models with Prompt-Aware Mixture of Audio Encoders](https://aclanthology.org/2025.emnlp-main.974.pdf)
  - [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf)
- **FLEURS** (measurement instrument): *measured_by*, 3 papers
  > We evaluate the models’ Word Error Rate (WER), memory footprint and latency on an out-of-distribution test dataset: the test split of the English Fleurs dataset (Conneau et al., 2022). (Section 7.2)
  - [Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.291.pdf)
  - [Are Generative Models Underconfident? Better Quality Estimation with Boosted Model Probability](https://aclanthology.org/2025.emnlp-main.166.pdf)
  - [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **ATIS** (measurement instrument): *measured_by*, 1 paper
  > WER (%) and WERR results of early, mid, and late fusion on ATIS and WSJ dataset. (Table 1)
  - [It's Never Too Late: Fusing Acoustic Information into Large Language Models for Automatic Speech Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/file/0231de0eff264c0639a4c43728b8b55b-Paper-Conference.pdf)
- **CoVoST 2** (measurement instrument): *measured_by*, 1 paper
  > testing speech-to-text recognition (ASR) and translation (ST) on MuST-C v1.0 and CoVoST2 datasets. (Abstract)
  - [Prepending or Cross-Attention for Speech-to-Text? An Empirical Comparison](https://aclanthology.org/2025.naacl-long.153.pdf)
- **Speech translation** (behavioral indicator): *causes*, 1 paper
  > In the context of ST, ASR performance influences translation quality; therefore, ASR was additionally assessed using Word Error Rate (WER) and Character Error Rate (CER). (Section 4.2)
  - [MultiMed-ST: Large-scale Many-to-many Multilingual Medical Speech Translation](https://aclanthology.org/2025.emnlp-main.599.pdf)

### → Speech recognition
- **Speech understanding** (construct): *causes*, 2 papers
  > “ASR and AST are foundational tasks that enable the model to understand speech”
  - [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf)
  - [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf)

### Associated with
- **SUPERB** (measurement instrument), 1 paper
  > We evaluate them on three common speech tasks with corresponding common benchmarks: ASR with TED-LIUMv3 (Hernandez et al., 2018), intent classification, a standard SLU task, with SLURP (Bastianelli et al., 2020), along with speaker ID with VoxCeleb1 (Nagrani et al., 2020), following the SUPERB configuration (Yang et al., 2021) (Section 4.4).
  - [Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b79416c0dc4b09feaa169ed5cdd63d4-Paper-Conference.pdf)
