# Speech classification
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Word identity prediction  

## State of the Field

**Space of definitions.** Across the papers, this behavior is described either as classifying an audio waveform of speech into a predefined set of categories or as word identity prediction, identifying a specific keyword or command from a spoken utterance. Across both formulations, the target is correct assignment of the spoken input to the relevant category, keyword, or command.

**Variants.** The named variants include raw speech classification with long sequences and word identity prediction. One paper studies the task on the SC10 subset of the Speech Commands dataset, while another places word identity prediction among tasks with several semantic difficulties and says word prediction is moderate in semantic difficulty.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead describe the task directly, including raw speech classification with long sequences and identification of a keyword or command from a spoken utterance.

**What it is taken as evidence of.** The only construct papers link it to is long-range dependency modeling, and the recorded link is a related one rather than a causal or correlational claim. In that usage, speech classification is used to evaluate the ability to learn long-range dependencies in real-world time-series data, and no other construct is linked to it.

## Sources

**Speech classification** (1 paper: [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf))
> The task of classifying an audio waveform of speech into a predefined set of categories.

**Word identity prediction** (1 paper: [Improving Semantic Understanding in Speech Language Models via Brain-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/95b7a93e60fdfd10cc202f44fd6adf5f-Paper-Conference.pdf))
> The task of identifying a specific keyword or command from a spoken utterance.

## Relationships

### Associated with
- **Long-range dependency modeling** (construct), 1 paper
  > To evaluate the ability to learn long-range dependencies in real-world time-series data, we conducted experiments on the speech classification task... (Appendix C.5)
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
