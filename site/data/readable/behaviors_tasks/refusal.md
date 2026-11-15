# Refusal
**Type:** Behavioral indicator  
**Supporting papers:** 126  
**Also known as:** Evasive response generation, Harmful query rejection, Unsafe prompt rejection, Toxic prompt rejection, Avoidance, Harmful content rejection, Refusal to answer, Refusal behavior, Refusal generation, Faithful reasoning, Punting, Answer refusal, Response refusal, Refusal to respond, Abstention, Rejecting request  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats refusal as abstaining from answering harmful, unsafe, malicious, toxic, unethical, or policy-violating requests, often through explicit rejection language such as "I cannot fulfill your request" or "I'm sorry, but I can't assist with that request." Most definitions count an explicit decline as refusal, while some also include generic or off-task replies, answers to a different question, returning an error message, or redirecting toward safer alternatives. A smaller line of work extends the behavior beyond harmful requests, using refusal for knowledge-limit statements, unsupported functionality, missing or contradictory information, uncertainty, selecting a "not sure" option, or declining to choose from invalid options.

**Variants.** Papers study refusal across safety prompts, blocklisted content, hate speech, moral dilemmas, politically sensitive questions, medical uncertainty, knowledge-boundary questions, and function-calling requests. The dominant variants are still direct rejections of harmful or unsafe inputs, but several papers use nearby labels, such as abstention, avoidance, evasive responses, punting, and rejecting a request. One definition explicitly separates avoidance from refusal by describing it as a related response that does not directly answer the input.

**Space of elicitation and scores.** Papers link refusal to 5 measurement instruments. The most direct measures are CAA, which includes Refusal as one of several concepts, StrongREJECT, which measures refusal rate on harmful prompts and can use a GPT-4o judge to decide whether the model answered, and AdvBench, a high-risk query set used to track refusal rate; Alpaca instruction dataset and Databricks Dolly-15k appear in related dataset uses for constructing refusal or compliance prefixes or refusal-target outputs. Across studies, scoring is usually binary refusal behavior or refusal rate, with some papers also using rejection tokens, phrase cues such as "I cannot," or classifier-based refusal filtering.

**What it is taken as evidence of.** Papers connect refusal to 10 constructs, and they do not center it on one construct alone. The most recurrent links are to Helpfulness, Honesty, Safety alignment, Alignment, and Commonsense reasoning, with 5 other constructs also linked; several papers claim causal relationships from Safety alignment and Alignment to Refusal, while others claim causal relationships from Refusal to Helpfulness and Commonsense reasoning, including evidence that refusing to answer "renders the response quite unhelpful." Honesty is described as related to Refusal rather than as its cause, so papers use the behavior both as an outcome of alignment-oriented constructs and as a behavior associated with downstream qualities.

## Sources

**Refusal** (11 papers: [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf), [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf), [Evaluating Copyright Takedown Methods for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/faed4276b52ef762879db4142655c699-Paper-Datasets_and_Benchmarks_Track.pdf), [Language Model Alignment in Multilingual Trolley Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f32be3e112e151707cb12528bdfa7d5-Paper-Conference.pdf), [SynthDetoxM: Modern LLMs are Few-Shot Parallel Detoxification Data Annotators](https://aclanthology.org/2025.naacl-long.294.pdf), [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf), [RAG LLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.281.pdf), [Foot-In-The-Door: A Multi-turn Jailbreak for LLMs](https://aclanthology.org/2025.emnlp-main.100.pdf), [Differentially Private Steering for Large Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45326c2df19fee16fc1ebc44941fea8e-Paper-Conference.pdf), [Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts](https://aclanthology.org/2025.acl-long.185.pdf), [CASE-Bench: Context-Aware SafEty Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25ab/sun25ab.pdf))
> The model's observable behavior of abstaining from responding to a malicious instruction, typically by stating it cannot assist with harmful requests.

**Evasive response generation** (1 paper: [A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2025/file/084cf2b3d73abafa1705336a0e9ebb1c-Paper-Conference.pdf))
> The model's behavior of avoiding a direct answer to a prompt, often as a safety mechanism, which can sometimes be an undesirable side effect of alignment.

**Harmful query rejection** (1 paper: [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf))
> The observable behavior of a model refusing to answer a harmful or malicious query, often by outputting a canned refusal phrase.

**Unsafe prompt rejection** (1 paper: [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf))
> The model declining or refusing to answer requests that are dangerous, unethical, or violate safety policies.

**Toxic prompt rejection** (1 paper: [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf))
> The observable behavior where a model correctly refuses to respond to a harmful or dangerous user request.

**Harmful content rejection** (1 paper: [HPS: Hard Preference Sampling for Human Preference Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25c/zou25c.pdf))
> The observable behavior of a model refusing to generate outputs that are inappropriate, offensive, or malicious.

**Avoidance** (1 paper: [Position: Political Neutrality in AI Is Impossible — But Here Is How to Approximate It](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fisher25a/fisher25a.pdf))
> The observable behavior of providing a related but non-responsive answer to a politically sensitive query, without directly addressing the input.

**Refusal to answer** (10 papers: [Perception of Knowledge Boundary for Large Language Models through Semi-open-ended Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/a1e0d6fa0c30b7d4f75dd9c7ed6189f2-Paper-Conference.pdf), [Injecting Universal Jailbreak Backdoors into LLMs in Minutes](https://proceedings.iclr.cc/paper_files/paper/2025/file/1160e7f31d0a74abbbe1bbf7924b949c-Paper-Conference.pdf), [Arabic Dataset for LLM Safeguard Evaluation](https://aclanthology.org/2025.naacl-long.285.pdf), [PerCul: A Story-Driven Cultural Evaluation of LLMs in Persian](https://aclanthology.org/2025.naacl-long.631.pdf), [LLMs Are Not Intelligent Thinkers: Introducing Mathematical Topic Tree Benchmark for Comprehensive Evaluation of LLMs](https://aclanthology.org/2025.naacl-long.161.pdf), [Wait, that's not an option: LLMs Robustness with Incorrect Multiple-Choice Options](https://aclanthology.org/2025.acl-long.75.pdf), [REINFORCE Adversarial Attacks on Large Language Models: An Adaptive, Distributional, and Semantic Objective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/geisler25a/geisler25a.pdf), [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143.pdf), [Human Feedback is not Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2024/file/f719b8ca81221f380836e573d479c223-Paper-Conference.pdf), [Large Language Models as Automated Aligners for benchmarking Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf))
> The action of explicitly declining to provide an answer to a question, often by stating an inability to do so or citing knowledge limitations.

**Refusal behavior** (4 papers: [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf), [Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations](https://aclanthology.org/2025.emnlp-main.145.pdf), [On the Learnability of Watermarks for Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a86d17b6cd70366d56ab48d2a05a4df1-Paper-Conference.pdf), [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf))
> The observable act of a model declining to respond to a harmful or unsafe prompt, indicating intact safety mechanisms.

**Refusal generation** (2 papers: [Improving LLM Safety Alignment with Dual-Objective Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25c/zhao25c.pdf), [AEGIS2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails](https://aclanthology.org/2025.naacl-long.306.pdf))
> Producing responses that decline to answer harmful queries, often using phrases like 'Sorry, I can’t provide that information'.

**Faithful reasoning** (1 paper: [CMedCalc-Bench: A Fine-Grained Benchmark for Chinese Medical Calculations in LLM](https://aclanthology.org/2025.emnlp-main.1302.pdf))
> The latent tendency of a model to abstain from answering when faced with missing or contradictory input information, reflecting clinical safety awareness.

**Punting** (1 paper: [MetaFaith: Faithful Natural Language Uncertainty Expression in LLMs](https://aclanthology.org/2025.emnlp-main.1505.pdf))
> The model's tendency to avoid answering a question altogether, often as a result of over-cautiousness induced by uncertainty prompts.

**Answer refusal** (1 paper: [JMMMU: A Japanese Massive Multi-discipline Multimodal Understanding Benchmark for Culture-aware Evaluation](https://aclanthology.org/2025.naacl-long.43.pdf))
> The model's observable action of declining to respond to a user's query, often for safety, privacy, or capability-limitation reasons.

**Response refusal** (2 papers: [Decoding Hate: Exploring Language Models' Reactions to Hate Speech](https://aclanthology.org/2025.naacl-long.45.pdf), [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf))
> Opting not to engage with a hate speech prompt, either by declining to answer or returning an error message.

**Refusal to respond** (1 paper: [HISTOIRESMORALES: A French Dataset for Assessing Moral Alignment](https://aclanthology.org/2025.naacl-long.131.pdf))
> An observable behavior where the model declines to provide an answer to a prompt, often for safety or capability reasons.

**Abstention** (1 paper: [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.353.pdf))
> The observable behavior of a model refusing to provide a direct answer to a user's query, often accompanied by a statement of inability or unwillingness to respond.

**Rejecting request** (1 paper: [CONFETTI: Conversational Function-Calling Evaluation Through Turn-Level Interactions](https://aclanthology.org/2025.acl-long.394.pdf))
> Producing responses that decline to perform a user request, typically due to unsupported functionality or policy constraints.

## Relationships

### Refusal →
- **Helpfulness** (construct): *causes*, 3 papers
  > ...a model that refuses to answer, while technically considered harmless, renders the response quite unhelpful [16].
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
- **Commonsense reasoning** (construct): *causes*, 1 paper
  > The bottom radar maps show that they fall behind in knowledge, information extraction, and commonsense reasoning compared to GPT-4o, partially because of this refusal behavior.
  - [MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/461f1fd5f92e5ca95764a88304dc39f7-Paper-Conference.pdf)
- **CAA** (measurement instrument): *measured_by*, 1 paper
  > Seven concepts, relevant to the helpful, honest, and harmless of LLMs, are included from CAA dataset (Rimsky et al., 2024): AI Coordination (AIC., for short), Corrigibility (CORR.), Hallucination (HALLU.), Myopic Reward (MR.), Survival Instinct (SI.), Sycophancy (SYC.), and Refusal (REF.).
  - [Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts](https://aclanthology.org/2025.acl-long.185.pdf)
- **StrongREJECT** (measurement instrument): *measured_by*, 1 paper
  > For generation, we use data from the StrongREJECT task (Souly et al., 2024). In particular, we measure the refusal rate of the model on harmful prompts, with the attack considered to have succeeded if a GPT-4o judge (gpt-4o-2024-05-13) considers the model to have answered the question. (Section 3)
  - [Scaling Trends in Language Model Robustness](https://raw.githubusercontent.com/mlresearch/v267/main/assets/howe25a/howe25a.pdf)
- **Fairness** (construct): *causes*, 1 paper
  > Refusal effectively avoids generating controversial or biased output, ensuring fairness and safety. (Section 3.1)
  - [Position: Political Neutrality in AI Is Impossible — But Here Is How to Approximate It](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fisher25a/fisher25a.pdf)
- **AdvBench** (measurement instrument): *measured_by*, 1 paper
  > on a set of 520 high-risk queries from AdvBench (Zou et al., 2023), all 9 LRMs models... consistently exhibited a significant drop in overall refusal rate under first-person prompting (Section 3.1)
  - [Path Drift in Large Reasoning Models: How First-Person Commitments Override Safety](https://aclanthology.org/2025.emnlp-main.990.pdf)

### → Refusal
- **Safety alignment** (construct): *causes*, 2 papers
  > In response, researchers have developed several methods to enhance LLM safety, known as safety alignment, including supervised fine-tuning (SFT) (Ouyang et al., 2022) and reinforcement learning from human feedback (RLHF) (Bai et al., 2022; Dai et al., 2024). As a result of these advancements, pre-trained LLMs like GPT-4 (OpenAI, 2023) and Llama (Touvron et al., 2023b) have become more adept at rejecting unsafe prompts.
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
  - [Injecting Universal Jailbreak Backdoors into LLMs in Minutes](https://proceedings.iclr.cc/paper_files/paper/2025/file/1160e7f31d0a74abbbe1bbf7924b949c-Paper-Conference.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > aligned LLMs readily refuse to answer many inappropriate prompts where the factual answer, e.g., could cause harm. (Section 1)
  - [REINFORCE Adversarial Attacks on Large Language Models: An Adaptive, Distributional, and Semantic Objective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/geisler25a/geisler25a.pdf)

### Associated with
- **Honesty** (construct), 2 papers
  > In this paper, we argue for the importance of alignment for honesty, ensuring that LLMs proactively refuse to answer questions when they lack knowledge, while still not being overly conservative. (Abstract)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
  - [Refine Knowledge of Large Language Models via Adaptive Contrastive Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbd010aed9a0d7f56144bd5dcaa95b9e-Paper-Conference.pdf)
- **Human preference alignment** (construct), 1 paper
  > “The ideal models are supposed to refuse to answer questions that violate human values and meanwhile provide appropriate justifications for rejection.”
  - [Large Language Models as Automated Aligners for benchmarking Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d591ef4c631b33ac4e08dd88f1ee1dff-Paper-Conference.pdf)
- **Harmlessness** (construct), 1 paper
  > ...a model that refuses to answer, while technically considered harmless, renders the response quite unhelpful [16].
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
- **Preference bias** (construct), 1 paper
  > In this task, we expect the model to refuse to give responses that may imply its preference towards any topic, so we use Refusal Rate (RR) as the metric.
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **Safety** (construct), 1 paper
  > These insights highlight that LLM safety relies on maximizing the probability of generating rejection tokens in response to harmful queries. (Section 2)
  - [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf)
- **Safe response generation** (behavioral indicator), 1 paper
  > I am sorry, but I cannot fulfill your request… is used as a safe response under the good bot goal, indicating refusal to generate harmful content. (Figure 1 and Section 4.2)
  - [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf)
- **Hallucination detection** (behavioral indicator), 1 paper
  > The hallucination detection task aims to test the model’s ability to decline answering questions that are not mentioned in the given context.
  - [LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs – No Silver Bullet for LC or RAG Routing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dv/li25dv.pdf)
- **Databricks Dolly-15k** (measurement instrument), 1 paper
  > For AutoPoison-refusal, we first generate poisoned datasets by replacing the generation targets in GPT-4-LLM and Databricks-Dolly-15k with two refusal outputs... (Section A.1)
  - [LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect](https://proceedings.neurips.cc/paper_files/paper/2024/file/064f6bcd7d3c72fb187bfca35ba2bfd4-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurement instrument), 1 paper
  > “For the refusal behavior vector, we randomly select 100 instructions from the Alpaca dataset ... and append them with 100 typical refusal or compliance behavior prefixes as responses”
  - [Programming Refusal with Conditional Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf)
