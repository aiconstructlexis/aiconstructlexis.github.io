# Premature termination
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Papers that define it treat premature termination as an observable failure mode in generated speech or audio: the output sequence is abruptly shortened, so the waveform is incomplete. As one study notes, speech token sequences can have "abruptly shortened lengths," leading to premature termination of audio waveforms (Mitigating Hallucinations in LM-Based TTS Models via Distribution Alignment Using GFlowNets).

**Variants.** The described setting is speech and audio output, where the behavior appears as shortened speech token sequences and incomplete audio waveforms.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead identify it directly from the generated output, looking for abruptly shortened sequences and incomplete waveforms.

**What it is taken as evidence of.** No construct is linked to it as what it evidences. Instead, papers connect it to two other behavioral indicators: one claims a causal relationship from Reward hacking to Premature termination, using language that shortened speech token sequences are "leading to premature termination of audio waveforms," and another claims a causal relationship from Task decomposition to Premature termination, in the context of task decomposition being used to prevent it.

## Sources

**Premature termination** (1 paper: [Mitigating Hallucinations in LM-Based TTS Models via Distribution Alignment Using GFlowNets](https://aclanthology.org/2025.emnlp-main.976.pdf))
> An observable failure mode where the model generates an output sequence that is abruptly shortened, resulting in incomplete audio waveforms.

## Relationships

### → Premature termination
- **Task decomposition** (behavioral indicator): *causes*, 1 paper
  > The primary responsibility of the Planning Agent is doing macro-level planning through task decomposition to prevent premature termination. (Section 3.3)
  - [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf)
- **Reward hacking** (behavioral indicator): *causes*, 1 paper
  > In GOAT, reward hacking is observed when the model generates speech token sequences with abruptly shortened lengths, leading to premature termination of audio waveforms. (Section 3.3)
  - [Mitigating Hallucinations in LM-Based TTS Models via Distribution Alignment Using GFlowNets](https://aclanthology.org/2025.emnlp-main.976.pdf)
