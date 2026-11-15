# LibriSpeech
**Type:** Measurement instrument  
**Supporting papers:** 24  
**Also known as:** Librispeech  

## State of the Field

**What it is.** Most papers describe LibriSpeech as a large corpus, dataset, or benchmark of read English speech derived from audiobooks, often aligned and segmented, and commonly framed as clean read speech for ASR. Definitions usually mention 960 hours of English reading audio, though one paper says it contains roughly 1000 hours and another extracts chunks from it to form a 1GB audio dataset for compression experiments. Papers use several subsets and settings, including train-clean-100, dev-clean, dev-other, test-clean, test-other, and 100-hour and 960-hour setups, while a smaller line simply describes Librispeech as a speech recognition dataset for closed-ended audio evaluation.

**What it is claimed to measure.** Across papers, LibriSpeech is linked to 1 construct and 2 behavioral indicators. The prevailing use is to measure Speech recognition: relationship evidence calls it an automatic speech recognition benchmark, a benchmark dataset of clean read speech for standard ASR tasks, and a test set that demonstrates ASR performance in a clean scenario. A smaller line uses it to measure Speech reconstruction, and one paper uses it to measure Utility preservation as part of a general utility evaluation built around standard ASR tasks.

**Space of uses.** No measurement instrument is linked to it directly. Papers most often position LibriSpeech as an ASR benchmark, but they also use it for pre-training, tokenizer training, mutual information estimation, phoneme recognition, reconstruction, and perplexity evaluation on speech-text sequences. It also appears alongside other benchmarks such as GigaSpeech, AMI, AIR-Bench, AudioCaps, and CHiME-4, and one paper pairs it with MELD in a broader utility evaluation.

## Sources

**LibriSpeech** (12 papers: [Language Modeling Is Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/3cbf627fa24fb6cb576e04e689b9428b-Paper-Conference.pdf), [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf), [SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/86d1ab582afb247ccaa84bec4a7e24f7-Paper-Conference.pdf), [SyllableLM: Learning Coarse Semantic Units for Speech Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2844b1bec82dd4be201f68715c03ed1b-Paper-Conference.pdf), [A Variational Framework for Improving Naturalness in Generative Spoken Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25z/chen25z.pdf), [Enhancing Speech Large Language Models with Prompt-Aware Mixture of Audio Encoders](https://aclanthology.org/2025.emnlp-main.974.pdf), [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.255.pdf), [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf), [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf), [Speech Discrete Tokens or Continuous Features? A Comparative Analysis for Spoken Language Understanding in SpeechLLMs](https://aclanthology.org/2025.emnlp-main.1266.pdf), [Wav2Prompt: End-to-End Speech Prompt Learning and Task-based Fine-tuning for Text-based LLMs](https://aclanthology.org/2025.naacl-long.354.pdf), [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf))
> A large corpus of read English speech, from which chunks are extracted to create a 1GB audio dataset for compression experiments.

**Librispeech** (2 papers: [Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf), [Soundwave: Less is More for Speech-Text Alignment in LLMs](https://aclanthology.org/2025.acl-long.917.pdf))
> A speech recognition dataset used for closed-ended audio evaluation.

## Relationships

### → LibriSpeech
- **Speech recognition** (behavioral indicator): *measured_by*, 8 papers
  > ASR | LibriSpeech test-clean/-other, GigaSpeech test | %WER (Table 2)
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
  - [VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf)
  - [Theory, Analysis, and Best Practices for Sigmoid Self-Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/a43b459e9fab3a703148ba0c83b8a442-Paper-Conference.pdf)
  - [Wav2Prompt: End-to-End Speech Prompt Learning and Task-based Fine-tuning for Text-based LLMs](https://aclanthology.org/2025.naacl-long.354.pdf)
  - [LASER: Attention with Exponential Transformation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duvvuri25a/duvvuri25a.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
  - [Enhancing Speech Large Language Models with Prompt-Aware Mixture of Audio Encoders](https://aclanthology.org/2025.emnlp-main.974.pdf)
  - [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf)
- **Speech reconstruction** (behavioral indicator): *measured_by*, 2 papers
  > We randomly sample 300 speech samples from LibriSpeech test set for speech reconstruction evaluation. (Section 4.2)
  - [SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/86d1ab582afb247ccaa84bec4a7e24f7-Paper-Conference.pdf)
  - [HALL-E: Hierarchical Neural Codec Language Model for Minute-Long Zero-Shot Text-to-Speech Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/e32aefe039c94b95505b243e4cff8aa2-Paper-Conference.pdf)
- **Utility preservation** (construct): *measured_by*, 1 paper
  > For general utility evaluation, we use AIR-Bench Chat..., LibriSpeech (Panayotov et al., 2015), a benchmark dataset of clean read speech for standard ASR tasks, and MELD... (Section 8.1)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
