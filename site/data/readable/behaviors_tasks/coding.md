# Coding
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Coding assistance  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats coding as responding to prompts that require code-related solutions or programming assistance. Definitions mostly converge on writing, debugging, and completing code, often framed as assistance to the user, while one related formulation expands the scope to writing, synthesizing, documenting, debugging, and reviewing code across programming languages. As one paper puts it, the task can involve "writing, debugging, or completing functional computer code, such as implementing a server" (Position: AI Should Not Be An Imitation Game: Centaur Evaluations).

**Variants.** Papers use nearby names such as coding assistance, and they study concrete instances such as implementing a functional HTTP server, Python programming problems, and long-context coding applications. Separate papers report that code generation and code debugging are related to coding, and one paper relates coding to instruction following in structured task settings. Coding also appears as a broader task category alongside domains such as creative writing and few-shot learning.

**Space of elicitation and scores.** Papers measure coding with 8 linked instruments. Linked instruments include Chatbot Arena, CodeContests, EvalPlus, HumanEval+, and LongBench-E. These are described as benchmarks or datasets that cover coding either directly or alongside other skills, and one linked benchmark is described as Python programming problems designed to be solvable by entry-level programmers.

**What it is taken as evidence of.** No paper explicitly links coding to a construct as something this behavior evidences. The material therefore does not specify a named construct that coding is taken to reflect.

## Sources

**Coding** (2 papers: [Instruct-SkillMix: A Powerful Pipeline for LLM Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf), [Position: AI Should Not Be An Imitation Game: Centaur Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/haupt25a/haupt25a.pdf))
> Responding to prompts that require code-related solutions or programming assistance.

**Coding assistance** (1 paper: [Position: AI Scaling: From Up to Down and Out](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25fh/wang25fh.pdf))
> The task of helping users write, debug, or complete computer code.

## Relationships

### Coding →
- **HumanEval+** (measurement instrument): *measured_by*, 1 paper
  > We evaluate models on 11 different benchmarks, covering skills such as ... coding (HumanEval+ [6, 32], MBPP+ [2, 32]) (Section 2.2).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **EvalPlus** (measurement instrument): *measured_by*, 1 paper
  > We evaluate models on 11 different benchmarks, covering skills such as ... coding (HumanEval+ [6, 32], MBPP+ [2, 32]) (Section 2.2).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **MBXP** (measurement instrument): *measured_by*, 1 paper
  > "open-web-math (Paster et al., 2023) and MBXP (Athiwaratkun et al., 2023). They address different capabilities of LLMs: reasoning and coding, respectively"
  - [PhyloLM: Inferring the Phylogeny of Large Language Models and Predicting their Performances in Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e28663712d5a3429a98918c3058f7b-Paper-Conference.pdf)
- **LongBench-E** (measurement instrument): *measured_by*, 1 paper
  > we further test LongMamba on the LongBench-E dataset (Bai et al., 2023), which covers 13 long-context applications, such as coding and few-shot learning. (Section 6.2)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > The benchmark [MTBench] covers diverse tasks such as reasoning, coding, mathematics, and other skill-based domains.
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **MBPP** (measurement instrument): *measured_by*, 1 paper
  > In the coding category, we assess using MBPP (Austin et al., 2021), a benchmark consisting of Python programming problems designed to be solvable by entry-level programmers. (Section 4.1).
  - [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf)
- **CodeContests** (measurement instrument): *measured_by*, 1 paper
  > For our analysis, we look at seven datasets spanning instruction-following, reasoning, mathematics, and coding: MT-Bench (Zheng et al., 2023), AlpacaEval 2.0 (Li et al., 2023), Arena Hard Auto (Li et al., 2024b), MixEval (Ni et al., 2024), MixEval-Hard, MATH (Hendrycks et al., 2021), and CodeContests (Li et al., 2022). (Section 3.2)
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Chatbot Arena** (measurement instrument): *measured_by*, 1 paper
  > "The most popular one is the Chatbot Arena ... which contains over one million user queries and evaluates models in various tasks such as code, math, and multilingual understanding"
  - [Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf)

### Associated with
- **Code generation** (behavioral indicator), 1 paper
  > Coding: The ability to write, synthesize, document, debug, and review code across various programming languages. (Section 2.1)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Code debugging** (behavioral indicator), 1 paper
  > Coding: The ability to write, synthesize, document, debug, and review code across various programming languages. (Section 2.1)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > Gemma-7B-Instruct performs better in structured tasks like reasoning and coding, where precise instruction-following is crucial (Section 3.1)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
