# Speech continuation
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is a continuation task: a model receives a prompt and generates the subsequent portion of speech so that it "seamlessly" or "coherently" follows what was given. Most descriptions stress contextual fit, using formulations such as a "coherent and contextually appropriate audio continuation" or "a coherent and natural-sounding continuation." Papers differ on the prompt, with some describing text plus an initial speech segment, including the initial 3 seconds of the ground truth speech, while others describe a spoken audio prompt; one paper also reports preferred continuations according to human raters.

**Variants.** Authors mostly call the behavior "speech continuation," with additional labels such as "direct speech continuation" and simply "continuation." The studied settings span text-conditioned continuation with an initial speech segment and spoken-audio continuation, and one formulation casts the objective as frame-level spectrogram regression, predicting each frame's spectrogram channels from previous spectrogram predictions plus ASR and LM context. Another paper evaluates continuation alongside cross-sentence tasks.

**Space of elicitation and scores.** No measurement instrument is linked to it, so papers do not connect speech continuation here to any named elicitation or scoring instrument.

**What it is taken as evidence of.** No construct is linked to it as evidence of, so papers do not specify what broader construct it reflects.

## Sources

**Speech continuation** (3 papers: [CLaM-TTS: Improving Neural Codec Language Model for Zero-Shot Text-to-Speech](https://proceedings.iclr.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf), [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf), [A Variational Framework for Improving Naturalness in Generative Spoken Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25z/chen25z.pdf))
> Continuing a speech utterance from a text prompt and an initial speech segment so that the output seamlessly follows the prompt.
