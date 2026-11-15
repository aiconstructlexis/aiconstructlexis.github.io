# Evaluation ability
**Type:** Construct  
**Supporting papers:** 13  
**Also known as:** Evaluation capability, Fine-grained evaluation capability, Judging ability, Text evaluation ability, Judgment capability, Judge ability, LLM-as-a-judge ability  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats evaluation ability as a latent capability of a model or LLM to accurately assess the quality or correctness of generated outputs. Most formulations focus on judging model responses or text, sometimes including intermediate reasoning steps or full trajectories, and they anchor accuracy against human judgments, score rubrics and reference answers, or adherence to instruction constraints. Smaller variants narrow it to fine-grained evaluation with user-defined criteria, coding-solution judgment, multimodal comparison that matches human voting, or judging that guides reranking, beam search, and refinement.

**Space of facets.** Papers mostly use a cluster of near-synonymous labels, including evaluation capability, judging ability, text evaluation ability, judgment capability, and judge ability, for the same underlying judging capacity. The clearest subtype is fine-grained evaluation capability, explicitly contrasted with coarse or generic preferences and tied to user-defined score rubrics and reference materials. A smaller line of work argues that reranking, beam search, and refinement are all tied to a single underlying fundamental judging capability, while another paper treats judge ability as a general ability of LLMs.

**Space of measurement.** Operationalization is benchmark-driven: papers link the construct to 7 measurement instruments and no behavioral indicators. The most frequently linked instruments are LLMBar, CommonGen, Feedback Bench, JudgeBench, and MT-Bench, plus 2 other instruments. These are benchmark or dataset style tasks that operationalize the construct through judging outputs: LLMBar targets instruction-following assessment, CommonGen directly compares generation and evaluation abilities, JudgeBench evaluates judges on challenging response pairs, and some benchmark groups use customized score rubrics together with correlation to GPT-4 or comparison to human judgments. These operationalizations mostly match the dominant definitions, but they instantiate the construct in narrower settings such as instruction-following, coding, or text generation comparison.

**Links.** Beyond measurement, papers link evaluation ability to 2 other constructs. One paper reports that it is related to generative ability, stating that language models find it simpler to evaluate a sentence than to generate it. Another paper claims a causal relationship from evaluation ability to general ability, describing judge-task training as enhancing the model's general capabilities.

## Sources

**Evaluation capability** (4 papers: [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf), [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf), [Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf), [StackEval: Benchmarking LLMs in Coding Assistance](https://proceedings.neurips.cc/paper_files/paper/2024/file/4126a607bbe2836cb6ca0eb45b75618b-Paper-Datasets_and_Benchmarks_Track.pdf))
> The model's latent ability to accurately assess the quality or correctness of a generated trajectory or its intermediate steps.

**Fine-grained evaluation capability** (1 paper: [Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf))
> The ability to judge text quality using detailed, user-defined criteria rather than only coarse or generic preferences.

**Judging ability** (2 papers: [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25af/zhou25af.pdf), [GenAI Arena: An Open Evaluation Platform for Generative Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/92249f9233286e437f808fa535d88b26-Paper-Datasets_and_Benchmarks_Track.pdf))
> The latent capacity of an LLM to accurately assess the quality of model-generated responses, particularly in guiding test-time computation through reranking, beam search, or refinement.

**Text evaluation ability** (1 paper: [CausalStock: Deep End-to-end Causal Discovery for News-driven Multi-stock Movement Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/54d689d58fe54c92aee2d732fc49fca8-Paper-Conference.pdf))
> The latent capability of an LLM to accurately assess and score text along multiple specified dimensions.

**Judgment capability** (1 paper: [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf))
> The latent ability of a model to assess whether a given response accurately adheres to the constraints of an instruction.

**Judge ability** (1 paper: [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf))
> The latent capability of a large language model to evaluate responses, provide accurate preference signals, and render critical judgments.

## Relationships

### Evaluation ability →
- **LLMBar** (measurement instrument): *measured_by*, 2 papers
  > For assessing the refiner’s judgment capability, we turn to LLMBar (Zeng et al., 2023), a dataset designed to measure the assessment ability of LLMs in the context of instruction-following tasks. (Section 3.2)
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
  - [Evaluating Large Language Models at Evaluating Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/afc8b034823271816d14f7c1aefe1dff-Paper-Conference.pdf)
- **CommonGen** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments to compare the text generation and evaluation abilities of LLMs using the CommonGen (Lin et al., 2020) task... (Section 4.1)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > Furthermore, measuring correlation with GPT-4 with 1222 customized score rubrics across four benchmarks (MT Bench, Vicuna Bench, Feedback Bench, Flask Eval) shows similar trends, bolstering PROMETHEUS’s capability as an evaluator LLM. (Abstract)
  - [Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf)
- **Vicuna-Bench** (measurement instrument): *measured_by*, 1 paper
  > Furthermore, measuring correlation with GPT-4 with 1222 customized score rubrics across four benchmarks (MT Bench, Vicuna Bench, Feedback Bench, Flask Eval) shows similar trends, bolstering PROMETHEUS’s capability as an evaluator LLM. (Abstract)
  - [Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf)
- **Feedback Bench** (measurement instrument): *measured_by*, 1 paper
  > Furthermore, measuring correlation with GPT-4 with 1222 customized score rubrics across four benchmarks (MT Bench, Vicuna Bench, Feedback Bench, Flask Eval) shows similar trends, bolstering PROMETHEUS’s capability as an evaluator LLM. (Abstract)
  - [Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf)
- **General ability** (construct): *causes*, 1 paper
  > Furthermore, our training method enhances the general capabilities of the model by constructing complicated judge task... (Abstract)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **RewardBench** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the judgment capabilities of our model, we conduct experiments on RewardBench (Lambert et al., 2024). (Section 1)
  - [Improve LLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **JudgeBench** (measurement instrument): *measured_by*, 1 paper
  > JudgeBench is a recent benchmark that evaluates LLM-based judges on challenging response pairs spanning knowledge, reasoning, math, and coding. (Section 3)
  - [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf)

### Associated with
- **Generative ability** (construct), 1 paper
  > We disclose that it is simpler for language models to evaluate a sentence than to generate it, even for small language models. (Section 1)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
