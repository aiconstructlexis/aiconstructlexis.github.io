# Audio captioning
**Type:** Behavioral indicator  
**Supporting papers:** 13  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is generating a natural-language or textual caption for an audio clip. Most definitions describe non-speech audio, especially environmental sounds or events, and some extend the scope to music or scene-based sounds. A few formulations make the output requirement more specific as a sentence or description of the sounds present in an audio clip, and one paper elicits it with the prompt 'write an audio caption describing the sound' and uses the model output as the prediction.

**Variants.** Papers use several nearby names for this task, most commonly audio captioning, and sometimes automatic audio captioning or AAC. The studied content is usually general non-speech audio, though papers explicitly mention environmental sounds, events, scene-based sounds, and music, including an example caption for a classical piece played at a slow tempo.

**Space of elicitation and scores.** Papers link audio captioning to three measurement instruments. The most frequent are AudioCaps and Clotho, with MusicCaps appearing less often; these are described as audio captioning benchmarks or datasets, and some papers describe AudioCaps and Clotho as human-annotated. Elicitation is sometimes prompt based, and scoring is described with conventional audio captioning metrics, with CIDEr appearing in one reported result label.

**What it is taken as evidence of.** Across these papers, the construct framing is narrow. The only linked construct is Audio understanding, and one paper relates audio captioning to it by saying that connecting audio encoders with LLMs enables various audio understanding tasks, such as automatic speech recognition and audio captioning. No other construct is linked in these papers.

## Sources

**Audio captioning** (6 papers: [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf), [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf), [Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf), [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf), [Towards Holistic Evaluation of Large Audio-Language Models: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.514.pdf), [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf))
> Generating natural language descriptions of non-speech audio content such as environmental sounds or events.

## Relationships

### Audio captioning →
- **AudioCaps** (measurement instrument): *measured_by*, 6 papers
  > evaluate LTU on the test set of two major audio captioning benchmarks Clotho v2 (Drossos et al., 2020) and AudioCaps (Kim et al., 2019) (Section 5.1)
  - [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf)
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
  - [An eye for an ear: zero-shot audio description leveraging an image captioner with audio-visual token distribution matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/4426af45e987692abf1b80108951ff8a-Paper-Conference.pdf)
  - [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf)
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
  - [Enhancing Speech Large Language Models with Prompt-Aware Mixture of Audio Encoders](https://aclanthology.org/2025.emnlp-main.974.pdf)
- **Clotho** (measurement instrument): *measured_by*, 3 papers
  > We evaluate our proposed approach on two popular and publicly available human-annotated audio captioning datasets: AudioCaps and Clotho (Tampere University licence), using conventional audio captioning metrics. (Section 4)
  - [An eye for an ear: zero-shot audio description leveraging an image captioner with audio-visual token distribution matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/4426af45e987692abf1b80108951ff8a-Paper-Conference.pdf)
  - [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf)
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
- **MusicCaps** (measurement instrument): *measured_by*, 1 paper
  > Table 2 summarizes the comparative results for audio captioning tasks on AudioCaps, Clotho, and MusicCaps benchmarks. (Section 4.2.1)
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)

### Associated with
- **Audio understanding** (construct), 1 paper
  > Connecting audio encoders with large language models (LLMs) allows the LLM to perform various audio understanding tasks, such as automatic speech recognition (ASR) and audio captioning (AC). (Abstract)
  - [Enhancing Speech Large Language Models with Prompt-Aware Mixture of Audio Encoders](https://aclanthology.org/2025.emnlp-main.974.pdf)
