# Prompt sensitivity
**Type:** Construct  
**Supporting papers:** 31  
**Also known as:** Prompt brittleness, Instruction sensitivity, Response consistency, Stylistic self-consistency, Robustness to spurious features, Sensitivity  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats prompt sensitivity as variation in a model's performance, outputs, predictions, or output distributions when prompts are reworded, reformatted, or reordered without changing their meaning. Most definitions center on semantically similar prompts or identical instructions, while narrower versions focus on formatting, verbalizers, example choice, or example order, and one survey narrows it further to whether known knowledge can be successfully verified only under certain prompt forms. A smaller line defines it specifically as changes in predicted class distributions across prompt rephrasings, without requiring access to ground truth, while another closely related framing emphasizes maintaining stable performance under irrelevant or meaning-preserving prompt variations such as formatting.

**Space of facets.** Papers use several nearby labels, including prompt brittleness, instruction sensitivity, response consistency, stylistic self-consistency, and robustness to spurious features. Some papers frame the phenomenon on the input side, as sensitivity to wording, detail, formatting, or order, while another frames instruction-induced accuracy fluctuations as differences in response consistency, meaning structurally, lexically, and logically stable outputs across prompt styles, with Cross-Response Similarity used for stylistic self-consistency. The terminology is not uniform: the label "sensitivity" is also used elsewhere for metric error detection, word-level importance in text classifiers, and the bit-flip behavior of functions.

**Space of measurement.** Prompt sensitivity is linked to 2 measurement instruments, LLM-as-a-judge and TREC, and no behavioral indicator is linked to it. In use, papers operationalize it by creating semantically equivalent prompt or instruction variants and comparing predicted class distributions, task performance, output distributions, or cross-response similarity: examples include normalized entropy over rephrasings without ground truth, standard deviation over instruction orderings, token-probability and discrete-choice metrics across task formats, and Cross-Response Similarity for stylistic self-consistency. Most of these measurements follow the dominant definitions by varying prompts while holding semantics fixed and then tracking changes in predictions or responses, while a smaller subset scores response stability or successful knowledge verification under different prompt forms.

**Links.** Among linked constructs, one paper states that prompt robustness is related to prompt sensitivity, noting that sensitivity can be used to compare the "robustness" of different LLMs to prompt variation. Another paper reports that prompt sensitivity correlates with selection bias, suggesting that a model weak on selection bias also tends to change its output across different prompt templates.

## Sources

**Prompt brittleness** (1 paper: [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf))
> The tendency of model predictions to change substantially under small changes in prompt formatting, verbalizers, example choice, or example order.

**Prompt sensitivity** (6 papers: [Motif: Intrinsic Motivation from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/a8de97fa77a09258b22880c230a83445-Paper-Conference.pdf), [Task Me Anything](https://proceedings.neurips.cc/paper_files/paper/2024/file/237ffa9a473eff1c66d085dba7f813ba-Paper-Datasets_and_Benchmarks_Track.pdf), [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf), [Knowledge Boundary of Large Language Models: A Survey](https://aclanthology.org/2025.acl-long.256.pdf), [Position: Contextual Integrity is Inadequately Applied to Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shvartzshnaider25a/shvartzshnaider25a.pdf), [Measuring Bias or Measuring the Task: Understanding the Brittle Nature of LLM Gender Biases](https://aclanthology.org/2025.emnlp-main.342.pdf))
> The tendency for a model's performance and output to vary based on different wordings of a prompt, even when the prompts are semantically similar.

**Instruction sensitivity** (2 papers: [What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf), [RCScore: Quantifying Response Consistency in Large Language Models](https://aclanthology.org/2025.emnlp-main.290.pdf))
> The degree to which a model's performance is affected by variations in the textual phrasing or ordering of an instruction, even when the semantic meaning is identical.

**Response consistency** (1 paper: [RCScore: Quantifying Response Consistency in Large Language Models](https://aclanthology.org/2025.emnlp-main.290.pdf))
> The degree to which a model produces structurally, lexically, and logically stable outputs across different instruction styles for the same underlying task.

**Stylistic self-consistency** (1 paper: [RCScore: Quantifying Response Consistency in Large Language Models](https://aclanthology.org/2025.emnlp-main.290.pdf))
> A model's ability to generate outputs that are stylistically similar to each other when responding to the same problem presented with varied instructions.

**Robustness to spurious features** (1 paper: [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf))
> The ability of a model to maintain stable performance despite the presence of irrelevant or meaning-preserving variations in the input, such as prompt formatting.

**Sensitivity** (4 papers: [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf), [SMAB: MAB based word Sensitivity Estimation Framework and its Applications in Adversarial Text Generation](https://aclanthology.org/2025.naacl-long.463.pdf), [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf), [Lower Bounds for Chain-of-Thought Reasoning in Hard-Attention Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bavandpour25a/bavandpour25a.pdf))
> The degree to which an LLM's predicted class distribution changes across semantically equivalent rephrasings of the prompt, reflecting its instability to input variations independent of ground truth.

## Relationships

### Prompt sensitivity →
- **TREC** (measurement instrument): *measured_by*, 1 paper
  > “Figure 2: Predicted class distributions over prompt rephrasings pτ across three samples of the same class Person (TREC dataset, Section 4).”
  - [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > To rigorously assess whether LLMs truly suffer from prompt sensitivity, we revisit this issue using a more robust evaluation strategy: LLMs as judges.
  - [Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs](https://aclanthology.org/2025.emnlp-main.1006.pdf)
- **Selection bias** (construct): *correlates*, 1 paper
  > This suggests that a model weak on selection bias also tends to change its output for different prompt templates. (Section 7.1)
  - [Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?](https://aclanthology.org/2025.emnlp-main.7.pdf)

### Associated with
- **Prompt robustness** (construct), 1 paper
  > The sensitivity should be used, for instance, as a guide to compare the “robustness” of different LLMs to variations of the prompt. (Section 3)
  - [What Did I Do Wrong? Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering](https://aclanthology.org/2025.naacl-long.73.pdf)
