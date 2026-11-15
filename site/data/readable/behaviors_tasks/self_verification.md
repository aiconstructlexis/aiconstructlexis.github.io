# Self-verification
**Type:** Behavioral indicator  
**Supporting papers:** 19  
**Also known as:** Answer verification, Double-checking  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is a model checking a previously generated answer, solution, or reasoning process for correctness or reliability. Papers differ in what counts as a successful check: some use code to test the answer, some compare answers from different prompts and accept the result only when they match, and some assess whether the output is consistent with context or other evidence. AutoMix: Automatically Mixing Language Models describes it as estimating the reliability of the model's own outputs; a smaller line of work treats it as double-checking by generating a second solution, and some papers connect failed verification to reviewing, adjusting, or self-correcting the output.

**Variants.** Papers use several names, most often answer verification, and also self-verification and double-checking. The behavior appears in math word problems with code-based checking, dialogue-related or context-grounded reasoning where verification is framed as entailment, multimodal long-context document understanding where responses are cross-checked with complementary sources, and reasoning setups that reattempt the problem after a failed check. Related settings mentioned by papers include table question answering, binary decision tasks such as yes-no QA, and Game of 24.

**Space of elicitation and scores.** Only one measurement instrument is linked to it, Game of 24, and that paper reports the link as related rather than saying the behavior is measured by the instrument. In practice, papers elicit or score the behavior with zero-shot or few-shot prompting, code execution, agreement checks across prompts, entailment-style verification, reviewer agents that cross-verify with complementary sources, and labels such as Correct, Incorrect, and Invalid. One paper also describes reviewing and adjusting the solution path when code-based verification returns False, and another line of work gives unsupervised feedback by checking whether a completed continuation matches the original trajectory.

**What it is taken as evidence of.** Papers link it to six constructs: calibration, context faithfulness, metacognition, reasoning, and reliability, plus one other construct. Most of these construct links are recorded as related, while one paper claims a causal relationship from self-verification to reliability. The recorded construct links thus span several labels rather than a single named construct.

## Sources

**Answer verification** (2 papers: [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf), [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf))
> The observable behavior of generating and executing a specific procedure, typically code-based, to check the validity of a previously derived answer.

**Self-verification** (1 paper: [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf))
> The observable process where a model assesses the correctness or reliability of its own generated output, typically by checking for consistency with a given context.

**Double-checking** (1 paper: [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf))
> The observable behavior of generating a subsequent solution to verify or re-evaluate a previously generated solution, often using the same reasoning strategy.

## Relationships

### Self-verification →
- **Iterative refinement** (behavioral indicator): *causes*, 1 paper
  > Incorporated with CSV, the model becomes capable of using code to verify answers, then reviewing and adjusting how it arrived at the solution if the verification result is False, aiming at obtaining the correct answer.
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > ...enables LLMs to self-correct their outputs through self-verification.
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Reliability** (construct): *causes*, 1 paper
  > Reviewer agent – Verifies and refines the initial answer to improve accuracy and reliability (Section 3)
  - [DocAgent: An Agentic Framework for Multi-Modal Long-Context Document Understanding](https://aclanthology.org/2025.emnlp-main.893.pdf)

### Associated with
- **Context faithfulness** (construct), 1 paper
  > Furthermore, AutoMix is designed with a dialogue-related or context-grounded reasoning setup in mind for effective self-verification, which does not include tasks like factual question-answering and commonsense reasoning. (Section 6)
  - [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf)
- **Calibration** (construct), 1 paper
  > "prior works have shown self-verification is not particularly effective for reasoning tasks and is often noisy and ill-calibrated"
  - [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf)
- **Table question answering** (behavioral indicator), 1 paper
  > Most LLM-based TableQA methods can be divided into three phases: question decomposition (Lewkowycz et al., 2022; Liu et al., 2022; Fu et al., 2022; Pasupat & Liang, 2015), sub-question TableQA reasoning and answer verification (Madaan et al., 2024; Ni et al., 2023).
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **Game of 24** (measurement instrument), 1 paper
  > It is particularly useful for problems where verification is significantly easier than solving the problem itself, e.g., the Game of 24 (Yao et al., 2024). (Section 2.2)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
- **Binary decision making** (behavioral indicator), 1 paper
  > A binary decision task, such as yes-no QA or answer verification, represents a major real-world scenario (Section 3)
  - [Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.503.pdf)
- **Self-awareness** (construct), 1 paper
  > “Self-awareness, i.e., the ability to assess and correct one’s generation”
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
- **Metacognition** (construct), 1 paper
  > Metacognition: This assesses prompts in explicitly guiding models to reason, self-monitor, and self-verify outputs to meet expectations and enhance reliability (e.b. Wang and Zhao (2024)).
  - [What Makes a Good Natural Language Prompt?](https://aclanthology.org/2025.acl-long.292.pdf)
- **Reasoning** (construct), 1 paper
  > “The core idea of ReVISE is to enable LLMs to verify their reasoning processes”
  - [ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf)
