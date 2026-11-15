# Last letter concatenation
**Type:** Measurement instrument  
**Supporting papers:** 7  
**Also known as:** LLC, LastLetter, Last Letter Concatenation, LastLetterConcatenation, LastLetterConcat  

## State of the Field

**What it is.** Across papers, the prevailing description is a benchmark, dataset, or test set in which a model concatenates the last letters of words in a name or other word sequence. Most definitions frame it as a symbolic reasoning task, while some describe it more narrowly as a simple text-processing or string-manipulation task; one definition also says it is used to evaluate algorithmic reasoning and length generalization in verification settings. Examples in the quoted passages ask for the last letters of names such as "Amy Brown" or "Craig Alice," and some papers specify four-word or four-name inputs.

**What it is claimed to measure.** Papers link it to 2 constructs and no behavioral indicators. It is most commonly reported as measuring Symbolic reasoning, with papers saying they use Last Letter Concatenation to examine or benchmark symbolic reasoning performance. A smaller line of work uses it to measure Reasoning more broadly, describing it as one of the standard reasoning datasets, so the recorded claims center on Symbolic reasoning with an additional broader reasoning use.

**Space of uses.** Papers usually use it as one benchmark among several, appearing alongside GSM8K, CSQA, and Coin Flip in broader reasoning evaluations. It is positioned as a benchmark test set for reporting accuracies, as a reasoning dataset for average performance reporting, and as a task leveraged to examine a method's symbolic reasoning performance.

## Sources

**LLC** (1 paper: [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf))
> Last Letter Concatenation, a reasoning task and dataset where the model must concatenate the last letters of words in a given name.

**LastLetter** (1 paper: [Self-Guiding Exploration for Combinatorial Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb9120be0dcaac0aec66d2e75deb69dd-Paper-Conference.pdf))
> A benchmark test set used to evaluate symbolic reasoning performance.

**Last Letter Concatenation** (1 paper: [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf))
> A string-manipulation benchmark used to evaluate algorithmic reasoning and length generalization in verification settings.

**Last letter concatenation** (1 paper: [Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf))
> A symbolic reasoning task used to test whether a model can follow letter-based transformation rules across inputs.

**LastLetterConcatenation** (1 paper: [Chain of Thoughtlessness? An Analysis of CoT in Planning](https://proceedings.neurips.cc/paper_files/paper/2024/file/3365d974ce309623bd8151082d78206c-Paper-Conference.pdf))
> A text-processing benchmark where the model concatenates the last letters of a sequence of words.

**LastLetterConcat** (1 paper: [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf))
> A dataset for evaluating symbolic reasoning where the task is to concatenate the last letters of a sequence of words.

## Relationships

### → Last letter concatenation
- **Symbolic reasoning** (construct): *measured_by*, 5 papers
  > For symbolic reasoning, we use Last Letter Concatenation and Coin Flip from Wei et al. (2022).
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
  - [Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > Our evaluations on standard reasoning datasets (GSM8K, CSQA, and LLC) with various LLMs and prompts show that TREACLE enables cost savings of up to 85% compared to baselines, while maintaining high accuracy. (Abstract)
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
