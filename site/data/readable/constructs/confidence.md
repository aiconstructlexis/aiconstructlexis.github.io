# Confidence
**Type:** Construct  
**Supporting papers:** 27  
**Also known as:** Model confidence, Prediction confidence  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats confidence as the model's own certainty about an answer, judgment, or generated response. Most definitions describe an internal assessment of whether a response is correct and whether the model should answer, abstain, or seek more information, while one paper narrows it to the likelihood that a judgment will align with human preference. A smaller line of work defines the same construct through observable signals of certainty, including consistency across multiple generations, token probabilities during generation, stability of outputs and embedding dynamics, or variance in perplexity across choices.

**Space of facets.** Rather than a shared subtype system, papers mostly use adjacent labels such as model confidence and prediction confidence for closely related notions of certainty. They attach confidence to different reference objects, including answer correctness, human agreement, causal relations, and generated instructions, and they distinguish between confidence that is verbalized or self-assessed by the model and confidence inferred from token probabilities, entropy, stability, or repeated generations. Papers do not link confidence to any other constructs here.

**Space of measurement.** Papers link confidence to 2 measurement instruments and 3 behavioral indicators, with no linked constructs. The named instruments are Verbalized confidence, introduced as one of the existing confidence measures, and WikiText, used in one paper "to assess the model's prediction confidence"; beyond these, papers operationalize confidence with token-level probabilities or their product, the proportion of generations affirming a correct causal relation, output stability and embedding dynamics, average token distribution entropy, and variance in perplexity scores across answer choices. Most operationalizations make certainty explicit, but they extract it from different observable signals rather than a single common procedure.

**Links.** In the recorded relationships, papers use related links rather than causal or correlational ones. Abstention is related to confidence, with one paper stating that an Abstention Module evaluates the expert system's confidence level; confidence is also related to hallucination, including "nonfactual responses with unwarranted confidence," and to self-evaluation, where one paper defines confidence from the score and probability of the token produced by the model to self-evaluate. Confidence is also recorded as being measured by Verbalized confidence and WikiText.

## Sources

**Confidence** (4 papers: [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf), [Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf), [On the Reliability of Large Language Models for Causal Discovery](https://aclanthology.org/2025.acl-long.471.pdf), [TurnBack: A Geospatial Route Cognition Benchmark for Large Language Models through Reverse Route](https://aclanthology.org/2025.emnlp-main.440.pdf))
> The model's internal assessment of its certainty in providing a correct answer, used to decide whether to answer or seek more information.

**Model confidence** (3 papers: [Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://aclanthology.org/2025.acl-long.276.pdf), [Token Signature: Predicting Chain-of-Thought Gains with Token Decoding Feature in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ci/liu25ci.pdf), [Improving Task Diversity in Label Efficient Supervised Finetuning of LLMs](https://aclanthology.org/2025.emnlp-main.1093.pdf))
> The degree to which a model's internal representations reflect certainty in its predictions, inferred from stability of outputs and embedding dynamics.

**Prediction confidence** (1 paper: [Streamlining Redundant Layers to Compress Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4b00a351b41358965613c118e87dc28c-Paper-Conference.pdf))
> The degree to which a model is certain about its predictions, operationally measured by the variance in perplexity scores across different choices for a given question.

## Relationships

### Confidence →
- **WikiText** (measurement instrument): *measured_by*, 1 paper
  > "WikiText (Merity et al., 2022) to assess the model’s prediction confidence" (Section 5.1, Datasets)
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)
- **Verbalized confidence** (measurement instrument): *measured_by*, 1 paper
  > We first consider two types of existing confidence measure—... (2) verbalized confidence
  - [Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > generating nonfactual responses with unwarranted confidence. (Section 1)
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
- **Abstention** (behavioral indicator), 1 paper
  > The goal of the Abstention Module is to evaluate the confidence level of the Expert system
  - [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf)
- **Self-evaluation** (behavioral indicator), 1 paper
  > We define confidence by utilizing the score and the probability of the token responded by the LLM to self-evaluate.
  - [Enhancing Graph Of Thought: Enhancing Prompts with LLM Rationales and Dynamic Temperature Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/c87245c9e8882bc1b6d4ec343d430e71-Paper-Conference.pdf)
