# LeetCode
**Type:** Measurement instrument  
**Supporting papers:** 3  
**Also known as:** Leetcode  

## State of the Field

**What it is.** Across the surveyed work, LeetCode is most commonly described as a collection of programming problems from the LeetCode platform or website. Some authors use it as a source for building code tasks, including fill-in-the-blank evaluations drawn from approximately 2,000 problems with Python, Java, and C++ solutions. A smaller line of work describes Leetcode as a benchmark of recent scraped problems, and another paper refers to it more generally as a coding benchmark.

**What it is claimed to measure.** Papers use it to measure one construct and one behavioral indicator. The reported links do not converge on a single target: it is used to measure code understanding in fill-in-the-blank code comprehension tasks, and it is also reported as measuring code generation, where one paper groups HumanEval and LeetCode 'for coding'.

**Space of uses.** No measurement instrument is linked to it. In practice, papers position it as part of a broader coding evaluation suite or as a problem source: one paper reports experiments on HumanEval, MBPP, APPS, CodeContests, and Leetcode, while another pairs HumanEval and LeetCode as coding evaluations.

**Concerns raised.** One paper foregrounds prior training exposure when using a recent scraped version, stating that the problems were chosen so that models released before July 2023 had not been trained on these data.

## Sources

**LeetCode** (2 papers: [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf), [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf))
> A platform providing a collection of coding problems, used as a source for creating fill-in-the-blank tasks.

**Leetcode** (1 paper: [SFS: Smarter Code Space Search improves LLM Inference Scaling](https://proceedings.iclr.cc/paper_files/paper/2025/file/387982dbf23d9975c7fc45813dd3dabc-Paper-Conference.pdf))
> A benchmark consisting of recent programming problems scraped from the Leetcode website, designed to test models on data they have not been trained on.

## Relationships

### → LeetCode
- **Code generation** (behavioral indicator): *measured_by*, 1 paper
  > ...HumanEval [4] and LeetCode [12] for coding... (Section 5.2)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
- **Code understanding** (construct): *measured_by*, 1 paper
  > "Fill in the Blank evaluates a model’s code comprehension ability... We collected approximately 2,000 coding problems from LeetCode"
  - [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf)
