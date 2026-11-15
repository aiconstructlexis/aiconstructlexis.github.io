# Auto-J test set
**Type:** Measurement instrument  
**Supporting papers:** 3  
**Also known as:** Auto-J, AutoJ  

## State of the Field

**What it is.** Across the definitions, the prevailing usage treats Auto-J as a curated or automated judge benchmark. Papers describe it as a benchmark for meta-evaluation of LLM judges, and one definition also presents it as a benchmark for evaluating reward models, particularly by examining correlation with human expert judgments. A smaller line of description specifies "Auto-J (Eval-P test set with ties)," a pairwise evaluation benchmark that includes tie outcomes.

**What it is claimed to measure.** The descriptions say papers use Auto-J to evaluate LLM judges and reward models, with the most common framing centered on meta-evaluation of judges and a secondary framing centered on correlation with human expert judgments. Papers in this literature do not link it to any named constructs or behavioral indicators, so the record does not attach it to any explicitly named construct.

**Space of uses.** Where usage is described, one paper places AutoJ alongside RewardBench and MT-Bench as one of three reward model benchmarks. Another paper uses the tie-enabled version for pairwise evaluation, describing it as a way to test judge models on indeterminate comparisons.

**Concerns raised.** One paper notes that the benchmark's allowance for ties results in lower scores across judges.

## Sources

**Auto-J** (2 papers: [Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf), [Direct Judgement Preference Optimization](https://aclanthology.org/2025.emnlp-main.103.pdf))
> A curated benchmark for meta-evaluation of LLM judges.

**AutoJ** (1 paper: [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf))
> An automated judge benchmark used to evaluate reward models, particularly on their correlation with human expert judgments.
