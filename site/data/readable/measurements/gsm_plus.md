# GSM-Plus
**Type:** Measurement instrument  
**Supporting papers:** 9  
**Also known as:** GSM-PLUS, GSMplus  

## State of the Field

**What it is.** Across the papers, GSM-Plus is most commonly described as an adversarial version or extension of GSM8K for grade-school math evaluation. Definitions converge on a benchmark or test suite of grade-school or grade-level math problems, with the dominant emphasis on being more challenging and on testing robustness or "resilience to adversarial perturbations," though one paper describes it more simply as a held-out set for mathematical reasoning.

**What it is claimed to measure.** Papers link GSM-Plus to three constructs and one behavioral indicator. The prevailing measurement claims are mathematical reasoning and mathematical problem solving, and smaller lines of work report it as measuring robustness and verification ability; one paper explicitly says it "tests model robustness." Overall, papers use it for several related math-performance targets rather than only one construct.

**Space of uses.** Papers typically use GSM-Plus alongside other math evaluations, especially GSM8k, MATH, SVAMP, ASDiv, and TheoremQA. In those uses it is positioned variously as a grade-school math benchmark, a robustness benchmark, and a held-out test set, with one paper noting that for robustness benchmarks it uses the original evaluation scripts with GPT-4o.

## Sources

**GSM-Plus** (3 papers: [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf), [ThinkSLM: Towards Reasoning in Small Language Models](https://aclanthology.org/2025.emnlp-main.1659.pdf), [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf))
> An adversarial version of the GSM8k benchmark, designed to be more challenging and test the robustness of a model's mathematical reasoning.

**GSM-PLUS** (1 paper: [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf))
> The GSM-PLUS benchmark, an extension of GSM8K, used to evaluate mathematical reasoning on grade-school math problems.

**GSMplus** (1 paper: [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf))
> A test suite of grade-level math problems used as a held-out set for evaluating mathematical reasoning.

## Relationships

### → GSM-Plus
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 2 papers
  > ...GSM-Plus [18], MATH, TheoremQA [6], SVAMP [28], and ASDiv [22] for math. (Section 5.2)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
  - [Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 2 papers
  > The model’s performance is evaluated on two grade school math benchmarks: GSM8k (Cobbe et al., 2021) and GSM-Plus (Li et al., 2024), which is an adversarial version of GSM8k. (Section 4.4)
  - [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > GSM-Plus, which tests model robustness. (Section 4.4)
  - [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **Verification ability** (construct): *measured_by*, 1 paper
  > “The test corpus includes 128 solutions for each question from GSM-Plus (Li et al., 2024) and MATH500 (Hendrycks et al., 2021) datasets.”
  - [Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf)
