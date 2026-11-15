# Audio understanding
**Type:** Construct  
**Supporting papers:** 7  
**Also known as:** Acoustic understanding, Audio Understanding, Sound event understanding, Audio comprehension  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats audio understanding as an ability, often explicitly a latent ability, to comprehend and process auditory content. Most papers give it broad scope, spanning speech, non-speech sounds, music, and basic acoustic or signal properties such as frequency, amplitude, temporal patterns, pitch, timbre, and loudness, sometimes alongside contextual sounds. Some authors additionally describe it as mapping audio into meaningful linguistic representations, while a smaller line of work narrows the construct either to spoken-dialogue understanding beyond transcribed text, including paralinguistic cues and environmental sounds, or to sound event understanding of environmental and other non-speech sources.

**Space of facets.** Papers systematize the construct mainly by domain and granularity. One recurring split is fine-grained versus coarse-grained understanding of audio, while other papers enumerate domains such as speech, non-speech sounds, music, paralinguistic cues, environmental sounds, and sound events. The labels acoustic understanding, audio understanding, and audio comprehension are used for closely similar broad abilities, whereas sound event understanding is used more narrowly for recognizing and interpreting sources and events, described as covering animals, the environment, and human activities, with tasks ranging from animal sound classification to emergency traffic detection and multi-channel sound event understanding.

**Space of measurement.** Operationalization is narrow in the linked evidence: papers connect the construct to one measurement instrument, MMAU, a benchmark, and to one behavioral indicator, audio captioning; no construct-to-construct links are recorded. MMAU is used to evaluate understanding and reasoning in complex audio question answering tasks, and is also described as evaluating auditory expertise in music, including melodic structure, harmony, instrument identification, and contextual music interpretation. This recorded measurement emphasis is narrower than the broadest definitions, because the benchmark evidence centers on QA-style evaluation and music rather than the full range of speech, non-speech, paralinguistic, and environmental content described elsewhere.

**Links.** Beyond measurement, the only reported non-measurement link is that audio captioning is related to audio understanding. The paper making this claim says that connecting audio encoders with LLMs allows the LLM to perform various audio understanding tasks, including automatic speech recognition and audio captioning. The papers do not report causal or correlational links for this construct.

## Sources

**Acoustic understanding** (1 paper: [VoxDialogue: Can Spoken Dialogue Systems Understand Information Beyond Words?](https://proceedings.iclr.cc/paper_files/paper/2025/file/011df158529ddceb5f2f7a65f2732a5a-Paper-Conference.pdf))
> The ability of a spoken dialogue system to process and comprehend multi-modal information in audio beyond the transcribed text, such as paralinguistic cues and environmental sounds.

**Audio understanding** (2 papers: [ADIFF: Explaining audio difference using natural language](https://proceedings.iclr.cc/paper_files/paper/2025/file/1e337afbbb9fc2de993b88df0db6161e-Paper-Conference.pdf), [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf))
> The ability to comprehend and process the fundamental properties of audio signals, including acoustic characteristics like pitch and timbre as well as contextual elements like environmental sounds.

**Audio Understanding** (1 paper: [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf))
> The latent ability to comprehend audio content, including speech, non-speech sounds, and music, to interact effectively with the world.

**Sound event understanding** (1 paper: [Dynamic-SUPERB Phase-2: A Collaboratively Expanding Benchmark for Measuring the Capabilities of Spoken Language Models with 180 Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce1a7774429d5c06cc744ff4260a8e9f-Paper-Conference.pdf))
> The latent ability to recognize and interpret environmental or non-speech sound sources and events.

**Audio comprehension** (1 paper: [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf))
> The latent ability of a model to understand and interpret auditory content such as sound and music, inferred from performance across diverse audio-related tasks.

## Relationships

### Audio understanding →
- **MMAU** (measurement instrument): *measured_by*, 2 papers
  > To further evaluate our model’s understanding and reasoning capabilities in complex audio QA tasks, we conducted experiments on AIR-Bench Chat (Yang et al., 2024) and MMAU (Sakshi et al., 2024) benchmarks. (Section 4.2.2)
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
  - [Towards Holistic Evaluation of Large Audio-Language Models: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.514.pdf)

### Associated with
- **Audio captioning** (behavioral indicator), 1 paper
  > Connecting audio encoders with large language models (LLMs) allows the LLM to perform various audio understanding tasks, such as automatic speech recognition (ASR) and audio captioning (AC). (Abstract)
  - [Enhancing Speech Large Language Models with Prompt-Aware Mixture of Audio Encoders](https://aclanthology.org/2025.emnlp-main.974.pdf)
