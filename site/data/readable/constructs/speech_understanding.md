# Speech understanding
**Type:** Construct  
**Supporting papers:** 8  
**Also known as:** Linguistic comprehension  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats speech understanding as a latent ability to interpret the semantic content of spoken language in audio, including words, phrases, context, and, in some formulations, robustness across accents, noise, and longer inputs. A smaller line of work frames it as linguistic comprehension that is demonstrated by answering questions correctly, and some authors broaden the construct to following spoken instructions or to extracting speaker attributes and acoustic features alongside content. The clearest variation is scope: most definitions stay close to semantic or linguistic meaning in speech, while some extend the term toward instruction following or paralinguistic information.

**Space of facets.** Papers commonly organize speech understanding through tasks such as speech recognition, spoken question answering, and speech instruction following. One benchmark treats it as one of three evaluation aspects alongside audio scene understanding and voice understanding (paralinguistic), whereas another description says speech understanding involves extracting both linguistic and paralinguistic information from speech. These descriptions separate and combine paralinguistic content in different ways.

**Space of measurement.** Operationalization is fairly concentrated: papers link speech understanding to two measurement instruments, AudioBench and SUPERB, and to three behavioral indicators, speech recognition, speech instruction following, and spoken question answering. AudioBench is introduced as a universal benchmark whose evaluation targets speech understanding, and another paper says SUPERB focuses on speech understanding. At the task level, papers operationalize the construct through ASR accuracy on evaluation sets, instruction-based question answering pairs, and following unseen instructions for ASR and AST tasks, so the linked measures center on recognition, answering, and instruction following even when definitions also mention context, accents, noise, length, or paralinguistic information.

**Links.** Beyond measurement, one paper claims a causal relationship from speech understanding to speech recognition, while another paper reports speech understanding as related to speech recognition. Papers also relate speech understanding to spoken question answering, and relate speech instruction following to speech understanding. No correlational links are reported.

## Sources

**Speech understanding** (4 papers: [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf), [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf), [SIFT-50M: A Large-Scale Multilingual Dataset for Speech Instruction Fine-Tuning](https://aclanthology.org/2025.acl-long.681.pdf), [Freeze-Omni: A Smart and Low Latency Speech-to-speech Dialogue Model with Frozen LLM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25aw/wang25aw.pdf))
> The latent ability of a model to interpret the semantic content of spoken language in audio, including comprehension of words, phrases, and context across diverse conditions such as accents, noise, and length.

**Linguistic comprehension** (1 paper: [Understanding the Modality Gap: An Empirical Study on the Speech-Text Alignment Mechanism of Large Speech Language Models](https://aclanthology.org/2025.emnlp-main.262.pdf))
> The model’s ability to understand spoken language content well enough to answer questions correctly.

## Relationships

### Speech understanding →
- **Speech recognition** (behavioral indicator): *causes*, 2 papers
  > “ASR and AST are foundational tasks that enable the model to understand speech”
  - [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf)
  - [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf)
- **AudioBench** (measurement instrument): *measured_by*, 1 paper
  > We introduce AudioBench, a universal benchmark designed to evaluate Audio Large Language Models (AudioLLMs). It encompasses 8 distinct tasks and 26 datasets... The evaluation targets three main aspects: speech understanding, audio scene understanding, and voice understanding (paralinguistic).
  - [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf)
- **SUPERB** (measurement instrument): *measured_by*, 1 paper
  > SUPERB (Yang et al., 2021) focuses on speech understanding... (Section 5.1)
  - [Recent Advances in Speech Language Models: A Survey](https://aclanthology.org/2025.acl-long.682.pdf)

### Associated with
- **Spoken question answering** (behavioral indicator), 1 paper
  > 3.3.1 Speech Understanding ... Speech Question Answering (SQA).
  - [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf)
- **Speech instruction following** (behavioral indicator), 1 paper
  > 3.3.1 Speech Understanding ... Speech Instruction (SI).
  - [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf)
