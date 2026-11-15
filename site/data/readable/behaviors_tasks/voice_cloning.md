# Voice cloning
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Zero-shot text-to-speech  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing framing treats voice cloning as zero-shot text-to-speech: generating speech in a new or unseen speaker's voice from a short audio prompt, without speaker-specific training or fine-tuning. Definitions also describe it as synthesizing speech that mimics a particular person's voice, often from a brief audio sample. Some formulations make the text input explicit and describe the target as natural speech conditioned on a speech prompt.

**Variants.** Most papers use the names zero-shot text-to-speech or zero-shot TTS, while some explicitly call it voice-cloning speech synthesis. A smaller line of work places it in multilingual settings or alongside speech editing, and one paper frames zero-shot TTS as a conditional continuation task in which prompting texts, target text, and prompting speech are concatenated as prefix context. One paper also reports it as related to text-to-speech synthesis.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior. Papers nevertheless describe evaluation in zero-shot TTS setups, including evaluation on the VCTK dataset and comparisons in zero-shot TTS tasks where one model outperforms another. The elicitation setup is usually described through text input plus a short speech prompt from an unseen speaker.

**What it is taken as evidence of.** Papers link it to two constructs, Naturalness and Robustness, and both links are framed as related. One paper further states that in zero-shot speech generation, performance includes robustness, speaker similarity, and naturalness. Because the construct links are reported as related rather than measured_by or correlates, papers do not explicitly identify a single construct that this behavior reflects.

## Sources

**Zero-shot text-to-speech** (3 papers: [VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing](https://aclanthology.org/2025.emnlp-main.137.pdf), [SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/86d1ab582afb247ccaa84bec4a7e24f7-Paper-Conference.pdf), [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25a/jia25a.pdf))
> Generating speech in a new speaker's voice using only a short audio prompt from that speaker, without any speaker-specific training.

**Voice cloning** (1 paper: [VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing](https://aclanthology.org/2025.emnlp-main.137.pdf))
> The specific task of synthesizing speech that mimics the voice of a particular person, often in a zero-shot setting from a brief audio sample.

## Relationships

### Associated with
- **Text-to-speech synthesis** (behavioral indicator), 1 paper
  > We apply DiTAR to zero-shot text-to-speech (TTS) that aims to generate speech from unseen speakers’ prompts. (Section 2)
  - [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25a/jia25a.pdf)
- **Robustness** (construct), 1 paper
  > In zero-shot speech generation, DiTAR achieves state-of-the-art performance in robustness, speaker similarity, and naturalness.
  - [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25a/jia25a.pdf)
- **Naturalness** (construct), 1 paper
  > In zero-shot speech generation, DiTAR achieves state-of-the-art performance in robustness, speaker similarity, and naturalness.
  - [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25a/jia25a.pdf)
