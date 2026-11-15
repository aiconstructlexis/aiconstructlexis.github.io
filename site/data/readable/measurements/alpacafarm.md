# AlpacaFarm
**Type:** Measurement instrument  
**Supporting papers:** 11  
**Also known as:** Alpacafarm  

## State of the Field

**What it is.** Most commonly, papers treat AlpacaFarm as an evaluation framework, benchmark, or dataset for open-ended instruction-following or conversation models. Across definitions, it is described as using human preference data and pairwise or model-based comparisons over model outputs, with content such as instructions, output pairs, demonstrations, and human preference annotations; some papers highlight a test set of 805 instructions, training and validation splits, and use of all 9.69k instructions, while a smaller line of work refers to the AlpacaFarm codebase or software framework for judging responses with a model evaluator.

**What it is claimed to measure.** Papers link AlpacaFarm to 2 constructs and 1 behavioral indicator. The named constructs are Helpfulness, where a paper uses its 805-instruction test set for assessing helpfulness, and Instruction following ability, where another paper uses the AlpacaFarm codebase to judge model responses; it is also reported as measuring Pairwise comparison, with one paper describing open-ended instruction-following benchmarks such as Alpacafarm as primarily relying on pairwise comparison.

**Space of uses.** In use, papers sample from multiple parts of AlpacaFarm, including randomly drawn instruction and output pairs, the first 1000 entries of its training split, a 200-instruction validation sample, and evaluations over another 1,000 instructions or all 9.69k instructions. Papers position it both as an open-ended instruction-following benchmark, sometimes alongside MT-Bench, LLMBar, and hh-rlhf, and as a resource for RLHF stages, reward model training, validation, and model-judged win-rate comparisons against reference outputs; no measurement instrument is linked to it.

**Concerns raised.** One paper notes low agreement between human annotators in AlpacaFarm, reporting 66% agreement.

## Sources

**AlpacaFarm** (7 papers: [Evaluating Large Language Models at Evaluating Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/afc8b034823271816d14f7c1aefe1dff-Paper-Conference.pdf), [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf), [Reward Model Ensembles Help Mitigate Overoptimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda7f9378a210c25e470e19304cce85d-Paper-Conference.pdf), [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf), [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf), [Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf), [Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment](https://aclanthology.org/2025.naacl-long.472.pdf))
> Evaluation framework for open-ended conversation models, using human or model-based comparisons to assess response quality and instructability.

**Alpacafarm** (1 paper: [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf))
> A benchmark for evaluating instruction-following models, which includes human preference annotations for pairwise comparisons.

## Relationships

### → AlpacaFarm
- **Helpfulness** (construct): *measured_by*, 1 paper
  > The first is the test set from AlpacaFarm (Dubois et al., 2023), which contains 805 instructions for assessing helpfulness. (Sec. 5.1)
  - [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf)
- **Instruction following ability** (construct): *measured_by*, 1 paper
  > We evaluate another 1,000 instructions and use the AlpacaFarm codebase (Dubois et al., 2024) to judge the responses from two models with GPT-4o. (Section 5.1)
  - [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)
- **Pairwise comparison** (behavioral indicator): *measured_by*, 1 paper
  > “open-ended instruction-following benchmarks (MT-Bench, Alpacafarm, and LLMBar), which primarily rely on pairwise comparison task.”
  - [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf)
