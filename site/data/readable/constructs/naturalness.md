# Naturalness
**Type:** Construct  
**Supporting papers:** 28  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats naturalness as the perceived human-likeness and fluency of generated output, most often synthesized speech, with descriptions emphasizing prosody, smoothness, authenticity, auditory quality, or being free from artifacts, sometimes explicitly beyond intelligibility or accuracy. Some authors extend the same label to generated text and dialogue, where it refers to human-like wording, coherent flow, turn-taking, and contextual appropriateness, and one paper shifts the unit of analysis to the corpus level by asking whether a set of model-generated texts could have been produced by native speakers. A smaller framing narrows it to language quality in responses, including grammar, pronoun usage, context correlation, and oral expression.

**Space of facets.** Papers unpack naturalness through nearby facets rather than a consistent subtype scheme. Prosody is a recurring dimension, sometimes presented as contributing to naturalness and expressiveness, and sometimes rated separately from naturalness; other papers describe the construct through flow, plausibility, contextual relevance, grammar, and oral expression. Across these uses, naturalness is usually kept distinct from intelligibility, accuracy, coherence, expressiveness, and overall quality, so the same name covers speech quality, dialogue flow, and corpus-level native-speaker-like text.

**Space of measurement.** Operationally, papers link naturalness to 3 measurement instruments and 1 behavioral indicator overall. The most frequently linked instrument is LLM-as-a-judge, followed by Human evaluation and G-Eval: LLM judges score activity sequences, dialogues, or synthesized speech against criteria such as sounding natural or aligning with a person's habits and environment, while human raters give overall subjective impressions or five-point ratings of how natural a conversation or speech sample sounds. Elsewhere, speech papers also use NISQA and mean-opinion style ratings, and these operationalizations usually follow the human-likeness framing, though some narrow it to dialogue flow, native-speaker indistinguishability, or task-specific fit.

**Links.** Beyond measurement, the reported links are all related links, and no causal or correlational claims are recorded. One paper relates naturalness to voice cloning in zero-shot speech generation, and another relates conversational ability to naturalness by describing conversational gains in terms of turn-taking prediction, response coherence, and naturalness.

## Sources

**Naturalness** (12 papers: [Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf), [CLaM-TTS: Improving Neural Codec Language Model for Zero-Shot Text-to-Speech](https://proceedings.iclr.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf), [PolyVoice: Language Models for Speech to Speech Translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a60c43ba078b723d3d517d28c50ded4c-Paper-Conference.pdf), [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf), [PicPersona-TOD : A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.403.pdf), [Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLM Communication](https://aclanthology.org/2025.naacl-long.203.pdf), [MADial-Bench: Towards Real-world Evaluation of Memory-Augmented Dialogue Generation](https://aclanthology.org/2025.naacl-long.499.pdf), [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf), [PRACTIQ: A Practical Conversational Text-to-SQL dataset with Ambiguous and Unanswerable Queries](https://aclanthology.org/2025.naacl-long.13.pdf), [Do Large Language Models have an English Accent? Evaluating and Improving the Naturalness of Multilingual LLMs](https://aclanthology.org/2025.acl-long.193.pdf), [A Variational Framework for Improving Naturalness in Generative Spoken Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25z/chen25z.pdf), [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey](https://aclanthology.org/2025.emnlp-main.40.pdf))
> The degree to which synthesized speech is perceived as fluent, human-like, and perceptually smooth, beyond mere intelligibility or accuracy.

## Relationships

### Naturalness →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 3 papers
  > When evaluating the likelihood of the activity sequences, GPT-4o is instructed to take the following criteria into account: Naturalness: How well the activity aligns with the person’s innate abilities, habits, and environment.
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
  - [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf)
  - [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey](https://aclanthology.org/2025.emnlp-main.40.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 2 papers
  > Overall naturalness Overall subjective impression of the conversation and whether it sounds natural. (Table 2)
  - [Wizard of Shopping: Target-Oriented E-commerce Dialogue Generation with Decision Tree Branching](https://aclanthology.org/2025.acl-long.641.pdf)
  - [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.726.pdf)
- **G-Eval** (measurement instrument): *measured_by*, 1 paper
  > For LLM-based evaluation, we employed G-EVAL(Liu et al., 2023), a state-of-the-art metric designed to assess various qualitative aspects of large language model outputs, including Fluency, Coherence, Naturalness, Empathy, and Patient-Centricity, where higher scores indicate better performance. (Section 5.1)
  - [AI Chatbots as Professional Service Agents: Developing a Professional Identity](https://aclanthology.org/2025.emnlp-main.652.pdf)

### Associated with
- **Voice cloning** (behavioral indicator), 1 paper
  > In zero-shot speech generation, DiTAR achieves state-of-the-art performance in robustness, speaker similarity, and naturalness.
  - [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25a/jia25a.pdf)
- **Conversational ability** (construct), 1 paper
  > "NTPP, significantly improves the conversational abilities of SLMs in terms of turn-taking prediction, response coherence, and naturalness"
  - [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf)
