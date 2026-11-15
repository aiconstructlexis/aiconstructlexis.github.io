# CoVoST 2
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** CoVoST2, CoVoST-2  

## State of the Field

**What it is.** Across these papers, CoVoST 2 is most commonly described as a multilingual speech-to-text translation corpus or benchmark derived from Common Voice, used for training and evaluation. Definitions differ on the source-target setup: some describe English speech translated into multiple typologically diverse languages, with one use case noting 15,500 English examples into seven languages, while others focus on general-domain French-English and German-English subsets or on 14 non-English source languages paired bidirectionally with English for 28 directions. A smaller framing presents it as the speech translation source corpus used inside CoVoGER to generate N-best lists.

**What it is claimed to measure.** Papers link CoVoST 2 to one construct and two behavioral indicators. The prevailing usage is to measure speech translation, with papers stating that speech translation is tested on CoVoST 2 and reporting settings such as En-De or English-to-multiple-language translation; a smaller line of work also uses it to measure speech recognition in joint ASR and ST evaluation. Separately, one paper reports CoVoST 2 as measuring cross-lingual alignment, saying its results confirm superior cross-lingual alignment and translation performance, so the measurement claims are mostly concentrated on translation with narrower links to speech recognition and cross-lingual alignment.

**Space of uses.** Papers link CoVoST 2 to one other measurement instrument, CoVoGER, and describe that relation by saying CoVoGER is constructed by decoding speech from CoVoST-2 for speech translation. Other papers use CoVoST2 alongside MuST-C and MSLT, either by collecting tailored data from their training and test splits or by testing speech-to-text recognition and translation on MuST-C v1.0 and CoVoST2 together. Across these uses, papers position it both as a benchmark for reporting speech translation results and as a source corpus within broader evaluation setups.

## Sources

**CoVoST 2** (1 paper: [Distilling an End-to-End Voice Assistant Without Instruction Training Data](https://aclanthology.org/2025.acl-long.388.pdf))
> A benchmark dataset for evaluating speech-to-text translation, containing English speech examples to be translated into multiple typologically diverse languages.

**CoVoST2** (1 paper: [Locate-and-Focus: Enhancing Terminology Translation in Speech Language Models](https://aclanthology.org/2025.acl-long.556.pdf))
> A large-scale multilingual speech-to-text translation corpus (Common Voice Speech-to-Text) used for training and evaluating speech translation models.

**CoVoST-2** (1 paper: [CoVoGER: A Multilingual Multitask Benchmark for Speech-to-text Generative Error Correction with Large Language Models](https://aclanthology.org/2025.emnlp-main.320.pdf))
> A multilingual speech-to-text translation corpus derived from Common Voice, used in the CoVoGER benchmark to generate N-best lists for 28 source-target language directions.

## Relationships

### → CoVoST 2
- **Speech translation** (behavioral indicator): *measured_by*, 4 papers
  > “En2Zh CoVoST2-En2Zh ...”
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
  - [Prepending or Cross-Attention for Speech-to-Text? An Empirical Comparison](https://aclanthology.org/2025.naacl-long.153.pdf)
  - [Distilling an End-to-End Voice Assistant Without Instruction Training Data](https://aclanthology.org/2025.acl-long.388.pdf)
  - [Soundwave: Less is More for Speech-Text Alignment in LLMs](https://aclanthology.org/2025.acl-long.917.pdf)
- **Speech recognition** (behavioral indicator): *measured_by*, 1 paper
  > testing speech-to-text recognition (ASR) and translation (ST) on MuST-C v1.0 and CoVoST2 datasets. (Abstract)
  - [Prepending or Cross-Attention for Speech-to-Text? An Empirical Comparison](https://aclanthology.org/2025.naacl-long.153.pdf)
- **Cross-lingual alignment** (construct): *measured_by*, 1 paper
  > These results confirm Audio-Reasoner’s superior cross-lingual alignment and translation performance. (Section 4.2, referring to CoVoST 2 results in Table 5)
  - [Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.1216.pdf)

### Associated with
- **CoVoGER** (measurement instrument), 1 paper
  > “To construct the COVOGER benchmark, we decode speech from two large-scale public datasets, Common Voice 20.0 for ASR and CoVoST-2 ... for ST.”
  - [CoVoGER: A Multilingual Multitask Benchmark for Speech-to-text Generative Error Correction with Large Language Models](https://aclanthology.org/2025.emnlp-main.320.pdf)
