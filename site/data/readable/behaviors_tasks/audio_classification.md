# Audio classification
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Sound classification  

## State of the Field

**Space of definitions.** Most papers treat audio classification as assigning an audio clip to a sound category or label. The prevailing formulation is that the clip is assigned one or more predefined labels, and one paper specifies category types such as sound events, genre, or speaker-related classes. A smaller line of work uses the name sound classification and describes assigning sound clips to semantic categories, and one paper notes that outputs may be label names or descriptions in text form rather than label indices.

**Variants.** Papers use both audio classification and sound classification, and they often place it alongside captioning within broader auditory task suites or audio classification benchmarks. The studied category sets include sound events, genre, and speaker-related classes, and one paper specifically reports sound classification on the ESC-50 dataset using tokenizer-derived representations.

**Space of elicitation and scores.** Only one measurement instrument is linked to audio classification: FSD50K. One paper measures it with FSD50K and reports the result as "FSD50k CLS - mAP," and no other instrument is linked.

**What it is taken as evidence of.** No construct is linked to audio classification, so the papers do not explicitly treat it as evidence of any construct.

## Sources

**Audio classification** (3 papers: [Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf), [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf), [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf))
> Assigning an audio clip to a sound category or label.

**Sound classification** (1 paper: [ALMTokenizer: A Low-bitrate and Semantic-rich Audio Codec Tokenizer for Audio Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25q/yang25q.pdf))
> Assigning sound clips to semantic categories using tokenizer-derived representations.

## Relationships

### Audio classification →
- **FSD50K** (measurement instrument): *measured_by*, 1 paper
  > FSD50k CLS - mAP (Table 1)
  - [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf)
