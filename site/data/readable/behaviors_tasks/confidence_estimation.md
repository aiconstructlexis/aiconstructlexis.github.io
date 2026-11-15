# Confidence estimation
**Type:** Behavioral indicator  
**Supporting papers:** 43  
**Also known as:** Probability estimation, Confidence Expression, Expressing uncertainty, Confidence score generation, Step correctness prediction, Verbalized confidence, Nuanced uncertainty expression, Linguistic uncertainty expression, Natural language uncertainty expression, Self-knowledge estimation, Uncertainty estimation, Self-evaluation  

## State of the Field

**Space of definitions.** Most papers describe this behavior as producing a confidence signal about an output, usually a numerical score or probability for whether an answer, claim, reasoning step, diagnostic decision, or a judge model's judgment is correct or aligned with human preferences. A smaller line of work treats the same behavior as explicit verbal or linguistic uncertainty, using hedges such as I am unsure or I am not sure but. Success is usually framed as tracking correctness or agreement, though papers vary in whether the target is answer correctness, step-rightness, factual correctness, or agreement with human preferences.

**Variants.** The literature studies this behavior at several granularities and gives it several nearby names. Common labels include probability estimation, step correctness prediction, self-knowledge estimation, verbalized confidence, and linguistic uncertainty expression, alongside other naming variants. It appears in judge models, classification and question answering settings, reasoning tasks, and diagnostic decision making, with signals attached to whole answers, individual reasoning steps, or token, sequence, and claim levels.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead elicit or score it directly by asking for probability scores, percentages, confidence in linguistic form, or class-wise values between 0.00 and 100.00, and by deriving confidence from token probabilities, token-span aggregation, agreement ratios between simulations, perplexity, token entropy, or internal states.

**What it is taken as evidence of.** Papers connect confidence estimation to six constructs rather than treating it as evidence of a single one. Calibration is the most common linked construct: some papers claim a causal relationship from confidence estimation to Calibration, while others relate the two. Trustworthiness is the next most common link, again with both causal and related claims, while smaller lines of work relate confidence estimation to Knowledge boundary awareness, Overconfidence, and Reasoning, and one paper reports that it correlates with Representational stability.

## Sources

**Confidence estimation** (4 papers: [Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf), [MAC-Tuning: LLM Multi-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.35.pdf), [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf), [SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fa1edbc195336e29893cdae0939e495f-Paper-Conference.pdf))
> The model generates a numerical score representing its certainty that its judgment aligns with human preferences.

**Probability estimation** (1 paper: [BIRD: A Trustworthy Bayesian Inference Framework for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/19452e14fe6e0a8ac00410f1eebcbded-Paper-Conference.pdf))
> The observable act of assigning a numerical probability or confidence score to a potential outcome given a context.

**Confidence Expression** (1 paper: [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf))
> Providing probability estimates or confidence levels for predictions, often by verifying if a predicted answer is correct via token probability.

**Expressing uncertainty** (2 papers: [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf), [Humanizing Machines: Rethinking LLM Anthropomorphism Through a Multi-Level Framework of Design](https://aclanthology.org/2025.emnlp-main.164.pdf))
> The observable behavior of a model explicitly stating its lack of confidence or knowledge in its response, such as by outputting phrases like 'I am unsure'.

**Confidence score generation** (1 paper: [Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8b78c39a262ea563ee51d2f6dba3b04-Paper-Conference.pdf))
> The action of producing numerical confidence values for each potential class in a classification task, expressed within a natural language response.

**Step correctness prediction** (1 paper: [Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens](https://aclanthology.org/2025.emnlp-main.171.pdf))
> The observable task of assigning a confidence score to each reasoning step indicating whether it is correct or incorrect, based on internal model states.

**Self-evaluation** (1 paper: [Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens](https://aclanthology.org/2025.emnlp-main.171.pdf))
> The observable behavior of an LLM producing internal confidence signals about its own reasoning steps without external feedback.

**Verbalized confidence** (1 paper: [Thinking Out Loud: Do Reasoning Models Know When They're Right?](https://aclanthology.org/2025.emnlp-main.73.pdf))
> The observable expression of a model's certainty in its answer, typically in the form of a percentage or probability statement.

**Nuanced uncertainty expression** (1 paper: [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf))
> The generation of text that qualifies an answer with expressions of doubt or uncertainty, such as "I am not sure but..." or "maybe".

**Linguistic uncertainty expression** (1 paper: [MetaFaith: Faithful Natural Language Uncertainty Expression in LLMs](https://aclanthology.org/2025.emnlp-main.1505.pdf))
> The observable use of words, phrases, and hedging language to convey a degree of confidence or doubt in a generated response.

**Self-knowledge estimation** (1 paper: [Will It Still Be True Tomorrow? Multilingual Evergreen Question Classification to Improve Trustworthy QA](https://aclanthology.org/2025.emnlp-main.434.pdf))
> The observable task of assigning a score to a model's own generated answer that reflects the model's confidence in its factual correctness, framed as a binary classification problem.

**Uncertainty estimation** (1 paper: [Will It Still Be True Tomorrow? Multilingual Evergreen Question Classification to Improve Trustworthy QA](https://aclanthology.org/2025.emnlp-main.434.pdf))
> The model's generation of confidence or uncertainty signals (e.g., perplexity, token entropy) in response to input questions, used to infer implicit awareness of evergreen-ness.

**Confidence scoring** (1 paper: [Knowledge-Aware Co-Reasoning for Multidisciplinary Collaboration](https://aclanthology.org/2025.emnlp-main.687.pdf))
> Assigning a numerical confidence level to a diagnostic decision based on factual consistency and evidence from a reasoning subgraph.

## Relationships

### Confidence estimation →
- **Calibration** (construct): *causes*, 3 papers
  > Bayesian methods, with their inherent ability to estimate uncertainty, serve as potent tools to mitigate overconfidence and enhance calibration. (Section ABSTRACT)
  - [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf)
  - [Zero-shot Model-based Reinforcement Learning using Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf)
  - [Calibration Across Layers: Understanding Calibration Evolution in LLMs](https://aclanthology.org/2025.emnlp-main.742.pdf)
- **Trustworthiness** (construct): *causes*, 2 papers
  > In this work, we introduce model-internal confidence estimators (MICE), which improve the trustworthiness and safety of language models as tool-calling agents. (Section 8)
  - [MICE for CATs: Model-Internal Confidence Estimation for Calibrating Agents with Tools](https://aclanthology.org/2025.naacl-long.615.pdf)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Representational stability** (construct): *correlates*, 1 paper
  > We hypothesize that an LLM’s confidence correlates with the robustness of its internal states; specifically, the final hidden states that lead to the tokens of a high-confidence answer should exhibit greater stability when subjected to targeted perturbations. (Section 3)
  - [Calibrating LLM Confidence by Probing Perturbed Representation Stability](https://aclanthology.org/2025.emnlp-main.530.pdf)

### Associated with
- **Overconfidence** (construct), 1 paper
  > The performance of Med-LVLMs in uncertainty estimation is unsatisfactory, revealing a poor understanding of their medical knowledge limits. Additionally, these models tend to exhibit overconfidence, thereby increasing the risk of misdiagnoses. (Sec 1)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Knowledge boundary awareness** (construct), 1 paper
  > While assessing capability-aware solvability of LLMs is underexplored, confidence or uncertainty estimation (Geng et al., 2024; Wen et al., 2024) offers a viable alternative.
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)
- **Reasoning** (construct), 1 paper
  > "we propose a set of training-free, graph-based confidence estimation methods tailored to reasoning tasks."
  - [All Roads Lead to Rome: Graph-Based Confidence Estimation for Large Language Model Reasoning](https://aclanthology.org/2025.emnlp-main.1620.pdf)
