# In-context prediction
**Type:** Behavioral indicator  
**Supporting papers:** 17  
**Also known as:** Few-shot prediction, Many-shot in-context learning, Context-based prediction, One-shot adaptation  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage treats this behavior as making a prediction for a new test example or query from examples supplied in the prompt or support set. Most formulations describe the model as taking context examples together with the new input and then predicting the target output, sometimes in a formal sequence such as (x1, g(x1), ..., xn, g(xn), xt) to predict g(xt). Some authors frame the same behavior more explicitly as producing the correct output by using labels or other information present in the surrounding context, rather than stored associations, and as learning and generalizing from new information given in the input.

**Variants.** Papers study several named variants, most commonly few-shot prediction, many-shot in-context learning, context-based prediction, and one-shot adaptation. These variants differ mainly in how much support is provided and what is being predicted: a small support set for text or fitness prediction, a large in-context example set before a new query, or a single context trajectory from which the model infers dynamics and then predicts from a new initial condition. Some work also contrasts few-shot settings with zero-shot settings that use no support data.

**Space of elicitation and scores.** Papers link this behavior to 1 measurement instrument, HELMET. Papers say it is measured by HELMET, a long-context benchmark that includes many-shot in-context learning among its task categories, and a description specifies Accuracy for scoring that task. No other measurement instrument is linked.

**What it is taken as evidence of.** The linked construct relations are not measurement or causal claims. Instead, papers relate it to 2 constructs: In-context learning and Long-context understanding. The relation to In-context learning is phrased in terms of using labels in the context to make a prediction, while the relation to Long-context understanding comes from treating many-shot in-context learning as one of the tasks that require handling long-context inputs, so papers do not present a single dominant construct link.

## Sources

**In-context prediction** (1 paper: [Rethinking Invariance in In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/01e8ecf628f8d9f62a1fd433d44d34ab-Paper-Conference.pdf))
> The observable task of generating a prediction for a new test example based on a set of context examples provided in the input prompt.

**Few-shot prediction** (1 paper: [Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/03dfa2a7755635f756b160e9f4c6b789-Paper-Conference.pdf))
> The task of making predictions based on a small number of examples (shots) provided in the context or prompt.

**Many-shot in-context learning** (1 paper: [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf))
> The observable task of learning a new task from a large number of examples provided within the context and then applying that learned skill to a new query.

**Context-based prediction** (1 paper: [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf))
> Producing the correct output by using labels or information present in the surrounding context rather than relying on stored associations.

**One-shot adaptation** (1 paper: [Zebra: In-Context Generative Pretraining for Solving Parametric PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/serrano25a/serrano25a.pdf))
> The observable behavior of inferring the dynamics of a system and making predictions for a new query after being provided with only a single example trajectory from that system.

## Relationships

### In-context prediction →
- **HELMET** (measurement instrument): *measured_by*, 3 papers
  > we present HELMET (How to Evaluate Long-context Models Effectively and Thoroughly). We curate a diverse set of application-centric long-context tasks across seven categories. Beyond widely adopted categories like ... we also add many-shot in-context learning (ICL)
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)

### Associated with
- **In-context learning** (construct), 1 paper
  > The ICL class of functions H uses only labels in the context to make a prediction
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)
- **Long-context understanding** (construct), 1 paper
  > Handling long-context inputs is crucial for large language models (LLMs) in tasks such as extended conversations, document summarization, and many-shot in-context learning. (Section ABSTRACT)
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
