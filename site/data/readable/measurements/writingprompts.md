# WritingPrompts
**Type:** Measurement instrument  
**Supporting papers:** 10  

## State of the Field

**What it is.** Across definitions, WritingPrompts is treated as a story-writing or story-generation dataset featuring creative stories from Reddit's writing prompts forum. Papers also describe it as a language modeling evaluation dataset; in one use, models are given the story topic as the prompt for generating a narrative, while another paper treats it as a benchmark corpus and test-data source for sentence-level AI-generated text detection.

**What it is claimed to measure.** In the recorded measurement links, papers use WritingPrompts to measure one construct, Language modeling ability, and one behavioral indicator, Story generation. The stated measurement role is therefore concentrated on those two targets rather than spread across many constructs or indicators.

**Space of uses.** Papers use WritingPrompts in several roles: as one of multiple corpora in broader evaluation, as training data for fine-tuning on story telling, and as a source corpus for constructing and testing sentence-level AI-generated text detection data. Quoted passages place it alongside XSum or XSUM and SQuAD, including a report of averaging AUROCs across XSum, SQuAD, and WritingPrompts; no other measurement instrument is linked to it through the recorded relationships.

## Sources

**WritingPrompts** (4 papers: [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf), [Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf), [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf), [SenDetEX: Sentence-Level AI-Generated Text Detection for Human-AI Hybrid Content via Style and Context Fusion](https://aclanthology.org/2025.emnlp-main.268.pdf))
> A dataset for language modeling evaluation featuring creative stories from the writing prompts forum of Reddit.

## Relationships

### → WritingPrompts
- **Language modeling ability** (construct): *measured_by*, 1 paper
  > We use 6 English textual corpora from 5 different domains for comprehensive evaluation... (4) WritingPrompts (Fan et al., 2018) features text from the writing prompts forum of Reddit. (Section 4.1.1)
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **Story generation** (behavioral indicator): *measured_by*, 1 paper
  > "(II) Story-telling: We also fine-tune LLaMa2 on the story-generation dataset WritingPrompts"
  - [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf)
