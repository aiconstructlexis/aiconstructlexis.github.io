# SORRY-Bench
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** SORRY-bench, Sorry-Bench, SorryBench  

## State of the Field

**What it is.** Across definitions, the prevailing usage treats SORRY-Bench as a benchmark dataset of unsafe or harmful prompts and instructions for evaluating model refusal, safety alignment, or harmfulness. Papers variously describe it as a dataset of unsafe prompts used to evaluate and train models, a harmfulness benchmark in the HarmfulQA context, a jailbreak evaluation benchmark, and a dataset for assessing whether an LLM rejects questions with harmful intent. Its content is described as 450 harmful instructions, with one definition adding that the prompts span 45 categories and another referring to 450 unseen harmful test sets.

**What it is claimed to measure.** Papers connect SORRY-Bench to 1 construct and 3 behavioral indicators. It is used to measure Safety, and the named behavioral indicators, in the order most frequently linked, are Harmful content generation, Harmful request refusal, and Jailbreaking. The measurement language varies across papers, including "text-only safety," "LLM safety refusal," and "harmfulness in the HarmfulQA context."

**Space of uses.** Papers use SORRY-Bench both as an evaluation benchmark and as source material for derived datasets. It appears alongside HEx-PHI and WildJailbreak in harmfulness or text-only safety evaluation, and alongside SALAD-Bench in jailbreaking evaluation; other work uses its unsafe prompts to build a preference dataset or combines it with Alpaca to create D+ and D-. Papers also position it as one of several established benchmarks for rejecting harmful-intent questions.

## Sources

**SORRY-Bench** (2 papers: [Unintentional Unalignment: Likelihood Displacement in Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf), [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf))
> A dataset of unsafe prompts used to evaluate and train models for safety alignment and refusal capabilities.

**SORRY-bench** (1 paper: [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf))
> A benchmark for evaluating harmfulness in the HarmfulQA context using harmful instructions and model compliance.

**Sorry-Bench** (1 paper: [Programming Refusal with Conditional Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf))
> A benchmark dataset containing harmful prompts across 45 categories, used to evaluate a model's refusal capabilities for unsafe content.

**SorryBench** (1 paper: [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf))
> A benchmark dataset used to assess an LLM's ability to reject questions with harmful intent.

## Relationships

### → SORRY-Bench
- **Safety** (construct): *measured_by*, 1 paper
  > For text-only safety, we use SorryBench (Xie et al., 2024) and WildJailbreak (Jiang et al., 2024) (Section 3.3)
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **Harmful request refusal** (behavioral indicator): *measured_by*, 1 paper
  > we identify three deficiencies underlying these existing evaluations, and address them with SORRY-Bench2, our proposed systematic benchmark to evaluate LLM safety refusal. (Section 1)
  - [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf)
- **Harmful content generation** (behavioral indicator): *measured_by*, 1 paper
  > HEx-PHI and SORRY-bench are two dedicated benchmarks for evaluating harmfulness in the HarmfulQA context. (Section 2.2)
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
- **Jailbreaking** (behavioral indicator): *measured_by*, 1 paper
  > To assess the generalizability of the weak-to-strong attack, we expanded our evaluation to include two new safety benchmarks: SALAD-Bench (Li et al., 2024) and SORRY-Bench (Xie et al., 2024). (Section 5.1)
  - [Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf)
