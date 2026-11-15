# Vicuna-Bench
**Type:** Measurement instrument  
**Supporting papers:** 20  
**Also known as:** Vicuna Bench, Vicuna-bench, Vicuna bench, GPT-4 evaluating benchmark, Vicuna, Vicuna Eval, Vicuna Evaluation, VicunaEval  

## State of the Field

**What it is.** Across papers, the prevailing usage is a benchmark or evaluation set for instruction-following and conversational response quality, often described as drawing on user-shared conversations or diverse predefined prompts and judged with GPT-4. Several definitions specify 80 questions, while one paper describes an adapted single-rating version with 80 single-turn chat prompts and 320 responses, and another frames it as a scheme where GPT-4 compares two model responses on 80 questions. A smaller set of definitions describes it more broadly as open-ended text generation, short-text conversational tasks, or general LLM performance evaluation.

**What it is claimed to measure.** Papers mainly use it to measure instruction following: it is linked to five constructs and four behavioral indicators, with instruction following ability and instruction following the most recurrent targets. Other reported uses include text generation, coding ability, and multi-turn dialogue, with several additional linked targets also reported. Overall, the claims center on instruction following but extend to several adjacent capabilities.

**Space of uses.** Papers usually use it alongside MT-Bench, and they also pair it with AlpacaEval, WizardLM, Dolly Eval, and Self-Instruct or related instruction-evaluation sets. Papers commonly present it as one benchmark within a larger evaluation suite, and some use GPT-4-based judging or pairwise comparison against a reference model when scoring responses.

## Sources

**Vicuna Bench** (2 papers: [Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf), [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf))
> A benchmark for assessing LLM responses to user prompts, used to evaluate the correlation between evaluator models and human or GPT-4 scores.

**Vicuna-Bench** (3 papers: [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf), [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf))
> Chatbot benchmark using user-shared conversations evaluated by GPT-4 to assess model performance in open-ended dialogue.

**Vicuna-bench** (1 paper: [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf))
> A benchmark used to evaluate a model's instruction-following and conversational abilities, where model outputs are compared against a reference model (gpt-3.5-turbo) using GPT-4 as the judge.

**Vicuna bench** (1 paper: [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf))
> A benchmark used to evaluate the performance of LLMs on a variety of tasks.

**VicunaEval** (2 papers: [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf), [Adversarial Moment-Matching Distillation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbae8efcc23a0cb6d15a20f245514020-Paper-Conference.pdf))
> A benchmark dataset used to evaluate an LLM's performance and response quality on short-text, conversational tasks.

**GPT-4 evaluating benchmark** (1 paper: [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf))
> An evaluation protocol that uses the GPT-4 model to assess and compare the quality of responses from different instruction-following models across a set of 80 questions.

**Vicuna** (4 papers: [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf), [MiniLLM: Knowledge Distillation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/8ac015d409635f196f9e3e9dcfb9a94e-Paper-Conference.pdf), [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf), [Add-One-In: Incremental Sample Selection for Large Language Models via a Choice-Based Greedy Paradigm](https://aclanthology.org/2025.emnlp-main.270.pdf))
> Benchmark based on user-shared conversations to evaluate open-ended text generation quality and helpfulness of model responses.

**Vicuna Eval** (2 papers: [Self-Instructed Derived Prompt Generation Meets In-Context Learning: Unlocking New Potential of Black-Box LLMs](https://aclanthology.org/2025.acl-long.92.pdf), [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf))
> An instruction-following evaluation dataset used to assess the quality of model responses across diverse prompts.

**Vicuna Evaluation** (1 paper: [Beyond Logits: Aligning Feature Dynamics for Effective Knowledge Distillation](https://aclanthology.org/2025.acl-long.1125.pdf))
> Benchmark comprising 80 challenging questions designed to evaluate the Vicuna model's performance on complex instruction-following tasks.

## Relationships

### → Vicuna-Bench
- **Instruction following ability** (construct): *measured_by*, 4 papers
  > To rigorously evaluate the instruction-following capabilities of AI models, we utilized three widely used benchmarks: MT-bench, Vicuna-bench, and the WizardLM testset (Section 4.1).
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)
  - [Towards the Law of Capacity Gap in Distilling Language Models](https://aclanthology.org/2025.acl-long.1097.pdf)
  - [ToDi: Token-wise Distillation via Fine-Grained Divergence Control](https://aclanthology.org/2025.emnlp-main.409.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 3 papers
  > To evaluate the instruction-following ability, we employ the three most widely recognized benchmarks, including AlpacaEval (Li et al., 2023), MT-bench (Zheng et al., 2023) and Vicuna-bench (Chiang et al., 2023).
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
  - [Preference Consistency Matters: Enhancing Preference Learning in Language Models with Automated Self-Curation of Training Corpora](https://aclanthology.org/2025.naacl-long.606.pdf)
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 3 papers
  > “we employ a broad array of out-of-distribution benchmarks to conduct a more comprehensive evaluation of the model’s capabilities. This includes assessing ... open-ended generation (Vicuna (Chiang et al., 2023) and WizardLM (Xu et al., 2023))”
  - [Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf)
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **Evaluation ability** (construct): *measured_by*, 1 paper
  > Furthermore, measuring correlation with GPT-4 with 1222 customized score rubrics across four benchmarks (MT Bench, Vicuna Bench, Feedback Bench, Flask Eval) shows similar trends, bolstering PROMETHEUS’s capability as an evaluator LLM. (Abstract)
  - [Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > MT-bench and Vicuna-bench are designed to test the models' competencies in various complex cognitive tasks, including mathematics, reasoning, complex format handling, and writing
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **Multi-turn dialogue** (behavioral indicator): *measured_by*, 1 paper
  > MT-bench and Vicuna-bench are designed to test the models' competencies in various complex cognitive tasks, including mathematics, reasoning, complex format handling, and writing through both multi-turn and single-turn dialogues.
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 1 paper
  > MT-bench and Vicuna-bench are designed to test the models' competencies in various complex cognitive tasks, including mathematics, reasoning, complex format handling, and writing
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **Coding ability** (construct): *measured_by*, 1 paper
  > Figure 4 illustrates the Llama-2-7B-star_instruct's performance enhancements across nine metrics, with notable substantial improvements in math, coding and fermi problem-solving... Figure 4: Radar plot of detailed scores for Llama-2-7B-star_instrcut against the major baseline on different subtasks of (a) Vicuna-Bench and (b) MT-Bench.
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **General ability** (construct): *measured_by*, 1 paper
  > To evaluate the LLM’s general performance in short-text tasks, we measure its WinRate against the text-davinci-003 model using 100 queries from AlpacaEval and 80 queries from VicunaEval. (Section 5.1)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
