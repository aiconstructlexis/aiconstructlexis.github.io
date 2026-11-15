# MIND
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across the descriptions, MIND is most commonly framed as a hallucination detection method that automatically labels data during detection to train a classifier. A smaller framing describes it as an unsupervised method: it truncates Wikipedia articles, prompts an LLM to continue the next sentence, and generates truth labels by matching named entities between the continuation and the original source text.

**What it is claimed to measure.** Papers describe MIND as serving hallucination detection, but no constructs and no behavioral indicators are linked to it.

**Space of uses.** The usage described in the papers centers on self-generated labeling rather than reliance on pre-annotated datasets. One account explicitly contrasts it with SAPLMA on that basis, and another describes a workflow built from truncated Wikipedia articles, next-sentence continuation, and named-entity matching to produce truth labels. No measurement instrument is linked to it.

## Sources

**MIND** (2 papers: [HD-NDEs: Neural Differential Equations for Hallucination Detection in LLMs](https://aclanthology.org/2025.acl-long.309.pdf), [Unsupervised Hallucination Detection by Inspecting Reasoning Processes](https://aclanthology.org/2025.emnlp-main.1124.pdf))
> A classification-based hallucination detection method that automatically labels data during detection to train its classifier.
